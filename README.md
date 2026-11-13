The central idea behind the project is to develop a technology-based solution that makes the IEP development process faster, more efficient, individualized, and professionally manageable, while maintaining human oversight, learner privacy, fairness, and the quality of educational planning for learners with special needs in primary schools. This version also makes one important academic distinction: the AI should generate a professional-reviewable draft, rather than independently deciding what a child needs. There will be need for a programmer to handle the backend of the AI based IEP Generator.
# IEP Assist — Python edition (research prototype)

Pure-Python version of IEP Assist: **front end and back end are both Python**.
Fictional data only. No legal compliance and no organisational endorsement is claimed.

| Layer | Technology |
|---|---|
| UI / UX | NiceGUI (Python; renders a responsive web UI in the browser) |
| Backend | Python modules, SQLite database, PBKDF2-hashed passwords, server-side sessions |
| Generator | Rule-based mock AI (`iep_assist/generator.py`) behind an `IEPGeneratorService` interface |
| Exports | PDF (reportlab), Word (python-docx), plain text |

## Run it
1. Install Python 3.10 or newer from python.org.
2. Windows: double-click `run.bat`. Mac/Linux: run `./run.sh`.
   (Or manually: `pip install -r requirements.txt` then `python main.py`.)
3. Open http://localhost:8080 and sign in with a demo account (password `demo-password`):
   - `teacher@demo.school` — own IEPs, can edit
   - `coordinator@demo.school` — all IEPs, can edit
   - `leader@demo.school` — all IEPs, view only

## Test it
    pytest -q tests/test_backend.py          # 16 backend tests incl. the 7 scenarios
    python tests/e2e_browser.py              # drives the real UI in Chromium (app must be running on PORT=8099)

## Where to look for gaps
- `iep_assist/generator.py`   evidence-matching and generation (mock AI)
- `iep_assist/catalogue.py`   keyword patterns, goal structures, accommodations, strategies
- `iep_assist/patterns.py`    wording patterns for needs, strengths, baselines
- `iep_assist/goal_quality.py`, `validation.py`   goal checks and form rules
- `iep_assist/scenarios.py`, `scenario_data.py`   seven fictional test cases
- `iep_assist/storage.py`     SQLite, login, roles, audit log (replace for production)
- `iep_assist/ui/`            pages and reusable components

## Changing the look
Settings > Appearance in the app (palettes, colours, app name, text size), or the CSS block in `iep_assist/ui/theme.py`.

## Plugging in a real AI model later
Implement `IEPGeneratorService.generate(learner, **opts) -> dict` and keep the evidence-only rules:
no baselines, scores, diagnoses or family information may be invented.
