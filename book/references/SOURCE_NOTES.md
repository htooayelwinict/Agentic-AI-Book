# Source Notes

## Uploaded Manuscript Sources

- `BOOK.md`: author mission, open-knowledge framing, humility, educational warning.
- `THANKYOU_NOTE.md`: named acknowledgement section.
- `CHAPTER-1.md`: Agentic AI, Agent vs Workflow, n8n examples, initial LLM explanation.
- `agent_harness_vs_loop_report_my.md`: Agent Loop, Agent Harness, loop-inside-harness mental model.
- `agent_harness_vs_loop_report.md`: English terminology reference only.
- `agent_harness_vs_loop_report.pdf`: visual/layout reference only.
- `CHAPTER-6.md`: Travis-2 chapter base.
- `CHAPTER-7.md`: DeepAgents/FacebookSurfer chapter base.
- `prompts`: workflow/prompt style reference only; content not copied.
- `models`: provider/model reference only; config values not copied.

## Repo Docs/Code Sources

| Local source | GitHub repo |
| ------------ | ----------- |
| `repo_sources/P-2` | `https://github.com/htooayelwinict/P-2` |
| `repo_sources/travis-2` | `https://github.com/htooayelwinict/travis-2` |
| `repo_sources/bot` | `https://github.com/htooayelwinict/bot` |
| `repo_sources/allthebest` | `https://github.com/htooayelwinict/allthebest` |

- `repo_sources/P-2/README.md`
- `repo_sources/P-2/docs/ARCHITECTURE-ROUTING.md`
- `repo_sources/P-2/src/multi_agent_app/runtime.py`
- `repo_sources/P-2/src/multi_agent_app/states.py`
- `repo_sources/P-2/src/multi_agent_app/nodes.py`
- `repo_sources/P-2/src/multi_agent_app/classifier.py`
- `repo_sources/travis-2/docs/travis_2/TRAVIS_2_ARCHITECTURE.md`
- `repo_sources/travis-2/docs/travis_2/TRAVIS_2_HANDOVER_REPORT.md`
- `repo_sources/travis-2/docs/travis_2/TRAVIS_2_ISSUES.md`
- `repo_sources/travis-2/docs/travis_2/TRAVIS_2_CODE_REVIEW.md`
- `repo_sources/travis-2/src/travis_2/agent.py`
- `repo_sources/travis-2/src/travis_2/tools.py`
- `repo_sources/travis-2/src/travis_2/sandbox/docker_runner.py`
- `repo_sources/travis-2/src/travis_2/sandbox/network.py`
- `repo_sources/travis-2/src/travis_2/validators/code_validator.py`
- `repo_sources/travis-2/src/travis_2/validators/typescript_validator.js`
- `repo_sources/travis-2/src/travis_2/utils/state.py`
- `repo_sources/travis-2/src/travis_2/utils/nodes.py`
- `repo_sources/travis-2/src/travis_2/utils/middleware.py`
- `repo_sources/travis-2/src/travis_2/cli.py`
- `repo_sources/travis-2/travis2_skills/skills/websearch/SKILL.md`
- `repo_sources/travis-2/tests/test_travis_2_tools.py`
- `repo_sources/travis-2/tests/test_travis_2_sandbox.py`
- `repo_sources/travis-2/tests/test_travis_2_validator.py`
- `repo_sources/bot/docs/system-architecture.md`
- `repo_sources/bot/docs/security_analysis_report.md`
- `repo_sources/bot/src/agents/facebook_surfer.py`
- `repo_sources/bot/src/agents/planner.py`
- `repo_sources/bot/src/tools/registry.py`
- `repo_sources/bot/src/tools/security.py`
- `repo_sources/bot/src/metrics/trajectory_callback.py`
- `repo_sources/bot/src/metrics/scoring.py`
- `repo_sources/bot/src/metrics/pii_redaction.py`
- `repo_sources/bot/src/storage/trajectory_store.py`
- `repo_sources/bot/src/agents/reflection.py`
- `repo_sources/bot/src/session/__init__.py`
- `repo_sources/allthebest/README.md`
- `repo_sources/allthebest/docs/appv22-recovery-audit.md`
- `repo_sources/allthebest/appV2.2/appv22/`
- `repo_sources/allthebest/appV2.2/tests/test_no_appv21_coupling.py`
- `repo_sources/allthebest/appV2.2/tests/test_coding_agent.py`
- `repo_sources/allthebest/appV2.2/tests/test_compaction_timing.py`
- `repo_sources/allthebest/appV2.2/tests/test_ai_appv2_env_provider.py`

## Official Docs Verified For v0.1

- LangGraph overview/persistence: `https://docs.langchain.com/oss/python/langgraph/overview`, `https://docs.langchain.com/oss/python/langgraph/persistence`
- LangChain agents/tools/middleware: `https://docs.langchain.com/oss/python/langchain/agents`, `https://docs.langchain.com/oss/python/langchain/tools`, `https://docs.langchain.com/oss/python/langchain/middleware/overview`
- DeepAgents overview: `https://docs.langchain.com/oss/python/deepagents/overview`
- MCP specification: `https://modelcontextprotocol.io/specification/2025-06-18`
- Playwright intro: `https://playwright.dev/docs/intro`
- Qdrant collections/vector concept: `https://qdrant.tech/documentation/manage-data/collections/`
- OWASP Prompt Injection: `https://owasp.org/www-community/attacks/PromptInjection`
- Terraform plan/apply: `https://developer.hashicorp.com/terraform/cli/commands/plan`, `https://developer.hashicorp.com/terraform/cli/commands/apply`
- AWS IAM best practices and CloudTrail: `https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html`, `https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html`
- GitHub Actions overview: `https://docs.github.com/en/actions/get-started/understand-github-actions`
- Pi official site and repository: `https://pi.dev`, `https://github.com/earendil-works/pi`
- Hermes Agent official site and repository: `https://hermes-agent.org`, `https://github.com/NousResearch/hermes-agent`

## [SOURCE_NEEDED] / Not Verified For v0.1

- Broad 2026 comparisons of OpenAI Agents SDK, Claude Agent SDK, Google ADK, Microsoft Agent Framework, CrewAI, Hermes, Pi.
- Pi/Hermes historical timeline claims beyond the official sites, public repos, and appv22 repo-local source comments.
- "OpenClaw is just Pi" style claim. Verified public source only supports a narrower statement: OpenClaw third-party notices say portions were adapted from Pi/pi-mono and OpenClaw depends on `@earendil-works/pi-tui`.
- Official OpenAI documentation for tool/function calling and Agents concepts, if later used as broad product/API explanation.

## Claims Not To Publish Until Verified

- Any benchmark number.
- Any unsupported production maturity statement.
- Any absolute safety statement.
- Any final license claim.
- Any claim that OpenClaw is “just Pi”; source-level evidence supports only adapted portions from Pi/pi-mono plus `@earendil-works/pi-tui` dependency.
- Any appv22 claim implying final worker-kernel maturity.

## Image Publication Notes

Images and screenshots:
Unless explicitly stated otherwise, screenshots and images used in this book are for educational explanation, architecture evidence, or author-owned demo/reference purposes. Third-party logos, platform screenshots, external images, and quoted materials may have separate rights and are not automatically covered by the book’s CC BY-NC-SA 4.0 license.

- Chapter 13 Travis-2 images are local demo screenshots used to explain `run_playwright_code`, structured result quality, and current-date execution through tool boundary.
- Chapter 14 BrowserSurfer selected images are author-owned demo screenshots. They show a safe demo flow, terminal traces, and browser-agent state surfaces. They must be read as architecture evidence, not as platform-use instructions.
- Raw BrowserSurfer screenshot folders include many unused images. Only `book/references/images/websurfer/selected/browsersurfer-actual-*.png` are referenced by Chapter 14.

## Web References Added In Restart Pass

- LangGraph quickstart: `https://docs.langchain.com/oss/python/langgraph/quickstart`
- DeepAgents overview: `https://docs.langchain.com/oss/python/deepagents/overview`
- MCP specification: `https://modelcontextprotocol.io/specification/2025-06-18`
- Qdrant concepts: `https://qdrant.tech/documentation/concepts/`
- OWASP Prompt Injection: `https://owasp.org/www-community/attacks/PromptInjection`
- Business Insider loop-engineering article: `https://www.businessinsider.com/what-are-loops-ai-engineering-tips-2026-6`
- TechRadar OpenClaw overview: `https://www.techradar.com/pro/what-is-openclaw`
- TechRadar OpenClaw skills guide: `https://www.techradar.com/pro/what-are-openclaw-skills-a-detailed-guide`
- TechRadar OpenClaw security risks: `https://www.techradar.com/pro/here-are-the-openclaw-security-risks-you-should-know-about`
- OpenClaw third-party notices for Pi/pi-mono adapted portions and `@earendil-works/pi-tui` dependency: `https://raw.githubusercontent.com/openclaw/openclaw/main/THIRD_PARTY_NOTICES.md`
- OpenClaw safety analysis: `https://arxiv.org/abs/2604.04759`
- OpenClaw vulnerability taxonomy: `https://arxiv.org/abs/2603.27517`
- Additional OpenClaw/security context checked during restart:
  - TechRadar workflow automation article: `https://www.techradar.com/pro/how-to-automate-workflows-using-open-source-ai-agents`
  - TechRadar agent guardrails article: `https://www.techradar.com/pro/phishing-the-agent-why-ai-guardrails-arent-enough`
  - ClawSafety benchmark paper: `https://arxiv.org/abs/2604.01438`
  - Systematic OpenClaw variants evaluation: `https://arxiv.org/abs/2604.03131`
