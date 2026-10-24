# အခန်း ၁၈ - Myanmar Developer Roadmap

### အရာအားလုံးကို တစ်ပြိုင်နက် မလေ့လာပါနှင့်

Agentic AI လောကထဲဝင်လာသောအခါ စာဖတ်သူသည် စကားလုံးများစွာကိုတစ်ပြိုင်နက်တွေ့လိမ့်မည်။ LLM, Transformer, Tool Calling, MCP, RAG, LangGraph, DeepAgents, Skill, Sub-agent, Browser agent, DevOps automation, Coding agent စသည်တို့ဖြစ်သည်။ အရာအားလုံးကိုတစ်နေ့တည်းအကုန်ဖတ်ရန်ကြိုးစားလျှင် နားလည်မှုမတိုးဘဲ စကားလုံးများသာခေါင်းထဲရောသွားနိုင်သည်။

Framework များများသိခြင်းထက် concept အစီအစဉ်မှန်ခြင်းကပိုအရေးကြီးပါသည်။ Agentic AI ကိုလေ့လာရာတွင်လည်းမြေပုံလိုသည်။ မြေပုံမရှိလျှင် နာမည်ကြီး framework တစ်ခုမှနောက်တစ်ခုသို့ပြေးရင်း အင်ဂျင်နီယာအမြင်မရနိုင်ပါ။

### ပထမအဆင့်၊ စာရေးတော်ကို သိခြင်း

ပထမအဆင့်တွင် LLM, prompt, token, context, tool calling ကို နားလည်ပါ။ LLM သည် database မဟုတ်ကြောင်းသိပါ။ Tool output သည် instruction မဟုတ်ကြောင်း သိပါ။ Model output သည် probability-based ဖြစ်ကြောင်းသိပါ။ Transformer နှင့် attention ကို beginner အဆင့်နားလည်ရုံလုံလောက်သည်။ Machine learning textbook အကုန်ဖတ်ရန်မလိုသေး။

ဒီအဆင့်တွင် အခန်း ၀၁, ၀၂, ၀၃ ကို ပြန်ဖတ်ပါ။ Agentic AI ဆိုတာ ဘာလဲ၊ Workflow နှင့် Agent ဘာကွာသလဲ၊ Tool Calling ကို စာရေးတော်၏ လက်များဟု ဘာကြောင့် ပြောထားသလဲ ဆိုသည်ကို ကိုယ့်စကားဖြင့် ရှင်းပြနိုင်မှ နောက်အဆင့်သို့ သွားပါ။

### ဒုတိယအဆင့်၊ Workflow နှင့် Agent ကို ခွဲခြင်း

n8n ကဲ့သို့သော workflow tools များကိုလေ့လာပါ။ Deterministic automation သည် အလွန် ကောင်းသော အရာ ဖြစ်နိုင်သည်။ Agent သုံးရန်မလိုသောအရာကို Agent မသုံးခြင်းသည် engineering skill ဖြစ်သည်။

အလုပ်တစ်ခု Agent လိုသလား ဆုံးဖြတ်ရန် အချက် လေးချက် ကြည့်ပါ။ Rule-based ဖြစ်လျှင်၊ human judgment မလိုလျှင်၊ tool result အပေါ် မူတည်ပြီး လမ်းကြောင်း ပြောင်းရန် မလိုလျှင်၊ risk သေးလျှင် workflow ဖြင့် လုံလောက်သည်။ ဒီအချက်များ ခွဲတတ်မှ Workflow နှင့် Agent ကို ခွဲနိုင်ပါမည်။

### တတိယအဆင့်၊ Loop နှင့် Harness

Agent Loop သည် model/tool/observation cycle ဖြစ်သည်။ Harness သည် permission, memory, sandbox, verification, observability, persistence, safety ဖြစ်သည်။ Loop နှင့် Harness မခွဲနိုင်သေးလျှင် complex framework သို့မဝင်သေးပါနှင့်။

အခန်း ၀၄ နှင့် ၀၅ ကိုလေ့လာပါ။ Loop သည် အလုပ်လုပ်စေသည်။ Harness သည် အလုပ်ကို ဘောင်ထဲတွင်ထားသည်။ Modern agent များသည် loop inside harness ဖြစ်သည်။ ဒီဝါကျကိုလက်တွေ့နားလည်မှ နောက်တစ်ဆင့်သို့သွားပါ။

### စတုတ္ထအဆင့်၊ Prompt မှ Context သို့

Prompt Engineering ကို အရင် သင်ပါ။ Model ကို ဘယ်လို ခိုင်းမလဲ၊ output format ဘယ်လို သတ်မှတ်မလဲ၊ မသိလျှင် မသိကြောင်း ပြောခွင့် ပေးထားသလား၊ tool သုံး/မသုံး ဘယ်လို ဆုံးဖြတ်မလဲ ဆိုသည်တို့ကို prompt ထဲတွင် ရှင်းရှင်း ရေးတတ်ရမည်။

ထို့နောက် Context Engineering သို့သွားပါ။ Context window သည် စားပွဲပေါ်ရှိလက်ရှိစာရွက်ပုံဖြစ်သည်။ `AGENTS.md` နှင့် `SKILL.md` သည် agent အတွက်အလုပ်ခွင်စည်းကမ်းစာအုပ်ဖြစ်နိုင်သည်။ Compaction လုပ်သောအခါအရေးကြီးသောစည်းကမ်းများမပျောက်စေရ။ RAG သည် စာကြည့်တိုက်မှစာရွက်ပြန်ရှာပေးခြင်းဖြစ်သည်။ Memory သည် သိမ်းသင့်သော အရာကိုသာ ရွေးသိမ်းခြင်း ဖြစ်သည်။

### ပဉ္စမအဆင့်၊ Runtime Pattern များ

Planner/Worker/Verifier pattern, Tool Broker/Permission/Mutation Scope, Observability/Trajectory/Reflection တို့ကို အစီအစဉ်အတိုင်း လေ့လာပါ။ Safety chapter ကို ကျော်မသွားပါနှင့်။ Safety သည် Agentic AI ၏ အဓိက engineering discipline ဖြစ်သည်။

ဒီအဆင့်တွင် အခန်း ၀၈ မှ ၁၁ ကိုစနစ်တကျဖတ်ပါ။ Diagram များကိုကိုယ်တိုင်ပြန်ဆွဲပါ။ "ဒီ tool ကဘာကိုဖတ်ခွင့်ရှိလဲ", "ဘာကိုပြောင်းခွင့်ရှိလဲ", "အမှားဖြစ်လျှင်ဘယ် trace ကြည့်မလဲ" ဟုမေးပါ။

### ဆဋ္ဌမအဆင့်၊ Repo-backed Case Studies

Case study များကိုအလွတ်ဖတ်မထားပါနှင့်။ Repo ကိုဖွင့်ပြီး code path ကိုလိုက်ပါ။

P-2 မှ state boundary သင်ပါ။ Supervisor, Customer, Bridge သုံးခုကိုပုံဆွဲပါ။ `GlobalState` နှင့် `UnsafeState` ကိုနှိုင်းပါ။

Travis-2 မှ ထိန်းထားသော runtime စည်းကမ်းကိုသင်ပါ။ အရင်ဆုံး framework နာမည်များကိုမကြည့်ပါနှင့်။ `run_playwright_code` သည် စာရေးတော်ရေးသော TypeScript Playwright စာရွက်ကို ဘယ်အလုပ်ခန်းထဲတွင် run လုပ်သလဲလိုက်ဖတ်ပါ။ Docker sandbox runner, TypeScript validation gate, `execution_ok/data_ok`, websearch skill recipes ကိုနားလည်ပြီးမှ outer graph, `policy_action`, reducer-safe messages, middleware stack ကိုဆက်ဖတ်ပါ။

BrowserSurfer မှ browser-agent risk သင်ပါ။ ToolRegistry, thread_id, trajectory, output sanitization, session isolation ကိုစစ်ပါ။

appv22 မှ runtime recovery engineering သင်ပါ။ Pi-style loop/events/tools/TUI နှင့် Hermes-style compaction/recovery/guardrails ကိုခွဲမြင်ပါ။ appv22 သည် final worker kernel မဟုတ်ကြောင်းမမေ့ပါနှင့်။

### သတ္တမအဆင့်၊ DevOps နှင့် Coding Agent Thinking

DevOps agent ကိုစမည်ဆိုပါက CI log summary, Terraform plan explanation, read-only repo summarizer ကဲ့သို့ low-risk tasks မှစပါ။ Production mutation ကို human approval မရှိဘဲမလုပ်ပါနှင့်။ Cloud credential ကို full admin မပေးပါနှင့်။ Tool output ကို untrusted data အဖြစ်ဖတ်ပါ။

Coding agent ကိုလေ့လာမည်ဆိုပါက code review, test failure explanation, small patch, no-secret scan, diff review, test run discipline တို့မှစပါ။ Agent ကို "အကုန်လုပ်" ဟုမခိုင်းပါနှင့်။ Task scope, file boundary, tests, verifier ကိုသတ်မှတ်ပါ။

### နောက်ဆုံးအဆင့်၊ ကိုယ်ပိုင် Project သေးသေး

ကိုယ်ပိုင် project သေးသေး တစ်ခု လုပ်ပါ။ Documentation assistant, test failure explainer, read-only repo summarizer, local HTML browser-safety lab, fake CI log analyzer တို့သည် ကောင်းသော စမှတ်များ ဖြစ်သည်။

Real browser account, real cloud mutation, production secrets, public platform automation များနှင့်စောစောမစပါနှင့်။ အရင်ဆုံး local lab များတွင် boundary ကိုမြင်အောင်လုပ်ပါ။

### လေ့လာပြီးကြောင်း ကိုယ်တိုင်စစ်ရန် Milestone များ

Milestone များသည် ကိုယ်တိုင် မျက်စိ ရှိလာပြီလား စစ်ရန် အမှတ်အသားများ ဖြစ်သည်။

1. LLM, prompt, context, tool calling ကို သူငယ်ချင်း တစ်ယောက်အား ဥပမာဖြင့် ရှင်းပြနိုင်ရမည်။
2. Workflow သုံးရမည့် အလုပ်နှင့် Agent သုံးရမည့် အလုပ်ကို ခွဲနိုင်ရမည်။
3. Toy loop တစ်ခု ရေးပြီး max steps, empty result stop, repeat detector ထည့်နိုင်ရမည်။
4. Tool တစ်ခုအတွက် read scope, mutation scope, approval rule ရေးနိုင်ရမည်။
5. P-2, Travis-2, BrowserSurfer, appv22 တို့တွင် core lesson တစ်ခုစီကို diagram အကြမ်းဖြင့် ရှင်းပြနိုင်ရမည်။
6. DevOps task တစ်ခုကို read-only assistant အဖြစ် စပြီး human approval မရှိဘဲ mutation မလုပ်အောင် design လုပ်နိုင်ရမည်။

အရေးကြီးဆုံး milestone မှာ "ဒီ Agent က ဘာမြင်သလဲ၊ ဘာလုပ်ခွင့် ရှိသလဲ၊ ဘယ်အချိန်မှာ ရပ်သလဲ၊ အမှားဖြစ်ရင် ဘယ် trace ကြည့်မလဲ" ဟု မေးတတ်လာခြင်း ဖြစ်သည်။

### နိဂုံး

ဒီလမ်းကြောင်း၏ရည်ရွယ်ချက်မှာ framework တစ်ခုကိုကိုးကွယ်ရန်မဟုတ်ပါ။ Engineer မျက်စိရရန်ဖြစ်ပါသည်။ Agent တစ်ခုကို မြင်သောအခါ Loop, Harness, Tool boundary, State projection တို့ ဘယ်မှာ ရှိသလဲ၊ Memory ကို ဘယ်လို သိမ်းသလဲ၊ Safety ကို ဘယ်လို ထိန်းသလဲ၊ Verifier က ဘာစစ်သလဲ ဆိုသည်ကို ထောက်ပြနိုင်လာလျှင် စာဖတ်သူသည် Agentic AI hype ထဲတွင် မလမ်းပျောက်တော့ပါ။

---

**စာဖတ်သူအတွက် Source Notes:**

- Source သည် ဒီစာအုပ်၏ အခန်းများနှင့် repo-backed case study လေးခု ဖြစ်သည်။
- Learning order သည် framework depth မတိုင်မီ mental model ကိုဦးစားပေးရန်စီထားခြင်းဖြစ်သည်။
