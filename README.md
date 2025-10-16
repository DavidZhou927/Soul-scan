# Soul scan (fortune generator based on birth date)

Let’s be real — stress is piling up more and more these days, so it’s no wonder lots of us turn to fun little things like fortune-telling, tarot cards, or divination to grab a quick dose of comfort. Here’s a tiny, playful interactive Python program that fits right in: just punch in your birth date (for example `1990-01-01`), and it’ll spit out a silly little "fortune" — totally based on that date, no guesswork! You’ll get a category (Great/Moderate/Misfortune), a short cutesy verse, some casual advice, lucky numbers, a lucky color, and even a lucky direction.

Features
- Pure Python (does not rely on external networks or web scraping)
- Deterministic results: same date always yields the same fortune
- Supports interactive input, command line arguments, a simple Tkinter GUI, and a small Flask web UI

Quick start

1. Clone the repository and enter the project folder:

```bash
git clone https://github.com/DavidZhou927/Soul-scan.git
cd "Soul-scan"
```

2. (Recommended) create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies (optional) and run the web UI:

```bash
python3 -m pip install -r requirements.txt
python3 src/app.py
# open http://127.0.0.1:5000 in your browser
```

CLI and GUI

- CLI interactive: `python3 src/main.py`
- CLI one-off: `python3 src/main.py --date 1990-01-01 --html --theme china`
- Simple GUI: `python3 src/main.py --gui`

Web UI / HTML export (detailed)

If you prefer to use a browser interface or want a ready-made HTML export, follow these steps.

1) Start the Flask web app (foreground):

```bash
python3 src/app.py
```

Then open the interface in your browser at:

  http://127.0.0.1:5000

2) Start the Flask app in background (keeps terminal free):

```bash
nohup python3 src/app.py > server.log 2>&1 &
# then optionally: tail -f server.log
```

3) API: request a fortune as JSON (example with curl):

```bash
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"date":"1990-01-01"}' \
  http://127.0.0.1:5000/api/fortune | jq
```

4) Export a styled HTML page (browser or curl):

- Browser: use the web UI and click the export button. The UI will open an export page showing the styled HTML.
- Direct curl (example saves HTML to a file):

```bash
curl -s "http://127.0.0.1:5000/export?date=1990-01-01&theme=china" -o fortune_1990-01-01.html
open fortune_1990-01-01.html
```

Parameters for `/export` (query string):
- `date` — required, format YYYY-MM-DD
- `theme` — optional, e.g. `china` or `minimal`

5) Alternative: generate HTML from the CLI without starting the web server:

```bash
python3 src/main.py --date 1990-01-01 --html --theme china
# output file will be created in the project root (e.g. src/fortune_1990-01-01_<timestamp>.html)
```

Notes and troubleshooting

- If port 5000 is already in use, change the port in `src/app.py` or stop the process using that port.
- On macOS, use `open <file>` to open a generated HTML from the command line.
- If the web page doesn't render styles or the download button, ensure you have an internet connection for the small client-side CDN used by the export (html2canvas). The core API and CLI do not require external networks.

Verify determinism

Run the same command twice with the same date. The output should be identical (same title, verse, lucky numbers, seed).

Files of interest

- `src/fortune_generator.py` — core generator: seed derivation and deterministic RNG usage
- `src/main.py` — CLI entrypoint (interactive and parameter modes)
- `src/app.py` — Flask web UI and export endpoint
- `src/render_html.py` — HTML templates ("china" and "minimal") and export helper
- `src/templates/index.html`, `src/static/app.js` — web UI
- `DEMO_README.md` — short explanation for graders (determinism and creative choices)

License

See `LICENSE` for project licensing (MIT by default).

Contact

If you want the README adapted to a more academic tone for your instructor, I can prepare a one-page summary suitable for submission.

