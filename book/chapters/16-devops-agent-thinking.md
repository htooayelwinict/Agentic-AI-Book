# ၁၆။ DevOps Agent Thinking — Cloud နန်းတော်ထဲသို့ မျက်စိမှိတ် မဝင်စေရန်

### Cloud သည် ကစားကွင်းမဟုတ်

Agentic AI ကို DevOps ထဲသုံးမည်ဆိုလျှင်စိတ်လှုပ်ရှားစရာများစွာရှိသည်။ Agent သည် CI logs ဖတ်နိုင်သည်။ Terraform plan ကိုရှင်းပြနိုင်သည်။ CloudWatch log အရှည်ကြီးကိုအကျဉ်းချုပ်နိုင်သည်။ Runbook ဖတ်ပြီး next step အကြံပြုနိုင်သည်။ Pull request failure ကို file/line ဖြင့်ချိတ်နိုင်သည်။ Cost anomaly အကြောင်း report ထုတ်နိုင်သည်။

သို့သော် DevOps သည်ကစားကွင်းမဟုတ်။ Terraform apply မှားလျှင်เงินจริงကုန်နိုင်သည်။ AWS permission မှားလျှင် resource leak ဖြစ်နိုင်သည်။ CI log ထဲမှ secret ထွက်သွားနိုင်သည်။ Production database ကိုမတော်တဆထိနိုင်သည်။ DNS record တစ်ကြောင်းမှားလျှင် service တစ်ခုလုံးပျောက်နိုင်သည်။

ထို့ကြောင့် DevOps Agent Thinking ဆိုသည်မှာ "Agent ကို cloud tool ပေးလိုက်မယ်" ဟူသောအတွေးမဟုတ်။ Permission, read/write separation, human approval, audit log, rollback, blast radius, source evidence တို့ကိုအရင်စဉ်းစားခြင်းဖြစ်သည်။

ဤအခန်းသည် production manual မဟုတ်။ Beginner-friendly engineer handbook အဖြစ် DevOps agent ကိုဘယ်လိုစဉ်းစားရမည်ဆိုတာသင်ပေးရန်ဖြစ်သည်။

### အရင်ဆုံး ဖတ်ခိုင်းပါ၊ မပြောင်းခိုင်းပါနှင့်

DevOps agent ကိုစတင်ရာတွင် read-only tasks မှစသင့်သည်။ အကြောင်းမှာ read-only task များသည်အမှားရှိနိုင်သော်လည်း system state ကိုမပြောင်းစေသောကြောင့်ဖြစ်သည်။

အရင်ဆုံးစမ်းသင့်သော ဖတ်ရန်အလုပ်များ:

CI failure summary။

Terraform plan explanation။

Cloud log summary။

Runbook Q&amp;A။

Incident timeline draft။

Pull request risk checklist။

Cost report explanation။

Security advisory triage။

Mutating tasks များကိုနောက်မှသာစဉ်းစားပါ။

Terraform apply။

Kubernetes deploy/rollback။

AWS resource create/delete။

Secret rotation။

DNS change။

Database migration။

CI/CD pipeline modification။

အထူးသဖြင့် အောက်ပါစည်းကမ်းကို DevOps agent design ၏တံခါးပေါ်တွင်ကပ်ထားသင့်သည်။

```text
Deployment, secret rotation, production database, DNS, IAM, and destructive commands must be default-disabled and human-approved.
```

မြန်မာလိုပြောလျှင် deploy လုပ်ခြင်း၊ secret လှည့်ပြောင်းခြင်း၊ production database ထိခြင်း၊ DNS ပြောင်းခြင်း၊ IAM ပြင်ခြင်း၊ destructive command မောင်းခြင်းတို့သည် default အားဖြင့်ပိတ်ထားရမည်။ လူ့အတည်ပြုချက်ရမှသာဖွင့်ရမည်။

Beginner project တွင် mutating DevOps tools ကို Agent ထဲမထည့်သင့်။ အရင်ဆုံး read-only assistant, verifier, reporter အဖြစ်တည်ဆောက်ပါ။ စာရေးတော်ကိုနန်းတော်မြေပုံဖတ်ခိုင်းပါ။ နန်းတော်တံခါးဖွင့်သော့ကိုမပေးသေးပါနှင့်။

### P-2 သင်ခန်းစာ — Internal Note နှင့် Public Message ကြားတံတား

Incident response တွင် internal diagnosis ကို public status update အဖြစ်ပြောင်းရန်လိုနိုင်သည်။ Internal note ထဲတွင် hostnames, internal IP, customer-specific detail, secret-like values, unfinished diagnosis ပါနိုင်သည်။ Public message ထဲတွင်ထိုအရာများမပါသင့်။

P-2 ၏ Bridge pattern ကို DevOps communication တွင်အသုံးချနိုင်သည်။

```text
Ops Supervisor Agent
  - internal runbooks
  - incident logs
  - private diagnosis

Bridge
  - internal diagnosis -> public-safe wording
  - minimum projection only
  - no secrets
  - no internal hostnames

Public Status Agent
  - public status template
  - customer-safe language
```

အရေးကြီးသည်မှာ internal state အကုန် public status agent ဆီမပို့ရန်ဖြစ်သည်။ Public update ထုတ်ရန်လိုသောအချက်များကိုသာ project လုပ်ပါ။ P-2 မှသင်ရသည့် state boundary သည် DevOps comms တွင်အလွန်အသုံးဝင်သည်။

### Travis-2 သင်ခန်းစာ — Command Run သွားသည်ဆို၍ အလုပ်ပြီးမဟုတ်

DevOps agent သည် flexible tool use လိုနိုင်သည်။ Logs ဖတ်ရမည်။ GitHub Actions failure ဖတ်ရမည်။ Terraform plan parse လုပ်ရမည်။ သို့သော် command တစ်ကြောင်း run သွားသည်ဆိုရုံနှင့်အလုပ်ပြီးပြီဟုမဆိုရ။ Travis-2 မှယူရမည့်သင်ခန်းစာမှာ အလုပ်သမားကိုအလုပ်ခန်းထဲသို့ပို့ပြီး ပြန်လာသောအထောက်အထားကိုစစ်ရန်ဖြစ်သည်။ Docker sandbox ထဲတွင် script run စေခြင်းသည် DevOps task များအတွက်လည်းစဉ်းစားစရာကောင်းသော boundary ဖြစ်သည်။

```text
run_analysis
  -> evaluate_evidence
  -> replan_if_missing_data
  -> finalize_report
```

Travis-2 မှယူရမည့်အရေးကြီးဆုံးအချက်တစ်ခုမှာ `execution_ok` နှင့် `data_ok` ခွဲခြင်းဖြစ်သည်။ CI log fetch command အောင်မြင်သော်လည်း relevant error မတွေ့ပါက `data_ok=false` ဖြစ်သင့်သည်။ Terraform plan parse အောင်မြင်သော်လည်း destroy count မထုတ်နိုင်ပါက failure ဖြစ်သင့်သည်။ အင်ဂျင်နီယာအလုပ်တွင် "ပြေးသွားသည်" နှင့် "အသုံးဝင်သောအဖြေပြန်ရသည်" သည်မတူ။

DevOps agent တွင် "command ran successfully" သည် "analysis correct" မဟုတ်။ Shell exit code 0 သည်အမှန်တရား၏တံဆိပ်မဟုတ်။ Evidence စစ်ရမည်။

### BrowserSurfer သင်ခန်းစာ — Log နှင့် Issue Comment ကိုမယုံပါနှင့်

BrowserSurfer မှသင်ခန်းစာသည် browser တစ်ခုတည်းအတွက်မဟုတ်။ DevOps world တွင်လည်း untrusted text အများကြီးရှိသည်။ CI log ထဲတွင် malicious-looking instruction ပါနိုင်သည်။ GitHub issue comment ထဲတွင် model ကိုလမ်းလွဲစေသောစာပါနိုင်သည်။ Terraform plan output ထဲတွင် secret-like values ပါနိုင်သည်။ Alert description ထဲတွင် external user input ပါနိုင်သည်။

ထို့ကြောင့် DevOps agent တွင် tool output ကို data အဖြစ်သာကိုင်ရမည်။

လိုအပ်သော safety pieces:

Untrusted log wrapper။ ဤနေရာတွင် wrapper ဆိုသည်မှာ log ကို "instruction မဟုတ်၊ untrusted data" ဟုအကာအကွယ်အိတ်ဖြင့်ပတ်ပေးခြင်းဖြစ်သည်။ ၎င်းတစ်ခုတည်းဖြင့်ဘေးကင်းသွားခြင်းမဟုတ်။

Secret redaction။

Command allowlist။

Read-only credentials။

No automatic mutation။

Approval-gated mutation။

Audit log။

Source references။

DevOps agent သည် logs ဖတ်နိုင်သော်လည်း logs ကိုအမိန့်အဖြစ်မယူသင့်ချေ။

### appv22 သင်ခန်းစာ — Incident သည် Context ကိုပြည့်စေတတ်သည်

DevOps task များတွင် context အရှည်ကြီးများလာတတ်သည်။ Incident logs, CI output, Terraform plan, cloud inventory, runbook docs, Slack thread, GitHub issue, dashboard alert တို့အားလုံးတစ်ခါတစ်ရံတစ်ပြိုင်နက်လိုသည်။ Context overflow ဖြစ်နိုင်သည်။ Provider error ဖြစ်နိုင်သည်။ Tool output cap ထိနိုင်သည်။

appv22 မှယူရမည့်သင်ခန်းစာမှာ recovery engineering ဖြစ်သည်။ Context compaction, overflow recovery, faux/offline provider tests, tool-loop guardrails, session persistence, terminal status တို့ကိုစဉ်းစားပါ။ ဤနေရာတွင် terminal status ဆိုသည်မှာ command line ထဲတွင် agent ဘာလုပ်နေသလဲ၊ ဘယ်အဆင့်ရောက်နေသလဲ user ကိုပြသောအခြေအနေပြစာများဖြစ်သည်။ DevOps agent သည် "command run and answer" မဟုတ်။ Failure ဖြစ်လျှင်ဘာလုပ်မလဲဆိုတာပါ runtime design ထဲရှိရမည်။

### Terraform Agent Thinking

Terraform နှင့် Agent ချိတ်မည်ဆိုပါက read-only အဆင့်မှစပါ။

အရင်ဆုံးစမ်းသင့်သော ဖတ်ရန်အလုပ်များ:

`terraform fmt -check` result summary။

`terraform validate` result explanation။

`terraform plan` output summary။

Resource add/change/destroy count explanation။

Risky change highlight။

Missing tag/policy check။

လူ့အတည်ပြုချက်မရှိဘဲ မလုပ်ရမည့်အလုပ်များ:

`terraform apply`။

`terraform destroy`။

State file manipulation။

Provider credential changes။

Backend migration။

Terraform plan verifier တွင်အောက်ပါ signals ထည့်နိုင်သည်။

Destroy count &gt; 0။

Replacement count &gt; 0။

Public ingress added။

IAM wildcard permission။

Unencrypted storage။

Missing tags။

Cost-impacting resource class။

Agent သည် plan ကိုရှင်းပြနိုင်သည်။ Apply ကိုအလိုအလျောက်မလုပ်သင့်။ Human approval, plan artifact, diff summary, policy check, rollback plan, audit log မရှိဘဲ mutation မလုပ်ပါနှင့်။

### AWS Agent Thinking

AWS tools ကို Agent ပေးမည်ဆိုပါက IAM scope အရေးကြီးသည်။ Full admin credential မပေးပါနှင့်။ Read-only role မှစပါ။ Service-specific policy သုံးပါ။ Session duration ကန့်သတ်ပါ။ CloudTrail audit log သုံးပါ။

Read-only AWS tasks:

EC2 inventory summary။

CloudWatch log summary။

IAM policy risk explanation။

S3 bucket public access check။

Cost Explorer report summary။

Security Hub finding triage။

Mutating AWS tasks:

Create/delete resources။

Modify IAM policies။

Change security groups။

Deploy Lambda/ECS/EKS။

Mutating tasks များတွင် approval, change plan, rollback, blast radius summary လိုသည်။ Agent ကို cloud palace ထဲဝင်ခွင့်ပေးမည်ဆိုလျှင် အခန်းတံခါးတစ်ခန်းချင်းစီအတွက်သော့ခွဲပေးပါ။ နန်းတော် master key မပေးပါနှင့်။

### CI/CD Agent Thinking

CI/CD agent သည် beginner များအတွက်အသုံးဝင်ဆုံးစတင်ရာဖြစ်နိုင်သည်။ CI failure logs ဖတ်၍ error summary ပေးနိုင်သည်။ Test failure ကို file/line နှင့်ချိတ်နိုင်သည်။ Flaky test pattern ရှာနိုင်သည်။ Pull request checklist ထုတ်နိုင်သည်။

သို့သော် CI logs ထဲတွင် sensitive values ပါနိုင်သည်။ Build output ထဲတွင် untrusted text ပါနိုင်သည်။ PR comments များသည် prompt injection source ဖြစ်နိုင်သည်။ CI bot ကို repository write permission ပေးလျှင်အန္တရာယ်တက်သည်။

Safe architecture:

```text
read logs
  -> sanitize output
  -> extract failing test names
  -> cite file/line/test name
  -> suggest fix
  -> human applies or approves
```

CI failure walkthrough တစ်ခုကြည့်ပါ။ GitHub Actions log ထဲတွင် `tests/test_auth.py::test_login_redirect failed` ဟုတွေ့သည်။ Agent သည် log တစ်ခုလုံးကိုအမိန့်အဖြစ်မဖတ်သင့်ချေ။ ပထမဆုံး failing test name ကိုထုတ်သည်။ နောက် `AssertionError: expected 302 got 200` ကို evidence အဖြစ်ယူသည်။ ထို့နောက် related file path ကို cite လုပ်သည်။ "redirect behavior မလုပ်တော့သောကြောင့် test fail ဖြစ်နိုင်သည်" ဟု hypothesis ထုတ်သည်။ သို့သော် auto-commit မလုပ်သင့်ချေ။ Developer ကို diff suggestion နှင့် test command ပေးရုံဖြင့်ရပ်ရမည်။ ဤသည် read-only CI assistant ၏ဘေးကင်းသောအလုပ်ပုံစံဖြစ်သည်။

Agent auto-commit လုပ်မည်ဆိုပါက branch isolation, tests, diff review, approval, secret scan လိုသည်။ Beginner phase တွင်အရင်ဆုံး report-only mode ဖြင့်စပါ။

### Tool Policy ဥပမာ

DevOps agent tool policy ကိုဤသို့ရေးနိုင်သည်။

```yaml
tools:
  terraform_plan:
    mode: read_only
    approval: false
  terraform_apply:
    mode: mutate
    approval: required
    default: disabled
  aws_describe:
    mode: read_only
    role: readonly
  aws_modify:
    mode: mutate
    approval: required
    default: disabled
  read_ci_logs:
    mode: read_only
    sanitize: true
  create_pr_comment:
    mode: mutate
    approval: required
```

ဤ YAML သည် illustrative example ဖြစ်သည်။ Actual implementation မဟုတ်။ အဓိကသင်ခန်းစာမှာ tools ကို mode, approval, credential scope အလိုက်ခွဲရန်ဖြစ်သည်။

### Beginner အတွက် Architecture

DevOps assistant တစ်ခုကို safe beginner project အဖြစ်ဒီလိုတည်ဆောက်နိုင်သည်။

```text
User asks:
  "Why did CI fail?"

Agent flow:
  1. read CI logs
  2. sanitize output
  3. extract failing test names
  4. retrieve related files
  5. summarize likely cause
  6. verifier checks evidence
  7. final report with manual commands
```

ဤ flow တွင် mutation မရှိသေး။ Safe learning project အတွက်ကောင်းသည်။ နောက်တစ်ဆင့်တွင် PR comment draft ထုတ်နိုင်သည်။ သို့သော် post action ကို approval-gated လုပ်ပါ။

### စာဖတ်သူကိုယ်တိုင် ပြန်စစ်ပြင်ကြည့်ရန်

1. Terraform plan output sample တစ်ခုယူပြီး destroy count, replacement count, IAM wildcard ကို detect လုပ်သော parser ရေးပါ။
2. CI log summary agent တစ်ခုရေးပါ။ Raw log ကို 8KB cap လုပ်ပြီး secret-looking strings redact လုပ်ပါ။
3. P-2 style bridge သုံး၍ internal incident note မှ public-safe status update ထုတ်ပါ။
4. Travis-2 style `execution_ok/data_ok` schema ကို DevOps tool result တွင်သုံးပါ။
5. BrowserSurfer style prompt injection test ကို fake/local CI log ထဲထည့်ပြီး wrapper မရှိ/ရှိ version နှိုင်းပါ။
6. appv22 style faux provider ဖြင့် DevOps agent tests ကို network မလိုဘဲ run ပါ။ Faux provider ဆိုသည်မှာ real model API မခေါ်ဘဲ test အတွက်ပြန်ဖြေသော provider အတုဖြစ်သည်။

### နိဂုံး — Cloud Agent သည် စာရေးတော်သာမဟုတ်၊ အာဏာကိုင်သူဖြစ်သည်

DevOps Agent Thinking သည် cloud tool များပေးခြင်းမဟုတ်။ Read-only first, least privilege, approval-gated mutation, evidence-based verifier, audit log, redaction, recovery engineering တို့ပေါင်းစပ်ခြင်းဖြစ်သည်။

P-2 သည် privilege separation ကိုသင်ပေးသည်။ Travis-2 သည် model ရေးလာသော code ကို sandbox/tool-result contract ဖြင့်ထိန်းသည့် runtime စည်းကမ်းကိုသင်ပေးသည်။ BrowserSurfer သည် external tool output risk ကိုသင်ပေးသည်။ appv22 သည် recovery engineering ကိုသင်ပေးသည်။

Beginner developer အနေဖြင့် DevOps agent ကိုစမည်ဆိုပါက Terraform apply လုပ်တာမျိုးနဲ့မစပါနှင့်။ CI failure summary, Terraform plan explanation, log triage ကဲ့သို့ read-only tasks မှစပါ။ စာရေးတော်ကိုမြေပုံဖတ်တတ်အောင်သင်ပါ။ နန်းတော်သော့ကိုနောက်မှသာစဉ်းစားပါလော့။

---

**စာဖတ်သူအတွက် Source Notes:**

- **Repo-backed lessons:** P-2 မှ privilege separation, Travis-2 မှ sandboxed executable tool runtime, BrowserSurfer မှ untrusted tool output, appv22 မှ recovery engineering ကိုယူထားသည်။
- **DevOps terms:** Terraform, AWS, CI/CD တို့ကို educational examples အဖြစ်သုံးထားသည်။ Terraform plan/apply, AWS IAM/CloudTrail, GitHub Actions concept များကို official docs ဖြင့် v0.1 အတွက်စစ်ထားသည်။ Provider-specific deep command walkthrough များကို v0.2 တွင်သာချဲ့မည်။
- **Safety position:** Read-only first ဖြစ်သည်။ Mutation လုပ်ရန် approval, audit, rollback thinking, narrow credentials လိုသည်။

