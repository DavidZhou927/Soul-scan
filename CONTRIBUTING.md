Contributing & Upload guide

This file contains quick steps to prepare and push the repository to GitHub, aimed at the project owner.

1. Verify code and tests locally

- Run the web UI and do a quick manual check:
  python3 -m pip install -r requirements.txt
  python3 src/app.py
  Open http://127.0.0.1:5000 and test a few dates.

2. Prepare git

```bash
git add .
git commit -m "Prepare repo for submission"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

3. Optional: create a GitHub release or tag for the submission date.

4. If you prefer Docker-based deployment, ask me and I will add a Dockerfile and instructions.
