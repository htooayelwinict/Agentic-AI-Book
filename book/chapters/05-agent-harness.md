# ၀၅။ စာရေးတော်ကို ထိန်းကျောင်းသော ကြိုးများ

### ဦးနှောက်နှင့်လက်များရှိရုံဖြင့် မလုံလောက်ခြင်း

ယခင်အခန်းများတွင် ကျွန်ုပ်တို့သည် LLM ဟူသော "စာရေးတော်" အကြောင်း၊ ထိုစာရေးတော်၏ "လက်" များဖြစ်သော Tool Calling အကြောင်းနှင့်၊ ထိုလက်များကိုအသုံးပြု၍ အလုပ်တစ်ခုကိုအဆင့်ဆင့်လုပ်သွားသော Agent Loop အကြောင်းကိုလေ့လာခဲ့ကြသည်။ ယခုအခါ မေးခွန်းတစ်ခုကျန်နေသည်။ ဦးနှောက်ရှိပြီ၊ လက်ရှိပြီ၊ အလုပ်လုပ်သည့်ကွင်းဆက်ရှိပြီဆိုလျှင် Agent တစ်ခုအတွက်လုံလောက်ပြီလား။

အဖြေမှာ မလုံလောက်သေးချေ။ အကယ်၍သင်သည် အရက်မူးနေသော ကပ္ပတိန်တစ်ဦးအား သင်္ဘော၊ မြေပုံနှင့်အင်ဂျင်အားလုံးပေးလိုက်ပြီး "စင်ကာပူသို့သွားပါ" ဟုသာခိုင်းထားပါက ထိုသင်္ဘောသည်စင်ကာပူသို့ရောက်နိုင်သလို၊ သမုဒ္ဒရာအလယ်တွင်လမ်းပျောက်သွားနိုင်သည်။ ထို့ကြောင့် ကပ္ပတိန်ကိုထိန်းရန် သင်္ဘောသားများ၊ radar, compass, speed limit, fuel gauge, emergency brake, harbour rule များလိုအပ်သည်။ Agentic AI တွင် ထိုထိန်းကျောင်းမှုစနစ်ကိုပင် **Agent Harness** ဟုခေါ်နိုင်သည်။

Harness ဆိုသည်မှာ Agent Loop ကိုပတ်လည်မှထိန်းပေးသော အင်ဂျင်နီယာစနစ်ဖြစ်သည်။ Input ကိုဘယ်လိုလက်ခံမည်၊ Context ကိုဘယ်လိုထည့်မည်၊ Tool ကိုဘယ်လိုခွင့်ပြုမည်၊ Memory ကိုဘယ်လိုသိမ်းမည်၊ Dangerous action ဖြစ်လျှင်လူကိုဘယ်လိုမေးမည်၊ Error ဖြစ်လျှင်ဘယ်လိုပြန်ထူမည်၊ Agent ဘာလုပ်သွားသည်ကိုနောက်မှဘယ်လိုကြည့်မည်ဆိုသောအရာများအားလုံးသည် Harness အောက်တွင်ပါဝင်သည်။

### Harness သည် Framework နာမည်မဟုတ်

လူအများသည် Harness ဟူသောစကားလုံးကို framework တစ်ခု၏နာမည်ဟုထင်တတ်ကြသည်။ LangGraph သုံးလျှင် Harness ရပြီ၊ DeepAgents သုံးလျှင် Harness ရပြီ၊ LangChain middleware ထည့်လျှင် Harness ရပြီဟုအလွယ်ယူဆတတ်ကြသည်။ ဤယူဆချက်သည်အန္တရာယ်ရှိသည်။ Framework သည်အဆောက်အအုံဆောက်ရန်အတွက် သံချောင်းနှင့်သစ်သားပေးနိုင်သည်။ သို့သော်အိမ်၏ပုံစံ၊ တိုင်ခိုင်မာမှု၊ မီးဘေးလုံခြုံရေးတို့ကိုအင်ဂျင်နီယာကဆုံးဖြတ်ရသည်။

Agent Harness သည်ပစ္စည်းစုစည်းမှုမဟုတ်။ ဆုံးဖြတ်ချက်စုစည်းမှုဖြစ်သည်။ ဘာကို Agent မြင်ခွင့်ပေးမည်၊ ဘာကိုမပေးမည်၊ ဘယ် Tool ကိုဘယ်အခြေအနေတွင်ခေါ်ခွင့်ပေးမည်၊ ဘယ်အချိန်တွင် Stop လုပ်မည်၊ ဘယ်အချိန်တွင် Human Approval တောင်းမည်၊ ဘယ် memory ကိုဘယ် user အတွက်သိမ်းမည်ဆိုသောဆုံးဖြတ်ချက်များဖြစ်သည်။

DeepAgents ကဲ့သို့ framework များသည် tools, virtual filesystem, permissions, sandbox, skills, memory, summarization, subagents, human-in-the-loop စသည့်ပစ္စည်းများပေးနိုင်သည်။ သို့သော်ပစ္စည်းရရှိခြင်းသည်အိမ်ပြီးခြင်းမဟုတ်။ Framework သည်သံချောင်းနှင့်သစ်သားပေးသည်။ Harness ကိုတော့ engineer ကဆောက်ရသည်။ ဘယ်တိုင်ကိုဘယ်နေရာတွင်ထောင်မည်၊ မီးဘေးတံခါးဘယ်မှာထားမည်၊ ဧည့်သည်ကိုဘယ်ခန်းထဲဝင်ခွင့်ပေးမည်ဆိုတာ codebase တစ်ခုချင်းစီတွင်ဆုံးဖြတ်ရသည်။

Demo harness နှင့် real harness ကိုခွဲမြင်ပါ။ Demo harness တွင် user prompt, model call, tool list, final answer ရှိနိုင်သည်။ Presentation အတွက်လှသည်။ သို့သော် real harness တွင် permission check, state cleanup, tool timeout, output sanitizer, trace log, human approval, rollback path, memory isolation, failure recovery ပါရမည်။ Demo harness သည်စာရေးတော်ကိုစားပွဲတစ်လုံးပေးခြင်းဖြစ်သည်။ Real harness သည်အလုပ်ရုံတစ်ခုလုံးကိုစည်းကမ်းဖြင့်ဖွဲ့ခြင်းဖြစ်သည်။

### Harness ၏ အလုပ်များ

Harness ၏ပထမဆုံးအလုပ်မှာ **Context ကိုစီမံခြင်း** ဖြစ်သည်။ Model သည် context ထဲရှိသောအရာကိုသာမြင်နိုင်သည်။ User request, system prompt, tool description, retrieved docs, memory, skill file, browser snapshot, error log စသည်တို့အားလုံးသည် context ဖြစ်နိုင်သည်။ Context မကောင်းပါက Model ကောင်းသော်လည်း Agent မကောင်းနိုင်။

ဒုတိယအလုပ်မှာ **Tool Permission ကိုထိန်းခြင်း** ဖြစ်သည်။ Model က Tool Call တစ်ခုထုတ်နိုင်သည်။ သို့သော် ထို Tool ကိုတကယ် run ခွင့်ရှိမရှိ Runtime ကစစ်ရမည်။ "မလုပ်ပါနှင့်" ဟု prompt ထဲရေးထားခြင်းသည် permission မဟုတ်။ Tool Broker ကတားနိုင်မှ permission ဖြစ်သည်။

တတိယအလုပ်မှာ **Memory နှင့် State ကိုစီမံခြင်း** ဖြစ်သည်။ Agent သည်ယခင်ကဘာလုပ်ခဲ့သနည်း၊ user တစ်ယောက်၏ preference ကဘာလဲ၊ previous trajectory တွင်ဘာအောင်မြင်ခဲ့သနည်းဆိုတာကိုသိမ်းနိုင်သည်။ သို့သော် memory သည်ကောင်းကျိုးသာမဟုတ်။ မှားသော memory, stale memory, user တစ်ယောက်၏ memory ကိုတခြား user ထံထည့်မိခြင်းတို့သည်အန္တရာယ်ရှိသည်။

စတုတ္ထအလုပ်မှာ **Safety Boundary** ဖြစ်သည်။ Filesystem, browser session, shell command, cloud credential, API key, database connection စသည်တို့သည် Agent မြင်ခွင့်ရလျှင်အန္တရာယ်ကြီးနိုင်သည်။ Sandbox, scoped filesystem, read-only mode, approval gate များလိုသည်။

ပဉ္စမအလုပ်မှာ **Observability** ဖြစ်သည်။ Agent ဘာ Tool ကိုခေါ်သနည်း၊ ဘယ် result ရသနည်း၊ ဘာကြောင့် replan ဖြစ်သနည်း၊ ဘယ်အချိန် stop ဖြစ်သနည်းဆိုတာကိုနောက်မှကြည့်နိုင်ရမည်။ Trace မရှိသော Agent သည်မျက်စိပိတ်ထားသောလူကိုလမ်းညွှန်ခိုင်းခြင်းနှင့်တူသည်။

နောက်ဆုံးအလုပ်မှာ **Recovery** ဖြစ်သည်။ Tool fail ဖြစ်နိုင်သည်။ Context window ပြည့်နိုင်သည်။ Provider error ဖြစ်နိုင်သည်။ Browser session expire ဖြစ်နိုင်သည်။ Agent loop no-progress ဖြစ်နိုင်သည်။ Harness မရှိပါက Agent သည်ထိုအချိန်တွင်ပျက်ကျမည်။ Harness ရှိပါက ပြန်ထူနိုင်သည်။

### repo ဥပမာများ
အောက်ဖော်ပြပါ ဥပမာများသည် ကျွန်ုပ်စာရေးသူကိုယ်တိုင်တည်ဆောက်ထားသော (vibe code ထားသော) program repo များဖြစ်သည်။ ယင်းတို့ကိုအသုံးပြုပြီး Agentic AI နှင့်ပက်သက်သော အစိတ်အပိုင်းများ မည်သို့မည်ပုံ အကြမ်းဖျဥ်းတည်ဆောက်ထားပုံ လိုအပ်သော sdk နှင့် modules များအသုံးပြုထားပုံတို့ကို တတ်နိုင်သလောက် ရှေ့ဆက်အခန်းများတွင် ဆက်လက်ရှင်းပြသွားမည်ဖြစ်သည်။ 

### P-2 ထဲက Harness

P-2 repository သည် Harness ကို state boundary အဖြစ်သင်ပေးသည်။ Supervisor Agent သည် high privilege ဖြစ်သည်။ Customer Agent သည် low privilege ဖြစ်သည်။ Bridge Node သည် high privilege `GlobalState` မှ low privilege `UnsafeState` သို့ minimum safe instruction သာ project လုပ်သည်။ `secret_context` နှင့် `secret_key_ref` ကဲ့သို့ admin-only field များ customer side သို့မရောက်စေရ။

ဤသည်မှာ Harness ၏အကောင်းဆုံးဥပမာတစ်ခုဖြစ်သည်။ Model ကို "secret မပြောပါနှင့်" ဟုပြောခြင်းမဟုတ်။ Secret ကိုမြင်ခွင့်မပေးခြင်းဖြစ်သည်။ Customer Agent ကို admin files မဖတ်ပါနှင့်ဟုပြောခြင်းမဟုတ်။ `/docs` scope ကိုသာမြင်စေခြင်းဖြစ်သည်။ P-2 ၏သင်ခန်းစာမှာ Security သည် prompt မဟုတ်၊ architecture ဖြစ်သည်ဟုဆိုနိုင်သည်။

### Travis-2 ထဲက Harness

Travis-2 တွင် Harness ကို graph တစ်ခုတည်းအဖြစ်မမြင်သင့်။ Harness သည် graph အလှဆင်မဟုတ်။ အဓိကစက်ခန်းမှာ `run_playwright_code` tool ဖြစ်သည်။ Agent ရေးသော TypeScript Playwright စာရွက်ကို workspace ထဲရေးသည်။ လိုအပ်လျှင် AST validation တံခါးစောင့်ဖြတ်သည်။ ထို့နောက် host runner သို့မဟုတ် Docker sandbox runner ထဲတွင် run စေပြီး structured result ပြန်ယူသည်။ Outer LangGraph StateGraph နှင့် middleware stack သည် ထိုစက်ခန်းကိုပတ်လည်မှထိန်းသောဘောင်များဖြစ်သည်။

`AgentState` တွင် messages, loop_signals, policy_action, replan_count, telemetry, budget_snapshot စသည်တို့ပါသည်။ Middleware များသည် ModelCallLimit, SemanticLoopDetection, ContextEditing, Summarization, Skills loading စသည်တို့ကိုဆောင်သည်။ ဤသည်မှာ prompt ထဲတွင်မဖုံးထားသော policy plane ဖြစ်သည်။

Travis-2 မှသင်ရမည့်အချက်မှာ Harness သည် Agent ကိုကန့်သတ်ရန်သာမဟုတ်၊ Agent ကိုယုံကြည်နိုင်သောအလုပ်သမားဖြစ်လာအောင်လုပ်ရန်ဖြစ်သည်။ Docker sandbox ရှိသောကြောင့် model ရေးလာသော code သည် host နှင့်အလွန်နီးကပ်မသွားစေရ။ Loop detection ရှိသောကြောင့် လည်နေရုံနှင့်အလုပ်မတိုးသောအခြေအနေကိုမြင်နိုင်သည်။ Structured Playwright result ရှိသောကြောင့် `execution_ok` နှင့် `data_ok` ခွဲနိုင်သည်။ Reducer-safe message rewrite ရှိသောကြောင့် context editing ဖြစ်သောအခါ persistent state မပျက်သည်။

### BrowserSurfer ထဲက Harness

BrowserSurfer Bot တွင် Harness သည်ပို၍အရေးကြီးလာသည်။ Browser Tool များသည် real web page ကိုမြင်နိုင်ပြီး click, submit, JavaScript evaluate လုပ်နိုင်သည်။ ထို့ကြောင့် ToolRegistry, Pydantic schemas, SkillsMiddleware, MemorySaver, InMemoryStore, TrajectoryCallbackHandler, MetricsMiddleware, PII redaction, Qdrant trajectory store, ReflectionAgent စသည်တို့ပါလာသည်။

သို့သော် security analysis ကပြသကဲ့သို့ ထိုအရာများရှိရုံဖြင့်လုံခြုံသွားခြင်းမဟုတ်။ HITL disabled path ရှိနိုင်သည်။ Raw accessibility snapshot သည် prompt injection source ဖြစ်နိုင်သည်။ Shared browser session သည် state leakage ဖြစ်နိုင်သည်။ `browser_evaluate` သည် arbitrary JavaScript risk ဖြစ်နိုင်သည်။

ဤနေရာမှသင်ရမည့်အချက်မှာ Harness သည် "အင်္ဂါရပ်တွေများတယ်" ဆိုသောစာရင်းမဟုတ်ခြင်းဖြစ်သည်။ Feature ရှိခြင်းနှင့် safety enforce ဖြစ်ခြင်းသည်မတူ။ HITL config ရှိသည်ဆိုရုံဖြင့်လူ့ approval တကယ်တောင်းနေသည်ဟုမဆိုနိုင်။ Tool schema ရှိသည်ဆိုရုံဖြင့် permission boundary ရှိသည်ဟုမဆိုနိုင်။

### appv22 ထဲက Harness

appv22 သည် emerging runtime recovery lab ဖြစ်သည်။ ၎င်းကို final worker kernel ဟုမခေါ်ရ။ သို့သော် Harness တည်ဆောက်ရာတွင်ဘာတွေပါလာနိုင်သနည်းဆိုတာကိုကောင်းစွာမြင်စေသည်။ `agent/` တွင် loop နှင့် guardrails ရှိသည်။ `ai/` တွင် model provider များနှင့်ဆက်သွယ်ရာအခန်းရှိသည်။ Provider ဆိုသည်မှာ model ကိုတကယ်ခေါ်ပေးသော service layer ဖြစ်သည်။ `coding_agent/` တွင် session/tools/prompts ရှိသည်။ `compaction/` တွင် Hermes-style context compaction ရှိသည်။ `tui/` တွင် terminal ပေါ်မှ user-facing မျက်နှာပြင်ရှိသည်။

appv22 မှသင်ရမည့်အချက်မှာ Harness သည် runtime အရိုးတန်းဖြစ်လာနိုင်ခြင်းဖြစ်သည်။ Agent loop, provider error recovery, context overflow handling, tool-loop guardrails, session persistence, terminal status, tests စသည်တို့ကိုအတူတကွစဉ်းစားရသည်။ သို့သော် project သည် recovery lab ဖြစ်သောကြောင့် partial/gap/risk status များကိုဖုံးမထားရ။ Engineering honesty သည် Harness ၏အစိတ်အပိုင်းတစ်ခုပင် ဖြစ်သည်။

### Harness ကိုစစ်ရန် မေးခွန်းများ

Agent repository တစ်ခုကိုဖတ်သောအခါ အောက်ပါမေးခွန်းများကိုမေးပါ။

၁။ User input သည်ဘယ်နေရာမှဝင်သနည်း။

၂။ State schema တွင် high privilege နှင့် low privilege ခွဲထားသလား။

၃။ Tool registry ဘယ်မှာရှိသနည်း။

၄။ Tool permission ကို prompt ကထိန်းသလား၊ code ကထိန်းသလား။

၅။ Memory သည် user/thread/session အလိုက်ခွဲထားသလား။

၆။ Tool output ကို untrusted data အဖြစ်ကိုင်သလား။

၇။ Loop budget, timeout, stop condition ရှိသလား။

၈။ Trace log ရှိသလား။

၉။ Context window ပြည့်လျှင် compaction/recovery ရှိသလား။

၁၀။ Known gaps ကို docs ထဲတွင်ဖော်ပြထားသလား။

ဤမေးခွန်းများသည် Agentic AI ကို demo အဆင့်မှ engineering အဆင့်သို့ခေါ်ဆောင်သွားသောမေးခွန်းများဖြစ်သည်။

### နိဂုံး - စက်ကိုလွှတ်မထားဘဲ ထိန်းကျောင်းခြင်း

Agent Harness သည် Agent ကိုနှေးကွေးစေရန်ထားသော အတားအဆီးမဟုတ်။ Agent ကိုယုံကြည်ရသောအလုပ်သမားဖြစ်လာစေရန်ထားသော ထိန်းကျောင်းရေးစနစ်ဖြစ်သည်။ လူမိုက်အားဓားပေးပြီးတံခါးပိတ်ထားခြင်းသည်အန္တရာယ်ဖြစ်သည်။ သို့သော်လက်သမားအားကိရိယာပေးပြီး လုပ်ငန်းခွင်စည်းကမ်း၊ safety gear, supervisor, measurement tools ပေးခြင်းသည်အလုပ်ဖြစ်သည်။

Agentic AI တွင်လည်းထိုအတိုင်းပင်ဖြစ်သည်။ Loop သည်အလုပ်လုပ်စေသည်။ Harness သည်အလုပ်ကိုဘောင်ထဲတွင်ဖြစ်စေသည်။ နောက်အခန်းများတွင် ကျွန်ုပ်တို့သည် Harness ၏အစိတ်အပိုင်းများဖြစ်သော MCP, Skill, Sub-agent, Prompt Engineering, Context Engineering, Tool Broker, Observability, Safety စသည်တို့ကိုတစ်ခုချင်းစီဖွင့်ကြည့်မည်။

---
**စာဖတ်သူအတွက် Source Notes:**
- **Agent Harness:** Runtime infrastructure surrounding an agent loop: context, tools, state, safety, memory, observability, and recovery.
- **P-2:** State projection and scoped filesystem as security harness.
- **Travis-2:** `run_playwright_code`, Docker sandbox runner, validation gate, graph, and middleware together form the policy harness.
- **BrowserSurfer:** Browser-agent harness with registry, memory, trajectory, and security risks.
- **appv22:** Emerging recovery lab for loop, provider, compaction, TUI, and guardrails.
