import os
import sqlite3
from contextlib import contextmanager
from typing import Iterator

DB_PATH = os.environ.get("NOTES_DB", "notes.db")


@contextmanager
def get_conn() -> Iterator[sqlite3.Connection]:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db() -> None:
    with get_conn() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                body TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (datetime('now'))
            )
            """
        )


def list_notes() -> list[sqlite3.Row]:
    with get_conn() as conn:
        return conn.execute(
            "SELECT id, title, body, created_at FROM notes ORDER BY id DESC"
        ).fetchall()


def get_note(note_id: int) -> sqlite3.Row | None:
    with get_conn() as conn:
        return conn.execute(
            "SELECT id, title, body, created_at FROM notes WHERE id = ?", (note_id,)
        ).fetchone()


def create_note(title: str, body: str) -> int:
    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO notes (title, body) VALUES (?, ?)", (title, body)
        )
        return cur.lastrowid


def update_note(note_id: int, title: str, body: str) -> None:
    with get_conn() as conn:
        conn.execute(
            "UPDATE notes SET title = ?, body = ? WHERE id = ?", (title, body, note_id)
        )


def delete_note(note_id: int) -> None:
    with get_conn() as conn:
        conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
