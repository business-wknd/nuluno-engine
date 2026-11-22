# LinkedIn: raise the share of leads with a verified public email

- **Goal id:** `G-LI-PUBLIC-EMAILS`
- **Channel:** linkedin
- **Metric:** `public_email_coverage` = `verified_public_emails` / `reviewed_people`, should increase
- **Observation window:** 168 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `C-LI-ROLES`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), message (the next round starts with `A-ANGLES`), data (the next round starts with `C-LI-METRICS`)

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

### 8. Confirm the LinkedIn identity, sign-in, and who does what

Settle which LinkedIn profile or Company Page this goal works under, who signs in and publishes, and how research is done within LinkedIn's rules, so the round can run without fake accounts, blocked searches, or the owner being stopped halfway.

- **C-LINKEDIN-ACCESS.01** Ask the owner which LinkedIn identity this goal uses: their personal profile, the Company Page, or both. Get the public URL of each and open it with read_page to confirm it exists and matches the brand. Use the existing profile or Page; do not create a second one.  
  _Done when:_ The profile and Page URLs, the names shown on them, and the owner's confirmation that they are theirs.
- **C-LINKEDIN-ACCESS.02** If the goal posts as the Company Page, ask the owner to confirm they are an admin of that Page who can post and see its analytics. If they are not, research and drafting go on, and only posting as the Page waits until an existing admin adds them.  
  _Done when:_ The owner's role on the Page as they stated it or as shown in their screenshot, or a note that the role is missing.
- **C-LINKEDIN-ACCESS.03** The owner signs in to LinkedIn themselves, on the official LinkedIn sign-in screen or their company's single sign-on, and completes any verification code, identity check, or terms screen. Never ask for a password, never copy browser cookies, and never install extensions or tools that pull data from LinkedIn.  
  _Done when:_ A note of which account the owner is signed in as, and the time it was checked.
- **C-LINKEDIN-ACCESS.04** Agree who does each kind of work. LinkedIn forbids scraping and bots on its site, so the signed-in work inside LinkedIn is done by the owner by hand: searching, posting, sending messages, and opening analytics. The agent drafts, reads single public pages with read_page, checks company websites, and works from the owner's screenshots, pasted URLs, or LinkedIn's own data export. The agent posts or sends only through an official LinkedIn tool the owner has already set up.  
  _Done when:_ A short plan naming 'owner' or 'agent' for searching, publishing, messaging, and reading numbers, with the route for each.
- **C-LINKEDIN-ACCESS.05** Test the plan once. If the goal needs people research, ask the owner to run one sample search on LinkedIn, such as a job title plus an industry, and send a screenshot of the results. Then use read_page on one public company page or profile URL to see what loads without sign-in.  
  _Done when:_ The sample search terms, what the screenshot and the public page showed, and the exact text of any limit message.
- **C-LINKEDIN-ACCESS.06** If a sign-in wall or search limit appears, do not switch to another account, create a new one, or try any workaround. Keep the owner's searches few and specific, wait for the limit to clear, or move the research to public company websites and team pages.  
  _Done when:_ The chosen route for research, with the reason, or a note that no limit appeared.
- **C-LINKEDIN-ACCESS.07** Write down the record rules for the rest of the round: every search keeps its exact terms, date, and URL; an email is recorded only if the person or their company published it, with the source URL, otherwise it stays empty; a job title is a hint, not proof of buying power; a public email is not permission to send marketing, so source, consent, and opt-outs are kept in separate columns of this round's list, or in that tool if the owner already uses a CRM.  
  _Done when:_ The rules as written, ready for the research and outreach steps.

**Hand back:** `linkedin_identity`, `page_admin_role`, `who_does_what`, `research_access`, `record_rules`

**If stuck:**
- `owner_action_needed`: If a verification code, identity check, or terms screen appears, stop and tell the owner which screen needs them; never enter codes or accept terms for them.
- `page_role_missing`: If the owner is not an admin of the Company Page, continue research and drafts, and ask the owner to have an existing admin add them before anything is posted as the Page.
- `wrong_account_signed_in`: If the signed-in account is not the agreed profile, stop and ask the owner to switch accounts or to do the work on their own device.
- `automation_prohibited`: If a route would need scraping, bulk extraction, a browser extension, or the agent clicking through LinkedIn while signed in, do not use it; ask the owner to do it by hand or to send LinkedIn's own data export.
- `search_limit_reached`: If LinkedIn shows a sign-in wall or a search limit, never use or create another account; keep the owner's searches small or research on public company websites.
- `restriction_notice`: If LinkedIn shows a warning or restriction on the account, stop all outreach and automation, save the notice word for word with its official link, and tell the owner.

### 9. Find people in the right buyer role on LinkedIn

Build a checked list of real people whose current role matches the buyer, each with evidence of need, so content and outreach reach people who can use or approve the product.

- **C-LI-ROLES.01** Write the buyer definition from the earlier segment and motive steps: the problem, industry, company size, and region. Name two kinds of role: the person who would use the product and the person likely to approve the purchase. Add exclusion rules such as competitors, existing customers, students, and recruiters.  
  _Done when:_ The buyer definition with user roles, approver roles, and exclusion rules.
- **C-LI-ROLES.02** Write three to five searches in the form 'job function + industry + buying trigger' or 'company + department', using the buyer's own words from the quotes, and save each one's exact terms and date. The owner runs them in LinkedIn by hand; the agent runs the same terms in its own web search and on company websites.  
  _Done when:_ A search log with terms, date, and where each was run: LinkedIn by the owner, web search, or a company site.
- **C-LI-ROLES.03** Collect candidates only by allowed routes: profile URLs or screenshots the owner sends from their own searches, a LinkedIn export the owner provides, single public pages read with read_page, and public company team pages. No scraping tools, no bulk extraction, no extra accounts, and no agent browsing inside LinkedIn while signed in. Remove duplicates by profile URL as you go and stop at 25 unique people this round.  
  _Done when:_ A deduplicated candidate list with each person's original profile URL and how they were found.
- **C-LI-ROLES.04** For each candidate, confirm the current role from a public page or the owner's screenshot: job title, company, the company's website domain, and the date checked. Where possible, check the company's own site lists them. If the current job cannot be confirmed, mark the person 'unknown', not qualified.  
  _Done when:_ For each person: title, company, domain, profile URL, date checked, and confirmed or unknown.
- **C-LI-ROLES.05** Look for public evidence of need: the person's own posts, the company website, job ads, or news that show the problem or a buying trigger. Quote it with its URL and date. A job title alone does not prove budget or buying power; mark buying power as 'guess' until the person says so.  
  _Done when:_ For each qualified person, at least one quote or fact with URL and date, or 'no need evidence found'.
- **C-LI-ROLES.06** Sort every reviewed person into qualified, excluded, or unknown, with a one-line reason each. Qualified means the current role is confirmed and matches the buyer definition. The reviewed total is every unique person checked, rejected and unknown ones included.  
  _Done when:_ Three lists with reasons, and the counts of qualified people and of everyone reviewed.
- **C-LI-ROLES.07** Rank qualified people with need evidence first, and keep no more than three per company on the final list, holding the rest as reserves. Do not message, connect with, or email anyone in this step; contact only happens in a later step the owner approves.  
  _Done when:_ The ranked final list with reserves marked, and a note that no one was contacted.

**Hand back:** `qualified_people`, `excluded_people`, `search_log`, `review_counts`

**If stuck:**
- `buyer_definition_missing`: If there is no clear buyer definition from the earlier steps, go back to the segment step before searching.
- `automation_prohibited`: If a route would need scraping or bulk extraction, do not use it; ask the owner to run the search by hand or provide LinkedIn's own export.
- `search_limit_reached`: If LinkedIn shows a sign-in wall or search limit, never use or create another account; keep the owner's searches small or switch to public company team pages.
- `job_title_uncertain`: If a title does not show whether the person uses or approves this kind of product, mark the person 'unknown' and do not count them as qualified.
- `no_need_evidence`: If no public evidence of need turns up, keep the person only if the role matches, mark need as 'not found', and do not invent a reason.
- `restriction_notice`: If LinkedIn shows a warning or restriction, stop searching, save the notice word for word, and tell the owner.

### 10. Find public business emails for LinkedIn leads

For each qualified LinkedIn lead, find a business email that the person or their company published, with its source, so the owner has real, checkable ways to reach them and the share of leads with a verified email goes up.

- **C-LI-EMAIL.01** Start from the qualified list from the role step. For each person, note the profile URL, current company, and the company website domain. If the person has left that company or the role no longer matches, move them to the no-email list with the reason. Never guess an address from a pattern such as first.last@company.  
  _Done when:_ The list of people to check, each with profile URL and company domain.
- **C-LI-EMAIL.02** Ask the owner to open each person's Contact info on LinkedIn, one at a time, and copy any email shown with the profile URL and the date. The agent does not open it itself. Many people show an email there only to their connections, so 'not shown' is a normal result.  
  _Done when:_ For each person, the email exactly as shown with its source and date, or 'not shown'.
- **C-LI-EMAIL.03** If LinkedIn shows none, use web search and read_page on the company's official website: team, about, author, or contact pages, and any personal website linked from the profile. Copy any email exactly with its URL and the date.  
  _Done when:_ For each person still missing an email, the pages checked and any email found with its URL.
- **C-LI-EMAIL.04** Check each address belongs to that person: their name is in it, or the page ties it to them. Shared inboxes such as info@, support@, sales@, or press@ are recorded as company contacts, not as the person's email.  
  _Done when:_ Each email marked 'personal' or 'shared inbox', with the reason.
- **C-LI-EMAIL.05** Mark each person as verified (their own address, shown by them on LinkedIn or published by them or their company, source saved), company inbox only, or none found with the email left empty. Do not buy lists, use email-guessing tools, or use data brokers.  
  _Done when:_ Every reviewed person with one of the three statuses.
- **C-LI-EMAIL.06** Record, for each email, where it was published and what for (for example 'for business inquiries'). A public email is not consent to receive marketing; mark consent as unknown and note any request not to be contacted. Keep this in the round's list, or in that tool if the owner already uses a CRM.  
  _Done when:_ For each email: source URL, stated purpose, consent 'unknown', and any opt-out noted.
- **C-LI-EMAIL.07** Count everyone reviewed and everyone verified. Send nothing in this step; any later email must be personal, say how the owner is connected to the product, offer an easy opt-out, follow anti-spam law, and be approved by the owner first.  
  _Done when:_ The reviewed and verified counts, and a note that no email was sent.

**Hand back:** `verified_emails`, `no_email_list`, `review_counts`

**If stuck:**
- `no_qualified_leads`: If the role step produced no qualified people, go back to it before looking for emails.
- `contact_email_hidden`: If neither LinkedIn nor the company site shows an email, leave it empty and mark the person 'none found'; never guess an address.
- `only_shared_inbox`: If only info@ or similar is published, record it as a company contact and do not count it as the person's verified email.
- `identity_mismatch`: If the email's page does not clearly tie it to this person at this company, do not count it and note why.
- `automation_prohibited`: If finding emails would need scraping or an email-guessing tool, do not use it; check pages one by one or ask the owner.
- `restriction_notice`: If LinkedIn shows a warning or restriction, stop opening profiles, save the notice word for word, and tell the owner.

### 11. Read this goal's numbers on LinkedIn (baseline numbers)

Record the exact numbers this goal is judged on, for one LinkedIn identity and one fixed date range, so each round is compared with the last on real counts. record_numbers lists exactly which numbers it needs.

- **C-LI-METRICS.01** Confirm what you are measuring: the goal's metric component names exactly as record_numbers lists them, the one LinkedIn identity (personal profile or Company Page, never both mixed), and the date range with its time zone. The range is the goal's observation window and the same length as the baseline.  
  _Done when:_ The component names, the profile or Page URL, and the date range with time zone.
- **C-LI-METRICS.02** Find where each of this goal's components lives. Follower totals and post numbers are in the profile's or Page's analytics, which the owner opens and sends as a screenshot or LinkedIn's own export. Inquiries come from comments on the round's posts (read public posts with read_page), LinkedIn messages the owner shares, and any email or form the owner already receives. Meetings come from the owner's calendar or booking tool; roles and emails from the round's reviewed lists.  
  _Done when:_ A list of each component with the screenshot, export, page, or list it will be read from.
- **C-LI-METRICS.03** Count only the components this goal lists, by their plain meaning. followers: the follower total, read as close to the end of the date range as possible. qualified_inquiries: different people in the range who asked about buying or using the product and fit the buyer definition. confirmed_meetings: demos where the prospect accepted an invite or confirmed a date and time in writing. reviewed_people or reviewed_roles: every unique person checked this round, rejected ones included. verified_public_emails: people whose own business email was published by them or their company, with a source URL. qualified_roles: people whose confirmed current role matches the buyer definition.  
  _Done when:_ Each count, with the list of items behind it (URLs or names) so it can be checked.
- **C-LI-METRICS.04** Count each person once. Leave out the owner, their team, the agent, test accounts, and bots. For rate goals, never drop rejected people from the reviewed total to lift the rate; if nobody was reviewed, record 0 and say so.  
  _Done when:_ A note of who was left out and why, and the reviewed total used.
- **C-LI-METRICS.05** Read supporting numbers where LinkedIn or tracking shows them: impressions and reactions from the post's analytics, and clicks per version (?v=A, ?v=B) from tracking. Write 'not shown' for anything not displayed. Treat a difference based on fewer than 20 clicks or inquiries per version as a hint, not a result, and do not credit a change across months to the content alone.  
  _Done when:_ The supporting numbers as displayed, with 'not shown' where missing and a note on sample size.
- **C-LI-METRICS.06** Add sales only if the owner already has payment records or the round's sale counter. Do not count the owner's own test payments. Where you cannot tell which post or conversation led to a sale, say so plainly.  
  _Done when:_ Any sales figure with its source, or a note that there is none.
- **C-LI-METRICS.07** Call record_numbers with each of this goal's components under its exact name, and a source that says where and when you read it. For a rate goal, pass both components separately, not the rate. If there is no history for a number, record 0 and say in the source that there is no history. Never estimate a number that you could not read.  
  _Done when:_ The record_numbers call as sent, with every component name, value, and source.

**If stuck:**
- `cannot_open_analytics`: If the analytics cannot be opened, ask the owner for a screenshot or LinkedIn's own export showing the numbers this goal needs, for the agreed identity and date range.
- `no_history`: If there is no history for a number, record 0 and say in source that there is no history; this round then sets the baseline.
- `numbers_from_wrong_identity`: If the screenshot or screen shows a different profile or Page from the agreed one, do not use those numbers and ask again.
- `inquiry_fit_unclear`: If you cannot tell whether a person fits the buyer definition, list them as unclear, do not count them, and ask the owner to decide.
- `too_early_to_read`: If the post or outreach is less than 24 hours old, report the numbers as early and read them again at the end of the range.

### 12. Read this goal's numbers on LinkedIn (result numbers)

Record the exact numbers this goal is judged on, for one LinkedIn identity and one fixed date range, so each round is compared with the last on real counts. record_numbers lists exactly which numbers it needs.

- **C-LI-METRICS.01** Confirm what you are measuring: the goal's metric component names exactly as record_numbers lists them, the one LinkedIn identity (personal profile or Company Page, never both mixed), and the date range with its time zone. The range is the goal's observation window and the same length as the baseline.  
  _Done when:_ The component names, the profile or Page URL, and the date range with time zone.
- **C-LI-METRICS.02** Find where each of this goal's components lives. Follower totals and post numbers are in the profile's or Page's analytics, which the owner opens and sends as a screenshot or LinkedIn's own export. Inquiries come from comments on the round's posts (read public posts with read_page), LinkedIn messages the owner shares, and any email or form the owner already receives. Meetings come from the owner's calendar or booking tool; roles and emails from the round's reviewed lists.  
  _Done when:_ A list of each component with the screenshot, export, page, or list it will be read from.
- **C-LI-METRICS.03** Count only the components this goal lists, by their plain meaning. followers: the follower total, read as close to the end of the date range as possible. qualified_inquiries: different people in the range who asked about buying or using the product and fit the buyer definition. confirmed_meetings: demos where the prospect accepted an invite or confirmed a date and time in writing. reviewed_people or reviewed_roles: every unique person checked this round, rejected ones included. verified_public_emails: people whose own business email was published by them or their company, with a source URL. qualified_roles: people whose confirmed current role matches the buyer definition.  
  _Done when:_ Each count, with the list of items behind it (URLs or names) so it can be checked.
- **C-LI-METRICS.04** Count each person once. Leave out the owner, their team, the agent, test accounts, and bots. For rate goals, never drop rejected people from the reviewed total to lift the rate; if nobody was reviewed, record 0 and say so.  
  _Done when:_ A note of who was left out and why, and the reviewed total used.
- **C-LI-METRICS.05** Read supporting numbers where LinkedIn or tracking shows them: impressions and reactions from the post's analytics, and clicks per version (?v=A, ?v=B) from tracking. Write 'not shown' for anything not displayed. Treat a difference based on fewer than 20 clicks or inquiries per version as a hint, not a result, and do not credit a change across months to the content alone.  
  _Done when:_ The supporting numbers as displayed, with 'not shown' where missing and a note on sample size.
- **C-LI-METRICS.06** Add sales only if the owner already has payment records or the round's sale counter. Do not count the owner's own test payments. Where you cannot tell which post or conversation led to a sale, say so plainly.  
  _Done when:_ Any sales figure with its source, or a note that there is none.
- **C-LI-METRICS.07** Call record_numbers with each of this goal's components under its exact name, and a source that says where and when you read it. For a rate goal, pass both components separately, not the rate. If there is no history for a number, record 0 and say in the source that there is no history. Never estimate a number that you could not read.  
  _Done when:_ The record_numbers call as sent, with every component name, value, and source.

**If stuck:**
- `cannot_open_analytics`: If the analytics cannot be opened, ask the owner for a screenshot or LinkedIn's own export showing the numbers this goal needs, for the agreed identity and date range.
- `no_history`: If there is no history for a number, record 0 and say in source that there is no history; this round then sets the baseline.
- `numbers_from_wrong_identity`: If the screenshot or screen shows a different profile or Page from the agreed one, do not use those numbers and ask again.
- `inquiry_fit_unclear`: If you cannot tell whether a person fits the buyer definition, list them as unclear, do not count them, and ask the owner to decide.
- `too_early_to_read`: If the post or outreach is less than 24 hours old, report the numbers as early and read them again at the end of the range.
