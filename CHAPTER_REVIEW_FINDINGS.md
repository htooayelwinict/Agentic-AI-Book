# Chapter Review Findings (full manuscript, read-only)

Date: 2026-10-24
Scope: `book/chapters/00-preface.md` through `19-references.md`, checked against `STYLE_GUIDE.md` and the four case-study repos under `repo_sources/`.
Method: five parallel reviewers, one block of chapters each, plus a cross-chapter mechanical pass (headings, assets, register counts, term variants). No chapter files were modified.

This report is review output only. Per `STYLE_GUIDE.md`, large prose changes should be discussed before any rewrite PR.

---

## Part 1 — Synthesis

### 1.1 Overall verdict

The ideas are right and the technical claims are overwhelmingly accurate. Across roughly 60 repo-anchored claims checked (class names, file paths, state fields, env flags, test names), every named artifact exists; only a handful of claims overstate (listed in 1.4). The through-line metaphor (စာရေးတော် → လက် → လက်နက်တိုက်စောင့် → ခြေရာ → တံခါးစောင့်) gives the book a real narrative, and the honesty about limits ("wrapper is not a guarantee", "run ≠ got data", "not production") is consistent and rare.

The improvement work is therefore not about correctness. It is about four things:

1. **Register.** The body prose does not use the register the author's own style guide prescribes.
2. **Concreteness.** Chapters 01–04 (the foundation) have zero code, zero tables, zero diagrams; chapter 12 (a code case study) shows no code.
3. **Duplication and length.** Several lessons are defined three to five times across chapters; chapters 13–15 restate their thesis repeatedly and could lose 25–45% with no loss of content.
4. **Finish.** Internal markers, author-to-self notes, slug headings, HTML entities and stale cross-references leaked into reader-facing text.

### 1.2 The register finding (highest leverage)

`STYLE_GUIDE.md` gives every "After" example in the conversational developer register (`…ကို ခေါ်ပြီး task ကို ဆက်လုပ်တယ်`, `…ပေးတာပါ`). The chapters are written in the literary register.

| Chapter | sentences ending `သည်။` | `တယ်။` | `ပါ။` | archaic `ချေ` |
|---|---|---|---|---|
| 01 | 54 | 0 | 2 | 6 |
| 02 | 46 | 0 | 4 | 7 |
| 03 | 39 | 1 | 1 | 6 |
| 04 | 31 | 2 | 0 | 4 |
| 05 | 103 | 0 | 6 | 3 |
| 06 | 99 | 0 | 5 | 2 |
| 07 | 86 | 0 | 15 | 0 |
| 08 | 72 | 0 | 8 | 2 |
| 09 | 69 | 0 | 10 | 0 |
| 10 | 91 | 0 | 9 | 1 |
| 11 | 90 | 0 | 10 | 2 |
| 12 | 121 | 0 | 27 | 1 |
| 13 | 146 | 0 | 24 | 9 |
| 14 | 247 | 0 | 41 | 4 |
| 15 | 173 | 0 | 29 | 16 |
| 16 | 80 | 0 | 30 | 3 |
| 17 | 11 | 0 | 85 | 0 |
| 18 | 27 | 0 | 37 | 0 |
| **Total** | **1,685** | **3** | **343** | **66** |

Three observations:

- This is a deliberate authorial voice, not machine translation. The metaphors are strong and should be kept.
- But every reviewer independently flagged the same passages as the ones that read "machine-made": 40–60-character unspaced word chains, six consecutive `…သည်။` staccato sentences (e.g. `09:29`, `10:95`), `ခြင်း`-chains (`08:7`, `16:61`), archaic particles (`ချေ`, `ပေသည်`, `ပါလော့`, `ဟူသော`, `၎င်း`, `ဤ`), and calqued verbs (`အကောင်အထည်ဖော်` for *run*, `မြှင့်တင်` for *cost increase*, `လေ့ကျင့်` for *prompt/configure*).
- The author already writes in the guide's register in the "Beginner အနေနှင့်…" asides (`05:11`, `05:56`, `06:7`), the Mini Labs, and chapter 17. Those passages read better than the body around them.

**Recommended decision:** keep the literary voice for chapter openers and metaphor paragraphs; write every *definitional and technical* sentence in the guide's plain register. Document this split in `STYLE_GUIDE.md` so contributors can follow it. Independently of that decision: remove `ချေ`/`ပေသည်`/`ပါလော့`/`ဟူသော`/`၎င်း`, break the staccato runs with connectives, split sentences over ~25 words, and replace `ကိရိယာ`/`ကိုယ်စားလှယ်` with `tool`/`Agent` as the guide already requires.

### 1.3 Tier 1 — mechanical fixes (safe, no voice change, do first)

| # | Issue | Where |
|---|---|---|
| 1 | Every chapter H1 is the filename slug (`# 01-agentic-ai-basics`). `scripts/build_book_pdf.py:50-53` reads this H1 for the PDF table of contents, so the printed TOC shows slugs. | all `book/chapters/*.md` line 1 |
| 2 | HTML entities in Markdown source (`&amp;`, `&gt;`) render literally. | `02:47`, `03:63`, `04:54`, `13:151`, `16:39`, `16:153-154` |
| 3 | Internal markers in reader text: `[SOURCE_NEEDED]` (evidence already exists at `19:70`), `[SYNC_MISMATCH]`. | `06:139`, `07:81`, `12:205` |
| 4 | Stale file reference `CHAPTER-7.md` (the real file is `07-context-engineering-memory-rag.md`). | `14:89`, `14:163`, `19:16` |
| 5 | Author-to-self editorial notes ("this book will not present X as…", "reader review said…"). | `09:73`, `09:101`, `11:82`, `11:100`, `11:110`, `11:112`, `14:111`, `17:93` |
| 6 | "v0.2" promises the reader cannot act on. | `12:13`, `12:252`, `13:13`, `17:334` |
| 7 | Broken back-reference: `07:132` cites "အခန်း ၀၃" for embeddings/attention; ch03 has none. | `07:132` |
| 8 | Node name mismatch: `run_worker` vs `run_agent` (ch13 and Travis-2 use `run_agent`). | `08:104` vs `08:146`, `13:7` |
| 9 | Dangling `n8n` reference, never introduced anywhere else in the book. | `18:17` |
| 10 | Spelling: `ပက်သက်`→`ပတ်သက်`; `အကြမ်းဖျဉ်း`/`အကြမ်းဖျဉ်း`→`အကြမ်းဖျင်း`; `လက်ဆွဲစာအုပ်`→`လက်စွဲစာအုပ်`; `လျင်`→`လျှင်`; `တခု`→`တစ်ခု`. | `05:54`, `06:85`, `07:109`, `15:142` |
| 11 | Bare-line "lists" written as separate paragraphs with no `-`. | `09:83-93`, `10:45-53`, `10:81-89`, `11:84-98`, `11:134-148` |
| 12 | `CITATION_VERIFICATION_MAP.md:66` points to a non-existent `book/CITATION_VERIFICATION_TODO.md`. | support file |
| 13 | References hygiene: missing OpenClaw `THIRD_PARTY_NOTICES.md` URL (relied on at `15:13,138,193`); orphan "Shwe U Daung" entry cited nowhere; private draft filenames listed without saying they are unpublished; duplicated license block; MCP spec pinned to `2025-06-18` with a newer revision available. | `19-references.md` |
| 14 | Hard-coded year in example (`"Myanmar population 2024"`). | `04:19` |

### 1.4 Tier 2 — technical corrections

| Where | Problem | Fix |
|---|---|---|
| `02:27` | Defines **Orchestration** as constraints on the agent (spending limit, "ask me first"). That is Guardrails/Harness/HITL. `03:33` and `02:51` use Orchestration in its normal sense (coordinating steps/tools). | Rename `02:27` to Harness/Guardrails, forward-ref ch05/09. |
| `02:19` | `ကိုယ်ပိုင်အသိ (Autonomy)` reads as self-awareness; and "if not reached, retries from the beginning" contradicts `04:31` (loop continues from current state). | `ကိုယ်ပိုင်ဆုံးဖြတ်ခွင့်`; "looks at the result and decides the next step". |
| `04:25` | "Chain of Thought significantly reduces hallucination, we found" — overclaim, uncited, conflates ReAct with CoT; most 2026 models have built-in reasoning. | Reword to accuracy-on-multi-step tasks; cite Wei 2022 / Yao 2022. |
| `04:55` | Source note says Stop Sequences end action calls. That is legacy text-ReAct; native tool calling uses `stop_reason`/`finish_reason`. | Replace or label historical. |
| `04:31` | "Can work for hours/days without human supervision" presented as a feature; contradicts `01:47` and ch09/11. | Hedge: *can* vs *should*. |
| `01:37` | Lists "writing code" as a tool. The tool is code *execution*; the model writes. Matters because `03:57` introduces PTC on exactly this distinction. | |
| `01:49`, `02:35` | "train the LLM" — readers prompt/configure/constrain, they do not train. | |
| `03:9` | JSON called a "language". | "data format". |
| `03:43-47` | Security example is the model inventing an *undefined* tool (`delete_user`). Runtimes reject unknown names trivially; the realistic risk is a *defined* tool with harmful arguments or injection-steered arguments. | Reframe; forward-ref ch09/11. |
| `03:19` | Type constraints put in `description`; they belong in the JSON Schema (`"type": "integer"`), and the runtime must validate against the schema. | |
| `06:66-77` | MCP primitives defined as read-vs-write; "reading a GitHub issue = Resource" is misleading (real servers expose reads as Tools). Correct distinction is *who controls*: Tool = model decides, Resource = host/app attaches, Prompt = user picks. Webpage content via a browser tool is tool output, not an MCP Resource. | Reframe; add host↔multiple clients↔servers to the diagram. |
| `06:83`, `06:111` | Skills described as whole-file injection; progressive disclosure (name+description always; body on match; files on demand) is the defining mechanism, presented here as optional. | |
| `06:107`, `07:96` | "Compaction may forget the rules" — in a sound harness, system-level instructions live outside compacted history. Risk is real only if rules sit in a user message. | State the architectural fix. |
| `08:60` | "untrusted advisory" uses *untrusted* in the fallible sense; elsewhere the book uses it in the hostile-data sense. | "advisory / fallible". |
| `10:67-73` | Section title "Test becomes Observability" conflates verification with runtime inspection. The real point (offline provider makes the runtime inspectable) is good. | Retitle; one sentence separating test vs trace. |
| `10:117-132` | `args_hash` advice: hash lets you detect repeats, not reproduce the call; teams keep a redacted sample too. | One sentence. |
| `11:33` | "OWASP says…" without naming it. | OWASP Top 10 for LLM Apps, LLM01; point to `19:54`. |
| `11:47-53` | Says wrapper is not sufficient but not *why*. | Models do not reliably honor delimiters; wrapper lowers probability, not a hard boundary. |
| `12:100` | "Admin-only fields **cannot** be included at schema level" — `TypedDict(total=False)` has no runtime enforcement; the guarantee comes from the bridge constructing a fresh two-key dict. `12:199` hedges correctly; `12:100` should match. | |
| `12:31`, `12:55`, `12:94`, `12:133` | Metaphor says the bridge *rewrites* a safe message (`ပြန်ရေး`, `ပြန်မွေး`); code copies `admin_input` verbatim (`nodes.py:219`). `12:203` already admits a secret in `admin_input` would cross. | "copies one field, drops the rest". |
| `12:59-92`, `12:129` | Diagram shows one hop; code has two (`bridge` → `bridge_admin_input` → `customer_from_bridge`, `runtime.py:56-85`). Supervisor and `LLMTaskClassifier` are conflated; when route is `route_bridge` the supervisor worker never runs. | |
| `12:231-234` | Exercises ask readers to write tests that already exist in `tests/test_runtime.py:52-106`. Exercise at `12:23` uses `origin="user_cli"`, which `GlobalState.origin` cannot even hold; the repo test uses `admin_cli`. | Point to the tests; make exercises *extend* them. |
| `12:205` | Warns about docs drift abstractly. Two verified drifts exist: `ARCHITECTURE-ROUTING.md:83-86` claims a keyword guard that `classifier.py` lacks (it lives only in the offline model); `README.md:60-61` says the Supervisor "extracts public info" but the bridge branch forwards untouched. | Name them; stronger lesson. |
| `13:10` vs `13:320` | Tool-output sanitization listed as a policy control; it is **off by default** (`TRAVIS2_TOOL_SANITIZATION_ENABLED=false`, `.env.example:89`). AST validation likewise default `false` (`.env.example:88`). | State defaults. |
| `13:215-228` | "Separate Docker network" — sandbox container has internet (`internet_enabled=True`, `docker_runner.py:309`). Beginners will read "sandbox network" as "no network". | |
| `13:367` | "Silent fallback to host mode" listed as hypothetical; it is real: `tools.py:464-469` treats any value other than exactly `docker` as host mode with no warning. | Promote to a verified gotcha. |
| `13` (omission) | Search-engine blocking is enforced at tool execution time (`tools.py:73,244`, `warnings=["blocked_search_engine"]`) — the clearest "policy in the execution path" example in the repo, unused. | |
| `14` (omission) | Chromium launched with `--disable-web-security` (`repo_sources/bot/src/session/__init__.py:33`). The repo's own security report calls it out. A chapter titled "browser tool agent security" never mentions that same-origin policy is off. | Add one paragraph. |
| `14:246` | HITL `interrupt_on` covers navigate/submit/close/evaluate; `browser_click`, `browser_type`, `browser_handle_dialog` are **not** gated, though screenshot 14-2 argues a settings click is a mutation. | Say so; closes the argument. |
| `14:254-260` | Security report (2026-01-20) says output sanitization "Missing"; `src/tools/security.py` now exists. Reader opening the report sees a contradiction. | One sentence: report predates wrapper. |
| `14:161` | `MemorySaver` "may not be" restart-proof — it is definitely in-memory. | |
| `15:130` | Claims the Pi/Hermes import boundary is tested. `tests/test_no_appv21_coupling.py` only checks `appv21` tokens. | Narrow the claim. |
| `15:156`, `15:163` | Recovery audit presented as current; its NEXT_PATCH (`test_app_integration.py`) already exists. | Date-stamp the audit. |
| `15:110` | `/compress` vs audit's `/compact`; source accepts both. | Mention both once. |
| `02:17`, `03:37`, `04:31` | Examples let the LLM delete email / send email / run unsupervised — violates `STYLE_GUIDE.md` "safe by default". | Archive/label; draft + approval; hedge. |

### 1.5 Tier 3 — structural improvements

**A. Chapters 01–04 need one concrete artifact each.** They are the foundation and currently contain 0 code blocks, 0 tables, 0 diagrams. Specifically:
- `01`: a one-sentence plain definition of Agent (LLM + tools + loop + goal) next to the metaphor; define *token* in Burmese once (used for billing in `04:37` but never defined).
- `02`: an Automation / Workflow / Agent comparison table (who decides next step, determinism, cost, when to use, dev example). The chapter title promises this comparison and never delivers it side by side. "Workflow" is used in three senses (`02:13`, `02:15-17`, `02:39`).
- `03`: one real, simplified, labelled tool definition (name / description / JSON Schema) and a 5-step round-trip diagram (user → model → tool_use → harness runs → tool_result → model → answer). The chapter stops at "send 15 back".
- `04`: the 8–10 line minimal loop pseudocode. This is the book's central chapter and the shortest; everything in 05–11 hangs on readers seeing `while not done: reply = model(messages, tools) …`. Name the state (`messages`) and the termination condition.
- Thread one developer example through 01→04 (coding agent: failing test → read error → edit → rerun) alongside the flowers/population stories.

**B. Introduce the four case-study repos once, before chapter 05 uses them.** `05:53-102` dumps 15+ class names (`GlobalState`, `TrajectoryCallbackHandler`, `ModelCallLimit`…) seven chapters before those repos are explained, and the author has to tell readers twice not to memorize them (`05:56`, `05:92`). Same pattern in `06:121`, `07:60-82` (the "better prompt" example is about writing *this book's* chapter 12 from P-2 internals), `08:60`, `08:95`, `09:47-101`. Fix: a one-paragraph introduction of the four repos in the preface or at the top of ch05; strip class-name lists from 05–11 and leave chapter pointers ("အခန်း ၁၄ မှာ").

**C. Give each lesson one owner chapter.** Currently:
- Untrusted-output *wrapper* is fully defined in `11:47`, `11:162`, `14:193`, `16:113`, `17:111`.
- *Faux/fake provider* defined in `15:90`, `16:267`, `17:276` (three names: faux provider, fake model, fake provider).
- `AGENTS.md`/`SKILL.md`/compaction section duplicated almost one-for-one: `06:101-111` ≈ `07:94-111`.
- Browser-tool risk list, approval dialog, skill supply chain, "schema mismatch is a feature": each appears in both ch09 and ch11 (`09:67-101` ↔ `11:78-124`), and the last also at `12:242`.
- CI failure walkthrough appears twice in ch16 (`16:17-28`, `16:202-208`).
Pick the owner, keep a one-line pointer elsewhere.

**D. Cut chapters 13, 14, 15 by 25–45% without losing content.**
- ch13 (42 KB): thesis "run ≠ got data" stated five times (`13:4`, `13:23`, `13:33-35`, `13:193-204`, `13:415`). `AgentState` table lists 12 fields, 3 are used. Middleware list has 8 bullets, 1 is explained. Reorder to match its own reading guide (problem → tool contract → where it runs → gates → control plane). Replace the 12-item failure checklist with the two verified gotchas. Target ~27 KB. Full proposed outline in Part 2, block 13–14.
- ch14 (56 KB): 14 component sections each ending "X is useful but not a guarantee" (`14:199, 209, 217, 236, 242, 248`). Screenshot section is 9 KB; three of five images teach the same lesson. Lab is duplicated (`14:17-23` and `14:301-314`). Collapse into five security lessons + a tool-risk table (from the security report's 22-tool inventory) + a "component | does | does not guarantee" table. Target ~31 KB.
- ch15 (41 KB): "not production / not a final kernel" five times (`15:7, 38, 104, 154, 175`); "inspiration ≠ dependency" three times; "six lessons" section restates every prior section and the conclusion restates the lessons. Hook (`15:42-46`, "day one beautiful, day two context fills") is buried after personal history; move it first. Compaction timing (`15:106-114`) as a 4-row table.
- Each should end with transferable principles, not a repo-specific bullet recap. Chapter 12's "Design Pattern များကိုနာမည်တပ်ခြင်း" (`12:211`) is the model already in the book.

**E. Chapter 12 should show the code it is about.** `BridgeNode.invoke` is 8 lines (`nodes.py:213-220`); `UnsafeState` is 7 (`states.py:19-25`). Start the "how to read" section with the offline command `multi-agent-cli --mode admin --model-mode offline` (`models.py:29-79`, no API key needed). Explain `ReadOnlyScopedNode`'s `interrupt_on` auto-reject (`nodes.py:66-147`) — it is the single most concrete illustration of ch09 mutation scope and ch11 HITL in the whole repo, and its `while __interrupt__` loop has no iteration cap (`nodes.py:126-140`), which is exactly ch11's loop-safety lesson occurring in the case study itself.

**F. Make chapter 17's labs runnable.** No lab states prerequisites, Python version, or whether a real LLM is needed (critical for Myanmar readers without payment access). No lab has expected output; `16:21-28` has exactly the right format. Only Lab 4 has a code skeleton. The announced `Build → Safe Failure Test → Fix → Reflect` frame is followed only by Lab 1. Order is not by difficulty (Labs 4 and 8 are easier than 3 and 5). Labs reference repos by name, never chapters by number; ch18 never mentions ch17.

**G. Make chapter 18 live up to its title.** Zero mentions of internet, payment, hardware, cost, free tiers, local models, or connection stability. The book already contains every lesson needed for a "Myanmar constraints" section: payment/API access → faux-provider-first (ch15/17); bandwidth → read `repo_sources/` offline; connection drops → session persistence (appv22). Add a Stage | Chapters | Labs | Milestone table. Switch Pali ordinals (`ပဉ္စမ / ဆဋ္ဌမ / သတ္တမ`) to numerals.

**H. Chapter scaffolding across the book.** Human-readable H1s; a one-line "ဒီအခန်းမှာ ဘာသိသွားမလဲ"; 3–5 Burmese takeaway bullets; chapters 01–07 have no Mini Lab while 08–11 do; Source Notes are English-only in 01–03, Burmese-headed in 04, and list concepts absent from the body (Zero-shot/Few-shot, Tokenization). Preface lacks "who this is for / what you need / how to read" even though `README.md:48-64` has it. The preface tool/model list (`00:19-50`) has no stated purpose and mixes model names with reasoning-effort settings; make it a dated colophon.

### 1.6 Consolidated terminology table (highest-frequency inconsistencies)

| Concept | Variants seen | Recommended |
|---|---|---|
| Agent | Agent; ကိုယ်စားလှယ် (glossed and unglossed); ကိုယ်စားလှယ်စနစ် | `Agent` (guide) |
| Tool | tool; ကိရိယာ; လက်နက်ကိရိယာ; ကိရိယာတန်ဆာပလာ | `tool` (guide) |
| Agent loop | Agent Loop; Agentic Loop; Reasoning Loop; ကွင်းဆက် | `Agent Loop` |
| Harness gloss | ထိန်းကျောင်းမှုစနစ်; ထိန်းကျောင်းရေးစနစ်; control layer; policy plane; လက်ထောက်; ကြီးကြပ်ရေးမှူး; Runtime | `Harness` + "control layer" once |
| Orchestration | constraints (02:27); multi-tool sequencing (03:33); frameworks (02:51) | normal sense only |
| Human approval | Human approval; human approval; လူ့အတည်ပြုချက်; Human-in-the-loop; HITL; Approval gate; operational gate | `human approval (HITL)` once, then one form |
| Tool Broker role | Tool Broker; gatekeeper; လက်နက်တိုက်စောင့်; တံခါးစောင့်; runtime broker; permission broker | `Tool Broker` + one Burmese image |
| Trajectory | Trajectory; ခြေရာ; လမ်းကြောင်း; tool trace | `trajectory`, gloss ခြေရာ |
| Skill gloss | လက်စွဲစာအုပ်; အလုပ်ခွင်စည်းကမ်းစာအုပ်; အလုပ်ခွင်လက်စွဲ; လက်ဆွဲစာအုပ် (typo) | `လက်စွဲစာအုပ်` |
| Sub-agent gloss | အငယ်စားလက်ထောက်; အလုပ်ခွဲလက်ထောက်; worker (collides with PWV Worker role) | pick one; say in ch08 the Worker *role* may be a sub-agent |
| Observation | Observation (စောင့်ကြည့်ချက်) [= surveillance]; အချက်အလက်သစ် | `Observation` (ရလဒ်) |
| Untrusted | hostile data (05, 06, 11); fallible advice (08:60) | reserve for hostile data |
| Faux provider | faux provider; fake model; fake provider | `faux provider` |
| Output wrapper | sanitization; sanitizer; wrapper; output boundary; အကာအကွယ်အိတ် | `wrapper` (concept), `sanitizer` (code) |
| Controlled runtime | Controlled Runtime; ထိန်းထားသော runtime; controlled-runtime | one |
| Memory | Memory; မှတ်ဉာဏ် | `Memory` (guide) |
| Agent counter | Agent တစ်ခု / Agent တစ်ယောက် (within ch12) | `ခု` unless metaphor is live |
| Spelling | ပက်သက်/ပတ်သက်; အကြမ်းဖျဉ်း/အကြမ်းဖျဉ်း/အကြမ်းဖျင်း; လက်ဆွဲ/လက်စွဲ | correct forms |

### 1.7 Suggested order of work

1. Tier 1 mechanical fixes (one PR; no voice change; ~1 hour).
2. Register decision written into `STYLE_GUIDE.md`.
3. Tier 2 technical corrections (one PR per chapter block).
4. Structural A (ch01–04 artifacts) and B (introduce repos once) — these change what every later chapter can assume.
5. Structural C (de-dup) then D (cut 13/14/15) — de-dup first so cuts don't remove the last copy of a lesson.
6. E, F, G (ch12 code, ch17 labs, ch18 Myanmar section).
7. Terminology pass last, after prose has settled.

---

## Part 2 — Full reviewer reports by block

The five block reports follow verbatim. Line numbers refer to the files as of 2026-10-24.

### Block 00–04

Reviewer note: Chapters 01–04 are written in a literary, essayistic Burmese register with sustained metaphors (စာရေးတော်, ကြက်တူရွေး, ကပ္ပတိန်, "လက်"). This is a real authorial voice, not machine translation, and the metaphors are the strongest thing in the block. But it is the exact register `STYLE_GUIDE.md:20-26, 61-67` labels "Before". The highest-leverage single decision for this block is: keep the literary voice for openers and metaphors, but write every definitional/technical sentence in the guide's plain developer register.

#### 00-preface.md

Summary. A personal note (50 lines): why the author wrote the book, a disclaimer that it is an introductory, non-production guide partly drawn from LangChain docs and the internet, then two code blocks listing software and LLM models used. It does not yet serve the reader who wants to know how to use the book.

Structural issues.
- No "who this is for / what you need / how to read" section. README.md:48-64 has all of this, but a reader opening the manuscript from `00-preface.md` never sees it.
- Lines 19-50: the tooling/model list has no purpose statement. "gpt-5.5 high / xhigh" (L47-49) and "gpt-5.3-codex-spark xhigh" (L45) are model + reasoning-effort settings, not model names. Suggest a dated "Colophon" paragraph moved to the end.
- L9: "LangChain documentation website နှင့် Internet ရှိ အချက်အလက်များကို ကိုးကားထားခြင်း" is a vague source claim. Point to `19-references.md`.
- H1 is the file slug.

Language quality.
- L3 is one 4-clause sentence spanning 3 lines. Split: "ကျွန်ုပ်က ပျင်းတတ်သူပါ။ စာအများကြီးကို စနစ်တကျ ရေးရတာ၊ နည်းပညာအချက်အလက်တွေ စုပြီး ပြန်ရေးရတာကို သိပ်မဝါသနာပါပါ။ ဒါပေမဲ့ ခိုင်မာတဲ့ ရည်ရွယ်ချက်တစ်ခုကြောင့် ဒီစာအုပ်ကို အပင်ပန်းခံ ရေးခဲ့ရပါတယ်။"
- L9 "မန်နျူရယ်" transliteration → "Production manual လည်း မဟုတ်ပါ။"
- L15 single 50-word sentence → "ဒီစာအုပ်က Agentic AI အခြေခံမိတ်ဆက်သာ ဖြစ်ပါတယ်။ ထဲမှာပါတဲ့ ဥပမာတွေနဲ့ GitHub repo တွေက သင်ကြားရေးအတွက်သာ ရည်ရွယ်ပါတယ်။ Production code အနေနဲ့ မသုံးပါနဲ့။"

Top 3: (1) add "ဒီစာအုပ်ကို ဘယ်လိုဖတ်မလဲ" section (audience, prerequisites — Docker Desktop is listed at L29 but never explained, chapter map); (2) dated colophon with purpose; (3) split L3, L11, L15.

#### 01-agentic-ai-basics.md

Summary. Punctures the "AI" buzzword and scopes to LLMs (L7), short history (L11-25), next-token prediction via parrot/clerk, defines agentic AI as "letting the parrot out of the room" with three ingredients (L33-39), closes with hallucination and Harness (L43-49). The skeptical tone is a real strength.

Structural issues.
- No crisp definition of "Agent" anywhere. L29 defines by metaphor only. Add: "Agent ဆိုတာ LLM + tool + loop + goal ပါ။ Model က ဘာလုပ်မလဲ ဆုံးဖြတ်၊ tool ခေါ်၊ result ကြည့်၊ ထပ်ဆုံးဖြတ် — goal ရောက်တဲ့အထိ။"
- Only agent example is the flowers story (L29-31). Add a developer-facing one ("failing test ကို fix ပေးပါ").
- Three components (L33-39) omit the loop, which 04 introduces as the missing piece.
- "Token" never explained in Burmese anywhere in 01–04, yet 04:37 bills the reader by tokens.
- Harness (L47) and Context (L15, L21) appear before definition.
- Source Notes (L53-60) English-only, list concepts absent from the body.
- No takeaways, no exercises.

Technical accuracy.
- L13 places rule-based AI "ထိုစဉ်က" in Turing's time (1950); AI as a term dates from 1956.
- L13 "Software Engineering ၏ အကန့်အသတ်" frames determinism as a limitation of SE; 02:39 correctly prefers deterministic automation. → "rule-based system ရဲ့ အကန့်အသတ်".
- L15 implies neural nets arose to fix language and early ones were RNNs; NNs predate RNNs by decades.
- L17 "reads the whole sentence at once" vs L23 "emits the next word" read as contradiction. Add: "input ကို တစ်ပြိုင်နက် ဖတ်တယ်၊ output ကိုတော့ token တစ်လုံးချင်း ထုတ်တယ်။"
- L35 labels all of Reasoning as "(Reflection)"; planning is the other half.
- L37 "ကုဒ်များ ရေးသားခြင်း" listed as a tool; the tool is code execution.
- L49 "လေ့ကျင့်" (train) is the wrong verb; same at 02:35.
- L25 consciousness claim stated as fact; hedge lightly.

Language (worst, with rewrites).
- L7 → "ဒီစာအုပ်မှာ AI လို့ ပြောတိုင်း နောက်ကွယ်က တကယ်အလုပ်လုပ်နေတဲ့ engine — **LLM (Large Language Model)** — ကိုပဲ ဆိုလိုပါတယ်။"
- L33 → "LLM ကို Agent ဖြစ်လာအောင် အောက်ပါ အပိုင်းသုံးခုနဲ့ ပေါင်းပေးရတယ် -"
- L35 → "အလုပ်မလုပ်ခင် model ကို 'ဘာလုပ်သင့်လဲ'၊ လုပ်ပြီးရင် 'မှန်ရဲ့လား' လို့ ကိုယ့်ဘာသာ ပြန်မေးခိုင်းတာ (Reflection)။"
- L47 → "Engineer ရဲ့ အလုပ်က hallucination ကို ဘောင်ခတ်ဖို့နဲ့ Agent မှားမဆုံးဖြတ်မိအောင် **Harness** (model အပြင်ဘက်က control layer) ဆောက်ဖို့ပါ။ Chapter 05 မှာ အသေးစိတ်ပြောပါမယ်။"
- L49 ", နှင့်" before last list item is an English "and" calque. → "နောက်အခန်းတွေမှာ ဒီ 'စာရေးတော်' ကို ဘယ်လို ခိုင်းမလဲ၊ ဘယ်ဘောင်ထဲ ထားမလဲ၊ ဘယ် technique တွေနဲ့ စွမ်းရည်မြှင့်မလဲ ဆွေးနွေးပါမယ်။"

Consistency. Four metaphors for the LLM in one chapter (စက်ရထား, စာစီစာကုံးသမား, ကြက်တူရွေး, စာရေးတော်) plus လူမိုက် for the agent; 03:19 then claims "LLM = လူမိုက်" which is not what 01 said.

Top 3: (1) plain Agent definition + developer example; (2) fix factual slips L13/L15/L17/L37/L49; (3) define Token; takeaways + 2 reflection questions; Burmese Source Notes with citations.

#### 02-agent-vs-workflow-vs-automation.md

Summary. Train vs ship-captain metaphor (L5-9); three tiers (L13-19); non-determinism and the drunk captain (L21-27) introducing "Orchestration"; tools as hands, "model calls, harness executes" (L29-35); decision heuristic (L37-41). Valuable: helps beginners decide whether they need an agent at all.

Structural issues.
- Title promises a three-way comparison; body never puts Automation, Workflow and Agent side by side. "Workflow" used three ways (L13, L15/17, L39). Add a table (who decides next step, determinism, cost, when to use, dev example). Aligns with Anthropic's "workflows vs agents" and is worth citing.
- L13 "အဆင့်သုံးဆင့်" (three steps) — they are three kinds.
- L39-41 heuristic is one question; a 4-5 line checklist would make it actionable.
- No summary/exercise.

Technical accuracy.
- L27 defines **Orchestration** as constraints on the agent's decisions. That is Guardrails/Harness/HITL (ch05, ch09). 03:33 and L51 use Orchestration in the normal sense.
- L19 "ကိုယ်ပိုင်အသိ (Autonomy)" reads as self-awareness → ကိုယ်ပိုင်ဆုံးဖြတ်ခွင့်.
- L19 "အစမှ ပြန်လည် ကြိုးစားသည်" — loop does not restart; contradicts 04:31.
- L17 example lets the LLM delete email — violates safe-by-default. Use archive/label.
- L23 add one clause on sampling/temperature; temperature 0 is not guaranteed identical.
- L51 "LangChain, CrewAI, AutoGen" — add LangGraph (README names it), date the list.
- L52 MCP definition is Anthropic's wording; attribute it.

Language.
- L13 → "ဦးနှောက်ကို ဘယ်လိုသုံးမလဲဆိုတဲ့ Workflow လိုတယ်။ အမျိုးအစား သုံးမျိုး ရှိတယ် -"
- L23 → "ဒါကို Non-deterministic လို့ ခေါ်တယ်။ တူတူမေးခွန်းကို မေးရင်တောင် အဖြေ တစ်ခါနဲ့တစ်ခါ မတူနိုင်တယ်။"
- L33 (the chapter's spine sentence, wrapped in two ခြင်း nominalizations; "အကောင်အထည်ဖော်" for execute is bureaucratic) → "အရေးကြီးတာက Agent (model) က tool ကို 'ခေါ်ချင်တယ်' လို့ ပြောတာသာ လုပ်နိုင်တယ်။ တကယ် run ပေးတာက ကျွန်ုပ်တို့ရဲ့ code (Harness) ပါ။"
- L35 → "စာရေးတော်ကို tool တွေ အများကြီး ချိတ်ပေးလိုက်တာနဲ့ တူတယ်။"
- L41 → "အရေးကြီးဆုံးက ထိန်းဖို့ engineering skill ပိုလိုတယ်။"
- L3/L5 ကိုယ်စားလှယ် → keep Agent: "Automation နဲ့ Agent ကြားက ချောက်ကမ္ဘာ".

Top 3: (1) comparison table + decision checklist; fix "three steps"; (2) fix L27 Orchestration and L19; (3) non-destructive L17 example; rewrite L33 plainly.

#### 03-llm-tool-calling-function-calling.md

Summary. LLM as scholar who can only write (L5-9); Tool Definition "contract" with `add_numbers` and simplified JSON (L11-19); why tools beat raw inference, over-reliance, multi-tool orchestration (L21-37); security (L39-49); state of the art and PTC (L51-57). The "model writes an order, runtime executes" framing is right.

Structural issues.
- No real tool definition shown. Show `name`, `description`, `input_schema` (JSON Schema with `type: integer`) once, labelled simplified, with a note that field names differ by provider.
- Round trip stops at "send 15 back" (L17). Finish it with a 5-step sequence diagram.
- Over-reliance fix is "System Prompting" only; mention `tool_choice`.
- L57 PTC arrives without problem framing (each tool call is a round trip; big results flood context). Register jumps.
- Source Notes L65-70: Zero-shot/Few-shot never appear in the body; Parallel Tool Calling deserves one body sentence; L69 is Burmese, rest English.
- No takeaways/exercises.

Technical accuracy.
- L9 JSON is a data format, not a language.
- L17 LLMs are *unreliable* at arithmetic, not incapable.
- L19 type constraints belong in schema, not description; runtime must validate against schema.
- L23 "we found tools are more effective" uncited; cite Toolformer/ReAct or soften.
- L37 "Email Tool ကို သုံးရမည်" — mutating action with no approval; make it draft + approve.
- L43-47 threat modelled as model inventing an undefined tool; realistic danger is a defined tool with harmful arguments or injection-steered arguments. Forward-ref ch09/11.
- L5 say Tool Calling / Function Calling are vendor synonyms.

Language.
- L9 → "ဒီစာက ရိုးရိုးစာ မဟုတ်ဘူး။ Program တွေ ဖတ်လို့ရတဲ့ **JSON** format နဲ့ ရေးထားတဲ့ 'အမိန့်စာ' ပါ။ ကျွန်ုပ်တို့အလုပ်က အဲဒီ JSON ကို ဖတ်ပြီး တကယ် run ပေးမယ့် code (Harness/Runtime) ရေးဖို့ပါ။"
- L19 "အဓိပ္ပာယ်ဖွင့်ဆို" calque → "Tool definition ရေးတဲ့အခါ အလွန်တိကျရမယ်။"
- L31 "'ပြန်လည်နှုတ်ဆက်ခြင်းဆောင်ရွက်သော API'" → "'greeting ပြန်ပေးတဲ့ API' ရှိလား လိုက်ရှာတတ်တယ်။"
- L47 → "Runtime က မစစ်ဘဲ အဲဒီ call ကို run လိုက်ရင်"
- L57 mixes formal and colloquial in adjacent sentences; use it as the model for re-registering the rest.

Consistency. Harness is "လက်ထောက်" L9, "Runtime" L47, "ကြီးကြပ်ရေးမှူး" L49.

Top 3: (1) real tool definition + 5-step round-trip diagram; (2) reframe security example; approval-gate the email; (3) PTC problem statement; unify register.

#### 04-agent-loop.md

Summary. Brain + hands are not enough without a loop (L5-9); ReAct Thought/Action/Observation with population lookup (L11-25); error recovery and max iterations (L27-33); token cost (L35-39); heartbeat metaphor and hand-off to Harness (L41-45). Never shows the loop.

Structural issues.
- Central chapter, shortest (56 lines), no pseudocode, no diagram. Add:
  ```
  while not done and step < MAX_STEPS:
      reply = model(messages, tools)
      if reply has tool_calls:
          results = harness.run(tool_calls)   # validate, permission, sandbox
          messages += results
      else:
          done = True
  ```
- Three names for one thing: Agent Loop, Reasoning Loop (L7), Agentic Loop (L31,33,37,43; also 02:19).
- State never mentioned: `messages` history is the working memory ch07 calls context.
- Termination described only negatively; say what "done" looks like.
- Add the coding-agent example (test fail → read → edit → rerun).
- Source Notes heading Burmese here, English in 01-03.

Technical accuracy.
- L25 CoT "significantly reduces hallucination, we found" — overclaim, uncited, conflates ReAct and CoT; 2026 models have built-in reasoning.
- L7 ordinary software has exception handling; the real difference is reading error *text* and choosing a different strategy.
- L31 "hours/days without supervision" as feature; hedge can vs should.
- L33 max iterations is the only brake; add token budget, timeout, repeated-action detection; "give up" → stop and report to a human.
- L19 hard-coded 2024.
- L55 Stop Sequences note describes legacy text-ReAct; native tool calling uses `stop_reason`.

Language.
- L5 → "အဲဒီအပိုင်းတွေ စုလိုက်ရုံနဲ့ Agent ဖြစ်မလာသေးဘူး။"
- L13 40-word ခြင်း-chain → "ReAct မှာ အဆင့်သုံးဆင့် ပတ်တယ်။ Thought — ဘာလုပ်မလဲ စဉ်းစား။ Action — tool ခေါ်။ Observation — ရလာတဲ့ result ကို ကြည့်။ ပြီးရင် ထပ်ပတ်။"
- L21 "Observation (စောင့်ကြည့်ချက်)" = surveillance; L31 glosses it differently. Keep English + "(ရလဒ်/တွေ့ရှိချက်)".
- L33 "ကုန်ကျစရိတ်များကို မြှင့်တင်" positive connotation → "API bill ကြီးသွားမယ်။"
- L39 → "အရာရာကို အသေးစိတ် စဉ်းစားခိုင်းမနေပါနဲ့။ အရေးကြီးတဲ့ အဆင့်မှာပဲ loop ပတ်ပါ။ လွယ်တဲ့အဆင့်တွေမှာ သေးပြီးမြန်တဲ့ model သုံးပါ။"
- L9, L45 "ဖြစ်ပေတော့သည်" twice.

Top 3: (1) loop pseudocode + diagram; name state and termination; (2) fix L25, L31, L55; add brakes to L33; (3) standardize "Agent Loop"; add coding-agent example.

#### Block 00–04 cross-chapter

Strengths: the spine ("model writes, harness executes") is right and consistent (02:33, 03:9, 03:49); metaphors carry across chapters; honest about limits in every chapter; good forward-referencing.

Five most important: (1) register decision applied consistently; remove ", နှင့်" calques and bureaucratic verbs; (2) one recurring dev example 01→04, tool definition + round trip in 03, loop pseudocode in 04, comparison table in 02; (3) fix definitional errors (Orchestration, Autonomy, loop restart, CoT/hallucination, Stop Sequences, "train", "writing code is a tool"); (4) safe-by-default examples (02:17, 03:37, 04:31); (5) scaffolding: real H1s, "ဒီအခန်းမှာ ဘာသိသွားမလဲ", takeaways, exercises, Burmese Source Notes with citations (Vaswani 2017; Yao 2022; Wei 2022; Anthropic "Building effective agents" 2024; modelcontextprotocol.io); define Token once.

Terminology table for this block is folded into Part 1 §1.6.

### Block 05–08

Reviewer note: the body prose of all four chapters is literary (သည်/၏/ဟူသော/ချေ/ပေ), while the "Beginner အနေနှင့်…" asides are in the plain developer register the style guide prescribes (`05:11`, `05:56`, `06:7`, `06:109`). The asides read better than the body.

#### 05-agent-harness.md

Summary. Harness as the control layer around the loop (context, permission, memory/state, safety, observability, recovery); Harness is decisions not a framework; previews how the four repos implement a harness; 7-item checklist and 10-question audit.

Structural issues.
- Case-study repos appear here for the first time with no introduction (`05:53-60`); `05:60` uses `GlobalState`, `UnsafeState`, `secret_context`; `05:82`/`05:90` dump 15+ class names. Author tells readers twice not to memorize them (`05:56`, `05:92`). A third of the chapter (`05:58-102`) is re-taught in ch12–15.
- Four competing metaphors: drunk captain + radar (`05:7`), house/engineer (`05:15-19`, repeated almost verbatim), scribe's desk vs workshop (`05:21`), carpenter (`05:142`).
- `05:15` and `05:19` say the same thing.
- No concrete minimal example; a 10–12 line pseudo-code block would anchor it.
- Six "jobs" (`05:25-37`), 7-item checklist (`05:106-112`) and 10 questions (`05:118-136`) overlap heavily; one table.
- No Mini Lab (ch07 and ch08 have one).

Technical accuracy.
- `05:100` "Hermes-style context compaction" undefined.
- `05:27` Tool Broker is the book's own term; say so explicitly.
- `05:15` DeepAgents needs a one-word gloss.
- `05:54` "vibe code ထားသော" undercuts trust in a chapter about discipline.

Language (worst): `05:5` one 60-word sentence → "အရင်အခန်းတွေမှာ LLM (စာရေးတော်)၊ သူ့လက်ဖြစ်တဲ့ Tool Calling၊ ပြီးတော့ အဲ့ဒီလက်တွေနဲ့ အလုပ်ကို အဆင့်ဆင့်လုပ်တဲ့ Agent Loop ကို လေ့လာခဲ့ပြီ။"; `05:17` → "Harness ဆိုတာ ပစ္စည်းစုထားတာ မဟုတ်ဘူး။ ဆုံးဖြတ်ချက်တွေ စုထားတာ။"; `05:54` two spelling errors (ပက်သက်, အကြမ်းဖျဉ်း), run-on, "sdk" casing; `05:78` "စာရွက်" for a script file, "တံခါးစောင့်ဖြတ်သည်" unnatural; `05:142` harsh image.

Consistency: Harness glossed as control layer / policy plane / ထိန်းကျောင်းမှုစနစ် / ထိန်းကျောင်းရေးစနစ်. `05:112` is ch11's lesson; add pointer.

Top 3: (1) shrink repo sections to 4–6 lines each, introduce the four repos once before `05:58`; (2) minimal harness pseudo-code after `05:51`; (3) one table + one metaphor.

#### 06-mcp-skill-subagent.md

Summary. MCP = bridge (client/server, Tool/Resource/Prompt), Skill = on-demand manual, Sub-agent = delegated worker; `AGENTS.md`/`SKILL.md` survival under compaction; "read OpenClaw hype coolly". Strongest-structured chapter of the block.

Structural issues.
- Skill section lacks a concrete `SKILL.md` example (6–8 lines with frontmatter).
- `06:101-111` duplicates `07:94-111` almost one-for-one.
- Sub-agent section (`06:113-121`) has no small example; jumps to P-2/BrowserSurfer class names.
- No exercise; the three closing questions (`06:145`) could become one.

Technical accuracy.
- `06:139` literal `[SOURCE_NEEDED]` in reader text; `19:70` already has the evidence.
- `06:73` "reading a GitHub issue = Resource" misleading; define by control (Tool = model decides, Resource = app attaches, Prompt = user picks).
- `06:77` webpage content is tool output, not an MCP Resource.
- `06:33-49` add host with multiple clients, 1:1 client↔server.
- `06:83` describes whole-file injection; progressive disclosure is the mechanism.
- `06:107`, `06:154` compaction oversimplification (rules belong at system level).
- `06:115` missing the main sub-agent benefit: bulky tool output stays in its context, short result returns.
- `06:5` promises "Checkpointer" and never covers it.

Language (worst): `06:17` "လက်စွဲစာအုပ်သည် နည်းပြ လုပ်ပေးသည်" unnatural → "လက်စွဲစာအုပ်က ဘယ်လိုလုပ်ရမလဲ ပြတယ်။"; `06:92` 40-char unspaced chain; `06:107` ချေ inside quoted rule; `06:145` "ကိရိယာ". Spelling `06:85` အကြမ်းဖျဉ်း.

Consistency: Sub-agent gloss varies (အငယ်စားလက်ထောက် / အလုပ်ခွဲလက်ထောက် / worker); Skill gloss varies.

Top 3: (1) fix Tool/Resource/Prompt framing and diagram; (2) real `SKILL.md` example + progressive disclosure; (3) remove `[SOURCE_NEEDED]`, collapse duplicated compaction section into a forward reference to ch07.

#### 07-context-engineering-memory-rag.md

Summary. Prompt Engineering first, Prompt vs Context, Context Window as the scribe's desk, RAG as librarian, Memory ("what not to remember"), three-run mini lab.

Structural issues.
- Title promises Context Engineering/Memory/RAG; half the chapter (`07:21-88`) is Prompt Engineering. Context Engineering never gets its own section (one sentence at `07:88`).
- Context Window section lacks tokens, rough sizes, cost/latency scaling, "lost in the middle".
- Compaction used (`07:96`, `07:164`, `07:180`) but defined only in ch06.
- "Better prompt" example (`07:66-82`) is about writing this book's ch12 from P-2 internals (`states.py`, `[SOURCE_NEEDED] markers`); replace with a reader-relatable repo example.
- RAG section has no worked chunk example or table; Memory section has no good/bad/malicious entry example.
- `07:109-111` restates the table above it.

Technical accuracy.
- `07:132` broken back-reference to ch03 for embeddings/attention.
- `07:132` retrieval described as embedding-only; mention hybrid (BM25 + vector) + rerank.
- `07:148` trajectory store called RAG, `07:154` called Memory, without saying they overlap.
- `07:96` compaction oversimplification (same as ch06).
- `07:48` "Prompt is not law" is the chapter's key message; promote to takeaway.

Language (worst): `07:25-32` translates every prompt-type term into Burmese (`Tool description → ကိရိယာအသုံးပြုနည်း`) — the guide's "before" pattern; `07:7` မည်သို့/မည်သည့်/ဟူသည် stack; `07:132` 45-char unspaced chain; `07:148` "အဆိပ်ရှိသော ညွှန်ကြားချက်" literal rendering; `07:109` typo လက်ဆွဲ and "မြန်မာလိုပြောလျှင်" opener in an all-Burmese book; `07:182` ကိုယ်စားလှယ်.

Top 3: (1) Context Engineering section with definition, token basics, before/after context packet, compaction defined here; (2) replace P-2 prompt example; fix ch03 back-ref; (3) worked RAG and Memory examples + chunk-size table.

#### 08-planner-worker-verifier.md

Summary. Role separation not "three agents"; Planner decomposes (advisory), Worker executes under task contract, Verifier checks evidence; LangGraph-style graph; `execution_ok` vs `data_ok`; Mini Lab. Clearest chapter of the block.

Structural issues.
- Verifier has no contract/example output (Worker has one at `08:70-81`). Add `verdict / evidence / missing / unsafe_actions` block.
- Missing: when NOT to use the pattern and what it costs (3× calls, latency, more surfaces).
- Missing: Verifier independence (fresh context, ground-truth inputs, deterministic checks first); `08:11` implies it.
- Case-study references without introduction (`08:60` PlanningAgent, `08:89-93`, `08:95`).
- No summary table (Role | Question | Implementation | Failure if weak).

Technical accuracy.
- `08:104` `run_worker` vs `08:146`/ch13 `run_agent`.
- `08:60` "untrusted advisory" blurs the security sense of untrusted.
- `08:113` is the most important line (Planner may be deterministic code; Verifier is tests + schema + LLM + human) — make it the thesis, not a late correction.

Language (worst): `08:5` long, "သွားရပ်သင့်မည်မဟုတ်" awkward; `08:7` ခြင်း×3 + double ကြောင့် → "ဘာလို့လဲဆိုတော့ plan ချတာ၊ လုပ်တာ၊ စစ်တာက မတူတဲ့ အလုပ်သုံးမျိုး ဖြစ်လို့ပဲ။"; `08:62` ကိရိယာ; `08:83` 50-char unspaced chain; `08:117` translated idiom.

Top 3: (1) Verifier output contract + independence; (2) cost / when-not-to-use paragraph; (3) fix node name, add closing 3-row table.

#### Block 05–08 cross-chapter

Strengths: honest engineering stance stated memorably; one-line "အလွယ်မှတ်ရန်" code blocks; asides and Mini Labs show the author can write in the plain register; ch06 opening and ch08 clinic example are models of the problem → model → example → risk structure.

Five most important: (1) introduce the four repos once before ch05 uses them; strip class-name lists; (2) register decision applied to body prose; replace ကိရိယာ/ကိုယ်စားလှယ်; (3) correct MCP primitive framing; (4) de-duplicate and relocate `AGENTS.md`/compaction material; define compaction in ch07; progressive disclosure; (5) resolve dangling references (`[SOURCE_NEEDED]`, ch03 back-ref, `run_worker`, "Hermes-style", "Checkpointer").

### Block 09–12

Reviewer note on register: ch09–11 are consistently literary (`သည်။` 69/91/90 vs `တယ်/ပါ` 10/9/11); ch12 switches register mid-chapter (lines 15–31 conversational, 33 onward literary). Pick (a) literary for 09–11 and smooth ch12, or (b) move the block to the guide's register.

#### 09-tool-broker-permission-mutation-scope.md

Structural issues.
- Tool Broker re-defined without reference to ch05 (`05:27-29` gatekeeper vs `09:9` armoury guard).
- Action scope vs Mutation scope not actually distinguished (`09:23`); give one example each (action-not-mutation: run tests, screenshot, pricing API).
- Title `09:3` "လူမိုက်အား ဓားမအပ်မိစေရန်" contradicts conclusion `09:113-115` ("not distrust"). `09:9` "သစ်ခုတ်ရန်လား လူခုတ်ရန်လား", `09:25` "Hammer, scalpel, gun" are violent imagery; house-keys analogy at `09:115` is better.
- No code; ch17 Lab 2 is a broker lab — cross-reference or lift 10 lines.
- Forward references without chapter pointers (`09:47,49,67,73,99,101`).
- Editorial notes in reader prose (`09:73`, `09:101`).
- Bare-line lists `09:83-93`.
- "Source Notes" in English for a Burmese reader (`09:120-125`).

Technical accuracy: `09:47` ToolRegistry/ToolSpec verified; `09:49`, `09:99` Travis-2 middleware and HMAC signing verified; `09:57-63` 5-level ladder is the author's own taxonomy — say so.

Language (worst): `09:13` negation inside nominal ("မသုံးခွင့်ရှိ"); `09:29` six consecutive "သိသည်" → "Tool Broker က tool တစ်ခုချင်းစီအကြောင်း ဒါတွေ သိထားတယ် — schema နဲ့ argument၊ side effect ရှိမရှိ၊ human approval လိုမလို၊ output ကို ဘယ်လို sanitize လုပ်ရမလဲ။"; `09:47` "ဟုမရိုးရှင်းနိုင်" ungrammatical; `09:65` mixes ဆိုတာ with သော…မဟုတ်.

Consistency: browser-tool risks, approval dialog, skill supply chain, "schema mismatch is a feature" duplicated in ch11 and ch12.

Top 3: (1) action/mutation examples + 10-line broker sketch; (2) remove material duplicated in ch11; (3) fix title/metaphor contradiction; strip editorial notes.

#### 10-observability-trajectory-reflection.md

Best-structured chapter of the block: problem → mental model → worked failure → risks → lab.

Structural issues.
- `10:67-73` "Test becomes Observability" conflates verification with inspection.
- Qdrant undefined (`10:41`).
- `execution_ok`/`data_ok` introduced here, explained in ch13; add pointer.
- Standard vocabulary (trace/span/LangSmith/OpenTelemetry) missing; P-2 README enables LangSmith tracing — unused tie-in.
- New idea in the conclusion (`10:164` session-scope leakage); move into Privacy section.
- Bare-line lists `10:45-53`, `10:81-89`.
- `10:71` hedge "ရှိလျှင်" — the file exists.

Technical accuracy: all named classes/files verified. `10:117-132` hash caveat.

Language (worst): `10:5` ကိရိယာ; `10:27` "စာရွက်စာတမ်း" (paperwork) wrong word; `10:95` six unrelated facts missing the "but" → "Tool success rate မြင့်ပေမဲ့ task success နည်းနိုင်တယ်။ Latency နည်းပေမဲ့ verification မရှိတော့ အမှားများနိုင်တယ်။…"; `10:117` ၎င်း.

Consistency: Trajectory as ခြေရာ (`10:3,35,138`), လမ်းကြောင်း (`10:11,13,162`), Trajectory.

Top 3: (1) retitle appv22 section; (2) add trace/span vocabulary with LangSmith example; (3) define Qdrant, drop hedge, bullets, move session-scope warning.

#### 11-safety-sandbox-prompt-injection-tool-output.md

Structural issues.
- Twelve sections in ~1200 words; `11:102-124` are 3-sentence stubs (Human Approval, Secrets, Skill supply chain, State Boundary). Merge or expand two and pointer the rest.
- Opening and injection/wrapper sections (`11:3-55`) are excellent; "poison letter in a bag labelled do-not-eat" (`11:49`) is the clearest metaphor in the block. Protect.
- Wrapper defined twice (`11:47-49`, `11:162`).
- Loop Safety (`11:126-148`) breaks the untrusted-input thread; tie to injection (a poisoned page can induce a loop) or move.
- Editorial meta-notes `11:82` (also word-order slip "မသာဖော်ပြရ" → "သာ မဖော်ပြရ"), `11:100`, `11:110`, `11:112`.
- `11:176-178` says repos start "from the next chapters" but 09–11 already lean on repo internals.
- Bare-line lists `11:84-98`, `11:134-148`.
- Missing: "defence | stops | does not stop" table.

Technical accuracy: `11:33` name OWASP LLM01; `11:51` `wrap_untrusted`/`wrap_and_check` verified; `11:74` verified; `11:106` `bot/src/main.py:95` is literally `# Handle HITL here if needed` — perfect "HITL as checkbox" exhibit; `11:47` say why wrapper is mitigation not boundary; `11:172` first mention of Travis-2's TypeScript nature is in the conclusion.

Language (worst): `11:5` double nominalisation; `11:23` "စာလုံးအမှား" misdescribes chatbot case; `11:47` "အပေါ်မှအောက်မှ"; `11:104` "ထိုအရာများ" vague; `11:178` register jump to ပါသည်.

Consistency: Human approval written five ways; gatekeeper metaphor split (လက်နက်တိုက်စောင့် vs တံခါးစောင့်).

Top 3: (1) collapse stubs; (2) defence table + why-wrapper-is-mitigation sentence; (3) remove meta-notes, fix OWASP citation and "next chapters" notice.

#### 12-p2-zero-trust-multi-agent-bridge.md

Structural issues.
- Zero actual code from the repo. `BridgeNode.invoke` is 8 lines (`nodes.py:213-220`), `UnsafeState` 7 lines (`states.py:19-25`).
- Diagram (`12:59-92`) omits the second hop (`bridge_admin_input` → `customer_from_bridge`, `runtime.py:56-85`); `12:98` lists the field with no explanation.
- Supervisor vs classifier conflated (`12:129`); `LLMTaskClassifier` decides (`nodes.py:185`); on `route_bridge` the supervisor worker never runs.
- Metaphor says "rewrite" (`12:31,55,94,133`), contract says copy verbatim (`nodes.py:219`). `12:203` caveat is correct.
- Exercises `12:231-234` ask for tests that exist (`tests/test_runtime.py:52-106`); `12:23` uses `origin="user_cli"` which the type cannot hold.
- Offline mode unmentioned (`models.py:29-79`, `--model-mode offline`).
- Read-only Customer asserted (`12:209`) but mechanism (`ReadOnlyScopedNode`, `interrupt_on`, `nodes.py:66-147`) unexplained; its `while __interrupt__` loop has no iteration cap (`nodes.py:126-140`) — ch11's lesson inside the case study; `nodes.py:80` also blocks `glob`/`grep` (reads).
- `12:205` `[SYNC_MISMATCH]` leaked.
- Mixed register.

Technical accuracy table: `12:98`, `12:100` field lists correct; `12:110-125` bridge contract correct; `12:155` scoped FS correct; `12:139-141` planes correct; `12:100` "မပါနိုင်အောင် schema အဆင့်" overstated (`TypedDict(total=False)` no runtime enforcement; README:191 same overclaim); `12:123` bridge *raises* `BridgeAccessError`, no graceful reject; docs drift confirmed: `ARCHITECTURE-ROUTING.md:83-86` keyword guard absent from `classifier.py:61-67` (exists only in offline model `models.py:62-75`); `README.md:60-61` "extracts public info" vs untouched forward; `12:249` source map omits `tests/test_runtime.py` and `models.py`; README:185 "security audits (Feb 2026) verified" unsubstantiated — don't import.

Language (worst): `12:4` colloquial quote in literary frame; `12:94`, `12:133` "ပြန်မွေး" (re-birth) odd verb → "လိုအပ်တဲ့ field တစ်ခုတည်းနဲ့ state အသစ်တစ်ခု ဆောက်ပေးတယ်။"; `12:135` scolding; `12:151` mixes ဒါ with ဟုမဆိုရ; `12:189` ဤသည် for a three-word sentence.

Consistency: Agent counter ခု vs ယောက် within the chapter (`12:4` vs `12:244`); Bridge as projection boundary / air gap / တံခါးစောင့် / တံတား / strips.

Top 3: (1) show the code + offline command; (2) fix diagram (two hops), separate classifier from supervisor, "copy one field" wording; (3) name the two verified docs drifts, explain `ReadOnlyScopedNode` and its missing cap, point exercises at existing tests.

#### Block 09–12 cross-chapter

Strengths: through-line metaphor gives 09→12 one argument (power → visibility → safety → real example); ch10 shape and ch11 first 55 lines are model pedagogy; every chapter ends with a safe lab; ~30 named artifacts all exist.

Five most important: (1) de-duplicate 09 vs 11 (~300 words); (2) real code into ch12 + fix diagram; (3) remove author-to-self notes (`09:73,101`, `11:82,100,110,112`, `12:205`); move English Source Notes; (4) register decision; break staccato runs (`09:29`, `10:95`); (5) label forward references with chapter numbers; convert bare-line lists; soften `11:176-178`.

### Block 13–14

#### 13-travis2-controlled-runtime.md (42 KB, 440 lines)

Summary. One idea: when a model writes code, the engineering work is in where it runs, what is checked before, and how the structured result is read. Centres on `run_playwright_code` (`execution_ok` vs `data_ok`), then Docker sandbox, AST validation, skills/signing, `AgentState`, reducer-safe sync, middleware, outer-graph routing. A beginner can follow the first third; struggles from `AgentState` onward.

Structural issues.
- Thesis restated five times (`13:4`, `13:23`, `13:33-35`, `13:193-204`, `13:415`); 25–30% restatement.
- Listings without lesson: `AgentState` table (12 fields, 3 used; the interesting schema-mismatch point at `13:290` is buried); middleware list (8 bullets, 1 explained); failure-mode list (12 items, no priority); source map (17 files in one line).
- Order: reading guide says tools.py first, graph last; chapter puts architecture diagram and PTC essay before the contract.
- PTC digression (`13:46-60`) 15 lines of general theory; belongs in ch03 with a pointer.
- Missing: host vs Docker comparison table; a real `run_playwright_code` result read out field-by-field; a pasteable 10-line lab function.
- Conclusion is a Travis-2-specific bullet recap, not transferable principles.

Technical accuracy.
- `13:10`/`13:320` sanitization off by default (`.env.example:89`, `middleware.py:893`); architecture doc §6 lists 7 middlewares and omits sanitization — doc/code disagree.
- `13:153` `<tool_output_untrusted>` wrapper only appears if sanitization enabled.
- `13:241-249` AST validation default `false` (`.env.example:88`).
- `13:251` name the banned patterns (`child_process`, `fs`, `eval()`, `new Function()`, `typescript_validator.js:24-165`).
- `13:215-228` sandbox container has internet (`docker_runner.py:309`).
- `13:367` silent host fallback is real (`tools.py:464-469`).
- Omission: runtime `blocked_search_engine` check (`tools.py:73,244`).
- `13:261` skill says a CAPTCHA page can set `data_ok=true` (`playwright/SKILL.md:166`) — sharper example.
- `13:13` v0.2 promise with no roadmap.
- Over-hedged: same disclaimer four times.

Language. `ဖြစ်သည်။` 42, `ဤ` 19, `ချေ` 9, `၎င်း` 6, `တယ်။` 0. Intro box uses `ပါသည်`, line 29 switches to literary. Rewrites: `13:4` → "Travis-2 မှာ model ရေးပေးတဲ့ TypeScript Playwright code ကို `run_playwright_code` tool ကနေတစ်ဆင့် ဘောင်ခတ်ပြီး run တယ်။"; `13:13` → add "Default မှာ အများစု ပိတ်ထားတယ်။"; `13:35` → "Model ရေးတဲ့ code ကို trusted code လို့ မယူရဘူး။ ဒါက untrusted input ပါ၊ run ခင် စစ်ရမယ်။"; `13:193` four `သို့သော်` clauses → one paragraph ending "Exit code က 'run ပြီးပြီ' ပဲ ပြောတယ်၊ 'ရပြီ' မပြောဘူး။"; `13:296` untranslated English sentence; `13:44` mixed metaphors.

Proposed outline (~27 KB): intro box (1 KB) → problem (2) → contract + real result + CAPTCHA example (5) → host vs Docker table (3) → gates: AST + search-engine block with defaults (3) → control plane: outer graph + middleware table (4) → two real gotchas (2) → runnable lab (2) → transferable principles (1.5) → source notes, 4 files (0.5). Move PTC to ch03/appendix; `AgentState` full table and reducer-safe sync to appendix; keep screenshot 13-3 only.

Top 3: (1) reorder to match own reading guide; (2) replace checklist and recap with two verified gotchas + principles; (3) register pass.

#### 14-browsersurfer-browser-tool-agent-security.md (56 KB, 331 lines)

Summary. Uses `bot` to show what rides along with a browser agent: facade, DeepAgents, thread/checkpointer/store, `ToolRegistry`, snapshot/ref, output wrappers, RAG planner, trajectory observer, metrics/reflection/Qdrant, skills middleware, HITL, security report. "Browser = living city" framing and ethical stance are clear. Reads as a complete architectural tour, not a focused lesson.

Structural issues.
- 14 sections, ~12 classes, ~10 metaphors; the actual security lessons are five (page content is data; refs go stale; shared session ≠ thread; wrapper ≠ guarantee; HITL config ≠ enforcement), all stated by line 199. `14:201-250` re-apply "X is not a guarantee" (`14:199, 209, 217, 236, 242, 248`).
- Opens well (`14:17-31`).
- Screenshots `14:109-155` ~9 KB; `14:111` is publication-process meta; 14-1/2/3 teach the same lesson; keep 14-4 and 14-5.
- Two overlapping "what to fix" lists (`14:256-272`, `14:288-299`); "wrapper is not a guarantee" five times.
- Lab duplicated (`14:17-23`, `14:301-314`).
- Missing: tool-risk table (from report's 22-tool inventory); thread-vs-session ASCII diagram; main diagram mixes Burmese inside the box (`14:46-47`).
- Conclusion lists 15 nouns (`14:318`); `14:320` is the strongest paragraph and should be the ending.

Technical accuracy.
- `14:89`, `14:163` stale `CHAPTER-7.md`.
- Omission: `--disable-web-security` (`src/session/__init__.py:33`) and `--disable-blink-features=AutomationControlled` (line 32); the repo's own report calls it out.
- `14:254-260` report (2026-01-20) says sanitization missing; `src/tools/security.py` now exists and is used (`utilities.py:420,479,565,607,763`, `navigation.py:226`).
- `14:213` loop detection threshold is 5 (`trajectory_callback.py:36,183-184`), abort via exception caught in `facebook_surfer.py:510-524`.
- `14:203` planner `min_score=0.4` vs retrieval default 0.47 vs docstring 0.7 — threshold drift.
- `14:246` `browser_click`, `browser_type`, `browser_handle_dialog` not in `interrupt_on` (`facebook_surfer.py:338-350`).
- `14:159` default `thread_id="default"` everywhere.
- `14:161` `MemorySaver` is definitely in-memory.
- `14:111` process claim; `selected/` has 7 unused variants.

Language. `ဖြစ်သည်။` 55, `ဤ` 22, `သို့သော်` 16, `ချေ` 4, `တယ်။` 0; literary vocabulary (`စာရေးတော်` 4, `ဗျာဒိတ်တော်` 2). Inconsistent word spacing at `14:29-31, 74-76, 85`. Rewrites: `14:31` bureaucratic naming note → "Chapter ထဲမှာ နာမည်ပြောင်းခေါ်ထားတာက 'platform တစ်ခုတည်းအတွက် guide' လို့ အထင်မမှားစေဖို့ပါ။"; `14:85` → concrete `InMemoryStore()`/`MemorySaver()` sentence; `14:121` → "ဒီပုံမှာ ပြောင်းသွားတာ တစ်ခုရှိတယ်။ Agent က chat box ထဲမှာ အကြံပေးနေတာ မဟုတ်တော့ဘူး။ Model ရေးတဲ့ စာက UI ထဲ ရောက်သွားပြီ။"; `14:215` `မူးယစ်မှု` means narcotic intoxication → "loop ထဲ ပိတ်မိနိုင်တယ်"; `14:70` six metaphors in one sentence.

Proposed outline (~31 KB): intro + naming note (1.5) → city problem (2) → what rides along, one English-only diagram (2.5) → five security lessons each with one code pointer incl. `--disable-web-security` and `interrupt_on` gaps (10) → 8-row tool risk table (1.5) → learning loop + threshold drift (3) → component | does | does not guarantee table (1.5) → single lab (2) → principles from `14:320` (1.5) → source notes incl. image provenance (1).

Top 3: (1) add `--disable-web-security` paragraph; (2) collapse 14 sections into five lessons + two tables; (3) fix `CHAPTER-7.md`, move `14:111`, register and spacing pass.

#### Block 13–14 cross-chapter

Strengths: good theses stated early; honest about config-dependent controls; safe local reading guides; ~25 claims checked, none false, only omissions and defaults; ASCII diagrams and ch13 contract tables are the best-presented material.

Five most important: (1) cut 35–45% by removing restatement (ch13 ≈ 27 KB, ch14 ≈ 31 KB, in line with ch12's 28 KB); (2) use real repo gotchas as evidence; (3) end with transferable principles (ch12 `12:211` is the model); (4) register pass (combined `ဖြစ်သည်။` 97, `ဤ` 41, `ချေ` 13, `တယ်။` 0) — discuss with author first per the guide; (5) fix stale/editorial references and shrink source maps.

### Block 15–19

#### 15-appv22-emerging-runtime-recovery-lab.md

Summary. Case study of `allthebest/appV2.2` as a runtime recovery lab: what was borrowed from Pi (loop, events, TUI, providers) and Hermes (compaction, overflow recovery, guardrails), `CodingApp.run_turn()`, compaction timing, guardrails, recovery audit, reading exercise. The book's "honest failure" chapter.

Structural issues.
- Hook buried (`15:42-46` "day one beautiful, day two context fills") after blockquote, reading plan, personal history (`15:32-40`).
- "Not production / not final kernel" five times (`15:7, 38, 104, 154, 175`); "inspiration ≠ dependency" three times; "six lessons" restates every section; conclusion restates lessons. ~25% cut possible.
- No code excerpt (ch13/14 have one); show `ToolGuardrailDecision` actions or `CompactionManager` phases.
- Compaction timing (`15:106-114`) as a 4-row table (Trigger | When | Signal | Bounded by).
- ASCII flow `15:21-28` excellent; add one for guardrail decision.
- Exercise (`15:160-169`) lacks expected findings per step.

Technical accuracy. Verified: event classes, `allow/warn/block/halt`, tool lists, args-hash signature, `SUMMARY_PREFIX`, `_redact_sensitive_text`, four timing phases, iteration budget → summary request, steering messages, test names, agent_loop.py port of Pi. Issues: `15:130` coupling test only checks `appv21` tokens, not Pi/Hermes imports (README:227 same overclaim); `15:156,163` audit is a snapshot (NEXT_PATCH `test_app_integration.py` now exists); `15:110` `/compress` vs `/compact`; `15:13,138,193` Pi-site-links-OpenClaw claim needs "as of" qualifier; `15:34` README has typo "decompressor"; `appv22` vs `appV2.2` never explained.

Language. 173 `သည်။`, 0 `တယ်။`, 14 `ချေ` (highest). Rewrites: `15:13` → "ဒါပေမဲ့ 'OpenClaw က Pi ပဲ' လို့ တစ်ကြောင်းတည်း ချုပ်ပြောတာက over-simplified ပါ။ Fact အနေနဲ့ မရေးသင့်ပါ။"; `15:36` "aka" chat register; `15:50` 40-word sentence with Latin comma; `15:98` capital T mid-sentence; `15:120` → "ဒီ file က တာဝန်တွေ အများကြီးရောနေတယ်။ Audit ကလည်း 'stabilize လုပ်၊ မချဲ့နဲ့' လို့ မှတ်ထားတယ်။"; `15:142` typos `လျင်`, `တခု`, capital Hype; `15:181` ပေသည်; `15:68` long.

Top 3: (1) restructure hook-first, two maturity warnings instead of five, lessons as a 6-bullet box; (2) one code excerpt + timing table; (3) fix `15:130`, date-stamp audit, language pass.

#### 16-devops-agent-thinking.md

Summary. DevOps agents start read-only, least-privilege, approval-gated mutation, redaction, audit, recovery; re-applies four case-study lessons to Terraform/AWS/CI; illustrative YAML policy; beginner architecture.

Structural issues.
- Strong opening (`16:3-11`) and the best expected-output exercise in the book (`16:15-28`); ch17 should copy it.
- Duplicate CI example (`16:17-28` and `16:202-208`).
- Three near-identical read-only/mutating lists (`16:34-53`, `16:134-149`, `16:167-181`) → one domain table.
- appv22 section (`16:124-128`) thin; add "CloudWatch log 50MB as tool result → overflow; appv22 pruning applies here".
- HTML entities `16:39`, `16:153-154`.
- `16:17` give a fake secret sample pattern.

Technical accuracy: no incorrect claims; concept-level use is accurate and conservative.

Language. 80 `သည်။`/30 `ပါ။`, 3 `ချေ`. Rewrites: `16:61` six `-ခြင်း` → "မြန်မာလိုပြောရင် deploy, secret rotation, production DB, DNS, IAM, destructive command — ဒါတွေအကုန် default ပိတ်ထားပါ။ လူက approve လုပ်မှ ဖွင့်ပါ။"; `16:101`, `16:103` → "Exit code 0 ဆိုတာ 'အဖြေမှန်တယ်' လို့ အာမခံတာ မဟုတ်ပါ။"; `16:92` uninto metaphor; `16:113` wrapper redefined; `16:275` archaic `ပါလော့`; `16:183` "cloud palace" mixed with `နန်းတော်`.

Top 3: (1) one domain table; fix entities; (2) merge duplicated CI example; (3) concrete appv22 overflow example + fake secret pattern.

#### 17-mini-labs.md

Summary. Ten local, safe labs following `Build → Safe Failure Test → Fix → Reflect`.

Structural issues (answers to the brief's questions).
- Doable by a beginner? Partly. One-line imperatives with no starter code; only Lab 4 has a snippet (`17:125-137`). Each lab needs a 10–15 line skeleton.
- Prerequisites: none stated (Python version, API key?). Labs 3, 7, 9 need a real model or a deliberately gullible scripted one — say which. Suggest per-lab header: Difficulty | Real LLM? | Prereq chapters | Time.
- Expected output: none in any lab; copy `16:21-28`.
- Safety boundaries: good (`17:71, 103, 230, 290, 338-340`); Labs 1, 4, 5, 6, 8 lack "no API key / no network" line.
- Ordering: Lab 4 and Lab 8 easier than Lab 3 and Lab 5. Suggest 1, 2, 4, 8 → 3, 6, 9 → 5, 7 → 10, or difficulty tags.
- Connection to chapters: only via repo names; ch18 never mentions ch17.
- Frame followed only by Lab 1 (`17:43-45`); restore `Reflect:`.
- Editorial leak `17:93` ("reader review").
- `17:334` "v0.2 fix task".
- `17:117` repo path missing `repo_sources/bot/` prefix.
- Wrapper and faux provider redefined.

Technical accuracy: nothing wrong; repo lessons map to real code; 2KB/8KB caps sensible.

Language: `ပါ` imperative (85×) appropriate. Fragments: `17:23-29` disconnected one-liners → one explanatory paragraph; `17:45`, `17:111`, `17:344` 13-item list sentence, `17:346` ambiguous.

Consistency: fake model / fake provider / faux provider within one chapter; Prompt injection casing.

Top 3: (1) per-lab header + expected output; (2) skeleton per lab + Reflect; (3) remove leak and v0.2, fix path, reorder.

#### 18-myanmar-developer-roadmap.md

Summary. Eight-stage learning order + six self-check milestones. Message: build the engineer's "eye" before chasing frameworks.

Structural issues.
- Concrete? Partly; no time estimates, no lab pointers, ch17 never mentioned.
- Local constraints: absent. Zero mentions of internet, payment, hardware, cost, free tiers, local models, power, community. Additions the book already supports: payment → faux-provider-first; bandwidth → offline `repo_sources/`; low-RAM → toy loops need no local model; connection → persistence (appv22); English reading → the keep-terms-in-English policy is itself a bridge.
- Dated items: framework names `18:5`, `n8n` `18:17` (dangling).
- Cross-references uneven (stages 2, 4, 6, 7, final have none) → Stage | Chapters | Labs | Milestone table.
- Ending (`18:81-83`) is one of the best in the block.
- Pali ordinals (`18:33, 39, 51`) → numerals.

Technical accuracy: fine.

Language. 27 `သည်။`/37 `ပါ။`. Rewrites: `18:23` "Harness *is* permission, memory…" robotic → "Harness ဆိုတာ loop ကိုပတ်ထားတဲ့ permission, memory, sandbox, verification, observability, persistence, safety အလွှာတွေပါ။"; `18:45` two metaphors + 8 jargon terms for a beginner roadmap; `18:41` `အလွတ်ဖတ်` ambiguous; `18:65` no spaces.

Top 3: (1) Myanmar constraints section; (2) stage/chapter/lab/milestone table; (3) fix `n8n`, simplify `18:45`, numerals.

#### 19-references.md

Structural/hygiene issues.
- Inconsistent formatting (bare filenames; table; `[url](url)` bullets).
- Private drafts (`19:9-18`, incl. `prompts`, `models`) not labelled as unpublished.
- Orphan `19:61` Shwe U Daung — cited nowhere.
- Cited but missing: OpenClaw `THIRD_PARTY_NOTICES.md` URL (relied on at `15:13,138,193`, `19:70`; URL in citation map L62 and SOURCE_NOTES L120).
- SOURCE_NOTES ↔ ch19 drift (LangGraph quickstart, Business Insider, TechRadar, ClawSafety papers listed in SOURCE_NOTES, not in ch19 or chapters).
- Duplicated license block (`19:35-41`).
- `CITATION_VERIFICATION_MAP.md:66` → non-existent `CITATION_VERIFICATION_TODO.md`.
- No chapter-to-reference mapping.
- MCP spec `2025-06-18` vs newer `2025-11-25`; arXiv IDs and platform URLs unverifiable offline; map marks OpenClaw articles `defer_v0_2` yet ch19 lists them as verified.

Language: `19:20` 30-word sentence; `19:33`; `19:70` `ဟူသော…ချေ`.

Top 3: (1) unify format, one license pointer; (2) add THIRD_PARTY_NOTICES, drop/relocate orphan, label private drafts; (3) split verified vs unverified; update/qualify MCP date.

#### Block 15–19 cross-chapter

Strengths: consistent safety posture backed by repos; ch15 more accurate than its own repo README; `16:15-28` exercise is the model; ch18 conclusion and milestones are good pedagogy; scribe/palace metaphor coherent across ch16/18.

Five most important: (1) make ch17 labs runnable; (2) make ch18 live up to its title; (3) tighten ch15 ~25%, fix `15:130`, date-stamp audit; (4) ch19 citation hygiene; (5) language pass (remove `ချေ/ပေသည်/ပါလော့/ဟူသော`), fix HTML entities, define wrapper and faux provider once.

---

## Part 3 — Mechanical pass data

Chapter asset inventory (as of 2026-10-24):

| Chapter | bytes | H3 | code blocks | table rows | images | Mini Lab |
|---|---|---|---|---|---|---|
| 01 | 26,559 | 5 | 0 | 0 | 0 | no |
| 02 | 17,964 | 5 | 0 | 0 | 0 | no |
| 03 | 18,531 | 5 | 0 | 0 | 0 | no |
| 04 | 13,756 | 5 | 0 | 0 | 0 | no |
| 05 | 27,288 | 10 | 2 | 0 | 0 | no |
| 06 | 24,795 | 8 | 3 | 5 | 0 | no |
| 07 | 25,867 | 8 | 5 | 6 | 0 | yes |
| 08 | 17,997 | 8 | 3 | 0 | 0 | yes |
| 09 | 15,311 | 8 | 4 | 0 | 0 | yes |
| 10 | 19,809 | 10 | 4 | 0 | 0 | yes |
| 11 | 23,214 | 13 | 4 | 0 | 0 | yes |
| 12 | 27,809 | 16 | 6 | 0 | 0 | exercises |
| 13 | 42,404 | 16 | 10 | 46 | 3 | lab |
| 14 | 55,879 | 19 | 3 | 0 | 5 | lab ×2 |
| 15 | 41,173 | 12 | 1 | 0 | 0 | exercise |
| 16 | 22,475 | 14 | 7 | 0 | 0 | exercise |
| 17 | 14,154 | 13 | 3 | 0 | 0 | — |
| 18 | 13,393 | 11 | 0 | 0 | 0 | no |

No chapter uses H2; all use H1 slug + H3 sections. No Mermaid diagrams anywhere; all diagrams are ASCII.
