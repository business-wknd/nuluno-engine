# IG增加淨追蹤人數

- **Goal id:** `G-IG-FOLLOWERS`
- **Language:** English (research and messaging steps) and 繁體中文 (channel steps)
- **Channel:** instagram
- **Metric:** `net_followers` = `followers`, should increase
- **Observation window:** 48 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), content (the next round starts with `C-IG-RESEARCH`), data (the next round starts with `C-IG-METRICS`)

## Steps

### 1. Read the product and what it sells

Build one dated fact sheet of what the product does, what it costs, and what is still unknown, so every later sentence of sales copy can be checked against something real.

- **S01.01** Open the product's own pages: home page, sales page, pricing page, and any help or delivery documents. Write down each URL and the date and time you read it.  
  _Done when:_ A list of URLs or file names, each with the time it was read.
- **S01.02** Look at the live product or a demo and list what a user can actually get done with it today. Ask the owner about anything you cannot see for yourself.  
  _Done when:_ Each listed function points to a screen, a document page, or the owner's confirmation.
- **S01.03** For each item on that list, mark whether the software does it, a person does it as a service, or it is not delivered yet.  
  _Done when:_ Every item is labeled software, human service, or not yet available, with who delivers it and any limit.
- **S01.04** Write down what is for sale: plan names, price, currency, billing period, current discounts, and when each discount ends. If a price is not shown on the product's pages, write 'unknown' and ask the owner.  
  _Done when:_ Every price and term has the URL or owner message it came from.
- **S01.05** Open the existing trial, sign-up, and buy links and check that each one loads and lands on the right product. Do not fill in forms and do not pay.  
  _Done when:_ Each link is listed with the page it actually reached and whether it worked.
- **S01.06** Collect proof that may be quoted: real customer cases, screenshots, numbers, and statements the owner has approved for public use.  
  _Done when:_ Each piece of proof has a source and a note on where it may be used.
- **S01.07** List what must never be promised without the owner's say: features that do not exist, new prices, extra deliverables, and business limits.  
  _Done when:_ A 'do not promise' list that later posts and replies can be checked against.
- **S01.08** Put everything into one product fact sheet: what is sold, proof, links, limits, and unknowns. Date it so later steps know which version they used.  
  _Done when:_ One dated fact sheet that the following steps can use without reopening the site.
- **S01.09** Note when the sources should be checked again, and update the fact sheet whenever the owner says something changed.  
  _Done when:_ A next-check date written on the fact sheet.

**Hand back:** `product_facts`, `offer_and_price`, `limits_and_unknowns`

**If stuck:**
- `site_unreachable`: If the product pages will not load, ask the owner for a working URL or the page text, and do not describe the product from memory.
- `price_not_shown`: If no price is visible, record the price as unknown and ask the owner; never guess one.
- `product_behind_login`: If the product can only be seen after signing in, ask the owner for screenshots or a short walk-through; never ask for a password.
- `pages_disagree`: If two pages state different prices or features, list both versions with their URLs and ask the owner which one is current.
- `broken_buy_link`: If a sign-up or buy link fails or lands on the wrong page, report it to the owner before any post sends people there.

### 2. Collect real buyer quotes

Gather the exact words real people use for this problem and the result they want, because copy written in buyers' own words gets read and copy written in the seller's words gets skipped.

- **A-VOC.01** List where real buyers talk about this problem: interviews, reviews, public help threads, customer emails, and refund reasons. Mark which of these the owner allows you to use.  
  _Done when:_ A source list with the URL or origin of each source and whether its use is allowed.
- **A-VOC.02** Collect at least five posts or comments where real people describe this problem in their own words. For each one keep the shortest exact quote, its URL, its date, and an anonymous label such as 'person 1' instead of a name.  
  _Done when:_ At least five quotes, each with URL, date, and anonymous label.
- **A-VOC.03** Sort each quote under one of five headings: the situation they were in, what they do today, what it costs them, the result they want, and what makes them hesitate before buying.  
  _Done when:_ Every quote sits under one heading.
- **A-VOC.04** Remove sellers promoting themselves, AI-written answers, and guesses with no source. If you cannot read the original text, mark it as missing and do not paraphrase it from memory.  
  _Done when:_ A list of what was removed and why.
- **A-VOC.05** Note which kind of people the sample came from (people who have not bought, buyers, people who refunded) and state its limits. Do not present it as the whole market.  
  _Done when:_ A short note on who is in the sample and who is missing.

**Hand back:** `buyer_quotes`, `sources`, `patterns_found`, `limits_and_unknowns`

**If stuck:**
- `no_real_quotes`: If you find fewer than five real quotes, ask the owner for customer emails or reviews, say which public places you searched, and label everything else as a guess.
- `source_unreadable`: If a page is blocked or needs sign-in, skip it or ask the owner for a copy; do not rebuild the quote from search snippets.
- `private_messages_without_permission`: If the only material is private customer messages, ask the owner whether they may be used and remove names before using them.
- `sensitive_personal_details`: If a quote exposes health, money, or relationship details about an identifiable person, drop the identifying details and keep only the need that relates to the product.

### 3. Group buyers by situation and trigger

Split buyers into groups by the moment the problem shows up, then choose one group to speak to, because a post aimed at one clear situation gets more clicks than a post aimed at everyone.

- **A-SEGMENTS.01** Read the collected quotes and the product fact sheet. Do not work out why people buy from their age or gender.  
  _Done when:_ Each observation points to a quote or a product fact.
- **A-SEGMENTS.02** Group buyers by five things: when the problem shows up, what they use instead today, what that costs them, the result they want, and the time, money, or skill they have.  
  _Done when:_ Two to four named groups, each described on those five points.
- **A-SEGMENTS.03** Attach at least one real quote to each group, or label the group as a guess. For each group, say who is not a fit.  
  _Done when:_ Each group shows its quote or the word 'guess', plus who it leaves out.
- **A-SEGMENTS.04** Leave ability to pay, who decides, budget, and timing as 'unknown' unless a source says otherwise. Do not answer these from a job title.  
  _Done when:_ A list of unknowns for each group.
- **A-SEGMENTS.05** Choose the one group you can reach on Threads now and that the product can serve today. Record why you chose it and what would show the choice is wrong.  
  _Done when:_ The chosen group, the reason, and at least one case that argues against it.

**Hand back:** `buyer_groups`, `chosen_group`, `why_chosen`, `unknowns`

**If stuck:**
- `no_real_quotes`: If there are no buyer quotes, go back and collect them; if the owner wants to continue anyway, label every group as a guess.
- `only_demographics`: If all you have is age, gender, or job title, do not build groups from it; ask the owner about three recent buyers and what happened just before they bought.
- `group_cannot_be_served`: If the best-supported group needs something the product does not do, choose the next group and report the gap to the owner.
- `groups_overlap`: If two groups differ only in name, keep the one with more quotes and drop the other.

### 4. Map each problem to a buying motive

Connect each stated problem to the deeper result the buyer wants, because people pay for a change in their life or work, not for a feature.

- **A-MOTIVES.01** For each group, reread the real quotes and separate the problem they have right now from the change they want in their life or work.  
  _Done when:_ Each group has a 'problem now' line and a 'change wanted' line, both tied to quotes.
- **A-MOTIVES.02** Give each motive a working label such as earning money or career, love or company, health, looks, being liked, saving time, independence, or belonging. Treat every label as a guess to be tested.  
  _Done when:_ A list of motives, each with its label and marked 'to be tested'.
- **A-MOTIVES.03** For each motive write the quote behind it, the situation, how confident you are, and any quote that points the other way. Do not infer sensitive weaknesses from personal data.  
  _Done when:_ Each motive has a quote, a confidence note (strong, some, or guess), and any opposing quote.
- **A-MOTIVES.04** Split each motive into three parts: the practical job they want done, how they want to feel, and how they want others to see them.  
  _Done when:_ Each motive lists its practical, emotional, and social part, with 'unknown' where there is no evidence.
- **A-MOTIVES.05** Keep only the parts the product can really help with. Do not inflate fear, and do not promise income, health, or relationship outcomes.  
  _Done when:_ A final list of motives the product can serve, plus the ones you dropped and why.

**Hand back:** `motives`, `supporting_quotes`, `guesses_to_test`, `limits`

**If stuck:**
- `no_real_quotes`: If a motive has no quote behind it, mark it as a guess and go back to collect buyer quotes before relying on it.
- `motive_does_not_fit_a_label`: If a motive does not fit the common labels, describe it in the buyer's own words and do not force it into one.
- `product_cannot_help`: If the product does not really help with a motive, drop it from the selling plan and tell the owner what buyers wanted.
- `sensitive_guess`: If a motive depends on guessing someone's health, finances, or relationship status, remove it and use only needs people stated themselves.

### 5. Pick the strongest motive and objection

Choose the single motive and the single objection that matter most to the chosen group right now, so the post makes one strong point and not five weak ones.

- **A-PRIORITY.01** For the chosen group, read the list of motives, what they use today, and the event that makes them look for a solution. Count repeated quotes from the same person once.  
  _Done when:_ The group name and the quotes used, with repeats from one person merged.
- **A-PRIORITY.02** Compare the motives on four points: how strong the quotes are, how urgent the timing is, what the buyer already pays or loses, and how much of it the product can help with. Judge by this evidence, not by scoring a fixed list of desires.  
  _Done when:_ A short comparison showing each motive against the four points.
- **A-PRIORITY.03** Name the main motive, the second motive, and the cases that contradict them. If the evidence is thin, keep two candidates and say so.  
  _Done when:_ Main and second motive, opposing cases, and a plain statement of how sure you are.
- **A-PRIORITY.04** Separate people who have the budget and the authority to buy from people who only want it. List unknown buying obstacles as questions to ask.  
  _Done when:_ Known objections, plus a list of open questions for the owner or for buyers.
- **A-PRIORITY.05** Pass the main motive on to the benefits step and the angle test. Write down beforehand which real replies or payments would prove it wrong.  
  _Done when:_ The main motive in one sentence and what result would disprove it.

**Hand back:** `main_motive`, `main_objection`, `second_motive`, `what_would_disprove_it`, `open_questions`

**If stuck:**
- `no_real_quotes`: If the ranking rests on no buyer quotes, say it is a guess and go back to collect quotes before treating it as settled.
- `evidence_too_thin`: If the quotes cannot separate two motives, keep both and let the angle test compare them.
- `cannot_tell_who_can_pay`: If nothing shows who has the budget or the say, leave it unknown and ask the owner who has actually paid before.
- `owner_disagrees`: If the owner believes a different motive is strongest, record both views with their evidence and test both.

### 6. Turn features into benefits you can prove

Translate each real feature into the benefit and result a buyer cares about, and mark exactly where proof stops, so the post is persuasive and still true.

- **A-LADDER.01** Read the product facts, the limits, and the buyer quotes one at a time. Do not add anything the product cannot do.  
  _Done when:_ The facts and quotes you used, each traceable to the fact sheet or a source URL.
- **A-LADDER.02** For each feature write a chain of four items: the feature, the benefit a buyer can observe, the result they want, and the point past which nothing may be promised.  
  _Done when:_ One chain per feature with all four items filled in.
- **A-LADDER.03** Mark each link in every chain as verified, guess, or unsupported, and give the reason.  
  _Done when:_ Every link carries one of the three marks and its basis.
- **A-LADDER.04** Check every number and every cause-and-effect claim separately. For example, 'meet people from five industries' and 'raise your chance of a new job' are two claims, and each needs its own proof.  
  _Done when:_ A list of claims, each with its proof or the note 'no proof, do not state as fact'.
- **A-LADDER.05** Choose the value statement that is both true and matches the main motive, and write it as one to three short message options ready to test.  
  _Done when:_ The chosen statement and its message options, each tied to verified facts.

**Hand back:** `chosen_message`, `message_options`, `facts_used`, `must_not_promise`

**If stuck:**
- `no_product_facts`: If the product fact sheet is missing or out of date, go back and read the product before writing any benefit.
- `claim_has_no_proof`: If a benefit has no proof, word it as an invitation to try or as something being tested, never as a result.
- `number_without_source`: If a number has no source, remove it or ask the owner where it comes from.
- `benefit_needs_missing_feature`: If the benefit buyers want depends on a feature that does not exist, drop it from the copy and tell the owner about the gap.

### 7. Design the sales angle test

Set up a fair comparison of two or three ways to present the same true benefit, with the win rule written before posting, so the numbers decide which one earns more link clicks.

- **A-ANGLES.01** Name one buyer group in one situation, the quote that represents them, the motive, and the benefit the product can deliver.  
  _Done when:_ Group, quote, motive, and benefit written in four short lines.
- **A-ANGLES.02** Write two or three angles: the progress they hope for, getting past the real obstacle, and a believable demonstration. Do not use fear to exaggerate outcomes.  
  _Done when:_ Two or three angles, each in one or two sentences.
- **A-ANGLES.03** For each angle list the facts that support it, the promises that are still unknown, and the wording that must not be used.  
  _Done when:_ Each angle has supporting facts, unknowns, and banned wording next to it.
- **A-ANGLES.04** Change only one thing between versions and keep the same channel, audience, and destination link. Before posting, write the guess being tested, how long the test runs, the number that counts as a win, and the cost in time or money.  
  _Done when:_ A test plan written before the first post, showing the guess, the duration, the win number, and the cost.
- **A-ANGLES.05** Choose the main number: qualified inquiries, sign-ups, payments, or another number named in advance (in this playbook, link clicks divided by views). Likes are supporting information only, and state when the test stops.  
  _Done when:_ The main number, the rule for stopping, and the versions ready to be written as posts.

**Hand back:** `test_guess`, `angles`, `facts_used`, `win_rule`

**If stuck:**
- `no_main_motive`: If no main motive has been chosen, go back and choose one before writing angles.
- `angle_needs_unproven_claim`: If an angle only works with a claim that has no proof, rewrite it as an invitation to try or drop the angle.
- `too_few_views_expected`: If the account is too small for the versions to get comparable views, say so and report the result as an early signal, not as proof.
- `cannot_measure_clicks`: If link clicks cannot be read anywhere, ask the owner how they can be checked, and do not declare a winner from likes.

### 8. 準備Instagram帳號、登入與授權

準備Instagram帳號、登入與授權

- **C-INSTAGRAM-ACCESS.01** 先讀本品牌IG URL、帳號ID與既有工具；列出目前登入的個人／專業帳號，不能用前一品牌  
  _Done when:_ 目標handle、可用工具與帳號讀回
- **C-INSTAGRAM-ACCESS.02** 開目標profile核對handle、品牌網址與管理權；登入別的帳號就切換到已授權品牌，不登出全部帳號  
  _Done when:_ profile URL及管理入口
- **C-INSTAGRAM-ACCESS.03** 未登入時走官方登入或連接器OAuth；續用本人已登入的瀏覽器，不讀cookie或把token貼進文件  
  _Done when:_ 登入狀態與授權範圍，無秘密
- **C-INSTAGRAM-ACCESS.04** Graph路徑先讀目前schema及權限，核對專業IG與Page連結；只支援個人帳號時保留官方可用路徑  
  _Done when:_ 支援發布／insights的能力讀回
- **C-INSTAGRAM-ACCESS.05** 只有新增帳號明確授權才填已確認的名稱／聯絡資料；OTP、CAPTCHA、條款確認交本人，保存返回頁面  
  _Done when:_ 既有帳號或待本人步驟
- **C-INSTAGRAM-ACCESS.06** 讀出本帳號可用的貼文格式、排程、insights與時區；不自行切換帳號類型  
  _Done when:_ 能力矩陣與觀察時區

**Hand back:** `subject_id`, `brand_match`, `actual_scopes`, `observed_at`

**If stuck:**
- `wrong_profile`: 重讀handle及品牌網址，回帳號切換器；不發布直到身分吻合。
- `missing_page_link`: 讀專業帳號連結；若無權限僅卡API發布，素材繼續。
- `upload_picker_blocked`: 在同一授權瀏覽器走原生檔案選擇器並核對本機圖；不擴大磁碟權限。
- `default_crop`: 選原始比例並目視核對四邊，重新讀回預覽。
- `publish_unknown`: 搜尋近期同圖／同文永久連結與時間，對帳後才決定是否重送。

### 9. 研究IG買家情境與內容鉤子

研究IG買家情境與內容鉤子

- **C-IG-RESEARCH.01** 在本品牌利基找近期Reels／輪播，逐篇讀原文而非只看粉絲大帳  
  _Done when:_ 原帖URL、日期、格式
- **C-IG-RESEARCH.02** 區分創作者宣傳、觀眾求助及可見互動；不可見觸及填null  
  _Done when:_ 需求引句及可見指標
- **C-IG-RESEARCH.03** 拆首屏、caption開頭、內容結構與CTA，核對是否適合我們的產品  
  _Done when:_ hook／結構／fact_ids
- **C-IG-RESEARCH.04** 把可測變數限制成鉤子或內容格式其中一項，不照抄素材  
  _Done when:_ 一個假設與兩版差異
- **C-IG-RESEARCH.05** 保存樣本選法、觀察窗口及不能推論的成效  
  _Done when:_ examples與limitations

**Hand back:** `original_url`, `author`, `published_at_or_unknown`, `actual_quote_or_empty`, `visible_metrics_only`

**If stuck:**
- `wrong_profile`: 重讀handle及品牌網址，回帳號切換器；不發布直到身分吻合。
- `missing_page_link`: 讀專業帳號連結；若無權限僅卡API發布，素材繼續。
- `upload_picker_blocked`: 在同一授權瀏覽器走原生檔案選擇器並核對本機圖；不擴大磁碟權限。
- `default_crop`: 選原始比例並目視核對四邊，重新讀回預覽。
- `publish_unknown`: 搜尋近期同圖／同文永久連結與時間，對帳後才決定是否重送。

### 10. 安排下一批內容與素材

安排下一批內容與素材

- **S10.01** 讀取目標與上輪結論：確認這批內容要解決哪個問題或測什麼差異。  
  _Done when:_ 每個項目能對應流程目標。
- **S10.02** 盤點可重用素材：檢查舊文、圖片、影片、示範與權利。  
  _Done when:_ 知道哪些可改編。
- **S10.03** 指定買家與階段：每項內容只設定清楚的主要對象。  
  _Done when:_ 訊息與購買階段相符。
- **S10.04** 選切角與證據：列問題、承諾、真實示範及可用案例。  
  _Done when:_ 主張能回到S01或S07證據。
- **S10.05** 決定格式與渠道：指定文章、輪播、短片、廣告或指南等形式。  
  _Done when:_ 格式與可用發布能力相符。
- **S10.06** 指定現有行動入口：選既有試用、購買、訊息或外部表單。  
  _Done when:_ 入口可達且與內容相符。
- **S10.07** 設計可比較版本：只改可辨識的切角、開頭、證據或形式。  
  _Done when:_ 版本標記與測試差異清楚。
- **S10.08** 拆成製作工作單：交S11、S12、S13需要的素材與輸出規格。  
  _Done when:_ 每單都有素材來源、尺寸／長度與完成標準。
- **S10.09** 排發布及回饋時間：交S14與觀測排程，設定與本輪相符的窗口。  
  _Done when:_ 每個版本能接回S33。
- **S10.10** 接回結果並更新：由S34或S32開下一批工作。  
  _Done when:_ 保留舊版與改動理由。

**Hand back:** `hypothesis`, `variants`, `fact_ids`, `acceptance_rule`

### 11. Write the post from proven facts

Write the Threads post that opens with the buyer's own situation and offers one true step forward with a link, because a specific, believable post is what makes a reader click through to the product site.

- **A-COPY.01** Read the chosen angle, the buyer quotes, and the product fact sheet. Open the post with the situation the reader is in right now, in words close to how buyers describe it.  
  _Done when:_ The opening line, with the quote and facts it draws on.
- **A-COPY.02** Then state one specific step forward the product helps with, and point to the existing link where the reader can act on it.  
  _Done when:_ One or more draft versions, each with one benefit and one link you have opened and checked.
- **A-COPY.03** Keep what the product delivers separate from what the buyer hopes will follow. Without data, do not write 'improves X%' and do not guarantee an outcome such as getting a job.  
  _Done when:_ A list of the claims in the post, each marked 'delivered by the product' or 'hoped-for result'.
- **A-COPY.04** If you write more than one version, change only one thing between them and label what changed, so the versions can be compared fairly.  
  _Done when:_ Each version is labeled with the single thing that differs.
- **A-COPY.05** Check every sentence against the fact sheet and against the way the owner writes. Remove any number without support, or reword it as a clearly labeled guess.  
  _Done when:_ The final text, a sentence-by-sentence fact check, and a note that it is ready to show the owner.

**Hand back:** `post_text`, `facts_used`, `claims_avoided`

**If stuck:**
- `no_chosen_angle`: If no angle has been chosen, go back to the angle test step before writing.
- `fact_missing_for_claim`: If a sentence needs a fact you do not have, remove the sentence or ask the owner; never fill the gap with a guess.
- `no_working_link`: If you do not have a product link that you have opened and seen load, ask the owner which URL to use.
- `owner_voice_unknown`: If you do not know how the owner writes, ask for two of their past posts and match that tone.
- `text_too_long`: If the text is over the Threads length limit, cut it to one situation, one benefit, and one link.

### 12. 製作與改版圖片素材

製作與改版圖片素材

- **S12.01** 讀取用途與規格：確認渠道、圖片類型、尺寸與數量。  
  _Done when:_ 每張圖的用途明確。
- **S12.02** 盤點可用視覺：讀品牌、產品畫面、照片及使用權。  
  _Done when:_ 素材來源可追查。
- **S12.03** 核對文字與主張：使用S11已核對文案。  
  _Done when:_ 價格與產品畫面一致。
- **S12.04** 安排資訊層次：決定標題、示範、證據與行動提示的位置。  
  _Done when:_ 一眼能理解重點。
- **S12.05** 實際製作圖片：使用可用圖片工具產出檔案。  
  _Done when:_ 取得可開啟的實際圖片。
- **S12.06** 檢查文字與細節：查看字形、裁切、產品畫面及是否有生成錯字。  
  _Done when:_ 關鍵文字與畫面正確。
- **S12.07** 檢查尺寸與格式：核對檔案類型、像素、容量與可讀性。  
  _Done when:_ 符合當前渠道需求。
- **S12.08** 製作必要版本：依測試需求裁切、改版或改比例。  
  _Done when:_ 版本各有用途與識別。
- **S12.09** 保存檔案與使用紀錄：交S14或S31可讀的檔案參照。  
  _Done when:_ 來源、版本、用途可查。

**Hand back:** `actual_file`, `mime_type`, `dimensions`, `sha256`, `visual_readback`

### 13. IG追蹤成長與內容到網站漏斗核對 (baseline numbers)

IG追蹤成長與內容到網站漏斗核對

- **C-IG-METRICS.01** 核對同IG ID、時區與比較期間；分開帳號總量及單篇內容  
  _Done when:_ account_id與window
- **C-IG-METRICS.02** 讀followers起訖或follows/unfollows，計淨增加；不能只用目前總粉絲  
  _Done when:_ 起訖counts
- **C-IG-METRICS.03** 讀reach、profile visits、可用link taps，缺欄位填null  
  _Done when:_ 各分母與source
- **C-IG-METRICS.04** 用既有網站分析匹配來源／期間；無追蹤資料不能推定是這篇導入  
  _Done when:_ sessions與attribution
- **C-IG-METRICS.05** 讀現有付款退款與全成本；漲粉、詢問、付款各自報告  
  _Done when:_ money_events與limitations

**If stuck:**
- `wrong_profile`: 重讀handle及品牌網址，回帳號切換器；不發布直到身分吻合。
- `missing_page_link`: 讀專業帳號連結；若無權限僅卡API發布，素材繼續。
- `upload_picker_blocked`: 在同一授權瀏覽器走原生檔案選擇器並核對本機圖；不擴大磁碟權限。
- `default_crop`: 選原始比例並目視核對四邊，重新讀回預覽。
- `publish_unknown`: 搜尋近期同圖／同文永久連結與時間，對帳後才決定是否重送。

### 14. IG輪播發布與公開讀回

IG輪播發布與公開讀回

- **C-IG-CAROUSEL.01** 讀同帳號近期貼文與本輪operation key，排除同圖同文已發  
  _Done when:_ 近期URL與去重結果
- **C-IG-CAROUSEL.02** 核對每張圖片的實際解碼、順序、文字安全區與使用權  
  _Done when:_ assets順序及sha256
- **C-IG-CAROUSEL.03** 在正確IG profile建輪播，保留原比例；預覽逐張核對裁切及首圖  
  _Done when:_ 預覽證據
- **C-IG-CAROUSEL.04** caption逐字核對事實、品牌網址與CTA；不加未授權價格／新承諾  
  _Done when:_ caption雜湊與fact_ids
- **C-IG-CAROUSEL.05** action-prepare後才執行單篇發布；未知結果先查近期內容  
  _Done when:_ operation_key
- **C-IG-CAROUSEL.06** 用公開永久連結重新讀每張圖、caption和handle；審核中另標狀態  
  _Done when:_ publications與readback

**Hand back:** `original_operation_id`, `platform_object_id`, `account_ref`, `published_state`, `exact_content_readback`, `permalink`

**If stuck:**
- `wrong_profile`: 重讀handle及品牌網址，回帳號切換器；不發布直到身分吻合。
- `missing_page_link`: 讀專業帳號連結；若無權限僅卡API發布，素材繼續。
- `upload_picker_blocked`: 在同一授權瀏覽器走原生檔案選擇器並核對本機圖；不擴大磁碟權限。
- `default_crop`: 選原始比例並目視核對四邊，重新讀回預覽。
- `publish_unknown`: 搜尋近期同圖／同文永久連結與時間，對帳後才決定是否重送。

### 15. IG追蹤成長與內容到網站漏斗核對 (result numbers)

IG追蹤成長與內容到網站漏斗核對

- **C-IG-METRICS.01** 核對同IG ID、時區與比較期間；分開帳號總量及單篇內容  
  _Done when:_ account_id與window
- **C-IG-METRICS.02** 讀followers起訖或follows/unfollows，計淨增加；不能只用目前總粉絲  
  _Done when:_ 起訖counts
- **C-IG-METRICS.03** 讀reach、profile visits、可用link taps，缺欄位填null  
  _Done when:_ 各分母與source
- **C-IG-METRICS.04** 用既有網站分析匹配來源／期間；無追蹤資料不能推定是這篇導入  
  _Done when:_ sessions與attribution
- **C-IG-METRICS.05** 讀現有付款退款與全成本；漲粉、詢問、付款各自報告  
  _Done when:_ money_events與limitations

**If stuck:**
- `wrong_profile`: 重讀handle及品牌網址，回帳號切換器；不發布直到身分吻合。
- `missing_page_link`: 讀專業帳號連結；若無權限僅卡API發布，素材繼續。
- `upload_picker_blocked`: 在同一授權瀏覽器走原生檔案選擇器並核對本機圖；不擴大磁碟權限。
- `default_crop`: 選原始比例並目視核對四邊，重新讀回預覽。
- `publish_unknown`: 搜尋近期同圖／同文永久連結與時間，對帳後才決定是否重送。
