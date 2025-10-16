document.addEventListener('DOMContentLoaded', function () {
  const btn = document.getElementById('btn');
  const dateInput = document.getElementById('date');
  const result = document.getElementById('result');
  const theme = document.getElementById('theme');

  btn.addEventListener('click', async () => {
    const d = dateInput.value.trim();
    if (!d) {
      alert('Please enter a date');
      return;
    }
    result.style.display = 'block';
    result.innerText = '占卜中...';
    try {
      const resp = await fetch('/api/fortune', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ date: d })
      });
      if (!resp.ok) {
        const err = await resp.json();
        result.innerText = 'Error: ' + (err.error || resp.statusText);
        return;
      }
      const data = await resp.json();
      // 显示结果
      result.innerHTML = `<div class="meta">Date: ${data.date} · Category: ${data.category} (score ${data.score})</div>` +
                         `<div class="poem">${data.poem}</div>` +
                         `<div style="margin-top:8px;">Advice: ${data.advice}</div>` +
                         `<div style="margin-top:8px;">Lucky numbers: ${data.lucky_numbers.join(', ')}</div>`;
      // export link
      const exportUrl = `/export?date=${encodeURIComponent(data.date)}&theme=${encodeURIComponent(theme.value)}`;
      const controls = document.createElement('div');
      controls.className = 'controls';
      const a = document.createElement('a');
      a.href = exportUrl;
      a.target = '_blank';
      a.innerText = 'Open styled page';
      controls.appendChild(a);
      result.appendChild(controls);
    } catch (e) {
      result.innerText = '请求失败: ' + e;
    }
  });
});
