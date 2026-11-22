# LinkedIn Ads: lower the cost per qualified lead

- **Goal id:** `G-LA-QUALIFIED-CPL`
- **Channel:** linkedin_ads
- **Metric:** `qualified_lead_cpl` = `spend_minor` / `qualified_leads`, should decrease
- **Observation window:** 168 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), creative (the next round starts with `S12`), data (the next round starts with `C-LA-METRICS`)

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

### 8. Confirm the LinkedIn ad account, Page, and spending limits

Settle which LinkedIn ad account and Company Page this goal uses, who works in Campaign Manager, and the owner's written spending limits, so ads can be drafted, run and measured without stopping halfway.

- **C-LINKEDIN_ADS-ACCESS.01** Ask the owner for the URL of the LinkedIn Company Page the ads will run under and the ad account they want to use. Open the Page URL as a public page and confirm it is the owner's brand. If an ad account already exists, use it; do not create a second one.  
  _Done when:_ The Company Page URL, the ad account name and ID as Campaign Manager shows them, and the owner's confirmation that both are theirs.
- **C-LINKEDIN_ADS-ACCESS.02** Decide who works in Campaign Manager: the owner, or the agent in a browser where the owner is already signed in, if the owner allows it. If nobody is signed in, the owner signs in themselves on LinkedIn's own sign-in screen and handles any code or identity check. Never ask for a password. If the owner already reaches the ad account through a tool that uses LinkedIn's advertising API, use only the access it already has; if that access is still waiting for LinkedIn's review, wait and work in Campaign Manager instead.  
  _Done when:_ Who will operate the ad account, and how sign-in was done.
- **C-LINKEDIN_ADS-ACCESS.03** Check the role the operator has on the ad account (it must allow creating and editing campaigns, for example Account manager or Campaign manager) and that the operator is allowed to run ads under the Company Page. If either is missing, the owner adds it from a Page or ad account admin login.  
  _Done when:_ The operator's role on the ad account, and whether ads can run under the Company Page.
- **C-LINKEDIN_ADS-ACCESS.04** Read the ad account's currency, time zone, and whether a payment method is already set up. Ask the owner to write down the daily budget and the total budget for this round in that currency. The agent never enters card details; if billing is missing, the owner adds it.  
  _Done when:_ Currency, time zone, billing status, and the owner's written daily and total limits.
- **C-LINKEDIN_ADS-ACCESS.05** List the conversions already set up in the ad account, what each one counts, and its attribution window, and whether the product site already has LinkedIn's Insight Tag. Do not add a tag or a new conversion here; if one is needed, write down exactly what and ask the owner.  
  _Done when:_ Each existing conversion with what it counts and its window, or a note that none exist.
- **C-LINKEDIN_ADS-ACCESS.06** If the round will use a Lead Gen Form, confirm the form will belong to this ad account, that the owner has a privacy policy URL for it, and who can download the leads. A filled form only allows a reply about that request, not adding the person to every mailing.  
  _Done when:_ The privacy policy URL opened and confirmed, who can download leads, or a note that the round sends people to the product site instead.
- **C-LINKEDIN_ADS-ACCESS.07** Write down the round's limits: the one campaign group and campaign this round may create or change, and that nothing else in the account will be switched on, paused or edited. Leave audience expansion and any automatic budget increase off unless the owner asks for them.  
  _Done when:_ The list of what this round may touch, with the owner's okay in writing.

**Hand back:** `ad_account_id`, `company_page_url`, `who_operates`, `budget_limits`, `conversion_sources`

**If stuck:**
- `page_role_missing`: If the operator cannot run ads for the Company Page, ask the owner to add the role from a Page admin login, and keep working on the copy meanwhile.
- `owner_action_needed`: If LinkedIn asks for a verification code, terms, or an identity check, stop and tell the owner which screen needs them; never enter codes or accept terms for them.
- `no_billing`: If the ad account has no payment method, ask the owner to add one themselves; never type card details.
- `no_written_budget`: If the owner has not written down both a daily and a total budget, do not prepare any campaign and ask for both numbers in the account's currency.
- `lead_download_not_allowed`: If nobody can download the form's leads, say so and plan to send people to the product site with the round's tracked link; never guess email addresses.
- `conversion_unknown`: If no conversion is set up, mark it unknown and rely on the round's tracked link and sale counter; add nothing to the site without the owner's yes.

### 9. Write the post from proven facts

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

### 10. Make the marketing images from real product visuals

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

### 11. Read this goal's numbers from LinkedIn Ads (baseline numbers)

Record the numbers this goal is judged on, from the ad account's reporting and the owner's own lead or sales records, for a fixed date range, so the baseline and the current round are compared on real numbers.

- **C-LA-METRICS.01** Confirm the ad account ID, the campaigns being measured, the date range, the time zone, and the currency. For the baseline, use the account's earlier campaigns with the same objective over a range of the same length. For the current reading, start when this round's ads went live and cover at least the goal's 168 hours.  
  _Done when:_ Ad account ID, campaign names and IDs, date range with time zone, and currency.
- **C-LA-METRICS.02** Find this goal's metric components and use those exact names with record_numbers: spend_minor and attributed_conversions for cost per conversion, spend_minor and qualified_leads for cost per qualified lead, link_clicks and impressions for link click rate.  
  _Done when:_ The list of component names this goal needs, copied exactly.
- **C-LA-METRICS.03** In the ad account's reporting, filter to only the measured campaigns and the date range, then read spend, impressions, and landing page clicks. Write spend in the currency's smallest unit: USD 123.45 is 12345; for a currency without cents, such as JPY, 1 yen is 1.  
  _Done when:_ Each figure as shown, with the filter used and the time it was read.
- **C-LA-METRICS.04** For attributed_conversions, read the chosen conversion and note its attribution window. Check it against the sale counter and the owner's payment records; never count the owner's or the agent's test purchases, and leave out refunded orders. If the window is still open, mark the number as early.  
  _Done when:_ The conversion count, its window, and how it matches the sales records.
- **C-LA-METRICS.05** For qualified_leads, take the leads from the form download or the site form and count only those that meet the rule written before the round, such as job role, company size, or stated need. Count each person once. A lead is not a sale, and no lead is ever invented.  
  _Done when:_ The qualified count, the rule used, and how many leads were left out and why.
- **C-LA-METRICS.06** For link_clicks, use landing page clicks from the reporting or the round's tracked link count, and name which one. Use the same source for the baseline and the current reading.  
  _Done when:_ The click count and its source, the same as in the other reading.
- **C-LA-METRICS.07** Write down refunds and the round's other costs if known, such as tools or the owner's hours, or 'unknown'. The return the ad account reports is not the owner's net income. Use the same definitions and sources for the baseline and the current reading, and never borrow a number from another goal.  
  _Done when:_ Refunds and other costs, or 'unknown', and a note that both readings use the same definitions.
- **C-LA-METRICS.08** Call record_numbers with each component by its exact name and a source naming the screen, export, or file and the read time. If there is no history, record 0 and say so in source. Never estimate a missing number, and change nothing in the ads while reading.  
  _Done when:_ The recorded numbers, each with its source, and any number left out with the reason.

**If stuck:**
- `cannot_open_reporting`: If you cannot open the ad account's reporting, ask the owner for an export or a screenshot filtered to the measured campaigns and date range.
- `no_history`: If the account has no earlier campaigns for this metric, record 0, say in source that there is no history, and let this round set the baseline.
- `conversion_unknown`: If no conversion is set up, use the sale counter and payment records only, and say in source that the ad account has no conversion.
- `lead_download_not_allowed`: If the leads cannot be downloaded, ask the owner to export them; never count qualified leads you cannot see.
- `too_early_to_read`: If the ads have run less than 168 hours or conversions may still arrive, record the numbers as early and read them again later.
- `numbers_from_wrong_account`: If an export or screenshot shows a different ad account or campaigns from the agreed ones, do not use it and ask again.

### 12. Build this round's LinkedIn ads as drafts, not running

Set up this round's campaign and ads in Campaign Manager without switching them on, so the owner can check every word, the audience, and the budget before any money is spent.

- **C-LA-DRAFT.01** Re-check the ad account ID, the Company Page, the operator's role, and the owner's written daily and total budget. If any of these is missing, stop here.  
  _Done when:_ The four items, confirmed on the day of drafting.
- **C-LA-DRAFT.02** Pick the objective that fits the goal's main number: website visits or conversions when people should reach the product page, lead generation when the goal counts leads. Read the audience options the ad account shows today; do not copy audience settings or typical costs from old guides.  
  _Done when:_ The objective chosen and why, and the audience options available today.
- **C-LA-DRAFT.03** Build the audience from the chosen buyer group: one job situation, such as a job function plus seniority and company size. Note the audience size estimate shown. If it is too small to run, adjust within the same buyer group; never widen to people who do not fit.  
  _Done when:_ The audience settings and the size estimate shown.
- **C-LA-DRAFT.04** Prepare each ad from the approved copy and image. The destination is the round's tracked link, with ?v=A, ?v=B for each version, and only one thing differs between versions. For a Lead Gen Form, keep it to at most four fields, add one question that tests the qualification rule, and add the privacy policy URL. Check every claim against the product facts; no invented numbers, testimonials, scarcity, or guarantees.  
  _Done when:_ Each ad's text, image, and link or form, with what differs between versions.
- **C-LA-DRAFT.05** Show the owner, word for word: each ad's text, headline, image, destination link or form questions, the audience, the objective, the daily and total budget, and the start and end dates. Get a clear yes before saving.  
  _Done when:_ The full draft as shown, and the owner's approval message.
- **C-LA-DRAFT.06** The operator agreed in the account step creates only this round's campaign and ads, saved as draft or paused. Set a daily budget and a total budget at or below the owner's limits, and an end date. Do not edit any other campaign. If saving seemed to fail, check the campaign list before trying again so nothing is created twice.  
  _Done when:_ One campaign and its ads in draft or paused status, and their IDs.
- **C-LA-DRAFT.07** Open the campaign again and check that the status, audience, budget, end date, and each ad's link or form match the approved draft. Report no leads or clicks yet; nothing has run.  
  _Done when:_ Campaign and ad IDs, their status, and a line-by-line match with the approved draft.

**Hand back:** `campaign_id`, `ad_ids`, `draft_status`, `budget_set`, `owner_approval`

**If stuck:**
- `no_written_budget`: If the owner has not written a daily and a total budget, do not create anything and ask for both numbers.
- `owner_has_not_approved`: If the owner has not said yes to this exact draft, do not save it in the ad account; show it and wait.
- `audience_too_small`: If the audience is too small to run, adjust it within the same buyer group or tell the owner; never widen to people who do not fit.
- `page_role_missing`: If the ads cannot run under the Company Page, ask the owner to fix the role, and keep the draft text ready.
- `link_does_not_open`: If the tracked link does not open the product page, fix it before saving the draft.
- `lead_download_not_allowed`: If leads from the form cannot be downloaded, switch to the product page with the tracked link and tell the owner.

### 13. Switch on only this round's LinkedIn ads

Start delivery of the approved draft ads, and nothing else, within the owner's written budget, so the round collects real numbers for the goal.

- **C-LA-ACTIVATE.01** Open the campaign and ads by the IDs from the draft step. Confirm the text, image, audience, link or form, and budget are the same as approved. If anything changed, show the owner again before going on.  
  _Done when:_ Campaign and ad IDs, and a check that each matches the approved draft.
- **C-LA-ACTIVATE.02** Get the owner's written yes to switch on, naming the daily budget, the total budget, and the end date in the account's currency. With no budget, a zero budget, or no yes, nothing is switched on.  
  _Done when:_ The owner's message approving the switch-on with the amounts and end date.
- **C-LA-ACTIVATE.03** Open the tracked link of each ad and confirm it reaches the product page, or preview the Lead Gen Form and confirm its questions and privacy link.  
  _Done when:_ Each link or form checked, with the page or form it showed.
- **C-LA-ACTIVATE.04** Switch on only this round's campaign and ads, by the operator agreed earlier. Do not switch on any other draft, raise the budget, or turn on audience expansion.  
  _Done when:_ Who switched on what, and when.
- **C-LA-ACTIVATE.05** Open the campaign again and read each ad's status and review state. If an ad is in review, wait; do not edit it to get around review. If an ad is rejected, read the reason and bring a fix to the owner.  
  _Done when:_ Status and review state of each ad, with the time read.
- **C-LA-ACTIVATE.06** Write down the start time and the planned stop: after the goal's 168 hours or when the total budget is spent, whichever comes first. Set the campaign's end date to match if the owner agreed.  
  _Done when:_ Start time, planned stop time, and whether an end date is set in the campaign.

**Hand back:** `campaign_id`, `ad_ids`, `live_status`, `started_at`, `planned_stop`

**If stuck:**
- `owner_has_not_approved`: If the owner has not approved switching on with a budget and end date, do not switch anything on; ask and wait.
- `ads_differ_from_draft`: If the ads no longer match the approved draft, show the owner the difference and get a new yes.
- `ad_in_review`: If an ad is still in review, wait and check again later; do not edit it to get around review.
- `ad_rejected`: If an ad is rejected, read the reason, draft a fix that keeps to the facts, and show the owner before resubmitting.
- `payment_failed`: If the ad account shows a billing problem, ask the owner to fix it themselves; never enter card details.

### 14. Read this goal's numbers from LinkedIn Ads (result numbers)

Record the numbers this goal is judged on, from the ad account's reporting and the owner's own lead or sales records, for a fixed date range, so the baseline and the current round are compared on real numbers.

- **C-LA-METRICS.01** Confirm the ad account ID, the campaigns being measured, the date range, the time zone, and the currency. For the baseline, use the account's earlier campaigns with the same objective over a range of the same length. For the current reading, start when this round's ads went live and cover at least the goal's 168 hours.  
  _Done when:_ Ad account ID, campaign names and IDs, date range with time zone, and currency.
- **C-LA-METRICS.02** Find this goal's metric components and use those exact names with record_numbers: spend_minor and attributed_conversions for cost per conversion, spend_minor and qualified_leads for cost per qualified lead, link_clicks and impressions for link click rate.  
  _Done when:_ The list of component names this goal needs, copied exactly.
- **C-LA-METRICS.03** In the ad account's reporting, filter to only the measured campaigns and the date range, then read spend, impressions, and landing page clicks. Write spend in the currency's smallest unit: USD 123.45 is 12345; for a currency without cents, such as JPY, 1 yen is 1.  
  _Done when:_ Each figure as shown, with the filter used and the time it was read.
- **C-LA-METRICS.04** For attributed_conversions, read the chosen conversion and note its attribution window. Check it against the sale counter and the owner's payment records; never count the owner's or the agent's test purchases, and leave out refunded orders. If the window is still open, mark the number as early.  
  _Done when:_ The conversion count, its window, and how it matches the sales records.
- **C-LA-METRICS.05** For qualified_leads, take the leads from the form download or the site form and count only those that meet the rule written before the round, such as job role, company size, or stated need. Count each person once. A lead is not a sale, and no lead is ever invented.  
  _Done when:_ The qualified count, the rule used, and how many leads were left out and why.
- **C-LA-METRICS.06** For link_clicks, use landing page clicks from the reporting or the round's tracked link count, and name which one. Use the same source for the baseline and the current reading.  
  _Done when:_ The click count and its source, the same as in the other reading.
- **C-LA-METRICS.07** Write down refunds and the round's other costs if known, such as tools or the owner's hours, or 'unknown'. The return the ad account reports is not the owner's net income. Use the same definitions and sources for the baseline and the current reading, and never borrow a number from another goal.  
  _Done when:_ Refunds and other costs, or 'unknown', and a note that both readings use the same definitions.
- **C-LA-METRICS.08** Call record_numbers with each component by its exact name and a source naming the screen, export, or file and the read time. If there is no history, record 0 and say so in source. Never estimate a missing number, and change nothing in the ads while reading.  
  _Done when:_ The recorded numbers, each with its source, and any number left out with the reason.

**If stuck:**
- `cannot_open_reporting`: If you cannot open the ad account's reporting, ask the owner for an export or a screenshot filtered to the measured campaigns and date range.
- `no_history`: If the account has no earlier campaigns for this metric, record 0, say in source that there is no history, and let this round set the baseline.
- `conversion_unknown`: If no conversion is set up, use the sale counter and payment records only, and say in source that the ad account has no conversion.
- `lead_download_not_allowed`: If the leads cannot be downloaded, ask the owner to export them; never count qualified leads you cannot see.
- `too_early_to_read`: If the ads have run less than 168 hours or conversions may still arrive, record the numbers as early and read them again later.
- `numbers_from_wrong_account`: If an export or screenshot shows a different ad account or campaigns from the agreed ones, do not use it and ask again.

### 15. Pause only this round's LinkedIn ads after the test

Stop spending on this round's ads once the observation time is over, without touching anything else in the account, so the result is fixed and the next round starts clean.

- **C-LA-STOP.01** List the campaign and ad IDs that this round switched on, taken from the switch-on step. Use only these; never take the whole account's campaign list.  
  _Done when:_ The IDs this round switched on.
- **C-LA-STOP.02** Confirm the round is over: at least 168 hours since start, or the total budget is spent. Confirm this round's numbers have been read and recorded; if not, read them first.  
  _Done when:_ Start time, time now or budget reached, and a note that the numbers were recorded.
- **C-LA-STOP.03** Tell the owner which campaign and ads will be paused, then pause only those. Do not delete or archive them, and do not change text, images, audience, or budget, so the round stays on record. Do not touch other campaigns or other brands.  
  _Done when:_ The IDs paused, who paused them, and when.
- **C-LA-STOP.04** Open each campaign and ad again and confirm the status shows paused and nothing is still delivering. If the pause seemed to fail, check the status before trying again, and do not call it stopped until the screen shows it.  
  _Done when:_ Status of each ID as shown after pausing, with the time read.
- **C-LA-STOP.05** Read the round's final spend from the ad account's reporting, in the currency's smallest unit, and compare it with the owner's total limit. If it went over, tell the owner the exact amount.  
  _Done when:_ Final spend in the smallest unit, and whether it stayed within the owner's limit.
- **C-LA-STOP.06** Write the one change the next round will test, such as a different job function or one different form question, with the same budget and qualification rule. Pausing does not give permission for a bigger budget.  
  _Done when:_ The single change planned for the next round.

**Hand back:** `paused_ids`, `status_shown`, `final_spend_minor`, `next_change`

**If stuck:**
- `ids_unknown`: If you do not know which IDs this round switched on, ask the owner or check the switch-on step; never pause by guessing.
- `numbers_not_recorded`: If this round's numbers are not recorded yet, read and record them first, then pause.
- `pause_not_confirmed`: If the status does not show paused, check again after a few minutes and ask the owner to pause it by hand if it still runs.
- `over_budget`: If spend went over the owner's total limit, pause at once and tell the owner the exact amount.
- `owner_wants_to_continue`: If the owner wants to keep the ads running, get a new written daily budget, total budget, and end date instead of pausing.
