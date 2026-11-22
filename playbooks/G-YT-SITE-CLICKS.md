# YouTube: raise link clicks from video descriptions

- **Goal id:** `G-YT-SITE-CLICKS`
- **Language:** English
- **Channel:** youtube
- **Metric:** `link_rate` = `link_clicks` / `views`, should increase
- **Observation window:** 168 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), content (the next round starts with `A-ANGLES`), format (the next round starts with `S13`), data (the next round starts with `C-YT-METRICS`)

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

### 8. Confirm the YouTube channel and who publishes

Settle which YouTube channel this round uses, who signs in and who presses publish or reply, and which features the channel can use, so the round's videos or replies go out under the right brand without stopping halfway.

- **C-YOUTUBE-ACCESS.01** Ask the owner for the URL of the YouTube channel this round will use. Open it as a public page and write down the handle and the channel ID (the part starting with 'UC' in a /channel/ URL, or the ID shown in the channel's About details). Go by the channel ID, not the display name, because several channels can share a name.  
  _Done when:_ The channel URL, handle and channel ID, opened as a public page.
- **C-YOUTUBE-ACCESS.02** Ask the owner which Google account manages that channel. If the channel belongs to a brand account, the owner must switch to that channel in the account menu; being signed in to Gmail does not mean you are acting as the channel. The owner signs in on the official Google page and does any two-step verification. Never ask for a password.  
  _Done when:_ The Google account that manages the channel, and the owner's confirmation that the right channel is selected.
- **C-YOUTUBE-ACCESS.03** Decide who publishes or replies: the owner on their own device, or the agent's own browser if it is already signed in as that channel. Have whoever publishes open YouTube Studio for this channel and check the channel name and picture at the top match the brand.  
  _Done when:_ Who will publish, and a note or screenshot showing YouTube Studio open on the right channel.
- **C-YOUTUBE-ACCESS.04** List what this round needs (upload a video, reply to comments, read analytics, a clickable link in a description) and check each one for this channel. Videos longer than 15 minutes and custom thumbnails need YouTube's extra features, which are usually unlocked by verifying the channel with a phone number; check the channel's feature eligibility in YouTube Studio settings. Links in Shorts descriptions and comments are not clickable, so a link-click goal needs a long video.  
  _Done when:_ A short list of the actions this round needs, each marked 'works', 'needs the owner' or 'not available', with the reason.
- **C-YOUTUBE-ACCESS.05** Create a new channel only if the owner asked for one in this conversation, with a name and handle the owner approved. The owner creates it from their own Google account, or the agent does it in a browser already signed in to that account after the owner says yes. Use one real account only, never extra or fake channels. If a new Google account is truly needed and the owner agrees, you may use inbox_address and read the verification code with inbox_latest; phone verification, identity checks and terms are left to the owner.  
  _Done when:_ The owner's request and the approved channel name, or a note that the existing channel is used.
- **C-YOUTUBE-ACCESS.06** If YouTube asks for a verification code the agent cannot read, a phone check, acceptance of terms or an identity check, stop and tell the owner exactly which screen needs it. Note where you stopped and return to the same channel once they are done.  
  _Done when:_ What the owner needs to do, on which screen, and where to resume, or a note that nothing was needed.
- **C-YOUTUBE-ACCESS.07** Check the channel's comment settings in YouTube Studio: whether comments are on, and whether comments are held for review. Note the time zone the channel's reports use, so later numbers are read for the right days.  
  _Done when:_ The comment setting, the review setting and the report time zone.
- **C-YOUTUBE-ACCESS.08** Finish by opening the public channel page again, and confirm whoever publishes can open the upload screen or the reply box on one of the channel's videos.  
  _Done when:_ Channel URL, handle, confirmation that upload or reply can be started, and the time this was checked.

**Hand back:** `channel_url`, `channel_id`, `who_publishes`, `available_actions`

**If stuck:**
- `wrong_channel_selected`: If the signed-in account is acting as a different channel or a personal channel, stop and ask the owner to switch to the channel with the agreed channel ID.
- `channel_does_not_exist`: If the URL shows no channel, tell the owner; a Google sign-in is not a channel, and a new one is created only if the owner asks.
- `owner_action_needed`: If a phone check, terms screen or identity check appears, stop and tell the owner which screen and which button; never accept terms or verify on their behalf.
- `agent_browser_not_signed_in`: If the agent's browser is not signed in as the right channel, set who_publishes to 'owner' and plan to hand them the final text and files.
- `feature_not_available`: If a needed feature such as clickable links or long uploads is not available, or YouTube limits how much the channel can upload or reply today, say so, change the round to use what works (for example a long video instead of a Short) or wait for the limit to reset, never switch to another channel, and never claim the link drives visits.
- `comments_disabled`: If comments are off on the channel or a video, do not change the setting yourself; tell the owner and leave that video out of any reply work.

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

### 11. Read this goal's numbers on YouTube (baseline numbers)

Record the numbers this goal is judged on, for the same channel and the same length of time before and after the round, so rounds are compared on real YouTube and link numbers. record_numbers lists exactly which numbers it needs.

- **C-YT-METRICS.01** Confirm the channel ID, the videos or comment threads you are measuring, the date range and the time zone. For the baseline use the same number of days just before the round; for the current reading use the round's own days. If you cannot open YouTube Studio analytics, ask the owner for screenshots or the numbers.  
  _Done when:_ Channel ID, video or comment URLs, date range with time zone, and how the numbers will be obtained.
- **C-YT-METRICS.02** Read the numbers exactly as YouTube Studio shows them for those videos and days: views, watch time, average view duration, subscribers gained and subscribers lost. Read Shorts and long videos separately and never add them into one figure without saying so.  
  _Done when:_ The numbers as displayed, split by Shorts and long videos, with the screen they came from and the time they were read.
- **C-YT-METRICS.03** Fill the goal's components by their exact names. For a subscriber goal, 'subscribers' is subscribers gained minus subscribers lost in the range. For a completion goal, 'video_starts' is the views of the measured videos; for 'completed_views', use a count of viewers who reached the end only if YouTube shows one. If it shows only the video's audience retention chart, multiply the views by the percentage still watching at the last moment of the video, round down, use the same method for the baseline and the current reading, and say in source that it was calculated from the retention chart. If the chart cannot be read at the end, leave 'completed_views' out and name it as missing.  
  _Done when:_ Each component name with its number and a one-line note on how it was read.
- **C-YT-METRICS.04** For a link-click goal, take 'link_clicks' from the round's tracked link (from tracking), not from YouTube, and 'views' from YouTube Studio for the same videos and days. Comments and likes never stand in for clicks.  
  _Done when:_ The tracked link's click count and the matching views, each with its source.
- **C-YT-METRICS.05** For a comment-request goal, 'eligible_requests' is the number of different request comments the round replied to, and 'qualified_replies' is the number of those commenters who answered back with a real next step (asked for the link, a price or a demo, or said they will try it). Count each person once, and never count likes or the owner's or the agent's own replies.  
  _Done when:_ Both counts, with the URL of each reply that was counted as qualified.
- **C-YT-METRICS.06** Add website visits or sales only if the owner already has a source for them, such as the tracked link, site analytics or payment records. Where you cannot tell which video or reply led to a visit or a sale, say so plainly.  
  _Done when:_ Each visit or sales figure names its source, and unknown links between video and sale are stated.
- **C-YT-METRICS.07** Pass the goal's exact component names to record_numbers with the source of each. If there is no history, record 0 and say in source that there is no history. Never estimate a missing number; leave it out and name it as missing.  
  _Done when:_ The record_numbers entry with every component, its source, and any missing number named.

**If stuck:**
- `cannot_open_analytics`: If you cannot open YouTube Studio analytics for this channel, ask the owner for screenshots of the screens that show the numbers this goal needs.
- `numbers_from_wrong_channel`: If a screen or screenshot shows a different channel from the agreed channel ID, do not use those numbers and ask again.
- `no_history`: If the channel has no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.
- `link_clicks_not_tracked`: If the description had no tracked link, say that link clicks cannot be read for this round, record nothing for clicks, and make sure the next round uses the tracked link.
- `too_early_to_read`: If the videos or replies are less than 48 hours old, YouTube figures may still be filling in; report the numbers as early and read them again later.

### 12. Upload the approved video to the right YouTube channel

Upload and publish the approved video or Short once, on the brand's own channel, with honest settings and the tracked link, and hand back its public URL, because only a live, correctly set video can move the goal's main number.

- **C-YT-VIDEO.01** Ask the owner for the URL of the brand's YouTube channel. The owner signs in to Google themselves. In YouTube Studio, confirm the channel selected is that brand channel and not a personal one.  
  _Done when:_ The channel URL, the channel name shown in YouTube Studio, and who will upload.
- **C-YT-VIDEO.02** Check the video file. A Short is vertical and up to 3 minutes; a regular video is usually horizontal. Confirm with the owner that they own or have licensed all footage, music and images in it.  
  _Done when:_ The file name, its length and shape, and the owner's confirmation of rights.
- **C-YT-VIDEO.03** Write the title (under 100 characters) and description (under 5,000 characters). Put the round's tracked link in the first two lines of the description; if there are two versions of the video, use ?v=A and ?v=B. Prepare a thumbnail for a regular video and a captions file if one exists.  
  _Done when:_ The title and description with character counts, the link with its version label, and the thumbnail and captions files if any.
- **C-YT-VIDEO.04** Check every claim in the title, description and video against the product fact sheet; remove anything you cannot support.  
  _Done when:_ A list of the claims in the video and text, each with its fact source.
- **C-YT-VIDEO.05** Ask the owner the required answers: whether the video is made for kids, whether it contains realistic altered or synthetic content if YouTube Studio asks, and whether it includes paid promotion. Never guess these answers.  
  _Done when:_ The owner's answer to each required setting.
- **C-YT-VIDEO.06** Show the owner the title, description, thumbnail, settings and the planned visibility (public now or scheduled) and get a clear yes.  
  _Done when:_ Everything that will go live, and the owner's approval message.
- **C-YT-VIDEO.07** Upload once as private or unlisted, by the owner or by the agent's own browser if it is signed in and the owner said yes. Wait until processing and YouTube's checks finish, then set it to public or schedule it as approved. If the upload seems to fail, check the channel's content list before uploading again.  
  _Done when:_ The video's status after checks, any copyright or restriction notice, and the time it went public or the scheduled time.
- **C-YT-VIDEO.08** Once the video is public, open its watch URL in a signed-out or private browser window. Check the channel name, title, description and that the link opens the product. If it is scheduled, record the scheduled time and do this check after it goes public. If the link is not clickable, as can happen with Shorts, tell the owner and do not claim the video sends visitors to the site.  
  _Done when:_ The public video URL, the title and description as they appear, and whether the link is clickable, or the scheduled time if it is not public yet.

**Hand back:** `video_url`, `published_text`, `visibility`

**If stuck:**
- `brand_channel_mismatch`: If YouTube Studio shows a different channel from the brand's, stop and ask the owner to switch to the right channel before uploading.
- `owner_has_not_approved`: If the owner has not said yes to the title, description and settings, do not make the video public; show them and wait.
- `copyright_claim`: If YouTube flags a copyright claim during checks, keep the video private and show the owner the notice; do not publish around it.
- `verification_needed`: If YouTube asks for phone verification or another identity check, tell the owner which screen needs them and wait.
- `external_link_unavailable`: If the description link is not clickable for this video, tell the owner and do not count the video as a source of site visits.

### 13. Read this goal's numbers on YouTube (result numbers)

Record the numbers this goal is judged on, for the same channel and the same length of time before and after the round, so rounds are compared on real YouTube and link numbers. record_numbers lists exactly which numbers it needs.

- **C-YT-METRICS.01** Confirm the channel ID, the videos or comment threads you are measuring, the date range and the time zone. For the baseline use the same number of days just before the round; for the current reading use the round's own days. If you cannot open YouTube Studio analytics, ask the owner for screenshots or the numbers.  
  _Done when:_ Channel ID, video or comment URLs, date range with time zone, and how the numbers will be obtained.
- **C-YT-METRICS.02** Read the numbers exactly as YouTube Studio shows them for those videos and days: views, watch time, average view duration, subscribers gained and subscribers lost. Read Shorts and long videos separately and never add them into one figure without saying so.  
  _Done when:_ The numbers as displayed, split by Shorts and long videos, with the screen they came from and the time they were read.
- **C-YT-METRICS.03** Fill the goal's components by their exact names. For a subscriber goal, 'subscribers' is subscribers gained minus subscribers lost in the range. For a completion goal, 'video_starts' is the views of the measured videos; for 'completed_views', use a count of viewers who reached the end only if YouTube shows one. If it shows only the video's audience retention chart, multiply the views by the percentage still watching at the last moment of the video, round down, use the same method for the baseline and the current reading, and say in source that it was calculated from the retention chart. If the chart cannot be read at the end, leave 'completed_views' out and name it as missing.  
  _Done when:_ Each component name with its number and a one-line note on how it was read.
- **C-YT-METRICS.04** For a link-click goal, take 'link_clicks' from the round's tracked link (from tracking), not from YouTube, and 'views' from YouTube Studio for the same videos and days. Comments and likes never stand in for clicks.  
  _Done when:_ The tracked link's click count and the matching views, each with its source.
- **C-YT-METRICS.05** For a comment-request goal, 'eligible_requests' is the number of different request comments the round replied to, and 'qualified_replies' is the number of those commenters who answered back with a real next step (asked for the link, a price or a demo, or said they will try it). Count each person once, and never count likes or the owner's or the agent's own replies.  
  _Done when:_ Both counts, with the URL of each reply that was counted as qualified.
- **C-YT-METRICS.06** Add website visits or sales only if the owner already has a source for them, such as the tracked link, site analytics or payment records. Where you cannot tell which video or reply led to a visit or a sale, say so plainly.  
  _Done when:_ Each visit or sales figure names its source, and unknown links between video and sale are stated.
- **C-YT-METRICS.07** Pass the goal's exact component names to record_numbers with the source of each. If there is no history, record 0 and say in source that there is no history. Never estimate a missing number; leave it out and name it as missing.  
  _Done when:_ The record_numbers entry with every component, its source, and any missing number named.

**If stuck:**
- `cannot_open_analytics`: If you cannot open YouTube Studio analytics for this channel, ask the owner for screenshots of the screens that show the numbers this goal needs.
- `numbers_from_wrong_channel`: If a screen or screenshot shows a different channel from the agreed channel ID, do not use those numbers and ask again.
- `no_history`: If the channel has no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.
- `link_clicks_not_tracked`: If the description had no tracked link, say that link clicks cannot be read for this round, record nothing for clicks, and make sure the next round uses the tracked link.
- `too_early_to_read`: If the videos or replies are less than 48 hours old, YouTube figures may still be filling in; report the numbers as early and read them again later.
