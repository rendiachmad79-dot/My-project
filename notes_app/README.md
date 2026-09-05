# Notes App

Aplikasi web **Buku Catatan** sederhana berbasis Flask + SQLite.

## Fitur
- Lihat daftar catatan
- Tambah catatan baru
- Edit catatan
- Hapus catatan

## Struktur
```
notes_app/
├── src/notes_app/
│   ├── __init__.py
│   ├── app.py            # Flask routes & factory
│   ├── db.py             # SQLite helper
│   └── templates/        # base, index, form
├── tests/test_app.py
├── pyproject.toml
├── requirements.txt
└── .gitignore
```

## Cara menjalankan

```bash
cd notes_app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# jalankan server
flask --app notes_app.app run --debug
# buka http://127.0.0.1:5000
```

## Testing

```bash
pytest
```
