import os
import tempfile

import pytest

from notes_app import create_app
from notes_app import db as dbmod


@pytest.fixture
def app():
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    os.environ["NOTES_DB"] = path
    app = create_app()
    app.config["TESTING"] = True
    yield app
    os.unlink(path)


@pytest.fixture
def client(app):
    return app.test_client()


def test_index_empty(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Belum ada catatan" in resp.data


def test_create_and_view_note(client):
    resp = client.post("/notes/new", data={"title": "Belajar", "body": "Flask"}, follow_redirects=True)
    assert resp.status_code == 200
    assert b"Belajar" in resp.data
    assert b"Flask" in resp.data


def test_create_requires_title(client):
    resp = client.post("/notes/new", data={"title": "", "body": "x"})
    assert resp.status_code == 400
    assert b"Judul wajib diisi" in resp.data


def test_edit_note(client):
    dbmod.create_note("Lama", "isi lama")
    notes = dbmod.list_notes()
    nid = notes[0]["id"]
    resp = client.post(f"/notes/{nid}/edit", data={"title": "Baru", "body": "isi baru"}, follow_redirects=True)
    assert resp.status_code == 200
    assert b"Baru" in resp.data
    assert dbmod.get_note(nid)["title"] == "Baru"


def test_delete_note(client):
    nid = dbmod.create_note("Hapus", "byebye")
    resp = client.post(f"/notes/{nid}/delete", follow_redirects=True)
    assert resp.status_code == 200
    assert dbmod.get_note(nid) is None


def test_edit_404(client):
    resp = client.get("/notes/9999/edit")
    assert resp.status_code == 404
