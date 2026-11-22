# Product Hunt: raise tracked site visits from a launch

- **Goal id:** `G-PH-LAUNCH-TRAFFIC`
- **Language:** English
- **Channel:** producthunt
- **Metric:** `attributed_sessions` = `attributed_sessions`, should increase
- **Observation window:** 168 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), message (the next round starts with `A-COPY`), data (the next round starts with `C-PH-METRICS`)

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

### 8. Confirm the Product Hunt account and who acts on it

Settle which real Product Hunt maker account the owner uses, whether the product already has a page, and who presses publish, so research, the launch and replies all run under the right account without stopping halfway.

- **C-PRODUCTHUNT-ACCESS.01** Ask the owner for the URL of their own Product Hunt profile and the product's website. Open the profile with read_page or your browser and confirm it exists, shows a real name, and is the owner's. Product Hunt accounts are for real people: use the owner's one personal account, and never create extra or brand-only accounts to act on Product Hunt.  
  _Done when:_ The profile URL, the name and handle shown on it, and the owner's confirmation that it is theirs.
- **C-PRODUCTHUNT-ACCESS.02** Search Product Hunt for the product's name and its website domain. If a page for this product already exists, open it and check whether the owner is listed as a maker. Plan to use that page; do not plan a second page for the same product.  
  _Done when:_ The URL of any existing product page with its listed makers, or a note that a search on the name and the domain found none.
- **C-PRODUCTHUNT-ACCESS.03** Decide who will press publish on Product Hunt: the owner on their own device, or your browser if it is already signed in to the owner's account and the owner agrees. If nobody is signed in, the owner signs in themselves on the official Product Hunt sign-in screen. Never ask for a password. If this goal only researches makers and posts nothing, write 'nobody, research only' and skip sign-in.  
  _Done when:_ Who will publish, how the owner signed in, and the handle shown after sign-in, or a note that this goal posts nothing.
- **C-PRODUCTHUNT-ACCESS.04** Create a new Product Hunt account only if the owner has none, this goal includes a launch or replies, and the owner asks for one in this conversation. The account must be in the owner's real name. If the owner agrees to sign up with the address from inbox_address, read the verification code with inbox_latest; otherwise the owner reads the code from their own email. Any terms screen or identity check is done by the owner.  
  _Done when:_ The new profile URL and the owner's request, or a note that the existing account is used.
- **C-PRODUCTHUNT-ACCESS.05** Read Product Hunt's current help pages on launching and community rules, and write down in three to six short lines what is not allowed. In every case: never buy votes, never trade votes, never use extra accounts, and never ask people to upvote; ask for feedback instead.  
  _Done when:_ A short list of the current rules with the help page URLs they came from.
- **C-PRODUCTHUNT-ACCESS.06** Settle how you will read Product Hunt data. Read public pages one at a time with read_page or your browser; do not bulk-download pages or use scraping tools. Do not use the Product Hunt API as a free lead list; its terms ask for permission before commercial use, so use it only if the owner already has that permission in writing. Profiles do not reliably show an email address, so any business email must later come from the maker's own public website, never from a guess built on a username.  
  _Done when:_ A one-line note on how data will be read, whether the owner has written API permission, and that emails will only come from makers' own websites.
- **C-PRODUCTHUNT-ACCESS.07** If this goal includes a launch or replies, confirm with the agreed account signed in that whoever publishes can open the screen for submitting a product and can post a comment. Do not submit or post anything in this step. If the goal only researches makers, write 'not needed'.  
  _Done when:_ Confirmation that the submit screen and the comment box open for the agreed account, with the time checked, or 'not needed'.

**Hand back:** `account_handle`, `profile_url`, `existing_product_page`, `who_publishes`

**If stuck:**
- `no_product_hunt_account`: If the owner has no Product Hunt account and this goal only researches makers, carry on without one; if it includes a launch or replies, ask whether they want one in their real name and create it only on a clear yes.
- `wrong_account_signed_in`: If the signed-in account is not the owner's agreed profile, stop and ask the owner to switch accounts or to act on their own device.
- `page_owned_by_someone_else`: If the product already has a page that lists other people as makers, do not create a new one; ask the owner to request maker access for that page through Product Hunt's help pages.
- `owner_action_needed`: If a verification screen, terms screen or identity check appears, stop and tell the owner which screen and which button; never accept terms for them.
- `no_api_permission`: If the owner has no written API permission, read public pages one at a time instead and say so in the hand-back.
- `agent_browser_not_signed_in`: If your browser is not signed in to the owner's account, set who_publishes to 'owner' and plan to hand them exact text to paste.

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

### 11. Read this goal's numbers for Product Hunt (baseline numbers)

Record the numbers this goal is judged on, for a fixed window before and after the round, from sources you can name, so rounds are compared on real counts and not on guesses. record_numbers lists exactly which numbers it needs.

- **C-PH-METRICS.01** Read the goal's metric components from where_are_we. Set the window: seven days, in the owner's time zone. For a baseline, use the seven days before the round starts; for current, the seven days after it starts. If a launch is involved, note that Product Hunt's launch day runs on Pacific Time and write both times.  
  _Done when:_ The component names, the start and end of the window with time zone, and whether this is the baseline or the current reading.
- **C-PH-METRICS.02** If the goal counts makers, read the maker list for the window: for the baseline, the last round's list; for current, this round's list. Count each row once (one per company). reviewed_makers is the rows whose profile and product site were actually opened and checked. qualified_makers is the rows marked qualified with a quoted need or sourced fit reason. verified_public_emails is the rows with an address the email step counted as verified, printed on the maker's own site, with the page URL. Never count unknown or excluded rows as qualified.  
  _Done when:_ Each maker count with the list it came from and the date that list was made, or 'no history' if there was no earlier list.
- **C-PH-METRICS.03** If the goal counts site visits, take the click count of this round's tracked link from tracking for the window. If the listing does not use the tracked link, or for a baseline before any tracked link existed, use visits referred by producthunt.com in the owner's site analytics and name it. Use the same source for baseline and current, and use one source only; never add two sources together.  
  _Done when:_ The visit count, the tool it came from, and the window it covers.
- **C-PH-METRICS.04** If the goal counts purchases, take the sale counter on the page shown after payment, or the owner's payment records for the window. Count only purchases from outside buyers that can be tied to this round. Leave out the owner's own test payments, refunded orders, and sales you cannot connect to this round, and say how many you left out.  
  _Done when:_ The purchase count, its source, and the number left out with the reason.
- **C-PH-METRICS.05** If a launch is live, also note the visible upvote and comment counts and the number of different people who asked a real question about the product. Do not count the owner, the hunter, other makers promoting their own products, or simple congratulations. These are context only, not the goal's number.  
  _Done when:_ The upvote and comment counts and the number of real questions, each with the launch page URL.
- **C-PH-METRICS.06** Call record_numbers with the goal's exact component names and a source for each. If there is no history for a component, record 0 and say in source that there is no history. Never estimate or fill a gap; if a component cannot be read, say which one and why.  
  _Done when:_ The record_numbers call with every component name, value and source.

**If stuck:**
- `no_history`: If there is no history for a component, record 0 and say in source that there is no history; the first round then sets the baseline.
- `no_purchase_source`: If there is no sale counter and the owner has no payment records to share, ask the owner for the sales in the window from their payment tool; if none exists, say so and do not estimate.
- `tracked_link_not_used`: If the live listing or replies do not use this round's tracked link, use the owner's site analytics for visits from producthunt.com and say so; if neither exists, record what you can and name the gap.
- `launch_not_live`: If the listing is still a draft, scheduled or pending, do not treat it as launched; record the current reading only once it is public.
- `too_early_to_read`: If the window has not closed, report the numbers as early and read them again when the seven days are over.
- `zero_denominator`: If the count a rate is divided by is 0, record the components as they are and do not report any rise or fall.

### 12. Prepare and publish the Product Hunt launch

Put one honest, approved Product Hunt listing live on a chosen launch day with the round's tracked link, because a clear listing that the owner backs in the comments is what sends visitors from Product Hunt to the product.

- **C-PH-LISTING.01** Search Product Hunt again for the product's name and website domain. If a page already exists and the owner is a listed maker, read Product Hunt's current rules on launching an existing product again and use that page. If it lists other makers, stop and ask the owner. Never create a second page for the same product.  
  _Done when:_ The existing page URL and its makers, or a note that none exists.
- **C-PH-LISTING.02** Open the screen for submitting a product, or Product Hunt's help pages, and write down each field and its current limit: name, tagline, description, topics, images, pricing type and links. Do not rely on old limits from memory.  
  _Done when:_ A list of the fields with the limits read today and where you read them.
- **C-PH-LISTING.03** Draft the listing from the product facts and the approved copy: a tagline with one specific benefit, a short description of what the product does today, one to three topics where these buyers browse, and a pricing type that matches the real price. Leave out features that are not live, invented numbers, testimonials, scarcity and guarantees.  
  _Done when:_ The draft text for each field, each within its limit, and a list of claims left out.
- **C-PH-LISTING.04** Choose the images: real screenshots, or images made earlier in this round if there are any. Confirm the owner has the right to use each one and that each shows the product as it is now.  
  _Done when:_ Each image file with what it shows and a note on who owns it.
- **C-PH-LISTING.05** Use the round's tracked link as the website link only if the form accepts it and the Product Hunt rules read earlier do not forbid redirect links; open it once to check it lands on the product. Otherwise use the plain product URL and tell the numbers step that visits will be read from producthunt.com referrals in the owner's site analytics. Draft the maker's first comment: who built it, why, what it does today, what it does not do yet, and a request for honest feedback, with the tracked link.  
  _Done when:_ The website link used, confirmation it opens the product, which source will count visits, and the first comment draft.
- **C-PH-LISTING.06** Agree a launch date with the owner. Product Hunt's launch day runs on Pacific Time; pick a day when the owner can answer comments for the full 24 hours. Keep draft, scheduled and live apart; a draft or a scheduled launch is not launched.  
  _Done when:_ The launch date and start time in Pacific Time and in the owner's time zone, and the owner's agreement.
- **C-PH-LISTING.07** Show the owner every field, the images, the website link and the first comment word for word, and get a clear yes. Any message the owner sends to friends or followers about the launch asks for feedback, not for upvotes. Never buy or trade votes and never use extra accounts.  
  _Done when:_ The full approved listing and the owner's yes message.
- **C-PH-LISTING.08** The agreed person submits or schedules the listing once: the owner, or your browser if it is signed in to their account and they said yes. If submitting seems to fail, check the owner's drafts and products before trying again so nothing is submitted twice. If it is pending review, wait; do not submit it again.  
  _Done when:_ Who submitted, when, and the state shown afterwards: scheduled, pending or live.
- **C-PH-LISTING.09** When it is live, open the public page and read back the name, tagline, description, makers and first comment. Click the website link and confirm it reaches the product. Hand back the public URL.  
  _Done when:_ The public listing URL, the text as it appears there, and confirmation the website link works.

**Hand back:** `listing_url`, `published_text`, `launch_date`, `website_link`

**If stuck:**
- `owner_has_not_approved`: If the owner has not said yes to the exact listing and first comment, do not submit; show them the text and stop until they answer.
- `duplicate_listing`: If the product already has a page, use it or ask the owner to request maker access; never create a second page.
- `fact_missing_for_claim`: If a field needs a fact you do not have, remove the claim or ask the owner; never fill it with a guess.
- `agent_cannot_publish`: If your browser is not signed in to the owner's account, give the owner the final fields, images and first comment to paste, and ask for the public URL.
- `pending_review`: If Product Hunt shows the listing as pending, wait and check again later; do not resubmit or treat it as launched.
- `owner_unavailable_on_launch_day`: If the owner cannot answer comments on the chosen day, pick another date with them before scheduling.

### 13. Read this goal's numbers for Product Hunt (result numbers)

Record the numbers this goal is judged on, for a fixed window before and after the round, from sources you can name, so rounds are compared on real counts and not on guesses. record_numbers lists exactly which numbers it needs.

- **C-PH-METRICS.01** Read the goal's metric components from where_are_we. Set the window: seven days, in the owner's time zone. For a baseline, use the seven days before the round starts; for current, the seven days after it starts. If a launch is involved, note that Product Hunt's launch day runs on Pacific Time and write both times.  
  _Done when:_ The component names, the start and end of the window with time zone, and whether this is the baseline or the current reading.
- **C-PH-METRICS.02** If the goal counts makers, read the maker list for the window: for the baseline, the last round's list; for current, this round's list. Count each row once (one per company). reviewed_makers is the rows whose profile and product site were actually opened and checked. qualified_makers is the rows marked qualified with a quoted need or sourced fit reason. verified_public_emails is the rows with an address the email step counted as verified, printed on the maker's own site, with the page URL. Never count unknown or excluded rows as qualified.  
  _Done when:_ Each maker count with the list it came from and the date that list was made, or 'no history' if there was no earlier list.
- **C-PH-METRICS.03** If the goal counts site visits, take the click count of this round's tracked link from tracking for the window. If the listing does not use the tracked link, or for a baseline before any tracked link existed, use visits referred by producthunt.com in the owner's site analytics and name it. Use the same source for baseline and current, and use one source only; never add two sources together.  
  _Done when:_ The visit count, the tool it came from, and the window it covers.
- **C-PH-METRICS.04** If the goal counts purchases, take the sale counter on the page shown after payment, or the owner's payment records for the window. Count only purchases from outside buyers that can be tied to this round. Leave out the owner's own test payments, refunded orders, and sales you cannot connect to this round, and say how many you left out.  
  _Done when:_ The purchase count, its source, and the number left out with the reason.
- **C-PH-METRICS.05** If a launch is live, also note the visible upvote and comment counts and the number of different people who asked a real question about the product. Do not count the owner, the hunter, other makers promoting their own products, or simple congratulations. These are context only, not the goal's number.  
  _Done when:_ The upvote and comment counts and the number of real questions, each with the launch page URL.
- **C-PH-METRICS.06** Call record_numbers with the goal's exact component names and a source for each. If there is no history for a component, record 0 and say in source that there is no history. Never estimate or fill a gap; if a component cannot be read, say which one and why.  
  _Done when:_ The record_numbers call with every component name, value and source.

**If stuck:**
- `no_history`: If there is no history for a component, record 0 and say in source that there is no history; the first round then sets the baseline.
- `no_purchase_source`: If there is no sale counter and the owner has no payment records to share, ask the owner for the sales in the window from their payment tool; if none exists, say so and do not estimate.
- `tracked_link_not_used`: If the live listing or replies do not use this round's tracked link, use the owner's site analytics for visits from producthunt.com and say so; if neither exists, record what you can and name the gap.
- `launch_not_live`: If the listing is still a draft, scheduled or pending, do not treat it as launched; record the current reading only once it is public.
- `too_early_to_read`: If the window has not closed, report the numbers as early and read them again when the seven days are over.
- `zero_denominator`: If the count a rate is divided by is 0, record the components as they are and do not report any rise or fall.
