import os
import re
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app, abort
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from app import db
from app.models import Member, MemberWork, ResearchSection, ResearchItem

bp = Blueprint('auth', __name__, url_prefix='/auth')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_upload_folder():
    upload_folder = os.path.join(current_app.static_folder, 'img', 'profiles')
    os.makedirs(upload_folder, exist_ok=True)
    return upload_folder


def _member_by_login_email(email):
    """Buscar miembro por cualquiera de sus emails habilitados para login."""
    e = (email or '').strip().lower()
    if not e:
        return None
    return Member.query.filter(db.or_(
        db.func.lower(Member.email) == e,
        db.and_(Member.personal_email_login,
                db.func.lower(Member.personal_email) == e),
        db.and_(Member.institutional_email_login,
                db.func.lower(Member.institutional_email) == e),
    )).first()


def _login_email_taken(member, email):
    """¿Otro miembro ya usa este email para iniciar sesión?"""
    e = (email or '').strip().lower()
    if not e:
        return False
    return Member.query.filter(Member.id != member.id).filter(db.or_(
        db.func.lower(Member.email) == e,
        db.and_(Member.personal_email_login,
                db.func.lower(Member.personal_email) == e),
        db.and_(Member.institutional_email_login,
                db.func.lower(Member.institutional_email) == e),
    )).count() > 0


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """Página de login para miembros"""
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))

    if request.method == 'POST':
        from app.security import rate_limited
        if rate_limited('login', limit=10, window_seconds=300):
            flash('Demasiados intentos de ingreso. Esperá unos minutos '
                  'y probá de nuevo.', 'error')
            return render_template('auth/login.xhtml'), 429

        email = request.form.get('email')
        password = request.form.get('password')

        member = _member_by_login_email(email)

        if member and member.check_password(password):
            login_user(member)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('auth.dashboard'))
        else:
            flash('Email o contraseña incorrectos', 'error')
    
    return render_template('auth/login.xhtml')


@bp.route('/logout')
@login_required
def logout():
    """Cerrar sesión"""
    logout_user()
    return redirect(url_for('main.home'))


@bp.route('/dashboard')
@login_required
def dashboard():
    """Dashboard del miembro - editar perfil"""
    return render_template('auth/dashboard.xhtml')


def _save_photo(member, photo):
    """Guardar la foto subida como <slug>.<ext>, borrando la anterior si cambia de extensión."""
    ext = photo.filename.rsplit('.', 1)[1].lower()
    filename = f"{member.slug}.{ext}"
    if member.photo and member.photo != filename:
        old_path = os.path.join(get_upload_folder(), member.photo)
        if os.path.exists(old_path):
            os.remove(old_path)
    photo.save(os.path.join(get_upload_folder(), filename))
    member.photo = filename


def _remove_photo(member):
    if member.photo:
        old_path = os.path.join(get_upload_folder(), member.photo)
        if os.path.exists(old_path):
            os.remove(old_path)
        member.photo = None


def apply_profile_form(member, form, files):
    """Volcar el formulario de perfil sobre `member` (sin commit).

    Lo usan el miembro para su propio perfil y el administrador para
    editar a cualquier integrante. Devuelve None si todo fue bien o un
    mensaje de error para mostrar con flash (en ese caso no hay que
    commitear).
    """
    member.name = form.get('name', member.name).strip() or member.name
    member.degree = form.get('degree', member.degree)
    member.position = form.get('position', member.position)
    member.bio = form.get('bio', member.bio)
    member.bio_en = form.get('bio_en', '').strip() or None
    member.linkedin = form.get('linkedin', member.linkedin)

    orcid_raw = form.get('orcid', '').strip()
    if orcid_raw:
        from app.orcid import normalize_orcid_id
        orcid_id = normalize_orcid_id(orcid_raw)
        if not orcid_id:
            return ('El ORCID iD no es válido. Copialo del perfil en orcid.org '
                    '(formato 0000-0000-0000-0000).')
        member.orcid = orcid_id
    else:
        member.orcid = None

    # Emails con visibilidad y habilitación de login
    member.personal_email = form.get('personal_email', member.personal_email)
    member.personal_email_public = 'personal_email_public' in form
    member.institutional_email = form.get('institutional_email', member.institutional_email)
    member.institutional_email_public = 'institutional_email_public' in form

    for field, flag in (('personal_email', 'personal_email_login'),
                        ('institutional_email', 'institutional_email_login')):
        wanted = flag in form
        value = getattr(member, field)
        if wanted and value and _login_email_taken(member, value):
            flash(f'El email {value} ya lo usa otro miembro para iniciar '
                  'sesión, no se puede habilitar.', 'error')
            wanted = False
        setattr(member, flag, wanted and bool(value))
    member.phone = form.get('phone', member.phone)
    member.phone_public = 'phone_public' in form

    # Foto de perfil
    photo = files.get('photo')
    if photo and photo.filename:
        if not allowed_file(photo.filename):
            return 'Formato de imagen no permitido. Usá PNG, JPG o WebP.'
        _save_photo(member, photo)
    if form.get('remove_photo') == '1':
        _remove_photo(member)

    # Contraseña (opcional)
    new_password = form.get('new_password')
    if new_password:
        member.set_password(new_password)
    return None


@bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """Editar perfil del miembro"""
    if request.method == 'POST':
        error = apply_profile_form(current_user, request.form, request.files)
        if error:
            db.session.rollback()
            flash(error, 'error')
            return redirect(url_for('auth.edit_profile'))
        db.session.commit()
        flash('Perfil actualizado correctamente', 'success')
        return redirect(url_for('auth.dashboard'))

    return render_template('auth/edit_profile.xhtml', member=current_user,
                           admin_mode=False,
                           form_action=url_for('auth.edit_profile'),
                           back_url=url_for('auth.dashboard'))


# ==========================================
# Recuperación de contraseña por email
# ==========================================

def _reset_serializer():
    from itsdangerous import URLSafeTimedSerializer
    return URLSafeTimedSerializer(current_app.config['SECRET_KEY'],
                                  salt='password-reset')


@bp.route('/forgot', methods=['GET', 'POST'])
def forgot_password():
    """Solicitar link de restablecimiento por email"""
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))

    if request.method == 'POST':
        from app.security import rate_limited
        if rate_limited('forgot', limit=3, window_seconds=900):
            flash('Demasiados pedidos de restablecimiento. Esperá unos '
                  'minutos y probá de nuevo.', 'error')
            return render_template('auth/forgot.xhtml'), 429

        email = request.form.get('email', '').strip().lower()
        member = _member_by_login_email(email)

        if member:
            token = _reset_serializer().dumps(member.id)
            reset_url = url_for('auth.reset_password', token=token, _external=True)
            try:
                from flask_mail import Message
                from app import mail
                msg = Message(
                    subject='[GIPIS] Restablecer tu contraseña',
                    recipients=[email],
                )
                msg.body = (
                    f"Hola {member.name},\n\n"
                    f"Recibimos un pedido para restablecer tu contraseña del sitio GIPIS.\n"
                    f"Entrá a este enlace (válido por 1 hora):\n\n{reset_url}\n\n"
                    f"Si no lo pediste vos, ignorá este mensaje.\n"
                )
                mail.send(msg)
            except Exception:
                current_app.logger.exception('Error enviando email de reset')
                flash('No se pudo enviar el email. Contactá a un administrador '
                      'del grupo para que restablezca tu contraseña.', 'error')
                return redirect(url_for('auth.forgot_password'))

        # Mensaje idéntico exista o no la cuenta (no revelar emails)
        flash('Si el email está registrado, te enviamos un enlace para '
              'restablecer la contraseña. Revisá tu casilla (y el spam).', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/forgot.xhtml')


@bp.route('/reset/<token>', methods=['GET', 'POST'])
def reset_password(token):
    """Definir nueva contraseña desde el link del email"""
    from itsdangerous import BadSignature, SignatureExpired
    try:
        member_id = _reset_serializer().loads(token, max_age=3600)
    except SignatureExpired:
        flash('El enlace expiró (dura 1 hora). Pedí uno nuevo.', 'error')
        return redirect(url_for('auth.forgot_password'))
    except BadSignature:
        flash('El enlace no es válido.', 'error')
        return redirect(url_for('auth.forgot_password'))

    member = Member.query.get(member_id)
    if not member:
        flash('El enlace no es válido.', 'error')
        return redirect(url_for('auth.forgot_password'))

    if request.method == 'POST':
        from app.security import rate_limited
        if rate_limited('reset', limit=10, window_seconds=900):
            flash('Demasiados intentos. Esperá unos minutos.', 'error')
            return redirect(url_for('auth.forgot_password'))

        password = request.form.get('password', '')
        confirm = request.form.get('confirm', '')
        if len(password) < 8:
            flash('La contraseña debe tener al menos 8 caracteres.', 'error')
        elif password != confirm:
            flash('Las contraseñas no coinciden.', 'error')
        else:
            member.set_password(password)
            db.session.commit()
            flash('Contraseña actualizada. Ya podés ingresar.', 'success')
            return redirect(url_for('auth.login'))

    return render_template('auth/reset_password.xhtml', token=token, member=member)


# ==========================================
# Mi producción (trabajos personales)
# ==========================================

# Sección sugerida al compartir, por tipo de trabajo
KIND_DEFAULT_SECTION = {
    'publication': 'publications',
    'project': 'projects',
    'thesis': 'doctoral',
}


def _target_member():
    """Miembro sobre cuya producción se opera: uno mismo o, para un
    administrador, el indicado en `member_id` (query string o formulario)."""
    member_id = request.values.get('member_id', type=int)
    if not member_id or member_id == current_user.id:
        return current_user
    if not current_user.is_admin:
        abort(403)
    return Member.query.get_or_404(member_id)


def _works_url(member):
    """URL de la página de producción de `member` (propia o como admin)."""
    if member.id == current_user.id:
        return url_for('auth.works')
    return url_for('auth.works', member_id=member.id)


def _works_context(member):
    return dict(member=member, admin_mode=member.id != current_user.id,
                works_url=_works_url(member))


@bp.route('/works', methods=['GET', 'POST'])
@login_required
def works():
    """Producción personal del miembro (o de otro integrante, para un admin)"""
    member = _target_member()
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        if not title:
            flash('El título es obligatorio.', 'error')
            return redirect(_works_url(member))

        kind = request.form.get('kind', 'publication')
        if kind not in MemberWork.KINDS:
            kind = 'publication'

        db.session.add(MemberWork(
            member_id=member.id,
            kind=kind,
            title=title,
            authors=request.form.get('authors', '').strip() or None,
            year=request.form.get('year', '').strip() or None,
            detail=request.form.get('detail', '').strip() or None,
        ))
        db.session.commit()
        flash('Trabajo agregado a la producción.', 'success')
        return redirect(_works_url(member))

    my_works = member.works.order_by(
        MemberWork.kind, MemberWork.year.desc()).all()
    sections = ResearchSection.query.order_by(ResearchSection.order).all()
    return render_template('auth/works.xhtml', works=my_works, sections=sections,
                           kinds=MemberWork.KINDS, default_sections=KIND_DEFAULT_SECTION,
                           **_works_context(member))


def _own_work_or_404(work_id):
    """Obra propia; un administrador puede operar sobre la de cualquiera."""
    work = MemberWork.query.get_or_404(work_id)
    if work.member_id != current_user.id and not current_user.is_admin:
        abort(403)
    return work


@bp.route('/works/<int:work_id>/edit', methods=['POST'])
@login_required
def edit_work(work_id):
    work = _own_work_or_404(work_id)
    work.title = request.form.get('title', work.title).strip() or work.title
    work.authors = request.form.get('authors', '').strip() or None
    work.year = request.form.get('year', '').strip() or None
    work.detail = request.form.get('detail', '').strip() or None
    kind = request.form.get('kind')
    if kind in MemberWork.KINDS:
        work.kind = kind
    # Si está compartido, reflejar los cambios en el ítem del sitio
    if work.shared_item:
        work.shared_item.title = work.title
        work.shared_item.authors = work.authors
        work.shared_item.year = work.year
        work.shared_item.abstract = work.detail
    db.session.commit()
    flash('Trabajo actualizado.', 'success')
    return redirect(_works_url(work.member))


def _release_shared_item(work):
    """Quitar el ítem del sitio solo si ningún otro miembro lo comparte"""
    item = work.shared_item
    work.shared_item_id = None
    if item:
        others = MemberWork.query.filter(
            MemberWork.shared_item_id == item.id,
            MemberWork.id != work.id,
        ).count()
        if others == 0:
            db.session.delete(item)


@bp.route('/works/<int:work_id>/delete', methods=['POST'])
@login_required
def delete_work(work_id):
    work = _own_work_or_404(work_id)
    back = _works_url(work.member)
    _release_shared_item(work)
    db.session.delete(work)
    db.session.commit()
    flash('Trabajo eliminado.', 'success')
    return redirect(back)


@bp.route('/works/<int:work_id>/share', methods=['POST'])
@login_required
def share_work(work_id):
    """Publicar un trabajo personal en la sección de Investigación elegida"""
    work = _own_work_or_404(work_id)
    back = _works_url(work.member)
    if work.shared_item:
        flash('Este trabajo ya está compartido en el sitio.', 'error')
        return redirect(back)

    section_id = request.form.get('section_id', type=int)
    section = ResearchSection.query.get(section_id) if section_id else None
    if not section:
        flash('Elegí una sección válida.', 'error')
        return redirect(back)

    # Evitar duplicados: mismo título (sin distinguir mayúsculas) en la sección
    existing = ResearchItem.query.filter(
        ResearchItem.section_id == section.id,
        db.func.lower(ResearchItem.title) == work.title.lower(),
    ).first()
    if existing:
        work.shared_item_id = existing.id
        db.session.commit()
        flash('Ya existía un ítem igual en esa sección; se vinculó el trabajo a ese ítem.', 'success')
        return redirect(back)

    slug_base = re.sub(r'[^a-z0-9]+', '-', work.title.lower()).strip('-')[:40] or 'item'
    slug = slug_base
    counter = 2
    while ResearchItem.query.filter_by(slug=slug).first():
        slug = f"{slug_base}-{counter}"
        counter += 1

    item = ResearchItem(
        slug=slug,
        title=work.title,
        authors=work.authors,
        year=work.year,
        abstract=work.detail,
        section_id=section.id,
    )
    db.session.add(item)
    db.session.flush()
    work.shared_item_id = item.id
    db.session.commit()
    flash(f'Trabajo publicado en "{section.title}".', 'success')
    return redirect(back)


# ==========================================
# Importación desde SIGEVA
# ==========================================

@bp.route('/sigeva/parse', methods=['POST'])
@login_required
def sigeva_parse():
    """Analizar el PDF de SIGEVA y mostrar la pantalla de revisión"""
    member = _target_member()
    back = _works_url(member)
    pdf = request.files.get('pdf')
    if not pdf or not pdf.filename.lower().endswith('.pdf'):
        flash('Subí un archivo PDF exportado de SIGEVA.', 'error')
        return redirect(back)

    try:
        from app.sigeva import parse_sigeva
        result = parse_sigeva(pdf.stream)
    except Exception:
        current_app.logger.exception('Error parseando PDF de SIGEVA')
        flash('No se pudo leer el PDF. ¿Es el CV exportado de SIGEVA?', 'error')
        return redirect(back)

    if not result['items'] and not result['profile']:
        flash('No se encontró información reconocible en el PDF.', 'error')
        return redirect(back)

    # Marcar los que ya existen en la producción del miembro para no preseleccionarlos
    existing = {w.title.lower() for w in member.works}
    for item in result['items']:
        item['duplicate'] = item['title'].lower() in existing

    groups = {}
    for idx, item in enumerate(result['items']):
        groups.setdefault(item['group'], []).append((idx, item))

    import json
    return render_template(
        'auth/sigeva_review.xhtml',
        profile=result['profile'],
        groups=groups,
        payload=json.dumps({'profile': result['profile'], 'items': result['items']}),
        **_works_context(member),
    )


@bp.route('/sigeva/import', methods=['POST'])
@login_required
def sigeva_import():
    """Guardar los elementos seleccionados en la revisión"""
    import json
    member = _target_member()
    back = _works_url(member)
    try:
        payload = json.loads(request.form.get('payload', '{}'))
    except ValueError:
        flash('Datos de importación inválidos. Volvé a subir el PDF.', 'error')
        return redirect(back)

    items = payload.get('items', [])
    selected = {int(i) for i in request.form.getlist('item') if i.isdigit()}

    existing = {w.title.lower() for w in member.works}
    imported = skipped = 0
    for idx in sorted(selected):
        if idx >= len(items):
            continue
        item = items[idx]
        title = (item.get('title') or '').strip()
        if not title:
            continue
        if title.lower() in existing:
            skipped += 1
            continue
        kind = item.get('kind')
        if kind not in MemberWork.KINDS:
            kind = 'publication'
        db.session.add(MemberWork(
            member_id=member.id,
            kind=kind,
            title=title[:500],
            authors=(item.get('authors') or '')[:500] or None,
            year=(item.get('year') or '')[:10] or None,
            detail=item.get('detail') or None,
            source='sigeva',
        ))
        existing.add(title.lower())
        imported += 1

    profile = payload.get('profile', {})
    profile_updates = []
    if request.form.get('profile_degree') and profile.get('degree'):
        member.degree = profile['degree'][:100]
        profile_updates.append('título')
    if request.form.get('profile_bio') and profile.get('bio'):
        member.bio = profile['bio']
        profile_updates.append('biografía')

    db.session.commit()

    parts = [f'{imported} trabajos importados']
    if skipped:
        parts.append(f'{skipped} ya existían')
    if profile_updates:
        parts.append(f'perfil actualizado ({", ".join(profile_updates)})')
    flash('. '.join(parts) + '.', 'success')
    return redirect(back)


# ==========================================
# Búsqueda de metadatos por DOI
# ==========================================

@bp.route('/doi/lookup')
@login_required
def doi_lookup():
    """Devolver metadatos de un DOI en JSON (para autocompletar formularios)"""
    from flask import jsonify
    from app.doi import normalize_doi, fetch_doi, DoiError

    doi = normalize_doi(request.args.get('doi', ''))
    if not doi:
        return jsonify(ok=False, error='Ingresá un DOI válido (ej: 10.1109/5.771073).')
    try:
        data = fetch_doi(doi)
    except DoiError as e:
        return jsonify(ok=False, error=str(e))
    except Exception:
        current_app.logger.exception('Error consultando DOI')
        return jsonify(ok=False, error='Error inesperado consultando el DOI.')
    return jsonify(ok=True, **data)


# ==========================================
# Importación desde ORCID
# ==========================================

@bp.route('/orcid/fetch', methods=['POST'])
@login_required
def orcid_fetch():
    """Consultar la API pública de ORCID y mostrar la pantalla de revisión"""
    from app.orcid import normalize_orcid_id, fetch_orcid_works, OrcidError

    member = _target_member()
    back = _works_url(member)
    # Permite pasar el iD en el formulario (y de paso guardarlo en el perfil)
    orcid_raw = request.form.get('orcid', '').strip()
    if orcid_raw:
        orcid_id = normalize_orcid_id(orcid_raw)
        if not orcid_id:
            flash('El ORCID iD no es válido. Copialo del perfil en orcid.org '
                  '(formato 0000-0000-0000-0000).', 'error')
            return redirect(back)
        if member.orcid != orcid_id:
            member.orcid = orcid_id
            db.session.commit()
    else:
        orcid_id = member.orcid

    if not orcid_id:
        flash('Cargá el ORCID iD para poder importar las publicaciones.', 'error')
        return redirect(back)

    try:
        result = fetch_orcid_works(orcid_id)
    except OrcidError as e:
        flash(str(e), 'error')
        return redirect(back)
    except Exception:
        current_app.logger.exception('Error consultando ORCID')
        flash('Ocurrió un error inesperado consultando ORCID.', 'error')
        return redirect(back)

    if not result['items']:
        flash('El registro ORCID no tiene trabajos públicos para importar.', 'error')
        return redirect(back)

    return _render_import_review(
        member,
        result['items'],
        source='orcid',
        source_label='ORCID',
        intro=(f'Esto es lo que encontramos en el registro ORCID '
               f'<a href="https://orcid.org/{orcid_id}" target="_blank" rel="noopener" '
               f'class="text-primary hover:underline font-medium">{orcid_id}</a>'
               + (f' ({result["name"]})' if result['name'] else '') + '.'),
    )


def _render_import_review(member, items, source, source_label, intro):
    """Pantalla de revisión compartida por las importaciones ORCID/OpenAlex"""
    existing = {w.title.lower() for w in member.works}
    for item in items:
        item['duplicate'] = item['title'].lower() in existing

    groups = {}
    for idx, item in enumerate(items):
        groups.setdefault(item['group'], []).append((idx, item))

    import json
    from markupsafe import Markup
    return render_template(
        'auth/import_review.xhtml',
        source=source,
        source_label=source_label,
        intro=Markup(intro),
        groups=groups,
        payload=json.dumps({'items': items}),
        **_works_context(member),
    )


@bp.route('/openalex/fetch', methods=['POST'])
@login_required
def openalex_fetch():
    """Buscar en OpenAlex publicaciones indexadas para el ORCID del miembro"""
    from app.openalex import fetch_openalex_works, OpenAlexError

    member = _target_member()
    back = _works_url(member)
    if not member.orcid:
        flash('Cargá el ORCID iD en el perfil para poder buscar en OpenAlex.', 'error')
        return redirect(back)

    try:
        result = fetch_openalex_works(member.orcid)
    except OpenAlexError as e:
        flash(str(e), 'error')
        return redirect(back)
    except Exception:
        current_app.logger.exception('Error consultando OpenAlex')
        flash('Ocurrió un error inesperado consultando OpenAlex.', 'error')
        return redirect(back)

    if not result['items']:
        flash('OpenAlex no tiene trabajos indexados para el ORCID iD.', 'error')
        return redirect(back)

    return _render_import_review(
        member,
        result['items'],
        source='openalex',
        source_label='OpenAlex',
        intro=(f'Esto es lo que OpenAlex tiene indexado para el ORCID '
               f'{member.orcid}, ordenado por citas. Puede incluir '
               f'trabajos que no están en el perfil de ORCID — y también '
               f'atribuciones erróneas: revisá antes de importar.'),
    )


IMPORT_SOURCES = {'orcid', 'openalex'}


@bp.route('/works/import', methods=['POST'])
@login_required
def works_import():
    """Guardar los trabajos seleccionados en la pantalla de revisión"""
    import json
    member = _target_member()
    back = _works_url(member)
    try:
        payload = json.loads(request.form.get('payload', '{}'))
    except ValueError:
        flash('Datos de importación inválidos. Volvé a hacer la búsqueda.', 'error')
        return redirect(back)

    source = request.form.get('source', 'orcid')
    if source not in IMPORT_SOURCES:
        source = 'orcid'

    items = payload.get('items', [])
    selected = {int(i) for i in request.form.getlist('item') if i.isdigit()}

    existing = {w.title.lower() for w in member.works}
    imported = skipped = 0
    for idx in sorted(selected):
        if idx >= len(items):
            continue
        item = items[idx]
        title = (item.get('title') or '').strip()
        if not title:
            continue
        if title.lower() in existing:
            skipped += 1
            continue
        kind = item.get('kind')
        if kind not in MemberWork.KINDS:
            kind = 'publication'
        db.session.add(MemberWork(
            member_id=member.id,
            kind=kind,
            title=title[:500],
            authors=(item.get('authors') or '')[:500] or None,
            year=(item.get('year') or '')[:10] or None,
            detail=item.get('detail') or None,
            source=source,
        ))
        existing.add(title.lower())
        imported += 1

    db.session.commit()

    source_names = {'orcid': 'ORCID', 'openalex': 'OpenAlex'}
    parts = [f'{imported} trabajos importados desde {source_names[source]}']
    if skipped:
        parts.append(f'{skipped} ya existían')
    flash('. '.join(parts) + '.', 'success')
    return redirect(back)


@bp.route('/works/<int:work_id>/unshare', methods=['POST'])
@login_required
def unshare_work(work_id):
    work = _own_work_or_404(work_id)
    if work.shared_item:
        _release_shared_item(work)
        db.session.commit()
        flash('El trabajo ya no se muestra en la página de Investigación.', 'success')
    return redirect(_works_url(work.member))

