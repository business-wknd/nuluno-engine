# TikTok Ads提高連結點擊率

- **Goal id:** `G-TA-LINK-CTR`
- **Language:** English and 繁體中文
- **Channel:** tiktok_ads
- **Metric:** `link_ctr` = `link_clicks` / `impressions`, should increase
- **Observation window:** 168 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), creative (the next round starts with `A-ANGLES`), data (the next round starts with `C-TA-METRICS`)

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

Split buyers into groups by the moment the problem shows up, then choose one group to speak to, because copy aimed at one clear situation gets more response than copy aimed at everyone.

- **A-SEGMENTS.01** Read the collected quotes and the product fact sheet. Do not work out why people buy from their age or gender.  
  _Done when:_ Each observation points to a quote or a product fact.
- **A-SEGMENTS.02** Group buyers by five things: when the problem shows up, what they use instead today, what that costs them, the result they want, and the time, money, or skill they have.  
  _Done when:_ Two to four named groups, each described on those five points.
- **A-SEGMENTS.03** Attach at least one real quote to each group, or label the group as a guess. For each group, say who is not a fit.  
  _Done when:_ Each group shows its quote or the word 'guess', plus who it leaves out.
- **A-SEGMENTS.04** Leave ability to pay, who decides, budget, and timing as 'unknown' unless a source says otherwise. Do not answer these from a job title.  
  _Done when:_ A list of unknowns for each group.
- **A-SEGMENTS.05** Choose the one group you can reach on this goal's channel now and that the product can serve today. Record why you chose it and what would show the choice is wrong.  
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

Set up a fair comparison of two or three ways to present the same true benefit, with the win rule written before posting, so the goal's own number decides which one works.

- **A-ANGLES.01** Name one buyer group in one situation, the quote that represents them, the motive, and the benefit the product can deliver.  
  _Done when:_ Group, quote, motive, and benefit written in four short lines.
- **A-ANGLES.02** Write two or three angles: the progress they hope for, getting past the real obstacle, and a believable demonstration. Do not use fear to exaggerate outcomes.  
  _Done when:_ Two or three angles, each in one or two sentences.
- **A-ANGLES.03** For each angle list the facts that support it, the promises that are still unknown, and the wording that must not be used.  
  _Done when:_ Each angle has supporting facts, unknowns, and banned wording next to it.
- **A-ANGLES.04** Change only one thing between versions and keep the same channel, audience, and destination link. Before posting, write the guess being tested, how long the test runs, the number that counts as a win, and the cost in time or money.  
  _Done when:_ A test plan written before the first post, showing the guess, the duration, the win number, and the cost.
- **A-ANGLES.05** Choose the main number: the goal's metric, shown with this step (for example link clicks divided by views, followers gained, or purchases). Likes are supporting information only, and state when the test stops.  
  _Done when:_ The main number, the rule for stopping, and the versions ready to be written as posts.

**Hand back:** `test_guess`, `angles`, `facts_used`, `win_rule`

**If stuck:**
- `no_main_motive`: If no main motive has been chosen, go back and choose one before writing angles.
- `angle_needs_unproven_claim`: If an angle only works with a claim that has no proof, rewrite it as an invitation to try or drop the angle.
- `too_few_views_expected`: If the account is too small for the versions to get comparable views, say so and report the result as an early signal, not as proof.
- `cannot_measure_main_number`: If the goal's main number cannot be read anywhere, ask the owner how it can be checked, and do not declare a winner from likes.

### 8. 準備TikTok Ads帳號、登入與授權

準備TikTok Ads帳號、登入與授權

- **C-TIKTOK_ADS-ACCESS.01** 核對Business Center與advertiser ID、角色、地區、幣別及時區  
  _Done when:_ advertiser資料讀回
- **C-TIKTOK_ADS-ACCESS.02** 沿既有登入／OAuth列出可操作帳號，真人驗證與企業文件交本人  
  _Done when:_ 登入與授權狀態
- **C-TIKTOK_ADS-ACCESS.03** 讀付款、帳號資格及現有pixel／Events API資料；不建立新追蹤碼  
  _Done when:_ 付款／事件可用性
- **C-TIKTOK_ADS-ACCESS.04** Spark Ads逐筆核對創作者授權碼／期間；非Spark也要素材商用權  
  _Done when:_ 授權範圍與到期時間
- **C-TIKTOK_ADS-ACCESS.05** 讀本輪campaign／ad group／ad狀態與上限，無範圍不啟用  
  _Done when:_ 物件allowlist與budget
- **C-TIKTOK_ADS-ACCESS.06** 讀影片處理／審核及連結實際狀態，不把草稿當配送  
  _Done when:_ processing、review、delivery分開

**Hand back:** `subject_id`, `brand_match`, `actual_scopes`, `observed_at`

**If stuck:**
- `spark_permission_expired`: 停止該素材啟用，改已授權素材或等待創作者新授權。
- `event_unavailable`: 等待資料或選可核對目標，不虛構購買。
- `video_review_pending`: 保留ad ID等待審核，不重建同ad。

### 9. Write the post from proven facts

Write the post or message that opens with the buyer's own situation and offers one true step forward, because specific, believable copy is what makes a reader act.

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
- `text_too_long`: If the text is over the channel's length limit, cut it to one situation, one benefit, and one link.

### 10. 製作不露臉影片與產品示範

製作不露臉影片與產品示範

- **S13.01** 確認影片目的與格式：讀用途、長度、比例與示範要求。  
  _Done when:_ 這支影片要說服誰清楚。
- **S13.02** 盤點真實畫面與素材權：確認既有錄影、截圖、配音及素材可用。  
  _Done when:_ 關鍵功能有真實畫面。
- **S13.03** 準備腳本與鏡頭順序：由S11腳本安排開頭、操作、結果與行動入口。  
  _Done when:_ 每段對得上現有素材。
- **S13.04** 取得允許的示範畫面：用既有素材或已准許示範環境錄製；真人節點另記。  
  _Done when:_ 畫面真實且不暴露客戶私密資料。
- **S13.05** 製作配音與字幕：用可用且有權使用的方法完成。  
  _Done when:_ 內容與腳本一致。
- **S13.06** 剪輯完整影片：完成畫面、字幕、節奏與片尾。  
  _Done when:_ 取得影片檔而非只有腳本。
- **S13.07** 檢查影音與事實：實際播放，核對聲音、字幕、功能畫面與敏感內容。  
  _Done when:_ 片頭、中段、結尾均正常。
- **S13.08** 輸出與轉換格式：依支援渠道輸出長短與比例版本。  
  _Done when:_ 格式、容量、長度符合要求。
- **S13.09** 準備封面及發布資料：將封面需求交S12，標題與說明交S11。  
  _Done when:_ S14或S31有完整發布包。
- **S13.10** 保存並交接：記錄版本、來源、字幕、檔案與用途。  
  _Done when:_ 下一步可讀取、播放與上傳。

**Hand back:** `actual_file`, `decoded_duration`, `dimensions`, `sha256`, `playback_readback`

### 11. TikTok Ads轉換歸因與全成本核對 (baseline numbers)

TikTok Ads轉換歸因與全成本核對

- **C-TA-METRICS.01** 以TikTok Ads精確帳號／物件ID讀本輪開始後的新報表，記原幣、時區與attribution window  
  _Done when:_ native account／window／currency
- **C-TA-METRICS.02** 讀spend、選定click／conversion action與樣本，未成熟轉換不補0  
  _Done when:_ raw numerator/denominator
- **C-TA-METRICS.03** 用本品牌現有CRM／金流核對qualified leads、external purchases、refunds及canonical order IDs  
  _Done when:_ sources與economic IDs
- **C-TA-METRICS.04** 核對八類成本、未來交付保留款與歸因完整性；平台ROAS不是本人淨收入  
  _Done when:_ money_events與limitations
- **C-TA-METRICS.05** 同口徑比較基準與當前，交goal_observation，不在讀數工作偷改廣告  
  _Done when:_ goal_observation

**If stuck:**
- `spark_permission_expired`: 停止該素材啟用，改已授權素材或等待創作者新授權。
- `event_unavailable`: 等待資料或選可核對目標，不虛構購買。
- `video_review_pending`: 保留ad ID等待審核，不重建同ad。

### 12. TikTok Ads影片PAUSED測試建立

TikTok Ads影片PAUSED測試建立

- **C-TA-DRAFT.01** 核對advertiser、Spark／非Spark身份及素材權利／有效期  
  _Done when:_ identity與rights
- **C-TA-DRAFT.02** 讀目前ad group目標、placement與影片規格，不套其他平台選項  
  _Done when:_ schema
- **C-TA-DRAFT.03** 把caption、CTA、既有目的地、每日／總額及PAUSED寫入草稿  
  _Done when:_ draft manifest
- **C-TA-DRAFT.04** prepare後建本輪campaign/ad group/ad並保存上傳／物件ID  
  _Done when:_ operation keys
- **C-TA-DRAFT.05** 讀回status、審核、身份、link及金額，processing不當配送  
  _Done when:_ ad_objects與delivery_state

**Hand back:** `original_object_ids`, `effective_status`, `native_budget_readback`, `review_or_delivery_state`

**If stuck:**
- `spark_permission_expired`: 停止該素材啟用，改已授權素材或等待創作者新授權。
- `event_unavailable`: 等待資料或選可核對目標，不虛構購買。
- `video_review_pending`: 保留ad ID等待審核，不重建同ad。

### 13. TikTok Ads單組啟用

TikTok Ads單組啟用

- **C-TA-ACTIVATE.01** 重讀advertiser ID、Spark授權與campaign/ad group/ad，只選本輪allowlist物件  
  _Done when:_ identity manifest
- **C-TA-ACTIVATE.02** 核對有效activate_ads範圍、原幣每日／總額及到期，零預算不能啟用  
  _Done when:_ grant與budget
- **C-TA-ACTIVATE.03** 確認草稿已通過素材／目的地核對；平台審核中另標，不繞審核  
  _Done when:_ draft/readback
- **C-TA-ACTIVATE.04** prepare後只啟用本輪ID，不啟動其他草稿或自動加預算  
  _Done when:_ operation_key
- **C-TA-ACTIVATE.05** 讀回status、effective delivery與budget，安排授權到期停止  
  _Done when:_ ad_objects與delivery_state

**Hand back:** `original_object_ids`, `effective_status`, `native_budget_readback`, `review_or_delivery_state`

**If stuck:**
- `spark_permission_expired`: 停止該素材啟用，改已授權素材或等待創作者新授權。
- `event_unavailable`: 等待資料或選可核對目標，不虛構購買。
- `video_review_pending`: 保留ad ID等待審核，不重建同ad。

### 14. TikTok Ads轉換歸因與全成本核對 (result numbers)

TikTok Ads轉換歸因與全成本核對

- **C-TA-METRICS.01** 以TikTok Ads精確帳號／物件ID讀本輪開始後的新報表，記原幣、時區與attribution window  
  _Done when:_ native account／window／currency
- **C-TA-METRICS.02** 讀spend、選定click／conversion action與樣本，未成熟轉換不補0  
  _Done when:_ raw numerator/denominator
- **C-TA-METRICS.03** 用本品牌現有CRM／金流核對qualified leads、external purchases、refunds及canonical order IDs  
  _Done when:_ sources與economic IDs
- **C-TA-METRICS.04** 核對八類成本、未來交付保留款與歸因完整性；平台ROAS不是本人淨收入  
  _Done when:_ money_events與limitations
- **C-TA-METRICS.05** 同口徑比較基準與當前，交goal_observation，不在讀數工作偷改廣告  
  _Done when:_ goal_observation

**If stuck:**
- `spark_permission_expired`: 停止該素材啟用，改已授權素材或等待創作者新授權。
- `event_unavailable`: 等待資料或選可核對目標，不虛構購買。
- `video_review_pending`: 保留ad ID等待審核，不重建同ad。

### 15. TikTok Ads觀察後只暫停本輪測試物件

TikTok Ads觀察後只暫停本輪測試物件

- **C-TA-STOP.01** 從本輪成功activate操作讀campaign／ad group／ad IDs，不用帳號全部物件清單當範圍  
  _Done when:_ owned active object IDs
- **C-TA-STOP.02** 核對本輪觀察窗及已存報表，保留原素材、預算和版本  
  _Done when:_ observation evidence
- **C-TA-STOP.03** prepare後只pause本輪已核對IDs；不取消訂單、刪campaign或動其他品牌  
  _Done when:_ scoped pause operation
- **C-TA-STOP.04** 讀effective status已不配送；逾時先對帳，不能標已停止  
  _Done when:_ ad_objects與delivery_state
- **C-TA-STOP.05** 下一輪另用單一變數測試與原範圍，暫停不擴大預算或授權  
  _Done when:_ changes與next-test boundary

**Hand back:** `original_object_ids`, `effective_status`, `native_budget_readback`, `review_or_delivery_state`

**If stuck:**
- `spark_permission_expired`: 停止該素材啟用，改已授權素材或等待創作者新授權。
- `event_unavailable`: 等待資料或選可核對目標，不虛構購買。
- `video_review_pending`: 保留ad ID等待審核，不重建同ad。
