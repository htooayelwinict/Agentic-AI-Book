# ၁၅။ appv22 — Pi နှင့် Hermes ကို Python ဘက်သို့ စမ်းသပ် port လုပ်ခြင်း

> **ဤ project က ဘာကိုပြသသလဲ**  
> appv22 သည် စာရေးသူက Pi နှင့် Hermes တို့မှ runtime idea များကို Python ဘက်သို့ prototype အဖြစ် port လုပ်စမ်းထားသော agent-runtime research workspace ဖြစ်သည်။ Agent loop, coding tools, provider boundary, session persistence, context compaction, terminal UI, recovery test များကို တစ်နေရာတည်းတွင်စမ်းထားသည်။
>
> **ဤ project ကို ဘယ်လိုမဖတ်သင့်သလဲ**  
> appv22 သည် final worker kernel မဟုတ်။ production-ready စနစ်မဟုတ်။ "ပြီးပြီ၊ ယုံပြီးသုံးပါ" ဟုကြေညာရန်မဟုတ်။ အလွန်သစ်သေးသော, gap များကိုလည်းဖုံးမထားသော, test-backed prototype lab တစ်ခုသာဖြစ်သည်။
>
> **Pi/Hermes နှင့် ဆက်စပ်ပုံ**  
> appv22 သည် Pi ကို Python package အဖြစ် import လုပ်ထားခြင်းမဟုတ်။ Hermes ကိုလည်း dependency အဖြစ်ဆွဲသုံးထားခြင်းမဟုတ်။ စာရေးသူက Pi ၏ coding-agent loop / TUI / provider abstraction idea များနှင့် Hermes ၏ compaction / overflow recovery / tool-loop guardrail idea များကိုဖတ်ပြီး Python ဖြင့်ပြန်တည်ဆောက်စမ်းထားခြင်းဖြစ်သည်။
>
> **သတိထားရန်**  
> OpenClaw နှင့် Pi ကြားတွင် source-level ဆက်စပ်မှုရှိသည်။ OpenClaw ၏ third-party notice တွင် OpenClaw ၏ implementation portions အချို့ကို Pi/pi-mono မှ adapted လုပ်ထားကြောင်းနှင့် `@earendil-works/pi-tui` ကို terminal UI rendering အတွက် depend လုပ်ထားကြောင်းဖော်ပြထားသည်။ သို့သော် "OpenClaw သည် Pi ပဲ" ဟုတစ်ကြောင်းတည်းဖြင့်ချုပ်ပြောခြင်းသည် over-simplified claim ဖြစ်သောကြောင့် fact အဖြစ်မရေးသင့်ချေ။

ဤအခန်းကို စာရေးသူအနေနှင့် ရှင်းရှင်းဝန်ခံပြီးစရမည်။ appv22 သည် ကျွန်ုပ်ကိုယ်ပိုင်ဒီဇိုင်းဆွဲထားခါစက ယခုနှင့်လုံးဝကိုခြားနားသော project ဖြစ်သည်။ သို့ရာတွင် Architecture ပိုင်းကို ရေလိုက်လွဲရင်း (အထူးသဖြင့် langchain sdk လိုဟာမျိုးမသုံးဘဲ) native agentic loop ကို ကိုယ်တိုင်လျှောက်စမ်းရင်းနဲ့ ပိုဆိုးလာပြီး dirty repo တခုဖြစ်လာတော့သည်။ ဒီ project စစချင်းကမူ decomposer , planner နဲ့ worker runtime nodes သုံးခုပါသော graph တခုဖြစ်ပြီး file mutation scope များအတွက် LLM models ပေါင်းများစွာကိုစမ်းရင်း အင်မတန် အကုန်အကျလည်းများခဲ့ရသည်။ ထို့နောက် X aka Twitter ကို အသုံးပြုရင်း Pi ကို ပြေးသတိရမိရာမှ Agentic Loop ကို adaptation လုပ်ရန် စိတ်ကူးရခဲ့သည်။ ထိုနောက် တွင်မူ Pi ကိုဖတ်သည်။ Hermes ကိုလည်း ရှာဖတ်သည်။ ထိုနှစ်ခုထဲမှ agent runtime အတွက်အသုံးဝင်မည့်အယူအဆများကို Python ဘက်တွင် ကိုယ်တိုင်လက်ဖြင့်ပြန်ရေးစမ်းကြည့်သည်။ တချို့နေရာတွင်အဆင်ပြေသည်။ တချို့နေရာတွင်လမ်းကြောင်းပေါ်ရောက်နေသည်။ သို့သော် စိတ်မရှည်တော့သဖြင့် codex 20x plan ဝယ်ပြီး တီးထုတ်ပေးလိုက်တော့သည်။ ဒါတောင် တချို့နေရာတွင်မူ recovery audit ထဲမှာပင် ရှိနေသေးသော project ဖြစ်သည်။

ထို့ကြောင့် appv22 ကိုဖတ်ရာတွင် အားပေးစာအဖြစ်လည်းမဖတ်သင့်ချေ။ အပြစ်ရှာစာအဖြစ်လည်းမဖတ်သင့်ချေ။ Runtime တစ်ခုသည် loop တစ်ခုရေးလိုက်ရုံဖြင့် မဖြစ်ကြောင်းကို လက်တွေ့ codebase တစ်ခုထဲကနေ ကြည့်ရန်ဖြစ်သည်။

Agent တစ်ခုကိုပထမဆုံးရေးသောနေ့တွင် အားလုံးကလှပနေတတ်သည်။ `while` loop တစ်ခုရှိသည်။ Model ကိုခေါ်သည်။ Tool result ကိုပြန်ထည့်သည်။ အဖြေတစ်ခုထွက်လာသည်။ ထိုအခါ လူတော်တော်များများက "Agent ပြီးပြီ" ဟုထင်တတ်ကြသည်။

သို့သော် နောက်နေ့တွင် context window ပြည့်လာသည်။ Provider က error ပြန်သည်။ Tool တစ်ခုတည်းကို agent ကထပ်ခါထပ်ခါခေါ်နေသည်။ User က "အခုဘာဖြစ်နေတာလဲ" ဟုမေးသောအခါ terminal ထဲတွင်ရှင်းရှင်းမမြင်ရ။ Session ပြန်ဖွင့်လိုက်လျှင် ယခင် state ကိုယုံရမရမသေချာတော့။

ဤနေရာမှစ၍ "loop ရှိခြင်း" နှင့် "runtime ရှိခြင်း" ကွာသွားသည်။ appv22 သည် ထိုကွာခြားချက်ကို စမ်းသပ်ဖော်ပြထားသော prototype ဖြစ်သည်။

### Pi ဘက်မှ ယူသည့် သင်ခန်းစာ

Pi ကိုဖတ်သောအခါ အဓိကမြင်ရသောအရာမှာ "minimal agent harness" ဟူသောစိတ်ကူးဖြစ်သည်။ အရာရာကို core ထဲသို့ထည့်မထားဘဲ, agent loop, tool calls, session history, skills, prompt templates, context engineering, TUI, multiple modes စသော primitive များကို အသုံးပြုသူ၏ workflow နှင့်လိုက်အောင်ချဲ့နိုင်စေရန်ဖွင့်ထားသည်။

ဤစာအုပ်အတွက် Pi ၏အရေးကြီးသောသင်ခန်းစာမှာ တစ်ခုတည်းဖြစ်သည်။ Coding agent ဆိုသည်မှာ model ကစာရေးပြီး user က copy ကူးသုံးသည့်အရာမဟုတ်။ Model က tool ခေါ်ချင်ကြောင်းပြောသည်။ Runtime က tool ကိုတကယ် execute လုပ်သည်။ Tool result ပြန်လာလျှင် message history ထဲသို့ပြန်ထည့်သည်။ Event များက UI ကိုအသိပေးသည်။ Iteration budget က အဆုံးမရှိပတ်မနေစေရန်ထိန်းသည်။

appv22 ထဲတွင် ထိုအယူအဆများကို Python ဘက်သို့ port လုပ်စမ်းထားကြောင်း source comment များကပြောထားသည်။ `agent_loop.py` တွင် Pi agent loop idea ကိုယူထားသည်။ `coding_agent/agent_session.py` တွင် Pi coding-agent session subset ကိုယူထားသည်။ `tui/` ထဲတွင် Pi-style terminal interaction idea များပါလာသည်။

သို့သော် ဤနေရာတွင် စာဖတ်သူမမှားစေရန်ထပ်ပြောရမည်။ Port လုပ်သည်ဆိုသည်မှာ upstream repo ကို runtime ထဲမှ import လုပ်ထားသည်ဟုမဆိုလိုချေ။ appv22 သည် Pi ကို dependency အဖြစ်မဆွဲသုံးဘဲ Pi ထဲက design idea များကို Python ဖိုင်များအဖြစ်ပြန်ရေးကြည့်သော prototype ဖြစ်သည်။

`agent_loop.py` ကိုဖတ်လျှင် event များစွာကိုတွေ့ရသည်။ `AgentStartEvent`, `TurnStartEvent`, `MessageStartEvent`, `ToolExecutionStartEvent`, `ToolExecutionEndEvent`, `TurnEndEvent`, `AgentEndEvent` စသည်တို့ဖြစ်သည်။ ဤ event များသည်အလှဆင်မဟုတ်။ Agent တစ်ပတ်လည်တိုင်း ဘာဖြစ်သွားသည်ကို user နှင့် runtime နှစ်ဖက်လုံးမြင်နိုင်စေရန်ထားသောခြေရာဖြစ်သည်။

Tool call ရှိလျှင် execute လုပ်သည်။ Tool result ကို message history ထဲသို့ပြန်ထည့်သည်။ Error သို့မဟုတ် abort ဖြစ်လျှင်ရပ်သည်။ Iteration budget ကုန်လျှင် summary တောင်းရန်ကြိုးစားသည်။ ဤသေးသေးလေးများကိုပေါင်းလိုက်မှ "agent loop" ဟုခေါ်နိုင်သည်။ Model ကိုထပ်ခါထပ်ခါခေါ်နေခြင်းသက်သက်တော့မဟုတ်ချေ။

စာဖတ်သူသည် ဤနေရာတွင် မိမိ project ကိုပြန်မေးသင့်သည်။ "ငါ့ agent မှာ event ရှိသလား။ Tool result ကိုဘယ်လိုသိမ်းသလဲ။ Stop condition ရှိသလား။ Iteration budget ရှိသလား။ User က ကြားဖြတ် steering message ပို့လျှင်ဘယ်လိုကိုင်မလဲ။" ဤမေးခွန်းများကိုမေးသောအခါမှ agent loop သည် engineering topic ဖြစ်လာသည်။

### Hermes ဘက်မှ ယူသည့် သင်ခန်းစာ

Hermes ကိုဖတ်ရာတွင် appv22 အတွက်အရေးကြီးသောစကားလုံးမှာ memory နှင့် recovery ဖြစ်သည်။ Hermes public site/repo များတွင် persistent memory, automated skill creation, multi-platform gateway, execution environments, browser/web control, trajectory export, container hardening စသောအရာများကိုဖော်ပြထားသည်။ appv22 သည် ထိုအရာအားလုံးကိုတစ်ပုံစံတည်းပြန်တည်ဆောက်ထားသည်ဟု မဆိုလို။ appv22 အတွက် အဓိကယူထားသောအပိုင်းမှာ context compaction, overflow recovery, tool-loop guardrail တို့ဖြစ်သည်။

ဤနေရာတွင် recovery ဟူသော English စကားလုံးကိုသုံးထားခြင်းမှာ အကြောင်းရှိသည်။ မြန်မာလို တိုက်ရိုက်ပြန်လျှင် တစ်ခါတစ်ရံ သဘာဝမကျတတ်သဖြင့်ပင်ဖြစ်သည်။ ဤအခန်းတွင် recovery ဆိုသည်မှာ "runtime အမှားတွေ့ပြီးနောက် အခြေအနေကိုပြန်စစ်၍ ဆက်လုပ်နိုင်သောလမ်းကိုရှာခြင်း" ဟုပဲဖတ်ပါ။

Agent conversation တစ်ခုသည် အချိန်ကြာလာလျှင် ရှင်းလင်းမှုလျော့လာတတ်သည်။ User instruction, file path, old tool output, error message, plan, test result, old summary, new request တို့ရောထွေးလာသည်။ အကုန်ထားလျှင် context window ပြည့်မည်။ အကုန်ဖျက်လျှင် memory ပျောက်မည်။ Summary လုပ်သော်လည်း latest user message ကိုမမှတ်နိုင်လျှင် agent သည် ယနေ့အလုပ်မလုပ်ဘဲ မနေ့ကအလုပ်ဆက်လုပ်သွားနိုင်သည်။

appv22 ၏ `compaction/compressor.py` သည် ထိုပြဿနာကိုနှစ်ဆင့်ဖြင့်ကိုင်ရန်ကြိုးစားသည်။ ပထမဆင့်မှာ deterministic pruning ဖြစ်သည်။ Duplicate tool output များကိုလျှော့ပစ်သည်။ အလွန်ကြီးသော tool result များချုံ့သည်။ Image payload များကို token budget အတွက်ထိန်းထားသည်။ Huge tool-call args များကို truncate လုပ်လိုက်သည်။

ဒုတိယဆင့်မှာ LLM summary compaction ဖြစ်သည်။ History ကို structured summary အဖြစ်ပြန်ရေးသည်။ Latest user message ကို active truth အဖြစ်ထားသည်။ Secrets/tokens များကို redact လုပ်သည်။ Summary marker များဖြင့် old context ကို reference-only ဖြစ်စေရန်ကြိုးစားသည်။

ဤနေရာတွင် သတိထားရမည့်အချက်မှာ summary သည်ကယ်တင်ရှင်မဟုတ်ခြင်းဖြစ်သည်။ Summary မှားလျှင် runtime ကိုလမ်းလွဲစေသည်။ Old task ကို active task အဖြစ်ရေးမိလျှင် agent သည် user ၏နောက်ဆုံးအမိန့်ကိုမလိုက်တော့။ Secret ပါသွားလျှင် safety ပြဿနာဖြစ်သည်။ ထို့ကြောင့် appv22 ထဲတွင် `SUMMARY_PREFIX` သည် latest user message wins ဟူသော guardrail ကိုထည့်ထားပြီး persistent memory ကို authority အဖြစ်ခွဲရန်ကြိုးစားထားသည်။

သို့သော် prefix တစ်ခုရေးထားခြင်းဖြင့် အရာရာလုံခြုံသွားသည်ဟု မယူသင့်ချေ။ Compaction သည် prompt trick မဟုတ်။ Runtime behavior ဖြစ်သည်။ Test, cooldown, fallback, bounded retry များဖြင့်စစ်ရသောအရာဖြစ်သည်။

### appv22 ထဲတွင် အမှန်တကယ်ချိတ်ထားသောနေရာ

`app.py` ထဲမှ `CodingApp` ကိုဖတ်လျှင် appv22 ၏အဓိကချိတ်ဆက်ရာကိုမြင်နိုင်သည်။ `AgentSession`, `ContextCompressor`, `CompactionManager`, model/provider config, TUI renderer, tool definitions တို့ကို ဤနေရာတွင်ပေါင်းထားသည်။

ဤနေရာကို "structure flow" အဖြစ်သာဖတ်လျှင် ဘာမှထူးမည်မဟုတ်ချေ။ စာဖတ်သူအနေဖြင့် "model call တစ်ခုကို runtime ကဘယ်နေရာတွေမှာဝင်စစ်သလဲ" ဟုပြန်ဖတ်သင့်သည်။

`CodingApp.run_turn()` တွင် prompt ကို model ထံပို့ပြီးအဖြေယူရုံမဟုတ်။ Prompt မပို့မီ output-cap recovery ကိုစစ်သည်။ Context overflow recovery ကိုစစ်သည်။ Failed turn context ကို compact လုပ်ရန်လိုမလိုစစ်သည်။ Prompt run ပြီးနောက် post-response compaction လိုမလိုထပ်ကြည့်သည်။ Provider error ထွက်လာလျှင် ထို error message ကို context ထဲတွင်ထားသင့်သလား, ဖယ်ပြီး compact-and-retry လုပ်သင့်သလား စဉ်းစားသည်။

ဤသည်မှာ appv22 ၏အရေးကြီးသောစမ်းသပ်ချက်ဖြစ်သည်။ Runtime သည် model call ကိုပတ်ထားသောအပြင်အဆင်မဟုတ်။ Model call မတိုင်မီ, model call နောက်ပိုင်း, failure ဖြစ်ပြီးနောက်, next turn မတိုင်မီ state ကိုပြန်ကြည့်သောစနစ်ဖြစ်သည်။

Beginner များအတွက် provider ဟူသောစကားလုံးကိုလည်း ရိုးရိုးဖတ်ပါ။ Provider ဆိုသည်မှာ model ကိုအမှန်တကယ်ခေါ်ပေးသော service boundary ဖြစ်သည်။ OpenAI-compatible endpoint ဖြစ်နိုင်သည်။ OpenRouter ဖြစ်နိုင်သည်။ Test အတွက် faux provider ဖြစ်နိုင်သည်။ appv22 သည် real API မခေါ်ဘဲ test လုပ်နိုင်ရန် faux provider tests များကိုထားထားသည်။ Agent runtime တစ်ခုသည် API key မရှိလျှင် test မလုပ်နိုင်သောအခြေအနေသို့ မရောက်သင့်ချေ။

Provider error များသည်တစ်မျိုးတည်းမဟုတ်။ Context overflow ဖြစ်နိုင်သည်။ Output cap ဖြစ်နိုင်သည်။ Rate limit ဖြစ်နိုင်သည်။ Auth error ဖြစ်နိုင်သည်။ Stream ပြတ်နိုင်သည်။ `ai/overflow.py` သည် error text များထဲမှ context overflow နှင့် output-token cap ကိုခွဲဖတ်ရန်ကြိုးစားထားသည်။ ဤသည်မှာ "error ဖြစ်လျှင် retry" ဟူသောရိုးရိုးစိတ်ကူးထက်ပိုကောင်းသောအရာဖြစ်သည်။

Retry ဆိုသည်မှာ "ထပ်လုပ်ကြည့်" မဟုတ်။ Error ဖြစ်စေသောအကြောင်းရင်းကိုနည်းနည်းဖြစ်စေပြင်ပြီးမှ ထပ်လုပ်ခြင်းဖြစ်သည်။ Context overflow ဖြစ်နေရာတွင် context မလျှော့ဘဲ retry လုပ်လျှင် အမှားကိုဒုတိယအကြိမ်ပြန်လုပ်ခြင်းသာဖြစ်သည်။

### Tool loop ကို prompt ဖြင့်သာမထိန်းသင့်ချေ

Agent တစ်ခုသည်တစ်ခါတစ်ရံ file တစ်ခုကိုဖတ်သည်။ မတွေ့။ နောက်တစ်ခါထပ်ဖတ်သည်။ မတွေ့။ `grep` လုပ်သည်။ မတွေ့။ နောက်တစ်ဖန် `grep` လုပ်သည်။ အလုပ်မတိုးသော်လည်း token ကုန်သည်။ User အချိန်ကုန်သည်။ Runtime အပေါ်တွင် Trust လျော့လာသည်။

ဤပြဿနာကို prompt ထဲတွင် "မပတ်ပါနှင့်" ဟုရေးထားရုံဖြင့်မလုံလောက်ချေ။ appv22 ၏ `agent/tool_guardrails.py` သည် tool call များကို runtime အဆင့်တွင်ကြည့်ရန်ကြိုးစားထားသည်။ Tool name နှင့် canonical args မှ stable signature ထုတ်သည်။ Result hash ကိုကြည့်သည်။ Same failure count, no-progress count များကိုတွက်သည်။ ထို့နောက် allow, warn, block, halt စသော decision များထုတ်နိုင်ရန်ကြိုးစားသည်။

အရေးကြီးသောခွဲခြားချက်တစ်ခုမှာ idempotent tool နှင့် mutating tool ဖြစ်သည်။ `read`, `grep`, `find`, `ls` ကဲ့သို့ read-style tools များသည် ထပ်ခေါ်လျှင် အန္တရာယ်နည်းနိုင်သည်။ `write`, `edit`, `browser_click`, `send_message` ကဲ့သို့ mutation ပါသော tools များသည် ထပ်ခါထပ်ခါလုပ်လျှင် အန္တရာယ်များနိုင်သည်။ ထို့ကြောင့် tool guardrail သည် moral advice မဟုတ်။ Runtime policy ဖြစ်သင့်သည်။

သို့သော် recovery audit အရ tool-loop guardrails သည် partial/risky area ဖြစ်နေသေးသည်။ ထို့ကြောင့် appv22 သည် "loop problem solved" မဟုတ်ချေ၊ appv22 သည် no-progress tool loop ပြဿနာကို runtime guardrail အဖြစ်စမ်းသပ်စဲပင်ရှိသေသည်။ 

### Context ကို ဘယ်အချိန်တွင်ချုံ့မလဲ

Context compaction တွင် "ချုံ့နိုင်သလား" ဟူသောမေးခွန်းထက် "ဘယ်အချိန်တွင်ချုံ့သင့်သလဲ" ဟူသောမေးခွန်းကပိုအရေးကြီးတတ်သည်။ အချိန်မမှန်လျှင် context ကောင်းကောင်းရှိနေရာမှ မလိုအပ်ဘဲ summary လုပ်မိနိုင်သည်။ နောက်ကျလွန်းလျှင် provider က context overflow ဖြင့်ငြင်းနိုင်သည်။

`compaction/timing.py` သည် preflight, post-response, overflow, manual စသောလမ်းကြောင်းများကိုခွဲထားသည်။ Preflight သည် model call မတိုင်မီ rough token estimate ဖြင့်စစ်ခြင်းဖြစ်သည်။ Post-response သည် provider usage သိပြီးနောက် next turn အတွက်စဉ်းစားခြင်းဖြစ်သည်။ Overflow သည် provider က context too large ဟုငြင်းလျှင် bounded recovery လုပ်ခြင်းဖြစ်သည်။ Manual သည် user/operator က `/compress` ခေါ်သောအခါဖြစ်သည်။

`tests/test_compaction_timing.py` တွင် immediate second compaction မလုပ်ခြင်း, real usage သိပြီးနောက် preflight ကိုခဏရွှေ့ခြင်း, overflow recovery bounded ဖြစ်ခြင်း စသော behavior များကိုစစ်ရင်ရေးထားသည်။ Recovery audit ထဲတွင် redundant compaction rewrite issue တစ်ခုကို fix လုပ်ထားသည်။

ဤနေရာမှစာဖတ်သူယူသင့်သောသင်ခန်းစာမှာ "summary ထုတ်နိုင်သည်" ဟူသော feature list မဟုတ်။ Summary ထုတ်သည့်အချိန်, summary ထပ် rewrite မဖြစ်စေရန်, summary မအောင်မြင်လျှင် fallback ဘယ်လိုလုပ်မလဲ, already-compacted transcript ကိုဘယ်လိုကိုင်မလဲ စသောအရာများက runtime quality ကိုဆုံးဖြတ်သည်။

### Session နှင့် TUI ကို မလှပစေရန်သာမဟုတ်၊ မြင်နိုင်စေရန်ရေးသည်

Coding agent တစ်ခုသည် answer box တစ်ခုတည်းမဟုတ်။ User သည် agent ကဘာဖတ်နေသလဲ, ဘာ tool ခေါ်နေသလဲ, ဘယ် model ကိုသုံးနေသလဲ, compaction ဖြစ်နေသလား, retry ဖြစ်နေသလား, abort လုပ်နိုင်သလား ဆိုသည်တို့ကိုမြင်ချင်သည်။ မမြင်ရလျှင် runtime ကိုယုံရခက်သည်။

`coding_agent/agent_session.py` သည် session, active tools, model cycling, compaction events, auto retry, branch summary, session store စသောအရာများစွာကိုကိုင်ထားသည်။ Recovery audit က ဤ file ကို mixed responsibility risk ရှိသည်ဟုမှတ်ထားသည်။ ထိုသတိပေးချက်သည် အရေးကြီးသည်။ File တစ်ခုထဲတွင်တာဝန်များအလွန်များလာလျှင် bug ရှာရခက်လာသည်။

`tui/` folder သည် terminal input, rendering, keybindings, status, image handling, interactive mode စသော Pi-style terminal idea များကိုယူထားသည်။ သို့သော် recovery audit က TUI runtime controls ကို partial/broken risk ဟုသတိပေးထားသည်။ ထို့ကြောင့် TUI ကိုပြီးပြည့်စုံသော UI အဖြစ်မရေးသင့်ချေ။ Agent runtime ကို user မြင်နိုင်စေရန်ကြိုးစားထားသောအပိုင်းဖြစ်သော်လည်း stabilization လိုနေသေးသောနေရာဖြစ်သည်။

### Inspiration နှင့် dependency ကို မရောသင့်ချေ

appv22 README က reference copies of upstream `hermes-agent/` and `pi/` codebases are not runtime dependencies ဟုရှင်းပြထားသည်။ Recovery audit ၏ kill list ထဲတွင် reference repos `pi/` နှင့် `hermes-agent/` ကို runtime dependencies အဖြစ်မသုံးရန်ထည့်ထားသည်။ `test_no_appv21_coupling.py` ကလည်း appv21/appV2.1 coupling မကျန်စေရန်စစ်ထားသည်။

ဤအချက်သည် beginner များအတွက်လည်းတန်ဖိုးရှိသည်။ Inspiration နှင့် dependency မတူ။ Port လုပ်ခြင်းနှင့် blind copy မတူ။ Design idea တစ်ခုဘယ်ကလာသလဲသိရန်လိုသလို, လက်ရှိ runtime ကဘယ်အရာပေါ်မူတည်နေသလဲကိုလည်းရှင်းရမည်။

အကယ်၍ appv22 သည် Pi/Hermes folder များကို runtime ထဲမှတိုက်ရိုက် import လုပ်နေခဲ့လျှင် boundary မသန့်တော့။ စမ်းသပ် project တစ်ခုဖြစ်သော်လည်း ထို boundary ကို test ဖြင့်စစ်ထားခြင်းကောင်းသည်။ အကြောင်းမှာ agent runtime တစ်ခုတွင် "ဘယ်အရာက source of truth လဲ" ဟူသောမေးခွန်းသည် အမြဲအရေးကြီးသောကြောင့်ဖြစ်သည်။

### OpenClaw hype ကို ဘယ်လိုဖတ်မလဲ

Agent ecosystem တွင် project အသစ်တစ်ခုထွက်တိုင်း hype တက်တတ်သည်။ OpenClaw ကဲ့သို့သော project/article များတွင် local gateway, skills, personal assistant, browser/computer control, security risk စသောစကားလုံးများမြင်ရတတ်သည်။ ထိုအချိန်တွင် developer တစ်ယောက်၏အလုပ်မှာ social media စကားစစ်ထိုးရန်မဟုတ်။ Architecture ကိုဖတ်ရန်ဖြစ်သည်။

မေးခွန်းများကိုရိုးရိုးထားပါ။ Loop ရှိသလား။ Tool broker ရှိသလား။ Skill loader ရှိသလား။ Memory/session ရှိသလား။ Context compaction ရှိသလား။ Provider boundary ရှိသလား။ Safety guardrail ရှိသလား။ User-facing runtime status ရှိသလား။

Pi official site သည် OpenClaw ကို SDK real-world integration example အဖြစ် link ထားသည်။ ထို့အပြင် OpenClaw ၏ `THIRD_PARTY_NOTICES.md` တွင် OpenClaw ၏ implementation portions အချို့ကို Pi/pi-mono မှ adapted လုပ်ထားကြောင်းနှင့် `@earendil-works/pi-tui` ကို terminal UI rendering အတွက် depend လုပ်ထားကြောင်း ဖော်ပြထားသည်။

ထို့ကြောင့် OpenClaw ကို Pi ecosystem နှင့်လုံးဝမဆိုင်သကဲ့သို့ဖတ်ခြင်းမမှန်။ သို့သော် "OpenClaw သည် Pi ပဲ" ဟုလည်းမချုပ်သင့်ချေ။ မှန်ကန်သောဖတ်နည်းမှာ OpenClaw သည် Pi/pi-mono မှအချို့ implementation idea/code portions များကိုယူထားပြီး Pi TUI package ကိုအသုံးပြုထားသော broader personal-agent runtime တစ်ခုဟုဖတ်ခြင်းဖြစ်သည်။

Hype ကိုပယ်ရန်မဟုတ်။ Hype ကို code-reading habit အဖြစ်ပြောင်းရန်ဖြစ်သည်။

### appv22 က စာဖတ်သူကို ဘာသင်ပေးသလဲ

ပထမသင်ခန်းစာမှာ loop သည်အစသာဖြစ်ခြင်းဖြစ်သည်။ Loop ထဲတွင် event, tool execution, stop condition, iteration budget, steering/follow-up message များပါလာမှ user-facing agent ဖြစ်လာသည်။

ဒုတိယသင်ခန်းစာမှာ provider boundary ကိုသီးခြားစဉ်းစားရခြင်းဖြစ်သည်။ Model API သည်အမြဲမမှန်။ Error text ကိုခွဲဖတ်ရသည်။ Faux provider ဖြင့် network/API key မလိုသော tests ရှိသင့်သည်။

တတိယသင်ခန်းစာမှာ context compaction သည် summary feature မဟုတ်ခြင်းဖြစ်သည်။ Deterministic pruning, LLM summary, secret redaction, latest-message priority, cooldown, bounded retry တို့ပါသော runtime behavior ဖြစ်သည်။

စတုတ္ထသင်ခန်းစာမှာ tool-loop guardrail သည် prompt advice မဟုတ်ခြင်းဖြစ်သည်။ Tool signature, result hash, idempotent/mutating distinction, allow/warn/block/halt decision များလိုသည်။

ပဉ္စမသင်ခန်းစာမှာ TUI သည်အလှဆင်မဟုတ်ခြင်းဖြစ်သည်။ Agent ဘာလုပ်နေသည်ကို user မမြင်လျှင် trust မတည်ဆောက်နိုင်။ သို့သော် TUI သည်ကျယ်သောအပိုင်းဖြစ်သောကြောင့် မတည်ငြိမ်သေးသောနေရာကို overclaim မလုပ်သင့်ချေ။

နောက်ဆုံးသင်ခန်းစာမှာ recovery audit သည်ရှုံးနိမ့်ချက်စာရင်းမဟုတ်ခြင်းဖြစ်သည်။ Gap map, kill list, NEXT_PATCH plan များသည် project ကိုအမှန်အတိုင်းမြင်စေသော engineering discipline ဖြစ်သည်။

### စာဖတ်သူကိုယ်တိုင် ဖတ်ကြည့်ရန်

ဤအခန်းပြီးလျှင် repo ကိုဖွင့်ပြီး အောက်ပါအတိုင်းဖတ်ကြည့်ပါ။

1. `README.md` ကိုဖတ်ပြီး appv22 ကို Pi x Hermes Python agent runtime ဟု repo ကဘယ်လိုဖော်ပြထားသလဲကြည့်ပါ။
2. `docs/appv22-recovery-audit.md` ကိုဖတ်ပြီး current state, gap map, kill list, NEXT_PATCH ကိုအရင်မှတ်ပါ။
3. `appV2.2/appv22/app.py` ထဲမှ `CodingApp.run_turn()` ကိုဖတ်ပါ။ Model call မတိုင်မီနှင့်နောက်ပိုင်း recovery check များကိုမှတ်ပါ။
4. `agent/agent_loop.py` ကိုဖတ်ပြီး event sequence နှင့် tool call loop ကိုဆွဲပါ။
5. `agent/tool_guardrails.py` တွင် idempotent/mutating tool lists နှင့် decision actions ကိုရှာပါ။
6. `compaction/compressor.py` တွင် deterministic pruning, summary prefix, redaction logic ကိုရှာပါ။
7. `compaction/timing.py` တွင် preflight/post-response/overflow/manual timing လမ်းကြောင်းများကိုခွဲပါ။
8. `tests/test_no_appv21_coupling.py`, `tests/test_ai_faux.py`, `tests/test_compaction_timing.py` ကိုဖတ်ပြီး appv22 သည် test ဖြင့်ဘယ် boundary များကိုစစ်ထားသလဲကြည့်ပါ။

ဤလေ့ကျင့်ခန်းများ၏ရည်ရွယ်ချက်မှာ appv22 ကိုသုံးစေရန်မဟုတ်။ Runtime တစ်ခုကို README, audit, source comment, test, entrypoint တို့ဖြင့်ဘယ်လိုဖတ်မလဲကိုလေ့ကျင့်ရန်ဖြစ်သည်။

### နိဂုံး

appv22 သည် အလွန်သစ်သော prototype recovery lab ဖြစ်သည်။ Final worker kernel မဟုတ်။ အပြီးသတ်နည်းလမ်းတစ်ခုအဖြစ်လည်း မကြေညာသင့်ချေ။ production-ready claim မလုပ်သင့်ချေ။ ဤသတိပေးချက်ကို အခန်းအစတွင်ပြောခဲ့သလို အဆုံးတွင်လည်းပြန်ပြောရခြင်းမှာ အရေးကြီးသောကြောင့်ဖြစ်သည်။

သို့သော် appv22 သည် beginner developer နှင့် engineer နှစ်မျိုးလုံးအတွက် အသုံးဝင်သောသင်ခန်းစာပေးသည်။ Agent loop ရေးခြင်းသည် ပထမခြေလှမ်းသာဖြစ်သည်။ ထို loop ကို provider boundary, tool guardrail, compaction timing, overflow recovery, session persistence, TUI, tests တို့ဖြင့်စစ်ပြီးထိန်းနိုင်မှ runtime ဟုခေါ်ထိုက်လာသည်။

ဒီအခန်းကိုဖတ်ပြီး စာဖတ်သူသည် "ငါလည်း loop တစ်ခုရေးမယ်" ဟုသာမထင်သင့်ချေ။ "ငါ့ loop က error ဖြစ်သွားလျှင် ဘယ်လိုပြန်စစ်မလဲ။ Context ပြည့်သွားလျှင် ဘယ်လိုချုံ့မလဲ။ Tool တစ်ခုတည်းကိုထပ်ခါထပ်ခါခေါ်နေလျှင် ဘယ်လိုရပ်မလဲ။ User က terminal ထဲတွင် ဘာဖြစ်နေသလဲမြင်နိုင်မလား။" ဟုမေးတတ်လာသင့်သည်။

ထိုမေးခွန်းများစမေးသောအခါ Agentic AI သည် buzzword မှ engineering သို့ကူးသွားပေသည်။

---

**စာဖတ်သူအတွက် Source Notes:**

- **GitHub source:** `https://github.com/htooayelwinict/allthebest`
- **Repo docs:** `README.md`, `docs/appv22-recovery-audit.md`
- **Core runtime files:** `appV2.2/appv22/app.py`, `appV2.2/appv22/agent/agent_loop.py`, `appV2.2/appv22/agent/tool_guardrails.py`, `appV2.2/appv22/ai/overflow.py`, `appV2.2/appv22/coding_agent/agent_session.py`, `appV2.2/appv22/compaction/compressor.py`, `appV2.2/appv22/compaction/timing.py`
- **Tests to read:** `appV2.2/tests/test_no_appv21_coupling.py`, `appV2.2/tests/test_agent_loop.py`, `appV2.2/tests/test_ai_faux.py`, `appV2.2/tests/test_ai_appv2_env_provider.py`, `appV2.2/tests/test_compaction.py`, `appV2.2/tests/test_compaction_timing.py`, `appV2.2/tests/test_tui.py`
- **Pi anchors:** `https://pi.dev`, `https://github.com/earendil-works/pi`
- **Hermes anchors:** `https://hermes-agent.org`, `https://github.com/NousResearch/hermes-agent`
- **OpenClaw/Pi context:** Pi site က OpenClaw ကို SDK integration example အဖြစ် link ထားသည်။ OpenClaw `THIRD_PARTY_NOTICES.md` က Pi/pi-mono မှ portions adapted လုပ်ထားကြောင်းနှင့် `@earendil-works/pi-tui` dependency ရှိကြောင်းဖော်ပြထားသည်။

