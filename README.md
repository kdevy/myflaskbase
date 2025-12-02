# doc

```
source venv/bin/activate
```
インストール
```
pip install -e .
```
開発用パッケージインストール
```
pip install .[dev]
```
テスト
```
pytest
```
環境変数設定 .env  
`python -c "import secrets; print(secrets.token_hex(32))"`
```
DB_USER = "root"
DB_PASS = "pass"
DB_HOST = "localhost"
DB_NAME = "flask"
SECRET_KEY = "secret key"
```