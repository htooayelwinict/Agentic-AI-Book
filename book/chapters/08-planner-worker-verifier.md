# ၀၈။ စီမံသူ၊ လုပ်သားနှင့် စစ်ဆေးသူ

### အလုပ်တစ်ခုကို လူတစ်ယောက်တည်း မအပ်သင့်သောအခါ

ရွာတစ်ရွာတွင်တံတားဆောက်မည်ဆိုပါစို့။ တံတားပုံဆွဲသူ၊ သံချောင်းဆွဲသူ၊ အုတ်သယ်သူ၊ အရည်အသွေးစစ်သူအားလုံးကိုလူတစ်ယောက်တည်းလုပ်ခိုင်းလျှင် ထိုသူအလွန်တော်သည်ဆိုသော်လည်းတံတားအောက်တွင်ကျွန်ုပ်တို့သွားရပ်သင့်မည်မဟုတ်။ အဘယ်ကြောင့်ဆိုသော်အလုပ်ကြီးတစ်ခုတွင် စီမံခြင်း၊ လုပ်ဆောင်ခြင်း၊ စစ်ဆေးခြင်းတို့သည်သဘာဝအားဖြင့်မတူသောစိတ်အလုပ်များဖြစ်သောကြောင့်ဖြစ်သည်။

Agentic AI တွင်လည်းထိုသဘောပင်။ Model တစ်ခုကို "စဉ်းစားပါ၊ tool သုံးပါ၊ code ရေးပါ၊ ပြန်စစ်ပါ၊ မှားလျှင်ပြင်ပါ၊ ပြီးပါကအောင်မြင်ကြောင်းကြေညာပါ" ဟုအားလုံးခိုင်းလိုက်လျှင် တစ်ခါတစ်ရံအလုပ်လုပ်နိုင်သည်။ သို့သော် အရေးကြီးသောအလုပ်များတွင် ထိုပုံစံသည်အလွန်လွယ်လွန်းသည်။ Model သည်မိမိလုပ်ခဲ့သောအမှားကိုမမြင်နိုင်တတ်။ မိမိရေးသောအဖြေကိုမိမိချစ်တတ်သည်။ လူသားလည်းထိုသို့ပင်။

ထို့ကြောင့် **Planner-Worker-Verifier** pattern ပေါ်လာသည်။ ဤ pattern သည် fancy multi-agent show မဟုတ်။ အလုပ်၏တာဝန်များကိုခွဲခြားပြီး တစ်ခုစီကိုပိုထိန်းချုပ်နိုင်အောင်လုပ်သော engineering pattern ဖြစ်သည်။

```text
Goal
  |
  v
Planner  -> plan, scope, fallback
  |
  v
Worker   -> execute bounded tasks with tools
  |
  v
Verifier -> test, inspect, reject or approve
  |
  +---- if failed, return to Planner/Worker
```

### Planner — စစ်မြေပုံဆွဲသူ

Planner ၏အလုပ်မှာ tool ကိုပထမဆုံးခေါ်ရန်မဟုတ်။ အလုပ်ကိုမည်သို့ခွဲမလဲဆုံးဖြတ်ရန်ဖြစ်သည်။ ကောင်းသော Planner သည် user request ကိုအပိုင်းပိုင်းခွဲသည်။ Scope ကိုသတ်မှတ်သည်။ မသေချာသောအရာများကိုမှတ်သည်။ Risk ရှိသောအပိုင်းကိုခွဲထုတ်သည်။ Test strategy ကိုစဉ်းစားသည်။

ဥပမာအားဖြင့် "book chapter 12 ကို P-2 repo အပေါ်အခြေခံပြီးရေးပါ" ဟုခိုင်းလျှင် Planner သည်ချက်ချင်းစာမရေးသင့်။ README, routing docs, runtime, states, nodes, classifier တို့ကိုဖတ်ရမည်ဟုဆုံးဖြတ်ရမည်။ ထို့နောက် core lesson ကိုရွေးရမည်။ Supervisor high privilege, Customer low privilege, Bridge projection boundary, GlobalState vs UnsafeState စသည်တို့ကိုအဓိကသင်ခန်းစာအဖြစ်ထားရမည်။ Code line အကုန်မထည့်သင့်ချေ။ Beginner အတွက် mental model ရေးရမည်။

Planner မကောင်းလျှင် Worker သည်တော်သော်လည်းအလုပ်လမ်းမှားသွားမည်။ စစ်မြေပုံမှားလျှင်ရဲဘော်များအားလုံးမှန်မှန်ချီတက်သော်လည်း တောင်ထဲဝင်သွားနိုင်သည်။

ကုဒ်မပါသောဥပမာတစ်ခုယူပါ။ ဆေးခန်းတစ်ခုတွင်လူနာတစ်ယောက်ဝင်လာသည်။ Planner သည် "ပထမဆုံးလက္ခဏာမေးမည်၊ အရေးပေါ်လက္ခဏာရှိ/မရှိခွဲမည်၊ လိုအပ်လျှင်ဆရာဝန်ထံပို့မည်" ဟုအစီအစဉ်ချသည်။ Worker သည်သွေးပေါင်တိုင်းသည်၊ အပူချိန်တိုင်းသည်၊ form ဖြည့်သည်။ Verifier သည် "အရေးပေါ်လက္ခဏာရှိလျှင် nurse ဆုံးဖြတ်ချက်ဖြင့်မပြီး၊ ဆရာဝန်ကိုခေါ်ရမည်" ဟုစစ်သည်။ ဤသုံးခုကိုလူတစ်ယောက်တည်းလုပ်နိုင်သော်လည်းတာဝန်ခွဲထားသောကြောင့်အမှားအချို့ကိုဖမ်းနိုင်သည်။

Planner ၏အရေးကြီးသော output များမှာ -

အလုပ်၏နယ်ပယ်။

လုပ်ရန်အဆင့်များ။

ရှောင်ရန်အရာများ။

လိုအပ်သော source များ။

Verifier စစ်ရမည့်အချက်များ။

Fallback plan။

Planner သည်အမြဲတမ်းအမှန်မဟုတ်။ Planner output ကိုလည်း untrusted advisory အဖြစ်ဖတ်ရမည်။ PlanningAgent သည်အကြံပေးသူဖြစ်သည်။ ဘုရင်မဟုတ်။

### Worker — လက်ထဲတွင် ကိရိယာကိုင်သူ

Worker သည်လုပ်ဆောင်သူဖြစ်သည်။ File ဖတ်သည်။ Code ရေးသည်။ Browser ဖွင့်သည်။ Database query လုပ်သည်။ Search လုပ်သည်။ Worker ၏အားသာချက်မှာ execution ဖြစ်သည်။ အားနည်းချက်မှာ scope creep ဖြစ်သည်။ Worker ကို "ဒီ folder ကိုသာဖတ်" ဟုမပြောလျှင် project တစ်ခုလုံးကိုဆွဲဖတ်သွားနိုင်သည်။ "write မလုပ်ပါနှင့်" ဟုမပြောလျှင်မလိုသောဖိုင်များပြင်သွားနိုင်သည်။

Worker ကိုကောင်းစွာသုံးရန် **အလုပ်စာချုပ်** (`task contract`) လိုသည်။ အလုပ်စာချုပ်ဆိုသည်မှာ Worker ကိုမလွှတ်ခင် "ဘာလုပ်ရမည်၊ ဘာမလုပ်သင့်၊ ဘယ်အထောက်အထားပြန်ပေးရမည်" ဟုရှင်းထားသောစာချုပ်ဖြစ်သည်။

```text
Input:
  - task
  - allowed files/tools
  - constraints

Output:
  - result
  - evidence
  - uncertainty
  - files changed, if any
```

Sub-agent များကို worker အဖြစ်သုံးရာတွင် P-2 သင်ခန်းစာသည်အရေးကြီးသည်။ Parent agent ၏ state အကုန်ကို worker ထံမပေးရ။ Worker task အတွက်လိုသော context သာပေးရမည်။ အလုပ်သမားကိုအုတ်သယ်ခိုင်းရာတွင်အိမ်ရှင်၏ဘဏ်စာရင်းအကုန်ပေးရန်မလိုသကဲ့သို့ဖြစ်သည်။

### Verifier — မယုံကြည်သော ဂိတ်စောင့်

Verifier ၏အလုပ်မှာ "အဖြေကလှသလား" မဟုတ်။ "အလုပ်ကတကယ်မှန်သလား" ဖြစ်သည်။ Agent world တွင်လှသောစာသားများသည်မကြာခဏမှားတတ်သည်။ Verifier သည် output ကို source နှင့်တိုက်သည်။ Test run လုပ်သည်။ Tool result ကိုစစ်သည်။ Missing edge case ကိုမေးသည်။ Safety rule မချိုးသလားကြည့်သည်။

Travis-2 ၏ evaluate/replan/finalize flow သည်ဤသဘောကိုကောင်းစွာပြသည်။ သို့သော် ထို graph ထဲမဝင်မီအရေးကြီးသောအလုပ်မှာ `run_playwright_code` မှပြန်လာသောစာရွက်ကိုအထောက်အထားအဖြစ်ဖတ်ခြင်းဖြစ်သည်။ Agent ရေးသော TypeScript Playwright script သည် run သွားနိုင်သည်။ သို့သော် `data_ok=false` ဖြစ်နိုင်သည်။ အလုပ်သမားသည်အလုပ်ရုံထဲဝင်သွားသည်ဆိုရုံနှင့် အလုပ်ပြီးပြီဟုမဆိုနိုင်။ ပြန်လာသောပစ္စည်းတွင်အသုံးဝင်သော data ပါသလားကိုကြည့်ရမည်။

Evaluate node က state ကိုကြည့်ပြီး `policy_action` ကိုဆုံးဖြတ်နိုင်သည်။ Continue လုပ်မလား၊ replan လုပ်မလား၊ stop လုပ်မလား။ ဤသည် Verifier thinking ကို tool result နှင့် graph flow နှစ်ခုလုံးထဲထည့်သွင်းခြင်းဖြစ်သည်။

BrowserSurfer တွင် TrajectoryCallbackHandler, scoring, ReflectionAgent တို့သည် Verifier/critic thinking ၏အစိတ်အပိုင်းများဖြစ်သည်။ Browser agent သည် page ကြည့်နိုင်သည်။ Form ဖြည့်နိုင်သည်။ Navigation side effect ရှိနိုင်သည်။ ထို့ကြောင့် "tool call successful" ဟုဆိုရုံဖြင့်မလုံလောက်။ Data useful ဖြစ်သလား၊ side effect ဖြစ်သွားသလား၊ untrusted page text ကို instruction အဖြစ်ယုံမိသလား စစ်ရမည်။

### Planner-Worker-Verifier ကို Graph ထဲသို့ ထည့်ခြင်း

Pattern ကိုစာရွက်ပေါ်တွင်နားလည်ရုံဖြင့်မလုံလောက်။ Runtime ထဲသို့ထည့်ရန်လိုသည်။ LangGraph ကဲ့သို့သော graph runtime တွင် node များကိုခွဲပြီး edge များဖြင့်လမ်းကြောင်းသတ်မှတ်နိုင်သည်။

```text
START
  -> plan
  -> run_worker
  -> evaluate
      -> finalize  (if ok)
      -> replan    (if insufficient)
      -> stop      (if unsafe or budget exhausted)
```

ဤ graph သည် model ကိုမသတ်ပစ်။ Model ၏လွတ်လပ်မှုကိုအလုပ်လုပ်နိုင်သည့်ဘောင်ထဲသို့ထည့်သည်။ Model သည် run_worker ထဲတွင် tool သုံးနိုင်သည်။ သို့သော် evaluate node သည်အလုပ်၏အခြေအနေကိုပြန်ကြည့်သည်။ Budget, loop, result quality, policy တို့ကိုစစ်သည်။

ဤနေရာတွင် beginner များမှားတတ်သည်မှာ Planner, Worker, Verifier အားလုံးကိုသီးခြား LLM agent အဖြစ်သာစဉ်းစားခြင်းဖြစ်သည်။ အမြဲမလိုပါ။ Planner သည် deterministic code ဖြစ်နိုင်သည်။ Worker သည် tool-enabled LLM ဖြစ်နိုင်သည်။ Verifier သည် unit test, schema validation, LLM critique, human review ပေါင်းစပ်ဖြစ်နိုင်သည်။ Pattern သည်နာမည်သုံးခုမဟုတ်။ တာဝန်သုံးခုဖြစ်သည်။

### Common Failure — စစ်ဆေးသူပါသော်လည်း မစစ်ခြင်း

Verifier အမည်ရှိ node ထည့်ထားရုံဖြင့်စနစ်ကောင်းမဖြစ်။ Verifier ကဘာစစ်မည်ကိုမသတ်မှတ်ထားလျှင် ၎င်းသည်စာရေးတော်၏အခြားမျက်နှာတစ်ခုသာဖြစ်သွားမည်။

မကောင်းသော Verifier က "အဖြေကကောင်းပါသည်" ဟုသာပြောသည်။

ကောင်းသော Verifier က "requested file သုံးခုထဲမှနှစ်ခုပဲဖတ်ထားသည်", "test မ run ထား", "tool output တွင် useful data မပါ", "source claim အတွက် citation မရှိ", "unsafe write action ပါ" ဟုပြောသည်။

Travis-2 ၏ structured Playwright result lesson သည်ဤနေရာတွင်အလွန်အသုံးဝင်သည်။ Browser action တစ်ခုတွင် `execution_ok` ဖြစ်နိုင်သည်။ သို့သော် `data_ok` မဖြစ်နိုင်။ Page ဖွင့်နိုင်သော်လည်းလိုသော data မရနိုင်။ ထို့ကြောင့် `ok = execution_ok and data_ok` ဟုစဉ်းစားခြင်းသည် Verifier mentality ဖြစ်သည်။ "Tool မပျက်ဘူး" ဆိုသည်မှာ "Task အောင်မြင်တယ်" မဟုတ်။

### Mini Lab — သင့် Agent ကို သုံးယောက်ခွဲကြည့်ပါ

စာဖတ်သူသည်သေးငယ်သော task တစ်ခုရွေးပါ။ ဥပမာ README တစ်ခုမှ setup instruction ကိုစစ်ခြင်း။

ပထမအဆင့်တွင် Planner prompt ရေးပါ။ "ဘာဖတ်မလဲ၊ ဘာစစ်မလဲ၊ ဘာမလုပ်ဘူးလဲ" ထုတ်ခိုင်းပါ။

ဒုတိယအဆင့်တွင် Worker ကို Planner output ထဲက allowed files/tools သာပေးပြီးလုပ်ခိုင်းပါ။

တတိယအဆင့်တွင် Verifier ကို source files, worker output, test result ပေးပြီး "pass/fail with evidence" ထုတ်ခိုင်းပါ။

နောက်ဆုံးတွင် Planner output မှားခဲ့သည့်နေရာများကိုမှတ်ပါ။ ဤလေ့ကျင့်ခန်းသည် multi-agent show မဟုတ်။ ကိုယ်တိုင် system designer ဖြစ်လာစေသောလေ့ကျင့်ခန်းဖြစ်သည်။

### နိဂုံး — အာဏာခွဲခြင်းသည် အလှဆင်မဟုတ်

Planner, Worker, Verifier pattern သည် Agent ကိုပိုရှုပ်အောင်လုပ်သောကစားစရာမဟုတ်။ အလုပ်တစ်ခုတွင် "စီမံခြင်း", "လုပ်ခြင်း", "စစ်ခြင်း" ကိုခွဲသိရန်သင်ပေးသော engineering discipline ဖြစ်သည်။ တစ်ခါတစ်ရံ Agent တစ်ခုတည်းလုံလောက်သည်။ တစ်ခါတစ်ရံ graph လိုသည်။ တစ်ခါတစ်ရံ human reviewer လိုသည်။

အရေးကြီးသည်မှာ Agent ကိုဘုရင်မထားရန်ဖြစ်သည်။ Planner ကအကြံပေးပါစေ။ Worker ကလုပ်ပါစေ။ Verifier ကမယုံကြည်ဘဲစစ်ပါစေ။ ထိုအခါ Agentic AI သည်စကားလုံးလှလှများထုတ်သောစာရေးတော်မှ အလုပ်ကိုတိုင်းတာနိုင်သောစနစ်သို့ရွေ့လာမည်။

---
**စာဖတ်သူအတွက် Source Notes:**
- **Planner-Worker-Verifier:** Role separation pattern for decomposition, execution, and validation.
- **Travis-2:** `run_playwright_code` result quality plus `run_agent -> evaluate -> replan -> finalize` shows verifier thinking.
- **BrowserSurfer:** Trajectory callbacks, scoring, and reflection support post-run inspection.
- **P-2:** Minimum state projection is useful when delegating work to sub-agents.
- **Structured result quality:** A tool can execute successfully while still failing the task.
