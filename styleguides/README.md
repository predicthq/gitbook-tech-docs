# PredictHQ Style Guide

## Introduction

This style guide defines the writing standards for our documentation. It uses the Google developer documentation style guide as its base. Its goal is to keep our documentation clear, accurate, and consistent, no matter who writes it—humans or AI.

## Audience and scope

**Who reads our documentation:** Developers and technical practitioners. We assume general technical competence, not familiarity with our product. We explain our concepts fully and don't explain theirs.

**Who writes our documentation:** Software engineers and Product management.

## About our Google base

Writers can consult the [Google developer documentation style guide](https://developers.google.com/style) for questions this page doesn't answer. **The AI enforces only what's written on this page**—it doesn't consult Google's guide or apply rules from it that aren't recorded here. If a Google rule matters to us, it lives on this page. When we decide to differ from Google style, we change the rule here and record why in the decision log.

## Voice and tone

Conversational but professional. Write like you're explaining something to a knowledgeable colleague: friendly and direct, not chatty and not stiff. No slang, no pop-culture references, no forced humor, no hype. This voice description is guidance, not flags: the AI writes and edits with it, and raises it only as suggestions for a human to weigh.

| Guidance                 | Do                                                              | Don't                                                                                 |
| ------------------------ | --------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Direct, not stiff        | ✅ "If the request fails, check your API key first."             | ❌ "In the event that the request should fail, it is advisable to verify the API key." |
| Professional, not chatty | ✅ "This query returns the last 30 days of results."             | ❌ "Ready for some query magic? This bad boy grabs a whole month of results!"          |
| Confident, not hyped     | ✅ "The batch endpoint processes up to 10,000 records per call." | ❌ "Our blazingly fast batch endpoint effortlessly crunches a massive 10,000 records!" |

The enforceable rules of voice:

* **G-1:** No exclamation points in body text.
* **G-2:** Contractions are fine (it's, don't, you're). Avoid stacked or unusual contractions (shouldn't've, mightn't).
* **G-3:** Don't use "please" in instructions. ✅ "Click **Save**." ❌ "Please click **Save**."

## Word list

Terms inherited from the Google guide _(G-4)_. Delete any row you disagree with—and log the change in the decision log so it sticks.

| Term                                      | Use                                           | Don't use               | Notes                             |
| ----------------------------------------- | --------------------------------------------- | ----------------------- | --------------------------------- |
| login (noun, adjective), log in (verb)    | "the login page" / "log in to your account"   | "login to your account" |                                   |
| email                                     | email                                         | e-mail                  |                                   |
| internet                                  | internet                                      | Internet                | Lowercase                         |
| open source                               | open source                                   | open-source             | Unhyphenated even as an adjective |
| sign-in (noun, adjective), sign in (verb) | "the sign-in flow" / "sign in to the console" | "signin"                |                                   |
| website                                   | website                                       | web site                |                                   |

**Banned filler that presumes ease** _(G-5)_: "simply," "easily," "just" (as a minimizer), "obviously," "of course," "quick" (as reassurance). ✅ "Run the installer." ❌ "Simply run the installer." _Exception: "just" meaning "only" or "recently" is fine ("returns just the first match")._

**Avoid time-anchored words that go stale** _(G-6)_: "currently," "at present," "new," "now" (as in "is now available"). State the fact without the anchor—documentation should read as true whenever it's read.

**"Click" a button or link, not "click on"** _(G-7)_. ✅ "Click **Save**." ❌ "Click on **Save**."

| Term                  | Use                   | Don't use           | Notes |
| --------------------- | --------------------- | ------------------- | ----- |
| Predicted Impact Area | Predicted Impact Area | Impact Area or PIA. |       |
|                       |                       |                     |       |
|                       |                       |                     |       |

## Grammar and mechanics

| ID   | Rule                                                  | Do                                         | Don't                                         | Exception                                                                                                                                           |
| ---- | ----------------------------------------------------- | ------------------------------------------ | --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| G-8  | Address the reader as "you"                           | ✅ "You can share the file with your team." | ❌ "The user should click Save."               | "The user" is correct when the reader is a developer and the sentence is about that developer's end users: "Your app asks the user for permission." |
| G-9  | Use present tense                                     | ✅ "The command creates a file."            | ❌ "The command will create a file."           | Future tense for genuinely future events ("Support for v2 ends in March")                                                                           |
| G-10 | Use active voice                                      | ✅ "The command creates the file."          | ❌ "The file is created by the command."       | Passive is fine when the actor is unknown or irrelevant ("The token is encrypted at rest") or to avoid blaming the reader                           |
| G-11 | Use the serial comma                                  | ✅ "tokens, keys, and secrets"              | ❌ "tokens, keys and secrets"                  |                                                                                                                                                     |
| G-12 | Spell out one through nine; numerals for 10 and above | ✅ "five workspaces," "24 integrations"     | ❌ "5 workspaces"                              | Numerals always for versions, units of measure, step references, and technical values                                                               |
| G-13 | Em dashes take no surrounding spaces                  | ✅ "The API—which is public—returns JSON."  | ❌ "The API — which is public — returns JSON." |                                                                                                                                                     |

## Formatting

| ID   | Element     | Rule                                                                          | Example                                                                                                            |
| ---- | ----------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| G-14 | Headings    | Sentence case, always                                                         | ✅ "Getting started with the API" ❌ "Getting Started With The API"—product names and proper nouns keep their casing |
| G-15 | UI elements | Bold UI element names as the user sees them, exact casing preserved           | ✅ Click **Create bucket**.                                                                                         |
| G-16 | Links       | Descriptive link text; never "click here" or "this page"                      | ✅ See the \[authentication guide].                                                                                 |
| G-17 | Lead-ins    | Introduce lists and code blocks with a sentence or fragment ending in a colon | ✅ "The response includes three fields:"                                                                            |

## Writing procedures

* **G-18:** Number sequential steps. Use a single bullet, not "1.", for a one-step procedure.
* **G-19:** State the location or goal before the action. ✅ "In the console, click **Settings**." ❌ "Click **Settings** in the console."
* **G-20:** One action per step. Combine only when actions are trivially linked ("Click **Save**, and then click **OK**" is acceptable as one step).
* **G-21:** Write steps in the imperative. ✅ "Open the file." ❌ "You should now open the file."

## Content types and templates

| Content type | Use it for | Template or example    |
| ------------ | ---------- | ---------------------- |
| Tech Docs    |            | Use Diátaxis framework |
|              |            |                        |
|              |            |                        |

## Accessible writing

* **G-22:** Write descriptive alt text for every meaningful image; use empty alt text for purely decorative images.
* **G-23:** Don't rely on color, position, or direction alone to convey meaning—avoid "the green button" and "the panel on the right." Name the element instead, and prefer "earlier" and "later" over "above" and "below."
* **G-16** applies here too: link text describes the destination and makes sense out of context.

## Inclusive language

* **G-24:** Use gender-neutral language. Use singular "they" when gender is unknown or irrelevant—never "he or she."
* **G-25:** Replace ableist and violent idioms: "confirmation check," not "sanity check"; "stop the process," not "kill the process" (the literal `kill` command keeps its name).

## Ownership and updates

* **Owner:** Robert Kern
* **Review cadence:** Annually
* **How to propose a change:** Slack or in-person discussion

## Decision log

Record every deliberate departure from Google style here, alongside other settled decisions, so debates don't reopen. Changing a rule above changes what the AI enforces; this log remembers why.

<table><thead><tr><th width="132.89453125">Date</th><th width="252.62890625">Decision</th><th width="131.0703125">Differs from Google?</th><th>Rationale</th></tr></thead><tbody><tr><td>2026-08-17</td><td>Adopt Google Style Guide.</td><td></td><td></td></tr></tbody></table>

***

_Based on the_ [_Google developer documentation style guide_](https://developers.google.com/style) _(snapshot at 2026-08-17), used under CC BY 4.0. Template structure adapted from The Good Docs Project for GitBook._
