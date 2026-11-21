# Product Hunt既有網站流量接成外部付款

- **Goal id:** `G-PH-LAUNCH-PURCHASE`
- **Language:** 繁體中文
- **Channel:** producthunt
- **Metric:** `site_purchase_rate` = `external_purchases` / `attributed_sessions`, should increase
- **Observation window:** 168 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (redo `C-PH-MAKERS`), motivation (redo `A-MOTIVES`), angle (redo `A-ANGLES`), message (redo `A-ANGLES`), data (redo `C-PH-METRICS`)

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

### 8. 準備Product Hunt帳號、登入與授權

準備Product Hunt帳號、登入與授權

- **C-PRODUCTHUNT-ACCESS.01** 先讀產品頁、makers與topics公開資料，核對當前登入是否為已授權maker  
  _Done when:_ 產品slug、maker profile與擁有權
- **C-PRODUCTHUNT-ACCESS.02** API另核對既有token、scope與商用許可；官方文件要求商用先獲許可，不能當免費名單API  
  _Done when:_ 商用許可／讀取方式
- **C-PRODUCTHUNT-ACCESS.03** 需要登入時沿官方提供方式；OAuth、本人驗證、條款確認由帳號本人完成  
  _Done when:_ 登入checkpoint
- **C-PRODUCTHUNT-ACCESS.04** Email不是標準保證欄位；只從maker本人公開網站／商務聯絡頁核對，不由username拼地址  
  _Done when:_ 公開商務來源與email或null
- **C-PRODUCTHUNT-ACCESS.05** 上架前先找現有listing與重複產品；只有本品牌有權時準備既有產品資料  
  _Done when:_ 現有listing及擁有權
- **C-PRODUCTHUNT-ACCESS.06** 核對當前launch與討論規則，不買票、不互投、不把其他makers自推當買方需求  
  _Done when:_ 當前規則與排除紀錄

**Hand back:** `subject_id`, `brand_match`, `actual_scopes`, `observed_at`

**If stuck:**
- `api_commercial_permission`: 等待既有許可或本人可用的正式資料路徑。
- `email_not_available`: 如實輸出email=null與profile來源，不猜Email。
- `duplicate_listing`: 維護已擁有listing或保存待本人，不重複上架。
- `launch_time_mismatch`: 核對平台排程時區與公開日期；草稿不當已launch。
- `maker_not_buyer`: 沒有實際需求訊號不標高意向客戶。

### 9. Write the post from proven facts

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

### 10. Product Hunt launch流量與付費結果 (baseline numbers)

Product Hunt launch流量與付費結果

- **C-PH-METRICS.01** 確認listing確實公開，保存launch時間與平台口徑  
  _Done when:_ listing/window
- **C-PH-METRICS.02** 讀可見comments／votes與既有網站referral sessions，分開分母  
  _Done when:_ raw metrics
- **C-PH-METRICS.03** maker／hunter互動不當目標買家，沒有需求不標商機  
  _Done when:_ qualified inquiries
- **C-PH-METRICS.04** 現有付款資料可對應來源才算可歸因，未設追蹤不改產品硬補  
  _Done when:_ purchases/costs/limitations

**If stuck:**
- `api_commercial_permission`: 等待既有許可或本人可用的正式資料路徑。
- `email_not_available`: 如實輸出email=null與profile來源，不猜Email。
- `duplicate_listing`: 維護已擁有listing或保存待本人，不重複上架。
- `launch_time_mismatch`: 核對平台排程時區與公開日期；草稿不當已launch。
- `maker_not_buyer`: 沒有實際需求訊號不標高意向客戶。

### 11. Product Hunt既有產品上架／維護

Product Hunt既有產品上架／維護

- **C-PH-LISTING.01** 查同產品是否已有listing並核對maker擁有權；有就不重複建  
  _Done when:_ existing listing與owner
- **C-PH-LISTING.02** 讀當前launch必填欄位與資格，只填已核對產品能力與既有網站  
  _Done when:_ requirements
- **C-PH-LISTING.03** 準備tagline、介紹、圖片和maker comment，逐項標來源／權利  
  _Done when:_ listing assets
- **C-PH-LISTING.04** 核對平台launch時區與期望日期；draft、scheduled、public分開  
  _Done when:_ schedule／timezone
- **C-PH-LISTING.05** prepare後只提交本listing，不投票、不互投、不代買曝光  
  _Done when:_ operation_key
- **C-PH-LISTING.06** 讀回listing URL、狀態、內容、網站與makers，pending則等審核事件  
  _Done when:_ listing與readback

**Hand back:** `submission_id`, `review_state`, `public_url_if_public`, `readback`

**If stuck:**
- `api_commercial_permission`: 等待既有許可或本人可用的正式資料路徑。
- `email_not_available`: 如實輸出email=null與profile來源，不猜Email。
- `duplicate_listing`: 維護已擁有listing或保存待本人，不重複上架。
- `launch_time_mismatch`: 核對平台排程時區與公開日期；草稿不當已launch。
- `maker_not_buyer`: 沒有實際需求訊號不標高意向客戶。

### 12. Product Hunt launch留言問題回覆

Product Hunt launch留言問題回覆

- **C-PH-ANSWERS.01** 讀本產品討論原串與作者問題，排除只是其他產品自推  
  _Done when:_ comment ID與question
- **C-PH-ANSWERS.02** 回現有facts核對答案，不答尚未完成的功能為已提供  
  _Done when:_ fact_ids
- **C-PH-ANSWERS.03** 保留原串回覆，不把支持投票者匯出冷郵件  
  _Done when:_ target及consent
- **C-PH-ANSWERS.04** prepare後用允許工具提交，重讀全文與作者  
  _Done when:_ operation_key與messages
- **C-PH-ANSWERS.05** 記未回答疑問與下一步，不把回覆數當銷售  
  _Done when:_ limitations

**Hand back:** `message_id`, `actual_recipient`, `reply_parent_if_reply`, `delivery_or_pending_state`, `readback`

**If stuck:**
- `api_commercial_permission`: 等待既有許可或本人可用的正式資料路徑。
- `email_not_available`: 如實輸出email=null與profile來源，不猜Email。
- `duplicate_listing`: 維護已擁有listing或保存待本人，不重複上架。
- `launch_time_mismatch`: 核對平台排程時區與公開日期；草稿不當已launch。
- `maker_not_buyer`: 沒有實際需求訊號不標高意向客戶。

### 13. Product Hunt launch流量與付費結果 (result numbers)

Product Hunt launch流量與付費結果

- **C-PH-METRICS.01** 確認listing確實公開，保存launch時間與平台口徑  
  _Done when:_ listing/window
- **C-PH-METRICS.02** 讀可見comments／votes與既有網站referral sessions，分開分母  
  _Done when:_ raw metrics
- **C-PH-METRICS.03** maker／hunter互動不當目標買家，沒有需求不標商機  
  _Done when:_ qualified inquiries
- **C-PH-METRICS.04** 現有付款資料可對應來源才算可歸因，未設追蹤不改產品硬補  
  _Done when:_ purchases/costs/limitations

**If stuck:**
- `api_commercial_permission`: 等待既有許可或本人可用的正式資料路徑。
- `email_not_available`: 如實輸出email=null與profile來源，不猜Email。
- `duplicate_listing`: 維護已擁有listing或保存待本人，不重複上架。
- `launch_time_mismatch`: 核對平台排程時區與公開日期；草稿不當已launch。
- `maker_not_buyer`: 沒有實際需求訊號不標高意向客戶。
