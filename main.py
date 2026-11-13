"""IEP Assist (Python edition) — run with:  python main.py   then open http://localhost:8080"""
import os
import secrets
from pathlib import Path

from nicegui import ui

from iep_assist.ui import page_iep, pages_info, pages_main  # noqa: F401  (importing registers the pages)

if __name__ in {'__main__', '__mp_main__'}:
    secret_file = Path('data/.storage_secret')
    secret_file.parent.mkdir(exist_ok=True)
    if not secret_file.exists():
        secret_file.write_text(secrets.token_hex(32))
    ui.run(title='IEP Assist (research prototype)', storage_secret=secret_file.read_text(), port=int(os.environ.get('PORT', 8080)),
           reload=False, show=False, favicon='📘')
