# Agentic AI Book

မြန်မာ Developer များအတွက် Agentic AI ကို လက်တွေ့အခြေခံနဲ့ နားလည်အောင် ရေးထားသော open-source book project ဖြစ်ပါတယ်။

ဒီ repo ရဲ့ အဓိကရည်ရွယ်ချက်က Agent, Tool Calling, RAG, MCP, Context Engineering, Coding Agent, DevOps Automation စတာတွေကို "ဘယ်လိုစဉ်းစားရမလဲ" ဆိုတဲ့ angle ကနေ ရှင်းပြဖို့ပါ။ Framework documentation ကို တိုက်ရိုက်ဘာသာပြန်ထားတာ မဟုတ်ပါ။ Production manual လည်း မဟုတ်ပါ။ Beginner ကနေ intermediate developer အထိ ဖတ်လို့ရအောင် practical thinking guide အနေနဲ့ ပြင်ဆင်ထားပါတယ်။

## What This Book Is

Agentic AI Book က AI agent system တွေကို developer mindset နဲ့ လေ့လာနိုင်အောင် စုစည်းထားတဲ့ manuscript project ပါ။

ဖတ်ရန်အစမှာ `book/chapters/00-license.md` နှင့် `book/chapters/00-preface.md` ဖြစ်သည်။ Chapter 12 မှ 15 အထိသည် repo-backed case study လေးခုဖြစ်သည်။

ဒီစာအုပ်မှာ theory တစ်ခုတည်းမဟုတ်ဘဲ:

- Agent loop ကို ဘယ်လိုမြင်ရမလဲ
- Tool တစ်ခုကို agent က သုံးတဲ့အခါ risk ဘယ်လိုစဉ်းစားရမလဲ
- Context, memory, RAG တို့က ဘာကွာလဲ
- MCP, skill, subagent ဆိုတာတွေကို beginner အနေနဲ့ ဘယ်လိုစတင်နားလည်ရမလဲ
- Coding agent နဲ့ DevOps automation ကို လုံခြုံစိတ်ချစွာ ဘယ်လိုသုံးမလဲ

ဆိုတာတွေကို တဖြည်းဖြည်းရှင်းပြဖို့ ရည်ရွယ်ထားပါတယ်။

## Who Should Read This

ဒီစာအုပ်က အောက်ပါသူတွေအတွက် ရေးထားပါတယ်။

- မြန်မာ developer များ
- AI agent / automation စတင်လေ့လာနေသူများ
- RAG, MCP, LangGraph, Coding Agent စတာတွေကို concept အနေနဲ့ နားလည်ချင်သူများ
- DevOps automation မှာ AI agent ထည့်သုံးဖို့ စဉ်းစားနေသူများ
- English technical docs ဖတ်နိုင်ပေမယ့် Burmese explanation နဲ့ ပိုမြန်မြန်နားလည်ချင်သူများ

## What Readers Will Learn

စာအုပ်ကို ဖတ်ပြီးရင် reader အနေနဲ့ အောက်ပါအရာတွေကို ပိုရှင်းရှင်းလင်းလင်းမြင်လာဖို့ မျှော်လင့်ပါတယ်။

- Agentic AI ဆိုတာ chatbot တစ်ခုထက် ဘာပိုလဲ
- Agent, workflow, automation တို့ကို ဘယ်လိုခွဲမလဲ
- Tool Calling / Function Calling ကို ဘယ်လိုအသုံးချမလဲ
- Context Engineering, Memory, RAG တို့ရဲ့ role
- Planner / Worker / Critic style agent pattern
- Guardrails, sandbox, permission, prompt injection စတဲ့ safety concerns
- Coding agent နဲ့ DevOps automation examples တွေကို ဘယ်လိုအကဲဖြတ်မလဲ

## Start Here / ဒီကစပါ 

Recommended reading order:

1. [License](book/chapters/00-license.md)
2. [Preface](book/chapters/00-preface.md)
3. [Agentic AI Basics](book/chapters/01-agentic-ai-basics.md)
4. [Agent vs Workflow vs Automation](book/chapters/02-agent-vs-workflow-vs-automation.md)
5. Continue chapter-by-chapter from the table of contents below.

If you are new to AI agents, start from Chapter 01. If you already know tool calling and RAG, you can jump to Chapter 06 or Chapter 07, then come back later.

## Table Of Contents

All links below point to existing manuscript files. Chapter prose is author-owned and should not be rewritten directly without prior discussion.

- [00 - License](book/chapters/00-license.md)
- [00 - Preface](book/chapters/00-preface.md)
- [00 - Thank You Note](book/chapters/00-thankyou_note.md)
- [01 - Agentic AI Basics](book/chapters/01-agentic-ai-basics.md)
- [02 - Agent vs Workflow vs Automation](book/chapters/02-agent-vs-workflow-vs-automation.md)
- [03 - LLM Tool Calling / Function Calling](book/chapters/03-llm-tool-calling-function-calling.md)
- [04 - Agent Loop](book/chapters/04-agent-loop.md)
- [05 - Agent Harness](book/chapters/05-agent-harness.md)
- [06 - MCP, Skill, Subagent](book/chapters/06-mcp-skill-subagent.md)
- [07 - Context Engineering, Memory, RAG](book/chapters/07-context-engineering-memory-rag.md)
- [08 - Planner, Worker, Verifier](book/chapters/08-planner-worker-verifier.md)
- [09 - Tool Broker, Permission, Mutation Scope](book/chapters/09-tool-broker-permission-mutation-scope.md)
- [10 - Observability, Trajectory, Reflection](book/chapters/10-observability-trajectory-reflection.md)
- [11 - Safety, Sandbox, Prompt Injection, Tool Output](book/chapters/11-safety-sandbox-prompt-injection-tool-output.md)
- [12 - P-2 Zero-Trust Multi-Agent Bridge](book/chapters/12-p2-zero-trust-multi-agent-bridge.md)
- [13 - Travis-2 Controlled Runtime](book/chapters/13-travis2-controlled-runtime.md)
- [14 - BrowserSurfer Browser Tool Agent Security](book/chapters/14-browsersurfer-browser-tool-agent-security.md)
- [15 - appv22 Emerging Runtime Recovery Lab](book/chapters/15-appv22-emerging-runtime-recovery-lab.md)
- [16 - DevOps Agent Thinking](book/chapters/16-devops-agent-thinking.md)
- [17 - Mini Labs](book/chapters/17-mini-labs.md)
- [18 - Myanmar Developer Roadmap](book/chapters/18-myanmar-developer-roadmap.md)
- [19 - References](book/chapters/19-references.md)

## Repository Structure

```text
.
├── README.md
├── CONTRIBUTING.md
├── ROADMAP.md
├── SECURITY.md
├── GLOSSARY.md
├── STYLE_GUIDE.md
├── STARTER_ISSUES.md
├── LICENSE-NEEDS-DECISION.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── LABELS.md
├── book/
│   ├── README.md
│   ├── LICENSE.md
│   └── chapters/
├── repo_sources/
├── scripts/
├── models
└── prompts
```

`book/` and `book/chapters/` are manuscript areas. Treat them carefully.

Useful file references:

- [book/README.md](book/README.md)
- [book/chapters/00-license.md](book/chapters/00-license.md)
- [book/chapters/00-preface.md](book/chapters/00-preface.md)

Repo-backed case study links:

1. [`P-2`](https://github.com/htooayelwinict/P-2)
2. [`travis-2`](https://github.com/htooayelwinict/travis-2)
3. [`bot / BrowserSurfer Bot`](https://github.com/htooayelwinict/bot)
4. [`allthebest / appv22`](https://github.com/htooayelwinict/allthebest)

## How To Contribute

Contribution လုပ်ချင်သူတွေကို ကြိုဆိုပါတယ်။ စာဖတ်သူတွေ ဖတ်ရတာ ပိုရှင်းသွားစေမယ့် small improvements တွေဆို အရမ်းအသုံးဝင်ပါတယ်။

ကူညီလို့ရတဲ့ contribution အမျိုးအစားတွေ:

- typo ပြင်ပေးခြင်း
- broken link report လုပ်ပေးခြင်း
- diagram suggestion ပေးခြင်း
- glossary ပိုရှင်းအောင် ကူညီခြင်း
- terminology consistency စစ်ပေးခြင်း
- beginner တွေအတွက် explanation ပိုလွယ်အောင် အကြံပေးခြင်း
- source/context ပါတဲ့ technical correction ပေးခြင်း
- issue discussion မှာ ပါဝင်ဆွေးနွေးခြင်း

အရေးကြီးတဲ့ rule:

Manuscript/chapter ကို အကြီးစား rewrite လုပ်ထားတဲ့ PR ကို တိုက်ရိုက်မပို့ပါနဲ့။ အရင် issue ဖွင့်ပြီး maintainer နဲ့ ဆွေးနွေးပေးပါ။ ဒီစာအုပ်မှာ author voice က အရေးကြီးပါတယ်။ အထူးသဖြင့် Burmese + English mixed explanation style ကို မပျက်စေချင်ပါ။

အသေးစိတ် guide ကို [CONTRIBUTING.md](CONTRIBUTING.md) မှာ ဖတ်နိုင်ပါတယ်။

## Roadmap Summary

လက်ရှိ roadmap focus:

- diagram တွေ ပိုကောင်းအောင် ပြင်ဆင်ခြင်း
- glossary နဲ့ terminology consistency ပိုခိုင်အောင်လုပ်ခြင်း
- beginner-friendly examples တွေ ထည့်ခြင်း
- MCP, RAG, memory, LangGraph explanation တွေ ပိုချဲ့ခြင်း
- safer DevOps automation နဲ့ tool-calling examples တွေ ထည့်ခြင်း
- new readers/contributors တွေအတွက် contribution workflow ပိုလွယ်အောင်လုပ်ခြင်း

အသေးစိတ်ကို [ROADMAP.md](ROADMAP.md) မှာ ကြည့်နိုင်ပါတယ်။

## License Note

Manuscript license note ကို လက်ရှိ [book/LICENSE.md](book/LICENSE.md) မှာ ထည့်ထားပါတယ်။

Root-level `LICENSE` file ကတော့ မရှိသေးပါ။ Wider reuse, packaging, distribution မလုပ်ခင် maintainer က root repository license ကို ရှင်းရှင်းလင်းလင်းရွေးပြီး ထည့်သင့်ပါတယ်။ ဒီအချက်အတွက် [LICENSE-NEEDS-DECISION.md](LICENSE-NEEDS-DECISION.md) ကို ကြည့်ပါ။

ဒီနေရာမှာ license ကို အလိုအလျောက် မရွေးထားပါ။

## Author Note

ဒီ project ကို ကျွန်တော် Htoo Aye Lwin က ရေးသားပြီး maintain လုပ်ထားပါတယ်။

ဒီစာအုပ် Repo ရဲ့ Goal က perfect sounding ဖြစ်ဖို့ မဟုတ်ပါ။ Myanmar developers တွေအတွက် Agentic AI ကို practical language နဲ့  real engineering caution ပါအောင် ပိုနားလည်လွယ်စေဖို့ပါ။

တစ်ခုခုဖတ်ရတာ မရှင်းဘူးဆိုရင် issue ဖွင့်ပေးပါ။ စာဖတ်သူတစ်ယောက် ဘယ်နေရာမှာ confuse ဖြစ်လဲဆိုတာက စာရေးသူအတွက် တကယ်အသုံးဝင်တဲ့ feedback ပါ။