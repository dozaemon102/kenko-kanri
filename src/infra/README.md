# 散歩判 — 起動方法

## ラズパイで確認（PC に Docker 不要）← いまのおすすめ

→ **[pi-native/README.md](pi-native/README.md)** を参照

```bash
# Pi 上で
cd ~/sanpo-ban
chmod +x src/infra/pi-native/install.sh
./src/infra/pi-native/install.sh
# ブラウザ: http://<PiのIP>:8080
```

## Docker Compose（PC に Docker がある場合のみ）

```bash
cd src/infra
docker compose up --build
```

## フロント単体開発（Pi API に向ける）

```bash
cd src/frontend
npm install
# vite.config.ts の proxy 先を Pi の IP に変更するか、
# ビルド済み dist を Pi に置いて API から配信（install.sh が実行）
```

## iPhone ショートカット

POST `http://<PiのIP>:8080/api/v1/sync/health`  
詳細は [pi-native/README.md](pi-native/README.md)
