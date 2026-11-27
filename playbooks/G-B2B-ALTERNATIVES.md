# B2B SaaS: win trials from people searching for a competitor alternative

- **Goal id:** `G-B2B-ALTERNATIVES`
- **Channel:** b2b_search_ads
- **Metric:** `alternative_trial_signups` = `trial_signups`, should increase
- **Observation window:** 168 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), query (the next round starts with `C-ALT-RESEARCH`), content (the next round starts with `C-ALT-PAGES`), message (the next round starts with `C-GA-DRAFT`), delivery (the next round starts with `C-GOOGLE_ADS-ACCESS`), data (the next round starts with `C-B2B-METRICS`)

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

### 8. Confirm the SaaS offer, the sign-up path and where paid customers are counted

Pin down what a business buyer can sign up for and pay today, which accounts speak for the company, and where trials and paid customers are read, so every channel in this goal sends people to a working sign-up and every customer is counted once.

- **C-B2B-ACCESS.01** Use read_page on the pricing, sign-up and docs pages and write the offer: plans, monthly and yearly price, currency, trial length or free plan, whether a card is needed, refund policy, and who the product is for. The owner confirms it.  
  _Done when:_ The offer sheet with each line's URL and the owner's confirmation.
- **C-B2B-ACCESS.02** Open the sign-up flow up to the first screen that asks for details and check it loads on a computer and a phone. Create no account unless the owner asks for a test sign-up; if they do, use inbox_address for the email and inbox_latest for the code, and tell the owner to leave it out of the counts.  
  _Done when:_ The sign-up URL, what its first screen asks for, and any test account created.
- **C-B2B-ACCESS.03** Ask the owner where trials and paying customers are recorded: Stripe (connected on the hosted owner page, or an export), the product's admin, analytics, or a CRM they already use. Write which number comes from where. Never ask for a password or an API key.  
  _Done when:_ The source for trials, for paid customers and for visits, and who can read each.
- **C-B2B-ACCESS.04** Confirm that the sale counter from tracking is on the page shown after the first payment, or name the payment report that replaces it.  
  _Done when:_ Whether the sale counter is in place, or the report that will be used.
- **C-B2B-ACCESS.05** Ask which account speaks for the company in each channel this goal uses: the business email or sending domain, the founder's or company's profiles, the marketplace vendor account. Check that the names shown match the brand.  
  _Done when:_ Each account, who signed in, and the name shown.
- **C-B2B-ACCESS.06** Write the ideal customer in four lines from the research steps: company type and size, the buyer's role, the problem in their words, and what they use today. Add the 3 to 5 competitors buyers compare with, from the owner and from search.  
  _Done when:_ The four-line customer profile and the competitor list with URLs.
- **C-B2B-ACCESS.07** Agree the limits for this goal: daily caps for messages, the ad budget if ads are used, who presses send, and what may never be promised (roadmap features, custom work, discounts that do not exist). Get the owner's yes.  
  _Done when:_ The limits and the owner's approval message.

**Hand back:** `offer`, `signup_path`, `count_sources`, `accounts`, `customer_profile`

**If stuck:**
- `signup_broken`: If the sign-up or payment page fails, tell the owner before any channel sends people there.
- `no_count_source`: If paid customers cannot be read anywhere, ask the owner to connect Stripe on the owner page or export the customers list; never estimate.
- `wrong_account`: If a signed-in account is personal or another brand's, stop and ask the owner to switch.
- `offer_unclear`: If the pages and the owner disagree on price or plans, use neither until the owner confirms one.
- `owner_action_needed`: If a verification, terms or identity screen appears, stop and tell the owner which screen and which button.

### 9. Find the competitor searches buyers type and what they dislike about each

Find which 'alternative to' and 'versus' searches real buyers type, and what reviewers say they dislike about each competitor, from public sources, so the comparison pages and ads answer an actual buyer question honestly.

- **C-ALT-RESEARCH.01** For each competitor from the access step, list the searches buyers use: '{competitor} alternative', '{competitor} alternatives for {use case}', '{competitor} vs {product}', '{competitor} pricing', 'cheaper than {competitor}'. Check the search engine's suggestions and related questions for each, and the keyword tool's volumes if the owner's ad account is connected.  
  _Done when:_ The searches per competitor with where each came from and any volume shown.
- **C-ALT-RESEARCH.02** Use read_page on each competitor's pricing and feature pages and write what they charge and include today. Date it; prices change.  
  _Done when:_ Each competitor's plans and prices with URLs and the date read.
- **C-ALT-RESEARCH.03** Read public reviews of each competitor (G2, Capterra, app marketplace reviews, Reddit threads) and copy 5 to 10 complaints in the reviewers' words with links, above all the ones this product really solves.  
  _Done when:_ Quoted complaints with URLs, each marked 'we solve this', 'partly' or 'no'.
- **C-ALT-RESEARCH.04** Write a fair comparison table: where this product is better, where the competitor is better, and where they are the same, each with a source. Leave out anything you cannot verify.  
  _Done when:_ The comparison table with sources, including the competitor's real strengths.
- **C-ALT-RESEARCH.05** Pick 2 to 4 searches for this round, each with real volume or clear buying words and a complaint the product truly solves. Group them as the keyword groups the ad draft step will use.  
  _Done when:_ The chosen searches grouped for ads, with the reason for each.
- **C-ALT-RESEARCH.06** Note the rules: no competitor trademark in ad text where the ad platform or local law forbids it, no false or unverifiable claim about a competitor, and the date the comparison was checked shown on the page.  
  _Done when:_ The rules that apply, with a link to the ad platform's trademark policy.

**Hand back:** `searches`, `competitor_facts`, `complaints`, `comparison_table`, `chosen_searches`

**If stuck:**
- `no_competitor_known`: If no competitor is known, search the problem in buyer words and list the tools people mention before going on.
- `no_volume_data`: If no search volume can be seen, choose searches with clear buying words and write 'volume unknown'.
- `cannot_verify_claim`: If a fact about a competitor cannot be checked on their own pages or a public review, leave it out.
- `trademark_rule`: If the ad platform restricts a competitor's trademark, keep it out of the ad text and use it only as a keyword where allowed.

### 10. Confirm the Google Ads account, who edits it, and the budget cap

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

### 11. Read this goal's B2B numbers: trials, meetings, deals and paid customers (baseline numbers)

Record the number this goal is judged on, counted once per real company and net of tests, refunds and duplicates, for the window before this round and for this round, so channels are compared on buyers rather than activity.

- **C-B2B-METRICS.01** Call where_are_we (with lane in a month target) and copy this goal's component names and window.  
  _Done when:_ The goal id, the component names and the window in hours.
- **C-B2B-METRICS.02** Write the counting rule for each component before counting. trial_signups: a new trial or free-plan account from an outside company inside the window, from this goal's links or pages. deals_sold: codes or deals sold on the marketplace inside the window, minus refunds shown inside it. marketplace_signups: installs or sign-ups the marketplace or the tracked link credits to the listing. trial_to_paid_conversions and eligible_trials: trials in this round's group whose pay date fell inside the window, and how many of them paid. confirmed_meetings: a call with a target company that both sides accepted on the calendar. partner_paid_customers: customers who paid inside the window and came through a partner's link, code or introduction.  
  _Done when:_ The rule for this goal's components, with dates and time zone.
- **C-B2B-METRICS.03** Read the sources for the window: tracking (clicks per label and the sale counter), the payment tool or Stripe connection, the product's admin or analytics for sign-ups, the marketplace's vendor dashboard, and the calendar or CRM for meetings. If a source cannot be opened, ask the owner for an export of that exact window.  
  _Done when:_ Each source with the time it was read or the file received.
- **C-B2B-METRICS.04** Keep one row per company: merge duplicates by domain or email, and remove the owner's, team's, test and competitor accounts, free accounts given away, and refunds inside the window.  
  _Done when:_ What was removed and why, with counts before and after.
- **C-B2B-METRICS.05** For the baseline, count the same components for the same length of time just before this round. If there is no history, record 0 and say 'no history'.  
  _Done when:_ The baseline values and how they were taken.
- **C-B2B-METRICS.06** Call record_numbers with each component under its exact name and a source naming each report and when it was read. In a month target lane also pass paid_customers (paying customers since the month started, from the payment records), and visits and signups if you have them; they update the month progress and are not judged here. Never estimate.  
  _Done when:_ The record_numbers call as accepted.
- **C-B2B-METRICS.07** Write one line on where the funnel stalls: too few people reached, reached but not signing up, signing up but not using it, or using it but not paying.  
  _Done when:_ One line naming the stalled stage with the numbers behind it.

**If stuck:**
- `cannot_open_source`: If a source cannot be opened, ask the owner for an export of the exact window; never estimate.
- `no_history`: If there is no earlier window to compare, record 0 and say 'no history'; the first round sets the baseline.
- `attribution_unknown`: If a sign-up or payment cannot be tied to this goal's links, pages or partners, leave it out and say how many.
- `window_not_finished`: If the window has not ended, report the reading as early and read again when it ends.
- `denominator_zero`: If a rate's denominator is 0, record 0, say so in source, and claim no rate.

### 12. Publish an honest comparison page for each chosen competitor search

Give buyers who search for an alternative a page on the owner's site that answers their question fairly and puts the trial one click away, because a page that is fair to the competitor is the one buyers trust and search engines keep.

- **C-ALT-PAGES.01** For each chosen search, write one page: a title that matches the search ('{competitor} alternative for {use case}'), who should switch and who should not, the comparison table with sources and the date checked, the complaints it solves quoted from public reviews with links, how to switch (import, setup time), the price, and one call to the trial with the round's tracked link (?v= per page).  
  _Done when:_ Each page's full text with sources.
- **C-ALT-PAGES.02** Check every claim against the product facts and the competitor's own pages; remove anything not true today. Keep the competitor's strengths in.  
  _Done when:_ A claim-by-claim check.
- **C-ALT-PAGES.03** Show the owner each page word for word and get a clear yes.  
  _Done when:_ The owner's approval.
- **C-ALT-PAGES.04** The owner publishes it on their site, or the agent does with its own tools and the owner's yes. Check it loads, can be indexed (no noindex), has a clear title and description, and is linked from the site's footer or a 'compare' page so search engines find it.  
  _Done when:_ The live URL, the indexing check, and where it is linked from.
- **C-ALT-PAGES.05** Submit the page in the owner's search console if it is connected, or note that it is not. Pass the page URL as the first item in links.  
  _Done when:_ The submission result or 'not connected'.

**Hand back:** `page_urls`, `published_text`, `owner_approval`, `tracked_links`

**If stuck:**
- `no_site_access`: If nobody can publish on the site, submit the step as blocked and tell the owner exactly which page to add and where.
- `claim_not_verified`: If a claim cannot be verified today, remove it before publishing.
- `owner_has_not_approved`: If the owner has not approved the page, publish nothing.
- `page_noindex`: If the page cannot be indexed, ask the owner to remove the noindex setting before the round is measured.

### 13. Build the Google search ad as a paused draft

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

### 14. Switch on only this round's Google ads, within the approved cap

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

### 15. Read this goal's B2B numbers: trials, meetings, deals and paid customers (result numbers)

Record the number this goal is judged on, counted once per real company and net of tests, refunds and duplicates, for the window before this round and for this round, so channels are compared on buyers rather than activity.

- **C-B2B-METRICS.01** Call where_are_we (with lane in a month target) and copy this goal's component names and window.  
  _Done when:_ The goal id, the component names and the window in hours.
- **C-B2B-METRICS.02** Write the counting rule for each component before counting. trial_signups: a new trial or free-plan account from an outside company inside the window, from this goal's links or pages. deals_sold: codes or deals sold on the marketplace inside the window, minus refunds shown inside it. marketplace_signups: installs or sign-ups the marketplace or the tracked link credits to the listing. trial_to_paid_conversions and eligible_trials: trials in this round's group whose pay date fell inside the window, and how many of them paid. confirmed_meetings: a call with a target company that both sides accepted on the calendar. partner_paid_customers: customers who paid inside the window and came through a partner's link, code or introduction.  
  _Done when:_ The rule for this goal's components, with dates and time zone.
- **C-B2B-METRICS.03** Read the sources for the window: tracking (clicks per label and the sale counter), the payment tool or Stripe connection, the product's admin or analytics for sign-ups, the marketplace's vendor dashboard, and the calendar or CRM for meetings. If a source cannot be opened, ask the owner for an export of that exact window.  
  _Done when:_ Each source with the time it was read or the file received.
- **C-B2B-METRICS.04** Keep one row per company: merge duplicates by domain or email, and remove the owner's, team's, test and competitor accounts, free accounts given away, and refunds inside the window.  
  _Done when:_ What was removed and why, with counts before and after.
- **C-B2B-METRICS.05** For the baseline, count the same components for the same length of time just before this round. If there is no history, record 0 and say 'no history'.  
  _Done when:_ The baseline values and how they were taken.
- **C-B2B-METRICS.06** Call record_numbers with each component under its exact name and a source naming each report and when it was read. In a month target lane also pass paid_customers (paying customers since the month started, from the payment records), and visits and signups if you have them; they update the month progress and are not judged here. Never estimate.  
  _Done when:_ The record_numbers call as accepted.
- **C-B2B-METRICS.07** Write one line on where the funnel stalls: too few people reached, reached but not signing up, signing up but not using it, or using it but not paying.  
  _Done when:_ One line naming the stalled stage with the numbers behind it.

**If stuck:**
- `cannot_open_source`: If a source cannot be opened, ask the owner for an export of the exact window; never estimate.
- `no_history`: If there is no earlier window to compare, record 0 and say 'no history'; the first round sets the baseline.
- `attribution_unknown`: If a sign-up or payment cannot be tied to this goal's links, pages or partners, leave it out and say how many.
- `window_not_finished`: If the window has not ended, report the reading as early and read again when it ends.
- `denominator_zero`: If a rate's denominator is 0, record 0, say so in source, and claim no rate.

### 16. Pause only this round's Google ads and close the round

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
