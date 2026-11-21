# Reddit對話接成已核對外部購買

- **Goal id:** `G-RD-PURCHASES`
- **Language:** 繁體中文
- **Channel:** reddit
- **Metric:** `external_purchases` = `external_purchases`, should increase
- **Observation window:** 48 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (redo `A-SEGMENTS`), motivation (redo `A-MOTIVES`), angle (redo `A-ANGLES`), query (redo `C-RD-INTENT`), message (redo `A-COPY`), data (redo `C-RD-METRICS`)

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

### 8. 準備Reddit帳號、登入與授權

準備Reddit帳號、登入與授權

- **C-REDDIT-ACCESS.01** 核對目標username與已授權工具，先讀社群原文和目前版規再決定是否需要登入  
  _Done when:_ username、原文與rules URL
- **C-REDDIT-ACCESS.02** 登入使用官方流程；商用API資料使用另核對買家現有許可，不能因公開頁就當任意批量API權限  
  _Done when:_ 登入與資料取得依據
- **C-REDDIT-ACCESS.03** 確認社群自推、連結、帳齡／karma、flair與私訊規則，不主動累積假互動  
  _Done when:_ 規則全文與核對時間
- **C-REDDIT-ACCESS.04** 帳號資格不足、CAPTCHA或限制由本人處理；不建立替身帳號繞限制  
  _Done when:_ 限制種類與續接位置
- **C-REDDIT-ACCESS.05** 核對是否已有本品牌在原串回覆、被移除或被要求停止  
  _Done when:_ 原串歷史與去重鍵
- **C-REDDIT-ACCESS.06** 讀目前可用的comment／post工具；執行前讀回品牌揭露方式與可用回執  
  _Done when:_ 允許動作與回執能力

**Hand back:** `subject_id`, `brand_match`, `actual_scopes`, `observed_at`

**If stuck:**
- `community_no_promo`: 排除此社群推廣，不換拼字或私訊規避。
- `removed_by_automod`: 保留原comment ID與移除原因，不重貼；有正常申訴入口才準備說明。
- `api_commercial_permission`: 等待買家現有授權，不能自行購買或聲稱免費商用。
- `old_or_resolved_thread`: 排除已解決／過期需求，不做銷售跟進。
- `no_results`: 修正問題詞與社群假設，回報真實零則。

### 9. Reddit子版需求與替代方案搜尋

Reddit子版需求與替代方案搜尋

- **C-RD-INTENT.01** 先讀目標subreddit版規，再以痛點詞／alternative詞搭時間篩選  
  _Done when:_ rules URL、query與time filter
- **C-RD-INTENT.02** 開原post及comments讀當前解法、角色與是否已解決  
  _Done when:_ post fullname、author與context
- **C-RD-INTENT.03** 排除jobs、自推、買家不符、刪除及舊需求，保存明確理由  
  _Done when:_ excluded
- **C-RD-INTENT.04** 將需求原話逐字保留最小引句，連到產品fact_ids及適配原因  
  _Done when:_ evidence_quote與fit
- **C-RD-INTENT.05** 以允許資料路徑保存cursor；交demand_posts，不假湊目標數  
  _Done when:_ demand_posts與cursor

**Hand back:** `original_url`, `identity`, `observed_need`, `inferred_fit_separately`, `exclusions`

**If stuck:**
- `community_no_promo`: 排除此社群推廣，不換拼字或私訊規避。
- `removed_by_automod`: 保留原comment ID與移除原因，不重貼；有正常申訴入口才準備說明。
- `api_commercial_permission`: 等待買家現有授權，不能自行購買或聲稱免費商用。
- `old_or_resolved_thread`: 排除已解決／過期需求，不做銷售跟進。
- `no_results`: 修正問題詞與社群假設，回報真實零則。

### 10. Reddit需求回覆後實際結果 (baseline numbers)

Reddit需求回覆後實際結果

- **C-RD-METRICS.01** 列本輪post/comment IDs及已核對公開可見狀態  
  _Done when:_ permalinks與visibility
- **C-RD-METRICS.02** 只計新買方回覆、已解決、要求連結／示範，不把upvotes當成交  
  _Done when:_ qualified events
- **C-RD-METRICS.03** 從已接CRM與付款來源對應同人／訂單，不能把未回覆補成興趣  
  _Done when:_ CRM與economic IDs
- **C-RD-METRICS.04** 核對網站來源與成本，明示匿名流量歸因限制  
  _Done when:_ observations與limitations

**If stuck:**
- `community_no_promo`: 排除此社群推廣，不換拼字或私訊規避。
- `removed_by_automod`: 保留原comment ID與移除原因，不重貼；有正常申訴入口才準備說明。
- `api_commercial_permission`: 等待買家現有授權，不能自行購買或聲稱免費商用。
- `old_or_resolved_thread`: 排除已解決／過期需求，不做銷售跟進。
- `no_results`: 修正問題詞與社群假設，回報真實零則。

### 11. Reddit版規內的相關答案

Reddit版規內的相關答案

- **C-RD-REPLY.01** 核對subreddit規則與原串最新答案，不以私訊繞自推規則  
  _Done when:_ 原對象與原串ID
- **C-RD-REPLY.02** 重讀需求原話、時間及CRM已回／停止狀態  
  _Done when:_ source_event_id與contact_id
- **C-RD-REPLY.03** 用已核對事實先解決眼前問題，揭露品牌關係；未提出要求不轉冷郵件  
  _Done when:_ text與fact_ids
- **C-RD-REPLY.04** 先準備單筆reply意圖，核對目的地與冷卻限制  
  _Done when:_ operation_key
- **C-RD-REPLY.05** 讀回平台message/comment ID、全文與時間；未知先對帳，更新CRM  
  _Done when:_ messages

**Hand back:** `message_id`, `actual_recipient`, `reply_parent_if_reply`, `delivery_or_pending_state`, `readback`

**If stuck:**
- `community_no_promo`: 排除此社群推廣，不換拼字或私訊規避。
- `removed_by_automod`: 保留原comment ID與移除原因，不重貼；有正常申訴入口才準備說明。
- `api_commercial_permission`: 等待買家現有授權，不能自行購買或聲稱免費商用。
- `old_or_resolved_thread`: 排除已解決／過期需求，不做銷售跟進。
- `no_results`: 修正問題詞與社群假設，回報真實零則。

### 12. Reddit需求回覆後實際結果 (result numbers)

Reddit需求回覆後實際結果

- **C-RD-METRICS.01** 列本輪post/comment IDs及已核對公開可見狀態  
  _Done when:_ permalinks與visibility
- **C-RD-METRICS.02** 只計新買方回覆、已解決、要求連結／示範，不把upvotes當成交  
  _Done when:_ qualified events
- **C-RD-METRICS.03** 從已接CRM與付款來源對應同人／訂單，不能把未回覆補成興趣  
  _Done when:_ CRM與economic IDs
- **C-RD-METRICS.04** 核對網站來源與成本，明示匿名流量歸因限制  
  _Done when:_ observations與limitations

**If stuck:**
- `community_no_promo`: 排除此社群推廣，不換拼字或私訊規避。
- `removed_by_automod`: 保留原comment ID與移除原因，不重貼；有正常申訴入口才準備說明。
- `api_commercial_permission`: 等待買家現有授權，不能自行購買或聲稱免費商用。
- `old_or_resolved_thread`: 排除已解決／過期需求，不做銷售跟進。
- `no_results`: 修正問題詞與社群假設，回報真實零則。
