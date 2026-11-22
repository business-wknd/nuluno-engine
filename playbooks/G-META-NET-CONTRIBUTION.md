# Meta Ads: raise net profit per customer after all costs

- **Goal id:** `G-META-NET-CONTRIBUTION`
- **Language:** English
- **Channel:** meta_ads
- **Metric:** `net_per_customer` = `net_after_all_costs_minor` / `external_purchases`, should increase
- **Observation window:** 72 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), creative (the next round starts with `C-META-CREATIVE`), delivery (the next round starts with `C-META_ADS-ACCESS`), data (the next round starts with `C-META-METRICS`)

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

### 8. Confirm the Meta ad account, brand Page and spending limits

Settle which ad account, which brand Page and Instagram account, who operates Ads Manager, and how much the owner allows to be spent, so ads can run under the right brand without the round stopping halfway.

- **C-META_ADS-ACCESS.01** Ask the owner for the brand website, the Facebook Page and the Instagram account the ads should run under. Note how you will work: in your own browser already signed in to Meta Ads Manager, or through the owner's screen and screenshots.  
  _Done when:_ The website, Page URL, Instagram handle, and who will operate Ads Manager.
- **C-META_ADS-ACCESS.02** The owner signs in to Ads Manager themselves; never ask for a password. List the business portfolios and ad accounts the owner can see, let the owner pick one, and write down its ad account ID, currency and time zone. If there are several, do not choose for them.  
  _Done when:_ The chosen ad account ID, its currency and time zone, and the owner's choice in their own words.
- **C-META_ADS-ACCESS.03** Check that the brand's own Page and Instagram account are connected to this ad account and can be chosen as the ad's identity. If you open a new ad to see the identity choice, discard that draft afterwards so nothing is left in the account. If they cannot be chosen, stop the ads part of the round; never run the ads under another brand's Page.  
  _Done when:_ The Page and Instagram account shown as choosable for this ad account, a note that any test draft was discarded, or a note that they are missing.
- **C-META_ADS-ACCESS.04** Check the account's health in Account Quality and in the ad account's payment settings. Sort any problem into one type: one rejected ad, a restricted account, a payment problem, or missing permission. Copy the exact wording of each notice.  
  _Done when:_ Account status, the problem type if any, and the exact notice text with the date it was read.
- **C-META_ADS-ACCESS.05** Confirm the signed-in person can create and edit ads and can open the ad account's reporting. Open the reporting for the last 7 days and check that real numbers appear, not a message about a plan limit or missing permission. If only reading works, plan for the owner to make every change by hand from the drafts you prepare.  
  _Done when:_ What the signed-in person can do (read reports, create drafts, switch ads on and off), and whether real numbers appeared in reporting.
- **C-META_ADS-ACCESS.06** If Meta asks for a two-factor code, an identity check, a new payment method or acceptance of terms, stop. Tell the owner which screen and which button, and wait. Resume on the same screen once they are done.  
  _Done when:_ What the owner had to do, on which screen, and where you resumed.
- **C-META_ADS-ACCESS.07** Create a new ad account or business portfolio only if the owner asked for one in this conversation, and only through Meta's own screens. Keep to one real account. If creation seems to fail, check whether it was created before trying again; never make a second one.  
  _Done when:_ The new account ID with the owner's request, or a note that the existing account is used.
- **C-META_ADS-ACCESS.08** Ask the owner to write down the limits for this round: the daily budget, the total for the round, the end date, and the currency. Without a written amount above zero, this round may only prepare ads that stay off.  
  _Done when:_ The owner's written message with daily budget, round total, end date and currency, or a note that no spend is approved.

**Hand back:** `ad_account`, `brand_identity`, `account_health`, `who_operates`, `approved_limits`

**If stuck:**
- `brand_page_not_available`: If the brand's Page or Instagram account cannot be selected in this ad account, stop the ads part and ask the owner to give the ad account access to the Page; never use another Page instead.
- `account_restricted_or_unpaid`: If the account is restricted or has a payment problem, tell the owner the exact notice and Meta's next step shown on screen; never add or pay with a card for them.
- `owner_action_needed`: If a code, identity check, payment method or terms screen appears, stop and tell the owner which screen and which button; never enter codes or accept terms for them.
- `signed_out_again`: If the session expires, ask the owner to sign in once more; if it expires again, switch to the owner operating Ads Manager from your drafts.
- `no_budget_approved`: If the owner has not written a daily budget and round total, continue preparing drafts that stay off and ask for the two numbers before any ad is switched on.
- `several_ad_accounts`: If the owner can see more than one ad account, list them by ID and name and let the owner choose; never pick one yourself.

### 9. Map past Meta ad results and how each number will be counted

Lay out what past ads spent and returned, and fix the counting rules for this goal once, so the before and after numbers of this round are compared the same way and the weak point is visible.

- **C-META-BASELINE.01** In the ad account's reporting, list the campaigns, ad sets and ads that ran in the last 30 days, with their status, budget, amount spent and the dates they ran. If you cannot open reporting, ask the owner for a screenshot or an export of the same view.  
  _Done when:_ A table of past campaigns, ad sets and ads with IDs, status, budget, spend and dates, and where it was read.
- **C-META-BASELINE.02** For the same 30 days, read impressions, frequency, link clicks, landing page views and the result each campaign was set to get (purchases, leads or another conversion). Write each number exactly as shown and 'not shown' where it is missing.  
  _Done when:_ The numbers per campaign as displayed, with the name of the result each campaign counts.
- **C-META-BASELINE.03** Write down the attribution setting (for example 7-day click, 1-day view), the account time zone, and how long after a click sales usually arrive. These must stay the same for the baseline and the current read.  
  _Done when:_ The attribution setting, time zone and typical delay, stated as the rule for this goal.
- **C-META-BASELINE.04** Find where real sales, leads and refunds are recorded: the payment provider, the order list, the lead form inbox, or a CRM if the owner already uses a CRM. Ask the owner whether the Meta pixel is installed on the product page, because Meta only counts landing page views and website conversions where it is. A purchase reported by Meta is not money received; note how you will match the two and count each order only once.  
  _Done when:_ The name of each source for sales, leads and refunds, whether the pixel is on the product page, and how a Meta result will be matched to one real order or lead.
- **C-META-BASELINE.05** Propose what counts for this goal and ask the owner to confirm or correct it: what makes a lead qualified, which orders count as outside customers (not the owner, team, tests or bots), and which costs are included in full costs. Write each rule in one sentence.  
  _Done when:_ The counting rules in plain sentences, confirmed by the owner.
- **C-META-BASELINE.06** List every part of the goal's main number you cannot yet get, such as unknown fees or no sales source, and leave it empty; never estimate. If there is no past ad history, say so; the first round sets the baseline.  
  _Done when:_ A list of missing pieces and why each is missing, or a note that every piece has a source.
- **C-META-BASELINE.07** From the table, name where results drop most: few impressions, low link click rate, clicks that do not load the page, or page visits that do not buy. Do not change any ad during this step.  
  _Done when:_ One sentence naming the weakest stage, with the two numbers that show it.

**Hand back:** `past_results`, `counting_rules`, `money_sources`, `missing_pieces`, `weakest_stage`

**If stuck:**
- `cannot_open_reporting`: If you cannot open the ad account's reporting, ask the owner for a screenshot or export of the last 30 days by campaign, with the columns you need.
- `no_sales_source`: If there is no record of real sales or leads outside Meta, tell the owner the goal cannot be judged on money yet and ask where orders arrive; do not use Meta's numbers as money received.
- `plan_limit_text_not_numbers`: If a tool returns a message about a plan limit instead of numbers, do not treat it as a number; read the same figures from the ad account's reporting or ask the owner for a screenshot.
- `attribution_changed`: If past campaigns used different attribution settings, pick one with the owner and note that older numbers are not directly comparable.
- `no_history`: If the account has never run ads, write that there is no history and move on; the first round's read becomes the baseline.

### 10. Diagnose current Meta ads and design a one-change test

Find out why current ads are falling short and design two ad versions that differ in one thing only, so the round shows clearly which change moves the goal's main number.

- **C-META-CREATIVE.01** Read the ads that ran most recently: their IDs, impressions, frequency, link click rate, cost per result, and how long they have run. Do not judge any ad with under 1,000 impressions or under 72 hours of delivery.  
  _Done when:_ A short table of recent ads with these numbers and which ones have enough data to judge.
- **C-META-CREATIVE.02** Sort the problem into one type: not delivering, stuck in review or rejected, wrong audience, or tired creative. Call it tired only when frequency is above 3 and the link click rate fell by at least 20% over 7 days or more; one bad day is not enough.  
  _Done when:_ The problem type and the numbers that support it.
- **C-META-CREATIVE.03** If the problem is delivery, review or account health, stop here and send the round back to the account step; if it is the wrong audience, send it back to the buyer group step. A new creative fixes neither. Otherwise continue.  
  _Done when:_ A note that the problem is in the ad itself, or which step the round was sent back to.
- **C-META-CREATIVE.04** From the chosen angle, buyer quotes and buying motive, pick one thing to change: the hook, the image, the format (image, carousel, video) or the offer wording. Write a one-sentence guess of why it will do better.  
  _Done when:_ The single thing that changes and the one-sentence guess, with the quote or motive it comes from.
- **C-META-CREATIVE.05** Write a brief for version A (the current best ad, unchanged) and version B (the one change). For each, list the opening line, the headline, the image or video needed, the button, and the tracked link with ?v=A or ?v=B. Keep the first line of the ad text under 125 characters.  
  _Done when:_ Two briefs side by side, showing they differ only in the chosen element.
- **C-META-CREATIVE.06** Next to each claim in the briefs, name the product fact that supports it. Remove any number, testimonial, deadline or guarantee the facts do not support.  
  _Done when:_ Each claim paired with its product fact, and a list of claims removed.
- **C-META-CREATIVE.07** Set the rule for picking a winner before anything runs: the goal's main number, the goal's observation window (at least 72 hours), at least 1,000 impressions per version, and, when the goal counts purchases or leads, at least 5 of them per version. Call B the winner only if it beats A by 20% or more on the goal's main number; otherwise report 'no clear winner' and keep A. Keep the ad account, Page, audience and total budget the same as already approved; anything beyond that waits for the owner.  
  _Done when:_ The written winner rule and a note that budget, audience and Page stay within what the owner approved.

**Hand back:** `diagnosis`, `hypothesis`, `variants`, `acceptance_rule`

**If stuck:**
- `not_enough_data`: If no ad has 1,000 impressions and 72 hours of delivery, or no ad has run at all, write version A from the chosen angle as it stands and design version B with one change, without claiming any old ad is tired.
- `problem_is_not_creative`: If ads are not delivering, are rejected or the account is restricted, send the round back to the account step instead of writing new ads.
- `no_chosen_angle`: If no angle or buyer quotes exist yet, go back to the angle test step before writing briefs.
- `fact_missing_for_claim`: If a claim needs a fact you do not have, remove it or ask the owner; never fill the gap with a guess.
- `change_needs_more_budget`: If the test only works with a bigger budget or a new audience, write the request for the owner and keep the round within the current limits until they answer in writing.

### 11. Write the post from proven facts

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

### 12. Make the marketing images from real product visuals

Produce finished image files in the exact size the channel needs, built from real product visuals and approved copy, because a clear image that matches the product is what stops the scroll and moves the goal's main number.

- **S12.01** Write down what images this round needs: the channel and placement, the image type (single image, carousel, cover or ad), the pixel size, and how many. If the size is unknown, check the channel's current help page; for example 1080x1350 for a portrait feed image and 1080x1920 for a full-screen vertical one.  
  _Done when:_ A list of images with channel, placement, size and purpose for each.
- **S12.02** Collect the real visuals: product screenshots, product photos, logo and brand colours. Use only material the owner made or has the right to use; never copy other brands' images or stock photos without a licence.  
  _Done when:_ Each visual with where it came from and who owns it.
- **S12.03** Take the words only from the approved copy. For feed and ad images keep the text to at most two short lines, around 10 words, placed where it stays readable and clear of the channel's own buttons and captions; follow the channel's own text rules for covers and store screenshots. Do not let an image tool add numbers, prices, ratings or badges.  
  _Done when:_ The exact text for each image, matching the approved copy.
- **S12.04** Lay out each image with one headline, the product shown working, and one call to action. If there is more to say, split it into carousel slides instead of crowding one image.  
  _Done when:_ A short layout note or sketch for each image.
- **S12.05** Make the actual image files with the image or design tool available. Place the text as a real text layer, not generated lettering. A prompt or description is not a finished image. If the only available tool charges money, ask the owner before using it.  
  _Done when:_ Image files that open.
- **S12.06** Open each file at full size and check spelling, cropping, faces, and that any product screen shown is the real product. Fix any garbled or wrong text by rebuilding it, never by handing over a flawed image.  
  _Done when:_ A checked list of each image with any fixes made.
- **S12.07** Check each file's type (JPG or PNG), pixel size and file size against the channel's limits, and view it at phone width to confirm the text is readable.  
  _Done when:_ Type, pixel size and file size for each image, all within the channel's limits.
- **S12.08** If the round tests versions, make only the versions the test needs and change one thing between them, labelled A, B and so on. Do not make extra variations for channels not in this round.  
  _Done when:_ Each version labelled with the single thing that differs.
- **S12.09** Save the final files with clear names and a note of version, purpose and sources, in a place the publishing step can open and upload from.  
  _Done when:_ File paths or links that open, with the note for each file.

**Hand back:** `image_files`, `image_text`, `versions`, `sources`

**If stuck:**
- `no_real_product_visuals`: If there are no screenshots or photos of the real product, ask the owner for two or three, and meanwhile make a text-and-brand-colour design without fake product screens.
- `size_unknown`: If the channel's required size is unclear, check its current help page; if still unclear, ask the owner where the image will run.
- `text_garbled`: If the image tool produces wrong or garbled text, rebuild the text as a real text layer before handing over the file.
- `rights_unclear`: If you cannot tell who owns a visual, leave it out and use one the owner confirms they own.
- `image_tool_failed`: If the image tool fails, try another available tool with the same brief; do not start the whole brief over or create duplicate charges.

### 13. Read this goal's Meta Ads numbers and check them against real sales (baseline numbers)

Record the numbers this goal is judged on, read from the ad account and matched against real sales, leads and costs, so the before and after of the round are compared on real money and not on what the platform reports.

- **C-META-METRICS.01** Confirm the ad account ID, the ads being measured, the date range, the time zone and the attribution setting. For the baseline read, use the account's ads over the most recent past period as long as the goal's observation window; for the current read, use this round's campaign, ad set and ad IDs from the time they started delivering. Use the same attribution setting for both.  
  _Done when:_ Ad account ID, ad IDs, date range with time zone, and attribution setting.
- **C-META-METRICS.02** For the current read, wait until the goal's observation window (72 hours of delivery) has passed since the ads started delivering. If you must read earlier, mark the numbers as early and read again after the window.  
  _Done when:_ The time delivery started and the time of this read, with 'final' or 'early'.
- **C-META-METRICS.03** In the ad account's reporting, or from the owner's screenshot or export, read amount spent, impressions, link clicks, landing page views and the result the ads were set to get, for each version (A and B) and in total. Write each exactly as shown; write 'not shown' and do not estimate when a number is missing.  
  _Done when:_ The numbers per version and in total as displayed, with the screen or file they came from and the time they were read.
- **C-META-METRICS.04** Check leads, purchases and refunds against the owner's own records: the payment provider, the order list, the lead form inbox, the round's sale counter from tracking, or a CRM if the owner already uses a CRM. Apply the counting rules agreed in the baseline step and count only real outside customers; leave out the owner, team, tests, bots, duplicates and refunded orders.  
  _Done when:_ The count from the owner's records, the source name, and how many were left out and why.
- **C-META-METRICS.05** If the goal needs money, add up the money from matched outside sales after refunds, and every cost for the round: ad spend, payment fees, platform fees, commissions, software and tools, product or delivery cost, paid help, and any other cost, plus money held back for work still to deliver. Meta's return on ad spend is not the owner's income.  
  _Done when:_ Money from matched sales after refunds, and each cost with its amount and source, or 'unknown' where there is no source.
- **C-META-METRICS.06** Turn money into the currency's smallest unit for any component ending in _minor, using the currency's standard decimal places: multiply by 100 for currencies with two decimals, such as USD, EUR and TWD; use the amount as shown for currencies without decimals, such as JPY and KRW. Say which rule you used.  
  _Done when:_ Each money amount as shown and in the smallest unit, with the rule used.
- **C-META-METRICS.07** Call record_numbers with the goal's exact component names, as record_numbers lists them for this goal (for example spend_minor, impressions, link_clicks, landing_page_views, attributed_conversions, qualified_leads, external_purchases, net_after_all_costs_minor), and a source for each. If there is no history, record 0 and say so in source. If a source is incomplete, say what is missing in source. Never estimate, and never change any ad during this step.  
  _Done when:_ The record_numbers call with every component, its value and its source.

**If stuck:**
- `cannot_open_reporting`: If you cannot open the ad account's reporting, ask the owner for a screenshot or export with the columns this goal needs, for the exact date range.
- `no_sales_records`: If there is no record of real sales or leads outside Meta, say so in source and leave those components unrecorded; never copy Meta's reported purchases as real ones.
- `cost_unknown`: If a cost needed for money after costs has no source, list it as unknown and ask the owner for the figure; do not estimate it.
- `too_early_to_read`: If the observation window has not passed, record the numbers as early and read them again after the window ends; do not fill conversions that have not arrived yet with 0.
- `settings_differ_from_baseline`: If the attribution setting, time zone or range length differs from the baseline, read again with the baseline's settings before recording.
- `no_history`: If the account has no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.

### 14. Build this round's Meta ads switched off

Build the approved ad versions in the ad account, switched off and within the owner's budget, so nothing spends until the owner says yes and each version can be measured on its own.

- **C-META-DRAFT.01** Re-check the ad account ID, the brand Page and Instagram account, the campaign objective that fits the goal (sales, leads, or traffic for a goal about clicks or page loads), and the owner's written daily budget, round total and end date. Plan one campaign, one ad set per version with the same audience and placements, and one ad in each, all named with the round name.  
  _Done when:_ The list of objects to create with their names, and the limits quoted from the owner's message.
- **C-META-DRAFT.02** Show the owner each ad word for word: the ad text, headline, image or video, button, the Page and Instagram account it shows as, and the link. Get a clear yes for each version before building.  
  _Done when:_ The exact text and image of each version and the owner's approval message.
- **C-META-DRAFT.03** Use the round's tracked link as each ad's website link, with ?v=A or ?v=B to match the version. Open each link on a phone and check the product page loads in about 3 seconds and matches what the ad promises. If the goal counts landing page views or website conversions and the owner has not confirmed the Meta pixel is on that page, tell the owner before building.  
  _Done when:_ Each tracked link, which version it belongs to, a note that it loaded the right page, and whether the pixel is confirmed on that page.
- **C-META-DRAFT.04** In Ads Manager (your own browser if it is signed in and the owner agreed, otherwise the owner), create the campaign and one ad set per version. Split the approved daily budget equally and set it on each ad set, not on the campaign, so Meta cannot move money from one version to the other; the ad sets together must not exceed the approved daily budget. Set the end date the owner gave and, if the owner agrees, a campaign spending limit equal to the round total.  
  _Done when:_ The campaign and ad set names with each ad set's budget, the end date and any spending limit as shown on screen.
- **C-META-DRAFT.05** Upload the approved images or videos and create one ad per version in its own ad set. Check the ad preview for each placement shows the right image, text, Page name and link, with nothing cut off that changes the meaning.  
  _Done when:_ A preview check for each ad, with any placement turned off and why.
- **C-META-DRAFT.06** Turn the campaign, every ad set and every ad off before publishing them, so they are created but spend nothing. Do not use any option that would also publish or switch on other drafts or ads in the account.  
  _Done when:_ Each new object shown as off, and a note that no other draft or ad was touched.
- **C-META-DRAFT.07** Read back from the ad account each new object's ID, status, budget, end date, Page and link, and confirm spend is 0. If saving seemed to fail, search the account for the round name before trying again; never create a second copy.  
  _Done when:_ The IDs, status off, budget, end date and link of every new object, and spend of 0.

**Hand back:** `ad_ids`, `approved_ads`, `budget_settings`, `status_check`

**If stuck:**
- `owner_has_not_approved`: If the owner has not said yes to the exact text and image of a version, do not build it; show it to them and wait.
- `no_budget_approved`: If there is no written daily budget and round total, build nothing that can spend; prepare the ads off and ask the owner for the two numbers.
- `wrong_page`: If the brand's Page or Instagram account cannot be selected for the ad, stop building and go back to the account step; never use another Page.
- `link_does_not_open`: If a tracked link does not open the product page, stop before building that ad and fix the link with the owner.
- `not_sure_it_was_created`: If you are not sure an object was saved, search the account for the round name and use what exists; never create a duplicate.
- `account_restricted_or_unpaid`: If Ads Manager shows a restriction or payment problem, copy the exact notice, tell the owner, and stop; never pay or add a card for them.

### 15. Switch on only this round's Meta ads within the approved budget

Switch on exactly this round's ads after the owner's written yes, within the approved daily budget and total, so the test starts spending only what was agreed and its numbers can be read.

- **C-META-ACTIVATE.01** Open this round's campaign, ad set and ad IDs and check they are still off and unchanged since the owner approved them. List any other drafts or unpublished changes in the account and leave them alone.  
  _Done when:_ This round's IDs shown as off and unchanged, and a list of other drafts left untouched.
- **C-META-ACTIVATE.02** Find the owner's written approval to spend: daily budget, round total, end date and currency. Check each ad set budget is a whole amount above zero and that together they are not higher than the approved daily budget. If any of these is missing or zero, stop.  
  _Done when:_ The owner's approval quoted, and the budget and end date as set in the ad account.
- **C-META-ACTIVATE.03** Write a short change plan and show it to the owner: which objects go from off to on, the daily budget, the end date, the most it can spend in total, and how to undo it (switch them off). Wait for the owner's yes to this plan.  
  _Done when:_ The change plan and the owner's yes.
- **C-META-ACTIVATE.04** Switch on only this round's campaign, ad sets and ads, using your own browser if the owner said yes to that, otherwise the owner does it. Do not use any option that publishes all pending changes, and do not raise any budget.  
  _Done when:_ Who switched them on, at what time, which objects, and the link to each live ad if the ad preview offers one.
- **C-META-ACTIVATE.05** After about 15 minutes, read each object's delivery status in the ad account. 'In review' means not delivering yet. If an ad is rejected, copy the reason and tell the owner; do not edit and resubmit without their yes.  
  _Done when:_ Each object's delivery status with the time it was read, and any rejection reason.
- **C-META-ACTIVATE.06** Once the ads show as delivering, note the start time; the observation window counts from there. At 24 and 48 hours, check that spend so far is within the daily budget and that both versions are getting impressions.  
  _Done when:_ The delivery start time, and spend so far and impressions per version at the 24-hour and 48-hour checks.
- **C-META-ACTIVATE.07** Note the date and time when the observation window ends, so the numbers are read and the ads paused on time and never left running past the approved end date.  
  _Done when:_ The planned time for the current read and for pausing.

**Hand back:** `ad_ids`, `delivery_status`, `live_budget`, `delivery_start_time`

**If stuck:**
- `no_written_approval`: If the owner has not approved a daily budget, total and the change plan in writing, keep everything off and ask them.
- `ads_changed_since_approval`: If the text, image, link or budget changed after the owner approved, show the new version and get a new yes before switching on.
- `ad_rejected`: If an ad is rejected, copy the reason, tell the owner, and wait for their yes before editing or asking for a new review.
- `stuck_in_review`: If an ad is still in review after 24 hours, tell the owner and do not count review time in the observation window.
- `spend_above_limit`: If spend runs above the approved daily budget or heads past the round total, switch this round's ads off at once and tell the owner.
- `account_restricted_or_unpaid`: If a restriction or payment problem appears, copy the exact notice and tell the owner; never pay or add a card for them.

### 16. Read this goal's Meta Ads numbers and check them against real sales (result numbers)

Record the numbers this goal is judged on, read from the ad account and matched against real sales, leads and costs, so the before and after of the round are compared on real money and not on what the platform reports.

- **C-META-METRICS.01** Confirm the ad account ID, the ads being measured, the date range, the time zone and the attribution setting. For the baseline read, use the account's ads over the most recent past period as long as the goal's observation window; for the current read, use this round's campaign, ad set and ad IDs from the time they started delivering. Use the same attribution setting for both.  
  _Done when:_ Ad account ID, ad IDs, date range with time zone, and attribution setting.
- **C-META-METRICS.02** For the current read, wait until the goal's observation window (72 hours of delivery) has passed since the ads started delivering. If you must read earlier, mark the numbers as early and read again after the window.  
  _Done when:_ The time delivery started and the time of this read, with 'final' or 'early'.
- **C-META-METRICS.03** In the ad account's reporting, or from the owner's screenshot or export, read amount spent, impressions, link clicks, landing page views and the result the ads were set to get, for each version (A and B) and in total. Write each exactly as shown; write 'not shown' and do not estimate when a number is missing.  
  _Done when:_ The numbers per version and in total as displayed, with the screen or file they came from and the time they were read.
- **C-META-METRICS.04** Check leads, purchases and refunds against the owner's own records: the payment provider, the order list, the lead form inbox, the round's sale counter from tracking, or a CRM if the owner already uses a CRM. Apply the counting rules agreed in the baseline step and count only real outside customers; leave out the owner, team, tests, bots, duplicates and refunded orders.  
  _Done when:_ The count from the owner's records, the source name, and how many were left out and why.
- **C-META-METRICS.05** If the goal needs money, add up the money from matched outside sales after refunds, and every cost for the round: ad spend, payment fees, platform fees, commissions, software and tools, product or delivery cost, paid help, and any other cost, plus money held back for work still to deliver. Meta's return on ad spend is not the owner's income.  
  _Done when:_ Money from matched sales after refunds, and each cost with its amount and source, or 'unknown' where there is no source.
- **C-META-METRICS.06** Turn money into the currency's smallest unit for any component ending in _minor, using the currency's standard decimal places: multiply by 100 for currencies with two decimals, such as USD, EUR and TWD; use the amount as shown for currencies without decimals, such as JPY and KRW. Say which rule you used.  
  _Done when:_ Each money amount as shown and in the smallest unit, with the rule used.
- **C-META-METRICS.07** Call record_numbers with the goal's exact component names, as record_numbers lists them for this goal (for example spend_minor, impressions, link_clicks, landing_page_views, attributed_conversions, qualified_leads, external_purchases, net_after_all_costs_minor), and a source for each. If there is no history, record 0 and say so in source. If a source is incomplete, say what is missing in source. Never estimate, and never change any ad during this step.  
  _Done when:_ The record_numbers call with every component, its value and its source.

**If stuck:**
- `cannot_open_reporting`: If you cannot open the ad account's reporting, ask the owner for a screenshot or export with the columns this goal needs, for the exact date range.
- `no_sales_records`: If there is no record of real sales or leads outside Meta, say so in source and leave those components unrecorded; never copy Meta's reported purchases as real ones.
- `cost_unknown`: If a cost needed for money after costs has no source, list it as unknown and ask the owner for the figure; do not estimate it.
- `too_early_to_read`: If the observation window has not passed, record the numbers as early and read them again after the window ends; do not fill conversions that have not arrived yet with 0.
- `settings_differ_from_baseline`: If the attribution setting, time zone or range length differs from the baseline, read again with the baseline's settings before recording.
- `no_history`: If the account has no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.

### 17. Pause only this round's Meta ads when the window ends

Pause exactly this round's ads once the numbers are read, and confirm they stopped spending, so the round costs no more than approved and the next test starts clean.

- **C-META-STOP.01** Take the list of campaign, ad set and ad IDs that were switched on this round. Use only that list; never pause by picking from all ads in the account.  
  _Done when:_ This round's IDs, taken from the switch-on step.
- **C-META-STOP.02** Check that the observation window has ended and that the current numbers were recorded. If they were not, record them first so the read covers the full window.  
  _Done when:_ The window end time and a note that the current numbers are recorded.
- **C-META-STOP.03** Tell the owner exactly which ads will be paused. Keep an ad running only if the owner asks for it and writes a new daily budget, total and end date for it; record that it is still spending at their request.  
  _Done when:_ The list shown to the owner and their answer, with any new written limits for an ad kept running.
- **C-META-STOP.04** Switch off only those IDs, using your own browser if the owner agreed, otherwise the owner does it. Do not delete anything, do not edit text, images or budgets, and do not touch other campaigns or brands.  
  _Done when:_ Who switched them off, at what time, and which IDs.
- **C-META-STOP.05** After about 15 minutes, read each object's delivery status and confirm it is off and not delivering. If it is unclear, check again before trying anything else; never report it as stopped without seeing it.  
  _Done when:_ Each ID with its status as shown and the time read.
- **C-META-STOP.06** Read the final amount spent for the round and compare it with the approved total. If it went over, report by how much.  
  _Done when:_ Final spend in the account currency and in its smallest unit, next to the approved total.
- **C-META-STOP.07** Write what the next round should test: one new change, the same account, Page and limits. Pausing never raises the budget or extends the owner's approval.  
  _Done when:_ One sentence on the next test and a note that the limits stay as approved.

**Hand back:** `paused_ids`, `status_after_pause`, `final_spend`, `next_test`

**If stuck:**
- `numbers_not_recorded`: If the current numbers were not recorded yet, record them first, then pause.
- `ids_unknown`: If you do not have this round's IDs, search the account for the round name and confirm the list with the owner before pausing anything.
- `still_delivering`: If an ad still shows as delivering after pausing, check again after 15 minutes and then ask the owner to switch it off by hand.
- `agent_cannot_change_ads`: If your browser cannot switch ads off, give the owner the exact list of IDs to switch off and ask for a screenshot after.
- `spend_over_total`: If final spend is above the approved total, pause at once and report the amount over to the owner.
