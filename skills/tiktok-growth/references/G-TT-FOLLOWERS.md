# TikTok: grow net followers with short videos

- **Goal id:** `G-TT-FOLLOWERS`
- **Language:** English
- **Channel:** tiktok
- **Metric:** `net_followers` = `followers`, should increase
- **Observation window:** 48 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), content (the next round starts with `C-TT-RESEARCH`), link_eligibility (the next round starts with `C-TIKTOK-ACCESS`), data (the next round starts with `C-TT-METRICS`)

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

### 8. Confirm the TikTok account, who posts, and the link option

Settle which TikTok account will post, who presses post, whether the profile can show a clickable website link, and which numbers can be read, so videos go out under the right brand and the goal's number can be measured.

- **C-TIKTOK-ACCESS.01** Ask the owner for the URL of the TikTok profile that will post and the brand's website. Open the profile as a public page and confirm it exists and belongs to the brand. If it exists, use it and do not create a second account.  
  _Done when:_ The profile URL, the handle, and the owner's confirmation that it is theirs.
- **C-TIKTOK-ACCESS.02** Decide who presses post: the owner in the TikTok app, or the agent's own browser if it is already signed in to that account and the owner agrees. Some TikTok features work only in the app, so the owner may need to do those parts. Never ask for a password, and do not reuse another brand's signed-in session.  
  _Done when:_ Who will post, and which parts the owner must do in the app.
- **C-TIKTOK-ACCESS.03** If the owner asked for a new account, the owner signs up on the official TikTok screen with their real details. If an email code is needed, the agent may give an address from inbox_address and read the code with inbox_latest. Phone checks, QR confirmations, and puzzles are for the owner. Create one real account only.  
  _Done when:_ How sign-in or sign-up was done, which steps the owner handled, and the resulting handle.
- **C-TIKTOK-ACCESS.04** Check the account type, the country or region it is set to, and whether the profile can show a clickable website link right now. Do not assume every account has this, because it differs by account type and region. Do not switch the account type or fill in business details to get a link unless the owner asks and the details are true.  
  _Done when:_ The account type, the region, and a yes or no on whether a clickable website link can be added.
- **C-TIKTOK-ACCESS.05** If a website link is available, plan to put the round's tracked link in the profile, with the owner's approval of the change. If it is not available, tell the owner that clicks and sales from TikTok cannot be tracked through the profile this round, and focus on video numbers.  
  _Done when:_ The planned profile link, or a note that no clickable link is available and what that means for measurement.
- **C-TIKTOK-ACCESS.06** Check the sound and footage rights for the planned videos. Business accounts can use only sounds cleared for commercial use, so prefer original audio. Read the current length and size limits on the upload screen instead of assuming them.  
  _Done when:_ The sound and footage source for each planned video, marked original or cleared, and the limits shown on the upload screen.
- **C-TIKTOK-ACCESS.07** Check which numbers the account's analytics shows, such as video views, average watch time, full-watch share, profile views, and followers, and the time zone it uses. If analytics is off or empty, note that it may only fill in after the first post and a day or two of delay.  
  _Done when:_ A list of numbers that can be read, the time zone, and how they will be obtained.

**Hand back:** `account_handle`, `profile_url`, `who_publishes`, `profile_link`, `numbers_visible`

**If stuck:**
- `bio_link_ineligible`: If the profile cannot show a clickable website link, do not treat plain text in the bio as a trackable link; tell the owner and measure video numbers only.
- `owner_action_needed`: If TikTok asks for a phone check, QR confirmation, puzzle, or terms, stop and tell the owner exactly which screen needs them, then resume where you stopped.
- `music_not_licensed`: If a planned sound is not cleared for commercial use, switch to original audio or a cleared sound before the video is made.
- `web_mobile_difference`: If a feature exists only in the app, write down the exact step for the owner to do on their phone; never describe a web button you have not seen.
- `analytics_not_ready`: If analytics shows nothing yet, note it and plan to read numbers after the first video has been live for at least 48 hours.
- `handle_not_the_brand`: If the signed-in account is a personal account or another brand, stop before any posting and ask the owner which account to use.

### 9. Study TikTok openings and calls to action that fit the buyer

Find how real TikTok videos about the buyer's problem open and end, and turn that into one opening or call-to-action test, because the first seconds and the ending decide whether viewers keep watching, follow, or click.

- **C-TT-RESEARCH.01** Turn the chosen angle and buyer quotes into three to five TikTok search phrases, such as '<situation> tutorial', '<problem> review', or '<category> alternative'. Search with web search, read_page, or the agent's browser.  
  _Done when:_ The search phrases and the date they were searched.
- **C-TT-RESEARCH.02** Collect at least ten videos from the last 90 days that speak to the buyer's problem. Choose them for the problem they address, not for a trending sound. Write down the URL, the author, and the posting date, or 'unknown'.  
  _Done when:_ A list of at least ten video URLs with author and date or 'unknown'.
- **C-TT-RESEARCH.03** For each video, write a short note on the first three seconds: the first image, the on-screen text, and the first spoken line. Also note the length, the pace, whether captions are on screen, and how it ends. Paraphrase; quote no more than a few words.  
  _Done when:_ A note per video covering the opening, length, pace, captions, and ending.
- **C-TT-RESEARCH.04** Read the comments and copy up to three real viewer questions or objections per video word for word. Skip comments from the creator and obvious spam.  
  _Done when:_ Viewer questions and objections, each with the video URL it came from.
- **C-TT-RESEARCH.05** Record only the numbers shown publicly, such as views, likes, and comments. Profile visits, link clicks, and site visits are not public, so leave them empty and never guess them. Do not treat views as sales.  
  _Done when:_ The public numbers per video, with private numbers left empty.
- **C-TT-RESEARCH.06** Pick one thing for the next video to test, either the opening or the call to action, and write versions A and B that differ only in that thing. Choose the opening when the goal's main number depends on watching or following, and the call to action when it depends on profile visits, clicks, or sales.  
  _Done when:_ The single thing tested, versions A and B, and the videos or viewer quotes each draws on.
- **C-TT-RESEARCH.07** Take from the account step whether the profile can show a clickable website link. If it cannot, the call to action must not say 'link in bio', the test should aim at video numbers or profile visits only, and the plan must not claim website sales can be measured.  
  _Done when:_ A note on whether a link is available and how the call to action was adjusted.

**Hand back:** `videos_studied`, `openings_found`, `viewer_questions`, `test_plan`

**If stuck:**
- `too_few_relevant_videos`: If fewer than ten relevant videos turn up, widen the search phrases to the buyer's wider situation or extend the date range to 180 days, and say so.
- `cannot_open_tiktok_pages`: If TikTok pages will not open for the agent, ask the owner to share five to ten video links they find relevant, and study those.
- `bio_link_ineligible`: If the profile cannot show a clickable link, drop 'link in bio' from every call to action and test openings or profile visits instead.
- `music_not_licensed`: If a pattern depends on a sound the brand cannot use commercially, note it and plan the test with original audio.
- `no_buyer_problem_match`: If the videos found do not match the buyer's problem, go back to the buyer quotes and rewrite the search phrases before collecting more.

### 10. Write the post from proven facts

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

### 11. Make a faceless demo video from real product footage

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

### 12. Read this goal's numbers on TikTok (baseline numbers)

Record the numbers this goal is judged on, for the account's videos before and after the new video, so rounds are compared on real numbers from video to profile to website to sale. record_numbers lists exactly which numbers it needs.

- **C-TT-METRICS.01** Confirm the TikTok handle, which videos you are measuring, the date range, and the time zone. For a baseline, use the account's recent videos over a range of the same length as this round; for current, use this round's video URL over this round's range. Note whether the profile has a clickable website link.  
  _Done when:_ The handle, the video URLs, the date range with time zone, and whether a profile link exists.
- **C-TT-METRICS.02** Pass only this goal's metric components, by these exact names: followers for net followers; completed_views and video_starts for completion rate; profile_visits and video_views for profile visit rate; website_clicks and profile_visits for profile link rate; external_purchases and attributed_sessions for site purchase rate. Decide where each is read before reading anything, and never borrow a number from another goal.  
  _Done when:_ A list of each component name and the source it will be read from.
- **C-TT-METRICS.03** Open the video's analytics and the account's analytics, or ask the owner for screenshots if you cannot, and read the numbers exactly as displayed. video_views and video_starts are the views TikTok shows for the video. If full watches are shown only as a percentage, multiply it by the views on the same screen, round down, and say so in source. For followers, record the net change in the range, the end count minus the start count, and say so in source.  
  _Done when:_ The numbers as displayed, the screen they came from, and the time they were read.
- **C-TT-METRICS.04** Keep each stage separate: video views are not profile visits, profile visits are not website clicks, and website clicks are not site visits. Read website_clicks from the round's tracked link, split by ?v= label if there are versions. If the baseline period had no tracked link, read website clicks for both baseline and current from TikTok's analytics and give the tracked-link count in source as a cross-check.  
  _Done when:_ Each stage's number with its own source, and no stage filled in from another.
- **C-TT-METRICS.05** Read attributed_sessions from the owner's site analytics with TikTok as the source; if there is none, use clicks on the round's tracked link and say in source that these are clicks, not sessions. Read external_purchases from the sale counter or payment records, count each paid order once, and leave out refunds and the owner's own test payments. Do not add new tracking code.  
  _Done when:_ Site visit and purchase counts with their sources, and any orders excluded and why.
- **C-TT-METRICS.06** If the account has no history for a number, record 0 and say in source that there is no history. If TikTok does not show a number, write 'not shown' and never estimate it. If the video is less than 48 hours old, label the numbers early and read again later.  
  _Done when:_ Each zero or missing number with its reason.
- **C-TT-METRICS.07** Call record_numbers with each component by its exact name and a source naming the screen, screenshot, link, or record and the time read. If a rate's bottom number is 0, still record both numbers and do not claim any improvement.  
  _Done when:_ The record_numbers call with every component, its value, and its source.

**If stuck:**
- `cannot_open_analytics`: If you cannot open TikTok's analytics, ask the owner for screenshots of the video's and the account's analytics for the exact date range.
- `analytics_not_ready`: If analytics is empty or the video is less than 48 hours old, label any numbers early and read them again after the delay.
- `no_history`: If the account has no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.
- `numbers_from_wrong_account`: If a screenshot shows a different handle or other videos, do not use those numbers and ask again.
- `bio_link_ineligible`: If the profile has no clickable link, record website clicks and site visits from TikTok as 'not available' in source and do not estimate them.
- `purchase_source_missing`: If there is no sale counter, site analytics, or payment record, say so in source and do not count any purchases.

### 13. Publish one TikTok video and confirm it

Publish the approved vertical video once, under the right account and with the right cover, caption, and profile link, and hand back its public URL, because the video must be live exactly as approved before its numbers can be read.

- **C-TT-VIDEO.01** Open the final video file and check it: vertical 9:16, the opening hook shows in the first two seconds, on-screen captions are readable, a cover frame is chosen, and the sound is original or cleared for commercial use. Check its length against the limit shown on TikTok's upload screen.  
  _Done when:_ The file name, length, cover frame, and sound source, with each check passed.
- **C-TT-VIDEO.02** Confirm the handle about to post is the agreed one, and look through its last ten videos so you do not repeat the same opening or caption.  
  _Done when:_ The handle and a note on the recent videos you checked.
- **C-TT-VIDEO.03** Write the caption: one line on the viewer's situation, one true benefit, and a call to action, aiming for under 300 characters with no more than five relevant hashtags. Links in captions are not clickable, so point to the profile link only if the profile has one. Use only claims the product facts support.  
  _Done when:_ The caption text, its character count, and the facts it relies on.
- **C-TT-VIDEO.04** If the profile can show a website link, prepare the round's tracked link for it, with ?v=A or ?v=B if this round runs one version at a time. Open the link and check it lands on the product page. One profile link carries one label, so when two versions run at the same time, compare them on each video's own numbers instead. Do not change the profile yet.  
  _Done when:_ The profile link as it will appear, opened and confirmed to load, or a note that no link is available.
- **C-TT-VIDEO.05** Show the owner the video, the cover, the caption word for word, and any profile link change, and get a clear yes before anything goes public.  
  _Done when:_ The exact material shown to the owner and their approval quoted word for word.
- **C-TT-VIDEO.06** Make the approved profile link change, then upload the video once. The agent does this only if its own browser is signed in to the agreed account and the owner said yes; otherwise the owner does it from the app using the approved files and caption. If the upload is still processing, wait and do not upload again.  
  _Done when:_ Who changed the link and posted, the date and time, and any processing or review status shown.
- **C-TT-VIDEO.07** Once the video is public, open its URL and read back the caption, the handle, the cover, and that captions show on screen. A video still under review is not live. If posting seemed to fail, check the profile before trying again so nothing is posted twice.  
  _Done when:_ The public video URL, the caption as it appears there, and the handle.

**Hand back:** `video_url`, `published_caption`, `profile_link`, `posted_at`

**If stuck:**
- `owner_has_not_approved`: If the owner has not said yes to this exact video, cover, and caption, do not post; show them the material and stop until they answer.
- `wrong_account_signed_in`: If the signed-in account is not the agreed handle, stop and ask the owner to switch accounts or to post it themselves.
- `music_not_licensed`: If the sound is not original or cleared for commercial use, replace it before posting and show the owner the new version.
- `video_processing`: If the video is still processing or in review, wait and check its status again later; never upload the same video twice.
- `web_mobile_difference`: If posting or setting the cover works only in the app, give the owner the files, caption, and exact steps, and ask them to send back the video URL.
- `bio_link_ineligible`: If the profile cannot show a clickable link, remove 'link in bio' from the caption and post with a call to follow or visit the profile instead.

### 14. Read this goal's numbers on TikTok (result numbers)

Record the numbers this goal is judged on, for the account's videos before and after the new video, so rounds are compared on real numbers from video to profile to website to sale. record_numbers lists exactly which numbers it needs.

- **C-TT-METRICS.01** Confirm the TikTok handle, which videos you are measuring, the date range, and the time zone. For a baseline, use the account's recent videos over a range of the same length as this round; for current, use this round's video URL over this round's range. Note whether the profile has a clickable website link.  
  _Done when:_ The handle, the video URLs, the date range with time zone, and whether a profile link exists.
- **C-TT-METRICS.02** Pass only this goal's metric components, by these exact names: followers for net followers; completed_views and video_starts for completion rate; profile_visits and video_views for profile visit rate; website_clicks and profile_visits for profile link rate; external_purchases and attributed_sessions for site purchase rate. Decide where each is read before reading anything, and never borrow a number from another goal.  
  _Done when:_ A list of each component name and the source it will be read from.
- **C-TT-METRICS.03** Open the video's analytics and the account's analytics, or ask the owner for screenshots if you cannot, and read the numbers exactly as displayed. video_views and video_starts are the views TikTok shows for the video. If full watches are shown only as a percentage, multiply it by the views on the same screen, round down, and say so in source. For followers, record the net change in the range, the end count minus the start count, and say so in source.  
  _Done when:_ The numbers as displayed, the screen they came from, and the time they were read.
- **C-TT-METRICS.04** Keep each stage separate: video views are not profile visits, profile visits are not website clicks, and website clicks are not site visits. Read website_clicks from the round's tracked link, split by ?v= label if there are versions. If the baseline period had no tracked link, read website clicks for both baseline and current from TikTok's analytics and give the tracked-link count in source as a cross-check.  
  _Done when:_ Each stage's number with its own source, and no stage filled in from another.
- **C-TT-METRICS.05** Read attributed_sessions from the owner's site analytics with TikTok as the source; if there is none, use clicks on the round's tracked link and say in source that these are clicks, not sessions. Read external_purchases from the sale counter or payment records, count each paid order once, and leave out refunds and the owner's own test payments. Do not add new tracking code.  
  _Done when:_ Site visit and purchase counts with their sources, and any orders excluded and why.
- **C-TT-METRICS.06** If the account has no history for a number, record 0 and say in source that there is no history. If TikTok does not show a number, write 'not shown' and never estimate it. If the video is less than 48 hours old, label the numbers early and read again later.  
  _Done when:_ Each zero or missing number with its reason.
- **C-TT-METRICS.07** Call record_numbers with each component by its exact name and a source naming the screen, screenshot, link, or record and the time read. If a rate's bottom number is 0, still record both numbers and do not claim any improvement.  
  _Done when:_ The record_numbers call with every component, its value, and its source.

**If stuck:**
- `cannot_open_analytics`: If you cannot open TikTok's analytics, ask the owner for screenshots of the video's and the account's analytics for the exact date range.
- `analytics_not_ready`: If analytics is empty or the video is less than 48 hours old, label any numbers early and read them again after the delay.
- `no_history`: If the account has no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.
- `numbers_from_wrong_account`: If a screenshot shows a different handle or other videos, do not use those numbers and ask again.
- `bio_link_ineligible`: If the profile has no clickable link, record website clicks and site visits from TikTok as 'not available' in source and do not estimate them.
- `purchase_source_missing`: If there is no sale counter, site analytics, or payment record, say so in source and do not count any purchases.
