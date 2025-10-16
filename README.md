<<<<<<< HEAD
# Soul-scan
This is a Python-based fortune generator that creates deterministic results (including fortune categories, verses, and lucky numbers) from a birth date, accessible via CLI, GUI, or a Flask web interface with HTML export support.
=======

# AI Fortune (fortune generator based on birth date)

This is a small interactive Python program. Enter a birth date (for example `1990-01-01`) and the program will deterministically produce a short "fortune" based on that date, including a category (Great/Moderate/Misfortune), a short verse, advice, lucky numbers, a lucky color and direction.

Features:
- Pure Python (does not rely on external networks or web scraping)
- Deterministic results: same date always yields the same fortune
- Supports interactive input and command line arguments

How to run

1. Use a Python 3.8+ environment (macOS comes with Python3 by default, or use pyenv/venv).

2. From the project root (where `src/` is located):

```bash
cd /path/to/repo
python3 src/main.py
```

3. Or generate directly with a date argument:

```bash
# AI Fortune

A small, self-contained Python project that deterministically generates a short "fortune" from a user's birth date. The project includes a command-line interface, an optional Tkinter GUI, and a small Flask web UI with a styled export page.

This top-level README is grader-friendly and explains how to run and verify the project quickly.

Quick Start

1. Clone the repository and enter the project folder:

```bash
git clone <your-repo-url>
cd <repo-folder>
```

2. (Recommended) create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies and run the web UI:

```bash
python3 -m pip install -r requirements.txt
python3 src/app.py
# open http://127.0.0.1:5000 in your browser
```

CLI and GUI

- CLI interactive: `python3 src/main.py`
- CLI one-off: `python3 src/main.py --date 1990-01-01 --html --theme china`
- Simple GUI: `python3 src/main.py --gui`

Verify determinism

Run the same command twice with the same date. The output should be identical (same title, verse, lucky numbers, seed).

Files of interest

- `src/fortune_generator.py` — core generator: seed derivation and deterministic RNG usage
- `src/main.py` — CLI entrypoint (interactive and parameter modes)
- `src/app.py` — Flask web UI and export endpoint
- `src/render_html.py` — HTML templates ("china" and "minimal") and export helper
- `src/templates/index.html`, `src/static/app.js` — web UI
- `DEMO_README.md` — short explanation for graders (determinism and creative choices)

Ready for GitHub

When you're ready to upload:

```bash
git add .
git commit -m "Add AI Fortune project"
git branch -M main
git remote add origin <your-github-url>
git push -u origin main
```

If you want, I can also add a `Dockerfile` or a short deployment guide for hosting (Render/Heroku/etc.).

License

See `LICENSE` for project licensing (MIT by default).

Contact

If you want the README adapted to a more academic tone for your instructor, I can prepare a one-page summary suitable for submission.
>>>>>>> 828ffbd (Add AI Fortune project: CLI, web UI, templates and docs)
