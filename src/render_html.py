from typing import Dict
from pathlib import Path

_HTML_TMPL = {
    'china': '''<!doctype html>
<html lang="zh-CN">
  <html lang="en">
<head>
  <meta charset="utf-8" />
  <title>AI 占卜签 - {title}</title>
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;700&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: 'Noto Serif SC', serif; background: radial-gradient(circle at 10% 10%, #fff7ed, #f6f8fb); color:#222; padding:30px; }}
    .card {{ max-width:780px; margin:18px auto; background:linear-gradient(180deg, rgba(255,255,255,0.95), rgba(255,250,245,0.9)); border-radius:14px; padding:22px; box-shadow:0 18px 40px rgba(18,20,30,0.06); border:1px solid rgba(180,150,120,0.06); }}
    .title {{ font-size:1.8rem; font-weight:700; color:#a94b2a; letter-spacing:0.6px; }}
    .meta {{ color:#6b6b6b; margin-top:6px; font-size:0.95rem; }}
    .poem {{ margin-top:18px; font-size:1.2rem; line-height:1.9; color:#2b3a42; padding:18px; border-radius:8px; background:linear-gradient(90deg, rgba(250,245,240,0.6), rgba(255,255,255,0.4)); border-left:6px solid rgba(170,120,80,0.14); }}
    .advice {{ margin-top:14px; padding:12px; border-radius:10px; background:rgba(255,250,240,0.7); color:#3d3d3d; border:1px dashed rgba(200,160,120,0.08); }}
    .lucky {{ margin-top:14px; display:flex; gap:10px; flex-wrap:wrap; }}
    .badge {{ padding:8px 12px; background:rgba(255,255,255,0.95); border-radius:999px; box-shadow:0 6px 18px rgba(30,30,50,0.06); border:1px solid rgba(220,200,180,0.12); }}
    .footer {{ margin-top:16px; color:#888; font-size:0.9rem; }}
    .svg-deco {{ width:100%; height:140px; display:block; margin-bottom:6px; }}
    .toolbar {{ margin-top:12px; display:flex; gap:8px; }}
    .btn {{ padding:8px 12px; background:#a94b2a; color:#fff; border-radius:8px; text-decoration:none; font-weight:600; }}
  </style>
</head>
<body>
  <div class="card" id="card">
    <svg class="svg-deco" viewBox="0 0 900 140" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
      <rect width="900" height="140" fill="#fff8f1" />
      <g>
        <path d="M0 120 C150 20 300 140 450 70 C600 10 750 120 900 60" stroke="#e6cbb3" stroke-width="2.8" fill="none"/>
      </g>
      <text x="40" y="88" fill="#7a3520" font-size="28" font-family="serif">{title}</text>
      <circle cx="820" cy="40" r="28" fill="#f2e7da" stroke="#e0c9b0" />
      <text x="808" y="46" fill="#b85c2a" font-size="18" font-family="serif">签</text>
    </svg>

    <div class="title">{title} <span style="font-weight:400; font-size:0.95rem; color:#6b6b6b">— {category} (分数 {score})</span></div>
      <div class="meta">Birth date: {date} · Seed: {seed}</div>
    <div class="poem">{poem}</div>
      <div class="advice">Advice: {advice}</div>

    <div class="lucky">
        <div class="badge">Lucky numbers: {lucky_numbers}</div>
        <div class="badge">Lucky color: {lucky_color}</div>
        <div class="badge">Lucky direction: {lucky_direction}</div>
    </div>

    <div class="toolbar">
        <a class="btn" id="downloadBtn" href="#">Download PNG</a>
      <a class="btn" href="#" onclick="window.print();return false;">打印</a>
    </div>

      <div class="footer">Generated locally — AI Fortune · For entertainment only</div>
  </div>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
  <script>
    const btn = document.getElementById('downloadBtn');
    btn.addEventListener('click', function (e) {{
      e.preventDefault();
      html2canvas(document.getElementById('card'), {{ scale: 2 }}).then(canvas => {{
        const a = document.createElement('a');
        a.href = canvas.toDataURL('image/png');
        a.download = 'fortune_{date}.png';
        a.click();
      }});
    }});
  </script>
</body>
</html>
''',

    'minimal': '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Fortune - {title}</title>
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <style>
    body {{ font-family: system-ui, sans-serif; background:#fafafa; color:#111; padding:20px; }}
    .card {{ max-width:680px; margin:12px auto; background:#fff; padding:18px; border-radius:8px; box-shadow:0 6px 20px rgba(10,10,20,0.06); }}
    .title {{ font-size:1.4rem; font-weight:700; color:#222; }}
    .poem {{ margin-top:12px; font-size:1.05rem; color:#333; }}
    .lucky {{ margin-top:12px; }}
  </style>
</head>
<body>
  <div class="card" id="card">
    <div class="title">{title} — {category} (score {score})</div>
    <div class="meta">date: {date} · seed: {seed}</div>
    <div class="poem">{poem}</div>
    <div class="advice">{advice}</div>
    <div class="lucky">Lucky: {lucky_numbers} · {lucky_color} · {lucky_direction}</div>
  </div>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
  <script>
    // minimal has no download button by default
  </script>
</body>
</html>
'''
}


def render_to_html(f: Dict, theme: str = 'china') -> str:
  """将签文渲染为 HTML 并写入到 src/fortune_<date>_<ts>.html，返回文件路径字符串。
  支持主题：'china'（中国风），'minimal'（简洁）。
  """
  import datetime
  ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
  out_dir = Path(__file__).resolve().parent
  out_path = out_dir / f"fortune_{f['date']}_{ts}.html"
  tmpl = _HTML_TMPL.get(theme, _HTML_TMPL['china'])
  html = tmpl.format(
    title=f.get('title', '占卜签'),
    category=f.get('category', ''),
    score=f.get('score', ''),
    date=f.get('date', ''),
    seed=f.get('seed', ''),
    poem=f.get('poem', ''),
    advice=f.get('advice', ''),
    lucky_numbers=', '.join(str(n) for n in f.get('lucky_numbers', [])),
    lucky_color=f.get('lucky_color', ''),
    lucky_direction=f.get('lucky_direction', '')
  )
  out_path.write_text(html, encoding='utf-8')
  return str(out_path)
