# Github Setup


# 目次
- [Githubアカウントの作成](#githubアカウントの作成)
- [Githubアカウントの設定](#githubアカウントの設定)
- [リポジトリの新規作成](#リポジトリの新規作成)
- [プライベートリポジトリへユーザを招待する](#プライベートリポジトリへユーザを招待する)
- [リポジトリの削除](#リポジトリの削除)


## Githubアカウントの作成
----------------------------------------
- [Github](https://github.com/)にアクセスし、`Sign up`をクリックする。
- `email`、`password`、`username`を登録する。
- 登録したメールアドレスに認証コードが届くので、認証する。
- How many team members will be working with you? -> Just me
- Are you a student or teacher? -> 選択なし
- What specific features are you interested in using? -> 選択なし
- Continue for free -> アカウントが作成される


## Githubアカウントの設定
----------------------------------------
- Settings
    - Public profile
        - Contributions & Activity
            - Include private contributions on my profile -> Check -> Update preferences
    - Appearance
        - Tab size preference -> 4
    - Emails
        - Keep my email addresses private -> Check
        - Block command line pushes that expose my email -> Check


## リポジトリの新規作成
----------------------------------------
### プライベートリポジトリの作成
- `Repositories` -> `New`をクリックし、任意の新規リポジトリ(Private)を作成する。
- リポジトリの設定が以下となっていることを確認する。
    - Collaborators
        - PRIVATE REPOSITORY -> Yes
        - DIRECT ACCESS -> 0
        - Manage access -> None
    - Code security and analysis (Default設定)
        - All disable

### パブリックリポジトリの作成
- `Repositories` -> `New`をクリックし、任意の新規リポジトリ(Public)を作成する。
- - リポジトリの設定が以下となっていることを確認する。
    - Collaborators
        - PUBLIC REPOSITORY -> Yes
        - DIRECT ACCESS -> 0
        - Manage access -> None
    - Branches -> Add branch protection rule
        - Branch name pattern -> 保護対象ブランチ名
        - Require a pull request before merging -> Check
            - Require approvals -> Check & 1
            - Dismiss stale pull request approvals when new commits are pushed -> Check
            - Require approval of the most recent push -> Check
            - Require conversation resolution before merging -> Check
            - それ以外 -> Default
    - Code security and analysis (Default設定)
        - Dependency graph -> Enable
        - Secret scanning -> Enable
        - それ以外 -> Disable


## プライベートリポジトリへユーザを招待する
----------------------------------------
- リポジトリを開く。
- `Settings` -> `Collaborators` -> `Manage access` -> `Add people`
- `Add a collaborator to <repository_name>`が開くので、招待したいGithubユーザ名を記載する。
- 該当するユーザが表示されるので、クリックして`Add <user_name> to this repository`をクリックする。
- 以下を確認する。
    - `Settings` -> `Collaborators` -> `Who has access` -> `DIRECT ACCESS`の数が増加していること。
    - `Settings` -> `Collaborators` -> `Manage access`に招待したアカウントが表示されていること。


## リポジトリの削除
----------------------------------------
- 削除したいリポジトリを開く。
- `Settings` -> `General` -> `Danger Zone` -> `Delete this repository`
- `Are you absolutely sure?`ウィンドウが表示されるので、記述に従ってリポジトリ名を記載し、`I underdtand the consequence, delete this repository`をクリックする。
