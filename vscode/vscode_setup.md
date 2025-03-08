# VSCode Setup


## 目次
----------------------------------------
- [目次](#目次)
- [VSCodeインストール手順](#vscodeインストール手順)
- [インストールする拡張機能](#インストールする拡張機能)
- [詳細設定](#詳細設定)
- [拡張機能の信頼性チェック項目](#拡張機能の信頼性チェック項目)
- [参考文献](#参考文献)


## VSCodeインストール手順
----------------------------------------
- 以下のサイトでVSCodeのインストーラをインストールする。  
    [Download Visual Studio Code](https://code.visualstudio.com/Download)  
    ※User Installer(ログインユーザにのみインストール)を選択する。  
    ※220702時点のインストーラ：VSCodeUserSetup-x64-1.68.1.exe
- インストーラをダブルクリックして実行する。
- 「使用許諾契約書の同意」→「同意する」→「次へ」
- 「インストール先の指定」→デフォルト(以下)のまま「次へ」  
    `C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code`
- 「スタートメニューフォルダーの指定」→デフォルトのまま「次へ」
- 「追加タスクの選択」→以下の項目にのみチェックを入れて、「次へ」
    - エクスプローラーのファイルコンテキスト メニューに「Codeで開く」アクションを追加する
    - エクスプローラーのディレクトリコンテキスト メニューに「Codeで開く」アクションを追加する
    - PATHへの追加
- 「インストール準備完了」→「インストール」
- 「Visual Studio Codeセットアップウィザードの完了」→「完了」


## インストールする拡張機能
----------------------------------------
### C
- [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [詳細設定](#cc設定)

### Makefile
- [Makefile Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.makefile-tools)

### Python
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [詳細設定](#python設定)

### Markdown
- 基本機能: [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- 図の作成: [Markdown Preview Mermaid Support](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)
- プレビュー: デフォルトのプレビュー機能を使用
- PDF化: [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf)
- [詳細設定](#markdown設定)

### HTML
- [HTML CSS Support](https://marketplace.visualstudio.com/items?itemName=ecmel.vscode-html-css)


## 詳細設定
----------------------------------------
### 設定の優先順位
-  Folder -> Workspace -> Userの順で設定が優先される(Userが最優先)。

### 共通設定
- editor.fontSize -> 13
- editor.fontFamily -> Consolas, monospace
- editor.tabSize -> 4
- editor.renderWhitespace -> All
- editor.showUnused -> Uncheck
- terminal.integrated.defaultProfile.windows -> Command Prompt

### ユーザスニペット
- `File -> Preference -> Configure User Snippets` でファイル種別ごとのスニペット(テキストフォーマット)を設定。
- 任意のファイルで使用できるスニペットは`New Global Snippets file...`で作成する。
- 作成済みのユーザスニペットは`Existing Snippets`と表示される。
- 例：Numpy形式のdocstringの定義。`_dc`と入力すると候補に出るので、`Enter`で置き換わる ($0：最終カーソル位置) 。
```json
"np_docstring": {
    "prefix": "_dc",
    "body": [
        "$0\"\"\"brief discription.\n",
        "main discription.\n",
        "Parameters",
        "----------",
        "val : type",
        "\tdiscription.\n",
        "Returns",
        "-------",
        "val : type",
        "\tdiscription.\n",
        "Notes",
        "-----",
        "- supplement\n",
        "\"\"\""
    ],
    "description": "numpy docstring"
}
```

### C/C++設定
- ワークスペースを開く
- 「Ctrl + Shift +P」 でコマンドパレットを開く
- 「C/Cpp: Edit Configurations (JSON)」を選択する
- 「.vscode\c_cpp_properties.json」が作成される
    - .vscodeが存在しない場合はプロジェクト直下に生成される

### Python設定
#### インタプリタの設定
- Anaconda Promptを開き、以下のコマンドを入力し、Python実行環境のパスを取得する。
    ``````````````powershell
    >conda info -e
    ``````````````
- python.defaultInterpreterPath -> 上記で取得したパス。
#### VSCodeから実行できるようにするための設定
- Anaconde Promptを起動し、以下のコマンドを入力する。
    ``````````````````````powershell
    >conda init powershell
    ``````````````````````
- Windows PowerShellを「管理者として実行」し、以下のコマンドを入力する。
    ``````````````````````````````````powershell
    >Set-ExecutionPolicy RemoteSigned
    ``````````````````````````````````
- **TODO**: 本コマンドの影響を確認する。

### Markdown設定
#### Markdown共通設定
- 自動改行を無効化する。(他環境でも共通した表示にするため)
    - markdown.preview.breaks -> Uncheck
#### Markdown All in One設定
- 現在のタブ幅を継承するようにする。
    - markdown.extension.list.indentationSize -> inherit
- 自動プレビュー表示を無効化する。
    - markdown.extension.preview.autoShowPreviewToSide -> Uncheck
- 目次の自動更新
    - markdown.extension.toc.updateOnSave -> Uncheck
- 目次化する見出しレベルをh2タグのみとする。
    - markdown.extension.toc.levels -> 2..2
#### Markdown PDF設定
- 自動改行を無効化する。(他環境でも共通した表示にするため)
    - markdown-pdf.breaks -> Uncheck
- ヘッダーにMarkdownファイル名と日付を表示しないようにする。
    - markdown-pdf.headerTemplate -> `<div></div>`
- 常にMarkdownファイルと同じディレクトリに出力する。
    - markdown-pdf.outputDirectoryRelativePathFile -> Check
- 余白を調整する。
    - markdown-pdf.margin.top -> お好み
    - markdown-pdf.margin.bottom -> お好み
    - markdown-pdf.margin.right -> お好み
    - markdown-pdf.margin.left -> お好み


## 拡張機能の信頼性チェック項目
----------------------------------------
- ネット上に否定的な意見がないか。
- 作者名にバッジがついているか(Visual Studio Marketplaceによって認証されているか)。
    - [Verified extension publishers](https://code.visualstudio.com/updates/v1_62#_verified-extension-publishers)
- インストール数が十分に多いか。
- ChangelogとIssues/Pull Requestsが紐づいているか。
- ユーザーからのレーティングが低くないか。
- ユーザーの否定的レビューにセキュリティ関連の指摘がないか。
- GithubリポジトリのContributorsが複数人か。
- Githubリポジトリのスターが十分多いか。
- 作者のGithubアカウントに評価に見合ったバッジがついているか。
- IssuesおよびPull Requestsが長期間放置されていないか。
    - 放置されている場合、放置されている理由等がコメントされているか。


## 参考文献
----------------------------------------
- [Visual Studio Code Docs](https://code.visualstudio.com/docs) ・・・公式ドキュメント
