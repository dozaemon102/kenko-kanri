# 詳細設計書 レビュー結果

- **対象:**
  - `projects/sanpo-ban/docs/features/sanpo-ban/detailed-design/v1-core.md`
- **参照:** `projects/sanpo-ban/docs/features/sanpo-ban/requirements.md`, `basic-design.md`
- **レビュー日:** 2026-06-13
- **判定:** 合格

## サマリー

全必須 FR が API・DB・画面に対応している。MySQL スキーマと Dashboard 計算の整合、Health 同期、Notion UI トークンが定義済み。認証なし方針も一貫。

## 指摘一覧

### Critical

なし

### Suggestion

| ID | 該当ファイル / 箇所 | 指摘 | 修正案 |
|----|---------------------|------|--------|
| S-001 | v1-core.md §8 | ショートカット JSON の日付プレースホルダ | 実装時に `docs/infra/ios-shortcuts.md` で具体例を固定 |

## チェックリスト結果

| 区分 | 件数 |
|------|------|
| Critical | 0 |
| Suggestion | 1 |
