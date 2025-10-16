AI Fortune — Demo README

Purpose

This short demo README explains the core design decisions and deterministic mechanics used in the AI Fortune project. It's written for instructors or reviewers to understand how the system maps a birth date to a reproducible fortune and why certain creative choices were made.

Quick overview

- Project: A small interactive Python program that generates a short fortune (title, verse, category, advice, lucky numbers, color, direction) from a birth date.
- Interfaces: CLI, small Tkinter GUI, and a Flask web UI with a styled Chinese-themed HTML export.
- Primary requirement satisfied: user input (birth date) drives a dynamic, meaningful response.

Determinism: how and why

- Seed derivation: For any input date (YYYY-MM-DD), the program computes SHA-256(date_string) and uses the first 16 hex digits as an integer seed.
- Deterministic RNG: The seed initializes Python's random.Random(seed) instance, which is then used to select a fortune template, lucky numbers, color, and direction.
- Deterministic outputs: Because the seed is purely derived from the input date, the same date always produces the same fortune and the same lucky elements.

Why deterministic?

- Reproducibility: determinism makes the output verifiable by graders and students: the same input -> same output.
- No network dependency: keeps the project self-contained and avoids scraping or external API variability.

Mapping: data -> output

- Title & verse: selected from an internal list of original templates (English translations provided). Templates are intentionally short, poetic, and neutral for cross-cultural readability.
- Score: derived from seed % 100, used to classify into three categories: Great Luck (>=75), Moderate Luck (40-74), Misfortune (<40).
- Advice: short messages composed from category + a secondary message bucketed by score ranges.
- Lucky numbers: five unique numbers sampled from 1..49 using the deterministic RNG.
- Presentation: terminal colored output; optional HTML export (Chinese-style theme) that includes a client-side "Download PNG" button powered by html2canvas.

Creative & pedagogical choices

- Templates: original, concise, and culturally neutral English verses to make the project understandable to international reviewers.
- Chinese-style export: visual theme preserves aesthetic intent (paper texture, ink tones, SVG flourish) but all text labels are in English for accessibility.
- Client-side PNG export: demonstrates end-to-end interactive UX without server-side image rendering.

Running & quick tests (for graders)

- CLI test (example):
  python3 src/main.py --date 1990-01-01 --html --theme china
  - Produces terminal output and writes a file like `src/fortune_1990-01-01_YYYYMMDD_HHMMSS.html`.

- Web UI: (after installing requirements)
  python3 -m pip install -r requirements.txt
  python3 src/app.py
  Open http://127.0.0.1:5000 — enter a date and press the button.

Grading notes

- Reproducibility test: use two or more dates and verify consistent output across runs.
- Unit-testable core: the `generate_fortune(date)` function is deterministic and could be tested with simple assertions (e.g., expected seed, expected category range, fixed lucky numbers for a given date).

Limitations & extensions

- No external "traditional almanac" data is used; if required, an optional scraper module can be added (requires specifying a source and handling terms of use).
- Themes: additional visual themes (ink, gold leaf, rice paper) are straightforward to add as HTML templates.

Contact

If you want an instructor-facing summary or a slide with visuals, I can produce a one-slide PDF or a short video demo of the web UI in action.
