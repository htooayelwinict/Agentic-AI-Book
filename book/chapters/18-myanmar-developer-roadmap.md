# ၁၈။ မြန်မာ Developer များအတွက် လေ့လာရေးလမ်းကြောင်း

### အရာအားလုံးကို တစ်ပြိုင်နက် မစားပါနှင့်

Agentic AI လောကထဲဝင်လာသောအခါ စာဖတ်သူသည်စကားလုံးများစွာကိုတစ်ပြိုင်နက်တွေ့လိမ့်မည်။ LLM, Transformer, Tool Calling, MCP, RAG, LangGraph, DeepAgents, Skill, Sub-agent, Browser agent, DevOps automation, Coding agent စသည်တို့ဖြစ်သည်။ ထိုအရာများကိုတစ်နေ့တည်းအကုန်ဖတ်ရန်ကြိုးစားလျှင် စာအုပ်တစ်အုပ်လုံးကိုမစားဘဲဝါးရန်ကြိုးစားသောသူနှင့်တူသွားမည်။

Framework များများသိခြင်းထက် concept အစီအစဉ်မှန်ခြင်းကပိုအရေးကြီးသည်။ Agentic AI ကိုလေ့လာရာတွင်လည်းမြေပုံလိုသည်။ မြေပုံမရှိလျှင်နာမည်ကြီး framework တစ်ခုမှနောက်တစ်ခုသို့ပြေးရင်းအင်ဂျင်နီယာအမြင်မရနိုင်။

### ပထမအဆင့် — စာရေးတော်ကိုသိခြင်း

ပထမအဆင့်တွင် LLM, prompt, token, context, tool calling ကိုနားလည်ပါ။ LLM သည် database မဟုတ်ကြောင်းသိပါ။ Tool output သည် instruction မဟုတ်ကြောင်းသိပါ။ Model output သည် probability-based ဖြစ်ကြောင်းသိပါ။ Transformer နှင့် attention ကို beginner အဆင့်နားလည်ရုံလုံလောက်သည်။ Machine learning textbook အကုန်ဖတ်ရန်မလိုသေး။

ဤအဆင့်တွင် အခန်း ၀၁, ၀၂, ၀၃ ကိုပြန်ဖတ်ပါ။ Agentic AI ဆိုတာဘာလဲ။ Workflow နှင့် Agent ဘာကွာသလဲ။ Tool Calling သည်စာရေးတော်၏လက်များဟုဘာကြောင့်ပြောရသလဲ။ ဤမေးခွန်းများရှင်းမှနောက်အဆင့်သို့သွားပါ။

### ဒုတိယအဆင့် — Workflow နှင့် Agent ကိုခွဲခြင်း

n8n ကဲ့သို့သော workflow tools များကိုလေ့လာပါ။ Deterministic automation သည်မကောင်းသောအရာမဟုတ်။ အလွန်ကောင်းသောအရာဖြစ်နိုင်သည်။ Agent သုံးရန်မလိုသောအရာကို Agent မသုံးခြင်းသည် engineering skill ဖြစ်သည်။

အလုပ်တစ်ခုသည် rule-based ဖြစ်သလား။ Human judgment လိုသလား။ Tool result အပေါ်မူတည်ပြီးလမ်းကြောင်းပြောင်းရန်လိုသလား။ Risk ကြီးသလား။ ဤမေးခွန်းများမေးတတ်မှ Workflow နှင့် Agent ကိုခွဲနိုင်မည်။

### တတိယအဆင့် — Loop နှင့် Harness

Agent Loop သည် model/tool/observation cycle ဖြစ်သည်။ Harness သည် permission, memory, sandbox, verification, observability, persistence, safety ဖြစ်သည်။ Loop နှင့် Harness မခွဲနိုင်သေးလျှင် complex framework သို့မဝင်သေးပါနှင့်။

အခန်း ၀၄ နှင့် ၀၅ ကိုလေ့လာပါ။ Loop သည်အလုပ်လုပ်စေသည်။ Harness သည်အလုပ်ကိုဘောင်ထဲတွင်ထားသည်။ Modern agent များသည် loop inside harness ဖြစ်သည်။ ဤဝါကျကိုလက်တွေ့နားလည်မှ နောက်တစ်ဆင့်သို့သွားပါ။

### စတုတ္ထအဆင့် — Prompt မှ Context သို့

Prompt Engineering ကိုအရင်သင်ပါ။ Model ကိုဘယ်လိုခိုင်းမလဲ။ Output format ဘယ်လိုသတ်မှတ်မလဲ။ မသိလျှင်မသိကြောင်းပြောခွင့်ပေးထားသလား။ Tool သုံး/မသုံးဘယ်လိုဆုံးဖြတ်မလဲ။

ထို့နောက် Context Engineering သို့သွားပါ။ Context window သည်စားပွဲပေါ်ရှိလက်ရှိစာရွက်ပုံဖြစ်သည်။ `AGENTS.md` နှင့် `SKILL.md` သည် agent အတွက်အလုပ်ခွင်စည်းကမ်းစာအုပ်ဖြစ်နိုင်သည်။ Compaction လုပ်သောအခါအရေးကြီးသောစည်းကမ်းများမပျောက်စေရ။ RAG သည်စာကြည့်တိုက်မှစာရွက်ပြန်ရှာပေးခြင်းဖြစ်သည်။ Memory သည်အရာအားလုံးသိမ်းခြင်းမဟုတ်။ သိမ်းသင့်သောအရာကိုသာသိမ်းခြင်းဖြစ်သည်။

### ပဉ္စမအဆင့် — Runtime Pattern များ

Planner, Worker, Verifier pattern ကိုလေ့လာပါ။ Tool Broker, Permission, Mutation Scope ကိုလေ့လာပါ။ Observability, Trajectory, Reflection ကိုလေ့လာပါ။ Safety chapter ကိုကျော်မသွားပါနှင့်။ Safety သည်စိတ်မလှုပ်ရှားစရာအပိုင်းမဟုတ်။ Agentic AI ၏အဓိက engineering discipline ဖြစ်သည်။

ဤအဆင့်တွင် အခန်း ၀၈ မှ ၁၁ ကိုစနစ်တကျဖတ်ပါ။ Diagram များကိုကိုယ်တိုင်ပြန်ဆွဲပါ။ "ဒီ tool ကဘာကိုဖတ်ခွင့်ရှိလဲ", "ဘာကိုပြောင်းခွင့်ရှိလဲ", "အမှားဖြစ်လျှင်ဘယ် trace ကြည့်မလဲ" ဟုမေးပါ။

### ဆဋ္ဌမအဆင့် — Repo-backed Case Studies

Case study များကိုအလွတ်ဖတ်မထားပါနှင့်။ Repo ကိုဖွင့်ပြီး code path ကိုလိုက်ပါ။

P-2 မှ state boundary သင်ပါ။ Supervisor, Customer, Bridge သုံးခုကိုပုံဆွဲပါ။ `GlobalState` နှင့် `UnsafeState` ကိုနှိုင်းပါ။

Travis-2 မှ ထိန်းထားသော runtime စည်းကမ်းကိုသင်ပါ။ အရင်ဆုံး framework နာမည်များကိုမကြည့်ပါနှင့်။ `run_playwright_code` သည် စာရေးတော်ရေးသော TypeScript Playwright စာရွက်ကို ဘယ်အလုပ်ခန်းထဲတွင် run လုပ်သလဲလိုက်ဖတ်ပါ။ Docker sandbox runner, TypeScript validation gate, `execution_ok/data_ok`, websearch skill recipes ကိုနားလည်ပြီးမှ outer graph, `policy_action`, reducer-safe messages, middleware stack ကိုဆက်ဖတ်ပါ။

BrowserSurfer မှ browser-agent risk သင်ပါ။ ToolRegistry, thread_id, trajectory, output sanitization, session isolation ကိုစစ်ပါ။

appv22 မှ runtime recovery engineering သင်ပါ။ Pi-style loop/events/tools/TUI နှင့် Hermes-style compaction/recovery/guardrails ကိုခွဲမြင်ပါ။ appv22 သည် final worker kernel မဟုတ်ကြောင်းမမေ့ပါနှင့်။

### သတ္တမအဆင့် — DevOps နှင့် Coding Agent Thinking

DevOps agent ကိုစမည်ဆိုပါက CI log summary, Terraform plan explanation, read-only repo summarizer ကဲ့သို့ low-risk tasks မှစပါ။ Production mutation ကို human approval မရှိဘဲမလုပ်ပါနှင့်။ Cloud credential ကို full admin မပေးပါနှင့်။ Tool output ကို untrusted data အဖြစ်ဖတ်ပါ။

Coding agent ကိုလေ့လာမည်ဆိုပါက code review, test failure explanation, small patch, no-secret scan, diff review, test run discipline တို့မှစပါ။ Agent ကို "အကုန်လုပ်" ဟုမခိုင်းပါနှင့်။ Task scope, file boundary, tests, verifier ကိုသတ်မှတ်ပါ။

### နောက်ဆုံးအဆင့် — ကိုယ်ပိုင် Project သေးသေး

ကိုယ်ပိုင် project သေးသေးတစ်ခုလုပ်ပါ။ Documentation assistant တစ်ခုကောင်းသည်။ Test failure explainer တစ်ခုကောင်းသည်။ Read-only repo summarizer တစ်ခုကောင်းသည်။ Local HTML browser-safety lab တစ်ခုကောင်းသည်။ Fake CI log analyzer တစ်ခုကောင်းသည်။

Real browser account, real cloud mutation, production secrets, public platform automation များနှင့်စောစောမစပါနှင့်။ အရင်ဆုံး local lab များတွင် boundary ကိုမြင်အောင်လုပ်ပါ။

### လေ့လာပြီးကြောင်း ကိုယ်တိုင်စစ်ရန် Milestone များ

Milestone များသည် certificate မဟုတ်။ ကိုယ်တိုင်မျက်စိရှိလာပြီလားစစ်ရန်အမှတ်အသားများဖြစ်သည်။

ပထမ milestone — LLM, prompt, context, tool calling ကိုသူငယ်ချင်းတစ်ယောက်အားဥပမာဖြင့်ရှင်းပြနိုင်ရမည်။

ဒုတိယ milestone — Workflow သုံးရမည့်အလုပ်နှင့် Agent သုံးရမည့်အလုပ်ကိုခွဲနိုင်ရမည်။

တတိယ milestone — Toy loop တစ်ခုရေးပြီး max steps, empty result stop, repeat detector ထည့်နိုင်ရမည်။

စတုတ္ထ milestone — Tool တစ်ခုအတွက် read scope, mutation scope, approval rule ရေးနိုင်ရမည်။

ပဉ္စမ milestone — P-2, Travis-2, BrowserSurfer, appv22 တို့တွင် core lesson တစ်ခုစီကို diagram အကြမ်းဖြင့်ရှင်းပြနိုင်ရမည်။

ဆဋ္ဌမ milestone — DevOps task တစ်ခုကို read-only assistant အဖြစ်စပြီး human approval မရှိဘဲ mutation မလုပ်အောင် design လုပ်နိုင်ရမည်။

အရေးကြီးဆုံး milestone မှာ framework name မဟုတ်။ "ဒီ Agent ကဘာမြင်သလဲ၊ ဘာလုပ်ခွင့်ရှိသလဲ၊ ဘယ်အချိန်မှာရပ်သလဲ၊ အမှားဖြစ်ရင်ဘယ် trace ကြည့်မလဲ" ဟုမေးတတ်လာခြင်းဖြစ်သည်။

### နိဂုံး — Framework မဟုတ်၊ မျက်စိ

ဤလမ်းကြောင်း၏ရည်ရွယ်ချက်မှာ framework တစ်ခုကို worship လုပ်ရန်မဟုတ်။ Engineer မျက်စိရရန်ဖြစ်သည်။ Agent ကိုမြင်သောအခါ Loop ဘယ်မှာလဲ။ Harness ဘယ်မှာလဲ။ Tool boundary ဘယ်မှာလဲ။ State projection ဘယ်မှာလဲ။ Memory ဘယ်လိုသိမ်းလဲ။ Safety ဘယ်လိုထိန်းလဲ။ Verifier ဘာစစ်လဲ။ ဤမေးခွန်းများကိုမေးနိုင်လာလျှင် စာဖတ်သူသည် Agentic AI hype ထဲတွင်မလမ်းပျောက်တော့။

---

**စာဖတ်သူအတွက် Source Notes:**

- Source သည် full v0.1 manuscript synthesis နှင့် repo-backed case studies လေးခုဖြစ်သည်။
- Learning order သည် framework depth မတိုင်မီ mental model ကိုဦးစားပေးရန်စီထားခြင်းဖြစ်သည်။

