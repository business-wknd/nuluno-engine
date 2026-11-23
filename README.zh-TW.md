<h1 align="center">Nuluno Engine</h1>

<p align="center"><b>你的 AI 寫完行銷計畫就忘了。<br>Nuluno Engine 讓它盯著一個銷售數字，直到數字動起來。</b></p>

<p align="center"><a href="README.md">English</a> · 繁體中文 · <a href="https://engine.nuluno.com/">雲端版（免費）</a> · <a href="playbooks/">作法</a></p>

```sh
npx skills add business-wknd/nuluno-engine
```

裝好後跟你的 AI 說：**「用 Nuluno Engine 賣 https://你的產品.com」**

**支援：** 讀得懂 Agent Skills 的 AI（Codex、Cursor、Claude Code、Gemini CLI 等）、任何 MCP 用戶端，以及可以新增自訂 MCP 連接器的聊天 AI（例如 Claude、ChatGPT Business）——到 [engine.nuluno.com](https://engine.nuluno.com/) 免費拿一個連接網址即可。

<p align="center"><img src="docs/loop.gif" width="760" alt="Engine 退回沒做完的步驟和個人頁面連結，等數字，判定沒達標，只改一個地方開第二輪"></p>

## 它幫你解決什麼

- **問題：** 你請 AI 幫忙賣東西，它給你一大篇建議就停了；隔天開新對話，它全忘了，也沒人知道到底有沒有賣出去。
- **Engine 做的事：** 給 AI 一個有數字的目標，把工作拆成一步一步，每一步交出成果才放行；發文後等觀察期，用平台上的真實數字判定；沒達標就找出一個原因、只改一個地方，再跑一輪。
- **你的體驗：** 你只說一句話。AI 自己讀網站、找真實買家的說法、寫文案；需要你的時候只問一件事（例如「這段文字可以發嗎？」）。換對話、換電腦也接著做。

| 你的 AI 自己做 | 加上 Nuluno Engine |
|---|---|
| 寫完計畫就說做完了 | 一次一步；要交的東西少一樣就退回 |
| 「發好了！」 | 要附那則貼文本身的公開網址；個人頁面或不存在的網址會被退回 |
| 「效果不錯」 | 一輪只在記下有來源的數字後才結束 |
| 開新對話就從頭來 | 進度會保存，下次接著做 |
| 一次改五個地方 | 每輪只改一個；跟之前字句相同的改法會被退回 |

Engine 自己不發文、不寄信、不花錢；AI 做事，每一次發布、寄出、花費都由你核准。

## 月目標模式

給 Engine 一個月的數字，例如「30 天 100 個付費客戶」，它算出每個渠道每天要做到多少。

```sh
python3 engine/nuluno.py target 100 --days 30 --price 39 --currency USD
python3 engine/nuluno.py plan G-TH-LINK-RATE G-RD-PURCHASES G-EM-PURCHASE
python3 engine/nuluno.py month
```

- **每天的數字：** `set_month_target` 和 `plan_month` 把目標換算成每天要多少付費客戶、註冊和造訪，並把造訪分給 1 到 5 個不同渠道的目標，每個目標是一條獨立的線：一開始平均分，第 3 天起依每條線的點擊分。還沒量到的轉換率會標成假設（造訪的 2% 付費），直到數到 100 次造訪和 1 位付費客戶。
- **每天一輪：** 每條線每一輪最多等 24 小時看數字。`month_status` 顯示目前付費人數、進度、每條線的步驟和今天的額度，以及 `next`：現在該做哪條線。每個目標工具都接受 `lane`。
- **一次核准：** `submit_batch` 把一週的貼文、回覆、Email 和廣告一次交給你；`request_ad_budget` 只請你核准一次廣告每日上限。核准由你來做：雲端版在你的私人頁面，本機版由你自己在真正的終端機執行 `nuluno.py approve <batch_id> --all` 或 `nuluno.py approve-budget` 並輸入 yes，沒有可以跳過這一步的參數。在月目標的線上，發布或寄出的步驟沒有附 `approved_item` 一律被拒絕，而且發出的文字必須和核准的一字不差。超過核准上限的花費會標記 `over_budget`。
- **雲端版：** 免費版：1 條線的月計畫，每週在你的私人頁面核准一次，付費人數來自成交計數器和你記錄的數字，造訪由追蹤連結計算。Pro：5 個產品，最多 5 條線，每個產品用自己的 Stripe 限制型唯讀金鑰讀取付費人數，並用你自己的 Anthropic 金鑰每天自動跑，花費不超過你設定的每日上限。

## 內容

99 個銷售作法，由 155 個可重複使用的步驟組成（共 1,116 個檢查項目），整理成 24 個 Agent Skills，涵蓋 Threads、Instagram、X、TikTok、YouTube、Reddit、LinkedIn、Product Hunt、Meta／Google 等廣告、Email、線上講座、合作夥伴、App Store 與 Google Play。作法本身用英文寫成，AI 會用你的語言跟你溝通。

安裝方式、工具清單、規則與資料安全的完整說明請看 [英文版 README](README.md)。授權：Apache-2.0。
