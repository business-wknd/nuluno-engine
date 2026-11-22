# Instagram: raise bio link clicks per profile visit

- **Goal id:** `G-IG-LINK-RATE`
- **Channel:** instagram
- **Metric:** `profile_link_rate` = `link_clicks` / `profile_visits`, should increase
- **Observation window:** 48 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), content (the next round starts with `A-COPY`), data (the next round starts with `C-IG-METRICS`)

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

### 8. Confirm the Instagram account and who publishes

Settle which Instagram account posts, whether its insights can be read, and who presses Share, so every post and every number in this goal comes from the right brand account.

- **C-INSTAGRAM-ACCESS.01** Ask the owner for the URL of the brand's Instagram profile. Open it as a public page and check that the handle, name, and bio website match this product, not a personal account or a brand from an earlier goal.  
  _Done when:_ The profile URL and handle, with a note that the name and bio website match the product.
- **C-INSTAGRAM-ACCESS.02** Ask the owner whether the account is a professional account (business or creator). Insights such as reach, saves, and profile visits only exist on professional accounts. Do not switch the account type yourself; if it is personal, ask the owner whether they want to switch it in the app.  
  _Done when:_ The account type, and the owner's answer if a switch was discussed.
- **C-INSTAGRAM-ACCESS.03** Note which Instagram accounts are signed in right now in the agent's browser or tools. If another account is active, switch to the brand account in the account switcher without signing out of the others; if the brand account is not there, the owner signs in on the official Instagram screen. Never ask for a password and never copy cookies or tokens.  
  _Done when:_ The handles that are signed in, and the brand handle now active, or a note that nobody is signed in.
- **C-INSTAGRAM-ACCESS.04** Decide who presses Share: the owner in the Instagram app, or the agent if its browser or Instagram tool is signed in to this exact handle. If the agent uses a tool rather than a browser, check that the tool shows this handle and can both create a post and read insights; if it can only read, the owner publishes.  
  _Done when:_ Who will publish, the handle shown as signed in, and what the agent's tool can and cannot do on this account.
- **C-INSTAGRAM-ACCESS.05** Decide who reads the numbers: the agent if it can open the account's insights, or the owner by sending screenshots. Ask the owner who can read direct messages, and write down the time zone the insights use.  
  _Done when:_ Who reads insights and messages, and the time zone.
- **C-INSTAGRAM-ACCESS.06** Write down the current bio and bio link exactly as they appear. Instagram captions do not make links clickable, so a later step may ask to point the bio link at this round's tracked link; that change needs the owner's yes.  
  _Done when:_ The current bio text and bio link, copied from the profile.
- **C-INSTAGRAM-ACCESS.07** Create a new account only if the owner asked for one in this conversation and no brand account exists. Use one real account with the owner's approved name, bio, and website. Sign up with the owner's email, or with inbox_address if the owner agrees, and read the code with inbox_latest. Never invent a birthday or other details.  
  _Done when:_ The owner's request and the approved profile details, or a note that the existing account is used.
- **C-INSTAGRAM-ACCESS.08** If Instagram asks for a phone code, a login check, a CAPTCHA, an identity check, or acceptance of terms, stop and tell the owner which screen needs them. Note where you stopped and continue from there once they are done.  
  _Done when:_ What the owner must do, on which screen, and where to resume, or a note that nothing was needed.
- **C-INSTAGRAM-ACCESS.09** Open the public profile once more and confirm that whoever publishes can start a new post on this handle. Write down the time you checked.  
  _Done when:_ Profile URL, handle, account type, who publishes, and the time of the check.

**Hand back:** `account_handle`, `profile_url`, `account_type`, `who_publishes`

**If stuck:**
- `wrong_account_signed_in`: If the active account is a personal account or another brand, stop before any posting and ask the owner to switch to the brand account or to post it themselves.
- `personal_account_no_insights`: If the account is personal, tell the owner the goal's numbers cannot be read there and ask whether they want to switch it to a professional account in the app themselves.
- `owner_action_needed`: If a phone code, login check, CAPTCHA, identity check, or terms screen appears, stop and tell the owner which screen and which button; never do these for them.
- `agent_not_signed_in`: If neither the agent's browser nor its tool is signed in to the brand handle, set who_publishes to 'owner' and plan to hand them the final files and caption.
- `account_restricted`: If Instagram says the account is restricted or an action is blocked, stop all posting and ask the owner to check the account's status in the app; never try a second account.

### 9. Study Instagram posts and comments for hooks that work

Find, from real recent posts and comments in the product's niche, the buyer situations and opening hooks worth testing, so the next post starts from what this audience already responds to.

- **C-IG-RESEARCH.01** Write a short search list from the chosen angle and buyer quotes: 3 to 5 keywords or hashtags, and 5 accounts in the niche of different sizes, not only the biggest ones. Include accounts the buyers follow, not only competitors.  
  _Done when:_ The keywords, hashtags, and account handles you will search.
- **C-IG-RESEARCH.02** Open at least 10 carousels or Reels from the last 90 days, one by one, with read_page or the agent's browser. Record each post's URL, author, date (or 'unknown'), format, and only the likes, comments, or views that are visible. Never guess reach.  
  _Done when:_ A list of at least 10 posts with URL, author, date, format, and visible numbers.
- **C-IG-RESEARCH.03** Read the comments under those posts. Copy at least 5 comments, word for word, where a person describes a problem, asks how to do something, or asks where to buy. Keep the creator's own promotion apart from what the audience says.  
  _Done when:_ At least 5 exact comment quotes, each with the post URL it came from.
- **C-IG-RESEARCH.04** For the 3 posts with the most visible engagement for their account size, break down the first slide or first 2 seconds, the first caption line, the order of the content, and the call to action.  
  _Done when:_ A breakdown of 3 posts: hook, first caption line, structure, and call to action.
- **C-IG-RESEARCH.05** Check each hook against the product fact sheet. Drop any hook that would need a claim the product cannot back up, such as a result, a number, or a before-and-after you do not have.  
  _Done when:_ The hooks kept and the hooks dropped, each with a one-line reason.
- **C-IG-RESEARCH.06** Write one test idea that changes only one thing: the hook, or the layout inside the format this goal publishes (for example a checklist carousel versus a step-by-step carousel). Describe version A and version B in one line each, in the product's own words; never copy another creator's images, text, or video.  
  _Done when:_ One hypothesis and two versions that differ in one labeled thing.
- **C-IG-RESEARCH.07** Write down how you picked the posts, the date range, and what this research cannot show. Visible likes and comments do not show reach, followers gained, or sales.  
  _Done when:_ A short note on sample choice, date range, and limits.

**Hand back:** `examples`, `buyer_quotes`, `hypothesis`, `limitations`

**If stuck:**
- `login_wall`: If Instagram shows a sign-in wall and no posts, search the web for public post URLs in the niche, or ask the owner to send 10 post links or screenshots from their app.
- `too_few_recent_posts`: If fewer than 10 posts from the last 90 days can be found, widen to 180 days, say so in limitations, and keep going.
- `no_buyer_comments`: If the comments hold fewer than 5 real questions or problems, use the buyer quotes already collected for this goal and say so; never write quotes yourself.
- `hook_needs_unproven_claim`: If every strong hook depends on a result the product cannot prove, ask the owner for the proof or pick a hook built on the buyer's situation instead.
- `private_or_removed_post`: If a post is private or removed, leave it out and pick another; never describe a post you could not open.

### 10. Plan this round's post and the files it needs

Turn the chosen angle, the research, and last round's result into one post with one clear idea and a production brief, so the round tests that idea against the goal's main number.

- **S10.01** Read the goal, its main number, and last round's result with where_are_we. Write in one sentence what this round should improve and the one thing it tests. If there is an earlier round, keep its post as it was and note what changes and why. If there is none, start from the chosen angle; never claim an earlier winner that does not exist.  
  _Done when:_ One sentence naming the goal's number, the thing being tested, and last round's result with the reason for the change, or 'first round'.
- **S10.02** List the posts, photos, videos, and product screenshots the owner already has. Mark each one 'owner made', 'licensed', or 'unknown'. Leave out anything marked unknown until the owner confirms the rights.  
  _Done when:_ A list of usable files, each with its rights status.
- **S10.03** Give the post one buyer group and one stage: first hears of the problem, compares options, or is ready to buy. If the idea speaks to two groups, keep one and save the other for a later round.  
  _Done when:_ The post's one buyer group and stage.
- **S10.04** Pick the angle and the proof: the problem, the promise, and a real demo, screenshot, or fact from the product fact sheet. Leave out any result you cannot prove.  
  _Done when:_ The angle and the facts or demos the post relies on.
- **S10.05** Use the format this goal's plan publishes: a carousel of 4:5 images at 1080 x 1350, or, for the Reels goal, a vertical 9:16 Reel at 1080 x 1920.  
  _Done when:_ The format and size of the post.
- **S10.06** Choose the one action the post asks for, matched to the goal's main number: save, follow, send a message, or tap the link in bio. If it sends people to the product, get this round's tracked link from tracking and open it to check it loads; if tracking says it is not available, use the product URL and note that clicks will be read from Instagram.  
  _Done when:_ The call to action, and the link opened and checked, or a note that the post has no link.
- **S10.07** Write version A, the one this round publishes. If the research suggests a second idea, write version B that differs in one thing only (the hook, the proof, or the layout), label the difference, and keep it as the candidate change for the next round. Do not publish both in one round: Instagram has one bio link and the round is judged on one post.  
  _Done when:_ Version A, and version B if any, labeled with the single difference and marked 'next round'.
- **S10.08** Write a production brief for version A: slide count or video length, the text for each slide or on-screen line, the files to use, and the size. Keep slide text under 20 words and put the hook on the first slide or in the first 2 seconds.  
  _Done when:_ One brief with files, size, length, and the text for each part.
- **S10.09** Pick the publish day and hour, at a time the owner can approve and, if the account's insights show when followers are most active, inside that time. Note that the numbers are read when the goal's observation window ends (48 hours for these goals), and that no other post for this goal goes out during the window.  
  _Done when:_ The planned publish date and hour with time zone, and when the numbers will be read.

**Hand back:** `batch_plan`, `versions`, `production_brief`, `schedule`

**If stuck:**
- `no_chosen_angle`: If no angle has been chosen, go back to the angle test step before planning the post.
- `no_usable_files`: If there are no files with known rights, plan a post made from product screenshots or plain text slides, and ask the owner for one real photo or demo.
- `no_working_link`: If the link does not open the product, stop and ask the owner which product URL to use before planning a link call to action.
- `too_many_differences`: If version B differs from version A in more than one thing, cut it back to one difference so the next round can show what worked.
- `fact_missing_for_claim`: If the post needs a fact you do not have, drop that claim or ask the owner; never fill the gap with a guess.

### 11. Write the post from proven facts

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

### 12. Make the marketing images from real product visuals

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

### 13. Read this goal's numbers on Instagram (baseline numbers)

Record the numbers this goal is judged on, for the account before and after the new post, so each round is compared on real numbers. record_numbers lists exactly which numbers it needs.

- **C-IG-METRICS.01** Confirm the handle, whether this is the baseline or the current reading, and the time zone. The baseline is read just before this round's post goes live; the current reading is read after the goal's observation window ends, which the engine tells you (48 hours for these goals). Read only the components the step lists, and leave out any the engine says it counted itself.  
  _Done when:_ Handle, baseline or current, the components needed, and the time zone.
- **C-IG-METRICS.02** For numbers read per post, such as reach, saves, and profile visits: for the baseline, add up the account's last 3 to 5 posts of the same format from the past 30 days, each at least 48 hours old; for the current reading, use this round's post. Take both parts of a rate from the same posts, and keep per-post numbers apart from account totals.  
  _Done when:_ The posts measured with their URLs, and each number as shown, per post and added up.
- **C-IG-METRICS.03** For a Reel, read the views figure the Reel's insights show and use it for video_starts, saying so in source. Use a figure for views that reached the end only if the insights display one as a number, either a count or a percentage you can multiply by views; never read it off a graph by eye.  
  _Done when:_ Views and the end-of-video figure exactly as displayed, with the screen they came from, or a note that no end-of-video figure is shown.
- **C-IG-METRICS.04** For followers, read the follower count on the profile at the moment of reading; it is a running total and the engine subtracts the earlier reading. Note follows and unfollows too if the account's insights show them. Never report the total alone as this round's growth.  
  _Done when:_ The follower count with the time read, plus follows and unfollows if shown.
- **C-IG-METRICS.05** For link clicks and profile visits on the account: in the current reading, link_clicks are usually counted by the engine from the tracked link, so leave them out when the step says so. For the baseline, read external link taps and profile visits from the account's insights for the shortest date range offered that ends just before publishing, both from the same range.  
  _Done when:_ Link clicks and profile visits with their source and date range.
- **C-IG-METRICS.06** For qualified_inquiries, keep a running total: the number of different people who asked in comments or direct messages about price, availability, how to buy, or whether the product fits their case, counted from this goal's first baseline reading (0 at that reading). Leave out the owner, the agent, spam, and bots. The owner reads direct messages or sends screenshots.  
  _Done when:_ The running total of different people who asked, with the date and a short summary of each question, without names.
- **C-IG-METRICS.07** Call record_numbers with only this goal's metric components, by their exact names from the step's list. Put the screen or tool, the post URLs, the date range, and the time read in source. If there is no history for a component, record 0 and say in source that there is no history. Never estimate a number Instagram does not show.  
  _Done when:_ The record_numbers call with each component name, its value, and its source.
- **C-IG-METRICS.08** Report site visits or sales separately and only from a source the owner already has, such as site analytics or payment records. Say plainly when a visit or sale cannot be tied to the post.  
  _Done when:_ Any visit or sales figure with its source, or a note that none was available.

**If stuck:**
- `cannot_open_insights`: If you cannot open the insights, ask the owner for a screenshot of the post's insights or the account's insights for each number this goal needs.
- `component_not_shown`: If Instagram does not display a number this goal needs, ask the owner for another source they already have; if none exists, submit status 'blocked' naming the missing number, and never estimate it or read it off a graph.
- `no_history`: If the account has no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.
- `numbers_from_wrong_account`: If a screenshot or screen shows a different handle from the agreed one, do not use those numbers and ask again.
- `too_early_to_read`: If the observation window has not ended, report the numbers as early and read them again once the engine says the window is over.
- `personal_account_no_insights`: If the account is personal and shows no insights, record only what the public profile shows, say so in source, and send the owner back to the account step.

### 14. Publish one Instagram carousel and confirm it

Publish the approved carousel once, under the right account, and hand back its public URL, because the post has to be live and exactly as approved before its numbers can be measured.

- **C-IG-CAROUSEL.01** Confirm the handle about to post is the agreed brand account. Look through its last 12 posts so you do not publish the same images or caption twice.  
  _Done when:_ The handle, and a note on the recent posts you checked.
- **C-IG-CAROUSEL.02** Open every slide file and check it shows correctly, is in the planned order, uses one size (4:5 at 1080 x 1350 works well), keeps text away from the edges, and is owner made or licensed. Check the slide count is within Instagram's current limit.  
  _Done when:_ The ordered list of slide files, the slide count, and the rights status of each.
- **C-IG-CAROUSEL.03** Check the caption against the product fact sheet: under 2,200 characters, no more than 5 hashtags, and no price, promise, or number the facts do not support. Links in captions are not clickable, so a link call to action points to the link in bio.  
  _Done when:_ The final caption, its character count, and the facts each claim relies on.
- **C-IG-CAROUSEL.04** If the call to action uses the bio link, get this round's tracked link from tracking and open it to check it loads the product. Changing the bio link changes the owner's profile, so it is part of the approval.  
  _Done when:_ The tracked link, opened and checked, and the bio link it would replace, or a note that the bio link stays.
- **C-IG-CAROUSEL.05** Show the owner the slides in order, the exact caption, and any bio link change. Get a clear yes to this exact version before anything goes live.  
  _Done when:_ The owner's approval message for these slides, this caption, and this bio link.
- **C-IG-CAROUSEL.06** The agreed person updates the bio link if approved, creates the post, adds the slides in order, and checks the preview of every slide for bad crops. Press Share once. If an upload is still running, wait; do not press Share again.  
  _Done when:_ Confirmation that the preview matched the approved slides, who pressed Share, and when.
- **C-IG-CAROUSEL.07** Open the post's public URL and check every slide, the slide order, the caption, and the handle. Open the profile and check the bio link. If the post shows as under review or not yet public, report that status and do not post again; if publishing seemed to fail, check the profile for the post before any retry.  
  _Done when:_ The public post URL, the caption as it appears there, and the live bio link.

**Hand back:** `post_url`, `published_text`, `bio_link`

**If stuck:**
- `owner_has_not_approved`: If the owner has not said yes to these exact slides, caption, and bio link, do not publish; show them and stop until they answer.
- `wrong_account_signed_in`: If the signed-in account is not the agreed handle, stop and ask the owner to switch accounts or to post it themselves.
- `agent_cannot_publish`: If the agent cannot post, give the owner the slide files in order, the caption, and the bio link, and ask them to send back the post URL.
- `bad_crop`: If the preview cuts off text or images, pick the original size in the crop option, or resize every slide to the same 4:5 size, then check the preview again.
- `post_not_visible`: If the post does not show up after Share, check the profile again after a few minutes before any retry, and never post the same carousel twice.
- `link_does_not_open`: If the tracked link does not open the product, stop before publishing and fix the link with the owner.

### 15. Read this goal's numbers on Instagram (result numbers)

Record the numbers this goal is judged on, for the account before and after the new post, so each round is compared on real numbers. record_numbers lists exactly which numbers it needs.

- **C-IG-METRICS.01** Confirm the handle, whether this is the baseline or the current reading, and the time zone. The baseline is read just before this round's post goes live; the current reading is read after the goal's observation window ends, which the engine tells you (48 hours for these goals). Read only the components the step lists, and leave out any the engine says it counted itself.  
  _Done when:_ Handle, baseline or current, the components needed, and the time zone.
- **C-IG-METRICS.02** For numbers read per post, such as reach, saves, and profile visits: for the baseline, add up the account's last 3 to 5 posts of the same format from the past 30 days, each at least 48 hours old; for the current reading, use this round's post. Take both parts of a rate from the same posts, and keep per-post numbers apart from account totals.  
  _Done when:_ The posts measured with their URLs, and each number as shown, per post and added up.
- **C-IG-METRICS.03** For a Reel, read the views figure the Reel's insights show and use it for video_starts, saying so in source. Use a figure for views that reached the end only if the insights display one as a number, either a count or a percentage you can multiply by views; never read it off a graph by eye.  
  _Done when:_ Views and the end-of-video figure exactly as displayed, with the screen they came from, or a note that no end-of-video figure is shown.
- **C-IG-METRICS.04** For followers, read the follower count on the profile at the moment of reading; it is a running total and the engine subtracts the earlier reading. Note follows and unfollows too if the account's insights show them. Never report the total alone as this round's growth.  
  _Done when:_ The follower count with the time read, plus follows and unfollows if shown.
- **C-IG-METRICS.05** For link clicks and profile visits on the account: in the current reading, link_clicks are usually counted by the engine from the tracked link, so leave them out when the step says so. For the baseline, read external link taps and profile visits from the account's insights for the shortest date range offered that ends just before publishing, both from the same range.  
  _Done when:_ Link clicks and profile visits with their source and date range.
- **C-IG-METRICS.06** For qualified_inquiries, keep a running total: the number of different people who asked in comments or direct messages about price, availability, how to buy, or whether the product fits their case, counted from this goal's first baseline reading (0 at that reading). Leave out the owner, the agent, spam, and bots. The owner reads direct messages or sends screenshots.  
  _Done when:_ The running total of different people who asked, with the date and a short summary of each question, without names.
- **C-IG-METRICS.07** Call record_numbers with only this goal's metric components, by their exact names from the step's list. Put the screen or tool, the post URLs, the date range, and the time read in source. If there is no history for a component, record 0 and say in source that there is no history. Never estimate a number Instagram does not show.  
  _Done when:_ The record_numbers call with each component name, its value, and its source.
- **C-IG-METRICS.08** Report site visits or sales separately and only from a source the owner already has, such as site analytics or payment records. Say plainly when a visit or sale cannot be tied to the post.  
  _Done when:_ Any visit or sales figure with its source, or a note that none was available.

**If stuck:**
- `cannot_open_insights`: If you cannot open the insights, ask the owner for a screenshot of the post's insights or the account's insights for each number this goal needs.
- `component_not_shown`: If Instagram does not display a number this goal needs, ask the owner for another source they already have; if none exists, submit status 'blocked' naming the missing number, and never estimate it or read it off a graph.
- `no_history`: If the account has no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.
- `numbers_from_wrong_account`: If a screenshot or screen shows a different handle from the agreed one, do not use those numbers and ask again.
- `too_early_to_read`: If the observation window has not ended, report the numbers as early and read them again once the engine says the window is over.
- `personal_account_no_insights`: If the account is personal and shows no insights, record only what the public profile shows, say so in source, and send the owner back to the account step.
