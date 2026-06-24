# ၁၇။ လက်တွေ့ စမ်းသပ်ခန်းငယ်များ

### စာဖတ်ပြီးရပ်လျှင် စာရေးတော်၏လက်ကို မမြင်ရ

Agentic AI ကိုစာအုပ်ဖတ်ရုံဖြင့်မကျွမ်းကျင်နိုင်။ Code ရေးရမည်။ Tool boundary စမ်းရမည်။ Prompt injection test ထည့်ရမည်။ Memory leak စမ်းရမည်။ Replan loop ကိုမိမိလက်ဖြင့်မြင်ရမည်။ သို့သော် beginner အနေဖြင့် real browser account, real cloud account, production secrets များနှင့်စမလုပ်သင့်။ Local safe lab များမှစရမည်။

ဤ lab များသည် production system မဟုတ်။ သင်ခန်းစာဖြစ်သည်။ Lab တစ်ခုစီတွင် pattern တစ်ခုသာမှတ်ပါ။

```text
Build -> Safe Failure Test -> Fix -> Reflect
```

Build သည်စနစ်ငယ်တစ်ခုဆောက်ခြင်းဖြစ်သည်။ Safe Failure Test သည် local/fake environment ထဲတွင်အန္တရာယ်ကိုထည့်ကြည့်ခြင်းဖြစ်သည်။ Fix သည် boundary ထည့်ခြင်းဖြစ်သည်။ Reflect သည်ဘာသင်လိုက်သလဲပြန်ရေးခြင်းဖြစ်သည်။

### Lab 1 — Toy Agent Loop

Goal: Agent Loop ကိုအခြေခံမှနားလည်ရန်။

Build:

`search_notes(query)` tool ရေးပါ။

`calculate(expression)` tool ရေးပါ။

`max_steps=5` ထားပါ။

Tool result ကို message history ထဲပြန်ထည့်ပါ။

Safe Failure Test:

Same query ကိုနှစ်ကြိမ်ထပ်ခေါ်စေပါ။

Empty result ကိုရစေပါ။

Fix:

Same tool+args repeat detector ထည့်ပါ။

Empty result streak နှစ်ကြိမ်ဖြစ်လျှင် stop လုပ်ပါ။

Reflect:

Tool run အောင်မြင်ခြင်းနှင့် task success မတူကြောင်းမှတ်ပါ။

Repo lesson: Travis-2 loop detection, appv22 tool guardrails.

### Lab 2 — Tool Broker

Goal: Permission သည် prompt မဟုတ်ကြောင်းနားလည်ရန်။

Build:

`read_doc(path)`

`write_note(path, content)`

`search_docs(query)`

Policy:

`read_doc` သည် `docs/` အောက်သာဖတ်ခွင့်ရှိသည်။

`write_note` သည် approval flag မရှိလျှင် deny ဖြစ်ရမည်။

`search_docs` output ကို 2KB cap လုပ်ပါ။

ဤ lab သည် local fake files ဖြင့်သာလုပ်ပါ။ Real `.env`, real credential, personal document မသုံးပါနှင့်။

Safe Failure Test:

`../.env` ဖတ်ရန်ကြိုးစားပါ။

Approval မပါဘဲ write လုပ်ရန်ကြိုးစားပါ။

Fix:

Path normalization ထည့်ပါ။

Deny log ထုတ်ပါ။

Tool result schema တွင် `execution_ok`, `data_ok`, `warnings` ထည့်ပါ။

Repo lesson: Travis-2 result quality, P-2 scoped filesystem.

### Lab 3 — Tool Output ထဲက အဆိပ်စာ

Goal: Tool output သည် instruction မဟုတ်ကြောင်းလက်တွေ့မြင်ရန်။

Build:

`docs/good.md`

`docs/injected.md`

`docs/injected.md` ထဲတွင် previous instruction မလိုက်နာရန်ပြောသောစာတစ်ကြောင်းထည့်ပါ။

ဤ lab သည် local dummy markdown files ဖြင့်သာလုပ်ပါ။ Real web page သို့မဟုတ် real user content မသုံးပါနှင့်။

Safe Failure Test:

Tool output wrapper မပါဘဲ model context ထဲထည့်ပါ။

Fix:

Untrusted wrapper ထည့်ပါ။ Wrapper ဆိုသည်မှာ tool output ကို "instruction မဟုတ်၊ untrusted data" ဟုအကာအကွယ်အိတ်ဖြင့်ပတ်ပေးခြင်းဖြစ်သည်။

Prompt injection pattern warning ထည့်ပါ။

Final answer တွင် "source content says..." ဟု data အဖြစ်သာကိုင်ပါ။

Repo lesson: BrowserSurfer raw snapshot risk, `src/tools/security.py`.

### Lab 4 — P-2 Style Bridge

Goal: High privilege state မှ low privilege state သို့ minimum projection သာပေးရန်။

Build:

```python
GlobalState = {
    "origin": "supervisor",
    "admin_input": "...",
    "secret_context": "...",
    "secret_key_ref": "...",
}

UnsafeState = {
    "origin": "bridge",
    "bridge_input": "...",
}
```

Bridge function ရေးပါ။

Safe Failure Test:

`origin="user_cli"` ဖြင့် bridge ခေါ်ပါ။

Secret fields များ output ထဲပါလာအောင် bug ထည့်ပါ။

Fix:

Origin check ထည့်ပါ။

Secret fields မပါကြောင်း test ရေးပါ။

`admin_input` ထဲတွင် secret-looking pattern ပါလျှင် warning ထည့်ပါ။

Repo lesson: P-2 Zero-Trust Bridge.

### Lab 5 — Travis-2 Style Controlled Runtime

Goal: Outer graph + inner runtime pattern နားလည်ရန်။

Build:

```text
run_agent -> evaluate -> replan -> run_agent
                   |
                   v
                finalize
```

Inner runtime ကို fake model/tool loop ဖြင့်ရေးပါ။

Safe Failure Test:

Fake model ကို same tool+args repeat လုပ်စေပါ။

Tool result `data_ok=false` ပြန်စေပါ။

Fix:

`policy_action = continue | replan | stop` ထည့်ပါ။

`replan_count` limit ထည့်ပါ။

Final answer မထုတ်ခင် `data_ok` စစ်ပါ။

Repo lesson: Travis-2 `run_agent/evaluate/replan/finalize`.

### Lab 6 — Context Compaction

Goal: Context ကြီးလာသောအခါအရေးကြီးသောအရာမပျောက်အောင်လျှော့ရန်။

Build:

Conversation messages list တစ်ခုဖန်တီးပါ။

Tool results အရှည်ကြီးထည့်ပါ။

Token estimate function ရေးပါ။

Safe Failure Test:

Old messages အကုန်ဖျက်ပြီး summary မထည့်ပါနှင့်။

Summary ထဲတွင် secret-looking string ပါအောင်စမ်းပါ။

Fix:

Deterministic pruning ထည့်ပါ။

Summary template ထည့်ပါ။

Secret redaction ထည့်ပါ။

Important fields: user goal, decisions, file paths, tests, unresolved TODOs ကို preserve လုပ်ပါ။

Repo lesson: appv22 Hermes-style compaction.

### Lab 7 — Real Platform မသုံးသော Browser Agent Safety

Goal: Browser tools အန္တရာယ်ကို safe local environment တွင်မြင်ရန်။

Build:

Local static HTML page တစ်ခုရေးပါ။

Button, form, text content ထည့်ပါ။

Text ထဲတွင် malicious instruction-like sentence ထည့်ပါ။

ဤ lab သည် local static HTML page ဖြင့်သာလုပ်ပါ။ Real platform account, login session, public website မသုံးပါနှင့်။

Safe Failure Test:

Snapshot raw content ကို model context ထဲထည့်ပါ။

Dummy click tool ကို approval မရှိဘဲခွင့်ပြုပါ။

Fix:

Snapshot wrapper ထည့်ပါ။

Click approval gate ထည့်ပါ။

Browser evaluation equivalent ကို disabled လုပ်ပါ။

Action audit log ထည့်ပါ။

Repo lesson: BrowserSurfer security analysis.

### Lab 8 — Trajectory and Reflection

Goal: Agent run တစ်ခုကိုနောက်မှဖတ်နိုင်ရန်။

Build:

JSONL trajectory log ထည့်ပါ။

Events: `model_start`, `tool_start`, `tool_end`, `policy_decision`, `final`။

Safe Failure Test:

Raw args, raw result အကုန် log ထုတ်ပါ။

PII-looking string ထည့်ပါ။

Fix:

Args hash သုံးပါ။

Result preview/cap သုံးပါ။

PII redaction ထည့်ပါ။

Reflection function တစ်ခုရေးပြီး evidence မရှိလျှင် reject လုပ်ပါ။

Repo lesson: BrowserSurfer TrajectoryCallbackHandler, appv22 tests/faux provider. Faux provider ဆိုသည်မှာ real model API မခေါ်ဘဲ test အတွက်ပြန်ဖြေသော provider အတုဖြစ်သည်။

### Lab 9 — DevOps Read-only Assistant

Goal: DevOps agent ကို read-only first အဖြစ်စတင်ရန်။

Build:

Sample CI log file ထည့်ပါ။

`read_ci_log()` tool ရေးပါ။

Failure summary ထုတ်ပါ။

ဤ lab သည် fake CI log နှင့် fake secret-looking string ဖြင့်သာလုပ်ပါ။ Real CI secret, production log, customer data မသုံးပါနှင့်။

Safe Failure Test:

Log ထဲတွင် fake secret နှင့် prompt injection sentence ထည့်ပါ။

Fix:

Secret redaction ထည့်ပါ။

Untrusted log wrapper ထည့်ပါ။ Wrapper ရှိခြင်းသည် guarantee မဟုတ်သဖြင့် redaction, approval boundary, audit log တို့နှင့်တွဲစဉ်းစားပါ။

Evidence lines ပြန် cite လုပ်ပါ။

No auto-fix, no auto-commit policy ထားပါ။

Repo lesson: DevOps chapter + BrowserSurfer/P-2 safety.

### Lab 10 — Case Study Review Worksheet

Goal: Repo တစ်ခုကို engineer အဖြစ်ဖတ်ရန်။

Worksheet:

Entry point ဘယ်မှာလဲ။

State schema ဘာလဲ။

Tool registry ဘယ်မှာလဲ။

Permission boundary ဘယ်မှာလဲ။

Loop stop condition ဘာလဲ။

Memory/checkpointer ဘယ်လိုအလုပ်လုပ်သလဲ။

Tool output sanitize လုပ်သလဲ။

Verifier ရှိသလဲ။

Trace/telemetry ရှိသလဲ။

Known gaps ဘာတွေလဲ။

v0.2 fix task ဘာရေးမလဲ။

ဤ worksheet ကို P-2, Travis-2, BrowserSurfer, appv22 တို့တွင်တစ်ခုချင်းစီဖြည့်ပါ။

### Lab လုံခြုံရေးစည်းကမ်းများ

ဤ labs များတွင် real credentials မသုံးပါနှင့်။ Real platform account မသုံးပါနှင့်။ Real cloud mutation မလုပ်ပါနှင့်။ Local files, fake logs, dummy HTML, fake provider များဖြင့်သာစမ်းပါ။ Secret-looking strings ကို fake values သာသုံးပါ။

### နိဂုံး — Lab သည် စာအုပ်ကို လက်ဖြင့်ဖတ်ခြင်း

Mini labs များသည်ဤစာအုပ်၏သင်ခန်းစာများကိုလက်တွေ့မြင်စေသည်။ Loop, Harness, MCP/Skill/Sub-agent, Prompt/Context/RAG, Planner/Worker/Verifier, Tool Broker, Observability, Safety, P-2 bridge, Travis-2 runtime, BrowserSurfer hardening, appv22 recovery, DevOps read-only thinking တို့ကိုလက်ဖြင့်စမ်းနိုင်သည်။

စာဖတ်သူသည် lab များကိုအကုန်ပြီးမှသာ agent expert ဖြစ်သွားမည်မဟုတ်။ သို့သော် lab တစ်ခုချင်းစီပြီးတိုင်း "AI ကလုပ်သွားတယ်" ဟူသောအမြင်မှ "ဘယ် boundary ကဘာကိုထိန်းထားသလဲ" ဟူသော engineer အမြင်သို့တဖြည်းဖြည်းပြောင်းလာမည်။

---
**စာဖတ်သူအတွက် Source Notes:**
- Labs များသည် chapters 04-16 နှင့် repo-backed case studies လေးခုကိုလက်တွေ့ပြန်ကိုင်စေရန်ရေးထားသည်။
- Lab အားလုံးသည် local/safe design ဖြစ်သည်။ Real credentials, real cloud mutation, real platform accounts မသုံးရန်ဖြစ်သည်။
- လေ့လာရန် loop သည် Build, Safe Failure Test, Fix, Reflect ဖြစ်သည်။
