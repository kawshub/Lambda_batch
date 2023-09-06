## デプロイ方法
### コンフィグファイル修正
configs/config.yamlに必要情報を記載する
### Lambdaファイル格納
lambdaディレクトリに「index.py」というファイル名でLambdaファイルを配置
### 初期化
```
python -m venv .venv
source .venv/bin/activate
pip install pipenv
pipenv sync --dev
cdk ls
```
### デプロイ
```
cdk deploy
```