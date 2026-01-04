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
    db/
    img/
        ba-90.ico
    services/
    static/
    storage/
    templates/
    .env
    sql_dojo.exe
    launcher.exe
```

### コンソール表示ありで起動する
- `sql-dojo_release`フォルダをカレントディレクトリにして実行
```
pyinstaller --name sql_dojo --icon "img\ba-90.ico" --console "sql_dojo\dbapp.py"
```

### コンソール表示なしで起動する
- `sql-dojo_release`フォルダをカレントディレクトリにして実行
```
pyinstaller --name sql_dojo --icon "img\ba-90.ico" --noconsole "sql_dojo\dbapp.py"
```

### ランチャーの`.exe`化
- `sql-dojo_release`フォルダをカレントディレクトリにして実行
```
pyinstaller --noconsole --onefile --add-data "img\ba-90.ico;img" sql_dojo\launcher.py --icon=img\ba-90.ico
```