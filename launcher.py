import subprocess
import tkinter as tk
import os
import signal
from pathlib import Path

import sys

def resource_path(relative_path):
    # PyInstaller
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent / relative_path
    # スクリプト実行時
    return Path(__file__).resolve().parent / relative_path

# 設定
# 同階層にある`sql_dojo.exe`のパス
APP_EXECUTABLE = resource_path("sql_dojo.exe")

flask_process = None

def start_app():
    global flask_process

    exe_path = str(APP_EXECUTABLE)
    print("APP_EXECUTABLE =", exe_path)

    # Flaskアプリをサブプロセスとして起動
    flask_process = subprocess.Popen(
        [exe_path], 
        stdout=subprocess.DEVNULL, 
        stderr=subprocess.DEVNULL
    )
    label_status.config(text="( ´,_ゝ`) < お笑いSQL道場 起動中ｗｗｗ")


def stop_app():
    if flask_process:
        try:
            flask_process.terminate()
        except:
            pass
    root.destroy()

# GUI
root = tk.Tk()
root.title("🚀お笑いSQL道場 Launcher")
root.geometry("320x130")

label_status = tk.Label(
    root, 
    text="( ´,_ゝ`) < 起動していないｗｗｗ", 
    font=("Yu Gothic UI", 12))

label_status.pack(pady=10)

btn_quit = tk.Button(
    root, 
    text="糸冬 了", 
    font=("Yu Gothic UI", 12), 
    command=stop_app)
btn_quit.pack(pady=5)

# 起動後即Flaskアプリを開始
root.after(200, start_app)

root.mainloop()
