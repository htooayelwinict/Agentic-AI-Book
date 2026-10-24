# Style Guide

This guide is for future contributors. Do not apply it by rewriting chapters without discussion.

## Burmese + English Technical Style

Use Burmese for explanation and flow. Keep common technical terms in English when translating them would make the sentence harder to understand.

Good style:

```text
Agent က tool ကိုခေါ်တဲ့အခါ permission scope ကို သေချာစဉ်းစားရမယ်။
```

Avoid forcing every English term into Burmese if the result sounds unnatural.

Before / after:

```text
Before: ကိုယ်စားလှယ်သည် ကိရိယာအသုံးပြုခြင်းကို ဆောင်ရွက်သည်။
After: Agent က tool ကို ခေါ်ပြီး task ကို ဆက်လုပ်တယ်။
```

```text
Before: အချက်အလက်ပြန်လည်ရယူမှုဖြင့်ဖြည့်စွက်ထားသော စာသားထုတ်လုပ်ခြင်း။
After: RAG ဆိုတာ answer မဖြေခင် relevant data ကို အရင်ရှာပြီး model ကို context အနေနဲ့ ပေးတာပါ။
```

## Terms To Keep In English

Usually keep these in English:

- Agent
- Tool Calling
- Function Calling
- Context
- Context Engineering
- RAG
- MCP
- Memory
- Workflow
- Guardrails
- Sandbox
- Prompt Injection
- Coding Agent
- DevOps

You can explain them in Burmese after the English term.

## Avoid Robotic Burmese

Avoid sentences that sound like direct machine translation.

Prefer short, natural sentences. If a sentence becomes too long, split it.

Avoid overusing formal words when a normal developer phrase is clearer.

Before / after:

```text
Before: အသုံးပြုသူ၏ တောင်းဆိုချက်အား စနစ်မှ ထည့်သွင်းစဉ်းစားခြင်းအား ပြုလုပ်သည်။
After: System က user request ကို အရင်ကြည့်တယ်။
```

```text
Before: လုပ်ငန်းစဉ်သည် အောင်မြင်မှုရှိကြောင်း သေချာစေရန် အတည်ပြုခြင်းကို ပြုလုပ်ရမည်။
After: Task ပြီးပြီလို့ မပြောခင် result ကို verify လုပ်ရမယ်။
```

## Register: Conversational For Explanation

The book keeps the literary register (`သည်။`, `၏`, `ဤ`, `၎င်း`, `ချေ`) for chapter openers, metaphors, and the preface. Every definitional or technical sentence uses the plain developer register (`တယ်။` / `ပါတယ်။` for statements, `ပါ။` for instructions), the same register as the "After" examples in this guide and the `Beginner အနေနှင့်…` asides.

Chapter 04 is the reference chapter for this register.

| Pattern to avoid in technical prose | Use instead | Why |
|---|---|---|
| `…သည်။` on every sentence | `…တယ်။` / `…ပါတယ်။` (statements), `…ပါ။` (instructions) | Matches how the guide's own examples read |
| `၎င်း` | `သူ` (agent / person), `ဒါ` (thing / idea), or repeat the noun | Ambiguous after two sentences |
| `ဤ` | `ဒီ` | Register |
| `ဟူသော` / `ဟု` | `ဆိုတဲ့` / `လို့` | Register |
| `…မဟုတ်ချေ` / `…မရှိပေ` | `…မဟုတ်ပါဘူး` / `…မရှိပါဘူး` | `ချေ/ပေ` is archaic |
| `X ခြင်းသည် Y ခြင်းဖြစ်သည်` | `X ရင် Y တယ်` or `X တာက Y ပါ` | Nominalised chains read as translation |
| `အကောင်အထည်ဖော်` for *run / execute* | `run တယ်` or `လုပ်တယ်` | Calque of "implement" |
| `ဖန်တီး` for *create code* | `ဆောက်တယ်` / `ရေးတယ်` | `ဖန်တီး` is artistic creation |
| Four-syllable compounds (`ထုတ်ဖော်ပြောဆိုခိုင်းခြင်း`) | Two syllables (`ထုတ်ပြောခိုင်းတာ`) | Shorter reads as human |
| Unspaced chains over ~40 characters | Space between word groups | Line breaking on phones |
| Six same-ending sentences in a row | Vary length; one idea per sentence | Rhythm |
| Burmese gloss after an English term on every use | Gloss once in parentheses, then English only | See "Terms To Keep In English" |

Before / after:

```text
Before: ၎င်းကို Software Engineering တွင် "Non-deterministic" ဟု ခေါ်သည်။ ဆိုလိုသည်မှာ တူညီသော မေးခွန်းကို မေးသော်လည်း အဖြေမှာ တစ်ခါနှင့်တစ်ခါ မတူဘဲ ပြောင်းလဲနေခြင်း ဖြစ်သည်။
After: ဒါကို Software Engineering မှာ Non-deterministic လို့ ခေါ်ပါတယ်။ မေးခွန်း တစ်ခုတည်းကို ထပ်မေးရင် အဖြေ တစ်ခါနဲ့ တစ်ခါ မတူဘူး ဆိုတဲ့ သဘောပါ။
```

Pronoun: `ကျွန်တော်တို့` is the default in technical prose. If a chapter already uses `ကျွန်ုပ်တို့` throughout, keep it consistent within that chapter.

## Machine-Prose Patterns To Avoid

These shapes are fine once per chapter. Repeated, they make prose read as generated no matter how good the Burmese is. Search for them before opening a PR.

| Pattern | How to spot it | Fix |
|---|---|---|
| Negation reflex: `X မဟုတ်။ Y ဖြစ်သည်။` | Search `မဟုတ်။` | Keep the one that carries the chapter thesis. State the rest positively. |
| Negation headings: `### Metrics သည် ဂဏန်းသေတ္တာမဟုတ်` | Read the headings alone | Name the thing, not what it is not. |
| Em-dash subtitle headings: `### Thing — clever gloss` | Search `^###.* — ` | Heading is the thing. The gloss becomes the first sentence under it. |
| Staccato inventories: `A ရှိသည်။ B ရှိသည်။ C ရှိသည်။` | Three or more two-word sentences in a row | One sentence with commas, or a bulleted list. |
| Rhetorical question chains: `…သလား။ …သလား။ …သလား။` | Three or more questions back to back | One question, then say what good looks like. |
| Telling the reader how to feel: `ဤအချက်သည် အရေးကြီးသည်။`, `သင်ခန်းစာကဒီမှာပါ။` | Search `အရေးကြီးသည်။`, `သင်ခန်းစာက` | Cut the sentence. The next sentence should show it. |
| Praise-then-pivot: `ဒီ design သည်လမ်းမှန်ဖြစ်သည်။ သို့သော်…` | Search `ဖြစ်သည်။ သို့သော်` | Say what is wrong directly. |
| Closing flourish: `…ပင် ဖြစ်ပေတော့သည်။` | Search `ဖြစ်ပေတော့သည်` | End on the fact. |
| Blockquote TL;DR at the top of a chapter | `>` in the first ten lines | Either every chapter has one written as a real paragraph, or none do. |
| Bold-term-colon bullets carrying prose: `- **Term:** two full sentences` | Count `- **` per chapter | Glossary and Source Notes only. Prose goes in a paragraph. |

Two searches find most of it: `မဟုတ်။` and three `သလား။` in a row.

Chapter 04 has none of these and is the reference.

## Suggesting Chapter Edits

The author voice matters. For large prose changes:

1. Open an issue first.
2. Quote only the small sentence or section you want to discuss.
3. Explain why it is confusing.
4. Suggest a replacement in the same tone.
5. Wait for maintainer direction before opening a rewrite PR.

Before / after:

```text
Before: "This whole section is weak. I rewrote it."
After: "This paragraph may be hard for beginners because Planner and Worker are introduced together. Could we split it into two shorter examples?"
```

```text
Before: PR ထဲမှာ chapter တစ်ခုပြီးတစ်ခု prose အကုန်ပြန်ရေးခြင်း။
After: Issue ဖွင့်ပြီး confusing part, reason, suggested direction ကို အရင်ဆွေးနွေးခြင်း။
```

## Writing Examples

Examples should be:

- small
- safe by default
- realistic
- beginner-readable
- clear about assumptions

Avoid examples that mutate real systems unless clearly marked as lab-only.

Before / after:

```text
Before: Run this script to delete old production resources.
After: Lab-only example: print the resources that would be deleted, then require human approval before any real delete action.
```

```text
Before: The agent can deploy automatically.
After: The agent can prepare a deployment plan, run checks, and ask a human to approve before deploy.
```

## Beginner-Friendly Explanation

When explaining a hard concept:

- start with the problem
- give a simple mental model
- show one small example
- mention the risk or limitation
- avoid pretending the topic is easier than it is

Before / after:

```text
Before: MCP is a protocol for model-context interoperability.
After: MCP ကို model နဲ့ tools ကြားက standard connection layer လို့ စဉ်းစားနိုင်တယ်။ Server က tool တွေ expose လုပ်တယ်၊ client က model နဲ့ချိတ်ပြီး သုံးတယ်။
```

```text
Before: Context Engineering is prompt optimization.
After: Context Engineering က prompt တစ်ကြောင်းပြင်တာထက် ပိုကျယ်တယ်။ Model ကို ဘာ information ပေးမလဲ၊ ဘာဖယ်မလဲ၊ tool result ကို ဘယ်လိုပြမလဲဆိုတာအထိ ပါတယ်။
```

## Pull Request Rule

Large prose rewrites need issue discussion first.

Small typo fixes and support-file improvements can go directly to PR.
