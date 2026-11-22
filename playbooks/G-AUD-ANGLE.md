# 驗證哪個具體銷售角度帶來有效詢問

- **Goal id:** `G-AUD-ANGLE`
- **Language:** English (research and messaging steps) and 繁體中文 (channel steps)
- **Channel:** audience
- **Metric:** `qualified_inquiry_rate` = `qualified_inquiries` / `eligible_exposures`, should increase
- **Observation window:** 168 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), data (the next round starts with `S33`)

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

### 2. 找出誰會買、為什麼現在買

找出誰會買、為什麼現在買

- **S02.01** 讀取產品與這輪目標：確認要找首批用戶、試用、購買或續購。  
  _Done when:_ 研究目標與現有方案相符。
- **S02.02** 列出候選使用情境：依實際任務、替代方案與使用者類型提出候選分組。  
  _Done when:_ 每組描述的是具體情境。
- **S02.03** 收集需求原話：查可用討論、詢問、評價、訪談與交易背景。  
  _Done when:_ 原話有日期、來源及情境。
- **S02.04** 區分使用者與付款者：辨識誰操作、誰受益、誰付錢或批准。  
  _Done when:_ 角色有依據，未知者保留。
- **S02.05** 整理想改善的結果：記錄省時、省錢、收入、便利、安心、身分或其他實際動機。  
  _Done when:_ 動機連到需求原話與工作情境。
- **S02.06** 找出現在開始找解法的原因：核對事件、期限、工作量或替代方案失效。  
  _Done when:_ 有可觀察的觸發條件。
- **S02.07** 整理顧慮與不購買原因：記錄信任、價格、學習成本、既有習慣與風險等。  
  _Done when:_ 能對應真實疑問。
- **S02.08** 判斷購買階段：分清剛發現問題、比較方案、準備採購及已買等狀態。  
  _Done when:_ 內容與跟進可按狀態選用。
- **S02.09** 評估可接觸程度與價值：比較需求強度、可達渠道、成本與適配。  
  _Done when:_ 優先順序有理由。
- **S02.10** 交付客群與訊息對照：列每組的情境、動機、證據、顧慮與可測切角。  
  _Done when:_ S06、S08、S10、S30能直接取用。
- **S02.11** 接收實際結果修訂：以新回覆、試用及付款更新分組。  
  _Done when:_ 保留前後版本與修改理由。

**Hand back:** `sourced_segments`, `hypotheses`, `unknowns`

### 3. Collect real buyer quotes

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

### 8. Write the post from proven facts

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

### 9. 彙整成效並核對付款與成本 (baseline numbers)

彙整成效並核對付款與成本

- **S33.01** 盤點這輪可用資料：列平台報表、外部表單、訊息、付款與成本來源。  
  _Done when:_ 每個來源有權限及範圍。
- **S33.02** 確定期間、時區與幣別：按工作計畫統一比較口徑。  
  _Done when:_ 能區分不同貨幣與日期。
- **S33.03** 讀取最新實際資料：按可用工具取得必要欄位與更新時間。  
  _Done when:_ 欄位來自實際規格。
- **S33.04** 核對內容與廣告版本：把流量、訊息及廣告ID接到對應工作。  
  _Done when:_ 知道哪個版本產生何種可見結果。
- **S33.05** 清理重複與測試資料：按原始ID、事件、訂單與明確測試標記去重。  
  _Done when:_ 測試不混成外部新增銷售。
- **S33.06** 核對名單與回覆品質：區分留下資料、可聯絡、有需求與已購買。  
  _Done when:_ 各階段分母清楚。
- **S33.07** 核對付款與退款：回到可用交易紀錄確認金額、時間與狀態。  
  _Done when:_ 未付合約、未收訂單與實收分開。
- **S33.08** 整理全部可得成本：納廣告、平台、金流、佣金、工具、交付與人事等。  
  _Done when:_ 每筆有來源或標未知。
- **S33.09** 處理未來交付與份額：需要時列保留款、待交付成本與可取得份額。  
  _Done when:_ 預收與可自由使用金額分開。
- **S33.10** 計算可合理判斷的結果：實際計算率、費用、已核對貢獻及缺口。  
  _Done when:_ 分母與公式可查。
- **S33.11** 註明歸因與增量限制：分平台自報來源、可追蹤關聯及有對照的增加結果。  
  _Done when:_ 沒有把相關當因果。
- **S33.12** 輸出與安排更新：交S32／S34資料版本、時間與缺件。  
  _Done when:_ 下一輪知道資料是否夠新。

### 10. 彙整成效並核對付款與成本 (result numbers)

彙整成效並核對付款與成本

- **S33.01** 盤點這輪可用資料：列平台報表、外部表單、訊息、付款與成本來源。  
  _Done when:_ 每個來源有權限及範圍。
- **S33.02** 確定期間、時區與幣別：按工作計畫統一比較口徑。  
  _Done when:_ 能區分不同貨幣與日期。
- **S33.03** 讀取最新實際資料：按可用工具取得必要欄位與更新時間。  
  _Done when:_ 欄位來自實際規格。
- **S33.04** 核對內容與廣告版本：把流量、訊息及廣告ID接到對應工作。  
  _Done when:_ 知道哪個版本產生何種可見結果。
- **S33.05** 清理重複與測試資料：按原始ID、事件、訂單與明確測試標記去重。  
  _Done when:_ 測試不混成外部新增銷售。
- **S33.06** 核對名單與回覆品質：區分留下資料、可聯絡、有需求與已購買。  
  _Done when:_ 各階段分母清楚。
- **S33.07** 核對付款與退款：回到可用交易紀錄確認金額、時間與狀態。  
  _Done when:_ 未付合約、未收訂單與實收分開。
- **S33.08** 整理全部可得成本：納廣告、平台、金流、佣金、工具、交付與人事等。  
  _Done when:_ 每筆有來源或標未知。
- **S33.09** 處理未來交付與份額：需要時列保留款、待交付成本與可取得份額。  
  _Done when:_ 預收與可自由使用金額分開。
- **S33.10** 計算可合理判斷的結果：實際計算率、費用、已核對貢獻及缺口。  
  _Done when:_ 分母與公式可查。
- **S33.11** 註明歸因與增量限制：分平台自報來源、可追蹤關聯及有對照的增加結果。  
  _Done when:_ 沒有把相關當因果。
- **S33.12** 輸出與安排更新：交S32／S34資料版本、時間與缺件。  
  _Done when:_ 下一輪知道資料是否夠新。
