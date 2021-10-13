# ApexStalker

# 使い方
## APIの準備
`.env_sample`を参考に`.env`を同階層に生成します。  
API_ENDPOINTとAPI_KEYは[Apex Legends API](https://tracker.gg/developers/docs/titles/apex)で取得してください。

## Pythonの準備
Python 3.7+が必須です。
- virtual envを作ります
```bash
python -m venv apex
```
- 作った環境に入ります
```bash
source ./apex/bin/activate
```
- 依存関係を入れます
```bash
pip install -r requirements.txt
```

## テーブルの作成
```bash
python initialize.py
```
でテーブルを作成します

## ウォッチするユーザーの追加
```bash
python add.py <userID> <platform> <ランク初期値> 0
```
で追加できます。
- <platform>`origin`か`psn`(プレステ)を入れます
- <userID>はそのplatformでのidを入れます
- ランク初期値は今のランクもしくは0とか入れます
