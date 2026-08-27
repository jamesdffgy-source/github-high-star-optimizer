# GitHub High-Star Optimizer

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Türkçe](README.tr.md) · [Bahasa Indonesia](README.id.md)

<p align="center">
  <img src="docs/assets/github-high-star-optimizer-readme-hero.png" alt="コードを変更せずに Audit、Prepare、Apply、Publish を行う GitHub High-Star Optimizer のワークフロー。" />
</p>

> Agent Skills 標準に準拠し、Codex、Claude Code、互換ホストで利用できるポータブル Skill です。既存の GitHub プロジェクトを、製品コードを変更せずに明確で信頼できる公開準備済みのリポジトリへ整えます。

GitHub High-Star Optimizer が改善するのは実在するプロジェクトの公開面だけです。ポジショニング、README 構成、根拠に基づくビジュアル、リポジトリのメタデータ、Release Notes、多言語紹介、倫理的な公開資料を扱います。Star 数を約束したり、エンゲージメントを操作したりしません。

> 正式な基準は[英語 README](README.md)です。この翻訳はネイティブによる確認前です。差異がある場合は英語版を参照してください。

## 改善対象

- **名前と検索性：** タスク語との適合、現在の GitHub 検索サンプル、名前の衝突、メタデータ整合性、改名コストを評価します。
- **明確さ：** 対象者、課題、結果、差別化要因、次の行動を明示します。
- **信頼性：** 重要な主張をリポジトリの根拠に結び付け、制限と実際の出力を示します。
- **見せ方：** README Hero、Social Preview、Release 画像、バッジ、情報設計を整えます。
- **配布：** プラットフォーム別文面、ドライラン、承認済み API／Webhook 配信、フォーラム向け補助キュー、重複防止、結果記録を扱います。
- **境界：** ソース、依存関係、ビルド、テスト、CI、実行設定、製品の挙動は変更しません。

## 4 つのモード

| モード | 内容 | 変更範囲 |
|---|---|---|
| **Audit** | 公開面を採点し、課題の優先順位を付けます。 | 変更なし |
| **Prepare** | 別ディレクトリに文面と素材を作成します。 | 変更なし |
| **Apply** | 明示的に承認された非コードファイルだけを反映します。 | 承認済みファイルのみ |
| **Publish** | 承認後に GitHub メタデータ、Release、公開面を更新します。 | 明示的に承認された操作のみ |

## クイックスタート

1. このリポジトリをクローンします。
2. [インストールガイド](docs/INSTALLATION.md)に従い、内側の [`github-high-star-optimizer`](github-high-star-optimizer) ディレクトリを Codex、Claude Code、または互換 Agent Skills ホストへインストールします。
3. 各ホストの呼び出し構文で、実在するリポジトリまたはワークスペースを指定します。

```text
Use $github-high-star-optimizer to audit this existing repository.
Only optimize its public presentation and release package; do not change code.
```

## 真実性のルール

重要な主張には、リポジトリのファイル、Release、デモ、Issue、ユーザー提供の事実、または明記された推論が必要です。生成画像で製品 UI、コマンド出力、ベンチマーク、連携、顧客、機能、Star 数を捏造してはいけません。Star の購入、相互交換、自動操作、報酬との交換も禁止します。

完全な手順は [`github-high-star-optimizer/SKILL.md`](github-high-star-optimizer/SKILL.md)、多言語ルールは [`multilingual-publishing.md`](github-high-star-optimizer/references/multilingual-publishing.md)、外部配布の自動化は [`distribution-automation.md`](github-high-star-optimizer/references/distribution-automation.md) を参照してください。

## ライセンス

[MIT](LICENSE)
