# ビルドステージ
FROM python:3.12-alpine as builder

# 作業ディレクトリを設定
WORKDIR /build

# 依存関係ファイルをコピー
COPY requirements/requirements.txt .

# Python依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# 実行ステージ
FROM python:3.12-alpine

# 作業ディレクトリを設定
WORKDIR /app

# ビルドステージから必要なファイルをコピー
COPY --from=builder /usr/local /usr/local
COPY src/ /app/src/

# コンテナ起動時に実行するコマンド
CMD ["python", "/app/src/main.py"]
