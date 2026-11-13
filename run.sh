#!/usr/bin/env bash
# Mac/Linux: creates a virtual environment on first run, then starts IEP Assist at http://localhost:8080
cd "$(dirname "$0")"
[ -d .venv ] || { python3 -m venv .venv && .venv/bin/pip install -r requirements.txt --quiet; }
.venv/bin/python main.py
