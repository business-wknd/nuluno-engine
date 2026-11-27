# Members: move free and one-time users to a paid or season plan

- **Goal id:** `G-BASE-UPGRADE`
- **Channel:** customer_base
- **Metric:** `upgrades` = `upgrades`, should increase
- **Observation window:** 168 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `C-BASE-SEGMENT`), motivation (the next round starts with `A-MOTIVES`), data (the next round starts with `C-BASE-METRICS`), fit (the next round starts with `C-BASE-UPGRADE`), message (the next round starts with `C-BASE-UPGRADE`)

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

### 8. Confirm the member list, the channels you may use and the limits

Find out exactly which list of existing members or customers can be used, through which channels the owner may message them, who agreed to what, and how much there is to sell, so every message goes only to people the brand may contact and no seat is sold that does not exist.

- **C-BASE-ACCESS.01** Ask the owner where members are recorded: a list uploaded on the hosted owner page, the payment tool (Stripe customers), a booking or ticketing tool, a CRM, a spreadsheet, a LINE Official Account or WhatsApp Business. If nothing is uploaded yet, ask for a CSV export with email or phone, name, status (member, paying, free, past) and last purchase date, uploaded on the owner page or shared as a file. Never ask for a password to their tools.  
  _Done when:_ The list source, its columns, the row count, and when it was exported.
- **C-BASE-ACCESS.02** For each channel the owner can message (email, LINE, WhatsApp, Instagram or Facebook messages, SMS), write which account sends, its sending limits and who presses send. Have the owner sign in, or confirm the agent's browser already is.  
  _Done when:_ Each channel with its sending account, limit and sender.
- **C-BASE-ACCESS.03** Check consent per channel: who agreed to marketing email or messages, who only bought (some countries allow email to past buyers about similar products if they can opt out; others do not), and who unsubscribed or asked to stop. Write the rule you will apply and ask the owner to confirm it. People with no record of agreeing are left out of marketing messages.  
  _Done when:_ The consent rule, how many people it allows per channel, and the owner's confirmation.
- **C-BASE-ACCESS.04** Get the do-not-contact list: unsubscribes, bounces, complaints, people who asked to stop, staff and test accounts. They are removed from every send in this goal.  
  _Done when:_ The do-not-contact list's size and where it came from.
- **C-BASE-ACCESS.05** Ask for the capacity: seats, tables, stock or onboarding slots per week and the dates they cover (for example 'Taipei Saturday events: 40 seats a week'). Every offer in this goal stays inside it; if the plan would sell more than exists, the plan changes, not the promise.  
  _Done when:_ Capacity per week with dates and source, or 'no limit' confirmed by the owner.
- **C-BASE-ACCESS.06** Read the current offer from the product's own pages: plans, prices, member or season options, existing discounts and referral rewards. Do not create plans, codes or rewards; the owner does that in their own tools if they decide to.  
  _Done when:_ The offer sheet with each line's URL.
- **C-BASE-ACCESS.07** Summarise in five lines (list, channels, consent rule, do-not-contact list, capacity) and get the owner's yes.  
  _Done when:_ The summary and the owner's approval message.

**Hand back:** `member_list`, `channels`, `consent_rule`, `suppression`, `capacity`

**If stuck:**
- `no_list`: If there is no member list, ask the owner to upload or export one and say exactly where on the owner page to do it; until then this goal sends nothing.
- `consent_unknown`: If nobody can say who agreed to messages, use only people who bought or wrote to the brand in the last 90 days and did not opt out, and tell the owner.
- `wrong_account`: If the signed-in sending account is personal or another brand's, stop and ask the owner to switch or to send themselves.
- `capacity_unknown`: If the owner cannot say how many seats or units exist, offer no dates or stock until they confirm.
- `personal_data_care`: Keep the list inside the hosted service or the owner's own files; never paste it into public places or other tools.

### 9. Pick the members this round is for

Turn the member list into one clear group for this goal, with a count and a reason, so the message speaks to their situation and the result is read against the right group.

- **C-BASE-SEGMENT.01** Apply the group this goal needs. Win back: paid or attended before, nothing in the last 60 to 180 days (pick the range from how often members normally come back). Referral: paying or recently active members who came at least twice or rated it well. Upgrade: free, trial or one-time buyers who used it at least once in the last 60 days. Write the exact rule with dates.  
  _Done when:_ The rule in one sentence with its date range.
- **C-BASE-SEGMENT.02** Count the group from the list, then remove the do-not-contact list and anyone outside the consent rule. When the hosted list is used, the counts come from it.  
  _Done when:_ The count before and after each removal.
- **C-BASE-SEGMENT.03** Split the group by what changes the message: city or location, what they bought, how long ago, how often. Keep at most 3 sub-groups; a sub-group under 30 people merges with another.  
  _Done when:_ The sub-groups with their counts.
- **C-BASE-SEGMENT.04** For each sub-group, write the one real reason to act now (a new date in their city, a season starting, a feature they asked for), taken from the product facts and the buyer research.  
  _Done when:_ One reason per sub-group with its source.
- **C-BASE-SEGMENT.05** Choose the channel per sub-group from the confirmed channels: the one they agreed to and use most.  
  _Done when:_ The channel per sub-group.
- **C-BASE-SEGMENT.06** Check capacity: if everyone in the group said yes, would it fit the seats or stock per week? If not, spread the sends over weeks or make the group smaller.  
  _Done when:_ The capacity check and the send plan by week.

**Hand back:** `segment_rule`, `counts`, `sub_groups`, `channel_plan`

**If stuck:**
- `group_too_small`: If the group has fewer than 30 people, widen the date range and say so.
- `list_out_of_date`: If the list was exported more than 14 days ago, ask the owner for a fresh export before anything is sent.
- `consent_unknown`: If you cannot tell who agreed to messages on a channel, leave those people out and tell the owner how many.
- `capacity_short`: If capacity cannot take the whole group, send to part of it now and the rest when seats free up.

### 10. Read this goal's member numbers (baseline numbers)

Record the number this goal is judged on, counted once per real person and net of refunds and tests, for the window before this round and for this round, so rounds are compared on paying members rather than replies.

- **C-BASE-METRICS.01** Call where_are_we (with lane in a month target) and copy this goal's component name and window: reactivated_paying_members, paid_referrals or upgrades.  
  _Done when:_ The goal id, the component name and the window in hours.
- **C-BASE-METRICS.02** Write the counting rule before counting. reactivated_paying_members: a member of this round's win-back group who paid again inside the window. paid_referrals: a new customer who paid inside the window and came through a member's link, label or code. upgrades: a free, trial or one-time user in this round's group who started a paid or season plan inside the window.  
  _Done when:_ The rule for this goal's component, with dates and time zone.
- **C-BASE-METRICS.03** Read the payment records for the window (the payment tool, the booking tool or the owner's export) and tracking's clicks per label. Match each payment to the group by email, member code or label.  
  _Done when:_ The sources read with times, and the matched payments.
- **C-BASE-METRICS.04** Remove the owner's, team's and test payments, refunds inside the window, duplicates, and anyone who was already on that plan or paid before the round started.  
  _Done when:_ What was removed and why, with counts.
- **C-BASE-METRICS.05** For the baseline, count the same thing for the same length of time just before this round, among the same kind of group (members who came back on their own, friends who arrived without an invite, upgrades without an offer). If there is no history, record 0 and say so.  
  _Done when:_ The baseline count and how it was taken.
- **C-BASE-METRICS.06** Call record_numbers with this goal's component and a source naming each report and when it was read. In a month target lane also pass paid_customers (paying customers since the month started, from the payment records), and visits and signups if you have them; they update the month progress and are not judged here. Never estimate; a reply or a booking that is not paid does not count.  
  _Done when:_ The record_numbers call as accepted.

**If stuck:**
- `cannot_open_payments`: If you cannot open the payment records, ask the owner for an export of the exact window; never estimate.
- `cannot_match`: If payments cannot be matched to the group, count only matched ones and say how many could not be matched.
- `no_history`: If there is no earlier window to compare, record 0 and say 'no history'.
- `window_not_finished`: If the window has not ended, report the reading as early and read again when it ends.
- `own_activity_mixed_in`: If the owner's, team's or test payments cannot be separated, ask the owner to mark them before recording.

### 11. Offer free and one-time users the paid or season plan that fits them

Show people who already tried the product the existing paid plan that matches how they use it, with the real price and what changes for them, so the ones who would get more from it move up without pressure.

- **C-BASE-UPGRADE.01** From the segment step, write how each sub-group uses the product today and which existing plan fits (for example 'came to two single events in three months: the season pass costs less than three single tickets'). Work out the saving or gain from the real prices; if it is not real for a sub-group, make them no offer.  
  _Done when:_ Each sub-group with the plan that fits and the calculation from the price page.
- **C-BASE-UPGRADE.02** Write one template per sub-group under 100 words with placeholders such as {first_name}, {times_used} and {what_they_get}. Give the price as shown on the product page, the one main benefit, a link to the plan with the round's tracked link (?v= per sub-group), and how to say no. Mention a deadline only if the offer really ends then. Each placeholder value is one line of at most 80 characters (40 for a name); where one needs more, write its limit, for example {what_they_get:120} (200 at most). Values carry no links; a link goes in the fixed text or a {link} placeholder.  
  _Done when:_ Each template with its placeholders.
- **C-BASE-UPGRADE.03** Get the template approved. In a month target, send it with submit_batch as one item of kind 'template' with text, audience_rule and daily_cap, and tell the owner to approve it on their owner page or with the approve command. Outside a month target, show the owner the template, the audience rule and the cap, and get a clear yes. Never approve it yourself.  
  _Done when:_ The template ids and the owner's approval.
- **C-BASE-UPGRADE.04** Check capacity before sending: a season or membership plan needs the seats or slots behind it. Send no more offers in a week than capacity could take if everyone said yes.  
  _Done when:_ The capacity check for this week's sends.
- **C-BASE-UPGRADE.05** Send once per person within the daily cap, from next_recipients on the hosted service or the owner's export, from the approved account. When today's messages are out, submit this step with approved_item set to the template's id (in a month target) and the sent texts in output; the engine checks each one against the approved template and the day's cap. Fill each placeholder with a true value: one line, at most 80 characters (40 for a name) unless the template sets its own limit, with no link except in a {link} placeholder.  
  _Done when:_ Per day: how many were sent and on which channel, with a sample of the sent texts.
- **C-BASE-UPGRADE.06** Answer replies from the fact sheet the same day where you can; refunds, billing and exceptions go to the owner. Record each upgrade with its payment reference and date.  
  _Done when:_ Replies with answers, and each upgrade with its payment reference.

**Hand back:** `plan_fit`, `templates`, `owner_approval`, `sent_record`, `upgrades`

**If stuck:**
- `no_fitting_plan`: If no existing plan is a real gain for a sub-group, make them no offer and tell the owner what plan they asked for.
- `owner_has_not_approved`: If the owner has not approved a template, send nothing with it.
- `capacity_full`: If the plan has no seats or slots left, stop sending offers for it at once.
- `billing_change_needed`: If upgrading needs something the payment tool cannot do yet, tell the owner; never change billing yourself.
- `over_daily_cap`: If more people are due than the cap allows, send the rest on later days.

### 12. Read this goal's member numbers (result numbers)

Record the number this goal is judged on, counted once per real person and net of refunds and tests, for the window before this round and for this round, so rounds are compared on paying members rather than replies.

- **C-BASE-METRICS.01** Call where_are_we (with lane in a month target) and copy this goal's component name and window: reactivated_paying_members, paid_referrals or upgrades.  
  _Done when:_ The goal id, the component name and the window in hours.
- **C-BASE-METRICS.02** Write the counting rule before counting. reactivated_paying_members: a member of this round's win-back group who paid again inside the window. paid_referrals: a new customer who paid inside the window and came through a member's link, label or code. upgrades: a free, trial or one-time user in this round's group who started a paid or season plan inside the window.  
  _Done when:_ The rule for this goal's component, with dates and time zone.
- **C-BASE-METRICS.03** Read the payment records for the window (the payment tool, the booking tool or the owner's export) and tracking's clicks per label. Match each payment to the group by email, member code or label.  
  _Done when:_ The sources read with times, and the matched payments.
- **C-BASE-METRICS.04** Remove the owner's, team's and test payments, refunds inside the window, duplicates, and anyone who was already on that plan or paid before the round started.  
  _Done when:_ What was removed and why, with counts.
- **C-BASE-METRICS.05** For the baseline, count the same thing for the same length of time just before this round, among the same kind of group (members who came back on their own, friends who arrived without an invite, upgrades without an offer). If there is no history, record 0 and say so.  
  _Done when:_ The baseline count and how it was taken.
- **C-BASE-METRICS.06** Call record_numbers with this goal's component and a source naming each report and when it was read. In a month target lane also pass paid_customers (paying customers since the month started, from the payment records), and visits and signups if you have them; they update the month progress and are not judged here. Never estimate; a reply or a booking that is not paid does not count.  
  _Done when:_ The record_numbers call as accepted.

**If stuck:**
- `cannot_open_payments`: If you cannot open the payment records, ask the owner for an export of the exact window; never estimate.
- `cannot_match`: If payments cannot be matched to the group, count only matched ones and say how many could not be matched.
- `no_history`: If there is no earlier window to compare, record 0 and say 'no history'.
- `window_not_finished`: If the window has not ended, report the reading as early and read again when it ends.
- `own_activity_mixed_in`: If the owner's, team's or test payments cannot be separated, ask the owner to mark them before recording.
