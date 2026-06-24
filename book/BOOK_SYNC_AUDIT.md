# Book Sync Audit

| Uploaded manuscript | Target chapter | Repo evidence | Usable now | Rewrite needed | Verification needed | v0.2 defer |
| ------------------- | -------------- | ------------- | ---------- | -------------- | ------------------- | ---------- |
| `BOOK.md` | `chapters/00-preface.md`, `README.md` | N/A | Yes | Light formatting only | Open-knowledge framing preserved | None |
| `THANKYOU_NOTE.md` | `chapters/00-preface.md` acknowledgement | N/A | Yes | Light formatting only | Named acknowledgements preserved | None |
| `CHAPTER-1.md` | `chapters/01-agentic-ai-basics.md`, `02`, `03` | N/A | Yes | Moderate technical correction | LLM/Transformer/Attention explanation corrected | Full NLP history |
| `agent_harness_vs_loop_report_my.md` | `chapters/04`, `05`, `08`, `09` | Repo case studies reinforce concepts | Yes | Heavy condensation | Current-framework claims marked `[SOURCE_NEEDED]` where not repo-backed | Broad 2026 framework comparison |
| `agent_harness_vs_loop_report.md` | Reference only | N/A | Yes | Do not copy formatting artifacts | English terminology cross-check only | Full translation comparison |
| `agent_harness_vs_loop_report.pdf` | Visual/layout reference only | N/A | Yes | No prose extraction | Table/section shape only | PDF layout polish |
| `CHAPTER-6.md` | `chapters/13-travis2-controlled-runtime.md` | `repo_sources/travis-2` / `https://github.com/htooayelwinict/travis-2` | Yes | Condense and sync with current repo | Travis-2 architecture, issues, code verified | Full handover conversion |
| `CHAPTER-7.md` | `chapters/14-browsersurfer-browser-tool-agent-security.md` | `repo_sources/bot` | Yes | Rename public case to BrowserSurfer; add safety framing | Security analysis and code anchors verified | Full tool inventory and rewrite plan |
| `prompts` | Style/prompt workflow reference only | N/A | Yes | Do not blindly insert | No common sensitive markers detected | Prompt library appendix |
| `models` | Provider/model configuration reference only | N/A | Yes | Do not copy config values | No common sensitive markers detected | Provider setup appendix |

## Repo Access Audit

| Repo | Local source | HEAD | Required files available | Result |
| ---- | ------------ | ---- | ------------------------ | ------ |
| `https://github.com/htooayelwinict/P-2` | `repo_sources/P-2` | `e270841` | Yes | Incorporated |
| `https://github.com/htooayelwinict/travis-2` | `repo_sources/travis-2` | `b17c968` | Yes | Incorporated |
| `https://github.com/htooayelwinict/bot` | `repo_sources/bot` | `6614286` | Yes | Incorporated |
| `https://github.com/htooayelwinict/allthebest` | `repo_sources/allthebest` | `bd0152a` | Yes | Incorporated |
