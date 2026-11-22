# Reddit: turn helpful replies into buyer conversations

- **Goal id:** `G-RD-REPLIES`
- **Language:** English
- **Channel:** reddit
- **Metric:** `qualified_reply_rate` = `qualified_replies` / `eligible_requests`, should increase
- **Observation window:** 48 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), query (the next round starts with `C-RD-INTENT`), message (the next round starts with `A-COPY`), data (the next round starts with `C-RD-METRICS`)

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

### 8. Confirm the Reddit account and each subreddit's rules

Settle which Reddit account posts, who presses publish, and what each target subreddit allows, so every reply or post stays within the rules and is not removed or banned.

- **C-REDDIT-ACCESS.01** Ask the owner for the Reddit username that will post. Open its public profile and note the account age, karma and recent activity, and whether its history is only about the product.  
  _Done when:_ The username, profile URL, account age, karma, and a one-line note on its history.
- **C-REDDIT-ACCESS.02** From the buyer situation, pick three to five subreddits where these buyers ask for help. For each, read the rules in the sidebar and the wiki, and copy the parts on self-promotion, links, private messages, minimum account age or karma, flair, required disclosure and promotion days.  
  _Done when:_ Each subreddit with its rules URL, the copied rule text, and the time you read it.
- **C-REDDIT-ACCESS.03** Mark each subreddit 'reply with a product mention allowed', 'story post allowed', 'answers only, no product' or 'no promotion'. If the rules are unclear, draft a short message to the moderators asking what is allowed and show it to the owner; it is sent, by the owner or by the agent's signed-in browser, only after the owner says yes.  
  _Done when:_ Each subreddit marked with what is allowed, and any moderator question with its approval.
- **C-REDDIT-ACCESS.04** Decide who publishes: the owner, or the agent's own browser if it is already signed in to that username. If nobody is signed in, the owner signs in on the official Reddit page. Never ask for a password; CAPTCHAs and checks are left to the owner.  
  _Done when:_ Who will publish, and confirmation that the right username is signed in.
- **C-REDDIT-ACCESS.05** Create a new account only if the owner asked for one in this conversation; you may use inbox_address and inbox_latest for the verification email. Use one real account only. Never create extra accounts to get around limits, never buy or trade upvotes or karma, and never ask others to vote.  
  _Done when:_ The owner's request and the new username, or a note that the existing account is used.
- **C-REDDIT-ACCESS.06** Check the account's past comments in the target subreddits, and, if whoever is signed in can open it, the account's inbox, for removals, moderator warnings, bans, or people asking the brand to stop. Note any thread where the brand already replied, so it is not answered twice.  
  _Done when:_ A list of past brand activity, removals and stop requests, or 'none found'.
- **C-REDDIT-ACCESS.07** Read Reddit pages one at a time with read_page or a browser. Do not scrape in bulk or pull data through Reddit's API for business use unless the owner already has permission for that.  
  _Done when:_ A note of how Reddit pages will be read this round.
- **C-REDDIT-ACCESS.08** Agree a one-line disclosure with the owner, for example 'Disclosure: I built this.' Then confirm whoever publishes can open the comment box in each allowed subreddit.  
  _Done when:_ The approved disclosure line, and the subreddits where the comment box opens.

**Hand back:** `username`, `subreddit_rules`, `who_publishes`, `disclosure_line`

**If stuck:**
- `community_no_promo`: If a subreddit forbids promotion, leave it out of product replies and posts; never get around it with altered spelling or private messages.
- `account_below_minimum`: If the account is too new or has too little karma for a subreddit, skip that subreddit this round and tell the owner; never farm karma or use another account.
- `owner_action_needed`: If a CAPTCHA, verification or terms screen appears, stop and tell the owner which screen to finish, then resume on the same account.
- `banned_or_removed_before`: If the account was banned or warned in a subreddit, leave that subreddit out and tell the owner.
- `api_commercial_permission`: If the round needs Reddit data beyond reading pages one at a time, wait for the owner's existing permission; never buy access or claim free business use.
- `wrong_account_signed_in`: If the signed-in account is not the agreed username, stop and ask the owner to switch or to post themselves.

### 9. Find recent Reddit posts from people who need the product

Read recent posts in the allowed subreddits and keep only those where a real person asks for what the product does, because the share of matching requests and the replies that follow depend on picking the right posts.

- **C-RD-INTENT.01** For each subreddit marked as allowed, write three to five searches from the buyer's own words, such as the problem in plain words, 'alternative to {category}', 'recommend {tool}' and 'looking for {solution}'. Search inside the subreddit, sorted by new, limited to the past month.  
  _Done when:_ Each subreddit with the searches and the time filter used.
- **C-RD-INTENT.02** Open each result and read the full post and its comments. Note what the person uses now, their role, and whether the question is already solved (a 'Solved' flair, an edit by the poster, or an accepted answer). Count every post you open as read, including the ones you drop later, so the share of matching posts is honest.  
  _Done when:_ A log of every post read, with its URL, the poster's username and a one-line summary, and the total number of posts read.
- **C-RD-INTENT.03** Drop job posts, self-promotion, posts from people who are not the buyer, deleted or removed posts, locked or archived posts, solved questions, and posts older than 30 days. Write the reason for each one.  
  _Done when:_ An excluded list, each with its URL and reason.
- **C-RD-INTENT.04** For each post you keep, copy the shortest exact quote that shows the need. Separately, write one line on why the product fits, citing the product fact it relies on, and mark it 'unsure' when the post does not say enough.  
  _Done when:_ Each kept post with its quote and a separate fit line marked 'fits' or 'unsure'.
- **C-RD-INTENT.05** Check each kept post for an earlier reply from the brand's account and drop it if one exists. Count each person once even if they posted twice.  
  _Done when:_ The kept list after removing duplicates and threads the brand already answered.
- **C-RD-INTENT.06** Hand over the kept posts, the excluded list and the counts, and note the last post read in each search so the next round continues from there. Never pad the list to reach a number; if nothing qualifies, report a real zero and say which searches or subreddits to change next.  
  _Done when:_ The final list with counts of posts read, kept and excluded, and where each search stopped.

**Hand back:** `qualified_posts`, `excluded`, `posts_read`, `searches_used`

**If stuck:**
- `community_no_promo`: If a subreddit forbids promotion, do not collect posts there for product replies; never move the conversation to private messages to get around it.
- `old_or_resolved_thread`: If a post is solved, locked, archived or older than 30 days, drop it and write the reason; never follow up on it to sell.
- `no_results`: If nothing qualifies, report a real zero, change the searches toward the buyer's own words or try another allowed subreddit, and never invent requests.
- `product_does_not_fit`: If the posts found ask for something the product does not do, drop them and go back to the buyer situation before searching again.
- `api_commercial_permission`: If you would need bulk data or Reddit's API to continue, stop at what you have read page by page and wait for the owner's existing permission.

### 10. Read this goal's numbers from Reddit and sales records (baseline numbers)

Record the numbers this goal is judged on, for the same length of time before and after the round, from the round's Reddit threads and the owner's own sales records, so rounds are compared on real people and real purchases. record_numbers lists exactly which numbers it needs.

- **C-RD-METRICS.01** Confirm the username, the list of this round's post and reply URLs, the date range and the time zone. For the baseline use the same number of days just before the round; for the current reading use the round's own days.  
  _Done when:_ Username, the URLs measured, and the date range with time zone.
- **C-RD-METRICS.02** Open each URL in a signed-out or private window and mark it 'visible', 'removed' or 'locked'. A removed reply can get no answers, so list it separately rather than hiding it.  
  _Done when:_ Each URL with its visibility and the time it was checked.
- **C-RD-METRICS.03** Count real responses only: a qualified reply or inquiry is a different person who asks for the link, a price or a demo, asks how to use the product, or says they will try it. Upvotes, thanks without a question, and the owner's or the agent's own comments never count. Count each person once and keep the URL of each one counted.  
  _Done when:_ The list of counted responses, each with its URL and the person's username.
- **C-RD-METRICS.04** Fill the goal's components by their exact names. 'read_requests' and 'qualified_requests' come from the search step's counts of posts read and kept. 'eligible_requests' is the number of different request threads the round replied to. 'qualified_replies' and 'qualified_inquiries' are the people counted in the step before; inquiries may also include private messages or emails the owner reports, if they mention Reddit.  
  _Done when:_ Each component name with its number and a one-line note on how it was counted.
- **C-RD-METRICS.05** For a purchase goal, count 'external_purchases' only from the round's sale counter in tracking or the owner's payment records, within the date range. Leave out the owner's or team's own test payments and refunded orders, and say plainly when a sale cannot be tied to Reddit.  
  _Done when:_ Each purchase counted with its source and date, and the ones left out with the reason.
- **C-RD-METRICS.06** Add website visits only if the owner already has a source for them, such as the tracked link or site analytics. If the owner already uses a CRM, check it for the same people; never turn a silent reader into a counted lead.  
  _Done when:_ Each extra figure names its source, and unknown links between Reddit and the result are stated.
- **C-RD-METRICS.07** Pass the goal's exact component names to record_numbers with the source of each. If there is no history, record 0 and say in source that there is no history. Never estimate a missing number; leave it out and name it as missing.  
  _Done when:_ The record_numbers entry with every component, its source, and any missing number named.

**If stuck:**
- `removed_by_automod`: If a reply or post was removed, keep its URL and the removal reason, count it as removed, and never post it again; if the subreddit offers a normal way to appeal, draft a short appeal and show it to the owner before anything is sent.
- `no_sales_source`: If there is no sale counter and no payment record to read, record no purchases for this round, say there is no source, and ask the owner to add the tracking sale counter to the page shown after payment.
- `no_history`: If there is no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.
- `cannot_tell_who_responded`: If you cannot tell whether a response comes from a real prospect or from the owner's side, leave it out and say so.
- `too_early_to_read`: If the replies or posts are less than 24 hours old, report the numbers as early and read them again later.

### 11. Reply in Reddit threads with a useful, disclosed answer

Answer each listed request in its own thread with real help and an honest product mention that the subreddit's rules allow and the owner approved, because a useful reply is what makes the poster answer back or try the product.

- **C-RD-REPLY.01** Reopen each kept thread. Confirm it is not locked, archived or removed, is not solved since, the brand has not replied, the poster has not asked people to stop, and the subreddit's rules still allow a product mention; if the owner already uses a CRM, also check it shows no earlier contact or opt-out for that person. Plan no more than three replies in one subreddit per day.  
  _Done when:_ The threads still open for a reply, each with its URL and the rule that allows it, and the ones dropped with a reason.
- **C-RD-REPLY.02** Draft one reply per thread. Answer the poster's actual question first with specific help that works even without the product. Then mention the product as one option, with the approved disclosure line, using only claims the product facts support. Write like a person in that subreddit, not like an ad, usually under 800 characters, and never reuse the same text in two threads.  
  _Done when:_ One draft per thread, each with the facts it relies on and the disclosure line.
- **C-RD-REPLY.03** Add the round's tracked link only if the subreddit allows links and the poster asked for a tool or a link; otherwise name the product without a link. If you test two versions, change one thing and give them ?v=A and ?v=B.  
  _Done when:_ Each draft marked 'with link' or 'no link', and the tracked link with its version tag where used.
- **C-RD-REPLY.04** Show the owner every reply word for word, next to the thread it answers and the rule that allows it. Nothing is posted until the owner says yes to that exact text.  
  _Done when:_ The approved texts and the owner's approval message.
- **C-RD-REPLY.05** Post each approved reply in its thread, under the post or the comment that asked, from the agreed username. The agent posts only if its browser is signed in to that account and the owner said yes; otherwise the owner posts. Leave at least 30 minutes between replies, never send it as a private message unless the poster asked for one, and press reply once.  
  _Done when:_ Who posted each reply and when.
- **C-RD-REPLY.06** Open each reply's link in a signed-out or private window to confirm it shows publicly, because a removed comment can still look normal to its author. If it does not show, record it as removed with any reason given, and never post it again.  
  _Done when:_ The public URL of each reply, or its 'removed' status with the reason.
- **C-RD-REPLY.07** Check each thread again after 24 and 48 hours. Draft answers to follow-up questions and show them to the owner before posting. Send no cold private messages and no follow-up to people who did not answer.  
  _Done when:_ A list of who answered back, what they asked, and the approved follow-up replies.

**Hand back:** `reply_urls`, `replied_text`, `removed_or_hidden`, `follow_ups`

**If stuck:**
- `owner_has_not_approved`: If the owner has not said yes to the exact text, do not post; show them the text and stop until they answer.
- `community_no_promo`: If the rules forbid a product mention, either post a helpful answer with no product mention, if the owner wants that, or skip the thread; never move to private messages to get around it.
- `removed_by_automod`: If a reply is removed, keep its URL and the reason, do not repost or reword it to slip past the filter, and if the subreddit offers a normal way to appeal, draft a short appeal and show it to the owner before anything is sent.
- `old_or_resolved_thread`: If the thread is solved, locked or archived, drop it and never follow up on it to sell.
- `poster_asked_to_stop`: If the poster says no thanks or asks not to be contacted, stop replying to them and remove them from the round.
- `wrong_account_signed_in`: If the signed-in account is not the agreed username, stop and ask the owner to switch or to post themselves.

### 12. Read this goal's numbers from Reddit and sales records (result numbers)

Record the numbers this goal is judged on, for the same length of time before and after the round, from the round's Reddit threads and the owner's own sales records, so rounds are compared on real people and real purchases. record_numbers lists exactly which numbers it needs.

- **C-RD-METRICS.01** Confirm the username, the list of this round's post and reply URLs, the date range and the time zone. For the baseline use the same number of days just before the round; for the current reading use the round's own days.  
  _Done when:_ Username, the URLs measured, and the date range with time zone.
- **C-RD-METRICS.02** Open each URL in a signed-out or private window and mark it 'visible', 'removed' or 'locked'. A removed reply can get no answers, so list it separately rather than hiding it.  
  _Done when:_ Each URL with its visibility and the time it was checked.
- **C-RD-METRICS.03** Count real responses only: a qualified reply or inquiry is a different person who asks for the link, a price or a demo, asks how to use the product, or says they will try it. Upvotes, thanks without a question, and the owner's or the agent's own comments never count. Count each person once and keep the URL of each one counted.  
  _Done when:_ The list of counted responses, each with its URL and the person's username.
- **C-RD-METRICS.04** Fill the goal's components by their exact names. 'read_requests' and 'qualified_requests' come from the search step's counts of posts read and kept. 'eligible_requests' is the number of different request threads the round replied to. 'qualified_replies' and 'qualified_inquiries' are the people counted in the step before; inquiries may also include private messages or emails the owner reports, if they mention Reddit.  
  _Done when:_ Each component name with its number and a one-line note on how it was counted.
- **C-RD-METRICS.05** For a purchase goal, count 'external_purchases' only from the round's sale counter in tracking or the owner's payment records, within the date range. Leave out the owner's or team's own test payments and refunded orders, and say plainly when a sale cannot be tied to Reddit.  
  _Done when:_ Each purchase counted with its source and date, and the ones left out with the reason.
- **C-RD-METRICS.06** Add website visits only if the owner already has a source for them, such as the tracked link or site analytics. If the owner already uses a CRM, check it for the same people; never turn a silent reader into a counted lead.  
  _Done when:_ Each extra figure names its source, and unknown links between Reddit and the result are stated.
- **C-RD-METRICS.07** Pass the goal's exact component names to record_numbers with the source of each. If there is no history, record 0 and say in source that there is no history. Never estimate a missing number; leave it out and name it as missing.  
  _Done when:_ The record_numbers entry with every component, its source, and any missing number named.

**If stuck:**
- `removed_by_automod`: If a reply or post was removed, keep its URL and the removal reason, count it as removed, and never post it again; if the subreddit offers a normal way to appeal, draft a short appeal and show it to the owner before anything is sent.
- `no_sales_source`: If there is no sale counter and no payment record to read, record no purchases for this round, say there is no source, and ask the owner to add the tracking sale counter to the page shown after payment.
- `no_history`: If there is no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.
- `cannot_tell_who_responded`: If you cannot tell whether a response comes from a real prospect or from the owner's side, leave it out and say so.
- `too_early_to_read`: If the replies or posts are less than 24 hours old, report the numbers as early and read them again later.
