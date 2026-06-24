# Style Guide

ဤစာအုပ်သည် AI textbook မဟုတ်။ လူဖတ်ရန်စာအုပ်ဖြစ်သည်။ နည်းပညာကို သင်ပေးရမည်ဖြစ်သော်လည်း စာရေးသူ၏ အသံကို သတ်မပစ်ရ။ Chapter တစ်ခုစီသည် checklist ဖြည့်ထားသော report မပုံစံမဟုတ်ဘဲ၊ စာဖတ်သူတစ်ယောက်ကို တကယ်ထိုင်ရှင်းပြနေသကဲ့သို့ ဖတ်ရမည်။

## အသံ

- Preface, author note, acknowledgement တို့တွင် မူရင်းစာရေးသူ၏ စိတ်ခံစားမှု၊ နှိမ့်ချမှု၊ ကျေးဇူးတရား၊ လူသားဆန်မှုကို မဖျက်ရ။
- Technical chapters များတွင်လည်း အလွန်ခြောက်သွေ့သော corporate documentation မရေးရ။ ရှင်းလင်းရမည်၊ သို့သော် အသက်မဲ့မဖြစ်ရ။
- Shwe U Daung ကို style primer အဖြစ်ယူရာတွင် copied prose မလုပ်ရ။ ယူရမည့်အရာမှာ စာဖတ်သူကို လက်ကမ်းခေါ်သကဲ့သို့ ရှင်းပြခြင်း၊ modern idea ကို မြန်မာစာဖတ်သူနားလည်သောဘဝနှင့်ချိတ်ခြင်း၊ moral responsibility မပျောက်စေခြင်းတို့သာဖြစ်သည်။
- “Opening Problem”, “Simple Definition”, “Mental Model”, “Common Mistakes” စသည့် heading များကို visible scaffold အဖြစ်မသုံးရ။ ထို logic သည် writer checklist အဖြစ်သာရှိရမည်။

## ဘာသာစကား

- Main prose ကို Myanmar ဖြင့်ရေးပါ။
- Agent, Workflow, Tool, MCP, Skill, Sub-agent, Harness, Loop, Runtime, Planner, Worker, Verifier, Prompt Engineering, Context Engineering, RAG, Middleware, StateGraph, Reducer, Checkpointer, ToolRegistry, Mutation Scope, CI/CD, Terraform, AWS စသည့် technical terms များကို English 그대로ထားနိုင်သည်။
- English term ပထမဆုံးသုံးသည့်နေရာတွင် အဓိပ္ပာယ်ကို စာကြောင်းထဲတွင်ပင် သဘာဝကျကျရှင်းပါ။

## Case Study များ

Case study chapter များသည် repo-backed ဖြစ်ရမည်။ သို့သော် handover report မဖြစ်ရ။ Code path များကို စာဖတ်သူအား “ဒီမှာသွားကြည့်ပါ” ဟု ပစ်ချမထားရ။ ပထမဦးစွာ သင်ခန်းစာကို ရှင်းပြပြီးမှ repo evidence ကိုထောက်ပြပါ။

## Safety

- လူပုဂ္ဂိုလ်၊ course၊ page၊ organization တိုက်ခိုက်မှုမပါရ။
- Platform-abuse, account misuse, stealth automation, harmful extraction, or evasion workflows မသင်ကြားရ။
- Browser agent အခန်းသည် hardening lesson ဖြစ်ရမည်။ Abuse manual မဖြစ်ရ။
- appv22 ကို final worker kernel, production maturity doctrine, final victory ဟုမရေးရ။

## Accuracy Markers

- မသေချာသော claim: `[SOURCE_NEEDED]`
- Manuscript/repo mismatch: `[SYNC_MISMATCH]`
- v0.2 သို့ရွှေ့မည့်အရာ: `[DEFER_V0_2]`
- Benchmark, absolute safety, or production maturity claim များကို source မရှိဘဲ မရေးရ။
