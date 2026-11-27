# Creators: get paying customers through creators whose audience wants the product

- **Goal id:** `G-CREATOR-COLLAB`
- **Channel:** partnerships
- **Metric:** `creator_paid_customers` = `external_purchases`, should increase
- **Observation window:** 168 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), partner (the next round starts with `C-CR-FIND`), proposal (the next round starts with `C-CR-OUTREACH`), followup (the next round starts with `C-CR-ENABLE`), motivation (the next round starts with `A-MOTIVES`), data (the next round starts with `C-CR-METRICS`)

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

### 8. Settle the creator offer, the contact account and how sales are counted

Agree with the owner, before any creator is contacted, what creators are offered, which account contacts them, how many may be contacted a day and how each creator's sales are counted, so every message promises only what the owner approved and every sale can be credited.

- **C-CR-ACCESS.01** Ask the owner which account contacts creators: the brand's business email, or the brand's own social account for creators who publish only a message route. Have the owner sign in, or confirm the agent's browser already is; never ask for a password. Check that the name and address shown match the brand.  
  _Done when:_ The contact account, who signed in, and the name shown on it.
- **C-CR-ACCESS.02** Write down what can be offered, from terms the owner already has or decides now: free access (which plan, for how long), an affiliate or referral share (percentage, how long a referral counts, when it is paid, minimum payout), a discount code for the creator's audience if one exists, and a paid sponsorship only if the owner sets a budget. If there are no terms, show the owner two or three options with what each costs and wait for a decision. Never promise money yourself.  
  _Done when:_ The offer the owner approved, quoted from their message, or the options shown and 'waiting for the owner'.
- **C-CR-ACCESS.03** Decide how each creator's sales are counted: the affiliate program the owner already runs (its link format), or, if there is none, call tracking for this round's tracked link and plan one label per creator (?v=creator-name). Confirm with the owner that the sale counter from tracking is on the page shown after payment, so purchases are counted by the engine.  
  _Done when:_ The link format with one example label, and whether the sale counter is in place.
- **C-CR-ACCESS.04** Agree the limits: how many creators may be contacted a day (start at 10 or fewer), at most one follow-up per creator after 5 business days, and who presses send. Platform rules come first: no bulk messages, and no contact through a route the creator did not publish.  
  _Done when:_ The daily cap, the follow-up rule and who sends, approved by the owner.
- **C-CR-ACCESS.05** Write the disclosure line creators will be given: they label the content as sponsored or affiliate as their platform and local law require (for example YouTube's paid promotion setting, or #ad), and the brand never asks them to hide it.  
  _Done when:_ The disclosure line.
- **C-CR-ACCESS.06** Ask the owner how free access is handed out (accounts or codes, how many, which plan, how they are activated) so creators can really try the product. If none can be issued, the offer is affiliate only and says so.  
  _Done when:_ How free access is given and how many are available, or 'affiliate only'.
- **C-CR-ACCESS.07** Put it in five lines (offer, contact account, link format, daily cap, disclosure) and get the owner's yes.  
  _Done when:_ The five-line summary and the owner's approval message.

**Hand back:** `offer_terms`, `contact_account`, `creator_tracking`, `limits`, `owner_approval`

**If stuck:**
- `no_terms`: If the owner has not decided what creators get, contact nobody; show the options and wait for the answer.
- `wrong_account`: If the signed-in account is personal or belongs to another brand, stop and ask the owner to switch or to send the messages themselves.
- `no_sale_counter`: If the sale counter is not on the after-payment page, ask the owner to add it, or name the payment report that will be used instead.
- `no_free_access`: If the owner cannot give creators free access, make the offer affiliate only and say so in every message.
- `owner_action_needed`: If a verification screen, terms screen or identity check appears, stop and tell the owner which screen and which button; never accept terms for them.

### 9. Find creators whose audience already wants the product

Build a checked shortlist of creators whose recent content draws exactly the buyers this product serves (for example piano cover channels for a sheet-music tool), each with a business contact they published, because fit with the audience sells far more than follower count.

- **C-CR-FIND.01** From the buyer group and motive chosen earlier, write who the creator's viewers must be and what they watch or read, for example 'people learning songs on piano watch tutorial and cover videos'. List 3 to 5 content types and the platforms where they live (YouTube, TikTok, Instagram, blogs, newsletters, podcasts).  
  _Done when:_ The audience description, the content types and the platforms.
- **C-CR-FIND.02** Search each platform and the web for those content types, for example 'piano tutorial {song}', '{niche} review' or '{niche} newsletter', with the brackets replaced. Collect at least 30 candidates with about 1,000 to 200,000 followers or subscribers; smaller creators answer more often and their audiences trust them. Skip direct competitors and accounts that only repost.  
  _Done when:_ The searches used, the date, and at least 30 candidates with profile URLs and follower counts as shown.
- **C-CR-FIND.03** For each candidate, use read_page on at least three posts or videos from the last 90 days. Note the views on recent posts (not only followers), what viewers ask in the comments, and whether those questions are what the product answers.  
  _Done when:_ For each candidate, the URLs read, typical recent views, and one line on audience fit with one comment quoted.
- **C-CR-FIND.04** Find each candidate's published business contact: the email on their channel's About page, their website's contact page, a 'work with me' or sponsorship page, or a creator marketplace profile. Use only contacts they published for business; never guess an address or use a personal one found elsewhere. Drop candidates with no published route.  
  _Done when:_ The contact route and the page it is published on, for each remaining candidate, and the list of dropped ones.
- **C-CR-FIND.05** Check what each candidate promoted before and how they disclosed it, and whether they work with a competitor now. Note any rate card or sponsorship terms they publish; if none are published, write 'unknown'.  
  _Done when:_ Past sponsors or 'none seen', how they disclose, any conflict, and published terms or 'unknown'.
- **C-CR-FIND.06** Rank by audience fit first, then recent views, then how clearly they invite business contact. Keep the top 10 to 20 for this round, each with one line on why their audience would buy.  
  _Done when:_ The ranked shortlist with the reason for each rank.
- **C-CR-FIND.07** Show the owner the shortlist and ask them to strike anyone they do not want linked to the brand. Contact nobody in this step.  
  _Done when:_ The owner's reply and the final list.

**Hand back:** `shortlist`, `fit_evidence`, `contact_routes`, `excluded`

**If stuck:**
- `too_few_fits`: If fewer than 10 creators fit, widen to nearby content types or platforms and tell the owner the list is thin.
- `no_published_contact`: If a strong candidate publishes no business contact, leave them off; never guess an email or message someone whose profile says no business requests.
- `competitor_conflict`: If a creator promotes a direct competitor now, mark the conflict and leave the choice to the owner.
- `page_unreadable`: If read_page cannot open a profile, use the platform's public web page or skip the candidate; never log in to collect pages.
- `owner_not_answered`: If the owner has not reviewed the shortlist, submit the step as blocked and say what they need to check.

### 10. Read paid customers from creator links (baseline numbers)

Record how many real outside customers paid through creators in a fixed window, credited to a creator only where a link, label or code shows it, so the next round keeps the creators who sell and drops the ones who do not.

- **C-CR-METRICS.01** Call where_are_we (with lane in a month target) and copy this goal's component name (external_purchases) and observation window. For the baseline use the same length of time just before this round's first invitation; for the current reading use the window since creators started publishing.  
  _Done when:_ The component name, the window with start, end and time zone, and whether this is the baseline or the current reading.
- **C-CR-METRICS.02** Read the engine's own counts first: tracking shows clicks per creator label and the sale counter's purchases in the window. If the step says the engine already counted external_purchases, leave it out of record_numbers; the engine's count is the one used.  
  _Done when:_ Clicks per label and the engine's purchase count, with the time read.
- **C-CR-METRICS.03** Read the payment records for the same window (the payment tool's report or the owner's export) and the affiliate program's report if there is one. Match each purchase to a creator by label, code or the buyer's own words; anything else is 'source unknown'.  
  _Done when:_ Each purchase with its creator or 'source unknown', and the report it came from.
- **C-CR-METRICS.04** Remove the owner's, team's and test payments, refunds inside the window, duplicates, and the free accounts given to creators; a creator's own free access is never a sale.  
  _Done when:_ What was removed and why, with counts before and after.
- **C-CR-METRICS.05** Write one line per creator: post URL, public views, clicks, purchases, and whether a commission is now owed.  
  _Done when:_ One line per creator with these numbers and their sources.
- **C-CR-METRICS.06** Call record_numbers with external_purchases (unless the engine counted it) and a source naming each report and when it was read. If there is no history, record 0 and say 'no history'. In a month target lane also pass paid_customers (paying customers since the month started, from the payment records), and visits and signups if you have them; they update the month progress and are not judged here. Never estimate.  
  _Done when:_ The record_numbers call as accepted.

**If stuck:**
- `cannot_open_payments`: If you cannot open the payment report, ask the owner for an export of the exact window; never estimate sales.
- `no_history`: If there is no earlier window to compare, record 0 and say 'no history'; the first round then sets the baseline.
- `attribution_unknown`: If a sale cannot be tied to a creator, count its source as unknown and credit no one.
- `window_not_finished`: If the window has not ended, report the reading as early and read again when it ends.
- `own_activity_mixed_in`: If the owner's, team's or test purchases cannot be separated, ask the owner to mark them before recording.

### 11. Send the approved creator invitation within the daily cap

Invite each shortlisted creator once, through the contact they published, with a short personal message built from one owner-approved template, so the owner approves the wording and the daily volume once and every creator still gets a message about their own work.

- **C-CR-OUTREACH.01** Write one invitation template under 120 words with placeholders in curly brackets, for example {first_name}, {their_video} (a recent piece of theirs) and {why_their_audience} (one line on why their viewers fit). Say plainly who you write for, the offer exactly as approved, what you ask (try it free and post only if they like it), and how to say no. Everything outside the brackets stays word for word the same in every message. Each placeholder value is one line of at most 80 characters (40 for a name); where one needs more, write its limit, for example {why_their_audience:120} (200 at most). Values carry no links; a link goes in the fixed text or a {link} placeholder.  
  _Done when:_ The template text and the list of its placeholders.
- **C-CR-OUTREACH.02** Write the audience rule in one sentence, for example 'creators on this round's approved shortlist, through their published business contact', and the daily cap agreed in the offer step.  
  _Done when:_ The audience rule and the daily cap.
- **C-CR-OUTREACH.03** Get the template approved. In a month target, send it with submit_batch as one item of kind 'template' with text, audience_rule and daily_cap, and tell the owner to approve it on their owner page or with the approve command. Outside a month target, show the owner the template, the audience rule and the cap, and get a clear yes. Never approve it yourself.  
  _Done when:_ The template's id and the owner's approval, or the owner's yes message.
- **C-CR-OUTREACH.04** Fill the placeholders for each creator from what you read on their own pages; each value is true and one line, at most 80 characters (40 for a name) unless the template sets its own limit such as {their_video:120}, with no link except in a {link} placeholder. If a value does not fit naturally, leave that creator out of this round rather than changing the fixed text.  
  _Done when:_ Each filled message with its recipient.
- **C-CR-OUTREACH.05** Send at most the daily cap per day, one message per creator, from the approved account; the owner sends if the agent has no tool for it. Never put several creators in one email, never switch to another channel, and if you are unsure whether a message went, check Sent before trying again. When today's messages are out, submit this step with approved_item set to the template's id (in a month target) and the sent texts in output; the engine checks each one against the approved template and the day's cap. Fill each placeholder with a true value: one line, at most 80 characters (40 for a name) unless the template sets its own limit, with no link except in a {link} placeholder.  
  _Done when:_ For each message, the recipient, the send time and who sent it.
- **C-CR-OUTREACH.06** After 5 business days with no answer, send at most one short follow-up that is part of the approved templates, then stop. A no or a request to stop ends contact for good and goes on the do-not-contact list.  
  _Done when:_ Follow-ups sent, replies received, and the do-not-contact list.
- **C-CR-OUTREACH.07** Record each reply in one list: yes, maybe (with their questions), no, or no answer. Pass each yes to the next step with what they asked for.  
  _Done when:_ The reply list with each creator's status.

**Hand back:** `template`, `owner_approval`, `sent_messages`, `replies`, `do_not_contact`

**If stuck:**
- `owner_has_not_approved`: If the owner has not approved the template, send nothing; show them the template, rule and cap and wait.
- `over_daily_cap`: If the shortlist is larger than the daily cap, send the rest on the following days; never go over the cap.
- `value_not_true`: If you cannot fill a placeholder with something true from their own pages, leave that creator out of this round.
- `bounce`: If an address bounces, remove it; never retry with a guessed spelling or another route.
- `platform_limit`: If the platform limits or flags the messages, stop for the day and tell the owner.

### 12. Give each creator who said yes free access, their own link and a short brief

Turn each yes into a live, disclosed piece of content that points to the product through the creator's own link, so their audience hears a true message and every sale can be credited to them.

- **C-CR-ENABLE.01** For each creator who said yes, set up what was promised: the free account or code the owner issued, and their own link: their affiliate link if a program exists, otherwise this round's tracked link with their label (?v=their-name). Open each link and check it lands on the right page.  
  _Done when:_ For each creator, the access given and the link, opened and confirmed.
- **C-CR-ENABLE.02** Write a one-page brief: who the product is for, the problem it solves in the buyer's words, three benefits from the proven benefits list, the price as shown on the product page, their link and code, the disclosure line, and a 'please do not say' list (no invented results, no guarantees, no fake urgency). Leave the creative choices to them.  
  _Done when:_ The brief, and a sentence-by-sentence check against the product facts.
- **C-CR-ENABLE.03** Show the owner the brief and the delivery message word for word and get a yes, then send each creator their brief once from the approved account.  
  _Done when:_ The owner's approval and, for each creator, the send time.
- **C-CR-ENABLE.04** Answer each creator's product questions from the fact sheet within one business day; anything not on it goes to the owner first.  
  _Done when:_ The questions asked and the answers given, with the owner's answer where one was needed.
- **C-CR-ENABLE.05** When a creator publishes, open the post and check that their link or code is there and the disclosure is shown. If something is missing, ask them politely once to fix it. Never ask them to change their opinion.  
  _Done when:_ Each live post URL, whether the link and the disclosure are present, and any fix requested.
- **C-CR-ENABLE.06** Record each creator's link, terms, post URL and publish date. A commission is owed only on a counted sale and paid only when it has really been paid.  
  _Done when:_ The creator record with link, terms, post URL, publish date and commission status.

**Hand back:** `creators_live`, `creator_links`, `brief_text`, `post_urls`

**If stuck:**
- `creator_not_live`: If no creator has published by the end of the window, record that; never publish on their behalf or write their post for them.
- `disclosure_missing`: If a post has no disclosure, ask the creator once to add it and tell the owner; do not promote that post until it is fixed.
- `link_broken`: If a creator's link does not open the product, fix it with tracking and send them the corrected link.
- `no_access_to_give`: If the owner has not issued the free accounts or codes, submit the step as blocked with exactly how many are needed.
- `creator_asks_for_money`: If a creator asks for a fee beyond the approved terms, take it to the owner and promise nothing.

### 13. Read paid customers from creator links (result numbers)

Record how many real outside customers paid through creators in a fixed window, credited to a creator only where a link, label or code shows it, so the next round keeps the creators who sell and drops the ones who do not.

- **C-CR-METRICS.01** Call where_are_we (with lane in a month target) and copy this goal's component name (external_purchases) and observation window. For the baseline use the same length of time just before this round's first invitation; for the current reading use the window since creators started publishing.  
  _Done when:_ The component name, the window with start, end and time zone, and whether this is the baseline or the current reading.
- **C-CR-METRICS.02** Read the engine's own counts first: tracking shows clicks per creator label and the sale counter's purchases in the window. If the step says the engine already counted external_purchases, leave it out of record_numbers; the engine's count is the one used.  
  _Done when:_ Clicks per label and the engine's purchase count, with the time read.
- **C-CR-METRICS.03** Read the payment records for the same window (the payment tool's report or the owner's export) and the affiliate program's report if there is one. Match each purchase to a creator by label, code or the buyer's own words; anything else is 'source unknown'.  
  _Done when:_ Each purchase with its creator or 'source unknown', and the report it came from.
- **C-CR-METRICS.04** Remove the owner's, team's and test payments, refunds inside the window, duplicates, and the free accounts given to creators; a creator's own free access is never a sale.  
  _Done when:_ What was removed and why, with counts before and after.
- **C-CR-METRICS.05** Write one line per creator: post URL, public views, clicks, purchases, and whether a commission is now owed.  
  _Done when:_ One line per creator with these numbers and their sources.
- **C-CR-METRICS.06** Call record_numbers with external_purchases (unless the engine counted it) and a source naming each report and when it was read. If there is no history, record 0 and say 'no history'. In a month target lane also pass paid_customers (paying customers since the month started, from the payment records), and visits and signups if you have them; they update the month progress and are not judged here. Never estimate.  
  _Done when:_ The record_numbers call as accepted.

**If stuck:**
- `cannot_open_payments`: If you cannot open the payment report, ask the owner for an export of the exact window; never estimate sales.
- `no_history`: If there is no earlier window to compare, record 0 and say 'no history'; the first round then sets the baseline.
- `attribution_unknown`: If a sale cannot be tied to a creator, count its source as unknown and credit no one.
- `window_not_finished`: If the window has not ended, report the reading as early and read again when it ends.
- `own_activity_mixed_in`: If the owner's, team's or test purchases cannot be separated, ask the owner to mark them before recording.
