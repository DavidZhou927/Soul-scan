from flask import Flask, request, jsonify, render_template, abort, Response
from fortune_generator import generate_fortune
from render_html import render_to_html
import datetime

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/fortune', methods=['POST'])
def api_fortune():
    data = request.get_json() or {}
    date_str = data.get('date')
    if not date_str:
        return jsonify({'error': '缺少 date 字段，格式 YYYY-MM-DD'}), 400
    try:
        dt = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    except Exception:
        return jsonify({'error': '日期解析失败，请使用 YYYY-MM-DD'}), 400
    f = generate_fortune(dt)
    return jsonify(f)

@app.route('/export')
def export_html():
    date_str = request.args.get('date')
    theme = request.args.get('theme', 'china')
    if not date_str:
        return abort(400, '缺少 date 参数')
    try:
        dt = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    except Exception:
        return abort(400, '日期解析失败，请使用 YYYY-MM-DD')
    f = generate_fortune(dt)
    html = render_to_html(f, theme=theme)
    # 返回 HTML 内容直接展示（读取文件并返回）
    with open(html, 'r', encoding='utf-8') as fh:
        content = fh.read()
    return Response(content, mimetype='text/html')

if __name__ == '__main__':
    # 运行开发服务器
    app.run(host='127.0.0.1', port=5000)
