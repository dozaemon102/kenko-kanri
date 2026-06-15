# API 契約レビュー結果（v3）

- **対象:**
  - `docs/features/sanpo-ban/contract/openapi.yaml`
  - `docs/features/sanpo-ban/contract/types.ts`
- **参照:** `detailed-design/v3-balance-ui.md`
- **レビュー日:** 2026-06-14
- **判定:** 合格

## サマリー

v3 詳細設計の全 API（追加 2、削除 4 系、Profile 変更、Health/Weight 体組成）が OpenAPI 3.0.3 に反映されている。廃止エンドポイントは契約から除外済み。types.ts と整合。

## 指摘一覧

### Critical

なし

### Suggestion

なし

## エンドポイント突合

| 詳細設計 | openapi.yaml |
|----------|--------------|
| GET /dashboard/top | ✓ |
| GET /dashboard/history/{metric} | ✓ |
| PUT/GET /profile (NEAT/TEF) | ✓ |
| 削除: today, walks, summary, recalculate-targets | ✓ 除外 |
| 継続: meals, foods, weights, sync, exercises | ✓ |

## チェックリスト結果

| 区分 | 件数 |
|------|------|
| Critical | 0 |
| Suggestion | 0 |
