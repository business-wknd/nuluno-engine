# Live demo: raise purchases among attendees

- **Goal id:** `G-WB-PURCHASE`
- **Language:** English
- **Channel:** webinar
- **Metric:** `purchase_rate` = `external_purchases` / `attendees`, should increase
- **Observation window:** 168 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), invite (the next round starts with `A-ANGLES`), data (the next round starts with `C-WB-METRICS`)

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

### 8. Confirm the meeting tool, host account and live presenter

Settle which brand account hosts the live demo, what its plan allows, who presents and where attendance numbers will come from, so the event can run under the right name without upgrades or surprises mid-way.

- **C-WEBINAR-ACCESS.01** Ask the owner which meeting or webinar tool the brand already uses and which account will host. The host must be the brand's account, not someone else's personal one. Use what exists; do not sign up for a new tool unless the owner asks in this conversation.  
  _Done when:_ The tool's name and the host account, confirmed by the owner.
- **C-WEBINAR-ACCESS.02** Decide who creates the event: the owner, or the agent's own browser if it is already signed in to the host account. If nobody is signed in, the owner signs in on the tool's official screen or company sign-in and enters any code themselves. Never ask for a password.  
  _Done when:_ Who will create the event, and the account name shown after sign-in.
- **C-WEBINAR-ACCESS.03** Read the plan's limits from the account's plan or billing page, or ask the owner: maximum participants, maximum meeting length, whether registration pages are included, whether recording is included, and whether this host account is allowed to create events. Do not buy an upgrade to get past a limit.  
  _Done when:_ Each limit with where it was read, or 'not known'.
- **C-WEBINAR-ACCESS.04** Confirm a real person will present the live demo: their name, role, and two or three dates and times they can do, with time zone. The agent cannot host or present a live session for people.  
  _Done when:_ The presenter's name and their available slots with time zone.
- **C-WEBINAR-ACCESS.05** Ask the owner whether the event will be recorded. Record only if the owner agrees and attendees are told at the start; if the tool has its own recording notice, leave it on. Write down where a replay would be shared, if anywhere.  
  _Done when:_ The recording decision and how attendees will be told.
- **C-WEBINAR-ACCESS.06** Confirm how people register: the tool's own registration page or a signup form the owner already has. Do not change the product's own signup or its tracking codes. Write down that registrations, people who join and purchases are read later from the tool's registration and attendee reports and the owner's payment records, never before the event happens.  
  _Done when:_ The registration route and the reports that will be used for the numbers.

**Hand back:** `host_account`, `who_creates_event`, `plan_limits`, `presenter`, `attendance_source`

**If stuck:**
- `plan_capacity_limit`: If the plan cannot hold the event, show the owner the limit and either plan a smaller event or wait; never upgrade or pay without the owner's written yes.
- `host_not_confirmed`: If no real person has agreed to present, prepare the details but do not create or announce the event.
- `owner_action_needed`: If a sign-in code, terms screen or identity check appears, stop and tell the owner which screen and which button; never enter codes or accept terms for them.
- `no_meeting_tool`: If the brand has no meeting tool, ask the owner which one they want; set up one free account in the brand's name only after they say so, and leave terms screens and any payment to the owner.
- `wrong_host_account`: If the signed-in account is personal or belongs to another brand, stop and ask the owner to switch to the agreed host account.

### 9. Read this goal's live demo numbers (baseline numbers)

Record the numbers this goal is judged on, for the event before this round and for this round's event, so rounds are compared on real registrations, attendance, meetings and sales. record_numbers lists exactly which numbers it needs.

- **C-WB-METRICS.01** Confirm which event you are measuring: its link or ID, date, time zone, and the date range. For the baseline use the owner's last comparable live event before this round; for the current reading use this round's event, read once the goal's observation window has passed (7 days after the event for these goals). If the event has not happened yet, do not record attendance.  
  _Done when:_ The event link or ID, its date and time zone, the date range, and whether this is the baseline or the current reading.
- **C-WB-METRICS.02** Read the tool's registration report and attendee report for that event, or ask the owner for an export or screenshot. Count each person once by email, even if they joined twice. Take out the host, presenter, owner, team and any test registration.  
  _Done when:_ Registrations and attendees as counted, with the report they came from, the time read, and what was removed.
- **C-WB-METRICS.03** Count attendees only as people who joined the live event. Where the attendee report shows time in session, note separately how many stayed at least 10 minutes, and how many watched a replay; replay views are not attendees.  
  _Done when:_ Live attendees, those who stayed 10 minutes or more, and replay views, each with its source.
- **C-WB-METRICS.04** List every question asked in the chat or Q&A and every request for a one-to-one demo. Count a confirmed meeting only when a date and time are accepted by both sides in writing or by an accepted calendar invite; requested, unanswered or cancelled meetings do not count. Signing up for the event is not agreement to marketing email.  
  _Done when:_ Each question, each meeting request, and each confirmed meeting with its date, time and confirmation.
- **C-WB-METRICS.05** Read sales from the round's sale counter and the owner's payment records for the date range. Count each order once, take out refunds and test or owner payments, and match buyers to attendees by email where possible. Say plainly where you cannot tell whether a sale came from the event.  
  _Done when:_ Purchases with their sources, how many were matched to attendees, and any sale whose link to the event is unclear.
- **C-WB-METRICS.06** Write down what the event cost: the tool's fee for the period, any paid promotion, and presenter time if the owner gives it. Keep costs separate from the goal's numbers.  
  _Done when:_ Each cost with its amount, currency and source, or 'not given by the owner'.
- **C-WB-METRICS.07** Call record_numbers with the exact component names this goal lists: registrations and attendees, confirmed_meetings, or external_purchases and attendees. Give each value its source. If there is no earlier event, record 0 and say 'no history' in the source. If the number you would divide by is 0, do not work out a rate; report it. Never estimate a number.  
  _Done when:_ The record_numbers call with every component, its value and its source.

**If stuck:**
- `attendance_pending`: If the event has not happened or its attendee report is not ready, report attendance as pending and read again later; never fill it in by guess.
- `cannot_open_report`: If you cannot open the tool's reports, ask the owner for an export or screenshot of the registration and attendee reports for that event.
- `no_history`: If there is no earlier comparable event, record 0 and say in the source that there is no history; the first round then sets the baseline.
- `zero_registrations`: If there were no registrations, record 0, do not work out a rate, and report that the invite step needs attention.
- `meeting_not_confirmed`: If a meeting request has no accepted date and time, list it as requested and leave it out of confirmed meetings.
- `sales_not_traceable`: If payments cannot be matched to the event, record only what the sale counter shows and state that the rest is unknown; never assign sales by guess.

### 10. Create the live demo event and its registration page

Create one real, owner-approved live demo of what the product does today, with a working registration page, because people can only register, attend and buy if a real event with a real presenter exists.

- **C-WB-SCHEDULE.01** Write a short event brief: who it is for (the chosen buyer group), the problem the demo solves (the chosen angle), what will be shown live, the presenter, a length of 30 to 45 minutes, and at least 10 minutes for questions. Show only features the product has today.  
  _Done when:_ The event brief, with each feature checked against the product facts.
- **C-WB-SCHEDULE.02** Pick a date and time at least 7 days ahead, in the main time zone of the buyer group, avoiding public holidays there. The owner and the presenter both confirm the slot.  
  _Done when:_ The date, time and time zone, and the owner's and presenter's confirmation.
- **C-WB-SCHEDULE.03** Look in the host account for an event already scheduled for this demo. If one exists, update that event instead of creating a second one.  
  _Done when:_ A note that no matching event exists, or the link of the existing one that will be used.
- **C-WB-SCHEDULE.04** Draft the event page: title, a short description of what attendees will see, date and time with time zone, length, presenter, and registration questions (name, email, and one optional 'what do you want to see?'). State facts only; no invented seat limits, bonuses or results. Show the owner the page text word for word and get a clear yes.  
  _Done when:_ The exact event page text and the owner's approval message.
- **C-WB-SCHEDULE.05** Create the event once in the host account: the owner does it, or the agent's own browser if signed in and the owner said yes. Turn registration on, keep capacity within the plan limit, and turn on the tool's reminder emails if it has them. If creating seems to fail, check the event list before trying again.  
  _Done when:_ The event ID and the registration page URL.
- **C-WB-SCHEDULE.06** Open the registration page as a visitor and check that it loads with the right title, date, time zone and presenter. If you make a test registration, use the owner's own address, check the confirmation carries the join link, and note it so it is taken out of the counts.  
  _Done when:_ Confirmation that the page loads correctly and the join link arrives, and any test registration noted.
- **C-WB-SCHEDULE.07** Hand over the event as 'waiting for the event'. Do not report any attendance, recording or replay until the event has happened and the tool's attendee report exists. If the time must change later, update this same event and tell registrants once.  
  _Done when:_ The event status, its date, and where attendance will be read after it.

**Hand back:** `event_id`, `registration_url`, `event_details`, `presenter_confirmed`, `attendance_source`

**If stuck:**
- `host_not_confirmed`: If no presenter has confirmed the slot, keep the event as a draft and do not open registration.
- `plan_capacity_limit`: If the plan cannot hold the expected number of people, show the owner the limit and set a smaller capacity; never upgrade without the owner's written yes.
- `owner_has_not_approved`: If the owner has not said yes to the event page text, do not create or publish the event; show them the text and stop until they answer.
- `duplicate_event`: If an event for this demo already exists, update it instead of creating another, so registrants do not get two invitations.
- `feature_not_ready`: If a feature in the brief is not live in the product, remove it from the agenda and the page; never demo or promise what does not exist.

### 11. Invite opted-in people to the live demo and follow up

Invite only people who agreed to hear from the brand or asked for a demo, with a personal, owner-approved message and the registration link from the first step, then remind registrants and follow up on questions, because the right invitations decide who registers, who shows up and who books or buys after.

- **C-WB-INVITE.01** Open the event's registration page and confirm it exists and shows the right title, date, time zone and presenter. Ask tracking for the round's tracked link; use it only if it can point at the registration page, with ?v=A and ?v=B if there are two invite versions. Otherwise use the registration page URL itself and read registrations from the tool's report.  
  _Done when:_ The registration page URL you opened and the link each invite version will carry.
- **C-WB-INVITE.02** Choose who to invite: contacts who agreed to hear from the brand, people who asked for a demo in an existing conversation, and communities whose rules allow event posts. Leave out anyone who unsubscribed, said no, already registered, or already bought (unless the demo is for customers). Keep to the owner's cap; for personal messages, at most 30 a day.  
  _Done when:_ The invite list or groups, the reason each is included, and the counts.
- **C-WB-INVITE.03** Write one invite under 120 words that names the reader's problem, what they will see, the date and time in their time zone, the length, the presenter, and the registration link from the first step. Say who is sending and that they run the product. No invented seat limits, deadlines or results. Emails carry the unsubscribe link or line.  
  _Done when:_ The invite text for each version, with its word count.
- **C-WB-INVITE.04** Show the owner, word for word, each invite version, the channel, and who will receive it, and get a clear yes before anything is sent or posted.  
  _Done when:_ The exact invites shown and the owner's approval message.
- **C-WB-INVITE.05** Send through the brand's own channel: the owner's email tool, or a reply in the existing conversation. The agent sends only with its own tools and the owner's yes; otherwise the owner sends. Send each invite once; if status is unclear, check Sent before retrying, and never resend through another channel. A community post ends with its public URL.  
  _Done when:_ Who sent, when, how many invites went out, and the public URL of any post.
- **C-WB-INVITE.06** Remind registrants once 24 hours before and once at the start, unless the tool already sends reminders. Send non-registrants at most one follow-up, no sooner than 3 days after the first invite and never after the event. The owner approves the reminder and follow-up text.  
  _Done when:_ Each reminder or follow-up with its text, date, audience and the owner's approval.
- **C-WB-INVITE.07** After the event, within 24 hours, draft a short personal reply for each attendee who asked a question or asked for a one-to-one demo: answer from the product facts and offer two times the presenter has confirmed, or the owner's booking link. Only these people get it, and only after the owner approves the text. Any link to the product uses the round's tracked link.  
  _Done when:_ The list of people followed up, each message as sent, and any times they accepted.
- **C-WB-INVITE.08** Keep invites sent, registrations, attendees, replay views, meetings and purchases separate. Never report invites as registrations; pass the event to the measuring step.  
  _Done when:_ A short record of what was sent and what is still waiting for the event or its reports.

**Hand back:** `invite_text`, `recipients`, `owner_approval`, `sent_record`, `tracked_links`

**If stuck:**
- `event_not_found`: If the registration page does not load or shows the wrong details, stop and go back to the event step before inviting anyone.
- `owner_has_not_approved`: If the owner has not said yes to this exact invite, do not send or post; show them the text and stop until they answer.
- `consent_unknown`: If you cannot tell whether a person agreed to hear from the brand, leave them out of the invite.
- `send_status_unknown`: If you cannot tell whether an invite went out, check Sent or the conversation first; never send it again or through a different channel.
- `recipient_said_no`: If someone replies no or asks to stop, remove them from all reminders and follow-ups at once and record it.
- `host_not_confirmed`: If the presenter cancels, do not send invites; tell the owner and move the event to a new confirmed time first.

### 12. Read this goal's live demo numbers (result numbers)

Record the numbers this goal is judged on, for the event before this round and for this round's event, so rounds are compared on real registrations, attendance, meetings and sales. record_numbers lists exactly which numbers it needs.

- **C-WB-METRICS.01** Confirm which event you are measuring: its link or ID, date, time zone, and the date range. For the baseline use the owner's last comparable live event before this round; for the current reading use this round's event, read once the goal's observation window has passed (7 days after the event for these goals). If the event has not happened yet, do not record attendance.  
  _Done when:_ The event link or ID, its date and time zone, the date range, and whether this is the baseline or the current reading.
- **C-WB-METRICS.02** Read the tool's registration report and attendee report for that event, or ask the owner for an export or screenshot. Count each person once by email, even if they joined twice. Take out the host, presenter, owner, team and any test registration.  
  _Done when:_ Registrations and attendees as counted, with the report they came from, the time read, and what was removed.
- **C-WB-METRICS.03** Count attendees only as people who joined the live event. Where the attendee report shows time in session, note separately how many stayed at least 10 minutes, and how many watched a replay; replay views are not attendees.  
  _Done when:_ Live attendees, those who stayed 10 minutes or more, and replay views, each with its source.
- **C-WB-METRICS.04** List every question asked in the chat or Q&A and every request for a one-to-one demo. Count a confirmed meeting only when a date and time are accepted by both sides in writing or by an accepted calendar invite; requested, unanswered or cancelled meetings do not count. Signing up for the event is not agreement to marketing email.  
  _Done when:_ Each question, each meeting request, and each confirmed meeting with its date, time and confirmation.
- **C-WB-METRICS.05** Read sales from the round's sale counter and the owner's payment records for the date range. Count each order once, take out refunds and test or owner payments, and match buyers to attendees by email where possible. Say plainly where you cannot tell whether a sale came from the event.  
  _Done when:_ Purchases with their sources, how many were matched to attendees, and any sale whose link to the event is unclear.
- **C-WB-METRICS.06** Write down what the event cost: the tool's fee for the period, any paid promotion, and presenter time if the owner gives it. Keep costs separate from the goal's numbers.  
  _Done when:_ Each cost with its amount, currency and source, or 'not given by the owner'.
- **C-WB-METRICS.07** Call record_numbers with the exact component names this goal lists: registrations and attendees, confirmed_meetings, or external_purchases and attendees. Give each value its source. If there is no earlier event, record 0 and say 'no history' in the source. If the number you would divide by is 0, do not work out a rate; report it. Never estimate a number.  
  _Done when:_ The record_numbers call with every component, its value and its source.

**If stuck:**
- `attendance_pending`: If the event has not happened or its attendee report is not ready, report attendance as pending and read again later; never fill it in by guess.
- `cannot_open_report`: If you cannot open the tool's reports, ask the owner for an export or screenshot of the registration and attendee reports for that event.
- `no_history`: If there is no earlier comparable event, record 0 and say in the source that there is no history; the first round then sets the baseline.
- `zero_registrations`: If there were no registrations, record 0, do not work out a rate, and report that the invite step needs attention.
- `meeting_not_confirmed`: If a meeting request has no accepted date and time, list it as requested and leave it out of confirmed meetings.
- `sales_not_traceable`: If payments cannot be matched to the event, record only what the sale counter shows and state that the rest is unknown; never assign sales by guess.
