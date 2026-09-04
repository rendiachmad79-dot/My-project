# My-project

Aplikasi Python CLI sederhana.

## Struktur

```
myproject/
├── src/myproject/main.py   # Entry point
├── tests/test_main.py      # Unit tests
├── requirements.txt
├── pyproject.toml
└── .gitignore
```

## Cara menjalankan

```bash
cd myproject
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .

myproject                   # Hello, World.
myproject Budi              # Hello, Budi.
myproject Budi --excited    # Hello, Budi!
```

## Testing

```bash
pytest
```
