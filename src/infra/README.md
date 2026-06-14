# 散歩判 — ローカル起動

## Docker Compose（推奨）

```bash
cd src/infra
docker compose up --build
```

- API: http://localhost:8080
- MySQL: localhost:3306（user/pass/db: `sanpo` / `sanpo` / `sanpo_ban`）

## フロントエンド開発

```bash
cd src/frontend
npm install
npm run dev
```

http://localhost:5173（API は 8080 にプロキシ）

## iPhone ショートカット

1. ヘルスケア → 歩数（今日）
2. POST `http://<PCのLAN IP>:8080/api/v1/sync/health`
3. JSON: `{"date":"YYYY-MM-DD","steps":1234,"weight_kg":72.0}`（weight は任意）

**注意:** トレッドミルを手入力した日にスマホも持つと、歩数とトレッドミルで消費 kcal が二重計上されます。

## Pi + SSD

MySQL の datadir を USB SSD にマウントしてから `docker compose` を利用してください（`docs/backlog.md` BL-005 参照）。
