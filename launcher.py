import subprocess
import tkinter as tk
import os
import signal
from pathlib import Path

import sys

def resource_path(relative_path: str | Path) -> Path:
    # PyInstallerで作った.exeによる実行時
    #   .exeファイルによる実行の場合、sys.frozen属性が存在する
    #   sys.frozen属性が存在したら、getattr(sys, "frozen")が
    #   何らかの値を返すので条件式がTrueになり、存在しなかったら
    #   デフォルト値のFalseを返すので条件式がFalseになる
    if getattr(sys, "frozen", False):
        # sys.executableは実行ファイルのフルパス
        #   -> 実行ファイルの親ディレクトリにrelative_pathを連結
        #   * sys.executableは絶対パスを返すことが保障されている
        #       ->resolve()メソッド不要
        return Path(sys.executable).parent / relative_path
    # スクリプト実行時
    #   -> このファイルの親ディレクトリにrelative_pathを連結
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

# [x]クリック時の動作 -> stop_app()に差し替え
root.protocol("WM_DELETE_WINDOW", stop_app)


# アイコン設定
ICON_PATH = resource_path("img/ba-90.ico")
root.iconbitmap(str(ICON_PATH))

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
