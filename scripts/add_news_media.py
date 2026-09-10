"""
Migración: galería y adjuntos de novedades.

Crea las tablas news_images y news_attachments (si no existen) y pasa la
imagen única legada (news.image) a la galería como primera foto.
Idempotente: se puede correr varias veces.
"""
import sqlite3
import os

DB_PATH = os.environ.get('DATABASE_PATH', 'instance/gipis.db')


def migrate():
    if not os.path.exists(DB_PATH):
        print(f"Base de datos no encontrada en {DB_PATH}. Nada que migrar.")
        return

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS news_images (
            id INTEGER PRIMARY KEY,
            news_id INTEGER NOT NULL REFERENCES news(id),
            path VARCHAR(255) NOT NULL,
            caption VARCHAR(300),
            caption_en VARCHAR(300),
            "order" INTEGER
        )""")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS news_attachments (
            id INTEGER PRIMARY KEY,
            news_id INTEGER NOT NULL REFERENCES news(id),
            path VARCHAR(255) NOT NULL,
            title VARCHAR(200),
            size INTEGER,
            "order" INTEGER
        )""")
    print("  ✓ Tablas news_images y news_attachments disponibles.")

    moved = 0
    for news_id, image in cur.execute(
            "SELECT id, image FROM news WHERE image IS NOT NULL AND image != ''").fetchall():
        exists = cur.execute(
            "SELECT 1 FROM news_images WHERE news_id = ? LIMIT 1", (news_id,)).fetchone()
        if exists:
            continue
        cur.execute(
            'INSERT INTO news_images (news_id, path, "order") VALUES (?, ?, 0)',
            (news_id, image))
        cur.execute("UPDATE news SET image = NULL WHERE id = ?", (news_id,))
        moved += 1
    if moved:
        print(f"  ✓ {moved} imagen(es) de portada pasadas a la galería.")
    else:
        print("  - Sin imágenes legadas para migrar.")

    # Categorías cargadas como texto libre antes de fijar las claves
    # (app/news_meta.py): se pasan a la clave equivalente.
    import unicodedata

    def norm(text):
        text = unicodedata.normalize('NFKD', text or '').encode('ascii', 'ignore').decode('ascii')
        return ' '.join(text.lower().split())

    legacy = {
        'cooperacion academica': 'cooperacion-academica',
        'cooperacion cientifica': 'cooperacion-cientifica',
        'vinculacion con empresas': 'vinculacion-transferencia',
        'vinculacion y transferencia': 'vinculacion-transferencia',
        'vinculacion-empresas': 'vinculacion-transferencia',  # clave usada brevemente el 2026-09-10
        'comunicacion publica de la ciencia': 'comunicacion-publica',
    }
    known = set(legacy.values())
    for news_id, category in cur.execute(
            "SELECT id, category FROM news WHERE category IS NOT NULL AND category != ''").fetchall():
        if category in known:
            continue
        key = legacy.get(norm(category))
        if key:
            cur.execute("UPDATE news SET category = ? WHERE id = ?", (key, news_id))
            print(f"  ✓ Novedad {news_id}: categoría '{category}' → '{key}'.")
        else:
            print(f"  ! Novedad {news_id}: categoría '{category}' no coincide con ninguna fija; se deja como está.")

    conn.commit()
    conn.close()
    print("Migración de galería y adjuntos de novedades completada.")


if __name__ == "__main__":
    migrate()
