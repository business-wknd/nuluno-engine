# Product Hunt: raise the share of makers with a sourced public email

- **Goal id:** `G-PH-PUBLIC-EMAILS`
- **Channel:** producthunt
- **Metric:** `public_email_coverage` = `verified_public_emails` / `reviewed_makers`, should increase
- **Observation window:** 168 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `C-PH-MAKERS`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), message (the next round starts with `A-ANGLES`), data (the next round starts with `C-PH-METRICS`)

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

### 9. Find Product Hunt makers who fit the product

Build a short, sourced list of real makers whose recent products and public words show a need the product meets, because only checked, well-fitting makers count toward the goal's main number and give later steps someone worth reaching.

- **C-PH-MAKERS.01** From the buyer groups and the strongest motive chosen earlier, write who a fitting maker is in two or three lines: the kind of product they launched, how recently (for example, in the last 90 days), and the situation that would make them need this product. Add a one-line guess to test, such as 'makers of B2B tools launched in the last 90 days need X because Y'. Also write who to leave out: competitors, the owner's own products, and people who say they do not want contact.  
  _Done when:_ The fit definition, the one-line guess, and the leave-out rules.
- **C-PH-MAKERS.02** Pick three to five searches: the product category, two or three known alternatives, and the job the buyer is trying to get done. Open Product Hunt search and topic pages for each with read_page or your browser, one page at a time.  
  _Done when:_ Each search or topic page URL you opened, and the date.
- **C-PH-MAKERS.03** From those pages, open each product that matches the fit definition and launched within the chosen time. Record the product page URL, the launch date, the product website, and the people listed as makers. The hunter who posted a product is not its owner unless they are also listed as a maker.  
  _Done when:_ One row per product with its page URL, launch date, website and maker names.
- **C-PH-MAKERS.04** For each maker, open their Product Hunt profile and the product website. Confirm they built or run the product and that the site is still live. Keep one row per company: if several makers run the same company, put them in one row and mark the one whose role fits best as the contact. Review at least 20 rows and stop at 50 per round, so each one gets a real check.  
  _Done when:_ A list of distinct rows reviewed, one per company, each with the makers' profile URLs, roles, company and a note that the site loads.
- **C-PH-MAKERS.05** For each maker, look for a public sign of need that the product meets: a line in their launch comments, a public post asking for help, a job post, or a roadmap item. Copy the exact words with the URL and date. A recent launch on its own is not a need and not a sign they will pay.  
  _Done when:_ For each maker, either a quoted need with URL and date, or 'no need found'.
- **C-PH-MAKERS.06** Keep what you saw separate from what you infer. Write the observed need in one field and your reason for fit in another. Mark a maker 'qualified' only when the fit rests on a quoted need or a clear, sourced fact about their situation.  
  _Done when:_ Each maker has an observed-need field and a separate fit-reason field.
- **C-PH-MAKERS.07** Sort every reviewed row into qualified, unknown or excluded, with one line of reason each. Do not contact anyone and do not guess any email address in this step.  
  _Done when:_ Three groups whose counts add up to the number of rows reviewed, each row with a reason.

**Hand back:** `fit_definition`, `searches_used`, `maker_list`, `excluded_makers`

**If stuck:**
- `no_fit_definition`: If no buyer group or motive was chosen earlier, go back to those steps before searching.
- `too_few_matches`: If the searches turn up fewer than 20 rows, widen the launch time or add two more searches, and say which change you made.
- `pages_blocked`: If Product Hunt pages will not open for you, ask the owner to open them and share what they show; do not use a scraping service.
- `no_api_permission`: If reading by API would need commercial permission the owner does not have, keep reading public pages one at a time.
- `maker_is_not_a_buyer`: If a maker shows no sign of need, mark them unknown or excluded; never mark them qualified only because they launched recently.

### 10. Find makers' public business emails from their own sites

For each qualified maker, find a business email the maker has published on their own website and record where it was found, because only sourced, public addresses count and only they can be contacted fairly later.

- **C-PH-EMAIL.01** Take the qualified rows from the latest maker list. For each, start at the Product Hunt product page, open the contact maker's profile, and follow the links they list to the product website or their personal site. Write down every URL in that path.  
  _Done when:_ For each row, the product page URL, profile URL and website URL.
- **C-PH-EMAIL.02** Confirm the website belongs to this maker or their product: the domain matches the link on the product page, or the maker is named on the site's about or team page.  
  _Done when:_ For each website, the page and line that ties it to the maker.
- **C-PH-EMAIL.03** Read the site's contact, about, press and legal notice pages and the page footer. Record any email address printed there, the URL of the page it is on, and what the page says it is for, such as partnerships, press or support.  
  _Done when:_ Each email found, with its page URL and stated purpose, and the date you read it.
- **C-PH-EMAIL.04** If no address is printed, record 'none found' and the pages you checked. Never build an address from a name or username, never use email-guessing, lookup or scraping services, and never treat the email used to sign in to Product Hunt, or a field Product Hunt does not show, as known. A contact form may be recorded as a form URL, not as an email.  
  _Done when:_ Makers with no email marked 'none found', with the pages checked.
- **C-PH-EMAIL.05** Mark each address by type: the maker personally, the company's general inbox, customer support, or press and partnerships. Count an address as a verified public business email only if it is on the maker's own site and is not a customer-support-only address.  
  _Done when:_ Each address with its type and a yes or no for counting as verified.
- **C-PH-EMAIL.06** Check the page for signs the maker does not want pitches, such as 'no solicitations'. Note them and exclude that address. A public address is not consent to marketing: do not add anyone to a mailing list. Any later message is one personal email, approved by the owner word for word, that says who is writing, how they relate to the product and why, includes a way to opt out, and follows anti-spam law.  
  _Done when:_ For each address, a note of any no-contact sign and 'not added to any list'.
- **C-PH-EMAIL.07** Hand back one row for each qualified row you checked: verified email with source, none found, or excluded with reason. Do not send anything in this step.  
  _Done when:_ A list whose rows match the qualified rows checked, each with a result and a source.

**Hand back:** `contacts_found`, `none_found`, `excluded_contacts`

**If stuck:**
- `no_qualified_makers`: If there is no list of qualified makers for this round, go back to the maker search step first.
- `no_website_listed`: If a maker lists no website and the product page links nowhere, mark them 'none found' and move on; do not search for private addresses.
- `email_not_published`: If the site shows only a contact form, record the form URL and mark the email as 'none found'; never guess an address.
- `site_not_theirs`: If you cannot tie the website to the maker, do not use any address from it and mark the row unknown.
- `no_contact_requested`: If the site asks not to be contacted for sales, exclude that maker and note the page.

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

### 12. Read this goal's numbers for Product Hunt (result numbers)

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
