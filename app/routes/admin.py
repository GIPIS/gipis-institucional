import os
import re
import unicodedata
from functools import wraps

from flask import Blueprint, render_template, redirect, url_for, flash, request, abort, current_app
from flask_login import login_required, current_user

from app import db
from app.models import Member, Category, ResearchSection, ResearchItem, Partner, News, NewsImage, NewsAttachment
from app.news_meta import (NEWS_CATEGORIES, NEWS_IMAGE_EXTENSIONS,
                           NEWS_ATTACHMENT_EXTENSIONS, is_valid_category)
from werkzeug.utils import secure_filename

bp = Blueprint('admin', __name__, url_prefix='/auth/admin')


def admin_required(f):
    @wraps(f)
    @login_required
    def wrapped(*args, **kwargs):
        if not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return wrapped


def slugify(name):
    """Generar slug único a partir del nombre (ej: 'Juan Pérez' -> 'jperez')"""
    normalized = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')
    parts = [p for p in re.sub(r'[^a-z ]', '', normalized.lower()).split() if p]
    if not parts:
        base = 'miembro'
    elif len(parts) == 1:
        base = parts[0]
    else:
        base = parts[0][0] + parts[-1]

    slug = base
    counter = 2
    while Member.query.filter_by(slug=slug).first():
        slug = f"{base}{counter}"
        counter += 1
    return slug


# ==========================================
# Miembros
# ==========================================

@bp.route('/members', methods=['GET', 'POST'])
@admin_required
def members():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        category_id = request.form.get('category_id', type=int)

        if not name or not email or not password:
            flash('Nombre, email y contraseña inicial son obligatorios.', 'error')
            return redirect(url_for('admin.members'))

        if not category_id:
            flash('Elegí una categoría: los miembros sin categoría no aparecen '
                  'en la página del grupo.', 'error')
            return redirect(url_for('admin.members'))

        if Member.query.filter_by(email=email).first():
            flash(f'Ya existe un miembro con el email {email}.', 'error')
            return redirect(url_for('admin.members'))

        member = Member(
            slug=slugify(name),
            name=name,
            email=email,
            degree=request.form.get('degree', '').strip() or None,
            position=request.form.get('position', '').strip() or None,
            role=request.form.get('role', 'member'),
            category_id=category_id,
            order=request.form.get('order', type=int) or 0,
        )
        member.set_password(password)
        db.session.add(member)
        db.session.commit()
        flash(f'Miembro {name} creado. Puede ingresar con {email}.', 'success')
        return redirect(url_for('admin.members'))

    all_members = Member.query.order_by(Member.order, Member.name).all()
    categories = Category.query.order_by(Category.order).all()
    return render_template('admin/members.xhtml', members=all_members, categories=categories)


@bp.route('/members/<int:member_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_member(member_id):
    """Editar el perfil completo de un integrante (mismo formulario que
    usa cada miembro para su perfil, más los datos administrativos)."""
    from app.routes.auth import apply_profile_form, _login_email_taken
    member = Member.query.get_or_404(member_id)
    categories = Category.query.order_by(Category.order).all()

    if request.method == 'POST':
        error = None

        email = request.form.get('email', '').strip().lower()
        if not email:
            error = 'El email de acceso es obligatorio.'
        elif email != (member.email or '').lower() and _login_email_taken(member, email):
            error = f'Ya existe un miembro con el email {email}.'

        category_id = request.form.get('category_id', type=int)
        category = Category.query.get(category_id) if category_id else None
        if not error and not category:
            error = ('Elegí una categoría: los miembros sin categoría no aparecen '
                     'en la página del grupo.')

        if not error:
            member.email = email
            member.category_id = category.id
            member.order = request.form.get('order', type=int) or 0
            error = apply_profile_form(member, request.form, request.files)

        if error:
            db.session.rollback()
            flash(error, 'error')
            return redirect(url_for('admin.edit_member', member_id=member.id))

        db.session.commit()
        flash(f'Perfil de {member.name} actualizado.', 'success')
        return redirect(url_for('admin.members'))

    return render_template('auth/edit_profile.xhtml', member=member,
                           admin_mode=True, categories=categories,
                           form_action=url_for('admin.edit_member', member_id=member.id),
                           back_url=url_for('admin.members'))


@bp.route('/members/<int:member_id>/role', methods=['POST'])
@admin_required
def toggle_role(member_id):
    member = Member.query.get_or_404(member_id)
    if member.id == current_user.id:
        flash('No podés cambiar tu propio rol.', 'error')
    else:
        member.role = 'member' if member.is_admin else 'admin'
        db.session.commit()
        flash(f'{member.name} ahora es {"administrador" if member.is_admin else "miembro"}.', 'success')
    return redirect(url_for('admin.members'))


@bp.route('/members/<int:member_id>/category', methods=['POST'])
@admin_required
def change_category(member_id):
    member = Member.query.get_or_404(member_id)
    category = Category.query.get(request.form.get('category_id', type=int))
    if not category:
        flash('Categoría inválida.', 'error')
    else:
        member.category_id = category.id
        db.session.commit()
        flash(f'{member.name} movido a "{category.name}".', 'success')
    return redirect(url_for('admin.members'))


@bp.route('/members/<int:member_id>/password', methods=['POST'])
@admin_required
def reset_password(member_id):
    """Generar una contraseña temporal para un miembro"""
    import secrets
    member = Member.query.get_or_404(member_id)
    temp_password = secrets.token_urlsafe(6)
    member.set_password(temp_password)
    db.session.commit()
    flash(f'Contraseña temporal de {member.name}: {temp_password} — '
          'compartila de forma segura; puede cambiarla desde su perfil.', 'success')
    return redirect(url_for('admin.members'))


@bp.route('/members/<int:member_id>/active', methods=['POST'])
@admin_required
def toggle_active(member_id):
    member = Member.query.get_or_404(member_id)
    if member.id == current_user.id:
        flash('No podés desactivar tu propia cuenta.', 'error')
    else:
        member.is_active = not member.is_active
        db.session.commit()
        flash(f'{member.name} {"activado" if member.is_active else "desactivado"}.', 'success')
    return redirect(url_for('admin.members'))


# ==========================================
# Investigación (secciones e items)
# ==========================================

@bp.route('/research')
@admin_required
def research():
    sections = ResearchSection.query.order_by(ResearchSection.order).all()
    return render_template('admin/research.xhtml', sections=sections)


@bp.route('/research/sections', methods=['POST'])
@admin_required
def add_section():
    title = request.form.get('title', '').strip()
    if not title:
        flash('El título de la sección es obligatorio.', 'error')
        return redirect(url_for('admin.research'))

    slug_base = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-') or 'seccion'
    slug = slug_base
    counter = 2
    while ResearchSection.query.filter_by(slug=slug).first():
        slug = f"{slug_base}-{counter}"
        counter += 1

    max_order = db.session.query(db.func.max(ResearchSection.order)).scalar() or 0
    db.session.add(ResearchSection(slug=slug, title=title, order=max_order + 1))
    db.session.commit()
    flash(f'Sección "{title}" creada.', 'success')
    return redirect(url_for('admin.research'))


@bp.route('/research/items', methods=['POST'])
@admin_required
def add_item():
    title = request.form.get('title', '').strip()
    section_id = request.form.get('section_id', type=int)
    if not title or not section_id:
        flash('Título y sección son obligatorios.', 'error')
        return redirect(url_for('admin.research'))

    db.session.add(ResearchItem(
        slug=_item_slug(title),
        title=title,
        authors=request.form.get('authors', '').strip() or None,
        year=request.form.get('year', '').strip() or None,
        abstract=request.form.get('abstract', '').strip() or None,
        section_id=section_id,
    ))
    db.session.commit()
    flash('Ítem agregado.', 'success')
    return redirect(url_for('admin.research'))


@bp.route('/research/items/<int:item_id>/edit', methods=['POST'])
@admin_required
def edit_item(item_id):
    item = ResearchItem.query.get_or_404(item_id)
    item.title = request.form.get('title', item.title).strip() or item.title
    item.authors = request.form.get('authors', '').strip() or None
    item.year = request.form.get('year', '').strip() or None
    item.abstract = request.form.get('abstract', '').strip() or None
    section_id = request.form.get('section_id', type=int)
    if section_id:
        item.section_id = section_id
    db.session.commit()
    flash('Ítem actualizado.', 'success')
    return redirect(url_for('admin.research'))


@bp.route('/research/items/<int:item_id>/delete', methods=['POST'])
@admin_required
def delete_item(item_id):
    item = ResearchItem.query.get_or_404(item_id)
    # Desvincular producción personal que apunte a este ítem
    from app.models import MemberWork
    MemberWork.query.filter_by(shared_item_id=item.id).update({'shared_item_id': None})
    db.session.delete(item)
    db.session.commit()
    flash('Ítem eliminado.', 'success')
    return redirect(url_for('admin.research'))


def _item_slug(title):
    slug_base = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')[:40] or 'item'
    slug = slug_base
    counter = 2
    while ResearchItem.query.filter_by(slug=slug).first():
        slug = f"{slug_base}-{counter}"
        counter += 1
    return slug


# ==========================================
# Red de Colaboración
# ==========================================

PARTNER_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'svg'}


def _partner_upload_folder():
    folder = os.path.join(current_app.static_folder, 'img', 'partners')
    os.makedirs(folder, exist_ok=True)
    return folder


def _save_partner_image(partner):
    """Guardar el logo subido (si hay); devuelve True si hubo error de formato."""
    image = request.files.get('image')
    if not image or not image.filename:
        return False
    ext = image.filename.rsplit('.', 1)[-1].lower()
    if ext not in PARTNER_IMAGE_EXTENSIONS:
        flash('Formato de imagen no permitido. Usá PNG, JPG, WebP o SVG.', 'error')
        return True
    _delete_partner_image(partner)
    filename = f"{partner.id}.{ext}"
    image.save(os.path.join(_partner_upload_folder(), filename))
    partner.image = f"partners/{filename}"
    return False


def _delete_partner_image(partner):
    if partner.image:
        path = os.path.join(current_app.static_folder, 'img', partner.image)
        if os.path.exists(path):
            os.remove(path)
        partner.image = None


@bp.route('/partners', methods=['GET', 'POST'])
@admin_required
def partners():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        if not name:
            flash('El nombre de la organización es obligatorio.', 'error')
            return redirect(url_for('admin.partners'))

        max_order = db.session.query(db.func.max(Partner.order)).scalar() or 0
        partner = Partner(
            name=name,
            url=request.form.get('url', '').strip() or None,
            order=max_order + 1,
        )
        db.session.add(partner)
        db.session.flush()  # asigna id para nombrar el archivo del logo
        if _save_partner_image(partner):
            db.session.rollback()
            return redirect(url_for('admin.partners'))
        db.session.commit()
        flash(f'"{name}" agregada a la Red de Colaboración.', 'success')
        return redirect(url_for('admin.partners'))

    all_partners = Partner.query.order_by(Partner.order).all()
    return render_template('admin/partners.xhtml', partners=all_partners)


# ==========================================
# Novedades
# ==========================================

def _news_folder(news_item, *parts):
    """Carpeta de archivos de una novedad: static/img/news/<slug>/[...]."""
    folder = os.path.join(current_app.static_folder, 'img', 'news', news_item.slug, *parts)
    os.makedirs(folder, exist_ok=True)
    return folder


def _news_slug(title):
    normalized = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode('ascii')
    slug_base = re.sub(r'[^a-z0-9]+', '-', normalized.lower()).strip('-')[:60] or 'novedad'
    slug = slug_base
    counter = 2
    while News.query.filter_by(slug=slug).first():
        slug = f"{slug_base}-{counter}"
        counter += 1
    return slug


def _news_content_html(raw):
    """Texto plano → párrafos HTML (novedad.xhtml renderiza content|safe).
    Si el texto ya trae etiquetas HTML se guarda tal cual. Las marcas
    [foto N] quedan en el texto y se resuelven al mostrar la novedad."""
    raw = (raw or '').strip()
    if not raw or '<' in raw:
        return raw or None
    from markupsafe import escape
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', raw) if p.strip()]
    return '\n'.join(
        '<p>' + str(escape(p)).replace('\n', '<br/>') + '</p>' for p in paragraphs
    )


def _news_content_text(content):
    """Inverso de _news_content_html para editar en el textarea: párrafos
    simples vuelven a texto plano; HTML más complejo se muestra tal cual."""
    if not content:
        return ''
    text = re.sub(r'<br\s*/?>', '\n', content)
    text = re.sub(r'</p>\s*<p>', '\n\n', text)
    text = re.sub(r'</?p>', '', text)
    if '<' in text:
        return content
    import html
    return html.unescape(text).strip()


def _parse_published_at(value):
    from datetime import datetime
    try:
        return datetime.strptime(value, '%Y-%m-%d')
    except (TypeError, ValueError):
        return datetime.now()


def _news_category(form):
    key = (form.get('category') or '').strip()
    return key if is_valid_category(key) else None


def _unique_filename(folder, base, ext):
    """Nombre libre dentro de folder: base.ext, base-2.ext, ..."""
    name = f"{base}.{ext}"
    counter = 2
    while os.path.exists(os.path.join(folder, name)):
        name = f"{base}-{counter}.{ext}"
        counter += 1
    return name


def _save_news_images(news_item):
    """Guardar las fotos subidas (campo 'images', múltiple) al final de la
    galería. Devuelve la cantidad de formatos rechazados."""
    rejected = 0
    next_order = max([img.order or 0 for img in news_item.images], default=-1) + 1
    folder = _news_folder(news_item)
    for upload in request.files.getlist('images'):
        if not upload or not upload.filename:
            continue
        ext = upload.filename.rsplit('.', 1)[-1].lower() if '.' in upload.filename else ''
        if ext not in NEWS_IMAGE_EXTENSIONS:
            rejected += 1
            continue
        base = secure_filename(upload.filename.rsplit('.', 1)[0])[:40].lower() or 'foto'
        filename = _unique_filename(folder, base, ext)
        upload.save(os.path.join(folder, filename))
        news_item.images.append(NewsImage(
            path=f"news/{news_item.slug}/{filename}", order=next_order))
        next_order += 1
    if rejected:
        flash(f'{rejected} archivo(s) de imagen no se subieron: usá PNG, JPG o WebP.', 'error')
    return rejected


def _save_news_attachments(news_item):
    """Guardar los adjuntos subidos (campo 'attachments', múltiple)."""
    rejected = 0
    next_order = max([a.order or 0 for a in news_item.attachments], default=-1) + 1
    folder = _news_folder(news_item, 'archivos')
    for upload in request.files.getlist('attachments'):
        if not upload or not upload.filename:
            continue
        original = upload.filename
        ext = original.rsplit('.', 1)[-1].lower() if '.' in original else ''
        if ext not in NEWS_ATTACHMENT_EXTENSIONS:
            rejected += 1
            continue
        base = secure_filename(original.rsplit('.', 1)[0])[:60] or 'archivo'
        filename = _unique_filename(folder, base, ext)
        full_path = os.path.join(folder, filename)
        upload.save(full_path)
        news_item.attachments.append(NewsAttachment(
            path=f"news/{news_item.slug}/archivos/{filename}",
            title=original.rsplit('.', 1)[0][:200],
            size=os.path.getsize(full_path),
            order=next_order))
        next_order += 1
    if rejected:
        flash(f'{rejected} adjunto(s) no se subieron. Formatos permitidos: '
              + ', '.join(sorted(NEWS_ATTACHMENT_EXTENSIONS)).upper() + '.', 'error')
    return rejected


def _remove_static_file(rel_path):
    path = os.path.join(current_app.static_folder, 'img', rel_path)
    if os.path.exists(path):
        os.remove(path)


def _update_news_media(news_item):
    """Aplicar epígrafes, orden y bajas de la galería y los adjuntos
    según los campos del formulario de edición."""
    form = request.form
    for img in list(news_item.images):
        if form.get(f'image_remove_{img.id}') == '1':
            _remove_static_file(img.path)
            news_item.images.remove(img)
            continue
        img.caption = form.get(f'image_caption_{img.id}', '').strip()[:300] or None
        img.caption_en = form.get(f'image_caption_en_{img.id}', '').strip()[:300] or None
        try:
            img.order = int(form.get(f'image_order_{img.id}', img.order or 0))
        except ValueError:
            pass
        focus = form.get(f'image_focus_{img.id}', '')
        if ',' in focus:
            try:
                fx, fy = (int(float(v)) for v in focus.split(',', 1))
                img.focus_x = min(100, max(0, fx))
                img.focus_y = min(100, max(0, fy))
            except ValueError:
                pass
    for pos, img in enumerate(sorted(news_item.images, key=lambda i: (i.order or 0, i.id or 0))):
        img.order = pos

    for att in list(news_item.attachments):
        if form.get(f'attachment_remove_{att.id}') == '1':
            _remove_static_file(att.path)
            news_item.attachments.remove(att)
            continue
        att.title = form.get(f'attachment_title_{att.id}', '').strip()[:200] or att.title


def _delete_news_files(news_item):
    """Borrar la carpeta de archivos de la novedad (galería + adjuntos + legado)."""
    import shutil
    if news_item.image:
        _remove_static_file(news_item.image)
    folder = os.path.join(current_app.static_folder, 'img', 'news', news_item.slug)
    if os.path.isdir(folder):
        shutil.rmtree(folder, ignore_errors=True)


@bp.route('/news', methods=['GET', 'POST'])
@admin_required
def news():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        if not title:
            flash('El título es obligatorio.', 'error')
            return redirect(url_for('admin.news'))

        item = News(
            slug=_news_slug(title),
            title=title[:300],
            title_en=request.form.get('title_en', '').strip()[:300] or None,
            category=_news_category(request.form),
            excerpt=request.form.get('excerpt', '').strip()[:500] or None,
            excerpt_en=request.form.get('excerpt_en', '').strip()[:500] or None,
            content=_news_content_html(request.form.get('content')),
            content_en=_news_content_html(request.form.get('content_en')),
            published_at=_parse_published_at(request.form.get('published_at')),
        )
        _save_news_images(item)
        _save_news_attachments(item)
        db.session.add(item)
        db.session.commit()
        flash(f'Novedad "{title}" publicada.', 'success')
        return redirect(url_for('admin.news'))

    from datetime import date
    all_news = News.query.order_by(News.published_at.desc()).all()
    for n in all_news:
        n.content_text = _news_content_text(n.content)
        n.content_text_en = _news_content_text(n.content_en)
    return render_template('admin/news.xhtml', news=all_news,
                           categories=NEWS_CATEGORIES,
                           image_extensions=sorted(NEWS_IMAGE_EXTENSIONS),
                           attachment_extensions=sorted(NEWS_ATTACHMENT_EXTENSIONS),
                           today=date.today().isoformat())


@bp.route('/news/<int:news_id>/edit', methods=['POST'])
@admin_required
def edit_news(news_id):
    item = News.query.get_or_404(news_id)
    item.title = request.form.get('title', item.title).strip()[:300] or item.title
    item.title_en = request.form.get('title_en', '').strip()[:300] or None
    item.category = _news_category(request.form)
    item.excerpt = request.form.get('excerpt', '').strip()[:500] or None
    item.excerpt_en = request.form.get('excerpt_en', '').strip()[:500] or None
    item.content = _news_content_html(request.form.get('content'))
    item.content_en = _news_content_html(request.form.get('content_en'))
    if request.form.get('published_at'):
        item.published_at = _parse_published_at(request.form.get('published_at'))
    _update_news_media(item)
    _save_news_images(item)
    _save_news_attachments(item)
    db.session.commit()
    flash('Novedad actualizada.', 'success')
    return redirect(url_for('admin.news'))


@bp.route('/news/<int:news_id>/delete', methods=['POST'])
@admin_required
def delete_news(news_id):
    item = News.query.get_or_404(news_id)
    _delete_news_files(item)
    db.session.delete(item)
    db.session.commit()
    flash('Novedad eliminada.', 'success')
    return redirect(url_for('admin.news'))


@bp.route('/partners/<int:partner_id>/edit', methods=['POST'])
@admin_required
def edit_partner(partner_id):
    partner = Partner.query.get_or_404(partner_id)
    partner.name = request.form.get('name', partner.name).strip() or partner.name
    partner.url = request.form.get('url', '').strip() or None
    order = request.form.get('order', type=int)
    if order is not None:
        partner.order = order
    if request.form.get('remove_image') == '1':
        _delete_partner_image(partner)
    if _save_partner_image(partner):
        return redirect(url_for('admin.partners'))
    db.session.commit()
    flash('Organización actualizada.', 'success')
    return redirect(url_for('admin.partners'))


@bp.route('/partners/<int:partner_id>/delete', methods=['POST'])
@admin_required
def delete_partner(partner_id):
    partner = Partner.query.get_or_404(partner_id)
    _delete_partner_image(partner)
    db.session.delete(partner)
    db.session.commit()
    flash('Organización eliminada.', 'success')
    return redirect(url_for('admin.partners'))
