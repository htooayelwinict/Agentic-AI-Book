# အခန်း ၁၅ - appv22: Emerging Runtime Recovery Lab

> **ဒီ project က ဘာကိုပြသသလဲ**
> appv22 က agent runtime တစ်ခုကို လက်တွေ့စမ်းရင်း ဘယ်နေရာတွေမှာပြဿနာပေါ်တတ်သလဲဆိုတာပြသည်။ Pi နှင့် Hermes မှ idea အချို့ကို Python ဘက်တွင် prototype အဖြစ်ပြန်တည်ဆောက်စမ်းထားသည်။ Agent loop, coding tools, provider boundary, session persistence, context compaction, terminal UI, recovery tests များကိုတစ်နေရာတည်းတွင်စမ်းထားသော research workspace ပါ။
>
> **ဒီ project ကို ဘယ်လိုမဖတ်သင့်သလဲ**
> appv22 ကို final worker kernel အဖြစ်မဖတ်ပါနှင့်။ production-ready စနစ်လည်းမဟုတ်ပါ။ "ပြီးပြီ၊ ယုံပြီးသုံးပါ" ဟုကြေညာထားသော project မဟုတ်ဘဲ gap များကိုမဖုံးထားသော test-backed prototype lab တစ်ခုသာဖြစ်သည်။
>
> **Pi/Hermes နှင့် ဆက်စပ်ပုံ**
> appv22 သည် Pi ကို Python package အဖြစ် import လုပ်ထားခြင်းမဟုတ်ပါ။ Hermes ကိုလည်း dependency အဖြစ်ဆွဲသုံးထားခြင်းမဟုတ်ပါ။ စာရေးသူက Pi ၏ coding-agent loop / TUI / provider abstraction idea များနှင့် Hermes ၏ compaction / overflow recovery / tool-loop guardrail idea များကိုဖတ်ပြီး Python ဖြင့်ပြန်တည်ဆောက်စမ်းထားခြင်းပါ။
>
> **သတိထားရန်**
> OpenClaw နှင့် Pi ကြားတွင် source-level ဆက်စပ်မှုရှိသည်။ OpenClaw ၏ third-party notice တွင် OpenClaw ၏ implementation portions အချို့ကို Pi/pi-mono မှ adapted လုပ်ထားကြောင်းနှင့် `@earendil-works/pi-tui` ကို terminal UI rendering အတွက် depend လုပ်ထားကြောင်းဖော်ပြထားသည်။ သို့သော် "OpenClaw သည် Pi ပဲ" ဟုတစ်ကြောင်းတည်းဖြင့်ချုပ်ပြောခြင်းသည် over-simplified claim ဖြစ်သောကြောင့် fact အဖြစ်မရေးသင့်ချေ။

### ဒီ case study ကို လက်တွေ့လိုက်ဖတ်နည်း

appv22 ကိုဖတ်ရာတွင် "ဒီ project ကိုသုံးမယ်" ဟုမစပါနှင့်။ "runtime တစ်ခု fail ဖြစ်သောအခါ ဘယ်နေရာတွေကဝင်ထိန်းသလဲ" ဆိုသောမေးခွန်းဖြင့်စပါ။

လက်တွေ့လိုက်ရန် path ကိုတစ်ခုသာရွေးပါ။ Context overflow path ကိုရွေးလျှင် `app.py`, `ai/overflow.py`, `compaction/compressor.py`, `compaction/timing.py`, နှင့် `tests/test_compaction_timing.py` ကိုဖတ်ပါ။ စာရွက်ပေါ်တွင် flow ကိုဒီလိုဆွဲပါ။

```text
model call
  -> provider says context too large
  -> overflow detector classifies error
  -> compaction manager trims/summarizes
  -> retry is bounded
  -> latest user message must still win
```

Expected result ကိုလည်းရှင်းထားပါ။ Context overflow ဖြစ်လျှင် blind retry မလုပ်ရပါ။ Context ကိုလျှော့ပြီးမှ retry လုပ်ရပါမည်။ Summary ထဲတွင် secret မပါရပါ။ Latest user message ကို old memory ကမကျော်ရပါ။ ဒီသုံးချက်ကိုရှာနိုင်လျှင် appv22 chapter ၏ recovery lesson ကိုလက်တွေ့မြင်ပြီဟုပြောလို့ရပါသည်။

ဒီအခန်းကို စာရေးသူအနေနှင့် ရှင်းရှင်းဝန်ခံပြီးစပါမည်။ appv22 သည် ကျွန်ုပ်ကိုယ်တိုင်ဒီဇိုင်းဆွဲခါစက ယခုမြင်ရသော project နှင့်လုံးဝမတူခဲ့ပါ။

စစချင်းမှာ decomposer, planner နှင့် worker runtime nodes သုံးခုပါသော graph တစ်ခုဖြစ်ခဲ့သည်။ File mutation scope များအတွက် LLM model များစွာကိုစမ်းရင်း အကုန်အကျလည်းများခဲ့သည်။ Architecture ကိုကိုယ်တိုင်လျှောက်စမ်းရင်း native agentic loop ဘက်သို့ရွေ့သွားပြီး repo သည်လည်းတဖြည်းဖြည်းရှုပ်လာခဲ့သည်။

ထို့နောက် X aka Twitter တွင် Pi ကိုပြန်သတိရရာမှ Agentic Loop ကို adaptation လုပ်ရန် စိတ်ကူးရခဲ့သည်။ Pi ကိုဖတ်သည်။ Hermes ကိုလည်းရှာဖတ်သည်။ ထိုနှစ်ခုထဲမှ agent runtime အတွက်အသုံးဝင်မည့်အယူအဆများကို Python ဘက်တွင် ကိုယ်တိုင်လက်ဖြင့်ပြန်ရေးစမ်းကြည့်သည်။

တချို့နေရာမှာအဆင်ပြေသည်။ တချို့နေရာမှာလမ်းကြောင်းပေါ်ရောက်နေသည်။ တချို့အပိုင်းများကတော့ recovery audit ထဲတွင်ပင်ရှိနေသေးသည်။ ထို့ကြောင့် appv22 ကို အပြီးသတ် worker kernel အဖြစ်မဖတ်ပါနှင့်။ Runtime recovery lab အဖြစ်ဖတ်ပါ။

appv22 ကိုဖတ်ရာတွင် အားပေးစာအဖြစ်လည်းမဖတ်ပါနှင့်။ အပြစ်ရှာစာအဖြစ်လည်းမဖတ်ပါနှင့်။ Runtime တစ်ခုသည် loop တစ်ခုရေးလိုက်ရုံဖြင့်မပြီးကြောင်းကို လက်တွေ့ codebase တစ်ခုထဲကနေကြည့်ရန်ဖြစ်ပါသည်။

Agent တစ်ခုကို ပထမဆုံးရေးသောနေ့တွင် အားလုံးက လှပနေတတ်သည်။ `while` loop တစ်ခုရှိသည်။ Model ကို ခေါ်သည်။ Tool result ကို ပြန်ထည့်သည်။ အဖြေတစ်ခု ထွက်လာသည်။ ထိုအခါ လူတော်တော်များများက "Agent တစ်ခုဖန်တီးနိုင်ပြီ" ဟု ထင်တတ်ကြသည်။

သို့သော် နောက်နေ့တွင် context window ပြည့်လာသည်။ Provider က error ပြန်သည်။ Tool တစ်ခုတည်းကို agent ကထပ်ခါထပ်ခါခေါ်နေသည်။ User က "အခုဘာဖြစ်နေတာလဲ" ဟုမေးသောအခါ terminal ထဲတွင်ရှင်းရှင်းမမြင်ရ။ Session ပြန်ဖွင့်လိုက်လျှင် ယခင် state ကိုယုံရမရမသေချာတော့။

ဒီနေရာမှစ၍ "loop ရှိခြင်း" နှင့် "runtime ရှိခြင်း" ကွာသွားသည်။ appv22 သည် ထိုကွာခြားချက်ကို စမ်းသပ်ဖော်ပြထားသော prototype ဖြစ်သည်။

### Pi ဘက်မှ ယူသည့် သင်ခန်းစာ

Pi ကိုဖတ်သောအခါ အဓိကမြင်ရသောအရာမှာ "minimal agent harness" ဟူသောစိတ်ကူးဖြစ်သည်။ အရာရာကို core ထဲသို့ထည့်မထားဘဲ, agent loop, tool calls, session history, skills, prompt templates, context engineering, TUI, multiple modes စသော primitive များကို အသုံးပြုသူ၏ workflow နှင့်လိုက်အောင်ချဲ့နိုင်စေရန်ဖွင့်ထားသည်။

Coding agent ဆိုသည်မှာ model ကစာရေးပြီး user က copy ကူးသုံးသည့်အရာမဟုတ်။ Model က tool ခေါ်ချင်ကြောင်းပြောသည်။ Runtime က tool ကိုတကယ် execute လုပ်သည်။ Tool result ပြန်လာလျှင် message history ထဲသို့ပြန်ထည့်သည်။ Event များက UI ကိုအသိပေးသည်။ Iteration budget က အဆုံးမရှိပတ်မနေစေရန်ထိန်းသည်။

appv22 ထဲတွင် ထိုအယူအဆများကို Python ဘက်သို့ port လုပ်စမ်းထားကြောင်း source comment များကပြောထားသည်။ `agent_loop.py` တွင် Pi agent loop idea ကိုယူထားသည်။ `coding_agent/agent_session.py` တွင် Pi coding-agent session subset ကိုယူထားသည်။ `tui/` ထဲတွင် Pi-style terminal interaction idea များပါလာသည်။

သို့သော် ဒီနေရာတွင် စာဖတ်သူမမှားစေရန်ထပ်ပြောရမည်။ Port လုပ်သည်ဆိုသည်မှာ upstream repo ကို runtime ထဲမှ import လုပ်ထားသည်ဟုမဆိုလိုချေ။ appv22 သည် Pi ကို dependency အဖြစ်မဆွဲသုံးဘဲ Pi ထဲက design idea များကို Python ဖိုင်များအဖြစ်ပြန်ရေးကြည့်သော prototype ဖြစ်သည်။

`agent_loop.py` ကိုဖတ်လျှင် event များစွာကိုတွေ့ရသည်။ `AgentStartEvent`, `TurnStartEvent`, `MessageStartEvent`, `ToolExecutionStartEvent`, `ToolExecutionEndEvent`, `TurnEndEvent`, `AgentEndEvent` စသည်တို့ဖြစ်သည်။ ဤ event များသည် Agent တစ်ပတ်လည်တိုင်း ဘာဖြစ်သွားသည်ကို user နှင့် runtime နှစ်ဖက်လုံး မြင်နိုင်စေရန်ထားသော ခြေရာဖြစ်သည်။

Tool call ရှိလျှင် execute လုပ်သည်။ Tool result ကို message history ထဲသို့ပြန်ထည့်သည်။ Error သို့မဟုတ် abort ဖြစ်လျှင်ရပ်သည်။ Iteration budget ကုန်လျှင် summary တောင်းရန်ကြိုးစားသည်။ ဤသေးသေးလေးများကိုပေါင်းလိုက်မှ "agent loop" ဟုခေါ်နိုင်သည်။ Model ကိုထပ်ခါထပ်ခါခေါ်နေခြင်းသက်သက်တော့မဟုတ်ချေ။

ဒီနေရာတွင် စာဖတ်သူက မိမိ project ကို ပြန်မေးသင့်သည်။ "ငါ့ agent က tool result ကို ဘယ်လိုသိမ်းသလဲ" ဟု စမေးပါ။ ထို့နောက် event, stop condition, iteration budget, user ၏ ကြားဖြတ် steering message ကို ကိုင်သောနည်း တို့ ရှိမရှိ စစ်ပါ။ ဒီအချက်များကို စစ်သောအခါမှ agent loop သည် engineering topic ဖြစ်လာသည်။

### Hermes ဘက်မှ ယူသည့် သင်ခန်းစာ

Hermes ကိုဖတ်ရာတွင် appv22 အတွက်အရေးကြီးသောစကားလုံးမှာ memory နှင့် recovery ဖြစ်သည်။ Hermes public site/repo များတွင် persistent memory, automated skill creation, multi-platform gateway, execution environments, browser/web control, trajectory export, container hardening စသောအရာများကိုဖော်ပြထားသည်။ appv22 သည် ထိုအရာအားလုံးကိုတစ်ပုံစံတည်းပြန်တည်ဆောက်ထားသည်ဟု မဆိုလို။ appv22 အတွက် အဓိကယူထားသောအပိုင်းမှာ context compaction, overflow recovery, tool-loop guardrail တို့ဖြစ်သည်။

ဒီနေရာတွင် recovery ဟူသော English စကားလုံးကိုသုံးထားခြင်းမှာ အကြောင်းရှိသည်။ မြန်မာလို တိုက်ရိုက်ပြန်လျှင် တစ်ခါတစ်ရံ သဘာဝမကျတတ်သဖြင့်ပင်ဖြစ်သည်။ ဒီအခန်းတွင် recovery ဆိုသည်မှာ "runtime အမှားတွေ့ပြီးနောက် အခြေအနေကိုပြန်စစ်၍ ဆက်လုပ်နိုင်သောလမ်းကိုရှာခြင်း" ဟုပဲဖတ်ပါ။

Agent conversation တစ်ခုသည် အချိန်ကြာလာလျှင် ရှင်းလင်းမှုလျော့လာတတ်သည်။ User instruction, file path, old tool output, error message, plan, test result, old summary, new request တို့ရောထွေးလာသည်။ အကုန်ထားလျှင် context window ပြည့်မည်။ အကုန်ဖျက်လျှင် memory ပျောက်မည်။ Summary လုပ်သော်လည်း latest user message ကိုမမှတ်နိုင်လျှင် agent သည် ယနေ့အလုပ်မလုပ်ဘဲ မနေ့ကအလုပ်ဆက်လုပ်သွားနိုင်သည်။

appv22 ၏ `compaction/compressor.py` သည် ထိုပြဿနာကိုနှစ်ဆင့်ဖြင့်ကိုင်ရန်ကြိုးစားသည်။ ပထမဆင့်မှာ deterministic pruning ဖြစ်သည်။ Duplicate tool output များကို လျှော့ပစ်သည်၊ အလွန်ကြီးသော tool result များကို ချုံ့သည်၊ image payload များကို token budget အတွက် ထိန်းသည်၊ huge tool-call args များကို truncate လုပ်သည်။

ဒုတိယဆင့်မှာ LLM summary compaction ဖြစ်သည်။ History ကို structured summary အဖြစ် ပြန်ရေးသည်၊ latest user message ကို active truth အဖြစ်ထားသည်၊ secrets/tokens များကို redact လုပ်သည်။ Summary marker များဖြင့် old context ကို reference-only ဖြစ်စေရန်ကြိုးစားသည်။

ဒီနေရာတွင် သတိထားရမည့်အချက်မှာ summary မှားလျှင် runtime ကို လမ်းလွဲစေခြင်းဖြစ်သည်။ Old task ကို active task အဖြစ်ရေးမိလျှင် agent သည် user ၏နောက်ဆုံးအမိန့်ကိုမလိုက်တော့။ Secret ပါသွားလျှင် safety ပြဿနာဖြစ်သည်။ ထို့ကြောင့် appv22 ထဲတွင် `SUMMARY_PREFIX` သည် latest user message wins ဟူသော guardrail ကိုထည့်ထားပြီး persistent memory ကို authority အဖြစ်ခွဲရန်ကြိုးစားထားသည်။

သို့သော် prefix တစ်ခုရေးထားခြင်းဖြင့် အရာရာလုံခြုံသွားသည်ဟု မယူသင့်ချေ။ Compaction သည် prompt trick မဟုတ်။ Runtime behavior ဖြစ်သည်။ Test, cooldown, fallback, bounded retry များဖြင့်စစ်ရသောအရာဖြစ်သည်။

### appv22 ထဲတွင် အမှန်တကယ်ချိတ်ထားသောနေရာ

`app.py` ထဲမှ `CodingApp` ကိုဖတ်လျှင် appv22 ၏အဓိကချိတ်ဆက်ရာကိုမြင်နိုင်သည်။ `AgentSession`, `ContextCompressor`, `CompactionManager`, model/provider config, TUI renderer, tool definitions တို့ကို ဒီနေရာတွင်ပေါင်းထားသည်။

ဒီနေရာကို "structure flow" အဖြစ်သာဖတ်လျှင် ဘာမှထူးမည်မဟုတ်ပါ။ စာဖတ်သူအနေဖြင့် "model call တစ်ခုကို runtime ကဘယ်နေရာတွေမှာဝင်စစ်သလဲ" ဟုပြန်ဖတ်သင့်သည်။

`CodingApp.run_turn()` တွင် prompt ကို model ထံပို့ပြီးအဖြေယူရုံမဟုတ်။ Prompt မပို့မီ output-cap recovery ကိုစစ်သည်။ Context overflow recovery ကိုစစ်သည်။ Failed turn context ကို compact လုပ်ရန်လိုမလိုစစ်သည်။ Prompt run ပြီးနောက် post-response compaction လိုမလိုထပ်ကြည့်သည်။ Provider error ထွက်လာလျှင် ထို error message ကို context ထဲတွင်ထားသင့်သလား, ဖယ်ပြီး compact-and-retry လုပ်သင့်သလား စဉ်းစားသည်။

ဤသည်မှာ appv22 ၏ အဓိကစမ်းသပ်ချက်ဖြစ်သည်။ Runtime ဆိုသည်မှာ model call မတိုင်မီ, model call နောက်ပိုင်း, failure ဖြစ်ပြီးနောက်, next turn မတိုင်မီ state ကို ပြန်ကြည့်သောစနစ်ဖြစ်သည်။

Beginner များအတွက် provider ဟူသောစကားလုံးကိုလည်း ရိုးရိုးဖတ်ပါ။ Provider ဆိုသည်မှာ model ကို အမှန်တကယ်ခေါ်ပေးသော service boundary ဖြစ်သည်။ OpenAI-compatible endpoint, OpenRouter, သို့မဟုတ် test အတွက် faux provider ဖြစ်နိုင်သည်။ appv22 သည် real API မခေါ်ဘဲ test လုပ်နိုင်ရန် faux provider tests များကိုထားထားသည်။ Agent runtime တစ်ခုသည် API key မရှိလျှင် test မလုပ်နိုင်သောအခြေအနေသို့ မရောက်သင့်ချေ။

Provider error များတွင် context overflow, output cap, rate limit, auth error, stream ပြတ်ခြင်း စသည်ဖြင့် အမျိုးမျိုးရှိသည်။ `ai/overflow.py` သည် error text များထဲမှ context overflow နှင့် output-token cap ကိုခွဲဖတ်ရန်ကြိုးစားထားသည်။ ဤသည်မှာ "error ဖြစ်လျှင် retry" ဟူသောရိုးရိုးစိတ်ကူးထက်ပိုကောင်းသောအရာဖြစ်သည်။

Retry ဆိုသည်မှာ error ဖြစ်စေသော အကြောင်းရင်းကို နည်းနည်းဖြစ်စေ ပြင်ပြီးမှ ထပ်လုပ်ခြင်းဖြစ်သည်။ Context overflow ဖြစ်နေရာတွင် context မလျှော့ဘဲ retry လုပ်လျှင် အမှားကိုဒုတိယအကြိမ်ပြန်လုပ်ခြင်းသာဖြစ်သည်။

### Tool loop ကို runtime policy ဖြင့် ထိန်းပါ

Agent တစ်ခုသည်တစ်ခါတစ်ရံ file တစ်ခုကိုဖတ်သည်။ မတွေ့။ နောက်တစ်ခါထပ်ဖတ်သည်။ မတွေ့။ `grep` လုပ်သည်။ မတွေ့။ နောက်တစ်ဖန် `grep` လုပ်သည်။ အလုပ်မတိုးသော်လည်း token ကုန်သည်။ User အချိန်ကုန်သည်။ Runtime အပေါ်တွင် Trust လျော့လာသည်။

ဤပြဿနာကို prompt ထဲတွင် "မပတ်ပါနှင့်" ဟုရေးထားရုံဖြင့်မလုံလောက်ချေ။ appv22 ၏ `agent/tool_guardrails.py` သည် tool call များကို runtime အဆင့်တွင်ကြည့်ရန်ကြိုးစားထားသည်။ Tool name နှင့် canonical args မှ stable signature ထုတ်သည်၊ result hash ကိုကြည့်သည်၊ same failure count နှင့် no-progress count များကို တွက်သည်။ ထို့နောက် allow, warn, block, halt စသော decision များထုတ်နိုင်ရန်ကြိုးစားသည်။

Idempotent tool နှင့် mutating tool ကို ခွဲရမည်။ `read`, `grep`, `find`, `ls` ကဲ့သို့ read-style tools များသည် ထပ်ခေါ်လျှင် အန္တရာယ်နည်းနိုင်သည်။ `write`, `edit`, `browser_click`, `send_message` ကဲ့သို့ mutation ပါသော tools များသည် ထပ်ခါထပ်ခါလုပ်လျှင် အန္တရာယ်များနိုင်သည်။ ထို့ကြောင့် tool guardrail သည် runtime policy ဖြစ်သင့်သည်။

သို့သော် recovery audit အရ tool-loop guardrails သည် partial/risky area ဖြစ်နေသေးသည်။ ထို့ကြောင့် appv22 သည် no-progress tool loop ပြဿနာကို runtime guardrail အဖြစ် စမ်းသပ်ဆဲအဆင့်တွင်သာ ရှိသေးသည်။

### Context ကို ဘယ်အချိန်တွင်ချုံ့မလဲ

Context compaction တွင် "ချုံ့နိုင်သလား" ဟူသောမေးခွန်းထက် "ဘယ်အချိန်တွင်ချုံ့သင့်သလဲ" ဟူသောမေးခွန်းကပိုအရေးကြီးတတ်သည်။ အချိန်မမှန်လျှင် context ကောင်းကောင်းရှိနေရာမှ မလိုအပ်ဘဲ summary လုပ်မိနိုင်သည်။ နောက်ကျလွန်းလျှင် provider က context overflow ဖြင့်ငြင်းနိုင်သည်။

`compaction/timing.py` သည် preflight, post-response, overflow, manual စသောလမ်းကြောင်းများကိုခွဲထားသည်။ Preflight သည် model call မတိုင်မီ rough token estimate ဖြင့်စစ်ခြင်းဖြစ်သည်။ Post-response သည် provider usage သိပြီးနောက် next turn အတွက်စဉ်းစားခြင်းဖြစ်သည်။ Overflow သည် provider က context too large ဟုငြင်းလျှင် bounded recovery လုပ်ခြင်းဖြစ်သည်။ Manual သည် user/operator က `/compress` ခေါ်သောအခါဖြစ်သည်။

`tests/test_compaction_timing.py` တွင် immediate second compaction မလုပ်ခြင်း, real usage သိပြီးနောက် preflight ကိုခဏရွှေ့ခြင်း, overflow recovery bounded ဖြစ်ခြင်း စသော behavior များကိုစစ်ရင်ရေးထားသည်။ Recovery audit ထဲတွင် redundant compaction rewrite issue တစ်ခုကို fix လုပ်ထားသည်။

Runtime quality ကို ဆုံးဖြတ်သည့်အရာမှာ "summary ထုတ်နိုင်သည်" ဟူသော feature ထက် summary ထုတ်သည့်အချိန်, summary ထပ် rewrite မဖြစ်စေရန်, summary မအောင်မြင်လျှင် fallback ဘယ်လိုလုပ်မလဲ, already-compacted transcript ကို ဘယ်လိုကိုင်မလဲ စသောအရာများဖြစ်သည်။

### Session နှင့် TUI သည် runtime ကို မြင်နိုင်စေသည်

Coding agent တစ်ခုတွင် user သည် agent က ဘာဖတ်နေသလဲ, ဘာ tool ခေါ်နေသလဲ, ဘယ် model ကိုသုံးနေသလဲ, compaction ဖြစ်နေသလား, retry ဖြစ်နေသလား, abort လုပ်နိုင်သလား ဆိုသည်တို့ကိုမြင်သင့်သည်။ မမြင်ရလျှင် runtime ကိုယုံရခက်သည်။

`coding_agent/agent_session.py` သည် session, active tools, model cycling, compaction events, auto retry, branch summary, session store စသောအရာများစွာကိုကိုင်ထားသည်။ စာဖတ်သူအနေဖြင့် ဤ file ကို mixed responsibility risk ရှိသည်ဟုမှတ်ထားသင့်သည်။ File တစ်ခုထဲတွင်တာဝန်များအလွန်များလာလျှင် bug ရှာရခက်လာသည်။

`tui/` folder သည် terminal input, rendering, keybindings, status, image handling, interactive mode စသော Pi-style terminal idea များကိုယူထားသည်။ သို့သော် လက်ရှိ TUI runtime controls သည် partial/broken risk ရှိနေသည်ကို စာဖတ်သူများ သတိချပ်စေချင်ပါသည်။ ထို့ကြောင့် TUI ကို ပြီးပြည့်စုံသော UI အဖြစ် မသတ်မှတ်သင့်သေးချေ။ Agent runtime ကို user မြင်နိုင်စေရန်ကြိုးစားထားသောအပိုင်းဖြစ်သော်လည်း stabilization လိုနေသေးသောနေရာဖြစ်သည်။

### Inspiration နှင့် dependency ကို ခွဲပါ

appv22 README က reference copies of upstream `hermes-agent/` and `pi/` codebases are not runtime dependencies ဟုရှင်းပြထားသည်။ Recovery audit ၏ kill list ထဲတွင် reference repos `pi/` နှင့် `hermes-agent/` ကို runtime dependencies အဖြစ်မသုံးရန်ထည့်ထားသည်။ `test_no_appv21_coupling.py` ကလည်း appv21/appV2.1 coupling မကျန်စေရန်စစ်ထားသည်။

Inspiration နှင့် dependency မတူ။ Port လုပ်ခြင်းနှင့် blind copy မတူ။ Design idea တစ်ခုဘယ်ကလာသလဲသိရန်လိုသလို, လက်ရှိ runtime ကဘယ်အရာပေါ်မူတည်နေသလဲကိုလည်းရှင်းရမည်။

appv22 က Pi/Hermes folder တွေကို runtime ထဲက တိုက်ရိုက် import လုပ်နေရင် boundary မသန့်တော့ပါဘူး။ `tests/test_no_appv21_coupling.py` ဆိုတဲ့ test ရှိပါတယ်။ ဒါပေမယ့် သူ စစ်တာက `appv21` ဆိုတဲ့ စာလုံး source ထဲ ပါမပါပဲ ဖြစ်ပြီး Pi/Hermes import ကို မစစ်ပါဘူး။ ဒါကြောင့် "boundary ကို test နဲ့ စစ်ထားတယ်" လို့ ပြောရင် တစ်ဝက်ပဲ မှန်ပါတယ်။ Test နာမည်က ပြောတာနဲ့ test ကိုယ်တိုင် စစ်တာ တူရဲ့လား အမြဲ ပြန်ဖတ်ပါ။ အကြောင်းမှာ agent runtime တစ်ခုတွင် "ဘယ်အရာက source of truth လဲ" ဟူသောမေးခွန်းသည် အမြဲအရေးကြီးသောကြောင့်ဖြစ်သည်။

### OpenClaw hype ကို ဘယ်လိုဖတ်မလဲ

Agent ecosystem တွင် project အသစ်တစ်ခုထွက်တိုင်း hype တက်တတ်သည်။ OpenClaw ကဲ့သို့သော project/article များတွင် local gateway, skills, personal assistant, browser/computer control, security risk စသောစကားလုံးများမြင်ရတတ်သည်။ ထိုအချိန်တွင် developer တစ်ယောက်၏အလုပ်မှာ social media စကားစစ်ထိုးခြင်းထက် architecture ကို ဖတ်ခြင်းဖြစ်သည်။

မေးခွန်းကို ရိုးရိုးထားပါ။ "ဒီ project ထဲမှာ runtime အစိတ်အပိုင်း ဘယ်နှစ်ခု တကယ်ရှိသလဲ" ဟု မေးပါ။ စစ်ရမည့်စာရင်းမှာ loop, tool broker, skill loader, memory/session, context compaction, provider boundary, safety guardrail, user-facing runtime status တို့ဖြစ်သည်။

Pi official site သည် OpenClaw ကို SDK real-world integration example အဖြစ် link ထားသည်။ ထို့အပြင် OpenClaw ၏ `THIRD_PARTY_NOTICES.md` တွင် OpenClaw ၏ implementation portions အချို့ကို Pi/pi-mono မှ adapted လုပ်ထားကြောင်းနှင့် `@earendil-works/pi-tui` ကို terminal UI rendering အတွက် depend လုပ်ထားကြောင်း ဖော်ပြထားသည်။

ထို့ကြောင့် OpenClaw ကို Pi ecosystem နှင့်လုံးဝမဆိုင်သကဲ့သို့ မသတ်မှတ်သင့်ချေ။ သို့သော် "OpenClaw သည် Pi ပဲ" ဟုလည်း ယတိပြတ်မယူဆသင့်ချေ။ OpenClaw သည် Pi/pi-mono မှအချို့ implementation idea/code portions များကိုယူထားပြီး Pi TUI package ကိုအသုံးပြုထားသော broader personal-agent runtime တစ်ခုသာဖြစ်သည်။

စာဖတ်သူတို့ မွေးမြူထားသင့်သော အကျင့်မှာ အင်တာနက်တွင် Hype တခုပေါ်လာလျင် ထို Hype ကို သေချာလေ့လာပြီး code-reading habit အဖြစ်ပြောင်းရန်ဖြစ်သည်။

### appv22 က စာဖတ်သူကို ဘာသင်ပေးသလဲ

1. Loop သည် အစသာဖြစ်သည်။ Loop ထဲတွင် event, tool execution, stop condition, iteration budget, steering/follow-up message များ ပါလာမှ user-facing agent ဖြစ်လာသည်။
2. Provider boundary ကို သီးခြားစဉ်းစားရသည်။ Model API သည် အမြဲမမှန်။ Error text ကို ခွဲဖတ်ရသည်။ Faux provider ဖြင့် network/API key မလိုသော tests ရှိသင့်သည်။
3. Context compaction သည် deterministic pruning, LLM summary, secret redaction, latest-message priority, cooldown, bounded retry တို့ပါသော runtime behavior ဖြစ်သည်။ Summary feature တစ်ခုထက် ပိုကျယ်သည်။
4. Tool-loop guardrail သည် runtime policy ဖြစ်သည်။ Tool signature, result hash, idempotent/mutating distinction, allow/warn/block/halt decision များ လိုသည်။
5. TUI သည် trust တည်ဆောက်ရာနေရာဖြစ်သည်။ Agent ဘာလုပ်နေသည်ကို user မမြင်လျှင် trust မတည်ဆောက်နိုင်။ သို့သော် TUI သည် ကျယ်ပြန့်သောအပိုင်းဖြစ်သောကြောင့် မတည်ငြိမ်သေးသောနေရာကို overclaim မလုပ်သင့်ချေ။
6. Recovery audit သည် project ကို အမှန်အတိုင်းမြင်စေသော engineering discipline ဖြစ်သည်။ Gap map, kill list, NEXT_PATCH plan များက ထိုအလုပ်ကို လုပ်သည်။

### စာဖတ်သူကိုယ်တိုင် ဖတ်ကြည့်ရန်

ဒီအခန်းပြီးလျှင် repo ကိုဖွင့်ပြီး အောက်ပါအတိုင်းဖတ်ကြည့်ပါ။

1. `README.md` ကိုဖတ်ပြီး appv22 ကို Pi x Hermes Python agent runtime ဟု repo ကဘယ်လိုဖော်ပြထားသလဲကြည့်ပါ။
2. `docs/appv22-recovery-audit.md` ကိုဖတ်ပြီး current state, gap map, kill list, NEXT_PATCH ကိုအရင်မှတ်ပါ။
3. `appV2.2/appv22/app.py` ထဲမှ `CodingApp.run_turn()` ကိုဖတ်ပါ။ Model call မတိုင်မီနှင့်နောက်ပိုင်း recovery check များကိုမှတ်ပါ။
4. `agent/agent_loop.py` ကိုဖတ်ပြီး event sequence နှင့် tool call loop ကိုဆွဲပါ။
5. `agent/tool_guardrails.py` တွင် idempotent/mutating tool lists နှင့် decision actions ကိုရှာပါ။
6. `compaction/compressor.py` တွင် deterministic pruning, summary prefix, redaction logic ကိုရှာပါ။
7. `compaction/timing.py` တွင် preflight/post-response/overflow/manual timing လမ်းကြောင်းများကိုခွဲပါ။
8. `tests/test_no_appv21_coupling.py`, `tests/test_ai_faux.py`, `tests/test_compaction_timing.py` ကိုဖတ်ပြီး appv22 သည် test ဖြင့်ဘယ် boundary များကိုစစ်ထားသလဲကြည့်ပါ။

ဤလေ့ကျင့်ခန်းများ၏ ရည်ရွယ်ချက်မှာ runtime တစ်ခုကို README, audit, source comment, test, entrypoint တို့ဖြင့် ဘယ်လိုဖတ်မလဲကို လေ့ကျင့်ရန်ဖြစ်သည်။

### နိဂုံး

appv22 သည် အလွန်သစ်သော prototype recovery lab ဖြစ်ပြီး final worker kernel, အပြီးသတ်နည်းလမ်း, production-ready စနစ် တစ်ခုမှ မဟုတ်။

သို့သော် appv22 သည် beginner developer နှင့် engineer နှစ်မျိုးလုံးအတွက် အသုံးဝင်သောသင်ခန်းစာပေးသည်။ Agent loop ရေးခြင်းသည် ပထမခြေလှမ်းသာဖြစ်သည်။ ထို loop ကို provider boundary, tool guardrail, compaction timing, overflow recovery, session persistence, TUI, tests တို့ဖြင့်စစ်ပြီးထိန်းနိုင်မှ runtime ဟုခေါ်ထိုက်လာသည်။

ဒီအခန်းကိုဖတ်ပြီး စာဖတ်သူသည် "ငါလည်း loop တစ်ခုရေးမယ်" ဟုသာ မထင်သင့်ချေ။ "ငါ့ loop က error ဖြစ်သွားလျှင် ဘယ်လိုပြန်စစ်မလဲ" ဟု မေးတတ်လာသင့်သည်။ ထိုမေးခွန်း၏နောက်တွင် context ပြည့်လျှင် ချုံ့နည်း၊ tool တစ်ခုတည်းကို ထပ်ခါထပ်ခါခေါ်နေလျှင် ရပ်နည်း၊ user က terminal ထဲတွင် ဘာဖြစ်နေသလဲ မြင်နိုင်ခြင်း တို့ ပါလာသည်။

ထိုမေးခွန်း စမေးသောအခါ Agentic AI သည် buzzword မှ engineering သို့ကူးသွားပေသည်။

---

**စာဖတ်သူအတွက် Source Notes:**

- **GitHub source:** `https://github.com/htooayelwinict/allthebest`
- **Repo docs:** `README.md`, `docs/appv22-recovery-audit.md`
- **Core runtime files:** `appV2.2/appv22/app.py`, `appV2.2/appv22/agent/agent_loop.py`, `appV2.2/appv22/agent/tool_guardrails.py`, `appV2.2/appv22/ai/overflow.py`, `appV2.2/appv22/coding_agent/agent_session.py`, `appV2.2/appv22/compaction/compressor.py`, `appV2.2/appv22/compaction/timing.py`
- **Tests to read:** `appV2.2/tests/test_no_appv21_coupling.py`, `appV2.2/tests/test_agent_loop.py`, `appV2.2/tests/test_ai_faux.py`, `appV2.2/tests/test_ai_appv2_env_provider.py`, `appV2.2/tests/test_compaction.py`, `appV2.2/tests/test_compaction_timing.py`, `appV2.2/tests/test_tui.py`
- **Pi anchors:** `https://pi.dev`, `https://github.com/earendil-works/pi`
- **Hermes anchors:** `https://hermes-agent.org`, `https://github.com/NousResearch/hermes-agent`
- **OpenClaw/Pi context:** Pi site က OpenClaw ကို SDK integration example အဖြစ် link ထားသည်။ OpenClaw `THIRD_PARTY_NOTICES.md` က Pi/pi-mono မှ portions adapted လုပ်ထားကြောင်းနှင့် `@earendil-works/pi-tui` dependency ရှိကြောင်းဖော်ပြထားသည်။
