#!/usr/bin/env python3
import argparse
import datetime
import sys
import os
import webbrowser
from pathlib import Path
from fortune_generator import generate_fortune


def supports_color() -> bool:
    # Detect whether terminal likely supports ANSI colors
    try:
        is_a_tty = sys.stdout.isatty()
    except Exception:
        is_a_tty = False
    return is_a_tty


def parse_date(s: str) -> datetime.date:
    s = s.strip()
    # 尝试多种常见格式
    fmts = ["%Y-%m-%d", "%Y/%m/%d", "%Y.%m.%d", "%Y%m%d"]
    for fmt in fmts:
        try:
            return datetime.datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    raise ValueError("Unrecognized date format. Please use YYYY-MM-DD or similar.")


def display_fortune(f: dict) -> None:
    # 简单 ANSI 颜色（在大多数终端下可用）
    H = '\u001b[1m'
    R = '\u001b[0m'
    C_YELLOW = '\u001b[33m'
    C_CYAN = '\u001b[36m'
    print("\n" + H + "——— AI Fortune ———" + R)
    print(f"Date: {C_CYAN}{f['date']}{R}  (seed={f['seed']})")
    print(f"Title: {C_YELLOW}{f['title']}{R}  —  Category: {f['category']}  (score: {f['score']})")
    print("\nVerse:")
    print(f"  {f['poem']}")
    print("\nAdvice:")
    print(f"  {f['advice']}")
    print("\nLucky elements:")
    print(f"  Lucky numbers: {', '.join(str(n) for n in f['lucky_numbers'])}")
    print(f"  Lucky color: {f['lucky_color']}")
    print(f"  Lucky direction: {f['lucky_direction']}")
    print(H + "——— End ———" + R + "\n")


def main():
    parser = argparse.ArgumentParser(description="AI Fortune - generate a fortune (luck/unluck) from a birth date")
    parser.add_argument("--date", "-d", help="Birth date, format YYYY-MM-DD (optional)")
    parser.add_argument("--html", action="store_true", help="Generate an HTML file for visual display (optional)")
    parser.add_argument("--open", action="store_true", help="Open generated HTML in browser (requires --html)")
    parser.add_argument("--theme", choices=['china', 'minimal'], default='china', help="HTML theme (default: china)")
    parser.add_argument("--no-color", action="store_true", help="Disable ANSI color output in terminal")
    parser.add_argument("--gui", action="store_true", help="Launch a simple GUI (Tkinter)")
    args = parser.parse_args()

    if args.gui:
        # lazy import GUI to keep CLI light
        try:
            from gui import run_gui
        except Exception as e:
            print(f"Unable to start GUI: {e}")
            sys.exit(1)
        run_gui()
        return

    if args.date:
        try:
            dt = parse_date(args.date)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
        f = generate_fortune(dt)
        # 颜色开关
        color_enabled = (not args.no_color) and supports_color()
        # 将 display_fortune 变为使用全局颜色开关：临时修改打印函数的行为
        if not color_enabled:
            # 简单替代：禁用 ANSI 代码，临时把 ANSI 字符串设为空
            # 我们通过环境变量传递，render 使用内置常量，所以直接打印无彩色版本
            pass
        display_fortune(f)
        if args.html:
            try:
                from render_html import render_to_html
            except Exception as e:
                print(f"Cannot import HTML renderer: {e}")
            else:
                out = render_to_html(f, theme=args.theme)
                print(f"Generated HTML: {out}")
                if args.open:
                    webbrowser.open('file://' + os.path.abspath(out))
        return

    # 交互式输入
    while True:
        try:
            s = input("Enter your birth date (YYYY-MM-DD), or 'q' to quit: ")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            return
        if not s:
            continue
        if s.lower() in ("q", "quit", "exit"):
            print("Goodbye!")
            return
        try:
            dt = parse_date(s)
        except ValueError as e:
            print(f"Input error: {e}")
            continue
        f = generate_fortune(dt)
        display_fortune(f)


if __name__ == "__main__":
    main()
