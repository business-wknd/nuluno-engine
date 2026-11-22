# 提高示範活動後外部付費比例

- **Goal id:** `G-WB-PURCHASE`
- **Language:** English (research and messaging steps) and 繁體中文 (channel steps)
- **Channel:** webinar
- **Metric:** `purchase_rate` = `external_purchases` / `attendees`, should increase
- **Observation window:** 168 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), invite (the next round starts with `A-ANGLES`), data (the next round starts with `C-WB-METRICS`)

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

### 8. 準備線上示範活動帳號、登入與授權

準備線上示範活動帳號、登入與授權

- **C-WEBINAR-ACCESS.01** 核對既有Zoom或會議服務的品牌host帳號、建立權與方案限制  
  _Done when:_ host ID與可用能力
- **C-WEBINAR-ACCESS.02** 官方登入／SSO由本人完成；不可新增付費方案以通過建會  
  _Done when:_ 登入與方案限制
- **C-WEBINAR-ACCESS.03** 核對活動時區、現有產品主講人、容量與錄影範圍  
  _Done when:_ 活動條件與授權
- **C-WEBINAR-ACCESS.04** 沿既有報名／會議功能建立，不改產品註冊或追蹤碼  
  _Done when:_ 外部工具入口
- **C-WEBINAR-ACCESS.05** 主講、錄影與參與同意需依既有條件；不能假裝AI已能主持真人課  
  _Done when:_ 主持人與錄影條件
- **C-WEBINAR-ACCESS.06** 會前核對報名與加入連結，實際出席／問答等待會後資料  
  _Done when:_ 報名、加入、出席分開

**Hand back:** `subject_id`, `brand_match`, `actual_scopes`, `observed_at`

**If stuck:**
- `plan_capacity_limit`: 顯示可用容量，不升級購買，等待本人或縮既定範圍。
- `host_not_confirmed`: 準備資料但不假裝活動已可交付。
- `attendance_pending`: 等meeting_completed／正式匯出，不捏造出席。

### 9. 活動報名到實際出席及成交核對 (baseline numbers)

活動報名到實際出席及成交核對

- **C-WB-METRICS.01** 讀同event ID的registration與attendance匯出，核對時區與去重  
  _Done when:_ event/window
- **C-WB-METRICS.02** 分報名、實際加入、停留及提問，未舉辦不填出席數  
  _Done when:_ raw metrics
- **C-WB-METRICS.03** 依實際問題接S19答案與可聯絡跟進，不把報名當全面行銷同意  
  _Done when:_ questions與consent
- **C-WB-METRICS.04** 核對現有交易、退款、主講／軟體／交付成本與歸因限制  
  _Done when:_ goal_observation與money_events

**If stuck:**
- `plan_capacity_limit`: 顯示可用容量，不升級購買，等待本人或縮既定範圍。
- `host_not_confirmed`: 準備資料但不假裝活動已可交付。
- `attendance_pending`: 等meeting_completed／正式匯出，不捏造出席。

### 10. 建立既有產品線上示範活動

建立既有產品線上示範活動

- **C-WB-SCHEDULE.01** 核對目標受眾、現有產品能力、真人主講人與可交付時段  
  _Done when:_ event brief
- **C-WB-SCHEDULE.02** 讀目前Zoom／會議工具schema、host與時區，沿既有方案  
  _Done when:_ host與schema
- **C-WB-SCHEDULE.03** 用既有報名入口和會議服務準備事件，不改產品註冊  
  _Done when:_ registration/join URLs
- **C-WB-SCHEDULE.04** prepare後建立本事件，讀回日期時區、容量與加入權限  
  _Done when:_ operation key與event ID
- **C-WB-SCHEDULE.05** 未舉辦時交waiting_external等待meeting_completed，不造出席／錄影  
  _Done when:_ event及wait_for

**Hand back:** `event_id`, `event_url`, `host_confirmed_or_pending`, `attendance_source`

**If stuck:**
- `plan_capacity_limit`: 顯示可用容量，不升級購買，等待本人或縮既定範圍。
- `host_not_confirmed`: 準備資料但不假裝活動已可交付。
- `attendance_pending`: 等meeting_completed／正式匯出，不捏造出席。

### 11. 向可聯絡對象邀請既有示範活動

向可聯絡對象邀請既有示範活動

- **C-WB-INVITE.01** 核對活動真實存在、時區、主講人與既有報名／加入入口  
  _Done when:_ event ID與links
- **C-WB-INVITE.02** 選已同意或正在原串要求示範的對象，取消已拒絕／購買舊跟進  
  _Done when:_ contact IDs與trigger
- **C-WB-INVITE.03** 寫對應需求的一次邀請，清楚時區與內容，不虛構限額  
  _Done when:_ personal text
- **C-WB-INVITE.04** prepare後以品牌正確渠道送出並讀回  
  _Done when:_ operation key與messages
- **C-WB-INVITE.05** 報名、到場、觀看與成交分開等真實事件  
  _Done when:_ state與limitations

**Hand back:** `message_id`, `actual_recipient`, `reply_parent_if_reply`, `delivery_or_pending_state`, `readback`

**If stuck:**
- `plan_capacity_limit`: 顯示可用容量，不升級購買，等待本人或縮既定範圍。
- `host_not_confirmed`: 準備資料但不假裝活動已可交付。
- `attendance_pending`: 等meeting_completed／正式匯出，不捏造出席。

### 12. 活動報名到實際出席及成交核對 (result numbers)

活動報名到實際出席及成交核對

- **C-WB-METRICS.01** 讀同event ID的registration與attendance匯出，核對時區與去重  
  _Done when:_ event/window
- **C-WB-METRICS.02** 分報名、實際加入、停留及提問，未舉辦不填出席數  
  _Done when:_ raw metrics
- **C-WB-METRICS.03** 依實際問題接S19答案與可聯絡跟進，不把報名當全面行銷同意  
  _Done when:_ questions與consent
- **C-WB-METRICS.04** 核對現有交易、退款、主講／軟體／交付成本與歸因限制  
  _Done when:_ goal_observation與money_events

**If stuck:**
- `plan_capacity_limit`: 顯示可用容量，不升級購買，等待本人或縮既定範圍。
- `host_not_confirmed`: 準備資料但不假裝活動已可交付。
- `attendance_pending`: 等meeting_completed／正式匯出，不捏造出席。
