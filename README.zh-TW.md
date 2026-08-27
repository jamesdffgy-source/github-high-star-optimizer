# GitHub 高星發布優化器

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Türkçe](README.tr.md) · [Bahasa Indonesia](README.id.md)

<p align="center">
  <img src="docs/assets/github-high-star-optimizer-readme-hero.png" alt="GitHub 高星發布優化器的稽核、準備、套用與發布流程，全程不修改專案程式碼。" />
</p>

> 一個遵循 Agent Skills 標準的可攜式 Skill：適用於 Codex、Claude Code 與相容宿主，把真實、既有的 GitHub 專案整理成更清楚、可信且可發布的儲存庫，同時不修改產品程式碼。

GitHub 高星發布優化器只改善真實專案的公開發布層：定位、README 結構、以證據為基礎的視覺素材、儲存庫中繼資料、Release Notes、多語言介紹與合規發布材料。它不承諾 Star 數量，也不操縱互動。

> 規範來源是[英文 README](README.md)。此翻譯尚未經過母語人工審校；若有差異，請以英文版為準。

## 優化內容

- **命名與搜尋：** 評估任務詞匹配、目前 GitHub 搜尋樣本、名稱衝突、後設資料一致性與改名成本。
- **清楚：** 說明受眾、問題、結果、差異點與主要下一步。
- **可信：** 重要敘述連結到儲存庫證據，並揭示限制與真實輸出。
- **展示：** README Hero、Social Preview、Release 圖片、徽章與資訊層級。
- **外部分發：** 建立平台專屬文案，支援試跑、經核准的 API/Webhook 自動發布、論壇輔助佇列、冪等防重複與結果回收。
- **邊界：** 不修改原始碼、相依套件、建置、測試、CI、執行設定或產品行為。

## 四種模式

| 模式 | 內容 | 修改範圍 |
|---|---|---|
| **Audit / 稽核** | 評分並排列發布層問題。 | 不修改 |
| **Prepare / 準備** | 在獨立目錄建立文案與素材。 | 不修改 |
| **Apply / 套用** | 套用明確核准的非程式碼檔案。 | 僅限核准清單 |
| **Publish / 發布** | 授權後更新 GitHub 中繼資料、Release 或發布頁面。 | 僅限明確授權操作 |

## 快速開始

1. 複製此儲存庫。
2. 依照[安裝指南](docs/INSTALLATION.md)，將內層 [`github-high-star-optimizer`](github-high-star-optimizer) 目錄安裝到 Codex、Claude Code 或相容的 Agent Skills 宿主。
3. 使用對應宿主的呼叫語法並指定真實儲存庫或工作區。

```text
使用 $github-high-star-optimizer 稽核這個既有儲存庫。
只優化公開展示與發布套件，不修改任何程式碼。
```

## 真實性規則

重要敘述必須來自儲存庫檔案、Release、示範、Issue、使用者提供的事實，或清楚標示的推論。生成圖片不得偽造產品介面、命令輸出、效能資料、整合、客戶、功能或 Star 數量。禁止買星、互刷、自動互動與以獎勵換取 Star。

完整流程請見 [`github-high-star-optimizer/SKILL.md`](github-high-star-optimizer/SKILL.md)，多語言規範請見 [`multilingual-publishing.md`](github-high-star-optimizer/references/multilingual-publishing.md)，外部分發自動化請見 [`distribution-automation.md`](github-high-star-optimizer/references/distribution-automation.md)。

## 授權

[MIT](LICENSE)
