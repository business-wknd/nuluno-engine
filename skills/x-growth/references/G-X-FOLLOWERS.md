# X: gain more net followers from threads

- **Goal id:** `G-X-FOLLOWERS`
- **Channel:** x
- **Metric:** `net_followers` = `followers`, should increase
- **Observation window:** 48 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `C-X-INTENT`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), hook (the next round starts with `A-ANGLES`), data (the next round starts with `C-X-METRICS`)

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

Write two or three ways to present the same true benefit, choose the one this round publishes, and write the win rule before posting, so the goal's own number, compared with the baseline, decides whether it works. The other angles are kept for later rounds.

- **A-ANGLES.01** Name one buyer group in one situation, the quote that represents them, the motive, and the benefit the product can deliver.  
  _Done when:_ Group, quote, motive, and benefit written in four short lines.
- **A-ANGLES.02** Write two or three angles: the progress they hope for, getting past the real obstacle, and a believable demonstration. Do not use fear to exaggerate outcomes.  
  _Done when:_ Two or three angles, each in one or two sentences.
- **A-ANGLES.03** For each angle list the facts that support it, the promises that are still unknown, and the wording that must not be used.  
  _Done when:_ Each angle has supporting facts, unknowns, and banned wording next to it.
- **A-ANGLES.04** Choose the one angle this round publishes. The round compares it with the baseline, not with the other angles; keep those unchanged for later rounds. Keep the same channel, audience, and destination link as the baseline. If a channel step later offers a second version (?v=B), it differs in one labeled thing only and is extra information; the verdict still comes from the round's total. Before posting, write the guess being tested, how long the round runs, the number that counts as a win, and the cost in time or money.  
  _Done when:_ A test plan written before posting, showing the chosen angle, the guess, the duration, the win number, the cost, and the angles kept for later rounds.
- **A-ANGLES.05** Choose the main number: the goal's metric, shown with this step (for example link clicks divided by views, followers gained, or purchases). Likes are supporting information only. State when the number is read.  
  _Done when:_ The main number, when it is read, and the chosen angle ready to be written as the post.

**Hand back:** `test_guess`, `angles`, `facts_used`, `win_rule`

**If stuck:**
- `no_main_motive`: If no main motive has been chosen, go back and choose one before writing angles.
- `angle_needs_unproven_claim`: If an angle only works with a claim that has no proof, rewrite it as an invitation to try or drop the angle.
- `too_few_views_expected`: If the post is unlikely to get enough views to compare with the baseline, say so and report the result as an early signal, not as proof.
- `cannot_measure_main_number`: If the goal's main number cannot be read anywhere, ask the owner how it can be checked, and do not declare a winner from likes.

### 8. Confirm the X account and who posts

Settle which X account will post, who presses post, and what limits that account has, so threads and replies go out under the right brand without stopping the owner halfway.

- **C-X-ACCESS.01** Ask the owner for the URL of the X profile that will post. Open it and confirm the handle, display name, bio and website link match the brand.  
  _Done when:_ The profile URL and handle, with the owner's confirmation that it is theirs.
- **C-X-ACCESS.02** Decide who presses post: the owner on their own device, or the agent only through a posting tool the owner connected that uses X's official API. X's automation rules forbid scripting the x.com website and can suspend the account, so the agent never posts by driving x.com in a browser. Write down which tools actually exist.  
  _Done when:_ Who will post, and the tool or device they will use.
- **C-X-ACCESS.03** If the owner needs to sign in, they do it themselves on x.com or in the X app. Never ask for a password, and never sign in for them.  
  _Done when:_ The owner's confirmation that they are signed in, and the handle shown after sign-in.
- **C-X-ACCESS.04** If X asks for an email or phone code, a CAPTCHA, terms or an identity check, stop and tell the owner exactly which screen needs it. Return to the same account once they finish.  
  _Done when:_ A note of what the owner had to do and where work resumed.
- **C-X-ACCESS.05** Note the account's limits that affect this round: whether it can post more than 280 characters, whether it can add images or video, and whether the owner can open post analytics. Do not buy an X plan or API access; if a step needs one, tell the owner the price shown and let them decide.  
  _Done when:_ A short list of what the account can and cannot do this round.
- **C-X-ACCESS.06** Use only this one real account. Never create extra accounts or switch accounts to get around limits; if X shows a limit, write down when it resets.  
  _Done when:_ Confirmation that one account is used, and any limit seen with its reset time.
- **C-X-ACCESS.07** If the account cannot post right now, finish what does not need posting, such as search phrases and drafts, and list the one thing the owner must do to unblock posting.  
  _Done when:_ The work already done and the single owner action still needed, or 'none'.

**Hand back:** `account_handle`, `profile_url`, `who_publishes`, `account_limits`

**If stuck:**
- `handle_not_the_brand`: If the signed-in account is a personal account or a different brand, stop before any posting and ask the owner which account to use.
- `owner_action_needed`: If a verification code, CAPTCHA, terms screen or identity check appears, stop and tell the owner which screen and which button; never enter codes or accept terms for them.
- `no_official_posting_tool`: If the agent has no posting tool that uses X's official API, set who_publishes to 'owner' and plan to hand them the final text to post.
- `account_limited`: If X shows the account is locked or limited, stop posting, tell the owner what X shows, and continue drafting until it is cleared.
- `paid_plan_needed`: If the round needs something only a paid X plan or paid API access offers, tell the owner what it is and the price shown, and let them decide; never buy it.

### 9. Find recent public posts on X where buyers ask for help

Collect recent public X posts where real people describe the problem the product solves, in their own words, because these show who to speak to and what to say, which is what moves the goal's main number.

- **C-X-INTENT.01** Write 3 to 5 search phrases from the buyer quotes and segments, such as "looking for" plus the task, "any recommendations" plus the category, or "alternative to" plus a tool buyers name. Add -filter:retweets and since: with a date 14 days back.  
  _Done when:_ The exact search phrases.
- **C-X-INTENT.02** Run each phrase on X search's Latest tab. If the owner connected a search tool that uses X's official API, the agent may use it; otherwise give the owner the phrases to run and ask them to paste back the post links, or use the agent's own web search for public x.com posts. Never script x.com or collect results in bulk, and stop if X shows a limit message.  
  _Done when:_ For each phrase, who ran it, the date run, and the number of posts looked at.
- **C-X-INTENT.03** Open each promising post itself, not a repost or quote, with read_page or through the owner if it does not load, and read the whole thread. Write down the post URL, author handle, date, and the person's exact words about their need.  
  _Done when:_ A list of posts with URL, handle, date and exact quote.
- **C-X-INTENT.04** Sort each post: keep it only if the person wants to switch tools, is looking for a product or service, or is stuck with their current way. Exclude promotions, job posts, vendors, bots, and needs already solved, with a reason.  
  _Done when:_ Kept and excluded posts, each with a one-line reason.
- **C-X-INTENT.05** For each kept post, check the product can actually solve this need using the fact sheet. Write what the person said and what you infer as two separate lines.  
  _Done when:_ For each kept post, the stated need and the inferred fit written separately.
- **C-X-INTENT.06** Check each kept post can be answered: replies are open to the owner's account, it is less than 7 days old, and the owner has not already replied to that person about it. Keep one entry per person.  
  _Done when:_ Each kept post marked 'can reply' or 'cannot reply', with one entry per person.
- **C-X-INTENT.07** Stop at 10 qualified posts or after 50 posts reviewed, whichever comes first. Hand back the list. Do not look up emails, phone numbers or other personal details beyond the public post.  
  _Done when:_ The final list with counts of posts reviewed, kept and excluded.

**Hand back:** `demand_posts`, `excluded_posts`, `search_phrases`

**If stuck:**
- `cannot_search_x`: If no official X search tool is connected and web search finds nothing usable, give the owner the exact phrases to run and ask them to paste back the post links.
- `rate_limited`: If X shows a limit message, stop, note the time, and continue from the same phrase after the limit resets.
- `no_matching_posts`: If no phrase finds a real need in the last 14 days, try two new phrases from different buyer quotes, then report zero with the phrases tried.
- `reply_restricted`: If the author limits replies, mark the post 'cannot reply'; never plan a mention or DM instead.
- `personal_data_requested`: If a later step asks for emails or phone numbers of these people, refuse and keep only the public post details.

### 10. Write the post from proven facts

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

### 11. Read this goal's numbers on X (baseline numbers)

Record the numbers this goal is judged on for the account and its threads, for a fixed range before and after the new post, so rounds are compared on real numbers. record_numbers lists exactly which numbers it needs.

- **C-X-METRICS.01** Confirm the X handle, the post or thread URLs being measured, whether this is the baseline or the current reading, the date range, and the time zone. Check whether you can open the post's analytics; if not, ask the owner for a screenshot or the numbers.  
  _Done when:_ Handle, post URLs, baseline or current, date range with time zone, and how the numbers will be obtained.
- **C-X-METRICS.02** If the goal needs followers, read the follower count on the profile at the start and the end of the range, at about the same time of day. Record the end count as followers and put the start count in source.  
  _Done when:_ Both follower counts with the time each was read.
- **C-X-METRICS.03** If the goal needs impressions, profile_visits or url_clicks, read them from each post's analytics. For a thread, decide once whether you use the first post only or the sum of all posts, and use the same choice for baseline and current. Impressions are views, not unique people.  
  _Done when:_ Each number as shown, the post it came from, and whether it is the first post or the thread total.
- **C-X-METRICS.04** For url_clicks, prefer the click count of the round's tracked link from tracking when the post used it, and note X's link click number next to it. Say which one you recorded, and use the same one for baseline and current.  
  _Done when:_ The click number recorded, its source, and the other number for comparison.
- **C-X-METRICS.05** If the goal needs qualified_conversations or qualified_replies, count each different person once who showed a real need for the product, with the URL of their reply or the date of their message. Do not count the owner's or the agent's own replies, bots or vendors. If it needs eligible_requests, count the public requests on the round's list that were still open to a reply in the range.  
  _Done when:_ Each count, with one URL or date per person or request and a one-line reason each qualifies.
- **C-X-METRICS.06** Add website visits or purchases only if the owner already has a source for them, such as the tracked link, site analytics or payment records. Where you cannot tell which post led to a sale, say so plainly; never infer a purchase.  
  _Done when:_ Each visit or sales figure names its source, and unknown links are stated.
- **C-X-METRICS.07** Call record_numbers with the goal's exact metric component names as listed for this goal, each with its source. If there is no history, record 0 and say so in source. Never estimate; if a number is not shown, say which one and why.  
  _Done when:_ The record_numbers call with each component, its value and its source.

**If stuck:**
- `cannot_open_analytics`: If you cannot open the post's analytics, ask the owner for a screenshot of it or for the numbers this goal needs.
- `no_history`: If the account has no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.
- `numbers_from_wrong_account`: If the screenshot or screen shows a different handle from the agreed one, do not use those numbers and ask again.
- `thread_counted_differently`: If the baseline used a different thread counting choice, read the baseline again the same way before comparing.
- `too_early_to_read`: If the post is less than 24 hours old, report the numbers as early and read them again when the 48-hour range ends.

### 12. Publish an approved X thread in order and confirm it

Publish the approved thread once, post by post in the right order under the right account, and hand back its public URL, because the thread must be live and complete before anything it does to the goal's main number can be measured.

- **C-X-POST.01** Confirm with the owner which X handle will post and who presses Post: the owner, or the agent's own browser if it is signed in to that account. Look at the profile's recent posts to make sure this round's first post is not already live.  
  _Done when:_ The handle, who will publish, and a note on the recent posts checked.
- **C-X-POST.02** Lay out the thread as a numbered list. Keep each post under 280 characters unless the account clearly allows longer posts, and keep the thread to 2 to 8 posts. The first post must make sense on its own. Attach images in the planned order with short alt text.  
  _Done when:_ The numbered thread with each post's character count and its images in order.
- **C-X-POST.03** If the thread links to the product, put the link only in the last post, using the round's tracked link. If there are two versions of the thread, add ?v=A to one and ?v=B to the other, and open the link once to confirm it loads.  
  _Done when:_ The exact link with its version label and confirmation it opens the product, or a note that the thread has no link.
- **C-X-POST.04** Check every post against the product fact sheet; remove any number, result, quote or promise you cannot support.  
  _Done when:_ The list of claims in the thread, each with its fact source.
- **C-X-POST.05** Show the owner the full thread word for word, with images, and get a clear yes before anything is posted.  
  _Done when:_ The approved thread and the owner's approval message.
- **C-X-POST.06** Publish the first post once. Then publish each next post as a reply to the one before it, in order, using X's own thread composer or reply button. Use only normal X features; never use scripts to get around X's rules.  
  _Done when:_ The URL of each post as it went live, in order.
- **C-X-POST.07** If publishing stops halfway, open the profile and find which posts are live. Continue from the first missing post as a reply to the last live one. Never post the first post again.  
  _Done when:_ A note of where it stopped and where it resumed, or a note that it ran without a break.
- **C-X-POST.08** Open the first post's public URL and read the whole thread: author handle, order, full text of each post, and that the link opens the product page.  
  _Done when:_ The thread's public URL, its text as it appears, and confirmation the link works.

**Hand back:** `thread_url`, `post_urls`, `published_text`

**If stuck:**
- `owner_has_not_approved`: If the owner has not said yes to this exact thread, do not post; show it to them and wait.
- `wrong_account_signed_in`: If the signed-in account is not the agreed handle, stop and ask the owner to switch accounts or post it themselves.
- `thread_partial`: If only part of the thread went live, continue from the first missing post as a reply to the last live one; never repost the first post.
- `rate_limited`: If X says you have hit a limit, wait until it lifts and then continue the same thread; never switch to another account.
- `agent_cannot_publish`: If the agent's browser cannot post, give the owner the numbered thread to post and ask them to send back the first post's URL.
- `link_does_not_open`: If the tracked link does not open the product page, stop before posting and fix the link with the owner.

### 13. Read this goal's numbers on X (result numbers)

Record the numbers this goal is judged on for the account and its threads, for a fixed range before and after the new post, so rounds are compared on real numbers. record_numbers lists exactly which numbers it needs.

- **C-X-METRICS.01** Confirm the X handle, the post or thread URLs being measured, whether this is the baseline or the current reading, the date range, and the time zone. Check whether you can open the post's analytics; if not, ask the owner for a screenshot or the numbers.  
  _Done when:_ Handle, post URLs, baseline or current, date range with time zone, and how the numbers will be obtained.
- **C-X-METRICS.02** If the goal needs followers, read the follower count on the profile at the start and the end of the range, at about the same time of day. Record the end count as followers and put the start count in source.  
  _Done when:_ Both follower counts with the time each was read.
- **C-X-METRICS.03** If the goal needs impressions, profile_visits or url_clicks, read them from each post's analytics. For a thread, decide once whether you use the first post only or the sum of all posts, and use the same choice for baseline and current. Impressions are views, not unique people.  
  _Done when:_ Each number as shown, the post it came from, and whether it is the first post or the thread total.
- **C-X-METRICS.04** For url_clicks, prefer the click count of the round's tracked link from tracking when the post used it, and note X's link click number next to it. Say which one you recorded, and use the same one for baseline and current.  
  _Done when:_ The click number recorded, its source, and the other number for comparison.
- **C-X-METRICS.05** If the goal needs qualified_conversations or qualified_replies, count each different person once who showed a real need for the product, with the URL of their reply or the date of their message. Do not count the owner's or the agent's own replies, bots or vendors. If it needs eligible_requests, count the public requests on the round's list that were still open to a reply in the range.  
  _Done when:_ Each count, with one URL or date per person or request and a one-line reason each qualifies.
- **C-X-METRICS.06** Add website visits or purchases only if the owner already has a source for them, such as the tracked link, site analytics or payment records. Where you cannot tell which post led to a sale, say so plainly; never infer a purchase.  
  _Done when:_ Each visit or sales figure names its source, and unknown links are stated.
- **C-X-METRICS.07** Call record_numbers with the goal's exact metric component names as listed for this goal, each with its source. If there is no history, record 0 and say so in source. Never estimate; if a number is not shown, say which one and why.  
  _Done when:_ The record_numbers call with each component, its value and its source.

**If stuck:**
- `cannot_open_analytics`: If you cannot open the post's analytics, ask the owner for a screenshot of it or for the numbers this goal needs.
- `no_history`: If the account has no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.
- `numbers_from_wrong_account`: If the screenshot or screen shows a different handle from the agreed one, do not use those numbers and ask again.
- `thread_counted_differently`: If the baseline used a different thread counting choice, read the baseline again the same way before comparing.
- `too_early_to_read`: If the post is less than 24 hours old, report the numbers as early and read them again when the 48-hour range ends.
