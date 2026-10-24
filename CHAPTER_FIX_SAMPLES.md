# Chapter Fix Samples

Companion to `CHAPTER_REVIEW_FINDINGS.md`. Each sample shows the current text, the proposed text, and what changed. Nothing in `book/chapters/` has been modified. The proposed text uses the conversational `တယ်/ပါ` register that `STYLE_GUIDE.md` already uses in its own examples; swap `ကျွန်တော်တို့` for `ကျွန်ုပ်တို့` if you prefer to keep the formal pronoun.

---

## Part A. Register and grammar rules applied

| Pattern in current text | Replacement | Why |
|---|---|---|
| `…သည်။` sentence endings in every sentence | `…တယ်။` / `…ပါတယ်။` for statements, `…ပါ။` for instructions | Matches the guide's "After" examples and the `Beginner အနေနှင့်…` asides already in the book |
| `၎င်း` | `သူ` (agent / person), `ဒါ` (thing / idea), or restate the noun | `၎င်း` is literary and ambiguous after two sentences |
| `ဤ` | `ဒီ` | Register |
| `ဟူသော` / `ဟု` | `ဆိုတဲ့` / `လို့` | Register |
| `…မဟုတ်ချေ` / `…မရှိပေ` / `…မနိုင်ချေ` | `…မဟုတ်ပါဘူး` / `…မရှိပါဘူး` / `…မနိုင်ပါဘူး` | `ချေ/ပေ` is archaic; 66 uses across the book |
| `X ခြင်းသည် Y ခြင်းဖြစ်သည်` | `X ရင် Y တယ်` or `X တာက Y ပါ` | Nominalised chains read as translation |
| `အကောင်အထည်ဖော်` for *run / execute* | `run တယ်` or `လုပ်တယ်` | Calque from English "implement" |
| `ဖန်တီး` for *create / write code* | `ဆောက်တယ်` / `ရေးတယ်` | `ဖန်တီး` is artistic creation |
| `ထုတ်ဖော်ပြောဆိုခိုင်းခြင်း` | `ထုတ်ပြောခိုင်းတာ` | Four-syllable compounds where two will do |
| 40+ character unspaced word chains | Space between every word group | Line-break and readability on phones |
| Six `သည်။` sentences in a row | Vary length; one idea per sentence; a short sentence after a long one | Rhythm |
| Burmese gloss repeated after an English term on every use | Gloss once in parentheses, then English only | `STYLE_GUIDE.md` rule on tech terms |

---

## Part B. Style-only samples (meaning unchanged)

### B1. `02:23` Non-deterministic paragraph

**Current**

> Agentic System တစ်ခုကို တည်ဆောက်ရာတွင် အင်ဂျင်နီယာများ ကြုံတွေ့ရသော အကြီးမားဆုံး ပြဿနာမှာ "ယုံကြည်မှု" ဖြစ်သည်။ ကျွန်ုပ်တို့၏ "သင်္ဘောကပ္ပတိန်" (LLM) သည် တစ်ခါတစ်ရံတွင် အရက်မူးနေသော ကပ္ပတိန်နှင့် တူတတ်သည်။ သူသည် အလွန်ပင် စကားတတ်သော်လည်း၊ လက်တွေ့တွင်မူ လမ်းမှားသို့ မောင်းနှင်သွားတတ်သည်။ ၎င်းကို Software Engineering တွင် "Non-deterministic" ဟု ခေါ်သည်။ ဆိုလိုသည်မှာ တူညီသော မေးခွန်းကို မေးသော်လည်း အဖြေမှာ တစ်ခါနှင့်တစ်ခါ မတူဘဲ ပြောင်းလဲနေခြင်း ဖြစ်သည်။

**Proposed**

> Agentic System ဆောက်တဲ့အခါ engineer တွေ အကြုံရဆုံး ပြဿနာက "ယုံရလား" ဆိုတာပါ။ ကျွန်တော်တို့ ကပ္ပတိန် (LLM) က တစ်ခါတစ်လေ အရက်မူးနေတဲ့ ကပ္ပတိန်လိုပါ။ စကားတော်ပေမယ့် လမ်းမှား မောင်းတတ်ပါတယ်။ ဒါကို Software Engineering မှာ **Non-deterministic** လို့ ခေါ်ပါတယ်။ မေးခွန်း တစ်ခုတည်းကို ထပ်မေးရင် အဖြေ တစ်ခါနဲ့ တစ်ခါ မတူဘူး ဆိုတဲ့ သဘောပါ။

**What changed:** register, `၎င်း` → `ဒါ`, `ဟု` → `လို့`, `ခြင်းဖြစ်သည်` chain removed, metaphor kept word for word.

### B2. `13:251` AST validation limits

**Current**

> AST validation သည် execution မလုပ်မီ banned syntax pattern များကိုရှာနိုင်သည်။ Plain string matching ထက်ပိုကောင်းသော်လည်း runtime behavior လုံခြုံကြောင်းသက်သေမပြနိုင်။ Dynamic behavior, remote page content, network response, data relevance တို့အားလုံးကိုအပြည့်မသိနိုင်။ ထို့ကြောင့် sandboxing, structured result interpretation, middleware policy, stdout relevance review တို့နှင့်တွဲသုံးရသည်။

**Proposed**

> AST validation က code မ run ခင် ပိတ်ထားတဲ့ syntax pattern တွေကို ရှာပေးပါတယ်။ String matching ထက် ပိုကောင်းပါတယ်။ ဒါပေမယ့် run လိုက်ရင် ဘာဖြစ်မလဲ ဆိုတာကိုတော့ မသိနိုင်ပါဘူး။ Remote page က ဘာပြန်လာမလဲ၊ network response ထဲ ဘာပါမလဲ၊ ဒါတွေ code ဖတ်ရုံနဲ့ မမြင်ရပါဘူး။ ဒါကြောင့် AST validation တစ်ခုတည်းနဲ့ မလုံလောက်ဘဲ sandbox, middleware policy, stdout review တွေနဲ့ တွဲသုံးရပါတယ်။

**What changed:** unspaced chains like `ကိုရှာနိုင်သည်` and `တို့အားလုံးကိုအပြည့်မသိနိုင်` broken up; four-item English list cut to three the reader has already met; one short sentence inserted for rhythm.

### B3. `14:22` Lab expected result

**Current**

> နောက်ဆုံး expected result ကိုရှင်းရှင်းထားပါ။ Agent သည် page text ကို instruction အဖြစ်မလိုက်ရပါ။ "စာမျက်နှာထဲတွင် injection-like text ပါသည်" ဟု data အဖြစ်သာဖော်ပြရပါမည်။ Click action တစ်ခုလုပ်ရန်လိုလျှင် approval gate မရှိဘဲမလုပ်ရပါ။ ဒီသုံးချက်ကိုစစ်နိုင်လျှင် BrowserSurfer chapter ၏ safety lesson ကိုလက်တွေ့မြင်ပြီဟုပြောလို့ရပါသည်။

**Proposed**

> နောက်ဆုံး ဘာရလဒ် မျှော်လင့်ထားလဲ ရှင်းရှင်း ချရေးပါ။ စစ်ရမယ့် အချက် သုံးချက်ပါ။
>
> 1. Agent က page ထဲက စာကို instruction အဖြစ် မလိုက်နာရဘူး။
> 2. "page ထဲမှာ injection လို စာ ပါတယ်" လို့ data အနေနဲ့ပဲ report လုပ်ရမယ်။
> 3. Click လုပ်ဖို့ လိုရင် approval မရဘဲ မလုပ်ရဘူး။
>
> ဒီသုံးချက် ပြည့်ရင် ဒီအခန်းက safety lesson ကို ကိုယ့်မျက်စိနဲ့ မြင်ပြီလို့ ပြောလို့ရပါတယ်။

**What changed:** a sentence that already lists three things becomes a numbered list; `၏` dropped; mixed `ပါ/ပါမည်/ပါသည်` endings unified.

---

## Part C. Technical corrections, with rewritten text

### C1. `02:19` Autonomy gloss and "restart from scratch"

**Current**

> ၃။ **Agentic Loop (ကိုယ်စားလှယ် ကွင်းဆက်):** ဤသည်မှာ အဆင့်မြင့်ဆုံး ဖြစ်သည်။ Agent သည် မိမိ၏ အလုပ်ကို မိမိဘာသာ ပြန်လည် စစ်ဆေးသည်။ "ငါ လုပ်လိုက်တာ မှန်ရဲ့လား"၊ "ပန်းတိုင်ကို ရောက်ပြီလား" ဟု မေးခွန်းထုတ်သည်။ အကယ်၍ မရောက်သေးပါက အစမှ ပြန်လည် ကြိုးစားသည်။ ဤသည်မှာ "ကိုယ်ပိုင်အသိ" (Autonomy) ရှိသော စနစ်ဖြစ်ပြီး၊ ကျွန်ုပ်တို့ ဤစာအုပ်တွင် အဓိကထား ဆွေးနွေးမည့် အကြောင်းအရာလည်း ဖြစ်သည်။

**Proposed**

> ၃။ **Agentic Loop:** ဒါက အဆင့် အမြင့်ဆုံးပါ။ Agent က ကိုယ်လုပ်လိုက်တဲ့ အလုပ်ကို ကိုယ့်ဘာသာ ပြန်စစ်ပါတယ်။ "ငါ လုပ်လိုက်တာ မှန်ရဲ့လား"၊ "ပန်းတိုင် ရောက်ပြီလား" လို့ မေးပါတယ်။ မရောက်သေးရင် အစက ပြန်စတာ မဟုတ်ပါဘူး။ ခုနက ရလဒ်ကို ကြည့်ပြီး နောက်တစ်လှမ်းကို ဆက်ရွေးပါတယ်။ ဒီလို ကိုယ့်ဘာသာ ဆုံးဖြတ်ပြီး ဆက်လုပ်နိုင်တာကို **Autonomy** လို့ ခေါ်ပါတယ်။ ဒီစာအုပ် တစ်အုပ်လုံး အဓိက ပြောမယ့် အကြောင်းအရာလည်း ဒါပါပဲ။

**What changed:** Autonomy is "decides and acts on its own", not "self-awareness" (`ကိုယ်ပိုင်အသိ`). The loop does not restart from scratch; it continues from the latest Observation, which is the whole point of chapter 04. The Burmese gloss `ကိုယ်စားလှယ် ကွင်းဆက်` is dropped because the book never uses it again.

### C2. `02:27` Orchestration defined as guardrails

**Current**

> ထို့ကြောင့် ကျွန်ုပ်တို့သည် "အရက်မူးနေသော ကပ္ပတိန်" ကို ထိန်းကျောင်းရန်အတွက် "သင်္ဘောသားများ" နှင့် "မြေပုံများ" ကို စနစ်တကျ ပြင်ဆင်ပေးရမည်။ ဤသည်ကို **Orchestration** ဟု ခေါ်သည်။ Agent သည် မိမိဘာသာ ဆုံးဖြတ်ချက် ချနိုင်သော်လည်း၊ ထိုဆုံးဖြတ်ချက်များကို ကျွန်ုပ်တို့ သတ်မှတ်ထားသော "ဘောင်" (Constraints) အတွင်း၌သာ ရှိစေရမည်။

**Proposed**

> ဒါကြောင့် "အရက်မူးနေတဲ့ ကပ္ပတိန်" ကို ထိန်းဖို့ "သင်္ဘောသား" တွေနဲ့ "မြေပုံ" တွေ ကြိုပြင်ထားရပါတယ်။ ဒီလို ဘောင်ခတ်တာကို **Guardrails** (Constraints) လို့ ခေါ်ပါတယ်။ Agent က ကိုယ့်ဘာသာ ဆုံးဖြတ်နိုင်ပေမယ့် ကျွန်တော်တို့ သတ်မှတ်ထားတဲ့ ဘောင်ထဲမှာပဲ ဆုံးဖြတ်ရပါမယ်။ ဥပမာ - "ကြိုက်သလို ဆုံးဖြတ်လို့ရတယ်၊ ဒါပေမဲ့ ငွေ တစ်သောင်းထက် ပိုသုံးမယ်ဆိုရင် ငါ့ကို အရင်မေး" ဆိုတာမျိုးပါ။
>
> **Orchestration** ကတော့ တစ်ခြား အရာပါ။ Agent, Tool, Memory, Human approval စတဲ့ အစိတ်အပိုင်းတွေကို ဘယ်အစီအစဥ်နဲ့ ဘယ်သူက ဘာလုပ်မလဲ ချိတ်ဆက် စီစဥ်ပေးတာကို ပြောတာပါ။ Guardrail က "ဘာ မလုပ်ရ" ကို သတ်မှတ်တယ်။ Orchestration က "ဘယ်လို အလုပ်လုပ်မလဲ" ကို စီစဥ်တယ်။ အခန်း ၃ မှာ Orchestration ကို ဒီအဓိပ္ပာယ်နဲ့ ဆက်သုံးသွားမှာပါ။

**What changed:** Guardrails and Orchestration separated. Chapter 03 already uses Orchestration correctly, so this fix also removes a contradiction between two chapters.

### C3. `04:25` Chain of Thought "significantly reduces hallucination"

**Current**

> ဤသို့ ထုတ်ဖော် ပြောဆိုခိုင်းခြင်း (Chain of Thought) သည် LLM ၏ ယောင်မှားမှု (Hallucination) ကို သိသိသာသာ လျှော့ချပေးနိုင်ကြောင်း ကျွန်ုပ်တို့ တွေ့ရှိရသည်။

**Proposed**

> ကိုယ် ဘာလုပ်နေလဲ ထုတ်ပြောခိုင်းတာကို **Chain of Thought** လို့ ခေါ်ပါတယ်။ ဒါက model ကို ပိုတော်သွားစေတာ မဟုတ်ပါဘူး။ အဓိက အသုံးဝင်တာက ကျွန်တော်တို့ ဘက်ကပါ။ Agent ဘယ်နေရာမှာ လမ်းလွဲသွားလဲ log ထဲမှာ ပြန်ကြည့်လို့ရတယ်။ Tool ခေါ်ဖို့ ဘာကြောင့် ဆုံးဖြတ်ခဲ့လဲ သိရတယ်။ Hallucination ကိုတော့ ဒါတစ်ခုတည်းနဲ့ မကာကွယ်နိုင်ပါဘူး။ Tool result ကို ပြန်စစ်တာ (Observation) နဲ့ Verifier (အခန်း ၈) က ပိုအရေးကြီးပါတယ်။

**What changed:** the uncited "significantly reduces hallucination" claim becomes a claim about observability, which is what the book actually demonstrates in chapters 08 and 10. It also stops promising something readers will test and find false.

### C4. `06:66-77` MCP Tool / Resource / Prompt as read vs write

**Current**

```text
Tool     = လုပ်
Resource = ဖတ်
Prompt   = ဘယ်လိုလုပ်
```
> - GitHub issue ကိုဖတ်ခြင်း = Resource
> - GitHub issue အသစ်ဖန်တီးခြင်း = Tool
> - Issue reply style guide = Prompt

**Proposed**

```text
Tool     = model က ခေါ်တယ်      (ဘာလုပ်မလဲ model ဆုံးဖြတ်)
Resource = app/host က ထည့်တယ်   (ဘာ context ပေးမလဲ app ဆုံးဖြတ်)
Prompt   = user က ရွေးတယ်       (ဘယ် template သုံးမလဲ user ဆုံးဖြတ်)
```
> ဥပမာ -
>
> - Model က issue #42 ကို ကြည့်ချင်လို့ `get_issue` ခေါ်တာ = Tool (ဖတ်တာပဲ ဖြစ်ပေမယ့် Tool ပါ)
> - Model က issue အသစ် ဖွင့်တာ = Tool
> - Editor က ဖွင့်ထားတဲ့ file ကို context ထဲ ကြိုထည့်ပေးတာ = Resource
> - User က `/review` template ကို ရွေးတာ = Prompt
>
> "ဖတ်/ရေး" နဲ့ မခွဲပါနဲ့။ ဘယ်သူက ဆုံးဖြတ်လဲ ဆိုတာနဲ့ ခွဲပါ။ Security အတွက် အရေးကြီးတာက Tool call တိုင်းကို model က ဆုံးဖြတ်တာမို့ Tool တွေမှာ permission ပြန်စစ်ရတယ် ဆိုတာပါ။ Webpage content ကတော့ ဘယ်လမ်းက ဝင်လာလာ data ပါ။ "previous instruction မလိုက်နာပါနဲ့" လို့ ရေးထားရင်လည်း instruction မဟုတ်ပါဘူး။

**What changed:** the MCP spec distinguishes the three by who controls them, not by read vs write. Read-only tools are common, and the GitHub MCP server exposes reading an issue as a tool. The security lesson at the end is kept and now follows from the correct model.

### C5. `12:100` and `12:102-103` P-2 "schema-level" guarantee and the bridge "rewrite"

**Current**

> Admin-only fields မပါနိုင်အောင် schema အဆင့်မှာခွဲထားသည်။

**Proposed**

> `UnsafeState` ထဲမှာ `secret_context` လို admin-only field တွေ မပါပါဘူး။ ဒါပေမယ့် `TypedDict` က type checker အတွက်သာ ဖြစ်ပြီး runtime မှာ ဘာမှ မတားပါဘူး။ Field တစ်ခု ထပ်ထည့်ပြီး dict ကို pass လိုက်ရင် Python က error မပေးပါဘူး။ တကယ် ကာကွယ်နေတာက `runtime.py` ထဲက `_customer_from_bridge_node` ပါ။ သူက `UnsafeState` အသစ် တစ်ခုကို field နှစ်ခုတည်းနဲ့ ကိုယ်တိုင် ဆောက်ပြီး customer node ကို ပေးတာမို့ secret တွေ ကူးမသွားတာပါ။ Schema က "ဒါ မပါသင့်ဘူး" လို့ ပြောတဲ့ စာချုပ်ပါ။ Runtime က စာချုပ်ကို တကယ် လိုက်နာအောင် လုပ်တဲ့ code ပါ။ နှစ်ခုလုံး လိုပါတယ်။
>
> Bridge ကလည်း admin_input ကို ပြင်ရေးတာ မဟုတ်ပါဘူး။ `bridge_input` အဖြစ် အတိုင်းသား ကူးထည့်တာပါ။ Secret ကို ဖျက်ပစ်တာ မဟုတ်ဘဲ မယူသွားတာပါ။ ဒါက ပိုရိုးရှင်းပြီး ပိုစစ်လွယ်ပါတယ်။

**What changed:** verified in `P-2/src/multi_agent_app/runtime.py:78-81` and `nodes.py:208`. The book's own line 203 already admits `TypedDict` has no runtime enforcement, so this moves the admission to where the claim is made.

### C6. `13:13` Travis-2 controls "depend on configuration"

**Current**

> Docker sandbox, AST validation, tool sanitization, safe summarization, skill signing တို့သည် configuration ပေါ်မူတည်သော controls များဖြစ်သည်။

**Proposed**

> Docker sandbox, AST validation, tool-output sanitization, safe summarization, skill signing တို့က configuration ပေါ် မူတည်ပါတယ်။ အရေးကြီးတာက `.env.example` ထဲမှာ `TRAVIS2_CODE_VALIDATION_ENABLED=false` နဲ့ `TRAVIS2_TOOL_SANITIZATION_ENABLED=false` ဖြစ်ပြီး `agent.py` ထဲ default တွေကလည်း `False` ပါ။ ဆိုလိုတာက repo ကို clone ပြီး ချက်ချင်း run ရင် ဒီ control နှစ်ခု အလုပ်မလုပ်ပါဘူး။ ဒီအခန်းမှာ control တစ်ခုချင်းစီ ပြောတဲ့အခါ "default ဖွင့်လား ပိတ်လား" ကို ထည့်ပြောသွားပါမယ်။

**What changed:** verified at `travis-2/.env.example:88-89` and `travis-2/src/travis_2/agent.py:257,259`. A reader who follows the chapter and runs the repo gets a different system from the one described unless this is said.

### C7. `14` BrowserSurfer HITL list and `--disable-web-security`

**Proposed addition to the HITL section**

> BrowserSurfer က HITL ဖွင့်ထားရင် `browser_evaluate`, `browser_navigate`, `browser_submit_form` ကို approval မေးပါတယ်။ ဒါပေမယ့် `browser_click` နဲ့ `browser_type` ကို မမေးပါဘူး။ ဒီအခန်းမှာ "settings click တစ်ချက်လည်း mutation ပါ" လို့ ပြောထားတာနဲ့ ဒီ list က ကိုက်မကိုက် ဖတ်သူ ကိုယ်တိုင် စဥ်းစားကြည့်ပါ။ ဒါက ဒီ repo မှာ သိထားရမယ့် gap တစ်ခုပါ။ Lab ထဲမှာ `browser_click` ကို `interrupt_on` ထဲ ထပ်ထည့်ကြည့်ပြီး ဘာကွာသွားလဲ ကြည့်ပါ။

**Proposed addition to the sandbox section**

> `src/session/__init__.py` မှာ Chromium ကို `--disable-web-security` နဲ့ launch ပါတယ်။ ဒါက browser ရဲ့ same-origin policy ကို ပိတ်တာပါ။ Page တစ်ခုက တစ်ခြား site ရဲ့ data ကို ဖတ်လို့ ရသွားပါတယ်။ ကိုယ့် Facebook account တကယ် login ထားတဲ့ browser မှာ ဒီ flag မသုံးပါနဲ့။ Lab profile အတွက်သာပါ။

**What changed:** verified at `bot/src/agents/facebook_surfer.py:340-346` and `bot/src/session/__init__.py:33`. A chapter titled browser agent security has to name the one flag that disables the browser's own security.

### C8. `15:130` appV2.2 coupling test

**Current**

> အကယ်၍ appv22 သည် Pi/Hermes folder များကို runtime ထဲမှတိုက်ရိုက် import လုပ်နေခဲ့လျှင် boundary မသန့်တော့။ စမ်းသပ် project တစ်ခုဖြစ်သော်လည်း ထို boundary ကို test ဖြင့်စစ်ထားခြင်းကောင်းသည်။

**Proposed**

> appv22 က Pi/Hermes folder တွေကို runtime ထဲက တိုက်ရိုက် import လုပ်နေရင် boundary မသန့်တော့ပါဘူး။ `tests/test_no_appv21_coupling.py` ဆိုတဲ့ test ရှိပါတယ်။ ဒါပေမယ့် သူ စစ်တာက `appv21` ဆိုတဲ့ စာလုံး source ထဲ ပါမပါပဲ ဖြစ်ပြီး Pi/Hermes import ကို မစစ်ပါဘူး။ ဒါကြောင့် "boundary ကို test နဲ့ စစ်ထားတယ်" လို့ ပြောရင် တစ်ဝက်ပဲ မှန်ပါတယ်။ Beginner အတွက် သင်ခန်းစာက ဒီမှာပါ။ Test နာမည်က ပြောတာနဲ့ test ကိုယ်တိုင် စစ်တာ တူရဲ့လား အမြဲ ပြန်ဖတ်ပါ။

**What changed:** verified at `allthebest/appV2.2/tests/test_no_appv21_coupling.py:7,20-30`. The weaker true claim makes a better lesson than the stronger false one.

---

## Part D. How to apply at scale

1. Fix Part C items first. Eight edits, each local to one paragraph, no voice decision needed.
2. Pick one short chapter (04 is the best candidate at 13 KB and the most important) and rewrite it fully in the Part B register. Read it aloud. If it sounds like you explaining to a junior at work, that is the target.
3. Add the Part A table to `STYLE_GUIDE.md` so contributors apply the same rules.
4. Then do the remaining chapters one per PR. The `Beginner အနေနှင့်…` asides and most of chapter 17 are already in the target register and can stay as they are.
