from pathlib import Path
import sys
import os
# アプリの設定値を集めたモジュール

# パス解決まわり
def get_base_dir():
    if getattr(sys, 'frozen', False):
        # .exeのあるフォルダ
        return Path(sys.executable).parent
    else:
        # 開発時
        return Path(__file__).resolve().parent
    
BASE_DIR = get_base_dir()
# print(BASE_DIR) # `sql-dojo_release/sql_dojo/`のパスを返す
DATA_DIR = BASE_DIR / "data"
STORAGE_DIR = BASE_DIR / "storage"
TEMPLATE_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

# DB接続まわり
DB_DRIVER = os.getenv("DB_DRIVER")
DB_SERVER = os.getenv("DB_SERVER")
DB_PORT = os.getenv("DB_PORT")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# 結果表示テーブルまわり

# 結果表示テーブルの初期表示
DEFAULT_COLUMNS = ["( ´_ゝ`)", "クエリ未実行"]
DEFAULT_ROWS = [
    ["(･ω･)", "クエリを入力して実行ボタンをクリックしてね！"]
]

# クエリ実行失敗時返却用データ（笑）
FAILED_COLUMNS = ["( ´,_ゝ`)", "ち～ん（笑）"]
FAILED_ROWS = [
    ["残念ｗ", "レコードセットが返らなかったよｗｗｗ"]
]

# CodeMirror関係
DEFAULT_EDITOR_HEIGHT = 300