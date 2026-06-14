# 最終受入レポート

- **feature:** sanpo-ban v2 バーコード
- **受入日:** 2026-06-13
- **判定:** 条件付き合格

## サマリー

v2 バーコード食事記録（Open Food Facts 連携）を Raspberry Pi 本番（ie-desktop）+ iPhone Safari で受入した。必須 AC（AC-014〜017）および v1.1 の AC-018 は達成。iOS Safari では **HTTPS（Tailscale Serve）** がライブカメラに必要であることを運用上確認。HTTP では「写真で読み取る」フォールバックで FR-037/039 を満たす。

**推奨 URL:** `https://ie-desktop.tail5bd839.ts.net/`

## 受入条件（AC）達成状況

### v2 スコープ

| AC ID | 内容 | 達成 | 根拠（テスト・手動確認） |
|-------|------|------|------------------------|
| AC-014 | 有効 JAN/EAN スキャン → 確認画面に名称・kcal・P/F/C | はい | Pi + iPhone（HTTPS）。backend `test_barcode.py` / API モック |
| AC-015 | 確認画面追加 → 当日摂取合計増加 | はい | Pi UI 確認 |
| AC-016 | OFF 未登録 → 手入力フォームへ | はい | 404 `BARCODE_NOT_FOUND` → 手入力 UI。`test_lookup_barcode_not_found` |
| AC-017 | バーコード追加でプリセット件数不増 | はい | `food_preset_id: null` 固定。`test_barcode_lookup_api` で presets 0 件確認 |
| AC-018 | 誤記録削除 → 集計から除外 | はい | v1.1 実装済。各タブ削除 UI（v1 受入で確認済、v2 でも継続） |

- **必須 AC 未達:** なし

### v1 スコープ（参照）

AC-001〜013 は 2026-06-13 v1 受入（Pi + iPhone）で **承認済**。v2 変更による回帰なし。

## トレーサビリティ（FR → 設計 → コード → テスト）

| 要件 ID | 詳細設計 | 実装 | テスト | 状態 |
|---------|----------|------|--------|------|
| FR-015 | v2-barcode §2 GET /foods/barcode | `open_food_facts.py`, `routes.py` | `test_barcode.py` | OK |
| FR-037 | v2-barcode §4.2 カメラ/手入力 | `barcode-flow.ts`（BarcodeDetector / ZXing / 写真） | 実機（Pi HTTPS） | OK |
| FR-038 | v2-barcode §4.3 確認画面 | `barcode-flow.ts` renderConfirmForm | 実機 | OK |
| FR-039 | v2-barcode §5.1 404/502 フォールバック | `barcode-flow.ts`, `errors.py` | `test_lookup_barcode_not_found` + 実機 | OK |
| FR-036 | v1-core / v2 §10 | DELETE routes + 各タブ UI | v1 受入 | OK |

- **必須 FR の断絶:** なし

## 権限マトリクスの検証

認証・認可なし（NFR-002）。v2 新 API も同一。LAN / Tailscale 内単一利用者前提 — **OK**。

| 操作 / FR | 期待 | 実装・テスト | 状態 |
|-----------|------|-------------|------|
| FR-015〜039 | ROLE-001 全操作可 | 認可チェックなし（設計どおり） | OK |

## 将来要件の移管

| FR ID | 概要 | 移管先 |
|-------|------|--------|
| FR-016 | 食べる判 ○△× | `docs/features/sanpo-ban/future.md` |
| FR-032 | 筋トレ詳細（重量・セット） | 同上 |
| FR-034 | 旅先モード | 同上 |
| FR-035 | Instagram タグメモ | 同上 |
| FR-014 | 食事複製（任意） | 同上 |

## verify-run 結果（参照）

- **判定:** 条件付き合格（`reviews/verify-run.md`）
- **補足:** Phase 5 時点は Pi 未検証だったが、本受入で Pi migration・build・restart・Tailscale HTTPS を完了

## review-code との整合

- `reviews/code.md` の Critical: **0 件（すべて解消）**
- Suggestion（Pi 反映・フロントテスト・duplicate barcode）は本受入で Pi 反映済。残: フロント自動テストなし（Suggestion のみ）

## 運用メモ（v2 追加分）

| 項目 | 内容 |
|------|------|
| HTTPS | iPhone Safari ライブカメラに必須。`tailscale serve --https=443 http://127.0.0.1:8080` |
| HTTP | `http://100.76.191.46:8080` も利用可（カメラ以外）。バーコードは「写真で読み取る」 |
| Alembic | Pi では `uv run alembic upgrade head` |
| ショートカット | Health 同期 URL を HTTPS に更新推奨 |

## 未達・フォローアップ

| 項目 | 対応 |
|------|------|
| フロントエンド自動テストなし | v3 以降または hotfix で検討 |
| duplicate_meal が barcode を複製しない | v2.1 候補（任意） |
| Tailscale Serve の永続化 | Pi 再起動後も serve 設定が残るか運用確認 |
