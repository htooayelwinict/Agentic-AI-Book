# ၁၄။ BrowserSurfer Bot — Agent ကိုလက်ပေးသင်သောအခါ

> **ဤ browser agent က ဘာကိုပြသသလဲ**  
> BrowserSurfer Bot သည် DeepAgents abstraction အောက်တွင် LangGraph-style runtime, LangChain StructuredTool registry, Playwright browser tools, thread state, trajectory memory, RAG planning, reflection, metrics စသည်တို့ကိုပေါင်းထားသော browser-agent prototype ဖြစ်သည်။
>
> **Browser tool များ ဘာကြောင့်စွမ်းအားကြီးသလဲ**  
> Browser tool သည်စာဖတ်ရုံမဟုတ်။ Page ဖွင့်နိုင်သည်။ Snapshot ဖတ်နိုင်သည်။ Button နှိပ်နိုင်သည်။ Text ရိုက်နိုင်သည်။ Form state ပြောင်းနိုင်သည်။ JavaScript tool ပေးထားလျှင် page အတွင်းပိုင်းကိုလည်းထိနိုင်သည်။
>
> **Browser tool များ ဘာကြောင့်အန္တရာယ်ရှိသလဲ**  
> Browser သည်စာအုပ်တစ်အုပ်မဟုတ်။ လှုပ်ရှားနေသောမြို့တစ်မြို့ဖြစ်သည်။ မြို့ထဲကကြော်ငြာစာ၊ button label, aria label, console message, network result အားလုံးသည် trusted instruction မဟုတ်။ Raw snapshot, shared session, stale refs, arbitrary JavaScript, incomplete HITL, weak output boundary တို့ကြောင့် indirect prompt injection နှင့် unsafe action risk များရှိသည်။
>
> **လုံခြုံရေးသတိပေးချက်**  
> ဤအခန်းသည် သင်ကြားရေးအတွက်သာဖြစ်သည်။ Browser agent ကိုဘယ်လိုခိုင်မာအောင်ထိန်းမလဲ၊ ဘယ်နေရာတွေမှာအန္တရာယ်ပေါ်နိုင်သလဲဆိုတာကိုဖွင့်ပြသည်။ အန္တရာယ်ရှိသော platform misuse workflow များ၊ account/security misuse workflow များ၊ သို့မဟုတ် rule-avoidance workflow များကိုမသင်ပေးပါ။ Repo ထဲရှိ `FacebookSurfer` သည် internal codename ဖြစ်ပြီး public chapter name သည် **BrowserSurfer Bot** ဖြစ်သည်။

### Browser သည် စာမျက်နှာမဟုတ်၊ လှုပ်ရှားနေသောမြို့ဖြစ်သည်

Chatbot တစ်ခုသည်စာပြန်သည်။ Browser agent တစ်ခုသည်မြို့ထဲဝင်သွားသည်။ လမ်းပေါ်ရှိဆိုင်းဘုတ်များကိုဖတ်သည်။ တံခါးများကိုမြင်သည်။ Button များကိုနှိပ်နိုင်သည်။ Form များကိုဖြည့်နိုင်သည်။ Session ရှိလျှင်အရင်ကဖွင့်ထားသောအခန်းထဲအထိဝင်နိုင်သည်။ ဤသည်မှာ browser agent ၏အလှလည်းဖြစ်သည်။ အန္တရာယ်လည်းဖြစ်သည်။

ဤ chapter ကိုဖတ်ရာတွင် အရေးကြီးဆုံးအချက်တစ်ခုကိုအစကတည်းကမှတ်ထားပါ။ BrowserSurfer Bot ကို platform သုံးနည်းသင်ခန်းစာအဖြစ်မဖတ်သင့်ချေ။ ဤစာအုပ်သည် “ဘယ် website ပေါ်မှာ ဘယ် button ကိုနှိပ်” ဆိုသောလမ်းညွှန်မဟုတ်။ Browser ကို Agent ၏လက်ဖြစ်အောင်ပေးလိုက်သောအခါ runtime, state, tools, memory, planning, security boundary များမည်သို့ပြဿနာဖြစ်လာသနည်းကိုဖွင့်ပြသော case study ဖြစ်သည်။

Repo ထဲတွင် `FacebookSurferAgent` ဟူသော class name ကိုတွေ့ရမည်။ ထိုနာမည်သည် internal codename ဖြစ်သည်။ Public-facing chapter တွင် BrowserSurfer Bot ဟုခေါ်မည်။ Internal codename ကိုဖော်ပြရခြင်းမှာ source file ကိုဖတ်သောအခါ reader မလမ်းပျောက်ရန်သာဖြစ်သည်။

### အဓိကရုပ်သွင် — Agent တစ်ကောင်မဟုတ်၊ အလုပ်ခန်းများစွာ

BrowserSurfer Bot ကိုအပြင်မှကြည့်လျှင် “Agent တစ်ကောင်” ဟုမြင်ရသည်။ အတွင်းသို့ဝင်ကြည့်လျှင် အခန်းများစွာပါသောအလုပ်ရုံဖြစ်သည်။

```text
User task
   |
   v
FacebookSurferAgent / BrowserSurfer facade
   |
   +-- optional PlanningAgent
   |      |
   |      v
   |   Qdrant မှ similar trajectories ပြန်ရှာ
   |   Success plan / avoid pattern ပြင်ဆင်
   |
   v
DeepAgents create_deep_agent(...)
   |
   +-- LangGraph-style runtime
   +-- MemorySaver checkpointer
   +-- optional InMemoryStore
   +-- SkillsMiddleware
   +-- ToolRegistry -> LangChain StructuredTools
   |
   v
Browser tools -> Playwright session
   |
   v
TrajectoryCallbackHandler
   |
   v
MetricsMiddleware -> scoring -> PII redaction -> ReflectionAgent -> Qdrant
```

ဤပုံတွင်အဓိကသင်ခန်းစာမှာ BrowserSurfer သည် browser tool တစ်ခုတည်းမဟုတ်ခြင်းဖြစ်သည်။ Facade ရှိသည်။ Planner ရှိသည်။ Tool registry ရှိသည်။ Checkpointer ရှိသည်။ Memory store ရှိနိုင်သည်။ Skills middleware ရှိသည်။ Browser session ရှိသည်။ Trajectory observer ရှိသည်။ Metrics processor ရှိသည်။ Reflection နှင့် Qdrant storage ရှိသည်။

နောက်တစ်နည်းပြောရလျှင် စာရေးတော်တစ်ဦးကို browser မြို့ထဲလွှတ်လိုက်ခြင်းမဟုတ်။ စာရေးတော်ကိုမြို့ထဲလွှတ်သောအခါ တံခါးစောင့်၊ လက်နက်စာရင်း၊ မှတ်တမ်းရေးသူ၊ လမ်းကြောင်းအကြံပေးသူ၊ အမှိုက်စစ်သူ၊ အတွေ့အကြုံသိမ်းသူတို့ပါအတူလိုက်ရခြင်းဖြစ်သည်။

### `FacebookSurferAgent` — ဆိုင်မျက်နှာစာနှင့် အတွင်းစက်ခန်း

`src/agents/facebook_surfer.py` ထဲမှ `FacebookSurferAgent` သည် BrowserSurfer Bot ၏ facade/orchestrator ဖြစ်သည်။ Facade ဆိုသည်မှာဆိုင်မျက်နှာစာနှင့်တူသည်။ Customer သည်ဆိုင်ထဲရှိသိုလှောင်ခန်း၊ မီးဖိုခန်း၊ ငွေရှင်းခန်း၊ ပစ္စည်းတင်ခန်းအားလုံးကိုမမြင်ရ။ Counter တစ်ခုကိုသာမြင်သည်။ BrowserSurfer ၏ caller သည်လည်း `invoke`, `stream`, `stream_events`, `get_state`, `update_state` စသော method များကိုမြင်သည်။ အတွင်းဘက်တွင်ဘာတွေချိတ်ထားသနည်းဆိုတာကို facade ကဖုံးပေးထားသည်။

သို့သော် facade သည်အဖုံးကောင်းရုံဖြစ်သည်။ အဖုံးအောက်ကစက်ခန်းကိုမဖတ်လျှင်အန္တရာယ်မမြင်ရ။ Constructor ထဲတွင် အောက်ပါအရာများကိုစတင်တည်ဆောက်ထားသည်။

- `register_all_tools()` ဖြင့် ToolRegistry ထဲမှ tools များကိုယူသည်။
- `InMemoryStore()` ကို memory ဖွင့်ထားလျှင်သုံးနိုင်သည်။
- `MemorySaver()` ကို checkpointer အဖြစ်ထားသည်။
- Metrics ဖွင့်ထားလျှင် `MetricsMiddleware` ကိုတည်ဆောက်သည်။
- Planning ဖွင့်ထားလျှင် `PlanningAgent` ကိုတည်ဆောက်သည်။
- System prompt ကိုတည်ဆောက်ပြီး `create_deep_agent(...)` ဖြင့် DeepAgents runtime ဖန်တီးသည်။

ဤနေရာတွင် design pattern သင်ခန်းစာရှိသည်။ `FacebookSurferAgent` သည် caller အတွက် interface ကိုရိုးရှင်းစေသည်။ သို့သော် dependency များကို constructor injection ဖြင့်အပြင်ကထည့်သွင်းထားခြင်းထက် internal construction များရှိသောကြောင့် testability tradeoff ရှိသည်။ Beginner အတွက်ဆိုလျှင် “class တစ်ခုထဲမှာအရာအားလုံးချိတ်ထားတာပဲ” ဟုသာမမြင်ပါနှင့်။ Engineer အတွက်မေးခွန်းမှာ “ဒီ facade အောက်က dependencies ကို test မှာဘယ်လိုလဲလှယ်မလဲ” ဖြစ်သည်။

### DeepAgents သည် LangGraph ကိုဖုံးထားသောအလွှာ

CHAPTER-7.md ၏အဓိကသင်ခန်းစာတစ်ခုမှာ DeepAgents ကိုသုံးထားသော်လည်း graph thinking ပျောက်မသွားရခြင်းဖြစ်သည်။ BrowserSurfer source ထဲတွင် raw `StateGraph` node/edge code များကိုအများကြီးမတွေ့ရနိုင်။ အကြောင်းမှာ `create_deep_agent(...)` က LangGraph-style runtime skeleton ကို abstraction အဖြစ်ဖန်တီးပေးထားသောကြောင့်ဖြစ်သည်။

Beginner အတွက်ရိုးရိုးပြောလျှင် DeepAgents သည် “ကြိုတင်ဆောက်ထားသောအလုပ်ရုံ” ဖြစ်သည်။ သင်သည် model, tools, checkpointer, store, middleware, system prompt တို့ကိုပေးလိုက်သည်။ DeepAgents က LangGraph execution engine တစ်ခုကိုအောက်တွင်ဖန်တီးပေးသည်။ ထိုကြောင့် graph code မမြင်ရသော်လည်း graph behavior မရှိဟုမဆိုနိုင်။

BrowserSurfer ကို graph view ဖြင့်မြင်လျှင် အောက်ပါအဆင့်များကိုစဉ်းစားရမည်။

```text
Input adaptation
  -> optional planning enrichment
  -> model reasoning
  -> tool selection
  -> browser tool execution
  -> tool output back into context
  -> optional more tool calls
  -> final response
  -> metrics/reflection/storage side branch
```

Bug အများစုသည်ဤ edge boundaries များတွင်ပေါ်တတ်သည်။ Planning text လွန်ကဲသွားသလား။ Tool output ကို data အဖြစ်ပတ်ထားသလား။ `thread_id` မှန်သလား။ Browser session သည်အခြား task နှင့်ရောနေသလား။ Metrics callback က tool event များကိုမှန်ကန်စွာဖမ်းသလား။ Final answer မထုတ်မီ verification ရှိသလား။ Graph syntax မမြင်ရသောကြောင့် graph discipline မလိုတော့ခြင်းမဟုတ်။

### Demo ပုံများ — မြို့ထဲဝင်သွားသော Agent ကို မျက်စိဖြင့်မြင်ခြင်း

BrowserSurfer demo screenshots များထဲတွင် live browser UI, compose screen, settings screen, terminal trace, planner trace စသောပုံများရှိသည်။ ဤနေရာတွင် သင်မြင်ရမည့်ပုံများသည် author ၏ကိုယ်ပိုင် demo မှ actual screenshots များဖြစ်သည်။ Publication review တွင် secrets, API keys, third-party private messages များကိုမတွေ့ခဲ့ရ။ Raw set ထဲရှိပုံအားလုံးကိုမထည့်ပါ။ Chat list / inbox ကဲ့သို့ဤသင်ခန်းစာအတွက်မလိုသောပုံများကိုချန်ထားသည်။ ဤအခန်းသည် platform သုံးနည်းမသင်။ Browser agent တစ်ခုသည် “စာပြန်သောစက်” မှ “မျက်နှာပြင်ကိုထိနိုင်သောစက်” ဖြစ်လာသောအခါ အင်ဂျင်နီယာကဘာတွေကြည့်ရမလဲဆိုတာကိုသင်သည်။

ဤပုံများသည် browser-agent architecture နှင့် safety/hardening အချက်များကို ရှင်းပြရန် အသုံးပြုထားသော educational/demo evidence များသာ ဖြစ်သည်။ Platform အသုံးပြုနည်း၊ abuse workflow, credential automation, scraping, evasion, သို့မဟုတ် operational misuse ကို သင်ကြားရန် မဟုတ်ပါ။

ထို့ကြောင့်အောက်ပါပုံများသည် actual demo evidence ဖြစ်သော်လည်း စာအုပ်၏ရည်ရွယ်ချက်ကိုမမေ့ပါနှင့်။ ပုံကိုကြည့်၍ “ဒီလို click လုပ်ရမယ်” ဟုမဖတ်သင့်ချေ။ “Agent က live UI, session, snapshot, planner memory, mutation boundary တို့ကိုထိလာသောအခါ ဘယ်လိုထိန်းရမလဲ” ဟုဖတ်ရသည်။

![BrowserSurfer pic 1: actual live browser surface demo](../references/images/websurfer/selected/browsersurfer-actual-1-live-browser-surface.png)

**ပုံ ၁၄-၁ — စာရေးတော်သည် စာရွက်မဟုတ်၊ မျက်နှာပြင်ကိုထိနေပြီ**

ဤပုံကိုကြည့်လိုက်လျှင် BrowserSurfer ၏အချိုးအကွေ့ကိုချက်ချင်းခံစားရသည်။ Agent သည် chat box ထဲတွင်အကြံပေးနေသူမဟုတ်တော့။ Browser dialog တစ်ခုထဲတွင်စာသားရှိသည်။ Account context ရှိသည်။ Audience state ရှိသည်။ Control များရှိသည်။ စာရေးတော်၏လက်သည်စာရွက်ပေါ်မှတက်ပြီး မျက်နှာပြင်ပေါ်သို့ရောက်လာသည်။

ဤအချိန်သည် developer အတွက်အလှဆုံးလည်းဖြစ်သည်။ အန္တရာယ်အရှိဆုံးလည်းဖြစ်သည်။ Model ကရေးသောစာသည် UI ထဲရောက်သွားသည်နှင့် “အဖြေ” မဟုတ်တော့။ Mutatable state ဖြစ်သွားသည်။ ပုံထဲတွင် “Only me” demo ဖြစ်နေသော်လည်း engineering lesson မပြောင်းပါ။ Model output သည် UI state ဖြစ်လာသည့်အခါ approval boundary ကိုဘယ်နေရာတွင်ထားမလဲဆိုသောမေးခွန်းဖြစ်သည်။

![BrowserSurfer pic 2: actual post settings mutation boundary demo](../references/images/websurfer/selected/browsersurfer-actual-2-mutation-boundary.png)

**ပုံ ၁၄-၂ — Settings screen သည် UI မဟုတ်၊ mutation boundary ဖြစ်သည်**

Beginner မျက်လုံးဖြင့်ကြည့်လျှင် settings screen သည် option list တစ်ခုသာဖြစ်သည်။ Engineer မျက်လုံးဖြင့်ကြည့်လျှင် ဤနေရာသည် policy gate ဖြစ်သည်။ Audience, schedule, sharing surface, final save/post action စသည်တို့သည် “ဘယ်သူ့ထံသို့သက်ရောက်မလဲ၊ ဘယ်အချိန်သက်ရောက်မလဲ၊ ဘယ်လောက်အထိပြန့်မလဲ” ကိုဆုံးဖြတ်သည်။

Browser agent ကိုလွှတ်ထားသောအခါ အန္တရာယ်သည် final button ကြီးတစ်ခုတည်းတွင်မရှိ။ သေးငယ်သော setting တစ်ခုသည်လည်း mutation scope ကိုပြောင်းနိုင်သည်။ ထို့ကြောင့် BrowserSurfer ကဲ့သို့သော system တွင် HITL approval သည် final click မတိုင်မီတင်မဟုတ်။ “ဒီ state ကိုဒီအတိုင်းထားပြီးဆက်လုပ်ခွင့်ရှိသလား” ဆိုသောအဆင့်များတွင်ပါလိုနိုင်သည်။

![BrowserSurfer pic 3: actual dynamic browser UI state demo](../references/images/websurfer/selected/browsersurfer-actual-3-dynamic-ui-state.png)

**ပုံ ၁၄-၃ — Page သည် အသက်ရှင်နေသည်**

Browser page သည်စာအုပ်စာမျက်နှာမဟုတ်။ သင်ဖတ်နေစဉ်ပြောင်းနိုင်သည်။ Suggestion ပေါ်လာနိုင်သည်။ Dialog height ပြောင်းနိုင်သည်။ Button state ပြောင်းနိုင်သည်။ ပုံထဲက hashtag suggestion box သည်ဤအချက်ကိုကောင်းကောင်းပြသည်။ Ref အဟောင်းသည်အခုတော့နေရာမှားနိုင်သည်။ Agent က “မိနစ်အနည်းငယ်ကမြင်ခဲ့သော ref” ကိုယုံပြီးနှိပ်လိုက်လျှင် အခြေအနေအသစ်ကိုမထိတော့ဘဲ အမှားတံခါးကိုထိနိုင်သည်။

ဤပုံသည် stale snapshot ပြဿနာကိုမြင်စေသည်။ BrowserSurfer prompt ထဲတွင် action တစ်ခုပြီးတိုင်း fresh snapshot ယူရန်စည်းကမ်းထားခြင်းသည်အလှဆင်မဟုတ်။ Browser မြို့ထဲတွင်တံခါးများရွေ့နေသောကြောင့်ဖြစ်သည်။ Page state ကိုမပြန်ကြည့်သော Agent သည် လမ်းညွှန်စာအဟောင်းကိုကိုင်ပြီးမြို့ထဲလျှောက်နေသောလူနှင့်တူသည်။

![BrowserSurfer pic 4: actual session restore and snapshot/ref generation trace](../references/images/websurfer/selected/browsersurfer-actual-4-session-snapshot-trace.png)

**ပုံ ၁၄-၄ — Snapshot/ref စက်ခန်း**

ဤ terminal trace ထဲတွင် session restore, tools registered, actual demo task, `[REFS]`, `[SNAPSHOT]`, `aria_snapshot length`, `Generated refs`, `Interactive elements` စသည်တို့ကိုမြင်ရသည်။ ဤနေရာသည် BrowserSurfer ၏မျက်စိတည်ဆောက်ရာစက်ခန်းဖြစ်သည်။ Agent သည် page ကိုလူလိုမြင်ခြင်းမဟုတ်။ Accessibility snapshot နှင့် refs အဖြစ် text context ထဲသို့ပြန်ပေးထားသောမြေပုံကိုဖတ်နေခြင်းဖြစ်သည်။

ထိုမြေပုံသည်အရေးကြီးသည်။ သို့သော် trusted command မဟုတ်။ Page ထဲကစာသား၊ aria label, button label, console output တို့သည် external data ဖြစ်သည်။ ထို့ကြောင့် tool output wrapper, sanitizer, permission boundary, verifier တို့လိုလာသည်။ Snapshot/ref များကိုမျက်စိအဖြစ်သုံးရသည်။ ဦးနှောက်အဖြစ်မယုံရ။

![BrowserSurfer pic 5: actual RAG planning and similar-pattern trace](../references/images/websurfer/selected/browsersurfer-actual-5-planning-rag-trace.png)

**ပုံ ၁၄-၅ — အတိတ်အောင်မြင်မှုသည် လက်ရှိအမိန့်မဟုတ်**

ဤပုံတွင် metrics collection နှင့် RAG-based planning ဖွင့်ထားသည်ကိုမြင်ရသည်။ `Found 1 similar pattern(s)` ဟူသော signal သည် BrowserSurfer ကယခင် trajectory ကိုပြန်ကြည့်ပြီး planning ကိုကူညီနိုင်ကြောင်းပြသည်။ ဤ design သည်စိတ်ဝင်စားစရာကောင်းသည်။ Developer အတွက် “ငါ့ Agent ကအတွေ့အကြုံမှသင်ယူနေပြီ” ဟူသောအချိန်ဖြစ်သည်။

သို့သော်အတိတ်အောင်မြင်မှုသည်လက်ရှိ page အတွက်ဗျာဒိတ်တော်မဟုတ်။ UI ပြောင်းနိုင်သည်။ Ref များ stale ဖြစ်နိုင်သည်။ ယခင် plan ထဲတွင် high-risk action hint ပါနိုင်သည်။ Current user intent နှင့်မတူနိုင်သည်။ ထို့ကြောင့် public book အတွက်အသေးစိတ် action plan ကိုဖယ်ထားသည်။ သင်ယူရမည့်အရာမှာ RAG planning ကို “အကြံပေးစာရွက်” အဖြစ်သာထားရန်ဖြစ်သည်။ Current page verifier, permission boundary, HITL gate, output sanitizer မပါလျှင် အတိတ်အောင်မြင်မှုသည်လက်ရှိအန္တရာယ်ဖြစ်နိုင်သည်။

### State discipline — `thread_id`, Checkpointer, Store

BrowserSurfer တွင် caller က `thread_id` ပေးနိုင်သည်။ Source ထဲတွင် `config = {"configurable": {"thread_id": thread_id}}` ဟူသောပုံစံဖြင့် LangGraph runtime ထဲသို့ထည့်သည်။ Beginner အတွက် `thread_id` သည် “conversation အတွက်စာအုပ်အမှတ်” ဖြစ်သည်။ Same thread id သည်တူညီသောစာအုပ်ကိုဆက်ရေးခြင်းဖြစ်နိုင်သည်။ Different thread id သည်စာအုပ်အသစ်ဖြစ်သင့်သည်။

`MemorySaver` သည် conversation state ကို checkpoint လုပ်ပေးသည်။ Tool result, model messages, execution lineage များကို thread အလိုက်ပြန်ယူနိုင်စေသည်။ ဤသည် restart-proof database memory မဟုတ်နိုင်သော်လည်း graph execution အတွက်အရေးကြီးသော persistence ဖြစ်သည်။

`InMemoryStore` သည် structured context storage အဖြစ်သုံးနိုင်သည်။ သို့သော်အမည်အတိုင်း memory ထဲတွင်ရှိသော store ဖြစ်သည်။ Durable production memory ဟုမယူသင့်ချေ။ CHAPTER-7.md တွင်ပြောထားသကဲ့သို့ checkpointer နှင့် store သည်တူသောအရာမဟုတ်။ Checkpointer သည် graph conversation lineage ကိုဆောင်သည်။ Store သည် context storage surface ဖြစ်နိုင်သည်။

အရေးကြီးသောအန္တရာယ်တစ်ခုမှာ browser session နှင့် graph thread state မတူခြင်းဖြစ်သည်။ `thread_id` ခွဲထားသည်ဆိုရုံဖြင့် browser page/session သည်အလိုအလျောက်ခွဲသွားသည်ဟုမယူသင့်ချေ။ Security analysis report တွင် shared/global browser session risk ကိုအထူးသတိပေးထားသည်။ Graph state ခွဲထားသော်လည်း browser session မခွဲထားလျှင် “စာအုပ်နှစ်အုပ်ရှိသော်လည်းတံခါးတစ်ခုပဲရှိ” သလိုဖြစ်နိုင်သည်။

Reader အနေဖြင့် repo ကိုဖတ်ရာတွင်မေးပါ။

- Default `thread_id` သည်ဘာလဲ။
- User တစ်ယောက်နှင့် task တစ်ခုအတွက် thread id ကိုဘယ်လိုတည်ဆောက်မလဲ။
- Browser session သည် per-thread လား၊ global လား။
- Checkpointer state နှင့် browser page state မညီလျှင်ဘာဖြစ်မလဲ။
- HITL resume လုပ်သောအခါ thread id မှားသွားလျှင်ဘာ session ကိုဆက်မလဲ။

### ToolRegistry — လက်နက်တိုက်စာရင်း

`src/tools/registry.py` သည် BrowserSurfer ၏အရေးကြီးသောအင်ဂျင်နီယာသင်ခန်းစာဖြစ်သည်။ Tools များကိုစာရင်းမဲ့ပေးထားခြင်းမဟုတ်။ `ToolSpec` ဖြင့် name, category, description, function, args schema တို့ကိုသတ်မှတ်သည်။ ထို့နောက် `to_langchain_tool()` က LangChain `StructuredTool` အဖြစ်ပြောင်းသည်။ Function သည် async ဖြစ်ပါက coroutine အဖြစ်ချိတ်သည်။ Pydantic schema သည် argument shape ကိုစစ်ပေးသည်။

လူသုံးစကားဖြင့်ဆိုလျှင် ToolRegistry သည်လက်နက်တိုက်စာရင်းဖြစ်သည်။ ToolSpec သည်လက်နက်တစ်ခု၏ကတ်ပြားဖြစ်သည်။ “နာမည်ဘာလဲ၊ ဘယ်အမျိုးအစားလဲ၊ ဘာလုပ်တတ်လဲ၊ ဘယ် input လက်ခံလဲ” ဟုရေးထားသည်။ Browser tool များတွင် navigation, interaction, forms, utilities, browser, vision စသော category များရှိနိုင်သည်။

ဤ design ၏အားသာချက်မှာ tool အသစ်ထည့်ရာတွင် orchestration logic ကိုတစ်ခါတည်းမဖျက်ရခြင်းဖြစ်သည်။ Tool list ကို capability inventory အဖြစ်မြင်နိုင်သည်။ Tool schema များကိုစစ်နိုင်သည်။ Callback နှင့် metrics layer တွင် tool name များကိုဖမ်းနိုင်သည်။

သို့သော် ToolRegistry သည် permission broker အပြည့်မဟုတ်။ Pydantic schema သည် argument type ကိုစစ်နိုင်သည်။ ဒါပေမဲ့ “ဤ tool ကိုဤ user task တွင် run ခွင့်ရှိသလား” ကိုမဖြေ။ `browser_evaluate` ထဲသို့ဘယ် JavaScript အမျိုးအစားခွင့်ပြုမလဲကို registry name တစ်ခုတည်းဖြင့်မသိနိုင်။ ထို့ကြောင့် registry သည်လက်နက်စာရင်းဖြစ်ပြီး၊ လက်နက်စောင့်မဟုတ်သေး။ Approval gate, allowlist, sanitizer, audit log, mutation scope တို့နှင့်တွဲမှ tool broker ဖြစ်လာသည်။

### Snapshot နှင့် Ref — Browser agent ၏မျက်စိ

BrowserSurfer ၏ browser tools ထဲတွင် snapshot/ref system သည်အလွန်အရေးကြီးသည်။ `browser_get_snapshot()` သည် page ၏ accessibility tree ကို YAML-like text အဖြစ်ပြန်ပေးနိုင်သည်။ Element တစ်ခုစီတွင် `ref` ရှိနိုင်သည်။ Agent သည်ထို ref ကိုသုံးပြီး tool call တစ်ခုခေါ်နိုင်သည်။

ဤ design သည်လူ့မျက်စိကိုစက်မျက်စိဖြင့်အစားထိုးခြင်းဖြစ်သည်။ လူက “အပြာရောင် button” ကိုမြင်သကဲ့သို့ Agent က `button "Post" [ref=e50]` စသောစာသားကိုမြင်သည်။ သို့သော် ref များသည်အမြဲတည်နေသောအိမ်နံပါတ်မဟုတ်။ Page ပြောင်းလျှင် ref များ stale ဖြစ်နိုင်သည်။ Dialog ဖွင့်လျှင် ref အဟောင်းသည် element အသစ်ကိုညွှန်နိုင်သည်။ ထို့ကြောင့် source prompt ထဲတွင် “action ပြီးတိုင်း fresh snapshot ယူ” ဆိုသောစည်းကမ်းပါသည်။

ဤနေရာတွင် beginner များအတွက်သင်ခန်းစာကြီးရှိသည်။ Browser agent မှားသွားခြင်းသည် model “မတော်” သောကြောင့်သာမဟုတ်။ Snapshot stale ဖြစ်သောကြောင့်ဖြစ်နိုင်သည်။ Ref မမှန်သောကြောင့်ဖြစ်နိုင်သည်။ Page content ကို instruction အဖြစ်မှားယူသောကြောင့်ဖြစ်နိုင်သည်။ Tool result ကို untrusted data အဖြစ်မပတ်သောကြောင့်ဖြစ်နိုင်သည်။

### Tool output wrapper — အကာအကွယ်အိတ်၊ အာမခံမဟုတ်

`src/tools/security.py` တွင် `wrap_untrusted` နှင့် `wrap_and_check` pattern များကိုတွေ့ရသည်။ `wrap_untrusted` သည် content ကို boundary marker များဖြင့်ပတ်သည်။ အဓိပ္ပာယ်မှာ “ဤစာသည် external data ဖြစ်သည်၊ instruction မဟုတ်” ဟု model ကိုသတိပေးခြင်းဖြစ်သည်။ `wrap_and_check` သည် suspicious injection pattern ရှိမရှိစစ်ပြီး sanitize လုပ်နိုင်သည်။

`src/tools/utilities.py` ထဲတွင် snapshot, JavaScript result, network data, console data, post data စသော tool outputs အချို့ကို `wrap_and_check` ဖြင့်ပတ်ထားသည်ကိုတွေ့ရသည်။ ဤသည်ကောင်းသောတိုးတက်မှုဖြစ်သည်။ သို့သော် wrapper သည်အာမခံချက်မဟုတ်။ အဆိပ်စာရွက်ကိုအိတ်ထဲထည့်ပြီး “မစားရ” ဟုရေးထားခြင်းနှင့်တူသည်။ အိတ်ရှိခြင်းကအဆိပ်ပျောက်သွားခြင်းမဟုတ်။

ထို့ကြောင့် wrapper ကို sanitizer, permission broker, HITL approval, session isolation, audit log, verifier တို့နှင့်တွဲရသည်။ “Tool output ကို wrapper ထည့်ထားပြီ၊ အားလုံးလုံခြုံပြီ” ဆိုသောအတွေးသည် browser agent တွင်အန္တရာယ်ရှိသည်။

### PlanningAgent — အတိတ်လမ်းကြောင်းမှ အကြံပေးသူ

`src/agents/planner.py` ထဲမှ `PlanningAgent` သည် RAG-based workflow planning ကိုလုပ်သည်။ Current task ကိုယူသည်။ Qdrant ထဲမှ similar trajectories များကိုရှာသည်။ Score နှင့် similarity threshold များဖြင့် filter လုပ်သည်။ Failed patterns များကို deprioritize လုပ်ရန်စဉ်းစားထားသည်။ ထို့နောက် planning model ကိုခေါ်ပြီး structured plan ထုတ်သည်။

ဒီ design ကို Strategy pattern အဖြစ်မြင်နိုင်သည်။ Planning ပိတ်ထားလျှင် Agent သည် normal execution ဖြင့်သွားသည်။ Planning ဖွင့်ထားလျှင် Agent သည် task မစမီ “အရင်ကဒီလိုအလုပ်မျိုးဘယ်လိုလုပ်ခဲ့သလဲ” ဟုမေးသည်။ အတိတ်ခြေရာတစ်ခုတွေ့လျှင် success plan ကို task ထဲသို့ inject လုပ်သည်။

လူ့ဥပမာဖြင့်ဆိုလျှင် လက်သမားတစ်ယောက်သည်အိမ်အသစ်မဆောက်ခင် အရင်အိမ်ဆောက်ခဲ့သောမှတ်တမ်းစာအုပ်ကိုဖတ်ခြင်းဖြစ်သည်။ ထိုမှတ်တမ်းစာအုပ်က “ဒီလိုတိုင်ကိုဒီလိုထောင်ခဲ့တာအဆင်ပြေတယ်” ဟုကူညီနိုင်သည်။ သို့သော်အိမ်အသစ်၏မြေပြင်၊ ရာသီဥတု၊ သစ်သားအမျိုးအစားကွဲနိုင်သည်။ အရင်မှတ်တမ်းကိုကူးချလျှင်အိမ်ပြိုနိုင်သည်။

Browser agent တွင်ဤအန္တရာယ်ပိုကြီးသည်။ အရင် trajectory ထဲမှ selector/ref များသည် stale ဖြစ်နိုင်သည်။ အရင် page layout သည်ပြောင်းသွားနိုင်သည်။ အရင် task သည် privacy-sensitive ဖြစ်နိုင်သည်။ အရင် plan ထဲတွင် high-risk action ပါနိုင်သည်။ ထို့ကြောင့် PlanningAgent output ကို “အကြံပေးစာရွက်” အဖြစ်သာယူရသည်။ Current page snapshot, permission policy, verifier တို့ဖြင့်ပြန်စစ်ရသည်။

### TrajectoryCallbackHandler — ဘာတွေဖြစ်သွားသလဲ မှတ်တမ်းရေးသူ

Agent တစ်ခုအလုပ်လုပ်နေစဉ် final answer တစ်ကြောင်းကိုသာကြည့်လျှင်ဘာဖြစ်ခဲ့သလဲမသိနိုင်။ BrowserSurfer တွင် `TrajectoryCallbackHandler` သည် Observer pattern အဖြစ် tool call events များကိုဖမ်းသည်။ Tool start, tool end, latency, status, output, token usage စသောအရာများကိုမှတ်သည်။ Empty/useless result များကိုစစ်သည်။ Same tool streak ကိုစစ်သည်။ Identical tool calls ထပ်ခါထပ်ခါဖြစ်လျှင် loop detection အဖြစ် abort လုပ်နိုင်သည်။

ဤ design သည်အရေးကြီးသည်။ Browser agent သည်တစ်ခါတစ်ရံ selector မတွေ့ဘဲတူညီသော tool ကိုထပ်ခါထပ်ခါခေါ်နိုင်သည်။ Model သည် “တစ်ခါထပ်စမ်းကြည့်ရင်ရမယ်” ဟုမူးသွားနိုင်သည်။ Callback observer မရှိလျှင် runtime သည်ထိုမူးယစ်မှုကိုမမြင်နိုင်။ Observer သည်အလုပ်သမား၏နောက်တွင်လမ်းကြောင်းမှတ်သောမှတ်တမ်းရေးသူဖြစ်သည်။

သို့သော် observer သည် policy enforcer အပြည့်မဟုတ်။ ၎င်းသည်မြင်သည်။ အချို့နေရာတွင် abort လုပ်နိုင်သည်။ သို့သော် tool permission, session isolation, output sanitization တို့ကိုအစားထိုးမထားနိုင်။ Observability သည် safety ၏အစိတ်အပိုင်းဖြစ်သည်။ Safety အားလုံးမဟုတ်။

### MetricsMiddleware, Reflection, Qdrant — အတွေ့အကြုံကိုသိမ်းသည့်စက်

Execution ပြီးသောအခါ `MetricsMiddleware` သည် callback မှ trajectory ကိုယူသည်။ Tool success, latency, token usage စသည့် metrics ကိုကြည့်ပြီး score တွက်သည်။ Store လုပ်သင့်/မသင့်စစ်သည်။ Trajectory summary လုပ်သည်။ PII redaction လုပ်သည်။ ReflectionAgent ရှိလျှင် “ဘာကောင်းခဲ့သလဲ၊ ဘာမှားခဲ့သလဲ” ဟုခွဲစိတ်စေသည်။ ထို့နောက် Qdrant ထဲသို့ trajectory ကိုသိမ်းနိုင်သည်။

ဤသည် BrowserSurfer ၏ self-learning loop ဖြစ်သည်။

```text
Plan
  -> Execute
  -> Observe
  -> Score
  -> Redact
  -> Reflect
  -> Store in Qdrant
  -> Reuse in next planning
```

ဤ loop သည်စိတ်ဝင်စားစရာကောင်းသည်။ သို့သော်အန္တရာယ်လည်းရှိသည်။ Bad trajectory ကို good trajectory အဖြစ်သိမ်းမိလျှင်နောက် run များကိုလမ်းမှားသွားစေမည်။ PII redaction မလုံလောက်လျှင် vector store သည်အတွေ့အကြုံဘဏ်မဟုတ်တော့ဘဲ privacy risk ဖြစ်သွားမည်။ ReflectionAgent ၏ critique သည် truth မဟုတ်။ Evidence-linked hypothesis ဖြစ်ရမည်။

### SkillsMiddleware — Domain စာအုပ်ကို context ထဲထည့်ခြင်း

`FacebookSurferAgent` သည် `SkillsMiddleware` ကိုသုံးသည်။ FilesystemBackend မှ skill files များကိုဖတ်ပြီး runtime context ထဲသင့်တော်သလိုထည့်နိုင်သည်။ Beginner အတွက် skill သည် “အလုပ်ရုံထဲကလုပ်နည်းစာအုပ်” ဖြစ်သည်။ BrowserSurfer တွင် domain-specific guidance, UI quirks, ref refresh rule, verification checkpoint, avoid pattern စသည်တို့ကို skill/prompt context အဖြစ်ပေးနိုင်သည်။

သို့သော် skill သည်လည်းအာဏာရှိသောစာဖြစ်သည်။ Skill source ကိုမယုံကြည်ရလျှင် Agent သည်မှားသောလမ်းညွှန်ကိုလိုက်နိုင်သည်။ Skill loading path, skill trust boundary, versioning, signing, review process တို့ကိုမစဉ်းစားလျှင် “လုပ်နည်းစာအုပ်” သည်အန္တရာယ်ရှိသောအမိန့်စာဖြစ်သွားနိုင်သည်။

### HITL — checkbox မဟုတ်၊ operational gate

Source ထဲတွင် `enable_hitl` သည် default false ဖြစ်သည်ဟုတွေ့ရသည်။ ဖွင့်ထားလျှင် high-risk tools အချို့အတွက် `interrupt_on` config ထည့်ထားသည်။ ဥပမာ navigation, form submission, browser close, browser evaluate စသည့် tool များကို approve/edit/reject decision လိုသောအရာများအဖြစ်သတ်မှတ်နိုင်သည်။

ဤ design သည်လမ်းမှန်ဖြစ်သည်။ သို့သော် HITL config ရှိခြင်းသည် HITL enforce ဖြစ်ခြင်းမဟုတ်။ User-facing approval UI ရှိသလား။ Reject လုပ်လျှင် tool မပြေးဘဲရပ်သလား။ Approval မရလျှင် fail-closed ဖြစ်သလား။ Thread resume မှန်သလား။ Audit log ထဲတွင် approval decision သိမ်းသလား။ ဤမေးခွန်းများမဖြေဘဲ “HITL ပါတယ်” ဟုမပြောသင့်။

Browser tool တွင် human approval သည်အလှဆင်မဟုတ်။ တံခါးသော့ဖြစ်သည်။

### Security analysis ကို ဘာကြောင့်အဓိကဖတ်ရသလဲ

BrowserSurfer ၏ security analysis report သည်ဤ chapter ၏အရေးကြီးဆုံးစာရွက်များထဲမှတစ်ခုဖြစ်သည်။ အကြောင်းမှာ browser agent ၏အန္တရာယ်သည် theoretical မဟုတ်။ Architecture ထဲတွင်တိုက်ရိုက်ရှိနေသောအရာများဖြစ်သည်။

**Indirect prompt injection**  
Page content, aria label, button name, console message, network response ထဲမှ instruction-like text သည် model ကိုလမ်းလွဲစေနိုင်သည်။ Page ထဲကစာသည် trusted instruction မဟုတ်။

**Raw snapshot ingestion**  
Accessibility snapshot သည် model context ထဲဝင်နိုင်သည်။ Wrapper ရှိသော်လည်း guarantee မဟုတ်။ Snapshot ကို data အဖြစ်ခွဲမဖတ်နိုင်လျှင် Agent သည် page ထဲကလှည့်စားစာကိုလိုက်နိုင်သည်။

**Shared browser session**  
Tool calls များသည် same browser page/context/session ကိုမျှဝေနိုင်သည်။ One tool action သည်နောက် tool action ၏မြေပြင်ကိုပြောင်းနိုင်သည်။

**High-risk browser evaluation**  
JavaScript evaluation tool သည်အထူးအန္တရာယ်ကြီးသည်။ Default-deny, allowlist, approval gate, output wrapper, audit log မပါဘဲလွှတ်မထားသင့်။

**HITL incomplete risk**  
Approval concept ရှိသည်ဆိုရုံမလုံလောက်။ Operationally enforced ဖြစ်ရမည်။

**Memory and trajectory privacy**  
Tool output, user text, page content, trajectory summary များထဲတွင် sensitive data ပါနိုင်သည်။ Qdrant သို့မသိမ်းမီ redaction နှင့် storage policy လိုသည်။

### ဘာကောင်းသလဲ၊ ဘာကိုပြင်ရမလဲ

BrowserSurfer repo ထဲတွင်ကောင်းသောသင်ခန်းစာများရှိသည်။

- DeepAgents ကိုသုံးပြီး LangGraph-style runtime complexity ကို facade အောက်တွင်ဖုံးထားသည်။
- ToolRegistry/ToolSpec/Pydantic schema ဖြင့် tool inventory ကိုစနစ်တကျထားသည်။
- `thread_id`, MemorySaver, optional InMemoryStore ဖြင့် state surface ကိုမြင်အောင်ထားသည်။
- PlanningAgent + Qdrant ဖြင့် similar trajectory reuse စမ်းထားသည်။
- TrajectoryCallbackHandler ဖြင့် tool execution ကို observer pattern အဖြစ်ဖမ်းသည်။
- MetricsMiddleware, scoring, PII redaction, ReflectionAgent, Qdrant storage ဖြင့် learning loop တည်ဆောက်ရန်ကြိုးစားထားသည်။
- `wrap_untrusted` / `wrap_and_check` ကဲ့သို့ output boundary pattern များရှိသည်။

သို့သော် reader သည်ဤ repo ကိုအောင်ပွဲကြေညာချက်အဖြစ်မဖတ်သင့်။ Hardening exercise အဖြစ်ဖတ်ရမည်။

ပြန်စဉ်းစားရန်လိုသောအချက်များမှာ -

1. `thread_id` နှင့် browser session isolation ကိုအတူစစ်ပါ။
2. High-risk browser tools ကို default-deny / approval-gated လုပ်ပါ။
3. `browser_evaluate` equivalent tool များကို allowlist နှင့် strict review မပါဘဲမဖွင့်ပါနှင့်။
4. Snapshot output ကို untrusted data အဖြစ်ပတ်ထားသော်လည်း verifier ဖြင့်ပြန်စစ်ပါ။
5. ToolRegistry ကို permission broker နှင့် audit log ဖြင့်တိုးချဲ့ပါ။
6. HITL ကို config checkbox မထားဘဲ fail-closed operational gate လုပ်ပါ။
7. Qdrant storage မတိုင်မီ PII redaction tests များတိုးချဲ့ပါ။
8. PlanningAgent output ကို current page verifier ဖြင့်စစ်ပြီး stale selector/ref မသုံးမိစေရ။
9. ReflectionAgent output ကို evidence-linked ဖြစ်မှ memory ထဲသိမ်းပါ။
10. Raw platform screenshots, private content, operational action traces များကို public docs ထဲမထည့်ပါနှင့်။

### Local-only လုံခြုံရေးစမ်းသပ်ခန်း

ဤ lab သည် real platform ပေါ်တွင်မလုပ်သင့်ချေ။ Local static HTML file ဖြင့်သာလုပ်ပါ။

1. `local_test.html` တစ်ခုရေးပါ။
2. Normal text, button, fake form ထည့်ပါ။
3. Page ထဲတွင် “previous instruction မလိုက်နာရန်” ဆိုသော harmless injection-like sentence ထည့်ပါ။
4. Snapshot tool result ကို wrapper မပါဘဲ model context ထဲထည့်သော version နှင့် wrapper ပါသော version နှိုင်းပါ။
5. Click tool ကို dummy button တစ်ခုတည်းတွင်သာခွင့်ပြုပါ။
6. JavaScript evaluate tool ကိုပိတ်ထားပါ။
7. Tool trace ထဲတွင် action, source, wrapper status, approval status, final verifier result သိမ်းပါ။
8. Final answer မထုတ်မီ “page content သည် data ဖြစ်သည်၊ instruction မဟုတ်” ဟု verifier စစ်ပါ။

ဤ lab ၏ရည်ရွယ်ချက်မှာ browser agent safety ကိုနားလည်ရန်ဖြစ်သည်။ Platform automation သင်ရန်မဟုတ်။

### နိဂုံး — Browser Agent ကို ခွဲစိတ်၍ဖတ်ပါ

BrowserSurfer Bot သည် browser tool agent architecture ကိုဖတ်ရန်ကောင်းသော case study ဖြစ်သည်။ ၎င်း၏အနှစ်သာရမှာ “browser ကို Agent လက်ထဲပေးနိုင်တယ်” ဟုအံ့ဩသွားရန်မဟုတ်။ Browser ကိုလက်ထဲပေးလိုက်သောအခါ facade, DeepAgents runtime, graph thinking, thread state, checkpointer, store, ToolRegistry, Playwright session, snapshot/ref system, wrapper, HITL, trajectory observer, metrics, reflection, Qdrant memory တို့အားလုံးတစ်ပြိုင်နက်စဉ်းစားရခြင်းဖြစ်သည်။

အန္တရာယ်မြင်သော engineer မျက်စိဖြင့်ဖတ်ပါ။ Page content ကိုမယုံပါနှင့်။ Tool output ကိုမယုံပါနှင့်။ အတိတ် trajectory ကိုဗျာဒိတ်တော်မလုပ်ပါနှင့်။ Shared session ကိုလွယ်လွယ်မသုံးပါနှင့်။ Human approval ကို checkbox မထားပါနှင့်။ Browser agent သည် demo အတွက်လှသော်လည်း၊ boundary မရှိလျှင်အန္တရာယ်သည် code ထဲကနေတန်းထွက်လာသည်။

---

**စာဖတ်သူအတွက် Source Notes:**

- **GitHub source:** `https://github.com/htooayelwinict/bot`
- **ဖတ်ထားသော source map:** `docs/system-architecture.md`, `docs/security_analysis_report.md`, `docs/codebase-summary.md`, `docs/studyGuide.md`, `src/agents/facebook_surfer.py`, `src/agents/planner.py`, `src/tools/registry.py`, `src/tools/security.py`, `src/tools/utilities.py`, `src/metrics/trajectory_callback.py`, `src/metrics/middleware.py`, `src/metrics/scoring.py`, `src/metrics/pii_redaction.py`, `src/storage/trajectory_store.py`, `src/storage/retrieval.py`, `src/agents/reflection.py`, `src/session/__init__.py`
- **နာမည်သတ်မှတ်ချက်:** `FacebookSurfer` သည် repo အတွင်း internal codename ဖြစ်သည်။ Public chapter name သည် BrowserSurfer Bot ဖြစ်သည်။
- **အဓိက lesson:** Browser agent တွင် state boundary, tool permission, output wrapping, session isolation, HITL enforcement, trajectory privacy, current-state verification တို့ကိုတပြိုင်နက်စဉ်းစားရသည်။
- **Safety boundary:** ဤအခန်းသည် educational architecture အတွက်သာဖြစ်သည်။ အန္တရာယ်ရှိသော platform-misuse guidance မပေးပါ။

