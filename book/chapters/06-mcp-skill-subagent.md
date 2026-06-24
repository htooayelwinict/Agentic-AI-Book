# ၀၆။ လမ်းတံတားများ၊ လက်စွဲစာအုပ်များနှင့် အငယ်စား လက်ထောက်များ

### စကားလုံးများ များလာသောအခါ မျက်စိမလည်စေရန်

Agentic AI လောကထဲသို့ဝင်လာသောအခါ စာဖတ်သူသည် စကားလုံးအသစ်များစွာဖြင့်ကြုံရပေလိမ့်မည်။ MCP, Skill, Sub-agent, Tool, Resource, Prompt, Memory, Checkpointer, Harness စသည်တို့ဖြစ်သည်။ ထိုစကားလုံးများသည် အချို့အချိန်တွင်အမှန်တကယ်အသုံးဝင်သော်လည်း၊ အချို့အချိန်တွင်လူနားမလည်အောင်ပြောသော buzzwords များလည်းဖြစ်နိုင်သည်။ ထို့ကြောင့် ဤအခန်းတွင် စကားလုံးများကိုအလွတ်ကျက်ရန်မဟုတ်၊ ၎င်းတို့ကို အင်ဂျင်နီယာမျက်စိဖြင့်ခွဲမြင်တတ်ရန်သာ ရည်ရွယ်သည်။

အလွယ်ဆုံးခွဲလျှင် -

**MCP** သည် Agent နှင့်ပြင်ပကမ္ဘာအကြား လမ်းတံတားဖြစ်သည်။

**Skill** သည် Agent အလုပ်လုပ်ရာတွင်ဖတ်ရသော လက်စွဲစာအုပ်ဖြစ်သည်။

**Sub-agent** သည် Main Agent ကအလုပ်ခွဲပေးသော အငယ်စားလက်ထောက်ဖြစ်သည်။

လမ်းတံတား၊ လက်စွဲစာအုပ်၊ လက်ထောက်။ ဤသုံးခုကိုမရောပါနှင့်။ လမ်းတံတားသည်ကမ္ဘာနှင့်ဆက်သည်။ လက်စွဲစာအုပ်သည်လုပ်နည်းပြသည်။ လက်ထောက်သည်တစ်စိတ်တစ်ပိုင်းအလုပ်လုပ်သည်။

### MCP — ပြင်ပကမ္ဘာသို့ ဆက်သွယ်သော လမ်းတံတား

LLM သည်အခန်းထဲတွင်ထိုင်နေသောစာရေးတော်နှင့်တူသည်။ သူသည်စာရေးတတ်သည်၊ အကြံပေးတတ်သည်၊ pattern များကိုခန့်မှန်းတတ်သည်။ သို့သော် ပြင်ပကမ္ဘာနှင့်မချိတ်ထားပါက file မဖတ်နိုင်၊ database မကြည့်နိုင်၊ GitHub issue မသိနိုင်၊ calendar မကြည့်နိုင်၊ internal docs မရှာနိုင်။ ထိုပြင်ပကမ္ဘာနှင့်ချိတ်ပေးရန် Tool များလိုသည်။ Tool များနှင့်ချိတ်ရာတွင် app တစ်ခုချင်းစီအတွက် custom integration များရေးနေရလျှင် အလွန်ရှုပ်ထွေးလာသည်။

နေ့စဉ်အလုပ်တစ်ခုနဲ့စကြည့်ပါ။ သင်သည် Agent ကို "မနက်ဖြန် team meeting အတွက် ပြင်ဆင်ပေးပါ" ဟုခိုင်းသည်ဆိုပါစို့။ Agent သည် calendar ကိုဖတ်ရမည်။ GitHub issue များကိုကြည့်ရမည်။ Project docs ထဲက milestone ကိုရှာရမည်။ Meeting note template တစ်ခုယူရမည်။ အရာတိုင်းအတွက် integration အသစ်ရေးနေရလျှင် Agent တစ်ခုတည်ဆောက်ခြင်းထက်တံတားဆောက်ခြင်းကအချိန်ပိုကုန်သွားမည်။ MCP သည်ထိုတံတားများကိုစည်းကမ်းတစ်ခုအောက်တွင်ချိတ်ပေးရန်ကြိုးစားသောနည်းဖြစ်သည်။

**MCP (Model Context Protocol)** သည် ထိုပြဿနာကိုဖြေရှင်းရန်ပေါ်လာသော standard connection ဖြစ်သည်။ MCP server တစ်ခုသည် "ငါ့ဆီမှာ Tool တွေရှိတယ်၊ Resource တွေရှိတယ်၊ Prompt template တွေရှိတယ်၊ ဒီ schema အတိုင်းခေါ်ပါ" ဟုပြောသော service ဖြစ်သည်။ Agent host ဘက်တွင် MCP client ရှိပြီး၊ model နှင့် MCP server အကြားတံတားဖြစ်သည်။

```text
Agent Host
   |
   v
MCP Client
   |
   v
MCP Server
   |
   +-- Tool: search_docs(query)
   +-- Resource: project://README.md
   +-- Prompt: incident_report_template
```

ဤနေရာတွင်အရေးကြီးသောအချက်မှာ MCP သည် Agent ကိုယ်တိုင်မဟုတ်ခြင်းဖြစ်သည်။ MCP သည် Agent အတွက်လုပ်နိုင်စွမ်းဆီသို့သွားသောတံတားဖြစ်သည်။ တံတားရှိလာသည်နှင့်တံခါးစောင့်လည်းလိုလာသည်။ Permission, authentication, output sanitization, audit log များသည် "နောက်မှထည့်မယ်" ဆိုသောအပိုပစ္စည်းများမဟုတ်တော့။

### Tool, Resource, Prompt မရောစေရန်

MCP တွင် **Tool**, **Resource**, **Prompt** ဟူသောအရာများကိုခွဲမြင်ရမည်။

Tool သည် လုပ်ဆောင်ချက်ဖြစ်သည်။ Search လုပ်နိုင်သည်၊ ticket ဖန်တီးနိုင်သည်၊ file write လုပ်နိုင်သည်၊ API call လုပ်နိုင်သည်။ Tool သည် side effect ရှိနိုင်သောကြောင့်အန္တရာယ်ရှိသည်။

Resource သည်ဖတ်စရာအချက်အလက်ဖြစ်သည်။ File content, document, database row, log snippet စသည်တို့ဖြစ်နိုင်သည်။ Resource သည် read-only ဖြစ်နိုင်သော်လည်း privacy risk ရှိသည်။

Prompt သည်လုပ်နည်းညွှန်ကြားချက်ဖြစ်သည်။ Incident report template, code review checklist, support reply style စသည်တို့ဖြစ်နိုင်သည်။ Prompt သည် Tool မဟုတ်သော်လည်း model behavior ကိုပြောင်းနိုင်သောကြောင့် trusted source ဖြစ်ရန်လိုသည်။

အလွယ်မှတ်ရန် -

```text
Tool     = လုပ်
Resource = ဖတ်
Prompt   = ဘယ်လိုလုပ်
```

ဤသုံးခုကိုရောသွားလျှင် security boundary ပျက်သည်။ Webpage content သည် Resource ဖြစ်သည်။ ၎င်းထဲတွင် "previous instruction မလိုက်နာပါနှင့်" ဟုရေးထားလျှင်လည်း Prompt မဟုတ်။ Data သာဖြစ်သည်။

### Skill — စာရေးတော်အတွက် လက်စွဲစာအုပ်

Skill ဟူသည် Agent အတွက် domain-specific လက်စွဲစာအုပ်ဖြစ်သည်။ Agent ကိုအရာအားလုံးအမြဲမှတ်ထားစေရန်မကြိုးစားဘဲ၊ လိုအပ်သောအချိန်မှ `SKILL.md` ကဲ့သို့သော file ကိုဖတ်စေခြင်းဖြစ်သည်။ Cook တစ်ယောက်သည် ဟင်းချက်တိုင်း recipe book အုပ်လုံးကိုမဖတ်။ လိုသော recipe ကိုဖတ်သည်။ Agent တွင်လည်း ထိုသဘောပင်။

Skill ထဲတွင် tool အသုံးပြုနည်း၊ workflow step, domain convention, safety warning, example များပါနိုင်သည်။ Travis-2 တွင် SkillsMiddleware သည် skill root မှ `skills/<name>/SKILL.md` ဖိုင်များကိုဖတ်ပြီး model context ထဲထည့်ပေးသည်။ Playwright task အတွက် Playwright skill, websearch task အတွက် websearch skill စသည်ဖြင့် model ကိုအလုပ်လုပ်နည်းပြနိုင်သည်။

သို့သော် Skill သည် documentation သက်သက်မဟုတ်။ Skill သည် instruction source ဖြစ်သည်။ မကောင်းသောလက်စွဲစာအုပ်တစ်အုပ်သည်လက်သမားကိုအတိုင်းအတာမှားတိုင်းစေနိုင်သကဲ့သို့ malicious skill တစ်ခုသည် Agent ကိုလမ်းလွဲစေနိုင်သည်။ ထို့ကြောင့် Skill loading တွင် "ဖိုင်ရှိတယ်ဆို၍ဖတ်မယ်" ဟုမလုပ်သင့်ချေ။ ဘယ် directory မှလာသနည်း၊ trusted လား၊ signature ကိုဘယ်လိုစစ်မလဲ၊ workspace skill က global skill ကို override လုပ်ခွင့်ရှိသလား၊ mismatch ဖြစ်လျှင် fail-closed လုပ်မလားဆိုသောဆုံးဖြတ်ချက်များလိုသည်။

### AGENTS.md နှင့် SKILL.md ကို Context Window ထဲတွင် ဘာကြောင့် ထိန်းသိမ်းရသနည်း

Coding Agent များတွင် `AGENTS.md` သို့မဟုတ် `SKILL.md` ကဲ့သို့သော file များကိုမကြာခဏတွေ့ရသည်။ Beginner များသည် ထိုဖိုင်များကို README ကဲ့သို့သာထင်တတ်ကြသည်။ အမှန်တွင် ထိုဖိုင်များသည် Agent အတွက် "အလုပ်ခွင်စည်းကမ်းစာအုပ်" ဖြစ်သည်။

`AGENTS.md` တွင် project အတွင်း agent လုပ်ရမည့်စည်းကမ်းများပါနိုင်သည်။ ဘယ် command run ရမည်၊ ဘယ် file မထိသင့်၊ ဘယ် style သုံးရမည်၊ test ဘယ်လို run ရမည်၊ secret မထုတ်သင့် စသည်တို့ပါနိုင်သည်။ `SKILL.md` တွင် task-specific workflow, tool usage, domain rule, safety instruction များပါနိုင်သည်။

Agent context window သည် ကပ္ပတိန်၏စားပွဲပေါ်ရှိလက်ရှိမြေပုံနှင့်တူသည်။ ထိုစားပွဲပေါ်မှ `AGENTS.md` နှင့် `SKILL.md` ကိုဖယ်လိုက်ပါက Agent သည် project စည်းကမ်းကိုမေ့သွားနိုင်သည်။ Compaction လုပ်ရာတွင်လည်း ထိုဖိုင်များ၏အရေးကြီးသော instruction များကိုထိန်းသိမ်းရန်လိုသည်။ အဘယ်ကြောင့်ဆိုသော် Agent သည်အလုပ်လုပ်နေစဉ် "ဘယ်အရာကိုမလုပ်သင့်ချေ" ဆိုသောစည်းကမ်းများကိုမေ့သွားပါက Tool ကိုမှားသုံးနိုင်သောကြောင့်ဖြစ်သည်။

သို့သော် `AGENTS.md` နှင့် `SKILL.md` ကိုအမြဲအပြည့်ထည့်ထားရမည်ဟုမဆိုလို။ Context window သည်အကန့်အသတ်ရှိသည်။ ထို့ကြောင့် အရေးကြီးသော rule များကို priority ပေး၍ထည့်ရမည်။ Large skill file များကိုလိုအပ်သောအချိန်မှဖတ်စေခြင်းကပိုကောင်းနိုင်သည်။ အရေးကြီးသောအချက်မှာ ထိုဖိုင်များသည် "စာရွက်စာတမ်း" မဟုတ်ဘဲ "runtime instruction source" ဖြစ်ကြောင်းသိထားရန်ဖြစ်သည်။

### Sub-agent — အလုပ်ခွဲပေးသော အငယ်စားလက်ထောက်

Sub-agent ဆိုသည်မှာ Main Agent မှတာဝန်ခွဲပေးသော Worker Agent ဖြစ်သည်။ Main Agent သည် project တစ်ခုလုံးကိုကိုင်ထားပြီး၊ Sub-agent ကို "ဒီ folder ကိုဖတ်ပြီး summary ထုတ်ပေးပါ" သို့မဟုတ် "ဒီ error ကိုရှာပေးပါ" ဟုတာဝန်ခွဲနိုင်သည်။ Sub-agent သည် fresh context ဖြင့်စနိုင်သည်။ Tool scope ကိုခွဲထားနိုင်သည်။ Output format ကို contract ချထားနိုင်သည်။

သို့သော် Sub-agent များများသုံးခြင်းသည် architecture ကောင်းသည်ဟုမဆိုလို။ လက်ထောက်များများရှိသော်လည်း အားလုံးကိုတစ်ပြိုင်နက်အမိန့်မှားပေးလျှင် အလုပ်ရုံတစ်ခုလုံးရှုပ်ထွေးသွားမည်။ Sub-agent တစ်ခုစီတွင် context boundary, tool boundary, budget, timeout, output contract, verifier လိုသည်။

P-2 ၏ Bridge lesson သည် Sub-agent design တွင်အလွန်အသုံးဝင်သည်။ Supervisor သည် Customer Agent ကို full state မပေး။ Minimum instruction သာပေးသည်။ Sub-agent များကိုလည်း parent state အကုန်မပေးသင့်။ Task အတွက်လိုသော context သာ project လုပ်သင့်သည်။

BrowserSurfer တွင် PlanningAgent နှင့် ReflectionAgent တို့သည် Sub-agent thinking ကိုသင်ပေးသည်။ PlanningAgent သည် past trajectory များကိုကြည့်၍ plan ထုတ်သည်။ ReflectionAgent သည် run ပြီးနောက် critique ထုတ်သည်။ သို့သော် output ကို truth အဖြစ်မယုံရ။ Verifier ဖြင့်ပြန်စစ်ရမည်။

### OpenClaw နှင့် Skill Hype ကို ခပ်အေးအေးဖတ်ကြည့်ခြင်း

ယနေ့ခေတ်တွင် OpenClaw ကဲ့သို့သော self-hosted agent system များအကြောင်း hype များစွာရှိသည်။ Messaging interface, local gateway, skills library, broad integrations စသည့်စကားလုံးများကြားရသည်။ လူအများက "Agent ကို message ပို့လိုက်ရုံဖြင့်အလုပ်လုပ်သွားပြီ" ဟုစိတ်လှုပ်ရှားကြသည်။ သို့သော်အင်ဂျင်နီယာတစ်ယောက်အနေဖြင့် hype ကို feature list အဖြစ်မဖတ်ပါနှင့်။ Boundary list အဖြစ်ဖတ်ပါ။

Skill များများရှိသည်ဆိုလျှင် မေးပါ — ထို Skill များကိုဘယ်သူရေးသနည်း။ Trusted လား။ Permission ဘယ်လောက်ရသလဲ။ Sandbox ရှိသလား။ Malicious instruction ပါလာနိုင်သလား။ Agent ကို message မှခိုင်းနိုင်သည်ဆိုလျှင် မေးပါ — command source ကိုဘယ်လို authenticate လုပ်သနည်း။ Broad integrations ရှိသည်ဆိုလျှင် မေးပါ — credentials ကိုဘယ်လို scope လုပ်ထားသနည်း။

အချို့ online discussion များတွင် OpenClaw-like systems များကို Pi-style loop, TUI, provider abstraction pattern များနှင့်နှိုင်းတတ်ကြသည်။ သို့သော် source-level evidence မရှိလျှင် "OpenClaw သည် Pi ပဲ" ဟုအမှန်တရားအဖြစ်မရေးသင့်။ ဤစာအုပ်တွင်ထိုအရာကို hype-reading fun fact အဖြစ်သာသုံးမည်။ Pattern တူနိုင်သည်။ Direct lineage ကိုတော့ source ဖြင့်သာအတည်ပြုရမည်။ [SOURCE_NEEDED]

### နိဂုံး - လမ်း၊ စာအုပ်၊ လက်ထောက်

MCP သည်လမ်းတံတားဖြစ်သည်။ Skill သည်လက်စွဲစာအုပ်ဖြစ်သည်။ Sub-agent သည်အငယ်စားလက်ထောက်ဖြစ်သည်။ သုံးခုလုံးသည် Agent ကိုပိုစွမ်းအားမြင့်စေသည်။ သို့သော် သုံးခုလုံးသည် trust boundary မရှိပါကအန္တရာယ်တိုးစေသည်။

စာဖတ်သူအနေဖြင့် နာမည်များကိုအလွတ်ကျက်ရန်မလို။ မေးခွန်းသုံးခုကိုသာအမြဲမေးပါ။ "ဒီအရာက Agent ကို ဘာလုပ်ခွင့်ပေးသလဲ"။ "ဒီအရာက Agent ကို ဘာဖတ်ခွင့်ပေးသလဲ"။ "ဒီအရာက Agent ကို ဘာကိုမှတ်ထားစေသလဲ"။ ထိုမေးခွန်းများမေးတတ်လာလျှင် MCP, Skill, Sub-agent တို့သည်buzzwords မဟုတ်တော့ဘဲ အင်ဂျင်နီယာကိရိယာများဖြစ်လာလိမ့်မည်။

---

**စာဖတ်သူအတွက် Source Notes:**

- **MCP:** Tool, Resource, Prompt များကို AI application ထံ expose လုပ်ရန်သုံးသော standard interface ဖြစ်သည်။
- **Tool / Resource / Prompt:** Tool သည် action ဖြစ်သည်။ Resource သည်ဖတ်ရန် context ဖြစ်သည်။ Prompt သည်ပြန်သုံးနိုင်သော instruction ဖြစ်သည်။
- **Skill:** `SKILL.md` နှင့် supporting files များပါသော workflow လက်စွဲစာအုပ်တစ်မျိုးအဖြစ်ဖတ်နိုင်သည်။
- **AGENTS.md:** Coding agent အတွက် project-level အလုပ်ခွင်စည်းကမ်းဖြစ်သည်။ Compaction လုပ်သော်လည်းအရေးကြီးသော rule များကိုထိန်းသိမ်းသင့်သည်။
- **Sub-agent:** ကိုယ်ပိုင် context, tools, budget, output contract ရှိသော delegated worker ဖြစ်သည်။
- **OpenClaw/Pi lineage:** Source-level evidence မရသေးသရွေ့ hype/context အဖြစ်သာဖတ်ရန်ဖြစ်သည်။
