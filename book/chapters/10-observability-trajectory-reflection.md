# ၁၀။ ခြေရာခံမှတ်တမ်းနှင့် ပြန်လည်ဆင်ခြင်ခြင်း

### စာရေးတော်မှားသောအခါ ဘယ်ခြေရာကိုကြည့်မလဲ

လူတစ်ယောက်အမှားလုပ်လျှင် "သူမှားသွားသည်" ဟုသာပြောခြင်းဖြင့်အလုပ်မပြီး။ ဘယ်အဆင့်တွင်မှားသနည်း။ အမိန့်ကိုနားလည်မှုမှားသလား။ ကိရိယာမှားသုံးသလား။ ရလဒ်ကိုမဖတ်ဘဲအဖြေထုတ်သလား။ အလုပ်ပြီးသွားပြီဟုထင်သော်လည်းအမှန်တွင် data မရသေးသလား။ ထိုမေးခွန်းများကိုမဖြေနိုင်လျှင် နောက်တစ်ကြိမ်လည်းအတူတူမှားမည်။

Agentic AI တွင်ဤပြဿနာပိုကြီးသည်။ Agent တစ်ခုသည်လူနှင့်စကားပြောသည်။ Planner output ထုတ်သည်။ Tool ခေါ်သည်။ Tool result ဖတ်သည်။ Replan လုပ်သည်။ Memory သုံးသည်။ Final answer ရေးသည်။ ထိုအဆင့်များထဲမှတစ်ခုခုမှားနိုင်သည်။ Final answer တစ်ခုတည်းကြည့်လျှင် အမှား၏အရင်းအမြစ်မမြင်နိုင်။

ထို့ကြောင့် **Observability** လိုသည်။ Observability ဆိုသည်မှာ log ရိုက်ထားခြင်းသက်သက်မဟုတ်။ System အတွင်းဘာဖြစ်သွားသည်ကို နောက်မှအထောက်အထားဖြင့်ပြန်ကြည့်နိုင်အောင်တည်ဆောက်ခြင်းဖြစ်သည်။

### Trajectory — စာရေးတော်ဖြတ်သန်းသွားသောလမ်း

Trajectory ဆိုသည်မှာ Agent တစ်ခု task တစ်ခုလုပ်စဉ် ဖြတ်သန်းသွားသောလမ်းကြောင်းဖြစ်သည်။

```text
User goal
  -> planner output
  -> model action
  -> tool call
  -> tool result
  -> policy signal
  -> replan / stop / continue
  -> final answer
  -> verifier result
```

ဤလမ်းကြောင်းကိုမြင်မှ debugging လုပ်နိုင်သည်။ Model က tool မှားရွေးသလား။ Tool result empty ဖြစ်သော်လည်း model ကသေချာဟန်ဖြင့်အဖြေထုတ်သလား။ Same tool ကိုထပ်ခါထပ်ခါခေါ်သလား။ Browser page ထဲမှ untrusted text ကို instruction အဖြစ်လိုက်သလား။ Replan ဖြစ်သင့်သည့်နေရာတွင် finalize ဖြစ်သလား။ Trajectory သည်ဤမေးခွန်းများကိုဖြေရန်အခြေခံစာရွက်စာတမ်းဖြစ်သည်။

Agent တစ်ခုတွင် final answer သာသိမ်းထားခြင်းသည် လူတစ်ယောက်သွားခဲ့သောခရီးစဉ်အတွက်နောက်ဆုံးဓာတ်ပုံတစ်ပုံသာသိမ်းထားခြင်းနှင့်တူသည်။ ချိုင့်ထဲဘယ်နေရာမှာကျသလဲသိချင်လျှင်လမ်းကြောင်းလိုသည်။

အမှားတစ်ခုကိုမြင်ကြည့်ပါ။ Agent ကို "ဒီ page ထဲက contact email ရှာပါ" ဟုခိုင်းသည်။ Agent က browser snapshot ဖတ်သည်။ Email မတွေ့။ ထို့နောက် search tool ကိုခေါ်သည်။ Search result empty ဖြစ်သည်။ သို့သော် final answer တွင် "contact@example.com ဖြစ်နိုင်သည်" ဟုခန့်မှန်းဖြေလိုက်သည်။ Final answer တစ်ခုတည်းကြည့်လျှင် "မှားဖြေတယ်" ဟုသာသိမည်။ Trajectory ကိုကြည့်လျှင် empty result နှစ်ကြိမ်ရပြီးနောက် hallucination ဖြစ်သွားကြောင်းမြင်မည်။ ထိုအခါ fix သည် prompt ပြင်ခြင်းသာမဟုတ်တော့။ Empty-result policy, verifier, stop condition ထည့်ရန်ဖြစ်လာသည်။

### BrowserSurfer ထဲက ခြေရာခံစနစ်

BrowserSurfer Bot သည် browser tool agent ဖြစ်သောကြောင့် trajectory အလွန်အရေးကြီးသည်။ Browser tool သည် real page ကိုမြင်နိုင်သည်။ Click လုပ်နိုင်သည်။ Navigation side effect ရှိနိုင်သည်။ ထို့ကြောင့် "အဖြေထုတ်နိုင်သလား" ထက် "အလုပ်လုပ်စဉ်ဘာတွေထိသွားသလဲ" ကိုမြင်ရမည်။

Repo ထဲတွင် `TrajectoryCallbackHandler` သည် LangChain callback အဖြစ် tool start, tool end, tool error များကိုဖမ်းနိုင်သောနေရာဖြစ်သည်။ Tool latency, result length, empty result, repeated tool input, same tool streak စသည်တို့ကို signal အဖြစ်မြင်နိုင်သည်။ Metrics layer သည် trajectory ကို score လုပ်ရန်ကြိုးစားသည်။ Tool success, latency, token usage, outcome စသည်တို့ကိုတွက်နိုင်သည်။

ထိုမှတစ်ဆင့် PII redaction လုပ်ပြီး Qdrant ထဲသို့ trajectory သိမ်းနိုင်သည်။ ReflectionAgent သည် run ပြီးနောက် "ဘာကောင်းခဲ့သလဲ၊ ဘာမှားခဲ့သလဲ၊ နောက်တစ်ကြိမ်ဘာသတိထားရမလဲ" ဟု critique ထုတ်နိုင်သည်။ PlanningAgent သည်နောက်ပိုင်း task များတွင် similar successful trajectories ကိုပြန်ရှာနိုင်သည်။

ဤအတွေးသည်လှပသည်။ သို့သော်အန္တရာယ်လည်းရှိသည်။

Score မှားလျှင် failed trajectory ကို success pattern အဖြစ်သိမ်းမိနိုင်သည်။

Redaction မလုံလောက်လျှင် sensitive data ကို memory ထဲသိမ်းမိနိုင်သည်။

ReflectionAgent output သည်အထောက်အထားမရှိသောအကြံဖြစ်နိုင်သည်။

Past trajectory သည် current task အတွက်အမြဲမမှန်နိုင်။

Browser selector နှင့် page structure သည်အချိန်နှင့်ပြောင်းနိုင်သည်။

ထို့ကြောင့် trajectory reuse သည်အတိတ်အတွေ့အကြုံကိုပြန်ဖတ်ခြင်းဖြစ်သည်။ ဗေဒင်ဟောခြင်းမဟုတ်။

### Travis-2 ထဲက State သည် မှတ်တမ်းစာအုပ်လည်းဖြစ်သည်

Travis-2 တွင် observability သည် `AgentState` ထဲရှိ control fields များမှလည်းမြင်ရသည်။ Loop detected ဖြစ်သလား။ Loop reason ဘာလဲ။ Policy action က continue, replan, stop ဘာလဲ။ Replan count ဘယ်လောက်လဲ။ Recent trajectory ရှိသလား။ Telemetry ရှိသလား။ Budget snapshot ဘယ်လိုလဲ။

SemanticLoopDetectionMiddleware သည် same tool input streak, same tool streak, empty result streak များကိုဖမ်းနိုင်သည်။ ModelCallLimitMiddleware သည် model call budget ကိုထိန်းသည်။ Structured Playwright result တွင် `execution_ok` နှင့် `data_ok` ခွဲထားခြင်းသည် observability ၏ကောင်းသောဥပမာဖြစ်သည်။

Page ဖွင့်နိုင်သည်။ ထို့ကြောင့် `execution_ok=true` ဖြစ်နိုင်သည်။ သို့သော်လိုသော data မရလျှင် `data_ok=false` ဖြစ်ရမည်။ ထို့ကြောင့် task-level `ok` သည် `execution_ok and data_ok` ဖြစ်သင့်သည်။ "Tool မပျက်ဘူး" ဆိုသည်မှာ "အလုပ်အောင်မြင်တယ်" မဟုတ်။

ဤသင်ခန်းစာသည် browser tool အတွက်သာမဟုတ်။ API call တစ်ခု 200 OK ပြန်လည်း business task fail ဖြစ်နိုင်သည်။ Test command exit 0 ဖြစ်လည်း assertion မမှန်နိုင်သည်။ Agentic system တွင် signal များကိုအဆင့်ခွဲဖတ်တတ်ရန်လိုသည်။

### appv22 တွင် Test သည် Observability ဖြစ်လာသည်

appv22 သည် emerging runtime recovery lab ဖြစ်သည်။ ထို project ကို final worker kernel ဟုမခေါ်ရ။ သို့သော် runtime engineering အတွက်စိတ်ဝင်စားစရာကောင်းသောအချက်မှာ tests များက system behavior ကိုမြင်စေခြင်းဖြစ်သည်။

`test_no_appv21_coupling.py` က cross-repo coupling မရှိကြောင်းစစ်သည်။ `test_coding_agent.py` က coding-agent behavior ကိုစမ်းသည်။ `test_compaction_timing.py` ရှိလျှင် compaction timing ကိုစစ်နိုင်သည်။ Offline/faux provider tests များသည် real model API မလိုဘဲစမ်းရန်ထားသော provider အတုကိုသုံးခြင်းဖြစ်သည်။ ထိုကြောင့် loop, model-provider boundary, guardrail behavior ကို network/API key မလိုဘဲပြန်ပြန်စမ်းနိုင်သည်။

Agentic AI တွင် model output သည်ပြောင်းလဲနိုင်သည်။ ထို့ကြောင့် deterministic test harness သည်မြင်နိုင်ခြင်းတစ်မျိုးဖြစ်သည်။ "ဒီ runtime ကဘယ်အခြေအနေမှာဘာလုပ်သင့်သလဲ" ကို test ထဲတွင်အတိအကျဖမ်းထားခြင်းသည် observability ၏အရေးကြီးသောအပိုင်းဖြစ်သည်။

### Reflection ကို ဘယ်လောက်ယုံမလဲ

Reflection ဆိုသည်မှာ run ပြီးနောက်ပြန်လည်ဆင်ခြင်ခြင်းဖြစ်သည်။ Model-based ReflectionAgent တစ်ခုသည် trajectory ကိုဖတ်ပြီး successful patterns, failed patterns, future suggestions ထုတ်နိုင်သည်။ ဤအရာသည်အသုံးဝင်သည်။ သို့သော် reflection သည်အမှန်တရားမဟုတ်။ Hypothesis ဖြစ်သည်။

ကောင်းသော reflection သည် exact evidence ကိုညွှန်ပြသည်။

ဘယ် tool call မှာ fail ဖြစ်သလဲ။

ဘယ် result က empty ဖြစ်သလဲ။

ဘယ် policy signal က stop ခဲ့သလဲ။

ဘယ် source ကိုမဖတ်ခဲ့သလဲ။

ဘာကိုမသေချာသလဲ။

မကောင်းသော reflection သည်အလှပြောသက်သက်ဖြစ်သည်။ "Agent did well", "Need improve planning" စသည့်ယေဘုယျစကားများသည် debugging အတွက်အသုံးမဝင်။ Reflection ကို memory ထဲသိမ်းမည်ဆိုပါကပိုပြီးသတိထားရမည်။ Evidence မပါသော reflection သည်အနာဂတ် agent ကိုလမ်းမှားစေနိုင်သည်။

### Metrics သည် ဂဏန်းသေတ္တာမဟုတ်

Metrics များသည်အသုံးဝင်သည်။ သို့သော်ဂဏန်းသည်အမှန်တရားမဟုတ်။ မီးအိမ်တစ်လုံးကဲ့သို့လမ်းကိုအလင်းပေးနိုင်သော်လည်းလမ်းအစားမလျှောက်ပေးနိုင်။ Tool success rate မြင့်နိုင်သည်။ Task success နည်းနိုင်သည်။ Latency နည်းနိုင်သည်။ Verification မရှိသဖြင့်အမှားများနိုင်သည်။ Token usage နည်းနိုင်သည်။ Context မလုံလောက်နိုင်သည်။

Metrics ကိုဘုရင်မထားပါနှင့်။ Metrics ကိုအချက်ပြမီးအဖြစ်သုံးပါ။ Engineer ၏အလုပ်မှာထိုအချက်ပြမီးများကိုအဓိပ္ပာယ်ဖတ်ပြီး trajectory နှင့် evidence ထဲပြန်ဝင်စစ်ရန်ဖြစ်သည်။

ဥပမာ -

```text
tool_success_rate high
task_success_rate low
=> tool runs, but agent is solving wrong problem

latency low
verification_missing true
=> fast, but possibly careless

retrieval_count high
answer_grounding low
=> many documents, poor use of evidence
```

### Privacy မပါသော Observability သည် ပြဿနာအသစ်

"အကုန် log ထုတ်" သည် observability မဟုတ်။ ၎င်းသည် data leak ဖြစ်နိုင်သည်။ Trace log ထဲတွင် user input, browser content, tool output, file path, API response, error stack, email address, phone number, project secret pattern, browser session hint စသည်တို့ပါနိုင်သည်။

Safe observability တွင် raw data သိမ်းခြင်းထက် metadata သိမ်းခြင်းကိုဦးစားပေးရမည်။

```text
Bad:
  raw_tool_args: full user document
  raw_tool_result: full page content

Better:
  args_hash: 91fd...
  result_length: 1250
  execution_ok: true
  data_ok: false
  redaction_applied: true
```

BrowserSurfer တွင် PII redaction utility ရှိခြင်းသည်ကောင်းသောအစဖြစ်သည်။ သို့သော် pattern-based redaction သည်အမြဲမလုံလောက်။ Domain-specific secrets, screenshots, attachments, browser storage data တို့ကိုသီးခြားစဉ်းစားရမည်။

P-2 တွင်လည်း bridge crossing ကိုမြင်နိုင်ရန်လိုသည်။ သို့သော် trace ထဲတွင် secret fields မထည့်သင့်ချေ။ "Bridge crossed, origin verified, secret fields dropped" ကဲ့သို့ metadata သိမ်းခြင်းကပိုသင့်တော်သည်။

### Mini Lab — JSONL ခြေရာခံမှတ်တမ်းရေးပါ

Toy agent loop တစ်ခုတွင် JSONL trajectory log ထည့်ပါ။

```json
{
  "turn_id": "abc",
  "step": 1,
  "event": "tool_end",
  "tool": "search_docs",
  "args_hash": "91fd...",
  "execution_ok": true,
  "data_ok": false,
  "result_length": 0,
  "policy_action": "replan"
}
```

Raw args မသိမ်းပါနှင့်။ Long result အကုန်မသိမ်းပါနှင့်။ Result length, status, warning, redaction flag, policy action စသည်တို့ကိုသိမ်းပါ။ ထို့နောက် repeated tool+args detection ကို log မှပြန်တွက်ပါ။ Failed run တစ်ခုနှင့် successful run တစ်ခုကိုနှိုင်းပါ။

နောက်တစ်ဆင့်တွင် reflection function တစ်ခုရေးပါ။ Trajectory ကိုဖတ်ပြီး failure point, evidence, next action သုံးခုသာထုတ်ပါ။ Evidence မရှိသော reflection ကို reject လုပ်ပါ။ ဤလေ့ကျင့်ခန်းသည် agent debugging ကိုခံစားချက်မှအထောက်အထားသို့ပြောင်းစေသည်။

### နိဂုံး — အမှားကိုမြင်နိုင်ခြင်းသည် ဉာဏ်၏တစ်ဝက်

Observability သည် Agent ကိုမျက်စိတပ်ပေးခြင်းဖြစ်သည်။ Trajectory သည် Agent ဖြတ်သန်းသွားသောလမ်းကြောင်းဖြစ်သည်။ Reflection သည် run ပြီးနောက်သင်ခန်းစာထုတ်ခြင်းဖြစ်သည်။ Metrics သည် signal ဖြစ်သည်။ Test သည် behavior ကိုဖမ်းထားသောစာချုပ်ဖြစ်သည်။

သို့သော် trace, metric, reflection တို့ကိုလည်းမယုံကြည်လွန်းပါနှင့်။ ၎င်းတို့သည် privacy risk ဖြစ်နိုင်သည်။ Evidence မပါလျှင်လမ်းလွဲနိုင်သည်။ Session scope မခွဲလျှင် user တစ်ယောက်၏ခြေရာသည်အခြား user အတွက်အဆိပ်ဖြစ်နိုင်သည်။

အမှားကိုမြင်နိုင်သော Agent သည်ပြင်နိုင်သော Agent ဖြစ်သည်။ အမှားကိုမမြင်နိုင်သော Agent သည် လှပသော final answer များဖြင့်လမ်းလွဲနေသောစာရေးတော်သာဖြစ်သည်။

---
**စာဖတ်သူအတွက် Source Notes:**
- **Trajectory:** Ordered record of planning, model actions, tool calls, results, policy decisions, and final output.
- **BrowserSurfer:** `TrajectoryCallbackHandler`, scoring, PII redaction, Qdrant storage, ReflectionAgent, and PlanningAgent are observability anchors.
- **Travis-2:** Loop signals, `policy_action`, budget fields, and structured Playwright quality fields support debugging.
- **appv22:** Tests and faux/offline providers make runtime behavior inspectable without always requiring real model calls.
- **P-2:** Bridge observability should prefer metadata over secret-bearing raw traces.
