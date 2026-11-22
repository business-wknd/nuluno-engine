# TikTok Ads: raise the link click rate of video ads

- **Goal id:** `G-TA-LINK-CTR`
- **Language:** English
- **Channel:** tiktok_ads
- **Metric:** `link_ctr` = `link_clicks` / `impressions`, should increase
- **Observation window:** 168 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), creative (the next round starts with `S13`), data (the next round starts with `C-TA-METRICS`)

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

### 8. Confirm the TikTok Ads account, video rights and budget cap

Settle which TikTok ad account the round uses, who makes changes, which identity and videos may run, what it can measure, and how much the owner allows to spend, so the test runs on the right account with rights in place and never overspends.

- **C-TIKTOK_ADS-ACCESS.01** Ask the owner for the advertiser ID of the TikTok Ads Manager account and the Business Center it belongs to, if any. Identify the brand by advertiser ID, never by account name.  
  _Done when:_ The advertiser ID, any Business Center, and the owner's confirmation that it belongs to this brand.
- **C-TIKTOK_ADS-ACCESS.02** Decide who makes changes: the owner in their own browser, or the agent's browser if it is already signed in with access to this advertiser ID. The owner signs in themselves; never ask for a password. Note the signed-in user's role; an analyst role can only read.  
  _Done when:_ Who makes changes, the signed-in user, and their role on this ad account.
- **C-TIKTOK_ADS-ACCESS.03** If the owner has no TikTok ad account, the owner creates exactly one on the official TikTok for Business sign-up page. If the owner chooses an address from inbox_address for the sign-up, read the verification code with inbox_latest. Business documents, identity checks and payment details are entered by the owner. Never create extra accounts.  
  _Done when:_ The new advertiser ID and how the sign-up was verified, or a note that an account already existed.
- **C-TIKTOK_ADS-ACCESS.04** Read the account's country, currency, time zone, payment status and account review status. These decide every budget and report in the round. Do not add or change a payment method.  
  _Done when:_ Country, currency, time zone, payment status and review status, as shown in the account.
- **C-TIKTOK_ADS-ACCESS.05** Check the account's existing pixel and events: which events fired in the last 7 days, for example a completed payment or a submitted form, and which one matches the goal's main number. Do not create a new pixel or change the website in this step.  
  _Done when:_ The events that fired in the last 7 days, and the one this goal will be judged on, or 'none'.
- **C-TIKTOK_ADS-ACCESS.06** Decide the identity the ad runs under. For Spark Ads (an existing TikTok post), get the authorization code from the post's creator and write down its expiry date; it must last past the round's end. For any video, confirm the owner has commercial rights to the footage, voices and music, or uses music from TikTok's Commercial Music Library.  
  _Done when:_ The identity, any Spark code expiry date, and a rights note for each video.
- **C-TIKTOK_ADS-ACCESS.07** Ask the owner to write, in this conversation, the most the round may spend per day and in total, in the account currency, and the last day. Check the minimum daily budget TikTok shows for an ad group, and tell the owner if it is above their daily cap.  
  _Done when:_ The owner's written daily cap, total cap and end date, and the minimum daily budget shown.

**Hand back:** `advertiser_id`, `who_changes`, `currency_and_time_zone`, `event_to_judge`, `approved_caps`

**If stuck:**
- `wrong_advertiser`: If the ID belongs to another brand or another Business Center, stop and ask the owner for the exact advertiser ID.
- `analyst_only`: If the signed-in user can only read, set who_changes to 'owner' or ask the owner to change the role themselves.
- `account_under_review`: If the account is under review or needs documents, tell the owner which screen needs them and wait.
- `event_unavailable`: If no event fits the goal, do not invent purchases; use the tracked link and sale counter and tell the owner.
- `spark_permission_expired`: If the Spark code is missing or ends before the round does, use a video the owner has rights to or wait for a new code from the creator.
- `minimum_budget_above_cap`: If TikTok's minimum daily budget is above the owner's cap, show both figures and ask the owner for a new written cap or to skip TikTok.

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

### 10. Make a faceless demo video from real product footage

Produce a finished, playable video that shows the real product working, with subtitles and the right format for the channel, because a clear demo people watch to the end is what moves the goal's main number.

- **S13.01** Write down who the video must convince, the channel and placement, the length, and the shape; for example under 60 seconds and 1080x1920 vertical for short-form, or 16:9 for a longer video.  
  _Done when:_ One line on the viewer and the goal of the video, plus length and size.
- **S13.02** Collect real footage: screen recordings, screenshots, existing videos, music and voice the owner has the right to use. Every feature the video shows needs real footage of the product.  
  _Done when:_ A list of footage with where each piece came from, and any feature still missing footage.
- **S13.03** Turn the approved script into a shot list: a hook in the first 2 seconds, the product being used, the result, and one call to action. Replace any claim you cannot show on screen with one you can.  
  _Done when:_ A shot list where each line names the footage it uses.
- **S13.04** Record missing demo footage only in a demo account or test setup the owner approved, or cut it from existing material. Hide customer names, emails and private data. If a shot needs a real person's face or voice or a change to the live product, list it for the owner and make the rest.  
  _Done when:_ The new footage, checked for private data, and a list of any shots left for the owner.
- **S13.05** Add subtitles that match the script word for word, and a voice-over only with a voice the owner has the right to use. Check every number, product name and spelling in the subtitles.  
  _Done when:_ The subtitle file or burned-in subtitles, checked against the script.
- **S13.06** Edit the full video with footage, subtitles, pacing and an end card that shows the call to action. A script alone is not a finished video. If the only available editing or voice tool charges money, ask the owner before using it.  
  _Done when:_ A video file that plays.
- **S13.07** Play the whole video and check the start, middle and end: sound, subtitles, that each product screen is real, and that no private data or misleading scene appears.  
  _Done when:_ A note that the full video was played, with any fixes made.
- **S13.08** Export the versions each channel needs, checking length, size, shape and file size against the channel's limits. If a file fails, fix and export it again; never hand over the same broken file twice.  
  _Done when:_ Each exported file with its length, pixel size and file size.
- **S13.09** Prepare what publishing needs: a cover image, a title and a caption from the approved copy. If several versions are tested, label them A, B and so on, with one difference between them.  
  _Done when:_ The cover, title and caption for each version, labelled.
- **S13.10** Save the final files with clear names and a note of version, purpose, sources and subtitles, in a place the publishing step can open and upload from.  
  _Done when:_ File paths or links that open and play, with the note for each file.

**Hand back:** `video_files`, `versions`, `sources`, `publish_kit`

**If stuck:**
- `no_real_footage`: If there is no real footage of a feature, ask the owner for a screen recording of it and drop that claim from the video until it arrives.
- `private_data_on_screen`: If any frame shows customer names, emails or other private data, blur or recut it before going further.
- `needs_live_product_change`: If recording would change the live product or real customer data, stop that recording and ask the owner for a safe demo account or existing footage.
- `voice_rights_unclear`: If you cannot confirm the right to use a voice or music track, use subtitles only or a track the owner confirms they may use.
- `export_fails_limits`: If an export is over the channel's length or file size limit, shorten or compress it and check again before handing it over.

### 11. Read this goal's numbers from TikTok Ads (baseline numbers)

Record the exact numbers this goal is judged on, for the period before the round and for the round itself, from TikTok Ads and the owner's own records, so rounds are compared on real numbers. record_numbers lists exactly which numbers it needs.

- **C-TA-METRICS.01** Confirm the advertiser ID, the currency and the time zone. For the baseline, use the same number of days as the round lasts, ending the day before this round's ads are switched on, and count the account's existing campaigns. For the current reading, use the days since this round's ads were switched on and count only this round's campaign. Use the same event, click figure and qualification rule for both. If you cannot open the ad account's reporting, ask the owner for an export or screenshot.  
  _Done when:_ Advertiser ID, the campaigns counted, date range with time zone, currency, and how the numbers will be obtained.
- **C-TA-METRICS.02** Check which components record_numbers asks for and use those exact names. Goals that use this step ask for: spend_minor and attributed_conversions (cost per conversion), spend_minor and qualified_leads (cost per qualified lead), or link_clicks and impressions (link click rate).  
  _Done when:_ The list of component names this goal needs, copied from record_numbers.
- **C-TA-METRICS.03** Read spend for the range and convert it to the currency's smallest unit without rounding. Example: US$12.34 is 1234. For a currency shown without decimals, such as JPY, use the figure as shown. Never convert to another currency.  
  _Done when:_ Spend as shown, and the same figure in the smallest unit.
- **C-TA-METRICS.04** Read impressions and link clicks. Record only clicks that went to the destination link, not all clicks on the ad such as profile visits or likes, and use the same click figure in baseline and current. If the report shows only one click figure, say which kind it is. Compare it with the tracked link's own click count as a check and report both.  
  _Done when:_ Impressions, destination clicks, the tracked link's click count, and which figure was recorded.
- **C-TA-METRICS.05** For conversions, count only the event agreed for this goal and note the attribution window the report uses. Conversions can arrive days late; if the range ended less than 3 days ago, say in source that the number is early. Check purchases against the owner's payment records or the sale counter, count each order once, and leave out the owner's, test and refunded orders.  
  _Done when:_ The event name, attribution window, count, the payment record check, and whether it is early.
- **C-TA-METRICS.06** For qualified leads, use the qualification rule agreed for this goal, for example 'business owner in the target country who left a working email'; if none was written, write one with the owner before counting and keep it for every round. Count each person once from the lead form responses, the owner's lead list, or a CRM if the owner already uses a CRM. Leave out the owner, tests, duplicates and spam.  
  _Done when:_ The qualification rule, the count, and what was left out.
- **C-TA-METRICS.07** Call record_numbers with each component's exact name, its value, and a source naming the report or export, the advertiser ID, the date range and the time zone. If there is no history, record 0 and say 'no history' in source. Never estimate. Do not change any ad or budget in this step.  
  _Done when:_ The record_numbers call with names, values and sources.

**If stuck:**
- `cannot_open_reporting`: If you cannot open the ad account's reporting, ask the owner for an export or screenshot covering the exact date range.
- `no_history`: If the account has no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.
- `event_unavailable`: If the agreed event recorded nothing or does not exist, use the payment records, lead list or sale counter and say so; never invent purchases.
- `conversions_still_arriving`: If the range ended less than 3 days ago, record the numbers as early and read them again after 3 days.
- `numbers_from_wrong_account`: If the screen or export shows a different advertiser ID, do not use those numbers and ask again.
- `clicks_do_not_match`: If destination clicks and the tracked link's clicks differ by more than half, still record TikTok's destination clicks and report both figures in source.

### 12. Build the TikTok video ad as a switched-off draft

Create this round's TikTok campaign, ad group and video ad, switched off, exactly as the owner approved, so it can be switched on later with no surprises in budget, wording, rights or link.

- **C-TA-DRAFT.01** Before building, check again: the advertiser ID, the identity (Spark code valid past the round's end, or the account's own identity), the rights note for each video, and the owner's written daily cap, total cap and end date. If any cap is missing, stop.  
  _Done when:_ Advertiser ID, identity, rights note, and caps quoted from the owner's message.
- **C-TA-DRAFT.02** Check each video: vertical, the first two seconds show the buyer's situation, captions readable without sound, and length and file size within the limits the upload screen shows. If you test more than one video, change only the first two seconds between them.  
  _Done when:_ Each video file with its length, orientation, opening line, and what differs between versions.
- **C-TA-DRAFT.03** Plan the structure: one new campaign with the objective that matches the goal's main number, using the names the objective list shows: traffic for link clicks, lead generation for leads, website conversions or sales for purchases. A purchase objective needs the event chosen in the account step; if there is none, use traffic. One ad group with locations and language from the buyer segments, a daily budget no higher than the owner's cap, and a schedule ending on the round's last day. Do not copy settings from another platform.  
  _Done when:_ A written plan of objective, ad group targeting, budget and schedule.
- **C-TA-DRAFT.04** Write the ad text from the approved copy, under 100 characters, and pick one call-to-action button; a Spark Ad uses the post's own caption instead. Set the destination to the round's tracked link with ?v=A, ?v=B per video. Open the link and see the product page load. No invented numbers, testimonials, scarcity or guarantees.  
  _Done when:_ Ad text with character count, the button, and each destination URL confirmed to load.
- **C-TA-DRAFT.05** Show the owner word for word: each video, ad text, button, destination URL, objective, locations, daily budget and schedule. Get a clear yes before creating anything.  
  _Done when:_ The full draft as shown to the owner and their approval message.
- **C-TA-DRAFT.06** Create only this round's campaign, ad group and ads so that nothing can spend yet: set the ad group's schedule to start on a future day, and switch the campaign off before submitting if the screen allows it, otherwise right after submitting. Use the owner's browser, or the agent's own browser if the owner said yes. Touch nothing that already exists, and check the campaign list before any retry so nothing is created twice.  
  _Done when:_ The names and IDs of the new campaign, ad group and ads, that the campaign is off, and the schedule start as set.
- **C-TA-DRAFT.07** Open the draft again and check: campaign off, daily budget, currency, schedule, identity, destination URLs, video processing and review status. A processed or approved video is not live. If review is pending, keep the same ad ID and wait. If rejected, read the reason and fix only that part with the owner's yes.  
  _Done when:_ Each setting as it appears in the account, and each ad's review status.

**Hand back:** `campaign_id`, `ad_ids`, `daily_budget`, `destination_urls`, `review_status`

**If stuck:**
- `no_written_caps`: If the owner has not written a daily cap, total cap and end date, stop and ask for them before building.
- `owner_has_not_approved`: If the owner has not said yes to this exact draft, do not create it; show it and wait.
- `spark_permission_expired`: If the Spark code has expired or ends before the round, stop that ad and use a video the owner has rights to, or wait for a new code.
- `video_review_pending`: If an ad is still in review, keep its ad ID and check again later; never create a second copy of the same ad.
- `ad_rejected`: If an ad is rejected, read the stated reason and fix only that part with the owner's yes; if the product itself must change, stop that ad.
- `no_video_rights`: If the owner cannot confirm rights to a video's footage, voices or music, leave that video out.

### 13. Switch on only this round's TikTok ads, within the approved cap

Turn on only the approved switched-off campaign, at a budget the owner wrote down, so real viewers see the video and the goal's main number gets new data without risking more money than allowed.

- **C-TA-ACTIVATE.01** Open the draft and confirm the advertiser ID and the campaign, ad group and ad IDs from the draft step. These are the only items this step may switch on. Check that any Spark code is still valid past the round's end.  
  _Done when:_ The list of IDs to switch on, matching the draft step, and the Spark code expiry if used.
- **C-TA-ACTIVATE.02** Check the money against the owner's written caps: the daily budget is at or below the daily cap, the daily budget times the number of days is at or below the total cap, and the schedule ends on the round's last day. A zero or missing cap means do not switch on.  
  _Done when:_ Daily budget, number of days, planned total, end date, and the owner's caps side by side.
- **C-TA-ACTIVATE.03** Check each ad's review status. If it is still in review, wait and check again; never edit or copy an ad to get around review. If it is rejected, go back to the draft step.  
  _Done when:_ Each ad's review status at the time of the check.
- **C-TA-ACTIVATE.04** Ask the owner for a yes in this conversation to switch on now, stating the campaign name, daily budget, total cap and end date.  
  _Done when:_ The owner's message saying yes to these exact figures.
- **C-TA-ACTIVATE.05** Switch on only this round's campaign, ad group and ads, and move the schedule start to today if it was set in the future. Do not switch on any other item, raise any budget, or turn on automatic budget increases.  
  _Done when:_ The time the campaign was switched on and who switched it on.
- **C-TA-ACTIVATE.06** Within 3 hours, check the status and whether impressions have started. Then check spend once a day: it must stay under the daily cap, and when total spend comes within one daily budget of the total cap, run the stop step. If an ad shows as not delivering, write down the reason TikTok gives.  
  _Done when:_ Status, impressions, daily spend and total spend at each check, with the times read.
- **C-TA-ACTIVATE.07** Write down the stop date and total cap, and plan the stop step for whichever comes first, or the Spark code's expiry if that is sooner. Hand back the ad IDs, destination URLs, and an ad preview link or screenshot.  
  _Done when:_ The stop date, the planned stop trigger, and the ad IDs with preview link or screenshot.

**Hand back:** `switched_on_ids`, `live_since`, `delivery_status`, `stop_plan`

**If stuck:**
- `owner_has_not_approved`: If the owner has not said yes to switching on at these figures, do not switch on; ask and wait.
- `budget_over_cap`: If the daily budget or planned total is above the owner's cap, lower the budget to fit or ask the owner for a new written cap.
- `video_review_pending`: If an ad is still in review, keep the same ad ID and check again later; never create a copy to skip review.
- `spark_permission_expired`: If the Spark code has expired, leave that ad off and use a video the owner has rights to, or wait for a new code.
- `payment_problem`: If TikTok shows a payment problem, stop and tell the owner which screen needs them; never touch payment details.
- `not_delivering`: If there are no impressions after 24 hours, read the reason TikTok shows and report it; do not raise the budget.

### 14. Read this goal's numbers from TikTok Ads (result numbers)

Record the exact numbers this goal is judged on, for the period before the round and for the round itself, from TikTok Ads and the owner's own records, so rounds are compared on real numbers. record_numbers lists exactly which numbers it needs.

- **C-TA-METRICS.01** Confirm the advertiser ID, the currency and the time zone. For the baseline, use the same number of days as the round lasts, ending the day before this round's ads are switched on, and count the account's existing campaigns. For the current reading, use the days since this round's ads were switched on and count only this round's campaign. Use the same event, click figure and qualification rule for both. If you cannot open the ad account's reporting, ask the owner for an export or screenshot.  
  _Done when:_ Advertiser ID, the campaigns counted, date range with time zone, currency, and how the numbers will be obtained.
- **C-TA-METRICS.02** Check which components record_numbers asks for and use those exact names. Goals that use this step ask for: spend_minor and attributed_conversions (cost per conversion), spend_minor and qualified_leads (cost per qualified lead), or link_clicks and impressions (link click rate).  
  _Done when:_ The list of component names this goal needs, copied from record_numbers.
- **C-TA-METRICS.03** Read spend for the range and convert it to the currency's smallest unit without rounding. Example: US$12.34 is 1234. For a currency shown without decimals, such as JPY, use the figure as shown. Never convert to another currency.  
  _Done when:_ Spend as shown, and the same figure in the smallest unit.
- **C-TA-METRICS.04** Read impressions and link clicks. Record only clicks that went to the destination link, not all clicks on the ad such as profile visits or likes, and use the same click figure in baseline and current. If the report shows only one click figure, say which kind it is. Compare it with the tracked link's own click count as a check and report both.  
  _Done when:_ Impressions, destination clicks, the tracked link's click count, and which figure was recorded.
- **C-TA-METRICS.05** For conversions, count only the event agreed for this goal and note the attribution window the report uses. Conversions can arrive days late; if the range ended less than 3 days ago, say in source that the number is early. Check purchases against the owner's payment records or the sale counter, count each order once, and leave out the owner's, test and refunded orders.  
  _Done when:_ The event name, attribution window, count, the payment record check, and whether it is early.
- **C-TA-METRICS.06** For qualified leads, use the qualification rule agreed for this goal, for example 'business owner in the target country who left a working email'; if none was written, write one with the owner before counting and keep it for every round. Count each person once from the lead form responses, the owner's lead list, or a CRM if the owner already uses a CRM. Leave out the owner, tests, duplicates and spam.  
  _Done when:_ The qualification rule, the count, and what was left out.
- **C-TA-METRICS.07** Call record_numbers with each component's exact name, its value, and a source naming the report or export, the advertiser ID, the date range and the time zone. If there is no history, record 0 and say 'no history' in source. Never estimate. Do not change any ad or budget in this step.  
  _Done when:_ The record_numbers call with names, values and sources.

**If stuck:**
- `cannot_open_reporting`: If you cannot open the ad account's reporting, ask the owner for an export or screenshot covering the exact date range.
- `no_history`: If the account has no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.
- `event_unavailable`: If the agreed event recorded nothing or does not exist, use the payment records, lead list or sale counter and say so; never invent purchases.
- `conversions_still_arriving`: If the range ended less than 3 days ago, record the numbers as early and read them again after 3 days.
- `numbers_from_wrong_account`: If the screen or export shows a different advertiser ID, do not use those numbers and ask again.
- `clicks_do_not_match`: If destination clicks and the tracked link's clicks differ by more than half, still record TikTok's destination clicks and report both figures in source.

### 15. Pause only this round's TikTok ads and close the round

Switch off exactly the campaign this round switched on, confirm spending has stopped, and record the final spend, so the round's result is clean and no money leaks after the test.

- **C-TA-STOP.01** Take the list of IDs from the switch-on step. This list is the only thing this step may switch off. Never use 'all active campaigns' as the list.  
  _Done when:_ The campaign, ad group and ad IDs this round switched on.
- **C-TA-STOP.02** Confirm why the round ends: the end date arrived, the total cap was reached, the Spark code expired, or the owner asked. Make sure the current numbers were read for the full window before pausing; if not, read spend, clicks and conversions now.  
  _Done when:_ The reason the round ends, and the time the current numbers were read.
- **C-TA-STOP.03** Save the ads as they ran: video files, ad text, button, targeting, budget and destination URLs, so the next round can change one thing from a known start.  
  _Done when:_ A saved copy of the round's ads and settings.
- **C-TA-STOP.04** Tell the owner which items will be switched off, by name and ID. If the owner wants to keep them running, stop here and ask for a new written daily cap, total cap and end date.  
  _Done when:_ The message to the owner listing the items to switch off, and their answer.
- **C-TA-STOP.05** Switch off only those IDs. Do not delete any campaign, do not touch other campaigns or brands, and do not change payment settings.  
  _Done when:_ The time each item was switched off and who did it.
- **C-TA-STOP.06** Open the account again and confirm each item shows as off and not delivering. Compare spend at the time of pausing with spend 24 hours later; new impressions should stop. If the status did not change, check again before trying a second time.  
  _Done when:_ Status of each item and spend at pause time and 24 hours later.
- **C-TA-STOP.07** Record the final spend in the currency's smallest unit and write the one change the next round will test, for example a new first two seconds. The next round starts from a new draft; pausing never extends the budget or the owner's approval.  
  _Done when:_ Final spend in the smallest unit and the next round's single change.

**Hand back:** `paused_ids`, `paused_at`, `final_spend_minor`, `next_change`

**If stuck:**
- `ids_unknown`: If you do not have the IDs from the switch-on step, find the round's campaign by its exact name and creation date and confirm it with the owner before switching anything off.
- `pause_not_taking`: If the status does not show off, wait 15 minutes and check again before retrying; tell the owner if it still runs.
- `owner_wants_to_continue`: If the owner wants the ads to keep running, ask for a new written daily cap, total cap and end date before doing anything.
- `spend_after_pause`: If spend keeps rising 24 hours after the pause, check the status of every item and tell the owner the exact figures.
- `wrong_account`: If the signed-in account shows a different advertiser ID, stop and switch to the agreed account before pausing anything.
