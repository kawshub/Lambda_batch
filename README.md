## コピー方法
①新規プロジェクト用のリポジトリを作成
②本リポジトリをテキトーなディレクトリにクローン
```
git clone --bare git@github.com:kawshub/cdk_template.git
```
③新規プロジェクト用のリポジトリにプッシュ
```
cd OLD-REPOSITORY.git
git push --mirror https://github.com/EXAMPLE-USER/NEW-REPOSITORY.git
```
④ローカルにクローンした本リポジトリを削除
```
cd ..
rm -rf cdk_template.git
```

## 事前準備
コンフィグファイルにアカウントIDを記載する

## 初期化コマンド
```
python -m venv .venv
source .venv/bin/activate
pip install pipenv
pipenv sync --dev
cdk ls
```