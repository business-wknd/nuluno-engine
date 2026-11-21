# Meta Ads提高點擊到既有網站載入率

- **Goal id:** `G-META-LANDING-RATE`
- **Status:** experimental
- **Channel:** meta_ads
- **Metric:** `landing_rate` = `landing_page_views` / `link_clicks`, should increase
- **Observation window:** 72 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (redo `A-SEGMENTS`), motivation (redo `A-MOTIVES`), angle (redo `A-ANGLES`), creative (redo `C-META-CREATIVE`), delivery (redo `C-META_ADS-ACCESS`), data (redo `C-META-METRICS`)

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

### 8. 準備Meta Ads帳號、登入與授權

準備Meta Ads帳號、登入與授權

- **C-META_ADS-ACCESS.01** 盤點已連接工具／官方Ads Manager；讀目前可以列帳號、素材、campaign及insights的schema  
  _Done when:_ 工具清單及實際read欄位
- **C-META_ADS-ACCESS.02** 以本人既有登入列出可用Business Portfolio與ad account；核對精確帳號ID和幣別／時區  
  _Done when:_ Business ID、ad account ID、幣別時區
- **C-META_ADS-ACCESS.03** 核對本品牌Page／IG與廣告帳號授權關係；選不到目標身分就卡廣告，不選別品牌代替  
  _Done when:_ Page/IG與管理角色證據
- **C-META_ADS-ACCESS.04** 讀Account Quality及付款狀態，分清單一ad拒登、帳號限制、付款問題和權限不足  
  _Done when:_ 原始限制種類與notice ID
- **C-META_ADS-ACCESS.05** 連接器回done仍檢查實際資料列，方案限制文字不當數字；不可用寫入則保留官方允許UI路徑  
  _Done when:_ 數值型別、來源與缺失能力
- **C-META_ADS-ACCESS.06** OAuth正常更新只用既有範圍；2FA／身分／新增付款與條款交本人  
  _Done when:_ 憑證更新或本人checkpoint
- **C-META_ADS-ACCESS.07** 新帳號建立僅在明確授權及正常官方入口下操作；建立失敗不重複造帳號  
  _Done when:_ 已建立ID或失敗續接
- **C-META_ADS-ACCESS.08** 對任何寫入核對本輪物件allowlist、每日／總額與到期停止；零預算只準備OFF草稿  
  _Done when:_ 帳號身分、物件及費用上限讀回

**Hand back:** `subject_id`, `brand_match`, `actual_scopes`, `observed_at`

**If stuck:**
- `connector_plan_string`: 拒當數字，保存限制原因，改可用的正式報表讀取。
- `write_disabled`: 不升級連接、不改成別品牌；在原範圍內用官方介面或等待能力。
- `wrong_page`: 停止發布，定位本品牌Page；素材研究繼續。
- `unpublished_drafts`: 僅開本輪campaign/adset/ad，不用Publish all改其他草稿。
- `billing_or_restriction`: 保存實際notice、金額未知與官方下一步；不代付新費用。
- `expired_token`: 最多正常刷新一次並重讀身分，仍失敗則本人授權。
- `unknown_write`: 以operation key及物件ID對帳，不重建或重複啟用。

### 9. Meta Ads基準、歸因與全成本盤點

Meta Ads基準、歸因與全成本盤點

- **C-META-BASELINE.01** 按指定campaign/adset/ad IDs讀status、effective_status、budget、spend及日期  
  _Done when:_ IDs/window/account currency
- **C-META-BASELINE.02** 分impressions、link clicks、landing page views與選定conversion action  
  _Done when:_ raw metrics與action type
- **C-META-BASELINE.03** 核對attribution window、account timezone和轉換延遲，兩期間口徑一致  
  _Done when:_ attribution model
- **C-META-BASELINE.04** 付款退款回現有來源去重；平台報告purchase不等於銀行實收  
  _Done when:_ money_events/economic IDs
- **C-META-BASELINE.05** 未知成本／追蹤欄位保留null，無可比資料等待，不先改廣告  
  _Done when:_ goal_observation與limitations

**Hand back:** `goal_observation`, `original_metric_fields`, `source_read_time`, `missing_components`, `economic_ids_if_required`

**If stuck:**
- `connector_plan_string`: 拒當數字，保存限制原因，改可用的正式報表讀取。
- `write_disabled`: 不升級連接、不改成別品牌；在原範圍內用官方介面或等待能力。
- `wrong_page`: 停止發布，定位本品牌Page；素材研究繼續。
- `unpublished_drafts`: 僅開本輪campaign/adset/ad，不用Publish all改其他草稿。
- `billing_or_restriction`: 保存實際notice、金額未知與官方下一步；不代付新費用。
- `expired_token`: 最多正常刷新一次並重讀身分，仍失敗則本人授權。
- `unknown_write`: 以operation key及物件ID對帳，不重建或重複啟用。

### 10. Meta素材疲乏與單一變數測試設計

Meta素材疲乏與單一變數測試設計

- **C-META-CREATIVE.01** 讀本輪已核對ads、素材ID、曝光、頻率、CPA及最少觀察時間  
  _Done when:_ baseline與creative IDs
- **C-META-CREATIVE.02** 分無配送／審核／受眾問題／素材疲乏，不能因一天差就判疲乏  
  _Done when:_ diagnosis及evidence
- **C-META-CREATIVE.03** 從受眾動機與原話選一個鉤子或格式，控制其他差異  
  _Done when:_ hypothesis與changed variable
- **C-META-CREATIVE.04** 為每版列文字、圖片／影片需求、fact_ids和觀測窗口  
  _Done when:_ content_batch
- **C-META-CREATIVE.05** 預算／身分／目的地沿本輪已確認範圍，需超出就保留待決定  
  _Done when:_ limits與test plan

**Hand back:** `hypothesis`, `variants`, `fact_ids`, `acceptance_rule`

**If stuck:**
- `connector_plan_string`: 拒當數字，保存限制原因，改可用的正式報表讀取。
- `write_disabled`: 不升級連接、不改成別品牌；在原範圍內用官方介面或等待能力。
- `wrong_page`: 停止發布，定位本品牌Page；素材研究繼續。
- `unpublished_drafts`: 僅開本輪campaign/adset/ad，不用Publish all改其他草稿。
- `billing_or_restriction`: 保存實際notice、金額未知與官方下一步；不代付新費用。
- `expired_token`: 最多正常刷新一次並重讀身分，仍失敗則本人授權。
- `unknown_write`: 以operation key及物件ID對帳，不重建或重複啟用。

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

### 13. Meta投放新觀察與付款成本核對 (baseline numbers)

Meta投放新觀察與付款成本核對

- **C-META-METRICS.01** 以Meta Ads精確帳號／物件ID讀本輪開始後的新報表，記原幣、時區與attribution window  
  _Done when:_ native account／window／currency
- **C-META-METRICS.02** 讀spend、選定click／conversion action與樣本，未成熟轉換不補0  
  _Done when:_ raw numerator/denominator
- **C-META-METRICS.03** 用本品牌現有CRM／金流核對qualified leads、external purchases、refunds及canonical order IDs  
  _Done when:_ sources與economic IDs
- **C-META-METRICS.04** 核對八類成本、未來交付保留款與歸因完整性；平台ROAS不是本人淨收入  
  _Done when:_ money_events與limitations
- **C-META-METRICS.05** 同口徑比較基準與當前，交goal_observation，不在讀數工作偷改廣告  
  _Done when:_ goal_observation

**If stuck:**
- `connector_plan_string`: 拒當數字，保存限制原因，改可用的正式報表讀取。
- `write_disabled`: 不升級連接、不改成別品牌；在原範圍內用官方介面或等待能力。
- `wrong_page`: 停止發布，定位本品牌Page；素材研究繼續。
- `unpublished_drafts`: 僅開本輪campaign/adset/ad，不用Publish all改其他草稿。
- `billing_or_restriction`: 保存實際notice、金額未知與官方下一步；不代付新費用。
- `expired_token`: 最多正常刷新一次並重讀身分，仍失敗則本人授權。
- `unknown_write`: 以operation key及物件ID對帳，不重建或重複啟用。

### 14. Meta PAUSED測試廣告建立

Meta PAUSED測試廣告建立

- **C-META-DRAFT.01** 核對精確ad account、Page／IG、目標及本輪物件  
  _Done when:_ identity manifest
- **C-META-DRAFT.02** 讀campaign/adset目前schema、幣別、預算／停止時間，所有新物件PAUSED  
  _Done when:_ draft manifest
- **C-META-DRAFT.03** 素材解碼後按工具支援上傳，確認asset hash及正確預覽  
  _Done when:_ asset receipt
- **C-META-DRAFT.04** prepare後只建本輪campaign/adset/creative/ad，逐筆保存ID  
  _Done when:_ operation keys與object IDs
- **C-META-DRAFT.05** 讀回身份、目的地、每日／整輪金額、status及effective_status，零預算保持OFF  
  _Done when:_ ad_objects與delivery_state

**Hand back:** `original_object_ids`, `effective_status`, `native_budget_readback`, `review_or_delivery_state`

**If stuck:**
- `connector_plan_string`: 拒當數字，保存限制原因，改可用的正式報表讀取。
- `write_disabled`: 不升級連接、不改成別品牌；在原範圍內用官方介面或等待能力。
- `wrong_page`: 停止發布，定位本品牌Page；素材研究繼續。
- `unpublished_drafts`: 僅開本輪campaign/adset/ad，不用Publish all改其他草稿。
- `billing_or_restriction`: 保存實際notice、金額未知與官方下一步；不代付新費用。
- `expired_token`: 最多正常刷新一次並重讀身分，仍失敗則本人授權。
- `unknown_write`: 以operation key及物件ID對帳，不重建或重複啟用。

### 15. Meta明確範圍內單組啟用

Meta明確範圍內單組啟用

- **C-META-ACTIVATE.01** 重讀本輪campaign/adset/ad IDs、Page／IG與最後草稿，排除其他未發布草稿  
  _Done when:_ scope readback
- **C-META-ACTIVATE.02** 核對有效啟用授權、每日／總額、到期與正整數最小貨幣單位；零預算停止  
  _Done when:_ grant與budget
- **C-META-ACTIVATE.03** 列現值→新值→預期→回退方式，prepare activate_ads  
  _Done when:_ operation intent
- **C-META-ACTIVATE.04** 僅啟用allowlist物件，不按Publish all，不自動增加budget  
  _Done when:_ operation key與IDs
- **C-META-ACTIVATE.05** 讀回status／effective_status／budget；審核中不當配送，對帳後排停止  
  _Done when:_ ad_objects與delivery_state

**Hand back:** `original_object_ids`, `effective_status`, `native_budget_readback`, `review_or_delivery_state`

**If stuck:**
- `connector_plan_string`: 拒當數字，保存限制原因，改可用的正式報表讀取。
- `write_disabled`: 不升級連接、不改成別品牌；在原範圍內用官方介面或等待能力。
- `wrong_page`: 停止發布，定位本品牌Page；素材研究繼續。
- `unpublished_drafts`: 僅開本輪campaign/adset/ad，不用Publish all改其他草稿。
- `billing_or_restriction`: 保存實際notice、金額未知與官方下一步；不代付新費用。
- `expired_token`: 最多正常刷新一次並重讀身分，仍失敗則本人授權。
- `unknown_write`: 以operation key及物件ID對帳，不重建或重複啟用。

### 16. Meta投放新觀察與付款成本核對 (result numbers)

Meta投放新觀察與付款成本核對

- **C-META-METRICS.01** 以Meta Ads精確帳號／物件ID讀本輪開始後的新報表，記原幣、時區與attribution window  
  _Done when:_ native account／window／currency
- **C-META-METRICS.02** 讀spend、選定click／conversion action與樣本，未成熟轉換不補0  
  _Done when:_ raw numerator/denominator
- **C-META-METRICS.03** 用本品牌現有CRM／金流核對qualified leads、external purchases、refunds及canonical order IDs  
  _Done when:_ sources與economic IDs
- **C-META-METRICS.04** 核對八類成本、未來交付保留款與歸因完整性；平台ROAS不是本人淨收入  
  _Done when:_ money_events與limitations
- **C-META-METRICS.05** 同口徑比較基準與當前，交goal_observation，不在讀數工作偷改廣告  
  _Done when:_ goal_observation

**If stuck:**
- `connector_plan_string`: 拒當數字，保存限制原因，改可用的正式報表讀取。
- `write_disabled`: 不升級連接、不改成別品牌；在原範圍內用官方介面或等待能力。
- `wrong_page`: 停止發布，定位本品牌Page；素材研究繼續。
- `unpublished_drafts`: 僅開本輪campaign/adset/ad，不用Publish all改其他草稿。
- `billing_or_restriction`: 保存實際notice、金額未知與官方下一步；不代付新費用。
- `expired_token`: 最多正常刷新一次並重讀身分，仍失敗則本人授權。
- `unknown_write`: 以operation key及物件ID對帳，不重建或重複啟用。

### 17. Meta Ads觀察後只暫停本輪測試物件

Meta Ads觀察後只暫停本輪測試物件

- **C-META-STOP.01** 從本輪成功activate操作讀campaign／ad group／ad IDs，不用帳號全部物件清單當範圍  
  _Done when:_ owned active object IDs
- **C-META-STOP.02** 核對本輪觀察窗及已存報表，保留原素材、預算和版本  
  _Done when:_ observation evidence
- **C-META-STOP.03** prepare後只pause本輪已核對IDs；不取消訂單、刪campaign或動其他品牌  
  _Done when:_ scoped pause operation
- **C-META-STOP.04** 讀effective status已不配送；逾時先對帳，不能標已停止  
  _Done when:_ ad_objects與delivery_state
- **C-META-STOP.05** 下一輪另用單一變數測試與原範圍，暫停不擴大預算或授權  
  _Done when:_ changes與next-test boundary

**Hand back:** `original_object_ids`, `effective_status`, `native_budget_readback`, `review_or_delivery_state`

**If stuck:**
- `connector_plan_string`: 拒當數字，保存限制原因，改可用的正式報表讀取。
- `write_disabled`: 不升級連接、不改成別品牌；在原範圍內用官方介面或等待能力。
- `wrong_page`: 停止發布，定位本品牌Page；素材研究繼續。
- `unpublished_drafts`: 僅開本輪campaign/adset/ad，不用Publish all改其他草稿。
- `billing_or_restriction`: 保存實際notice、金額未知與官方下一步；不代付新費用。
- `expired_token`: 最多正常刷新一次並重讀身分，仍失敗則本人授權。
- `unknown_write`: 以operation key及物件ID對帳，不重建或重複啟用。
