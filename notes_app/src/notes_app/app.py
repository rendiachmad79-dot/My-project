from flask import Flask, redirect, render_template, request, url_for

from . import db


def create_app(database: str | None = None) -> Flask:
    app = Flask(__name__)
    if database:
        import os
        os.environ["NOTES_DB"] = database

    with app.app_context():
        db.init_db()

    @app.route("/")
    def index():
        notes = db.list_notes()
        return render_template("index.html", notes=notes)

    @app.route("/notes/new", methods=["GET", "POST"])
    def new_note():
        if request.method == "POST":
            title = (request.form.get("title") or "").strip()
            body = (request.form.get("body") or "").strip()
            if not title:
                return render_template("form.html", note=None, error="Judul wajib diisi"), 400
            db.create_note(title, body)
            return redirect(url_for("index"))
        return render_template("form.html", note=None, error=None)

    @app.route("/notes/<int:note_id>/edit", methods=["GET", "POST"])
    def edit_note(note_id: int):
        note = db.get_note(note_id)
        if note is None:
            return ("Not found", 404)
        if request.method == "POST":
            title = (request.form.get("title") or "").strip()
            body = (request.form.get("body") or "").strip()
            if not title:
                return render_template("form.html", note=note, error="Judul wajib diisi"), 400
            db.update_note(note_id, title, body)
            return redirect(url_for("index"))
        return render_template("form.html", note=note, error=None)

    @app.post("/notes/<int:note_id>/delete")
    def delete_note(note_id: int):
        db.delete_note(note_id)
        return redirect(url_for("index"))

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
