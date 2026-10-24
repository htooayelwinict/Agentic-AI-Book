# 12-p2-zero-trust-multi-agent-bridge

> **ဒီ project က ဘာကိုပြသသလဲ**
> P-2 က Agent နှစ်ခုကြားတွင် "context အကုန်ပေးလိုက်ရင်လွယ်တယ်" ဆိုသောအမှားကိုတားပြထားသည်။ Supervisor Agent ကပိုမြင့်သောအာဏာရှိသည်။ Customer Agent က user-facing ဖြစ်သည်။ နှစ်ခုကြားတွင် full state မသွားရ။ လိုအပ်သော field လောက်သာ bridge ကကူးထည့်ပြီးပို့ရသည်။
>
> **စာဖတ်သူ ဘာကိုယူသွားရမလဲ**
> Multi-agent handoff ကို "message ပို့လိုက်တာ" လောက်နဲ့မကြည့်ပါနှင့်။ ဘယ် state field ဖြတ်သွားသလဲ၊ ဘယ် origin ကလာသလဲ၊ schema နှစ်ခုဘာကြောင့်မတူသလဲ၊ filesystem scope ဘယ်လိုကန့်ထားသလဲဆိုတာကိုကြည့်ပါ။
>
> **State boundary ဘာကြောင့်အရေးကြီးသလဲ**
> Secret မြင်ခွင့်ရှိသော Agent နှင့် user-facing Agent တို့ full state မျှဝေလိုက်လျှင် အန္တရာယ်ကချက်ချင်းကြီးလာသည်။ Prompt injection တစ်ကြောင်း၊ logic bug တစ်ခုတည်းနဲ့ internal note ထွက်သွားနိုင်သည်။
>
> **ဘာကို v0.2 သို့ချန်ထားသလဲ**
> Full code walkthrough, security test အသေးစိတ်, implementation file တစ်ခုချင်းစီကို v0.2 တွင်ဆက်ချဲ့မည်။ ဒီအခန်းမှာတော့ P-2 ကိုဖတ်ရမည့်အဓိကမျက်စိကိုအရင်ပေးထားသည်။

### ဒီ case study ကို လက်တွေ့လိုက်ဖတ်နည်း

ဒီအခန်းကို theory အဖြစ်သာဖတ်လိုက်လျှင် အရေးကြီးဆုံးအချက်လွတ်သွားနိုင်သည်။ P-2 ကိုစဖတ်တဲ့အခါ code အကုန်လိုက်ဖတ်ဖို့မလိုသေးပါ။ အရင်ဆုံးမေးရမည့်မေးခွန်းက တစ်ခုပဲ။ State ဘယ်ကနေဘယ်ကိုသွားသလဲ။

ပထမဆုံး `states.py` ကိုဖွင့်ပါ။ `GlobalState` နှင့် `UnsafeState` ကိုဘေးချင်းကပ်ရေးကြည့်ပါ။ Admin side မှာသာရှိသင့်သော field များကိုတစ်ဖက်တွင်ရေးပါ။ Customer side သို့သွားခွင့်ရှိသော field များကိုတစ်ဖက်တွင်ရေးပါ။ ဒီ table သေးသေးလေးမဆွဲနိုင်သေးလျှင် bridge lesson ကိုမမြင်သေးပါ။

ပြီးရင် `nodes.py` ထဲက Bridge behavior ကိုရှာပါ။ Bridge က state အကုန်ကူးပေးနေလား။ မဟုတ်ဘဲ `admin_input` ကိုသာ `bridge_input` အဖြစ်ကူးထည့်နေလား။ ဒီမေးခွန်းကို code ထဲမှာပဲဖြေပါ။

နောက်ဆုံး local/fake exercise တစ်ခုလုပ်ပါ။ `origin="supervisor"` ဖြစ်လျှင် `bridge_input` ထွက်ရပါမည်။ `origin="user_cli"` ဖြစ်လျှင် reject ဖြစ်ရပါမည်။ Output ထဲတွင် `secret_context` နှင့် `secret_key_ref` မပါရပါ။ ဒီသုံးချက်ကိုစစ်နိုင်လျှင် P-2 ၏ bridge lesson ကိုလက်တွေ့မြင်ပြီဟုပြောလို့ရပါသည်။

### အိမ်ရှင်ခန်းမှ ဧည့်ခန်းသို့ စာပို့ရာတွင်

အိမ်တစ်အိမ်တွင် လျှို့ဝှက်ခန်းရှိသည်ဆိုပါစို့။ ထိုခန်းထဲတွင် စာရင်းစာအုပ်များ၊ သော့များ၊ မိသားစုသီးသန့်စာရွက်များရှိသည်။ ဧည့်သည်တစ်ယောက်ကဧည့်ခန်းတွင်မေးခွန်းမေးလာသည်။ ဖြေရန်အတွက် အိမ်ရှင်သည်လျှို့ဝှက်ခန်းထဲကအချက်အလက်အချို့ကိုသုံးရနိုင်သည်။ သို့သော် ဧည့်သည်ကိုလျှို့ဝှက်ခန်းထဲခေါ်သွားပြီး စာရွက်အကုန်ဖတ်ခွင့်ပေးမည်လား။

မပေးသင့်။ အိမ်ရှင်သည်လိုအပ်သောအချက်တစ်ကြောင်းသာဧည့်ခန်းသို့ပို့ရမည်။ ဧည့်ခန်းတွင်ပြောလို့ရသောစကားသာပို့ရမည်။ လျှို့ဝှက်စာရွက်ကိုအိတ်လိုက်မပို့ရ။

P-2 ၏အဓိကသင်ခန်းစာကဒီမှာပါ။ Supervisor Agent ကလျှို့ဝှက်ခန်းထဲရှိသူပါ။ Customer Agent ကဧည့်ခန်းထဲရှိသူပါ။ Bridge Node ကအခန်းနှစ်ခန်းကြားကတံခါးစောင့်ပါ။ သူ့အလုပ်ကစာအိတ်အကုန်လွှဲပေးရန်မဟုတ်။ ဧည့်ခန်းထဲပြောလို့ရသောစာသားလောက်ကိုသာ ကူးထည့်ပေးရန်ဖြစ်သည်။

### Multi-agent ဟူသည် လူများလာခြင်းမဟုတ်

Beginner များသည် multi-agent ဟုကြားလျှင် Agent အများကြီးထားခြင်းကိုသာစိတ်ဝင်စားတတ်သည်။ Planner Agent, Worker Agent, Critic Agent, Customer Agent, Admin Agent စသည်ဖြင့်နာမည်များများရှိလျှင်စနစ်ကြီးတစ်ခုဟုထင်တတ်သည်။ သို့သော် Agent များများရှိခြင်းသည် architecture ကောင်းခြင်းမဟုတ်။

Agent တစ်ယောက်မှတစ်ယောက်သို့ဘာသွားသနည်း။ ဘယ် context သွားသနည်း။ ဘယ် secret ပါသွားနိုင်သနည်း။ ဘယ် tool scope ပါသွားသနည်း။ ဘယ် state field ဖြတ်သွားသနည်း။ ဒီမေးခွန်းများကိုမဖြေနိုင်လျှင် multi-agent system ဆိုတာ လူများသော်လည်းစည်းကမ်းမရှိသောရုံးတစ်ရုံးနှင့်တူသွားပါသည်။

P-2 ၏အလှသည် Agent များစွာရှိခြင်းမဟုတ်။ Agent များကြား state ကိုမယုံခြင်းဖြစ်သည်။ Zero trust ဆိုသည်မှာ "ဘယ်သူမှမယုံ" ဟုကြွေးကြော်ခြင်းမဟုတ်။ Trust boundary ဖြတ်တိုင်း minimum data သာပေးခြင်း၊ origin ကိုစစ်ခြင်း၊ schema ကိုခွဲခြင်း၊ tool scope ကိုကန့်သတ်ခြင်းဖြစ်သည်။

### ပြဿနာကိုအရင်ဆောက်ကြည့်ပါ

Company support system တစ်ခုစဉ်းစားကြည့်ပါ။ Admin assistant တစ်ခုသည် internal memo, admin docs, private notes, secret references များကိုမြင်နိုင်သည်။ Customer assistant တစ်ခုသည် public docs ကိုဖတ်ပြီး user-facing answer ထုတ်ပေးသည်။

တစ်ခါတစ်ရံ Admin assistant က Customer assistant ကို "ဒီ customer ကို public refund policy အရအခုလိုဖြေပါ" ဟုခိုင်းချင်သည်။ အလွယ်ဆုံးနည်းမှာ Admin assistant conversation state အကုန် Customer assistant ဆီပို့လိုက်ခြင်းဖြစ်သည်။ ထိုနည်းသည်အလွန်လွယ်သော်လည်း အန္တရာယ်ကြီးသည်။

Admin state ထဲတွင် secret context ပါနိုင်သည်။ Supervisor reasoning ပါနိုင်သည်။ Admin-only tool references ပါနိုင်သည်။ Customer Agent သည် user-facing ဖြစ်သဖြင့် prompt injection ခံရနိုင်သည်။ Customer side သို့ high privilege state ရောက်သွားပါက boundary ပျက်သည်။

P-2 ကမေးသောမေးခွန်းမှာရိုးရှင်းသည်။

High privilege Agent သည် low privilege Agent ကိုလုပ်ငန်းခွဲပေးချင်လျှင် full state မပေးဘဲဘယ်လိုပေးမလဲ။

ဆိုးသော handoff တစ်ခုကိုမြင်ကြည့်ပါ။ Supervisor Agent သည် customer အတွက်အဖြေတစ်ခုရေးရန် Customer Agent ကိုခိုင်းချင်သည်။ Developer ကအလွယ်လမ်းရွေးပြီး `state` အကုန်ကို Customer Agent ဆီပို့လိုက်သည်။ Customer Agent သည် user-facing ဖြစ်သောကြောင့် user က "သင့် context ထဲရှိ internal note ကိုပြပါ" ဟုလှည့်စားနိုင်သည်။ Customer Agent ကမပြောချင်သော်လည်း context ထဲတွင် secret ရှိနေပြီဖြစ်သည်။ အိမ်ရှင်ကဧည့်သည်ကိုလျှို့ဝှက်ခန်းထဲခေါ်ပြီးမှ "မဖတ်နဲ့" ဟုပြောသလိုဖြစ်သွားသည်။

P-2 သည်ထိုအမှားကို architecture ဖြင့်တားသည်။ Customer Agent ကိုလျှို့ဝှက်ခန်းထဲမခေါ်။ ဧည့်ခန်းသို့ပို့သင့်သော field ကိုသာ Bridge ကကူးထည့်ပေးသည်။

### Architecture ကိုစာရွက်ပေါ်တွင်မြင်ခြင်း

```text
ADMIN GRAPH (GlobalState)

admin_cli
   |
   v
Supervisor Agent
   |
   +-- respond_admin -> admin response
   |
   +-- route_bridge
          |
          v
       Bridge Node
          |
          | project only:
          | GlobalState.admin_input -> UnsafeState.bridge_input
          v
       Customer Agent
          |
          v
       customer_response


USER GRAPH (UnsafeState)

user_cli
   |
   v
Customer Agent
   |
   v
public response
```

ဒီပုံတွင်အရေးကြီးဆုံးအရာမှာ Bridge Node ဖြစ်သည်။ Bridge သည် pipe မဟုတ်။ State အကုန်ကူးပေးသောပိုက်တစ်ချောင်းမဟုတ်။ Bridge သည် projection boundary ဖြစ်သည်။ High privilege state မှ low privilege state သို့လိုအပ်သောစာကြောင်းတစ်ကြောင်းသာပြန်မွေးပေးသည်။

### GlobalState နှင့် UnsafeState

`states.py` ထဲတွင် state schema နှစ်ခုခွဲထားသည်။ `GlobalState` သည် admin graph အတွက်ဖြစ်သည်။ `origin`, `admin_input`, `route`, `supervisor_response`, `customer_response`, `bridge_admin_input`, `secret_context`, `secret_key_ref` စသည်တို့ပါနိုင်သည်။ ဤ state သည်လျှို့ဝှက်ခန်းဖြစ်သည်။

`UnsafeState` ကတော့ customer-facing side အတွက်ပါ။ `origin`, `user_input`, `bridge_input`, `response` ပဲ ပါပါတယ်။ `secret_context` လို admin-only field တွေ မပါပါဘူး။ ဒါပေမယ့် `TypedDict` က type checker အတွက်သာ ဖြစ်ပြီး runtime မှာ ဘာမှ မတားပါဘူး။ Field တစ်ခု ထပ်ထည့်ပြီး dict ကို pass လိုက်ရင် Python က error မပေးပါဘူး။ တကယ် ကာကွယ်နေတာက `runtime.py` ထဲက `_customer_from_bridge_node` ပါ။ သူက `UnsafeState` အသစ် တစ်ခုကို field နှစ်ခုတည်းနဲ့ ကိုယ်တိုင် ဆောက်ပြီး customer node ကို ပေးတာမို့ secret တွေ ကူးမသွားတာပါ။ Schema က "ဒါ မပါသင့်ဘူး" လို့ ပြောတဲ့ စာချုပ်ပါ။ Runtime က စာချုပ်ကို တကယ် လိုက်နာအောင် လုပ်တဲ့ code ပါ။ နှစ်ခုလုံး လိုပါတယ်။

Beginner developer များသည်ဤနေရာတွင် "state နှစ်ခုခွဲထားတာရှုပ်တယ်၊ တစ်ခုတည်းထားလိုက်ရင်လွယ်မယ်" ဟုတွေးနိုင်သည်။ သို့သော် security architecture တွင်လွယ်ခြင်းသည်အမြဲကောင်းခြင်းမဟုတ်။ State အတူတူထားလျှင် leak လမ်းပိုများလာနိုင်သည်။

P-2 တွင် `GlobalState.admin_input` နှင့် `UnsafeState.bridge_input` ဟုပင် field name ခွဲထားသည်။ ထိုခွဲခြင်းသည်အလှဆင်မဟုတ်။ "ဒီနေရာတွင် projection ဖြစ်နေသည်" ဟု code reader ကိုအသိပေးသောစာချုပ်ဖြစ်သည်။

တစ်ခု သတိထားပါ။ Bridge က `admin_input` ကို ပြင်ရေးတာ မဟုတ်ပါဘူး။ `bridge_input` အဖြစ် အတိုင်းသား ကူးထည့်တာပါ (`nodes.py` ထဲ "Forwards ONLY admin_input as bridge_input" ဆိုတဲ့ docstring ကို ကြည့်ပါ)။ Secret ကို ဖျက်ပစ်တာ မဟုတ်ဘဲ မယူသွားတာပါ။ ဒါက ပိုရိုးရှင်းပြီး ပိုစစ်လွယ်ပါတယ်။

### Bridge Contract — တံခါးစောင့်၏စည်းကမ်း

Bridge contract ကိုရိုးရိုးရေးလျှင်ဤသို့ဖြစ်သည်။

```text
Input:
  origin must be "supervisor"
  admin_input is the only forwarded payload

Output:
  origin = "bridge"
  bridge_input = admin_input

If origin != "supervisor":
  reject
```

`nodes.py` ထဲရှိ `BridgeNode.invoke()` သည် origin စစ်သည်။ Supervisor မဟုတ်လျှင် Bridge ကိုဖြတ်ခွင့်မပေး။ ဤသည်ရိုးရှင်းသော်လည်းအရေးကြီးသည်။ User graph မှတိုက်ရိုက် Bridge ကိုခေါ်၍ admin route ကိုကျော်တက်ခြင်းမဖြစ်စေရန်ဖြစ်သည်။

Bridge output သည် `UnsafeState` ဖြစ်သည်။ `secret_context` မပါ။ `secret_key_ref` မပါ။ Supervisor internal response မပါ။ Customer side အတွက်လိုသော `bridge_input` သာပါသည်။ Bridge သည် LLM မဖြစ်သင့်။ "Secret မပို့ပါနဲ့" ဟု model ကိုတောင်းဆိုခြင်းထက် deterministic code-level projection ကပိုခိုင်မာသည်။

### Supervisor, Customer, Bridge

Supervisor Agent သည် high privilege ဖြစ်သည်။ Admin input ကိုဖတ်နိုင်သည်။ Admin scoped filesystem ကိုမြင်နိုင်သည်။ Routing decision ချနိုင်သည်။ `respond_admin` သို့မဟုတ် `route_bridge` ကိုရွေးနိုင်သည်။

Customer Agent သည် low privilege ဖြစ်သည်။ Public docs scope ကိုသာမြင်သင့်သည်။ Customer-facing answer ကိုထုတ်ပေးသည်။ Admin secrets မမြင်သင့်။ Supervisor reasoning မမြင်သင့်။

Bridge Node သည် air gap ဖြစ်သည်။ စကားလက်ဆင့်ကမ်းသူမဟုတ်။ State ကိုပြန်မွေးပေးသူဖြစ်သည်။ High privilege state ကနေ low privilege state အသစ်ဆောက်ရာတွင် `admin_input` တစ်ခုတည်းကိုသာ ကူးထည့်သည်။

ဤသုံးယောက်၏ role ကိုမခွဲနိုင်လျှင် P-2 ကိုမနားလည်သေးဟုဆိုနိုင်သည်။

### Control Plane နှင့် Execution Plane

P-2 တွင် LangGraph သည် control plane ဖြစ်သည်။ ဘယ် node သို့သွားမလဲ၊ admin graph သို့ user graph ခွဲမလဲ၊ Bridge ကိုဘယ်အချိန်ဖြတ်မလဲဆိုတာထိန်းသည်။

DeepAgents nodes များသည် execution plane ဖြစ်သည်။ Model/tool loop, filesystem access, response generation တို့ကိုလုပ်သည်။

```text
Control plane:
  route, graph, bridge, origin checks

Execution plane:
  model loop, tools, filesystem, response writing
```

ဒီခွဲခြင်းကအရေးကြီးသည်။ Execution plane ထဲတွင် model မှားသော်လည်း control plane boundary ကြောင့် secret leakage blast radius လျှော့နိုင်သည်။ ဒါကို "လုံးဝလုံခြုံသည်" ဟုမဆိုရ။ "Logic bug တစ်ခုသည် security breach ဖြစ်မသွားစေရန် boundary ကူညီနိုင်သည်" ဟုမှတ်ရမည်။

### Scoped Filesystem — `/` ဟုမြင်သော်လည်း ကမ္ဘာမတူ

P-2 တွင် DeepAgents filesystem backends ကို virtual mode ဖြင့် scoped လုပ်ထားသည်။ Supervisor worker အတွက် real `./admin` directory ကို virtual `/` အဖြစ်မြင်စေသည်။ Customer worker အတွက် real `./docs` directory ကို virtual `/` အဖြစ်မြင်စေသည်။

Agent နှစ်ခုလုံးက `/` ဟုမြင်နိုင်သည်။ သို့သော်တကယ်မြင်သောကမ္ဘာကွဲသည်။ Supervisor ၏ `/` သည် admin scope ဖြစ်သည်။ Customer ၏ `/` သည် public docs scope ဖြစ်သည်။

ဒီ design မှယူရမည့်အချက်မှာ context boundary နှင့် tool boundary နှစ်ခုလုံးလိုခြင်းဖြစ်သည်။ Customer Agent ကို admin state မပေးသည့်အပြင် admin filesystem လည်းမပေးရ။ Context ကောင်းသော်လည်း tool scope ပျက်လျှင် boundary ပျက်နိုင်သည်။

### State Projection ကိုလက်တွေ့ကြည့်ခြင်း

Admin request တစ်ခုလာသည်ဆိုပါစို့။

```text
origin = admin_cli
admin_input = "public docs အရ customer ကို refund rule ရှင်းပြပါ"
secret_context = "internal-only note..."
secret_key_ref = "..."
```

Supervisor က route_bridge ဆုံးဖြတ်သည်။

```text
origin = supervisor
admin_input = "public docs အရ customer ကို refund rule ရှင်းပြပါ"
route = route_bridge
secret_context = "internal-only note..."
secret_key_ref = "..."
```

Bridge သည် origin စစ်ပြီး output အသစ်တည်ဆောက်သည်။

```text
origin = bridge
bridge_input = "public docs အရ customer ကို refund rule ရှင်းပြပါ"
```

Customer Agent သည် `bridge_input` ကိုသာမြင်သည်။ `secret_context` မရှိတော့။ `secret_key_ref` မရှိတော့။ Supervisor ၏ internal fields မရှိတော့။ ဤသည် projection ဖြစ်သည်။

### ဘာကောင်းသလဲ

P-2 ၏ကောင်းချက်ပထမမှာ blast radius လျှော့ခြင်းဖြစ်သည်။ Customer Agent prompt injection ခံရလျှင်ပင် admin state မမြင်နိုင်ရန်ရည်ရွယ်ထားသည်။

ဒုတိယမှာ code review လွယ်ခြင်းဖြစ်သည်။ Bridge contract ရိုးရှင်းသည်။ Reviewer သည် "ဒီ field က bridge ဖြတ်သွားနိုင်သလား" ဟုစစ်နိုင်သည်။

တတိယမှာ educational clarity ဖြစ်သည်။ Multi-agent handoff ကို security boundary အဖြစ်မြင်စေသည်။

စတုတ္ထမှာ schema mismatch ကို feature အဖြစ်အသုံးချခြင်းဖြစ်သည်။ Low privilege schema တွင် secret fields မရှိခြင်းက accident leak ကိုလျှော့နိုင်သည်။

### ဘာကိုသတိထားရမလဲ

Projection သည် full solution မဟုတ်။ `admin_input` ကိုယ်တိုင်တွင် secret ပါနေပါက Bridge သည်ထို string ကိုပို့နိုင်သည်။ ထို့ကြောင့် content sanitization, supervisor-side summary, admin UX warning လိုနိုင်သည်။

Classifier behavior သည်အရေးကြီးသည်။ Supervisor route decision မှားလျှင် bridge ဖြတ်သင့်/မဖြတ်သင့်ဆုံးဖြတ်ချက်မှားနိုင်သည်။ README နှင့် implementation ကြား docs drift ရှိ/မရှိစစ်ရမည်။ [SYNC_MISMATCH] ဖြစ်နိုင်သောနေရာများကို source audit ထဲတွင်မှတ်ထားသင့်သည်။

Scoped filesystem သည် path traversal, symlink, absolute path, unicode path edge cases များအတွက် test လိုသည်။ Sandbox ကိုအပြည့်အဝယုံကြည်သောစိတ်မထားသင့်။

Customer Agent ကို read-only ထားခြင်းသည်ကောင်းသည်။ သို့သော် public docs search အတွက် safe search wrapper လိုနိုင်သည်။ Security နှင့် usability ကိုအတူစဉ်းစားရမည်။

### Design Pattern များကိုနာမည်တပ်ခြင်း

P-2 မှ pattern များကိုအောက်ပါအတိုင်းသိမ်းထားနိုင်သည်။

**Projection Boundary** — Object အကုန်မပို့ဘဲ destination privilege အတွက်လိုသော field ကိုသာထုတ်ပေးသည်။

**Privilege Separation** — Supervisor high privilege, Customer low privilege ခွဲထားသည်။

**Control Isolation** — Admin graph နှင့် user graph ခွဲထားသည်။

**Capability Scoping** — Filesystem/tool access ကို role အလိုက်ကန့်သတ်သည်။

**Gatekeeper** — Bridge သည် origin check မအောင်လျှင် reject လုပ်သည်။

ဤ pattern များသည် P-2 တစ်ခုတည်းအတွက်မဟုတ်။ Internal support bot, DevOps assistant, browser automation agent, coding agent အားလုံးတွင်အသုံးဝင်သည်။

### စာဖတ်သူကိုယ်တိုင် ပြန်စစ်ပြင်ကြည့်ရန်

P-2 ကိုဖတ်ပြီးကိုယ်တိုင်စစ်ရန် exercise များ -

1. Bridge unit test ရေးပါ။ `origin != "supervisor"` ဖြစ်လျှင် reject ဖြစ်ရမည်။
2. `secret_context` နှင့် `secret_key_ref` သည် Customer side output ထဲမပါကြောင်း test ရေးပါ။
3. Admin input ထဲတွင် secret-looking text ပါလျှင် sanitizer warning ထုတ်မလား design note ရေးပါ။
4. Customer filesystem scope တွင် `../admin` ကဲ့သို့ path traversal attempt ကိုစမ်းသပ်မည့် test matrix ရေးပါ။
5. `GlobalState` နှင့် `UnsafeState` fields ကို table ဆွဲပြီး ဘယ် field က bridge ဖြတ်ခွင့်ရှိ/မရှိခွဲပါ။
6. Customer Agent ကို search capability ပေးမည်ဆိုလျှင် read-only safe wrapper ဘယ်လိုရေးမလဲစဉ်းစားပါ။

### နိဂုံး — တံတားကောင်းသည် အကုန်မသယ်

P-2 ၏သင်ခန်းစာကိုတစ်ကြောင်းတည်းပြောရလျှင် ဤသို့ဖြစ်သည်။ High privilege Agent နှင့် low privilege Agent ကြား full state မပေးပါနှင့်။ Minimum safe instruction သာ project လုပ်ပါ။

Bridge သည်ပိုက်မဟုတ်။ တံခါးစောင့်ဖြစ်သည်။ State schema mismatch သည်အဆင်မပြေသောအရာမဟုတ်။ Security feature ဖြစ်နိုင်သည်။ Scoped filesystem သည် prompt warning ထက်ပိုခိုင်မာသော boundary ဖြစ်နိုင်သည်။ Control plane နှင့် execution plane ကိုခွဲထားခြင်းသည် model/tool loop ၏အမှားများကိုအကန့်အသတ်ထဲထားနိုင်သည်။

စာဖတ်သူသည် P-2 ကိုဖတ်ပြီး "Agent နှစ်ယောက်ဆက်သွယ်တယ်" ဟုသာမှတ်လျှင်အဓိကသင်ခန်းစာလွတ်သွားမည်။ "ဘယ် state များမသွားသင့်သလဲ" ဟုမေးတတ်လျှင်တော့ P-2 ၏တံတားကိုတကယ်မြင်လာပြီ။

---
**စာဖတ်သူအတွက် Source Notes:**
- **GitHub source:** `https://github.com/htooayelwinict/P-2`
- **ဖတ်ထားသော source map:** `README.md`, `docs/ARCHITECTURE-ROUTING.md`, `src/multi_agent_app/runtime.py`, `src/multi_agent_app/states.py`, `src/multi_agent_app/nodes.py`, `src/multi_agent_app/classifier.py`
- **အဓိက lesson:** `GlobalState.admin_input -> UnsafeState.bridge_input` projection ဖြစ်သည်။ Full state handoff မလုပ်ခြင်းကဒီ case study ၏အသည်းနှလုံးဖြစ်သည်။
- **Security concept:** Separate state schema နှင့် scoped filesystem access သည် low-privilege side သို့ exposure လျှော့ပေးသည်။
- **ဆက်စစ်ရန်:** Classifier/docs drift, sensitive admin input အတွက် sanitizer behavior, path traversal/symlink edge cases များကို v0.2 တွင်စစ်ရန်လိုသေးသည်။
