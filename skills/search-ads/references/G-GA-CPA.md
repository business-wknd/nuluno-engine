# Google Ads: lower the cost per conversion

- **Goal id:** `G-GA-CPA`
- **Language:** English
- **Channel:** google_ads
- **Metric:** `conversion_cpa` = `spend_minor` / `attributed_conversions`, should decrease
- **Observation window:** 168 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), query (the next round starts with `C-GA-KEYWORDS`), message (the next round starts with `A-COPY`), data (the next round starts with `C-GA-METRICS`)

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

### 8. Confirm the Google Ads account, who edits it, and the budget cap

Settle which Google Ads account the round uses, who signs in and makes changes, what it can already measure, and how much the owner allows to spend, so the draft is built in the right account and never spends more than approved.

- **C-GOOGLE_ADS-ACCESS.01** Ask the owner for the 10-digit customer ID (shown as 123-456-7890) of the account that will run the ads, and the website it advertises. If the account sits under a manager account, write down both IDs. Identify the brand by customer ID, never by account name, because two accounts can share a name.  
  _Done when:_ The customer ID, any manager account ID, the website, and the owner's confirmation that this account belongs to this brand.
- **C-GOOGLE_ADS-ACCESS.02** Decide who makes changes: the owner in their own browser, or the agent's browser if it is already signed in to a Google account with access to this customer ID. The owner signs in themselves; never ask for a password. Note the access level of the signed-in user. Read only access cannot create drafts.  
  _Done when:_ Who makes changes, the signed-in Google account, and its access level for this customer ID.
- **C-GOOGLE_ADS-ACCESS.03** If the owner has no Google Ads account yet, the owner creates exactly one on the official Google Ads sign-up page and enters billing details themselves. Do not create extra accounts, and never create a new one to get around a suspension. Advertiser verification and identity checks are done by the owner.  
  _Done when:_ The new customer ID and the owner's note that they created it, or a note that an account already existed.
- **C-GOOGLE_ADS-ACCESS.04** Read the account's currency, time zone, billing status and advertiser verification status. The currency cannot be changed after the account is made, so every budget and report in this round uses this currency and time zone. Do not add, change or use a payment method.  
  _Done when:_ Currency, time zone, billing status and verification status, as shown in the account.
- **C-GOOGLE_ADS-ACCESS.05** Open the account's list of conversion actions. For each, write down the name, where it comes from (website, import, app or phone), whether it is primary or secondary, its status as shown, and how many it recorded in the last 30 days. Pick the one that matches the goal's main number. Do not add tags or change the website in this step.  
  _Done when:_ The list of conversion actions with their status and 30-day counts, and the one this goal will be judged on, or a note that none fits.
- **C-GOOGLE_ADS-ACCESS.06** List the existing campaigns with their status, daily budget, keyword match types and negative keywords. Agree with the owner that this round only creates one new search campaign, and that no existing campaign, keyword or negative list is changed.  
  _Done when:_ The existing campaigns that stay untouched, and the owner's agreement on what this round may create.
- **C-GOOGLE_ADS-ACCESS.07** Ask the owner to write, in this conversation, the most the round may spend per day and in total, in the account currency, and the last day of the round. Check whether recommendations are set to apply automatically; if they are, tell the owner they can change the test without asking and ask whether to turn that off. Never accept a recommendation as part of this round.  
  _Done when:_ The owner's written daily cap, total cap and end date, plus the auto-apply setting and the owner's choice.

**Hand back:** `customer_id`, `who_changes`, `currency_and_time_zone`, `conversion_to_judge`, `approved_caps`

**If stuck:**
- `wrong_customer_id`: If the ID belongs to a manager account or another brand, stop and ask the owner for the exact customer ID of this brand; never change settings at the manager level.
- `read_only_access`: If the signed-in user has read only access, set who_changes to 'owner' or ask the owner to grant standard access to that user themselves.
- `no_conversion_action`: If no conversion action fits the goal, do not install tags; plan to count results with the round's sale counter and site analytics, and tell the owner.
- `billing_or_verification_pending`: If billing is not set up or verification is pending, tell the owner which screen needs them and wait; the agent never enters payment details.
- `no_written_caps`: If the owner has not written a daily cap, total cap and end date, stop here and ask for them; never guess a budget.
- `account_suspended`: If the account is suspended, stop and tell the owner; never create another account to get around it.

### 9. Sort real Google search terms into keep, test and negative lists

Turn the search terms people actually typed into keep, test and negative lists with one fixed review rule, so the round's money goes to searches with buying intent and the goal's main number can move.

- **C-GA-KEYWORDS.01** Open the search terms report for the agreed customer ID and campaigns. Use the last 30 days ending yesterday, or the days since the campaign started if shorter, in the account time zone. If the account has never run search ads, skip to step 6.  
  _Done when:_ The customer ID, campaign names, date range with time zone, and how many search terms the report lists.
- **C-GA-KEYWORDS.02** Copy each search term with its impressions, clicks, cost and conversions, plus the keyword and match type that triggered it. Keep keywords and search terms apart: a keyword is what the account bids on, a search term is what the person typed.  
  _Done when:_ A table of search terms with those columns and the keyword that triggered each.
- **C-GA-KEYWORDS.03** Mark each term as brand (contains the brand or product name) or non-brand. Then put each non-brand term in one class: buying (wants the product's job done, compares options, asks price), research (how-to or free information), job seeker (jobs, salary, careers), free seeker (free, download, crack), or unrelated (a different meaning). Add a one-line reason when the class is not obvious.  
  _Done when:_ Every term with its brand mark, class and, where needed, a reason.
- **C-GA-KEYWORDS.04** Write down the review rule and keep it the same in every round: review every term with at least one click, or the top 100 by cost if there are more. Count the terms reviewed, the terms marked buying, and the total cost of terms marked job seeker, free seeker or unrelated. The measurement step uses this same rule.  
  _Done when:_ The written review rule and the three counts it gives for this date range.
- **C-GA-KEYWORDS.05** Propose negative keywords only with clear evidence: a job seeker, free seeker or unrelated term that spent money, or a word that repeats in at least three such terms. Use phrase or exact match for multi-word negatives. Never add a generic negative list, never block a word that also appears in a term that converted, and never delete keywords just because their volume is low. If the window has fewer than 30 clicks in total, mark every negative as a candidate only.  
  _Done when:_ Each proposed negative with its match type, the terms that justify it, and a check against converting terms.
- **C-GA-KEYWORDS.06** Propose the keywords to keep or add, at most 20, grouped so each group serves one buyer situation from the segments and the chosen angle. Use phrase or exact match for a small budget. With no search history, build them from the buyer quotes and patterns such as '{job} software', '{category} price' and '{category} alternative', search each one on Google and note whether the results show buying intent.  
  _Done when:_ Keyword groups with match types, each keyword tied to the quote or search result it came from.
- **C-GA-KEYWORDS.07** Write the one change this round tests, for example 'the same keywords plus these 12 negatives' or 'one new ad group for situation X'. The change goes into this round's new campaign only, never into an existing one, and everything else stays the same. Do not change the sales page or tracking here. Show the owner the keep list, the negative list and the test change, and get a yes before the draft step uses them.  
  _Done when:_ A one-sentence test plan, the final lists, and the owner's approval message.

**Hand back:** `search_terms_reviewed`, `keep_keywords`, `negative_keywords`, `review_rule`, `test_change`

**If stuck:**
- `no_search_history`: If the account has never run search ads, build the lists from buyer quotes and Google search results and mark every keyword as untested.
- `cannot_open_report`: If you cannot open the search terms report, ask the owner for an export or screenshot of it for the agreed date range.
- `too_few_clicks`: If the range has fewer than 30 clicks, propose negatives only as candidates and do not remove any keyword.
- `negative_blocks_converter`: If a proposed negative would block a term that converted, drop that negative and note why.
- `wrong_account`: If the report shows a different customer ID from the agreed one, do not use it and ask the owner again.

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

### 11. Read this goal's numbers from Google Ads (baseline numbers)

Record the exact numbers this goal is judged on, for the period before the round and for the round itself, from Google Ads and the owner's payment records, so rounds are compared on real numbers. record_numbers lists exactly which numbers it needs.

- **C-GA-METRICS.01** Confirm the customer ID, the currency and the time zone. For the baseline, use the same number of days as the round lasts, ending the day before this round's ads are switched on, and count the account's existing search campaigns. For the current reading, use the days since this round's ads were switched on and count only this round's campaign. Use the same conversion action, review rule and sources for both. If you cannot open the ad account's reporting, ask the owner for an export or screenshot.  
  _Done when:_ Customer ID, the campaigns counted, date range with time zone, currency, and how the numbers will be obtained.
- **C-GA-METRICS.02** Check which components record_numbers asks for and use those exact names. Goals that use this step ask for: spend_minor and attributed_conversions (cost per conversion), irrelevant_spend_minor and spend_minor (share of wasted spend), qualified_queries and reviewed_queries (search term fit), or external_purchases and attributed_sessions (purchase rate of ad visitors).  
  _Done when:_ The list of component names this goal needs, copied from record_numbers.
- **C-GA-METRICS.03** Read cost for the range and convert it to the currency's smallest unit without rounding. Example: US$12.34 is 1234. For a currency shown without decimals, such as JPY, use the figure as shown. Never convert to another currency.  
  _Done when:_ Cost as shown, and the same figure in the smallest unit.
- **C-GA-METRICS.04** For conversions, count only the conversion action agreed for this goal, and write down the click-through conversion window shown in its settings. Google can add conversions days after the click. If the range ended less than 7 days ago, say in source that the number is early and read it again 7 days later if the round is still open. Google's conversion value or return on ad spend is not the owner's income.  
  _Done when:_ The conversion action name, its conversion window, its count for the range, and whether it is early.
- **C-GA-METRICS.05** For search term numbers, apply the saved review rule and classes from the keywords step to this range: reviewed_queries is the count of terms reviewed, qualified_queries the count marked buying, irrelevant_spend_minor the cost of terms marked job seeker, free seeker or unrelated. If the report shows cost not tied to any visible term, say how much and leave it out.  
  _Done when:_ The three counts with the rule used, and any cost from hidden terms.
- **C-GA-METRICS.06** For purchases and visits, take external_purchases from the owner's payment records or the round's sale counter, counting each order once and only real outside buyers: leave out the owner's, test and refunded purchases. Count only purchases you can tie to Google Ads, and say how many other sales were left out. Take attributed_sessions from the site analytics' sessions from Google Ads (paid search) and name the report; use the same source for baseline and current.  
  _Done when:_ Purchases and sessions, each with its source, what was left out, and how many sales could not be tied to the ads.
- **C-GA-METRICS.07** Call record_numbers with each component's exact name, its value, and a source naming the report or export, the customer ID, the date range, the time zone and any 'early' note. If there is no history, record 0 and say 'no history' in source. Never estimate; a number that is not shown is not recorded. Do not change any ad, keyword or budget in this step.  
  _Done when:_ The record_numbers call with names, values and sources.

**If stuck:**
- `cannot_open_reporting`: If you cannot open the ad account's reporting, ask the owner for an export or screenshot covering the exact date range.
- `no_history`: If the account has no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.
- `conversions_still_arriving`: If the range ended less than 7 days ago, record the numbers as early and read them again after 7 days.
- `conversion_action_missing`: If the agreed conversion action does not exist or recorded nothing, use the payment records or sale counter and say so; never fill the gap with a guess.
- `numbers_from_wrong_account`: If the screen or export shows a different customer ID, do not use those numbers and ask again.
- `currency_mismatch`: If the report currency differs from the account currency agreed earlier, stop and confirm the currency with the owner; never convert to make it fit.

### 12. Build the Google search ad as a paused draft

Create this round's search campaign, keywords and ad in the account, switched off, exactly as the owner approved, so it can be switched on later with no surprises in budget, wording or link.

- **C-GA-DRAFT.01** Before building, check again: the customer ID, the owner's written daily cap, total cap and end date in the account currency, the target locations and language agreed with the owner from the buyer segments, and the conversion action. If any cap is missing, stop.  
  _Done when:_ Customer ID, caps quoted from the owner's message, end date, locations, language and conversion action.
- **C-GA-DRAFT.02** Plan the structure: one new search campaign for this round only, on Google Search with the Display Network switched off; one ad group per keyword group from the keywords step, with those keywords, match types and the approved negatives. Pick the bid strategy with the owner: if the agreed conversion action recorded fewer than 15 conversions in the last 30 days, use Maximize clicks with a maximum cost per click limit; otherwise use Maximize conversions. Daily budget no higher than the owner's daily cap, and an end date on the last day of the round.  
  _Done when:_ A written plan of campaign, ad groups, keywords, negatives, bid strategy, budget and dates.
- **C-GA-DRAFT.03** Write one responsive search ad per ad group from the approved copy: 8 to 15 headlines of 30 characters or fewer, and 2 to 4 descriptions of 90 characters or fewer; Chinese, Japanese and Korean characters count as two each. Each line must be backed by the product facts. No invented prices, discounts, ratings, 'best' or '#1' claims, scarcity or guarantees.  
  _Done when:_ Every headline and description with its character count and the fact it relies on.
- **C-GA-DRAFT.04** Google Ads does not accept a final URL that forwards to a different domain, so do not use the round's tracked link here. Set each ad's final URL to the product page with ?v=A, ?v=B when ads differ, plus utm_source=google&utm_medium=cpc so site analytics can count the visits. Open each URL and see the product page load. Tell the owner that sales from this round are counted with the sale counter and site analytics.  
  _Done when:_ The final URL for each ad, opened and confirmed to load the product page.
- **C-GA-DRAFT.05** Show the owner word for word: campaign name, locations, language, daily budget, end date, keywords, negatives, every headline and description, and the final URLs. Get a clear yes before creating anything.  
  _Done when:_ The full draft as shown to the owner and their approval message.
- **C-GA-DRAFT.06** Create only this round's campaign, ad groups and ads, in the owner's browser or the agent's own browser if the owner said yes. Set the campaign start date to a day in the future while building, and set the campaign to Paused as soon as the screen allows, at the latest right after publishing. Touch nothing that already exists. If a save seems to fail, check the campaign list before trying again so nothing is created twice.  
  _Done when:_ The names and IDs of the new campaign, ad groups and ads, all paused, and the start date as set.
- **C-GA-DRAFT.07** Open the draft again and check: status Paused, start date, daily budget, currency, end date, locations, language, Display Network off, bid strategy, keywords, negatives, final URLs, and each ad's policy status. A paused draft is not live. If an ad is disapproved, read the reason, fix only that line, and show the change to the owner.  
  _Done when:_ Each setting as it appears in the account, and each ad's policy status.

**Hand back:** `campaign_id`, `ad_ids`, `daily_budget`, `final_urls`, `policy_status`

**If stuck:**
- `no_written_caps`: If the owner has not written a daily cap, total cap and end date, stop and ask for them before building.
- `owner_has_not_approved`: If the owner has not said yes to this exact draft, do not create it; show it and wait.
- `policy_disapproved`: If an ad is disapproved, read the stated reason and rewrite only that line; if the product or page itself must change, stop that ad and tell the owner.
- `product_page_not_loading`: If the product page does not load or shows an error, do not build the ads; tell the owner which URL failed.
- `read_only_access`: If the signed-in user cannot create campaigns, hand the owner the full draft to enter themselves and ask for the IDs back.
- `duplicate_campaign`: If a second copy of the campaign appears, remove the extra paused copy only after the owner agrees, and keep one.

### 13. Switch on only this round's Google ads, within the approved cap

Turn on only the approved paused campaign, at a budget the owner wrote down, so real searches reach the ad and the goal's main number gets new data without risking more money than allowed.

- **C-GA-ACTIVATE.01** Open the paused draft and confirm the customer ID and the campaign, ad group and ad IDs from the draft step. These are the only items this step may switch on.  
  _Done when:_ The list of IDs to switch on, matching the draft step.
- **C-GA-ACTIVATE.02** Check the money against the owner's written caps: the daily budget times the number of days is at or below the total cap, and the end date is set. Google can spend up to twice the daily budget on a single day, so either set the daily budget to half the owner's daily cap or get the owner to write that a single day may reach twice the budget. A zero or missing cap means do not switch on.  
  _Done when:_ Daily budget, number of days, planned total, end date, the owner's caps side by side, and how the two-times rule was handled.
- **C-GA-ACTIVATE.03** Check each ad's policy status. If it is under review, wait and check again; never edit an ad to get around review. If it is disapproved, go back to the draft step.  
  _Done when:_ Each ad's policy status at the time of the check.
- **C-GA-ACTIVATE.04** Ask the owner for a yes in this conversation to switch on now, stating the campaign name, daily budget, total cap and end date.  
  _Done when:_ The owner's message saying yes to these exact figures.
- **C-GA-ACTIVATE.05** Switch on only this round's campaign, ad groups and ads, and set the start date to today if it was set in the future. Do not switch on any other paused item, raise any budget, or accept any recommendation.  
  _Done when:_ The time the campaign was switched on and who switched it on.
- **C-GA-ACTIVATE.06** Within 3 hours, check the status and whether impressions have started. Then check spend once a day: it must stay under the daily cap, and when total spend comes within one daily budget of the total cap, run the stop step. If the status says limited, write down the reason Google gives.  
  _Done when:_ Status, impressions, daily spend and total spend at each check, with the times read.
- **C-GA-ACTIVATE.07** Write down the stop date and the total cap, and plan the stop step for whichever comes first. Since a search ad has no public post URL, hand back the ad IDs, the final URL and a screenshot of the ad as shown in the account.  
  _Done when:_ The stop date, the planned stop trigger, and the ad IDs with final URL and screenshot.

**Hand back:** `switched_on_ids`, `live_since`, `delivery_status`, `stop_plan`

**If stuck:**
- `owner_has_not_approved`: If the owner has not said yes to switching on at these figures, do not switch on; ask and wait.
- `budget_over_cap`: If the daily budget or planned total is above the owner's cap, lower the budget to fit or ask the owner for a new written cap.
- `ad_under_review`: If an ad is still under review, keep the same ad and check again later; never create a copy to skip review.
- `ad_disapproved`: If an ad is disapproved, leave it paused, read the reason and go back to the draft step.
- `billing_problem`: If Google shows a billing problem, stop and tell the owner which screen needs them; never touch payment details.
- `not_delivering`: If there are no impressions after 24 hours, read the status reason Google shows and report it; do not raise the budget.

### 14. Read this goal's numbers from Google Ads (result numbers)

Record the exact numbers this goal is judged on, for the period before the round and for the round itself, from Google Ads and the owner's payment records, so rounds are compared on real numbers. record_numbers lists exactly which numbers it needs.

- **C-GA-METRICS.01** Confirm the customer ID, the currency and the time zone. For the baseline, use the same number of days as the round lasts, ending the day before this round's ads are switched on, and count the account's existing search campaigns. For the current reading, use the days since this round's ads were switched on and count only this round's campaign. Use the same conversion action, review rule and sources for both. If you cannot open the ad account's reporting, ask the owner for an export or screenshot.  
  _Done when:_ Customer ID, the campaigns counted, date range with time zone, currency, and how the numbers will be obtained.
- **C-GA-METRICS.02** Check which components record_numbers asks for and use those exact names. Goals that use this step ask for: spend_minor and attributed_conversions (cost per conversion), irrelevant_spend_minor and spend_minor (share of wasted spend), qualified_queries and reviewed_queries (search term fit), or external_purchases and attributed_sessions (purchase rate of ad visitors).  
  _Done when:_ The list of component names this goal needs, copied from record_numbers.
- **C-GA-METRICS.03** Read cost for the range and convert it to the currency's smallest unit without rounding. Example: US$12.34 is 1234. For a currency shown without decimals, such as JPY, use the figure as shown. Never convert to another currency.  
  _Done when:_ Cost as shown, and the same figure in the smallest unit.
- **C-GA-METRICS.04** For conversions, count only the conversion action agreed for this goal, and write down the click-through conversion window shown in its settings. Google can add conversions days after the click. If the range ended less than 7 days ago, say in source that the number is early and read it again 7 days later if the round is still open. Google's conversion value or return on ad spend is not the owner's income.  
  _Done when:_ The conversion action name, its conversion window, its count for the range, and whether it is early.
- **C-GA-METRICS.05** For search term numbers, apply the saved review rule and classes from the keywords step to this range: reviewed_queries is the count of terms reviewed, qualified_queries the count marked buying, irrelevant_spend_minor the cost of terms marked job seeker, free seeker or unrelated. If the report shows cost not tied to any visible term, say how much and leave it out.  
  _Done when:_ The three counts with the rule used, and any cost from hidden terms.
- **C-GA-METRICS.06** For purchases and visits, take external_purchases from the owner's payment records or the round's sale counter, counting each order once and only real outside buyers: leave out the owner's, test and refunded purchases. Count only purchases you can tie to Google Ads, and say how many other sales were left out. Take attributed_sessions from the site analytics' sessions from Google Ads (paid search) and name the report; use the same source for baseline and current.  
  _Done when:_ Purchases and sessions, each with its source, what was left out, and how many sales could not be tied to the ads.
- **C-GA-METRICS.07** Call record_numbers with each component's exact name, its value, and a source naming the report or export, the customer ID, the date range, the time zone and any 'early' note. If there is no history, record 0 and say 'no history' in source. Never estimate; a number that is not shown is not recorded. Do not change any ad, keyword or budget in this step.  
  _Done when:_ The record_numbers call with names, values and sources.

**If stuck:**
- `cannot_open_reporting`: If you cannot open the ad account's reporting, ask the owner for an export or screenshot covering the exact date range.
- `no_history`: If the account has no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.
- `conversions_still_arriving`: If the range ended less than 7 days ago, record the numbers as early and read them again after 7 days.
- `conversion_action_missing`: If the agreed conversion action does not exist or recorded nothing, use the payment records or sale counter and say so; never fill the gap with a guess.
- `numbers_from_wrong_account`: If the screen or export shows a different customer ID, do not use those numbers and ask again.
- `currency_mismatch`: If the report currency differs from the account currency agreed earlier, stop and confirm the currency with the owner; never convert to make it fit.

### 15. Pause only this round's Google ads and close the round

Pause exactly the campaign this round switched on, confirm spending has stopped, and record the final spend, so the round's result is clean and no money leaks after the test.

- **C-GA-STOP.01** Take the list of IDs from the switch-on step. This list is the only thing this step may pause. Never use 'all enabled campaigns' as the list.  
  _Done when:_ The campaign, ad group and ad IDs this round switched on.
- **C-GA-STOP.02** Confirm why the round ends: the end date arrived, the total cap was reached, or the owner asked. Make sure the current numbers were read for the full window before pausing; if not, read spend and conversions now.  
  _Done when:_ The reason the round ends, and the time the current numbers were read.
- **C-GA-STOP.03** Save the ads as they ran: headlines, descriptions, keywords, negatives, budget and final URLs, so the next round can change one thing from a known start.  
  _Done when:_ A saved copy of the round's ads and settings.
- **C-GA-STOP.04** Tell the owner which items will be paused, by name and ID. If the owner wants to keep them running, stop here and ask for a new written daily cap, total cap and end date.  
  _Done when:_ The message to the owner listing the items to pause, and their answer.
- **C-GA-STOP.05** Pause only those IDs. Do not delete or remove any campaign, do not touch other campaigns or other brands, and do not change billing.  
  _Done when:_ The time each item was paused and who paused it.
- **C-GA-STOP.06** Open the account again and confirm each item shows Paused. Compare spend at the time of pausing with spend 24 hours later; a small late charge can appear, but new clicks should stop. If the status did not change, check again before trying a second time.  
  _Done when:_ Status of each item and spend at pause time and 24 hours later.
- **C-GA-STOP.07** Record the final spend in the currency's smallest unit and write the one change the next round will test. The next round starts from a new draft; pausing never extends the budget or the owner's approval.  
  _Done when:_ Final spend in the smallest unit and the next round's single change.

**Hand back:** `paused_ids`, `paused_at`, `final_spend_minor`, `next_change`

**If stuck:**
- `ids_unknown`: If you do not have the IDs from the switch-on step, find the round's campaign by its exact name and creation date and confirm it with the owner before pausing.
- `pause_not_taking`: If the status does not show Paused, wait 15 minutes and check again before retrying; tell the owner if it still runs.
- `owner_wants_to_continue`: If the owner wants the ads to keep running, ask for a new written daily cap, total cap and end date before doing anything.
- `spend_after_pause`: If spend keeps rising 24 hours after the pause, check the status of every item and tell the owner the exact figures.
- `wrong_account`: If the signed-in account shows a different customer ID, stop and switch to the agreed account before pausing anything.
