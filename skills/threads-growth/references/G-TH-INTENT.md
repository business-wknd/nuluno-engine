# Threads: turn public requests for help into useful replies

- **Goal id:** `G-TH-INTENT`
- **Language:** English
- **Channel:** threads
- **Metric:** `qualified_reply_rate` = `qualified_replies` / `eligible_requests`, should increase
- **Observation window:** 48 hours after publishing
- **If the target is missed, the agent picks one bottleneck:** audience (the next round starts with `A-SEGMENTS`), motivation (the next round starts with `A-MOTIVES`), angle (the next round starts with `A-ANGLES`), message (the next round starts with `C-TH-INTENT`), data (the next round starts with `C-TH-METRICS`)

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

### 8. Confirm the Threads account and who publishes

Settle which Threads account will post and who presses publish (the owner, or the agent's own browser), so the post goes out under the right brand without the owner being stopped halfway.

- **C-THREADS-ACCESS.01** Ask the owner for the URL of the Threads profile that will post. Note separately which Threads account and which Instagram account are signed in right now; being signed in to Instagram does not mean the Threads profile exists.  
  _Done when:_ Both handles written down, with whether each profile exists.
- **C-THREADS-ACCESS.02** Open the Threads profile URL as a public page and confirm that it exists and belongs to the owner. If it exists, use it and do not create a second profile.  
  _Done when:_ The profile URL and the owner's confirmation that it is theirs.
- **C-THREADS-ACCESS.03** Decide who presses publish: the owner on their own device, or the agent's own browser if it is already signed in to that account. If nobody is signed in, the owner signs in themselves on the official Threads screen and, if it offers 'Continue with Instagram', checks the Instagram handle shown first. Never ask for a password.  
  _Done when:_ Who will publish, how the owner signed in, and the handle that was selected.
- **C-THREADS-ACCESS.04** Create a new Threads profile only if the owner asked for one in this conversation. Check the name, bio, and website link with the owner, and never enter a made-up birthday or made-up verification details.  
  _Done when:_ The owner's request and the profile details they approved, or a note that no new profile was needed.
- **C-THREADS-ACCESS.05** If Threads asks for a verification code, acceptance of terms, or an identity check, stop and tell the owner exactly which screen needs them. Note where you stopped and return to the same profile once they have finished.  
  _Done when:_ A note of what the owner needs to do, on which screen, and where to resume.
- **C-THREADS-ACCESS.06** After sign-in or profile creation, open the public profile again and the account's own profile screen. Confirm the handle matches the brand and that whoever publishes can open the new post box.  
  _Done when:_ Profile URL, handle, confirmation that a new post can be started, and the time this was checked.

**Hand back:** `account_handle`, `profile_url`, `who_publishes`

**If stuck:**
- `instagram_threads_mismatch`: If the Instagram account offered at sign-in is not the one tied to the intended Threads profile, have the owner go back to the account chooser and pick the right handle.
- `profile_does_not_exist`: If the Threads URL shows no profile, tell the owner; a successful Instagram sign-in is not a Threads profile, and a new one is created only if the owner asks.
- `owner_action_needed`: If a verification code, terms screen, or identity check appears, stop and tell the owner which screen and which button; never enter codes or accept terms for them.
- `agent_browser_not_signed_in`: If the agent's browser is not signed in to the right account, set who_publishes to 'owner' and plan to hand them the final text to post.
- `handle_not_the_brand`: If the signed-in account is a personal account or a different brand, stop before any posting and ask the owner which account to use.

### 9. Find recent Threads posts where people ask for help

Produce a checked list of recent public Threads posts where real people ask for a recommendation or describe the problem the product solves, because these posts are the round's eligible requests and the only places a reply can help.

- **C-TH-INTENT.01** Write 5 to 10 search phrases from the buyer quotes, in the words buyers use: '<task> recommend', 'any alternative to <tool>', 'how do I <problem>'. Use the buyers' language, not product terms.  
  _Done when:_ The list of phrases, each with the date it was run.
- **C-TH-INTENT.02** Search with Threads search in the agent's browser, or with a web search limited to threads.com or threads.net. Prefer posts from the last 7 days and drop anything older than 30 days.  
  _Done when:_ For each phrase, the candidate post URLs found and how they were found.
- **C-TH-INTENT.03** Open each candidate post itself. Read the author's handle, the date, the full text and the replies below it. A search snippet is not a read post.  
  _Done when:_ For each post: URL, author handle, date, and whether you read the full post and its replies.
- **C-TH-INTENT.04** Keep only posts where the author asks for a recommendation or describes the problem in their own words. Exclude sellers promoting themselves, trend or joke posts, posts already solved in the replies, and posts that limit who can reply.  
  _Done when:_ For each kept post, the exact quote that shows the need; for each excluded post, the reason.
- **C-TH-INTENT.05** Check each kept post against the product fact sheet: does the product truly solve what this person asked? Write the fit as your inference, separate from what they said. Also check whether the brand account already replied in that thread.  
  _Done when:_ Each kept post marked fits, partly fits, or does not fit, plus whether the brand already replied.
- **C-TH-INTENT.06** Hand back the qualified posts, the excluded ones and the unknown ones, each with a reason. The count of qualified posts is this round's number of eligible requests for the goal. If fewer than three qualify, report the true number; never invent a need.  
  _Done when:_ The qualified list with its count, and the excluded and unknown lists with reasons.

**Hand back:** `demand_posts`, `exclusions`, `search_phrases`

**If stuck:**
- `search_unavailable`: If Threads search does not work in your browser, use a web search limited to threads.com or threads.net; if a post cannot be opened, leave it out rather than guessing its content.
- `not_signed_in`: If Threads asks you to sign in to search, ask the owner to sign in in your browser or to run the phrases and send you the post URLs.
- `no_results`: If no post qualifies, rewrite the phrases once using different buyer words, then report the true zero.
- `already_replied`: If the brand already replied in a thread, exclude it; never reply to the same person twice in one round.
- `replies_restricted`: If the author limits who can reply, exclude the post and do not reach out by DM instead.

### 10. Read this goal's numbers on Threads (baseline numbers)

Record the numbers this goal is judged on, for the account's posts before and after the new post, so rounds are compared on real numbers. record_numbers lists exactly which numbers it needs.

- **C-TH-METRICS.01** Confirm which Threads profile and which posts you are measuring, the date range, and the time zone. Check whether you can open the Threads insights screen; if you cannot, ask the owner for a screenshot or the numbers.  
  _Done when:_ Profile handle, post URLs, date range with time zone, and how the numbers will be obtained.
- **C-TH-METRICS.02** Read the follower count at the start and end of the range, plus views, replies, and link clicks where Threads shows them. Write 'not shown' for any number Threads does not display, and do not estimate it.  
  _Done when:_ The numbers exactly as displayed, with the screen they came from and the time they were read.
- **C-TH-METRICS.03** Count conversations once per person who shows a real need for the product. Do not count the owner's or the agent's own replies as new prospects.  
  _Done when:_ The number of different people who asked about the product, with the URL of each reply.
- **C-TH-METRICS.04** Add website visits and sales only if the owner already has a source for them, such as site analytics or payment records. Where you cannot tell which post led to a visit or a sale, say so plainly.  
  _Done when:_ Each visit or sales figure names its source, and unknown links between post and sale are stated.

**If stuck:**
- `cannot_open_insights`: If you cannot open the Threads insights screen, ask the owner for a screenshot of it or for the numbers this goal needs.
- `link_clicks_not_shown`: If Threads shows no link clicks for the post, ask the owner for clicks from the site analytics or link tool they already use and name that source. If there is no source at all, say so; do not estimate.
- `no_history`: If the account has no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.
- `numbers_from_wrong_account`: If the screenshot or screen shows a different handle from the agreed one, do not use those numbers and ask again.
- `too_early_to_read`: If the post is less than 24 hours old, report the numbers as early and read them again later.

### 11. Reply helpfully to Threads posts that ask for help

Post one honest, useful reply under each qualified request, with the owner's approval, because a reply that solves the person's problem first is what turns a public request into a real conversation.

- **C-TH-REPLY.01** Reopen each post on the qualified list just before writing. Confirm the author, that the post is still up and still open to replies, that it was not solved, that the brand has not replied, and that the author has not asked people to stop.  
  _Done when:_ Each post marked still eligible or skipped, with the reason and the time checked.
- **C-TH-REPLY.02** Write one reply per post, under 500 characters. Answer the question first with something useful even if they never buy. Mention the product only if it truly fits, and say plainly that you make it, for example 'I'm the founder of ...'.  
  _Done when:_ One draft per post, its character count, and the line that states the relationship to the product.
- **C-TH-REPLY.03** If the reply includes a link, use the round's tracked link. If you are testing two reply angles, add ?v=A to one and ?v=B to the other, and change only the angle.  
  _Done when:_ Each draft's link and version label, or a note that it has no link.
- **C-TH-REPLY.04** Check each claim against the product fact sheet; remove any number, result or promise you cannot support. Do not move the person to DM or email unless they ask for it.  
  _Done when:_ Each draft with its claims and the fact each one rests on.
- **C-TH-REPLY.05** Show the owner every reply word for word, with the post it answers. Post at most 10 replies in a round, never the same text twice. Nothing goes out without the owner's yes.  
  _Done when:_ The approved replies and the owner's approval message.
- **C-TH-REPLY.06** Confirm the signed-in account is the agreed brand handle. Post each approved reply once, directly under the original post. The owner posts it, or the agent's own browser does if it is signed in and the owner said yes. Leave at least 10 minutes between replies.  
  _Done when:_ For each reply: who posted it and the time.
- **C-TH-REPLY.07** Open each reply's public URL. Check the text, the author handle and that it sits under the right post. If posting seemed to fail, look for the reply before trying again so nothing is posted twice.  
  _Done when:_ The public URL of each reply and its text as it appears there.
- **C-TH-REPLY.08** Over the next 48 hours, check each thread for answers. Draft short responses to real questions for the owner to approve, and stop at once if someone says no thanks.  
  _Done when:_ For each reply: no answer, answered with interest, or declined, with the URL of any answer.

**Hand back:** `reply_urls`, `published_text`, `author_responses`

**If stuck:**
- `owner_has_not_approved`: If the owner has not said yes to a reply's exact text, do not post it; show it to them and wait.
- `wrong_account_signed_in`: If the signed-in account is not the agreed brand handle, stop and ask the owner to switch accounts or post the replies themselves.
- `thread_solved_or_closed`: If the post was deleted, solved, or closed to replies, skip it and do not contact the author another way.
- `author_asked_to_stop`: If the author or anyone in the thread asks the brand to stop, do not reply again and record it.
- `reply_not_visible`: If a reply does not appear after posting, check again after a few minutes before any retry, and never post the same text twice.

### 12. Read this goal's numbers on Threads (result numbers)

Record the numbers this goal is judged on, for the account's posts before and after the new post, so rounds are compared on real numbers. record_numbers lists exactly which numbers it needs.

- **C-TH-METRICS.01** Confirm which Threads profile and which posts you are measuring, the date range, and the time zone. Check whether you can open the Threads insights screen; if you cannot, ask the owner for a screenshot or the numbers.  
  _Done when:_ Profile handle, post URLs, date range with time zone, and how the numbers will be obtained.
- **C-TH-METRICS.02** Read the follower count at the start and end of the range, plus views, replies, and link clicks where Threads shows them. Write 'not shown' for any number Threads does not display, and do not estimate it.  
  _Done when:_ The numbers exactly as displayed, with the screen they came from and the time they were read.
- **C-TH-METRICS.03** Count conversations once per person who shows a real need for the product. Do not count the owner's or the agent's own replies as new prospects.  
  _Done when:_ The number of different people who asked about the product, with the URL of each reply.
- **C-TH-METRICS.04** Add website visits and sales only if the owner already has a source for them, such as site analytics or payment records. Where you cannot tell which post led to a visit or a sale, say so plainly.  
  _Done when:_ Each visit or sales figure names its source, and unknown links between post and sale are stated.

**If stuck:**
- `cannot_open_insights`: If you cannot open the Threads insights screen, ask the owner for a screenshot of it or for the numbers this goal needs.
- `link_clicks_not_shown`: If Threads shows no link clicks for the post, ask the owner for clicks from the site analytics or link tool they already use and name that source. If there is no source at all, say so; do not estimate.
- `no_history`: If the account has no history for these numbers, record 0 and say in source that there is no history; the first round then sets the baseline.
- `numbers_from_wrong_account`: If the screenshot or screen shows a different handle from the agreed one, do not use those numbers and ask again.
- `too_early_to_read`: If the post is less than 24 hours old, report the numbers as early and read them again later.
