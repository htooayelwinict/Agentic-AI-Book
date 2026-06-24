# ၀၇။ Prompt မှ Context ဆီသို့ — စာရေးတော်၏ စားပွဲပေါ်ရှိ မြေပုံများ

### စကားညှိခြင်းမတတ်ဘဲ မှတ်ဉာဏ်အိမ်ကြီး မဆောက်ပါနှင့်

Agentic AI ကိုလေ့လာသူအများစုသည် Context Engineering, RAG, Memory, Vector Database စသောစကားလုံးများကိုကြားသည်နှင့် တန်း၍စာကြည့်တိုက်ကြီးဆောက်ချင်ကြသည်။ စာအုပ်အားလုံးကို embedding လုပ်မည်။ Qdrant သို့မဟုတ် vector database ထဲသိမ်းမည်။ Agent ကိုမေးလိုက်လျှင်အကုန်သိမည်ဟုထင်သည်။

ဤအတွေးသည် အနည်းငယ်မှန်သော်လည်း အနည်းငယ်အန္တရာယ်လည်းရှိသည်။ စာရေးတော်ကို စာကြည့်တိုက်ကြီးအလယ်တွင်ထားလိုက်ခြင်းဖြင့် စာရေးတော်ကောင်းဖြစ်လာမည်မဟုတ်။ သူ့ကိုမည်သို့မေးရမည်၊ ဘာကိုအဓိကထားစေမည်၊ မည်သည့်အချက်အလက်ကိုယုံရမည်၊ မည်သည့်စာရွက်ကို data အဖြစ်သာဖတ်ရမည်ဟူသည်ကို အရင်သင်ရမည်။

ထို့ကြောင့် Context Engineering မတိုင်မီ **Prompt Engineering** ကိုအရင်နားလည်ရမည်။ Prompt Engineering ဆိုသည်မှာ model ကိုလှည့်စားသောအတတ်မဟုတ်။ စာရေးတော်နှင့်အလုပ်လုပ်ရာတွင် စကားကိုစည်းကမ်းရှိရှိပြောတတ်ခြင်းဖြစ်သည်။ လူတစ်ယောက်ကိုအလုပ်ခိုင်းရာတွင် "ဟိုဟာလေးလုပ်ပေး" ဟုခိုင်းလျှင် ရလဒ်မတိကျနိုင်သကဲ့သို့၊ Agent ကိုလည်း မရှင်းလင်းသောစကားဖြင့်ခိုင်းလျှင် အလုပ်မတိကျနိုင်။

Prompt Engineering သည်စကားညှိခြင်းဖြစ်သည်။

Context Engineering သည်စာရေးတော်၏စားပွဲပေါ်တွင် ဘယ်စာရွက်များတင်ပေးမည်ဆိုသောအတတ်ဖြစ်သည်။

RAG သည် စားပွဲပေါ်မရှိသေးသောစာရွက်ကို စာကြည့်တိုက်မှပြန်ရှာပေးသောနည်းဖြစ်သည်။

Memory သည်ယခင်အလုပ်များမှ အရေးကြီးသောအချက်များကို နောင်တွင်ပြန်အသုံးပြုနိုင်အောင်သိမ်းထားသောစနစ်ဖြစ်သည်။

ဤလေးခုကိုရောသွားလျှင် Agent သည်သိသောပုံပေါက်သော်လည်း အလုပ်မသေချာတော့ပေ။

### Prompt Engineering — စာရေးတော်ကို ဘယ်လိုခိုင်းမလဲ

Prompt ဟုဆိုရာတွင် user ကရိုက်သောစာကြောင်းတစ်ကြောင်းကိုသာမဆိုလို။ Agent runtime တစ်ခုတွင် prompt အမျိုးအစားများစွာရှိသည်။

```text
System / Developer instruction  -> စနစ်စည်းကမ်း
User prompt                      -> အသုံးပြုသူ၏အမိန့်
Tool description                 -> ကိရိယာအသုံးပြုနည်း
Few-shot examples                -> နမူနာအလုပ်များ
Retrieved context                -> ပြန်ရှာယူထားသောအချက်အလက်
Skill / AGENTS rules             -> အလုပ်ခွင်လက်စွဲ
```

System instruction သည်အိမ်၏ဥပဒေနှင့်တူသည်။ User prompt သည်ယနေ့လုပ်ရမည့်အလုပ်ဖြစ်သည်။ Tool description သည်ကိရိယာတစ်ခု၏အသုံးပြုနည်းဖြစ်သည်။ Few-shot example သည် "ဒီလိုပုံစံနဲ့လုပ်" ဟုနမူနာပြခြင်းဖြစ်သည်။ Retrieved context သည်စာကြည့်တိုက်မှထုတ်လာသောစာရွက်ဖြစ်သည်။

Prompt Engineering ၏အခြေခံမေးခွန်းများမှာ ရိုးရှင်းသည်။

ပထမ၊ အလုပ်၏ရည်ရွယ်ချက်ကိုတိတိကျကျပြောထားသလား။

ဒုတိယ၊ အကန့်အသတ်ကိုပြောထားသလား။

တတိယ၊ output ပုံစံကိုပြောထားသလား။

စတုတ္ထ၊ မသိလျှင်မသိကြောင်းပြောရန်ခွင့်ပေးထားသလား။

ပဉ္စမ၊ tool သုံးရန်လို/မလိုကိုသတ်မှတ်ထားသလား။

Beginner များအတွက်အကြီးဆုံးအမှားမှာ Prompt ကိုကဗျာတစ်ပုဒ်လိုရေးပြီး deterministic system တစ်ခုလိုမျှော်လင့်ခြင်းဖြစ်သည်။ Prompt သည်ဥပဒေမဟုတ်။ Prompt သည် instruction ဖြစ်သည်။ Instruction သည် model behavior ကိုလမ်းညွှန်နိုင်သော်လည်း model ကိုသံမဏိတံတိုင်းဖြင့်ပိတ်မထားနိုင်။ ထို့ကြောင့် Prompt Engineering ကောင်းသည်ဆိုသည်မှာ prompt ကိုပြင်တာသာမဟုတ်၊ runtime boundary, tool permission, verifier, output sanitizer တို့နှင့်တွဲ၍စဉ်းစားခြင်းဖြစ်သည်။

### Prompt နှင့် Context ကြားရှိ ခြားနားချက်

Prompt သည် "ဘယ်လိုလုပ်" ဟုပြောသည်။

Context သည် "ဘာကိုကြည့်ပြီးလုပ်" ဟုပေးသည်။

ဥပမာအားဖြင့် စာရေးတော်ကို "ဤစာချုပ်ကို စီးပွားရေးအန္တရာယ်အနေနှင့်အကျဉ်းချုပ်ပါ" ဟုခိုင်းလျှင် Prompt ဖြစ်သည်။ စာချုပ်ဖိုင်အကြောင်းအရာကိုပေးလျှင် Context ဖြစ်သည်။ Prompt ကောင်းသော်လည်း Context မှားလျှင်အဖြေမှားနိုင်သည်။ Context ကောင်းသော်လည်း Prompt မရှင်းလျှင် အဖြေသည်လမ်းလွဲနိုင်သည်။

အလွန်ဆိုးသော prompt တစ်ခုကိုကြည့်ပါ။

```text
ဒီ repo ကိုကြည့်ပြီး ဘာမှားနေလဲပြော။
```

ဤ prompt သည်အလွန်ကျယ်သည်။ ဘယ် repo, ဘယ် branch, ဘယ် file, ဘာအန္တရာယ်, output ပုံစံဘာမျှမပါ။ ပိုကောင်းသော prompt သည်ဤသို့ဖြစ်နိုင်သည်။

```text
book/chapters/12-p2-zero-trust-multi-agent-bridge.md ကိုဖတ်ပါ။
P-2 repo source notes နှင့်မကိုက်သော claim များကိုသာရှာပါ။
စာရေးဟန်မပြင်ပါနှင့်။ Finding တစ်ခုစီကို evidence နှင့်ပြပါ။
```

သို့သော် prompt ကောင်းရုံမလုံလောက်သေး။ Context packet လည်းလိုသည်။

```text
Context packet:
- target chapter path
- P-2 README summary
- ARCHITECTURE-ROUTING.md excerpt
- states.py field names
- nodes.py bridge behavior
- known [SOURCE_NEEDED] markers
```

Prompt သည်အလုပ်အမိန့်ဖြစ်သည်။ Context packet သည်အလုပ်စားပွဲပေါ်တင်ပေးသောစာရွက်ဖြစ်သည်။ နှစ်ခုလုံးမညီလျှင်စာရေးတော်သည်အလုပ်လုပ်နေသကဲ့သို့ထင်ရပြီးအမှန်တွင်ခန့်မှန်းနေခြင်းသာဖြစ်နိုင်သည်။

Agent system များတွင် Context သည်အလွန်များလာတတ်သည်။ Chat history, tool output, retrieved docs, skill instructions, project rules, error logs, prior plan, user preferences စသည်တို့အားလုံး context ဖြစ်လာနိုင်သည်။ ထိုအရာအားလုံးကို model ထံတစ်ပြိုင်နက်ပို့လိုက်ခြင်းသည် ပညာမဟုတ်။ စာရေးတော်၏စားပွဲပေါ်တွင်စာရွက်ထောင်ချီပုံထားပြီး "အရေးကြီးတာရှာ" ဟုခိုင်းခြင်းနှင့်တူသည်။

Context Engineering ဆိုသည်မှာ အရေးကြီးသောစာရွက်ကိုအနီးဆုံးထားပြီး၊ အရေးမကြီးသောစာရွက်ကိုဖယ်၊ မသေချာသောစာရွက်ကိုသတိပေး၊ လျှို့ဝှက်စာရွက်ကိုမပေးခြင်းဖြစ်သည်။

### Context Window — စားပွဲပေါ်ရှိ လက်ရှိမြေပုံ

Context window ကို Beginner များသည် model ၏မှတ်ဉာဏ်ဟုထင်တတ်ကြသည်။ အမှန်မှာ context window သည် permanent memory မဟုတ်။ ၎င်းသည် လက်ရှိလုပ်ငန်းအတွက် model ရှေ့တွင်တင်ထားသောစာရွက်ပုံဖြစ်သည်။ စားပွဲကျယ်လျှင်စာရွက်ပိုတင်နိုင်သည်။ သို့သော်စာရွက်များလွန်းလျှင် စာရေးတော်သည်အရေးကြီးသောစာရွက်ကိုမမြင်တော့နိုင်။

Coding Agent များတွင် `AGENTS.md` နှင့် `SKILL.md` ကဲ့သို့သောဖိုင်များကို context ထဲတွင်ထိန်းသိမ်းရခြင်းသည် ဤသဘောကြောင့်ဖြစ်သည်။ `AGENTS.md` သည် project အလုပ်ခွင်စည်းကမ်းဖြစ်သည်။ "ဘယ်ဖိုင်မထိသင့်", "ဘယ် test run ရ", "ဘယ် style သုံး", "secret မထုတ်သင့်", "destructive command မသုံးသင့်" စသည်တို့ပါနိုင်သည်။ `SKILL.md` သည် task-specific လက်စွဲစာအုပ်ဖြစ်သည်။ Browser automation အတွက်တစ်မျိုး၊ PDF rendering အတွက်တစ်မျိုး၊ GitHub review အတွက်တစ်မျိုးဖြစ်နိုင်သည်။

Agent သည် context compaction ခံရသောအခါ conversation အဟောင်းများကိုအကျဉ်းချုပ်ထားရသည်။ ထိုအချိန်တွင် `AGENTS.md` နှင့် `SKILL.md` ၏အရေးကြီးသော rule များကိုမထိန်းသိမ်းနိုင်ပါက Agent သည်အလုပ်ခွင်စည်းကမ်းကိုမေ့သွားနိုင်သည်။ ဤသည်မှာ စာရေးတော်ကိုမိုးလင်းတိုင်းအလုပ်ခွင်သစ်သို့ပို့ပြီး "မနေ့ကစည်းကမ်းတွေကိုမေ့လိုက်" ဟုပြောခြင်းနှင့်တူသည်။

သို့သော် context window သည်အကန့်အသတ်ရှိသောကြောင့် အရာအားလုံးကိုအပြည့်ထည့်ထားရန်လည်းမဖြစ်နိုင်။ အကောင်းဆုံးနည်းမှာ rule များကိုအရေးကြီးမှုအလိုက်ခွဲခြင်းဖြစ်သည်။

| အမြဲစားပွဲပေါ်ထားရမည့်အရာ | လိုအပ်မှခေါ်ဖတ်ရမည့်အရာ |
| --- | --- |
| Safety rules | Long examples |
| File/editing boundaries | Domain references |
| Test commands | Optional workflows |
| User voice/style contract | Bulky generated notes |

မြန်မာလိုပြောလျှင် "မလုပ်ရမည့်စည်းကမ်း" နှင့် "အလုပ်၏အသံ" ကိုမမေ့စေရ။ သို့သော်နမူနာရှည်များ၊ reference အထူကြီးများကိုလိုအပ်ချိန်မှဖွင့်ဖတ်စေပါ။ စားပွဲပေါ်တွင်ဓားနှင့်အတိုင်းအတာကိုအမြဲထားနိုင်သည်။ သစ်တောအပြည့်ကိုတော့စားပွဲပေါ်တင်မထားနိုင်။

ဤနေရာတွင် P-2 ၏သင်ခန်းစာပြန်ဝင်လာသည်။ Context ကိုလည်း state ကဲ့သို့ပင် projection လုပ်ရမည်။ High privilege context အကုန်ကို low privilege agent ထံမပေးရ။ Sub-agent တစ်ခုကိုအလုပ်ခွဲပေးလျှင်လည်း task အတွက်လိုသော context သာပေးရသည်။

### RAG — စာကြည့်တိုက်မှူးကို အလုပ်ခန့်ခြင်း

RAG သည် Retrieval-Augmented Generation ဖြစ်သည်။ အလွယ်ပြောလျှင် model ကိုအကုန်အလွတ်ကျက်ခိုင်းမည့်အစား လိုအပ်သောအချိန်တွင်ပြင်ပစာကြည့်တိုက်မှစာရွက်ရှာပေးခြင်းဖြစ်သည်။

```text
User question
   |
   v
Retriever searches documents
   |
   v
Relevant chunks enter context
   |
   v
LLM writes answer using those chunks
```

RAG တွင်စာရွက်ရှာခြင်းသည်စာရွက်ရေးခြင်းထက်အရေးကြီးသည်။ Retriever မှားလျှင် LLM သည်မှားသောစာရွက်ကိုဖတ်ပြီးသေချာသောလေသံဖြင့်မှားသောအဖြေထုတ်နိုင်သည်။ Vector embedding သည်စာသားများကိုအဓိပ္ပာယ်နီးစပ်မှုအရကိန်းဂဏန်းမြေပုံပေါ်တင်ခြင်းဖြစ်သည်။ Cosine similarity သည်ထိုမြေပုံပေါ်တွင်ဘယ်စာရွက်ကမေးခွန်းနှင့်နီးသလဲတိုင်းတာသည့်နည်းတစ်ခုဖြစ်သည်။ သို့သော်ဤသည် LLM word generation ၏အပြည့်အစုံမဟုတ်ကြောင်း အခန်း ၀၃ တွင်ပြောခဲ့ပြီးဖြစ်သည်။ Embedding search သည်စာရွက်ရှာပေးခြင်းဖြစ်သည်။ Transformer generation သည် attention, learned parameters, token probability စသောအရာများဖြင့်စာရေးခြင်းဖြစ်သည်။ နှစ်ခုကိုမရောပါနှင့်။

RAG တွင် chunking လည်းအရေးကြီးသည်။ Chunk သေးလွန်းလျှင် context ပျောက်သွားသည်။ Chunk ကြီးလွန်းလျှင်အမှိုက်များလာသည်။ Beginner များသည် "စာမျက်နှာ ၅၀၀ လုံးကို embedding လုပ်လိုက်ရင်ရပြီ" ဟုထင်တတ်သည်။ အင်ဂျင်နီယာကတော့မေးရမည်။

ဒီစာရွက်ကိုဘယ်အရွယ်အစားဖြင့်ခွဲမလဲ။

Heading, function, paragraph boundary ကိုထိန်းသလား။

Metadata ထည့်ထားသလား။

Retrieved chunk ကို rerank လုပ်သလား။

Source citation ပြန်ပေးသလား။

Model မသိလျှင်မသိကြောင်းပြောနိုင်သလား။

BrowserSurfer တွင် trajectory reuse အတွက် Qdrant storage အသုံးပြုသော idea သည် RAG ကို "စာအုပ်ရှာခြင်း" အဖြစ်သာမဟုတ်ဘဲ "ယခင်လုပ်ငန်းအတွေ့အကြုံပြန်ကြည့်ခြင်း" အဖြစ်မြင်စေသည်။ PlanningAgent သည် past trajectory များမှသင်ခန်းစာယူနိုင်သည်။ သို့သော် ထို trajectory များထဲတွင် PII သို့မဟုတ်အဆိပ်ညွှန်ကြားချက်ပါလာနိုင်သောကြောင့် redaction နှင့် sanitization မရှိပါက memory သည်အန္တရာယ်ဖြစ်နိုင်သည်။

### Memory — မှတ်ထားသင့်သလား၊ မေ့သင့်သလား

Agent Memory ဟုဆိုလျှင် "အရာအားလုံးမှတ်မိသော AI" ဟုမတွေးပါနှင့်။ Memory design ၏အဓိကမေးခွန်းမှာ "ဘာကိုမှတ်မလဲ" ထက် "ဘာကိုမမှတ်သင့်ဘူးလဲ" ဖြစ်သည်။

Short-term memory သည် current task context ဖြစ်သည်။ Long-term memory သည် user preference, project facts, past trajectory, reusable plan စသည်တို့ဖြစ်နိုင်သည်။ သို့သော် long-term memory သည်အမြဲတမ်းကောင်းသောအရာမဟုတ်။ မှားသော fact တစ်ခုကိုသိမ်းထားလျှင် Agent သည်နောက်အခါတိုင်းမှားသွားနိုင်သည်။ Secret တစ်ခုကိုသိမ်းထားလျှင်နောက်ပိုင်း leak ဖြစ်နိုင်သည်။ Webpage ထဲက prompt injection တစ်ခုကို memory ထဲသိမ်းထားလျှင် အနာဂတ် run များကိုအဆိပ်သင့်စေနိုင်သည်။

Memory အတွက် rule သုံးခုထားနိုင်သည်။

ပထမ၊ မှတ်မည့်အရာကို user သို့မဟုတ် policy ဖြင့်ဆုံးဖြတ်ပါ။

ဒုတိယ၊ memory ထဲမဝင်မီ PII, secret, hostile instruction ကိုစစ်ပါ။

တတိယ၊ memory ကိုပြန်သုံးသောအခါ "trusted instruction" မဟုတ်ဘဲ "past observation" အဖြစ်သတ်မှတ်ပါ။

Travis-2 တွင် ContextEditingMiddleware နှင့် safe summarization idea များသည် context ကိုရှင်းလင်းစေသော harness အစိတ်အပိုင်းဖြစ်သည်။ appv22 တွင် compaction timing, overflow recovery, output-cap recovery စသောအရာများသည် memory/context engineering ကို runtime recovery ပြဿနာအဖြစ်မြင်စေသည်။ Context overflow ဖြစ်ခြင်းသည်စာရေးတော်ပျင်းခြင်းမဟုတ်။ စားပွဲပေါ်စာရွက်များပြည့်သွားခြင်းဖြစ်သည်။

### Prompt, Context, Memory ကို စမ်းသပ်နည်း

Mini lab အဖြစ်စာဖတ်သူသည် project တစ်ခုကိုရွေးပါ။ README, issue notes, test output သုံးခုကိုယူပါ။ Agent ကိုသုံးကြိမ်ခိုင်းပါ။

ပထမအကြိမ်တွင် prompt သာကောင်းအောင်ရေးပြီး context မပေးပါနှင့်။

ဒုတိယအကြိမ်တွင် context အများကြီးပေးပြီး prompt မရှင်းပါနှင့်။

တတိယအကြိမ်တွင် prompt ကိုတိကျအောင်ရေးပြီး context ကိုလိုအပ်သလောက်ရွေးပေးပါ။

နောက်ဆုံးရလဒ်သုံးခုကိုနှိုင်းယှဉ်ပါ။ ထိုအခါ Prompt Engineering နှင့် Context Engineering သည် fancy word မဟုတ်ကြောင်းတွေ့ရမည်။ စကားညှိခြင်းနှင့်စာရွက်စီခြင်းသည် Agent quality ကိုတကယ်ပြောင်းစေသည်။

### နိဂုံး — သိအောင်မဟုတ်၊ သေချာစွာသိအောင်

စာရေးတော်ကိုအရာအားလုံးသိစေရန်ကြိုးစားခြင်းသည်မလိုအပ်ပါ။ လက်ရှိအလုပ်အတွက်လိုသောအရာကိုရှင်းရှင်းပေးရန်လိုသည်။ Prompt သည်စကားညှိသည်။ Context သည်စားပွဲပေါ်စာရွက်တင်သည်။ RAG သည်စာကြည့်တိုက်မှရှာပေးသည်။ Memory သည်နောင်အတွက်သိမ်းသည်။ Compaction သည်စားပွဲကိုပြန်ရှင်းသည်။

Agentic AI တွင် "သိခြင်း" ထက် "ဘယ်အချက်အလက်ကို ဘယ်အချိန်တွင် ဘယ်အခွင့်အာဏာဖြင့် သုံးခွင့်ပေးမလဲ" ဆိုသောမေးခွန်းကပိုအရေးကြီးသည်။ ထိုမေးခွန်းကိုမေးတတ်မှ Agent သည်စာရွက်ပုံအောက်တွင်ပိနေသောစာရေးတော်မဟုတ်တော့ဘဲ အလုပ်လုပ်နိုင်သောကိုယ်စားလှယ်ဖြစ်လာမည်။

---
**စာဖတ်သူအတွက် Source Notes:**
- **Prompt Engineering:** Instruction, examples, constraints, and output contracts for model behavior.
- **Context Engineering:** Selecting, ordering, trimming, and protecting the information placed in the context window.
- **RAG:** Retrieval-Augmented Generation; retrieves external context before generation.
- **AGENTS.md / SKILL.md:** Runtime instruction sources for coding agents and skill workflows; preserve critical rules during compaction.
- **BrowserSurfer:** Uses trajectory storage/reuse ideas; memory must be redacted and treated as untrusted observation.
- **Travis-2 / appv22:** Context editing, summarization, compaction timing, and recovery are runtime engineering problems, not decoration.
