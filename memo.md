# 「お笑いSQL道場」プロジェクトのメモ
## リモートリポジトリにpushするとき
1. 必要な変更をコミット
2. リモートリポジトリのURLを`origin`に登録
    - `git remote add origin https://github.com/KeirinTarou/sql_dojo.git`
3. リモート追跡ブランチを作成する
    - `git push --set-upstream origin main`
        - git push --set-upstream <remote-branch-alias> <local-branch>
        - ローカルリポジトリに`origin/main`というリモート追跡ブランチが登録される
        - リモート追跡ブランチは、push、pullした時点でのリモートリポジトリの状態をローカルリポジトリに残しておくしくみ
            - 次回push、pullする際に、リモート追跡ブランチとの差分を利用する


## リモートリポジトリからpullするとき
1. プロジェクトルートディレクトリを用意する
    - アプリルートの1階層上のフォルダ
        - たとえば、元プロジェクトが次の構成の場合
            ```bash
            sql_dojo_release/
                sql_dojo/
                    .git/
                    dbapp.py
                venv/
            ```
        - リモートリポジトリの内容は`sql_dojo`ディレクトリ以下
        - pullする端末で`sql_dojo_release`ディレクトリに相当するディレクトリを作成する
    - `venv`をGit管理下に含めないようにするため
2. git-bashを開き、プロジェクトルートディレクトリをカレントディレクトリにする
    - 例: `cd C:/Users/seoo_/Downloads/distribution/sql_dojo_release`
3. `git clone https://github.com/KeirinTarou/sql_dojo.git sql_dojo`コマンド実行
    - カレントディレクトリに、リモートリポジトリの内容が`sql_dojo`フォルダ内に展開される
4. Python仮想環境作成
    - `python -m venv venv`コマンド実行
    - `venv\Scripts\activate`で仮想環境を有効化
5. 必要なモジュール・パッケージをインストール
    - `pip install -r sql_dojo\requirements.txt`コマンド実行
6. `.gitignore`に登録していた必要ファイルをコピー
    - 主なものは以下の通り
        - `sql_dojo`フォルダ: `.env`
        - `data`フォルダ: `practice.db`
        - `db`フォルダ: `source.xlsm`
        - `static/js`フォルダ: `jquery-3.7.1.min.js`

## `sql_dojo`を`.exe`ファイル化する
- 次のようなフォルダ構成になっている前提
- また、ビルド後の`sql_dojo.exe`と`launcher.exe`は同一フォルダ階層にある前提

```bash
sql_dojo_release/
    img/
        ba-90.ico
    sql_dojo/
        dbapp.py
        launcher.py
    venv/
```
- `sql_dojo.exe`ビルド後、`sql_dojo.exe`、`_internal`、`img`フォルダをインストールフォルダに移動する
- インストールフォルダの構成は次のとおり
```bash
sql_dojo/
    _internal/
    data/
    img/
        ba-90.ico
    static/
    storage/
    templates/
    .env
    sql_dojo.exe
    launcher.exe
```
`config.py`、`data`、`services`は

### コンソール表示ありで起動する
- `sql-dojo_release`フォルダをカレントディレクトリにして実行
```
pyinstaller --name sql_dojo --icon "img\ba-90.ico" --console "sql_dojo\dbapp.py"
```

### コンソール表示なしで起動する
- `sql-dojo_release`フォルダをカレントディレクトリにして実行
```
pyinstaller --name sql_dojo --icon "img\ba-90.ico" --noconsole --add-data "db\squat_data.db;db" "sql_dojo\dbapp.py"
```
- SQLite対応でコマンド変更

### ランチャーの`.exe`化
- `sql-dojo_release`フォルダをカレントディレクトリにして実行
```
pyinstaller --noconsole --onefile --add-data "img\ba-90.ico;img" sql_dojo\launcher.py --icon=img\ba-90.ico
```
# 参考
## PyInstallerについて
- [pyinstaller.org](https://pyinstaller.org/en/stable/)より

### PyInstallerコマンドリファレンス
#### 基本構文
```bash
pyinstaller [options] script [script ...] | specfile
```
- `script`は相対パス使用可
    - 最もシンプルなコマンドは次のとおり
        ```bash
        # カレントディレクトリで実行
        pyinstaller foo.py
        ```
    - `.spec`ファイルを使用する場合は次のとおり
        ```bash
        pyinstaller foo.spec
        ```

#### PyInstallerの動き
- `foo.py`の分析
- `foo.spec`ファイル生成（同一フォルダ）
- `build`フォルダ生成
- `build`フォルダ内に諸ファイルを生成
- `dist`フォルダ生成
- `dist`フォルダ内に`foo`フォルダ（実行可能ファイル入り）を生成

#### コマンドラインオプション
- `pyinstaller`コマンドそのもののオプション
    - `--distpath DIR`
        - バンドルしたアプリをどこに配置するか
        - デフォルトは`build`
    - `workpath WORKPATH`
        - ビルド時の一時ファイルをどこで展開するか
        - デフォルトは`dist`
    - `-y`, `--noconfirm`
        - ビルド時、`dist`フォルダが既に存在するときの、上書き確認メッセージを抑制する
    - `-c`, `--console`, `--nowindowed`
        - アプリ起動時にコンソールを表示する
        - ウィンドウアプリでなく、コンソールアプリということ
    - `-w`, `--windowed`, `--noconsole`
        - アプリ起動時にコンソールを表示しない
        - コンソールモードではなく、ウィンドウアプリということ
- 〝固め方〟を指定するオプション
    - `-D`, `--onedir`
        - one-folder-bundledモード（デフォルト）
    - `-F`, `--onefile`
        - one-file-bundledモード
    - `specpath DIR`
        - `.spec`ファイルを作るディレクトリ
        - デフォルトはカレントディレクトリ
    - `-n`, `--name NAME`
        - アプリ、`.spec`ファイルの名前
        - デフォルトは1つ目のスクリプトのファイルベースネーム
    - `--contents-directory CONTENTS_DIRECTORY`
        - one-folder-bundledモードのときのみ
        - ビルド時に生えてくる依存ファイル・フォルダ格納用フォルダ（デフォルトは`_internal`）の名前
        - `CONTENTS_DIRECTORY`に`.`を指定すると、すべて`.exe`と同階層に展開する
- 〝固める対象〟に関するオプション
    - `--add-data SOURCE:DEST`
        - `.exe`に固め込むファイル・フォルダを指定する
        - `DIST`は、アプリのトップレベルディレクトリからの相対パスで指定
        - Pythonスクリプト内で`import`の対象になっているモジュール・パッケージは指定不要
        - データファイルの類を`.exe`内に固め込みたいときに使うのが基本
        - 動的に`import`するようなモジュール・パッケージなど、PyInstallerによる自動収集の対象でないものもあり得るので、その都度確認する必要あり
    - `--add-binary SOURCE:DEST`
        - `--add-data`オプションのバイナリファイル版
    - `-p`, `--paths DIR`
        - エントリポイントであるPythonスクリプトがあるディレクトリ（＝トップレベルディレクトリ）の配下にないファイル・フォルダを固めたいとき、そのパスを指定する
        - 探す場所さえ教えたらPyInstallerが自動で追加してくれるファイル・フォルダが対象
    - `--hidden-import`, `--hiddenimport MODULENAME`
        - PyInstallが自動で追加してくれないモジュールを指定する




### PyInstallerがやっていること
- Analysis: 
    - プログラムが必要としているファイル（依存ファイル）の分析
        - ソースファイル内の`import`文に注目して必要なモジュール・ライブラリのリストを作る
        - PyInstallerが検知できないタイプの依存ファイルがあるときは、明示的にバインドする必要がある
        - PyInstallerに依存ファイルについて知らせるには、次の方法がある
            - `pyinstaller`コマンドのコマンドライン引数で渡す
            - import用のパスを、`pyinstaller`コマンドのコマンドライン引数で渡す
            - 初回ビルド時に生成される`.spec`ファイルを編集する
            - 依存パッケージ用のフックファイルを作成する
        - 特定のデータファイルにアクセスする必要のあるアプリである場合、そのデータファイルをバインドすることも可能。
            - `.spec`ファイルを編集することで可能となる
        - アプリをPythonから実行する場合（Pythonスクリプトとして実行する場合）と、`.exe`ファイルから実行する場合では、依存ファイルへのパス解決方式が異なるので、その点への配慮が必要
            - 典型的には下記のような解決方法をとる
                - one-file-bundleで`.exe`化したとき
                    ```py
                    if getattr(sys, 'frozen', False):
                        return Path(sys._MEIPASS) / relative_path
                    return Path(__file__).parent / relative_patn
                    ```
                - one-folder-bundleで`.exe`化したとき
                    ```py
                    if getattr(sys, 'frozen', False):
                        return Path(sys.executable).parent / relative_path
                    return return Path(__file__).parent / relative_path
                    ```
        - OSが持っていることがわかっているライブラリは、`.exe`の中には含めない

## `_MEIPPASS`について
- Main Executable Imageの略らしい
- one-file bundleの`.exe`ファイルは、実行時に一旦`C:\Users\<user_name>\AppData\Local\Temp\_MEIxxxx`のようなパスの一時ディレクトリを作成し、その中にファイルを展開する
- この一時ファイル`_MEIxxxx`を取得するためのPythonの変数が`sys._MEIPASS`である
