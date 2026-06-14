# API 契約レビュー結果（v2）

- **対象:** `docs/features/sanpo-ban/contract/openapi.yaml`
- **参照:** `detailed-design/v2-barcode.md`, `detailed-design/v1-core.md`
- **レビュー日:** 2026-06-13
- **判定:** 合格

## サマリー

v2 の `GET /foods/barcode/{barcode}`、`FoodLookup` スキーマ、`MealLog.barcode` が詳細設計と一致。v1.1 削除 API（walks/weights DELETE）も契約に追記済み。

## 指摘一覧

### Critical

| ID | 該当箇所 | 指摘 | 修正案 |
|----|----------|------|--------|
| — | — | なし | — |

### Suggestion

| ID | 該当箇所 | 指摘 | 修正案 |
|----|----------|------|--------|
| — | — | なし | — |

## チェックリスト結果

| 区分 | 件数 |
|------|------|
| Critical | 0 |
| Suggestion | 0 |

## 詳細設計との対応

| 詳細設計 | エンドポイント | openapi |
|----------|---------------|---------|
| v2-barcode | GET /foods/barcode/{barcode} | ✓ |
| v2-barcode | POST /meals + barcode | ✓ |
| v1.1 | DELETE /walks/{id} | ✓ |
| v1.1 | DELETE /weights/{id} | ✓ |
