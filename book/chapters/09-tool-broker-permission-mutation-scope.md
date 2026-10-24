# 09-tool-broker-permission-mutation-scope

### လူမိုက်အား ဓားမအပ်မိစေရန်

အခန်း ၀၃ တွင် Tool Calling ကို စာရေးတော်၏လက်များဟုပြောခဲ့သည်။ လက်ရှိလာပြီဆိုလျှင် အလုပ်လုပ်နိုင်သည်။ သို့သော်လက်ရှိလာသည်နှင့်အန္တရာယ်လည်းလာသည်။ စာရေးတော်သည် စာရေးရုံမဟုတ်တော့။ File ဖတ်နိုင်သည်၊ file ပြင်နိုင်သည်၊ browser ဖွင့်နိုင်သည်၊ command run နိုင်သည်၊ ticket ပိတ်နိုင်သည်၊ deployment စတင်နိုင်သည်။

ထိုအချိန်မှစ၍ Agent design သည် "model ဘယ်လောက်တော်သလဲ" ဆိုသောမေးခွန်းတစ်ခုတည်းမဟုတ်တော့ပေ။ "ဤစာရေးတော်ကိုဘယ်လက်နက်ပေးမလဲ" ဆိုသောမေးခွန်းဖြစ်လာသည်။

Tool Broker ဆိုသည်မှာ Agent နှင့် Tool များကြားတွင်ထိုင်သောလက်နက်တိုက်စောင့်ဖြစ်သည်။ Agent က "ဓားပေးပါ" ဟုပြောတိုင်းဓားမပေးရ။ "မင်းဘယ်သူလဲ၊ ဘာလုပ်မလဲ၊ ဒီအလုပ်အတွက်ဓားလိုသလား၊ သစ်ခုတ်ရန်လား လူခုတ်ရန်လား" ဟုမေးရသည်။

### Permission သည် စာချုပ်ဖြစ်သည်

Beginner များသည် permission ကို "Agent ကိုယုံ/မယုံ" အဖြစ်တွေးတတ်သည်။ အမှန်မှာ permission သည်ယုံကြည်မှုမဟုတ်။ Contract ဖြစ်သည်။ Agent တစ်ခုသည် read-only tool သုံးခွင့် ရှိနိုင်သော်လည်း write tool သုံးခွင့် မရှိနိုင်။ Browser navigate လုပ်ခွင့် ရှိနိုင်သော်လည်း form submit ခွင့်နှင့် shell command run ခွင့် မရှိနိုင်။

Permission ကိုသုံးမျိုးခွဲစဉ်းစားနိုင်သည်။

```text
Read scope      -> ဘာကိုဖတ်နိုင်သလဲ
Action scope    -> ဘာလုပ်နိုင်သလဲ
Mutation scope  -> ဘာကိုပြောင်းလဲနိုင်သလဲ
```

Read scope ကိုလည်း ခွဲထားရသည်။ Secret file ကိုဖတ်ခွင့်ရှိလျှင် Agent သည်မရေးသော်လည်း leak ဖြစ်နိုင်သည်။ Action scope သည် tool call ခွင့်ဖြစ်သည်။ Mutation scope သည် system state ပြောင်းခွင့်ဖြစ်သည်။ Mutation သည် database update, file write, message send, browser click, cloud resource create စသည်တို့ဖြစ်နိုင်သည်။

ဤသုံးခုကိုမခွဲဘဲ "agent has tools" ဟုပြောခြင်းသည်အလွန်မတိကျသောစကားဖြစ်သည်။ Hammer, scalpel, gun အားလုံးကို "tool" ဟုခေါ်နိုင်သည်။ သို့သော်အသုံးပြုခွင့်သည်တူမည်မဟုတ်။

### Tool Broker

Tool Broker သည် လက်နက်တိုက်စောင့် ဖြစ်သည်။ သူသည် tool registry ကို သိသည်၊ tool တစ်ခုစီ၏ schema နှင့် လိုအပ်သော argument ကို သိသည်၊ side effect ရှိ/မရှိ နှင့် human approval လို/မလို ကို သိသည်၊ tool output ကို ဘယ်လို sanitize လုပ်ရမလဲ သိသည်။

```text
Agent proposes tool call
   |
   v
Tool Broker checks:
  - identity / role
  - permission
  - argument schema
  - mutation risk
  - approval policy
  - audit logging
   |
   v
Tool executes or is rejected
```

BrowserSurfer တွင် ToolRegistry / ToolSpec / Pydantic argument schemas တို့သည် tool broker thinking ကိုမြင်စေသည်။ Tool တစ်ခုသည်နာမည်ရှိရမည်။ Argument schema ရှိရမည်။ Async binding ရှိရမည်။ Error handling ရှိရမည်။ Tool ကို model ထံပေးရာတွင် "ဒီ function ခေါ်ပါ" ဟုမရိုးရှင်းနိုင်။ Model သည် tool description ကိုဖတ်ပြီးဆုံးဖြတ်သောကြောင့် description ကိုလည်း security surface အဖြစ်မြင်ရမည်။

Travis-2 တွင် middleware chain သည် broker/policy plane အလုပ်တစ်ချို့ကိုလုပ်သည်။ Model call limit, semantic loop detection, context editing, summarization, skills loading စသည်တို့သည် prompt ထဲတွင်သတိပေးထားရုံမဟုတ်ဘဲ runtime layer ထဲတွင်ထားသော policy ဖြစ်သည်။

### Mutation Scope

Mutation Scope ဆိုသည်မှာ Agent ကမည်သည့်အရာကိုဘယ်အတိုင်းအတာအထိပြောင်းနိုင်သလဲဖြစ်သည်။ Read-only assistant တစ်ခုသည်အဖြေမှားပေးနိုင်သည်။ သို့သော် write-enabled agent တစ်ခုသည် system ကိုမှားပြင်နိုင်သည်။ Browser agent တစ်ခုသည် button တစ်ခုနှိပ်ခြင်းဖြင့် order submit, message send, setting change ဖြစ်နိုင်သည်။

Mutation scope ကိုစဉ်းစားရာတွင် အောက်ပါအဆင့်များအသုံးဝင်သည်။

```text
Level 0: Read only
Level 1: Draft only, no external effect
Level 2: Local file mutation with diff review
Level 3: External system mutation with human approval
Level 4: Autonomous external mutation in narrow sandbox
```

စာအုပ်ဖတ်သူအနေဖြင့် Level 4 ကိုစောစောမလိုက်ပါနှင့်။ Agent ကောင်းသည် ဆိုတာ မှန်သောအချိန်တွင် မှန်သော အာဏာသာ ရသော agent ဖြစ်သည်။ အရာအားလုံးကို အလိုအလျောက် လုပ်ခွင့်ရခြင်းက ကောင်းခြင်း မဟုတ်။

P-2 ၏ state schema mismatch lesson သည် permission design အတွက်အလွန်ကောင်းသည်။ Supervisor Agent သည် high privilege ဖြစ်သည်။ Customer Agent သည် low privilege ဖြစ်သည်။ Bridge Node သည် GlobalState အကုန်မပေးဘဲ `admin_input` မှ minimum safe instruction ကို `bridge_input` အဖြစ်သာ project လုပ်သည်။ State schema မတူခြင်းသည် inconvenience မဟုတ်။ Security feature ဖြစ်နိုင်သည်။

### Browser Tool များသည် အထူးအန္တရာယ်ရှိသည်

Browser tool သည် file read tool ထက်ပိုရှုပ်သည်။ Browser သည် untrusted content ကိုဖတ်သည်။ ထို page ထဲတွင် hidden prompt injection ပါနိုင်သည်။ Button နှိပ်လျှင် external side effect ဖြစ်နိုင်သည်။ Accessibility snapshot ထဲရှိစာသားများသည် data ဖြစ်သော်လည်း model က instruction အဖြစ်မှားယုံနိုင်သည်။

ထို့ကြောင့် BrowserSurfer case study တွင် browser tools ကိုအထူးသတိထားဖော်ပြရမည်။ `browser_evaluate` ကဲ့သို့သော high-risk browser evaluation tool များသည် developer အတွက်အလွန်အဆင်ပြေသော်လည်း security boundary မခိုင်ပါကအန္တရာယ်ကြီးသည်။ ဒီစာအုပ်သည် browser agent ကိုအန္တရာယ်ရှိသော platform misuse workflow များသင်ရန်မဟုတ်ပါ။ Browser tool agent များကိုဘယ်လိုအန္တရာယ်မြင်ရမလဲသင်ရန်ဖြစ်သည်။

Approval prompt တစ်ခုကိုစိတ်ကူးကြည့်ပါ။ Agent က "ဤ form ကို submit လုပ်မည်" ဟုဆိုသည်။ မကောင်းသော approval dialog သည် "OK?" ဟုသာမေးသည်။

ကောင်းသော approval dialog သည် "ဒီ tool သည် external website ပေါ်တွင် form submit လုပ်မည်။ Field များမှာ name, email, message ဖြစ်သည်။ Submit ပြီးလျှင် page state ပြောင်းနိုင်သည်။ Proceed လုပ်မလား" ဟုမေးသည်။

လူ့အတည်ပြုချက် ဆိုသည်မှာ လူက ဘာကို အတည်ပြုနေသလဲ နားလည်အောင် ပြပြီးမှ ဆုံးဖြတ်စေခြင်း ဖြစ်သည်။ Button တစ်ခု နှိပ်စေရုံနှင့် မပြီး။

Browser tool အတွက် broker မေးသင့်သောမေးခွန်းများ -

ဒီ page သည် trusted လား။

Tool output ကို untrusted data အဖြစ် wrap လုပ်ထားသလား။

Click/submit action အတွက် human approval လိုသလား။

Session state ကို user တစ်ယောက်မှတစ်ယောက်သို့မလွှဲမိအောင် thread_id ခွဲထားသလား။

Arbitrary JS ကိုပိတ်ထားသလား၊ သို့မဟုတ်အလွန်ကန့်သတ်ထားသလား။

Tool call log ရှိသလား။

### Skill များတွင်လည်း အာဏာရှိသည်

Skill file တစ်ခုသည် tool မဟုတ်ဟုဆိုပြီး လုံခြုံသည်ဟုမထင်ပါနှင့်။ `SKILL.md` သည် model ကိုလုပ်နည်းပြသော instruction source ဖြစ်သည်။ Malicious skill သည် Agent ကိုလမ်းလွဲစေနိုင်သည်။

ထို့ကြောင့် Travis-2 တွင် skill signing / trusted loading idea ပေါ်လာသည်။ Skill directory ဘယ်ကလာသလဲ ဆိုသည်ကို အရင် သိရမည်။ Workspace skill နှင့် global skill ကြား precedence ကို သတ်မှတ်ထားရမည်၊ unknown skill ကို fail-closed လုပ်ရမည်၊ signature mismatch ဖြစ်လျှင် ဘာလုပ်မည်ကို ကြိုဆုံးဖြတ်ထားရမည်။

OpenClaw public discussion များတွင် skill ecosystem နှင့် local machine access ကြောင့် security warning များများထွက်လာသည်။ ဤစာအုပ်တွင်ထိုအရာကို gossip အဖြစ်မသုံး။ Lesson အဖြစ်သုံးသည်။ Agent system တွင် "instruction source" ကိုလည်း software supply chain ကဲ့သို့စစ်ရမည်။

### Mini Lab: Tool ကို အန္တရာယ်အလိုက် အဆင့်ခွဲပါ

စာဖတ်သူသည်ကိုယ်ပိုင် agent project ထဲက tool list တစ်ခုရေးပါ။ Tool တစ်ခုစီအတွက်အောက်ပါ column များဖြည့်ပါ။

```text
Tool name | Reads what | Mutates what | External effect | Approval needed | Output trusted?
```

ထို့နောက် tool တစ်ခုစီကို Level 0 မှ Level 4 အထိအဆင့်ခွဲပါ။ Browser click tool ကို read-only tool နှင့်တန်းတူမထားပါနှင့်။ File write tool ကို search tool နှင့်တန်းတူမထားပါနှင့်။ Tool description ထဲတွင် "safe" ဟုရေးထားသည်ဆို၍ safe ဖြစ်မသွားပါ။

### နိဂုံး

Permission design သည် အလုပ်ကို တန်ဖိုးထားသော စိတ်မှ လာသည်။ Agent ကို မယုံကြည်ခြင်းနှင့် မဆိုင်။ လူတစ်ယောက်ကိုအလုပ်ခန့်လျှင်လည်းသော့အားလုံးမပေး။ တာဝန်အလိုက်ပေးသည်။ Agent သည်လည်းထိုသို့ပင်။

Tool Broker, Permission, Mutation Scope တို့သည် Agentic AI ၏လုံခြုံရေးဘောင်သာမဟုတ်ပါ။ အရည်အသွေးဘောင်လည်းဖြစ်သည်။ ဘောင်မရှိသော Agent သည်စွမ်းအားကြီးသောစာရေးတော်မဟုတ်ပါ။ အန္တရာယ်ကိုမမြင်ဘဲအာဏာကြီးသော tool ကိုကိုင်ထားသူနှင့်တူသည်။ ဘောင်ရှိသော Agent သည်စွမ်းအားနည်းသွားခြင်းမဟုတ်ပါ။ တာဝန်ယူနိုင်သောစနစ်တစ်ခုဖြစ်လာခြင်းပါ။

---
**စာဖတ်သူအတွက် Source Notes:**
- **Tool Broker:** Runtime layer that validates, authorizes, logs, and executes tool calls.
- **Mutation Scope:** The set of system state changes an agent is allowed to perform.
- **P-2:** Uses privilege separation and state projection as a security boundary.
- **BrowserSurfer:** ToolRegistry, ToolSpec, schemas, and browser-tool risks show why browser agents need strict boundaries.
- **Travis-2:** Middleware carries policy such as loop limits, context editing, summarization, and skill loading.
