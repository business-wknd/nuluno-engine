# B2B SaaS: sell a launch deal on SaaS deal marketplaces

- **Goal id:** `G-B2B-LTD`
- **Channel:** b2b_saas
- **Metric:** `deals_sold` = `deals_sold`, should increase
- **Observation window:** 168 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), proposal (the next round starts with `C-LTD-ACCESS`), content (the next round starts with `C-LTD-LISTING`), proof (the next round starts with `C-LTD-SUPPORT`), data (the next round starts with `C-B2B-METRICS`)

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

### 9. Choose the deal marketplace and get the deal terms approved by the owner

Pick the deal marketplace whose buyers match this product and settle deal terms the owner can afford to honour for as long as the deal promises, before anything is listed, because a lifetime deal can sell fast and every buyer must still be served afterwards.

- **C-LTD-ACCESS.01** List the SaaS deal marketplaces that could fit (for example AppSumo, PitchGround, Dealify or SaaS Mantra) and use read_page on each one's current partner or 'sell with us' page. Note who their buyers are, which categories they accept, and their published requirements and terms (working product, support, refund window, revenue share or fees). Quote what each page says today and write 'unknown' where it does not say.  
  _Done when:_ Each marketplace with its partner page URL, the quoted requirements and terms, and the date read.
- **C-LTD-ACCESS.02** Check the product against each marketplace's requirements: it works today without manual setup, it has help pages and a support contact, and it can redeem codes or create accounts for deal buyers the way the marketplace needs. List anything missing as owner work, never as done.  
  _Done when:_ A pass or missing list per marketplace.
- **C-LTD-ACCESS.03** Work out with the owner what one deal buyer costs: hosting and AI cost per active account per month, support time per buyer, payment and marketplace fees, and how long service is promised. Compare it with the deal price after the marketplace's share. If a lifetime deal loses money, propose a limited deal instead (a yearly deal, usage caps, or a capped number of codes).  
  _Done when:_ The cost per buyer, the net per sale after fees, and the recommendation with the numbers behind it.
- **C-LTD-ACCESS.04** Draft the deal terms: tiers (for example 1, 2 or 3 stacked codes), price per tier, what each includes and its usage limits, what is excluded (future plans, add-ons), the refund window the marketplace sets, the number of codes, and how long service is promised.  
  _Done when:_ The draft terms as a table.
- **C-LTD-ACCESS.05** Get the owner's written approval of the exact terms. The owner applies and signs the marketplace's partner agreement themselves; the agent never accepts terms for them. If the form needs a new vendor account, the owner creates it.  
  _Done when:_ The owner's approval of the terms and the application's status (who submitted it and when).
- **C-LTD-ACCESS.06** Write the support plan: who answers deal buyers, how fast, where (the deal page's questions, email, help desk), and how many new users a week the team can onboard.  
  _Done when:_ The support plan with names, response time and weekly capacity.

**Hand back:** `marketplace_choice`, `requirements_check`, `unit_economics`, `deal_terms`, `owner_approval`, `support_plan`

**If stuck:**
- `product_not_ready`: If the product does not meet a requirement, list the owner work and do not apply until it is done.
- `terms_lose_money`: If the deal loses money per buyer, do not recommend it; show the owner the numbers and the limited options.
- `owner_has_not_approved`: If the owner has not approved the exact terms in writing, list nothing.
- `application_rejected`: If the marketplace declines, record its reason and propose the next marketplace to the owner.
- `marketplace_waitlist`: If the marketplace has a waiting list, submit the step as blocked with the expected date.

### 10. Read this goal's B2B numbers: trials, meetings, deals and paid customers (baseline numbers)

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

### 11. Publish the deal listing with true claims and the approved terms

Get the deal live, or in a later round improve it, with a listing that states exactly what buyers get under the approved terms, with real screenshots and a demo, so buyers know what they pay for and refunds stay low.

- **C-LTD-LISTING.01** Read the marketplace's listing guide and two or three successful listings in the same category; note their sections, image sizes, video length and the questions buyers ask most.  
  _Done when:_ The guide URL, the listings read and the sections required.
- **C-LTD-LISTING.02** Write the listing from the product facts: a headline with the buyer's outcome, who it is for and not for, what it does today (no roadmap promises), the tiers exactly as approved, limits, and how to redeem. Mark anything that will change after the deal as 'not included'.  
  _Done when:_ The listing text with a source for each claim.
- **C-LTD-LISTING.03** Prepare assets from the real product: screenshots, a short demo of a real task (the demo video step's video can be used), and the founder's short note if the owner wants one.  
  _Done when:_ The asset list with file names and what each shows.
- **C-LTD-LISTING.04** Show the owner the listing and assets word for word and get a clear yes; then the owner, or the agent with its own tools and the owner's yes, submits it in the vendor dashboard.  
  _Done when:_ The owner's approval and the submission time.
- **C-LTD-LISTING.05** Answer the marketplace's review questions and make requested changes; any change to the terms goes back to the owner first.  
  _Done when:_ Each review question with the answer or change, and the owner's yes for any change to terms.
- **C-LTD-LISTING.06** When the deal is live, open the public deal page and check that price, tiers, limits and redemption steps match what was approved. Pass the deal page URL as the first item in links.  
  _Done when:_ The live deal page URL and the check against the approved terms.

**Hand back:** `listing_url`, `published_text`, `approved_terms_check`, `assets`

**If stuck:**
- `not_live_yet`: If the listing is still in review, submit the step as blocked with the expected live date.
- `terms_changed_by_marketplace`: If the marketplace asks for different terms, take them to the owner; change nothing without their yes.
- `claim_not_supported`: If a claim cannot be backed by the product facts, remove it.
- `redemption_fails`: If a code cannot be redeemed, stop promoting the deal and fix it with the owner first.

### 12. Answer deal buyers fast and tell the owner's list about the launch

During the window answer every question and review on the deal page from the fact sheet, help buyers redeem, and tell people who already opted in to hear from the brand, because on deal marketplaces quick, honest answers and early real reviews decide how many buy.

- **C-LTD-SUPPORT.01** Check the deal page's questions and reviews at least twice a day during the window. Answer each from the fact sheet in plain words from the brand's vendor account; roadmap, custom work and refunds go to the owner first.  
  _Done when:_ Each question with the answer posted and its time.
- **C-LTD-SUPPORT.02** Help each buyer who cannot redeem within the support plan's response time; record the problem and the fix.  
  _Done when:_ Redemption problems with the time each took to fix.
- **C-LTD-SUPPORT.03** Ask buyers who have used it for a few days for an honest review on the deal page. Never offer anything for a good review, never write reviews yourself and never ask the team to.  
  _Done when:_ Review requests sent (to whom, when) and reviews posted.
- **C-LTD-SUPPORT.04** If the owner has an opted-in list (email, LINE, a community), write one short launch note with the deal link, get the owner's yes on the exact text, and send it once within that list's normal limits.  
  _Done when:_ The approved note, where it was sent and to how many people.
- **C-LTD-SUPPORT.05** Keep a list of every complaint and refund reason. When the same problem appears three times, tell the owner the same day with a proposed fix.  
  _Done when:_ The complaint list with counts per reason and what was reported to the owner.

**Hand back:** `answers_posted`, `redemption_issues`, `review_requests`, `launch_note`, `complaints`

**If stuck:**
- `question_needs_owner`: If a question is about the roadmap, custom work or a refund, answer only after the owner decides.
- `review_incentive_asked`: Never offer a reward for reviews, even if a buyer asks for one.
- `refund_spike`: If refunds rise above the usual rate, tell the owner the same day with the reasons.
- `list_not_opted_in`: If nobody on a list agreed to hear from the brand, do not send them the launch note.

### 13. Read this goal's B2B numbers: trials, meetings, deals and paid customers (result numbers)

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
