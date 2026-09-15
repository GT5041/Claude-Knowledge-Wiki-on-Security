# Claude Security — Knowledge Wiki

> A single, source-traceable reference for how security works across Claude (the models, the API, Claude Code, and the enterprise products).
>
> **Last verified:** 2026-09-15 · **Maintainer:** repository owners · **Primary upstream source:** [Anthropic Trust Center](https://trust.anthropic.com)
>
> 🌐 **日本語版:** [Claude-Security.ja.md](Claude-Security.ja.md)

Every claim on this page carries a source tag such as `[S3]`. Resolve tags in the [Source register](#source-register). Nothing here supersedes Anthropic's own documentation or your contract — when this page and an official source disagree, the official source wins, and the page should be corrected.

---

## How to use this page

The same body of knowledge is indexed three ways so you can enter from whichever direction you are coming from:

| Entry point | Use it when | Go to |
|---|---|---|
| **By theme** | You know the topic ("data retention", "sandboxing") | [Theme index](#theme-index) → `T1`–`T11` |
| **By interest** | You know your role ("I'm the CISO", "I'm a developer") | [Interest index](#interest-index) → `I1`–`I7` |
| **By question** | You have a concrete question to answer | [FAQ](#faq) → `Q1`–`Q22` |

### Traceability model

| ID | Meaning | Example |
|---|---|---|
| `T#` | Theme — a subject area, with its own section below | `T2` Data handling |
| `I#` | Interest — a role/audience lens, mapping to themes and questions | `I3` Compliance & privacy |
| `Q#` | FAQ entry, tagged with the themes it belongs to | `Q3` What is ZDR? |
| `S#` | Official source in the [Source register](#source-register) | `[S2]` Claude Code data usage docs |

> **IDs are shared with the Japanese version.** `T5` is the same theme in both languages, `Q12` the same question, so audit notes can cite an ID regardless of which language the reader used.

Each theme section lists its sources. Each FAQ answer links back to its theme(s) and its source(s). Each interest lists the themes and questions that matter to it. That makes any statement on this page walkable in both directions: *claim → source*, and *source → everything derived from it*.

---

## Theme index

| ID | Theme | Covers | Main sources |
|---|---|---|---|
| [`T1`](#t1--governance-certifications-and-compliance) | Governance, certifications & compliance | Trust Center, SOC 2 / ISO, BAA, terms, usage policy | `[S1]` `[S3]` `[S9]` |
| [`T2`](#t2--data-handling-retention-and-model-training) | Data handling, retention & model training | What is sent, what is stored, for how long, training policy | `[S2]` `[S5]` |
| [`T3`](#t3--zero-data-retention-and-regulated-workloads) | Zero data retention & regulated workloads | ZDR scope and gaps, HIPAA readiness, Covered Models | `[S4]` `[S5]` |
| [`T4`](#t4--model-level-safety-and-safeguards) | Model-level safety & safeguards | Responsible scaling, usage policy, system cards, classifiers | `[S9]` `[S10]` `[S11]` |
| [`T5`](#t5--prompt-injection-and-untrusted-content) | Prompt injection & untrusted content | Direct vs indirect injection, product safeguards, app-level mitigations | `[S1]` `[S7]` `[S12]` |
| [`T6`](#t6--agent-permissions-and-the-approval-model) | Agent permissions & the approval model | Permission modes, allow/deny rules, working-directory boundary | `[S1]` `[S8]` |
| [`T7`](#t7--isolation-and-sandboxing) | Isolation & sandboxing | Bash sandbox, sandbox runtime, containers, gVisor, VMs | `[S6]` `[S7]` |
| [`T8`](#t8--identity-access-and-enterprise-administration) | Identity, access & enterprise administration | SSO/SCIM, RBAC, managed settings, login pinning, gateways | `[S3]` `[S4]` `[S13]` |
| [`T9`](#t9--network-and-deployment-security) | Network & deployment security | Proxies, egress control, cloud execution, provider choice | `[S1]` `[S2]` `[S7]` |
| [`T10`](#t10--monitoring-audit-and-compliance-operations) | Monitoring, audit & compliance operations | OpenTelemetry, Compliance API, Activity Feed, audit log export | `[S13]` `[S1]` |
| [`T11`](#t11--supply-chain-mcp-and-vulnerability-reporting) | Supply chain, MCP & vulnerability reporting | MCP/connector trust, third-party data, HackerOne | `[S1]` `[S3]` |

---

## Interest index

Pick the row that matches your job. Each row is an ordered reading path.

### `I1` — CISO / security leadership
*Question you are really answering: "can we deploy this, and what is the residual risk?"*
- Themes: [`T1`](#t1--governance-certifications-and-compliance) → [`T2`](#t2--data-handling-retention-and-model-training) → [`T4`](#t4--model-level-safety-and-safeguards) → [`T5`](#t5--prompt-injection-and-untrusted-content) → [`T10`](#t10--monitoring-audit-and-compliance-operations)
- Questions: [`Q1`](#q1) [`Q2`](#q2) [`Q5`](#q5) [`Q8`](#q8) [`Q16`](#q16)
- Start with: Trust Center `[S1]`, plus Anthropic's CISO guide to agentic AI `[S11]`.

### `I2` — Security architect / AppSec engineer
*"How do I build a boundary around an agent that writes and runs code?"*
- Themes: [`T5`](#t5--prompt-injection-and-untrusted-content) → [`T6`](#t6--agent-permissions-and-the-approval-model) → [`T7`](#t7--isolation-and-sandboxing) → [`T9`](#t9--network-and-deployment-security) → [`T11`](#t11--supply-chain-mcp-and-vulnerability-reporting)
- Questions: [`Q7`](#q7) [`Q8`](#q8) [`Q9`](#q9) [`Q12`](#q12) [`Q13`](#q13) [`Q19`](#q19)
- Start with: Securely deploying AI agents `[S7]` and Choose a sandbox environment `[S6]`.

### `I3` — Compliance, privacy & legal
*"Where does the data go, for how long, and under which agreement?"*
- Themes: [`T2`](#t2--data-handling-retention-and-model-training) → [`T3`](#t3--zero-data-retention-and-regulated-workloads) → [`T1`](#t1--governance-certifications-and-compliance) → [`T10`](#t10--monitoring-audit-and-compliance-operations)
- Questions: [`Q1`](#q1) [`Q2`](#q2) [`Q3`](#q3) [`Q4`](#q4) [`Q6`](#q6) [`Q16`](#q16) [`Q17`](#q17) [`Q20`](#q20)
- Start with: API and data retention `[S5]` and Claude Code data usage `[S2]`.

### `I4` — IT / platform administrator
*"How do I roll this out so that every developer lands in the configuration we approved?"*
- Themes: [`T8`](#t8--identity-access-and-enterprise-administration) → [`T6`](#t6--agent-permissions-and-the-approval-model) → [`T9`](#t9--network-and-deployment-security) → [`T10`](#t10--monitoring-audit-and-compliance-operations)
- Questions: [`Q10`](#q10) [`Q11`](#q11) [`Q14`](#q14) [`Q15`](#q15) [`Q19`](#q19)
- Start with: Claude Code ZDR/admin capabilities `[S4]` and the managed-settings docs `[S8]`.

### `I5` — Developer using Claude Code day to day
*"What is it allowed to do on my machine, and how do I not get burned?"*
- Themes: [`T6`](#t6--agent-permissions-and-the-approval-model) → [`T7`](#t7--isolation-and-sandboxing) → [`T5`](#t5--prompt-injection-and-untrusted-content) → [`T2`](#t2--data-handling-retention-and-model-training)
- Questions: [`Q7`](#q7) [`Q9`](#q9) [`Q11`](#q11) [`Q13`](#q13) [`Q18`](#q18) [`Q22`](#q22)
- Start with: Claude Code security `[S1]`.

### `I6` — Builder on the Claude API / Agent SDK
*"My product is the one that gets attacked. What do I owe my users?"*
- Themes: [`T5`](#t5--prompt-injection-and-untrusted-content) → [`T4`](#t4--model-level-safety-and-safeguards) → [`T7`](#t7--isolation-and-sandboxing) → [`T3`](#t3--zero-data-retention-and-regulated-workloads)
- Questions: [`Q8`](#q8) [`Q13`](#q13) [`Q17`](#q17) [`Q20`](#q20) [`Q21`](#q21)
- Start with: Mitigate jailbreaks and prompt injections `[S12]` and Securely deploying AI agents `[S7]`.

### `I7` — Procurement / third-party risk (TPRM)
*"Fill in the vendor questionnaire with evidence, not adjectives."*
- Themes: [`T1`](#t1--governance-certifications-and-compliance) → [`T2`](#t2--data-handling-retention-and-model-training) → [`T3`](#t3--zero-data-retention-and-regulated-workloads) → [`T11`](#t11--supply-chain-mcp-and-vulnerability-reporting)
- Questions: [`Q5`](#q5) [`Q6`](#q6) [`Q12`](#q12) [`Q17`](#q17)
- Start with: Trust Center `[S1]` for certificates, sub-processors and the report-request flow; Legal and compliance `[S3]` for which terms apply.

---

## Themes

### `T1` — Governance, certifications and compliance

**The one-line version:** Anthropic publishes its security program, certifications and compliance artifacts through the Trust Center; which contract governs you depends on which plan you are on.

- The Trust Center (<https://trust.anthropic.com>) is the canonical place for compliance artifacts — Claude Code's own security documentation points there for the SOC 2 Type 2 report, the ISO 27001 certificate and similar evidence. `[S1]`
- Anthropic also maintains a Transparency Hub, referenced from the product legal/compliance docs, alongside the Trust Center. `[S3]` `[S10]`
- **Which terms apply:** Commercial Terms of Service for Team, Enterprise and Claude API users; Consumer Terms for Free, Pro and Max users. If you already have a commercial agreement — whether direct (1P) or via Amazon Bedrock / Google Cloud's Agent Platform (3P) — it extends to Claude Code usage unless separately agreed. `[S3]`
- **Healthcare (BAA):** a BAA executed with Anthropic extends to a customer's API traffic through Claude Code *when ZDR is enabled for the relevant organization*. `[S3]` For the API itself, HIPAA readiness is a distinct arrangement — see [`T3`](#t3--zero-data-retention-and-regulated-workloads). `[S5]`
- **Acceptable use** is governed by the Anthropic Usage Policy. `[S3]` `[S9]`
- **Authentication terms matter for architecture:** OAuth sign-in is for subscription plan purchasers; developers building products should use API keys via the Claude Console or a supported cloud provider. Third-party developers may not offer Claude.ai login in their own applications, nor collect/store/intermediate Claude.ai credentials or session tokens. `[S3]`

> **Traceability note:** `trust.anthropic.com`, `anthropic.com`, `privacy.claude.com` and `support.claude.com` were not directly retrievable from the environment where this page was drafted (egress-restricted). Statements about them here are taken from Anthropic product documentation that cites them `[S1]` `[S3]` `[S5]`. Treat the linked pages themselves as authoritative and confirm certificate scope and dates there before quoting them in an assessment.

**Sources:** `[S1]` `[S3]` `[S5]` `[S9]` `[S10]`

---

### `T2` — Data handling, retention and model training

**The one-line version:** commercial traffic is not used to train models by default; retention length depends on plan and on your privacy setting.

**Training policy** `[S2]`
- *Consumer (Free, Pro, Max):* data is used to improve future models **only when the user's setting is on** — including Claude Code usage from those accounts. The setting can be changed at any time.
- *Commercial (Team, Enterprise, API, third-party platforms, Claude Gov):* Anthropic does **not** train generative models on code or prompts sent to Claude Code under commercial terms, unless the customer opts in — e.g. via the Development Partner Program, which an organization admin must expressly enable and which is first-party API only.
- API-side commitment: retained data is never used for model training without express permission. `[S5]`

**Retention** `[S2]`

| Population | Retention |
|---|---|
| Consumer, data-use setting **on** | 5 years |
| Consumer, data-use setting **off** | 30 days |
| Commercial (Team, Enterprise, API), standard | 30 days |
| Commercial with ZDR | see [`T3`](#t3--zero-data-retention-and-regulated-workloads) |
| Transcripts submitted via `/feedback`, `/bug`, `/share` | 5 years |
| Transcripts shared through the session-quality survey follow-up | up to 6 months |
| Local Claude Code transcripts on disk (`~/.claude/projects/`, plaintext) | 30 days by default, tunable with `cleanupPeriodDays` |

Organization-level retention on the API side has its own shapes: the Activity Feed retains 6 years; local session transcripts from Claude apps default to 6 years (or your org's custom conversation retention period); remote Cowork session transcripts 6 years unless deleted sooner. `[S5]`

**Transport and at-rest encryption** `[S2]`
- Prompts and outputs travel over TLS 1.2+. Claude Code is compatible with most VPNs and LLM proxies.
- At rest, encryption depends on the model provider: Anthropic API — infrastructure disk encryption (AES-256); Amazon Bedrock — AES-256 with AWS-managed keys, CMK via KMS; Google Cloud's Agent Platform — Google-managed keys, CMEK available; Microsoft Foundry — depends on hosting option (on "Hosted on Azure", prompts and completions stay in Azure and only usage metadata plus safety-flagged content egresses to Anthropic).

**Telemetry** `[S2]`
- *Metrics* (latency, reliability, usage patterns) — never include code, prompts or file paths; opt out with `DISABLE_TELEMETRY=1`.
- *Error reports* — stack traces from Claude Code internals, with known secret/path/email patterns redacted before leaving the machine; opt out with `DISABLE_ERROR_REPORTING=1`.
- `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` disables non-essential traffic in one switch. Two things are **not** covered by it: the WebFetch domain safety check (own opt-out: `skipWebFetchPreflight`) and official marketplace auto-install (`CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL`).
- On Bedrock, Google Cloud's Agent Platform, Microsoft Foundry and Claude Platform on AWS, error reporting/telemetry/bug reporting default to **off**.

**Sources:** `[S2]` `[S5]`

---

### `T3` — Zero data retention and regulated workloads

**The one-line version:** ZDR means prompts and responses are not stored at rest after the response is returned — but it is scoped, it is not self-serve, and several features fall outside it.

**ZDR on the API** `[S5]`
- Covers the Messages and Token Counting APIs for eligible features; Claude Code used with Commercial-organization API keys or through Claude Enterprise with ZDR enabled; Claude Platform on AWS on request.
- Does **not** cover: Claude Console (including playground), Claude Managed Agents, consumer plans, the Claude Team/Enterprise product interfaces (Claude Code on Enterprise being the exception), Claude for Excel, Covered Models, third-party integrations. CORS is unsupported for ZDR organizations — route browser calls through a backend proxy.
- Features marked "No" for ZDR are not blocked; they are *stateful by design* (Batch API stores jobs, Files API stores files, code execution uses persistent containers). Using them is a deliberate step outside your ZDR arrangement for that data.

**ZDR for Claude Code on Claude for Enterprise** `[S4]`
- Available to qualified accounts only; not in the standard Enterprise plan, not enableable from admin settings, requires Anthropic to enable it per organization. **A new organization under the same account does not inherit ZDR.**
- ZDR-enabled orgs still get cost controls per user, the analytics dashboard, server-managed settings and audit logs.
- **Features disabled under ZDR** (backend-enforced): Claude Code on the Web, Desktop cloud sessions, Claude Tag, Artifacts, feedback submission (`/feedback`, `/bug`, `/share`), Remote Control.
- **Not covered by ZDR even when enabled:** claude.ai chat, Cowork, Claude Code analytics metadata, user/seat management data, third-party integrations.
- Routing matters: ZDR applies to requests authenticating into the ZDR organization. A developer signing in with a personal account is not covered — pin logins with the `forceLoginMethod` / `forceLoginOrgUUID` managed settings. `[S4]` `[S8]`

**HIPAA readiness** `[S5]`
- A distinct arrangement from ZDR, and the right one if you handle PHI — it applies encryption, access controls and audit logging across the PHI lifecycle instead of requiring immediate deletion. You do not need both.
- Enforced at the **organization** level; non-eligible features are blocked with a `400 invalid_request_error`. Use a separate organization for non-HIPAA workloads.
- Eligible organizations can execute the standard BAA and enable HIPAA readiness in Claude Console → Settings → Privacy; negotiated BAAs go through sales.

**Covered Models** `[S5]` `[S4]`
- Claude Fable 5.1, Mythos 5.1, Fable 5 and Mythos 5 are designated Covered Models and **require 30-day data retention**; they are unavailable under ZDR unless expressly authorized. A ZDR org can enable 30-day retention for a single workspace to use them while other workspaces stay at zero retention.

**Retention regardless of arrangement** `[S5]` `[S4]`
- Anthropic may retain data where required by law, or where content is flagged by automated trust-and-safety systems — in which case inputs and outputs may be retained for **up to 2 years**.

**Sources:** `[S4]` `[S5]`

---

### `T4` — Model-level safety and safeguards

**The one-line version:** the model is one control among several — treat its resistance to manipulation as a strong default, not as a boundary.

- Claude models are *designed to resist* prompt injection; Anthropic points deployers to the model overview and to the **system card of the specific model being deployed** for evaluation details. Defense in depth is still explicitly recommended. `[S7]`
- Claude is described as "inherently resilient" to jailbreaks and injection, with the documented mitigations framed as *strengthening* guardrails rather than substituting for model behavior. `[S12]`
- For the computer use tool, Anthropic runs **additional classifiers** that detect potential prompt injections in screenshots and steer Claude to ask for user confirmation before acting (with documented opt-out). `[S12]`
- In Claude Code's **auto mode**, a separate classifier model reviews actions in place of the human and blocks ones it judges unsafe; explicit ask/deny rules still apply and organizations can turn auto mode off. `[S1]`
- Frontier-risk governance (the Responsible Scaling Policy and AI Safety Level standards), model system cards, and Anthropic's transparency reporting live on Anthropic's own sites. `[S9]` `[S10]` **Read the current version at the source before citing specifics** — level designations and policy versions change between model releases and were not verifiable from this drafting environment.

**Sources:** `[S1]` `[S7]` `[S9]` `[S10]` `[S11]` `[S12]`

---

### `T5` — Prompt injection and untrusted content

**The one-line version:** two different threat models share a name; the mitigations differ.

| | Direct injection / jailbreak | Indirect injection |
|---|---|---|
| Adversary | The user of your application | A third party who can influence content Claude reads |
| Vector | Crafted prompts | Web pages, emails, documents, OCR text, tool results, a repo's README |
| Goal | Bypass your guardrails | Redirect the agent using the user's own privileges |

`[S12]`

**Product-side safeguards in Claude Code** `[S1]`
- Permission system — sensitive operations need explicit approval in Manual mode.
- Context-aware analysis of the full request; input sanitization against command injection.
- Network-fetching commands (`curl`, `wget`) are **not** auto-approved by default.
- Isolated context window for web fetch, so fetched content cannot inject directly into the main context.
- Web search results are **summarized** rather than passed in raw. `[S7]`
- Trust verification for first-time codebases and new MCP servers (note: disabled when running non-interactively with `-p`).
- Command-injection detection: suspicious bash commands require manual approval even if previously allowlisted; unmatched commands **fail closed**.
- Natural-language explanations for complex bash commands, so a human can actually review them.
- Secure credential storage: macOS Keychain where available, file permissions on Windows and Linux.
- ⚠️ Windows: Anthropic recommends against enabling WebDAV or allowing access to `\\*` paths — WebDAV is deprecated by Microsoft and may let network requests bypass the permission system.

**Application-side mitigations if you are building on Claude** `[S12]`
1. Put untrusted content **only** in `tool_result` blocks — never in the system prompt or plain user text. Claude is trained to treat instructions inside tool results with skepticism.
2. Label the content's nature and provenance in the tool description or result structure.
3. State an untrusted-content policy in the system prompt explicitly.
4. JSON-encode third-party strings so quoting cannot be broken out of.
5. Do **not** put your own instructions in tool results — send them in the following user turn.
6. Least privilege: don't expose secrets the agent doesn't need; sandbox tools; scope permissions narrowly.
7. Screen tool output with a cheap classifier (e.g. Claude Haiku 4.5 + structured outputs) before returning it as a `tool_result`.
8. Pre-screen user input (harmlessness screens, input validation), and throttle or ban repeat offenders.
9. Red-team your own agent with deliberately poisoned documents before deploy; monitor outputs continuously.

**Working with untrusted content as a user** `[S1]`
Review commands before approval · avoid piping untrusted content straight into Claude · verify changes to critical files · run scripts and external-service calls inside VMs · report suspicious behaviour with `/feedback`.

> Anthropic states plainly that while these protections significantly reduce risk, **no system is completely immune**. `[S1]`

**Sources:** `[S1]` `[S7]` `[S12]`

---

### `T6` — Agent permissions and the approval model

**The one-line version:** permissions decide *whether an action runs*; isolation decides *what it can reach once it runs*. You need both.

- **Manual mode** starts read-only. Edits, test runs and commands are asked for, one-time or persistently. A built-in set of read-only commands (`ls`, `cat`, `git status`, …) runs without asking. `[S1]`
- **Working-directory boundary:** in Manual mode Claude Code writes only inside the startup folder and its subfolders, and asks before reading outside that boundary with Read/Grep/Glob. Widen with additional directories; narrow read access for read-only Bash with sandbox `denyRead` rules. `[S1]`
- **Accept Edits mode** auto-approves file edits and a fixed set of filesystem Bash commands (`mkdir`, `touch`, `rm`, `mv`, `cp`, `sed`) within the working directory; everything else still prompts. `[S1]`
- **Auto mode** replaces the human prompt with a classifier — a per-action control, *not* an isolation boundary. `[S1]` `[S6]`
- **`--dangerously-skip-permissions`** removes prompts entirely. Anthropic's guidance: always run such sessions inside a container, VM or the sandbox runtime, and as a non-root user (Claude Code refuses to start with this flag as root on Linux/macOS). `[S6]`
- **How bash rules are evaluated:** commands are parsed into an AST and matched against your rules. Unparseable or unmatched commands require approval; constructs such as `eval` always require approval regardless of allow rules. This is a **permission gate, not a sandbox** — apart from built-in checks (the critical-path check on `rm`/`rmdir`, the protected-paths list) it does not infer danger from a command's target or effects. `[S7]`
- **Organizational enforcement:** managed settings, shared permission configurations in version control, `/permissions` audits, and `ConfigChange` hooks to audit or block settings changes mid-session. `[S1]` `[S8]`
- **Responsibility is explicit:** "Claude Code only has the permissions you grant it. You're responsible for reviewing proposed code and commands for safety before approval." `[S1]`

**Sources:** `[S1]` `[S6]` `[S7]` `[S8]`

---

### `T7` — Isolation and sandboxing

**The one-line version:** pick the boundary that matches your threat model, and know what each one leaves outside it.

| Approach | What is inside the boundary | Docker? | Effort | Isolation strength |
|---|---|---|---|---|
| Sandboxed Bash tool (`/sandbox`) | Bash commands and children only | No | Minimal (macOS) / low (Linux, WSL2) | Per-command |
| Sandbox runtime (`@anthropic-ai/sandbox-runtime`) | Whole Claude Code process: file tools, MCP servers, hooks | No | Low | Good (secure defaults) |
| Dev container | Full dev environment | Yes | Medium | Setup dependent |
| Custom container | Full dev environment | Yes | Medium–high | Setup dependent |
| gVisor | Syscalls intercepted in userspace | Yes | Medium | Excellent (correct setup) |
| VM / Firecracker | Full OS, own kernel | No | High | Excellent (correct setup) |
| Claude Code on the web | Full OS, Anthropic-managed | No | None (subscription) | Anthropic-managed VM |

`[S6]` `[S7]`

**Key gaps to know**
- The built-in Bash sandbox does **not** cover MCP servers or command hooks — those run unconstrained on the host. Only whole-process approaches cover them. `[S6]`
- Isolation does not change **what is sent to the model**: prompts and files Claude reads still go to the API with or without a sandbox. `[S6]`
- Sandbox-runtime and similar proxies allowlist by client-supplied hostname and **do not terminate TLS**, so domain fronting can reach hosts outside the allowlist. Use a TLS-terminating proxy if your threat model needs it. `[S7]`
- Host-level sandboxes share the host kernel; a kernel vulnerability could enable escape. `[S7]`
- The sandbox runtime blocks high-risk writes by default (`.git/hooks`, `.git/config` unless allowed, `.mcp.json`, `.claude/commands`, `.claude/agents`, shell startup files), with weaker coverage on Linux/WSL2 for paths created *during* the session. A session that can write Claude Code's config paths can persist hooks, permission rules or MCP servers that run **unsandboxed next launch** — deny those paths explicitly and review writable paths after unattended runs. `[S6]`
- gVisor cost: ~0% for CPU-bound work, ~2× for simple syscalls, up to 10–200× for heavy file I/O. `[S7]`

**Hardening a container** `[S7]`
`--cap-drop ALL`, `--security-opt no-new-privileges`, a seccomp profile, `--read-only` with `tmpfs` scratch, `--network none` plus a Unix-socket proxy, `--memory` / `--pids-limit`, `--user 1000:1000`, code mounted `:ro`. **Do not mount `~/.ssh`, `~/.aws`, `~/.config`.** Even read-only mounts leak credentials — exclude `.env`, `~/.git-credentials`, `~/.aws/credentials`, gcloud ADC, `~/.azure/`, `~/.docker/config.json`, `~/.kube/config`, `.npmrc`, `.pypirc`, service-account JSON, `*.pem`, `*.key`.

**Sources:** `[S6]` `[S7]`

---

### `T8` — Identity, access and enterprise administration

**The one-line version:** the controls exist, but most of them only bind if you push them from the org side.

- **Credential handling:** Claude Code authenticates with OAuth tokens or API keys; tokens are stored in the macOS Keychain where available and protected by file permissions elsewhere. `[S1]` `[S3]`
- **Pin logins to your organization** with `forceLoginMethod` and `forceLoginOrgUUID` managed settings — otherwise a developer signing in with a personal account escapes your organization's policies, including ZDR. `[S4]`
- **Managed settings** deliver organizational standards; delivery is via MDM-managed file or server-managed settings on Claude.ai. `[S8]` Only the built-in Bash sandbox is enforceable by Claude Code itself — containers and VMs are conventions unless enforced by device management or software allowlisting. `[S6]`
- **Enterprise identity features** (SSO with domain capture, SCIM/JIT provisioning, role- and group-based access control, network-level access controls) are Claude Enterprise plan capabilities. `[S13]` `[S14]` — confirm the current feature list against the plan documentation before relying on it in a design.
- **Credential isolation pattern:** the recommended architecture is a proxy *outside* the agent's boundary that injects credentials into outgoing requests, so the agent never sees them, the proxy enforces an endpoint allowlist, and all requests are logged centrally. `[S7]`
- **Gateways:** Claude Code supports self-hosted LLM gateways for centralized credentials, usage tracking and cost control. `[S8]`

**Sources:** `[S1]` `[S3]` `[S4]` `[S6]` `[S7]` `[S8]` `[S13]` `[S14]`

---

### `T9` — Network and deployment security

**The one-line version:** control egress at a boundary the agent cannot rewrite.

**Cloud execution (Claude Code on the web), Anthropic-hosted** `[S1]` `[S2]`
- Each session runs in an isolated, Anthropic-managed VM.
- Network access is limited by default and can be disabled or restricted to specific domains.
- GitHub authentication goes through a secure proxy issuing a scoped credential inside the sandbox; **your real GitHub token never enters the sandbox**.
- Git push is restricted to the current working branch.
- All operations are logged for compliance and audit; all outbound traffic passes a security proxy.
- Session VMs are reclaimed after inactivity. Sessions can be deleted, which permanently removes the session's event data.
- Sessions routed to a **self-hosted environment** run on your infrastructure — isolation, egress and git credentials become your responsibility. `[S1]`

**Remote Control** `[S1]`
- Execution and file access stay local; traffic goes over TLS via the Anthropic API. While connected, the session transcript is stored on Anthropic servers to sync across devices. Uses multiple short-lived, narrowly scoped credentials that expire independently, to limit blast radius.

**Proxying** `[S7]`
- `ANTHROPIC_BASE_URL` routes sampling requests to your proxy in plaintext (inspectable, modifiable).
- `HTTP_PROXY`/`HTTPS_PROXY` route all HTTP traffic, but HTTPS becomes an opaque CONNECT tunnel — credential injection requires a TLS-terminating proxy and its CA in the agent's trust store.
- Not every program honours proxy env vars (Node's `fetch()` ignores them unless `NODE_USE_ENV_PROXY=1` on Node 24+); consider proxychains or iptables redirection to a transparent proxy.
- Cloud pattern: private subnet, no internet gateway, firewall egress only to your proxy (e.g. Envoy with `credential_injector`), minimal IAM on the agent's service account, log everything at the proxy.

**WebFetch domain safety check** `[S2]`
Before fetching a URL, the WebFetch tool sends **only the hostname** (not the path or page contents) to `api.anthropic.com` to check a safety blocklist. Passing hostnames are cached 5 minutes. This runs on every provider and is not disabled by `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`. If your network blocks `api.anthropic.com`, WebFetch fails until you allowlist it or set `skipWebFetchPreflight: true` — in which case pair it with `WebFetch` permission rules.

**Sources:** `[S1]` `[S2]` `[S7]`

---

### `T10` — Monitoring, audit and compliance operations

**The one-line version:** three different pipes, three different audiences — don't try to make one do all three jobs.

| Mechanism | Returns | For whom | Notes |
|---|---|---|---|
| **OpenTelemetry** (Claude Code monitoring, Cowork OTel logging) | Per-event telemetry streamed live to *your* collector — tokens, cost, host metadata, optionally prompts/responses | Platform, SRE | You run the collector `[S13]` `[S1]` |
| **Compliance API** (`/v1/compliance/*`) | Per-event records after the fact: Activity Feed, users/roles/groups, effective org settings, chats/files/projects, session transcripts from Cowork, Claude Code, Claude Science, Claude for M365 | Security, legal, compliance | Anthropic recommends it over OTel for retrieving Cowork/Claude Code session content `[S13]` |
| **Analytics APIs** (Enterprise + Claude Code) | Aggregated usage and cost | IT, FinOps | Different keys, provisioned separately `[S13]` |

- Compliance API keys: a **Compliance Access Key** (created in claude.ai) reaches every endpoint; an **Admin API key** (Claude Console) reaches the Activity Feed only. Shared rate limit 600 req/min per parent organization. `[S13]`
- **Audit log export** in claude.ai → Organization settings → Data and privacy is a narrower CSV download with a capped lookback and no content access; standardize on the Compliance API for ongoing programmatic use. `[S13]`
- **Inference hooks** (beta) act *inline*: your organization's AI security server receives each governed prompt before inference and can deny it in real time — the only listed mechanism that blocks rather than records. `[S13]`
- Claude Code usage can be monitored via OpenTelemetry metrics, and settings changes audited or blocked with `ConfigChange` hooks. `[S1]`
- ZDR organizations keep audit logs and the analytics dashboard, but contribution metrics are unavailable. `[S4]`

**Sources:** `[S1]` `[S4]` `[S13]`

---

### `T11` — Supply chain, MCP and vulnerability reporting

**The one-line version:** MCP servers and connectors are your trust decision, not Anthropic's.

- Claude Code lets users configure MCP servers; the allowed list lives in settings checked into source control. Anthropic's guidance: write your own or use providers you trust. `[S1]`
- Anthropic reviews connectors against listing criteria before adding them to the Anthropic Directory, **but does not security-audit or manage any MCP server**. `[S1]`
- Organizations can restrict or provide MCP servers centrally with managed MCP configuration, allowlists and denylists. `[S8]`
- MCP servers and hooks run as separate processes **outside** the built-in Bash sandbox — see [`T7`](#t7--isolation-and-sandboxing). `[S6]`
- Data processed by third-party tools, MCP servers or external integrations is **not** covered by ZDR or HIPAA readiness; review those services independently. `[S4]` `[S5]`
- **Vulnerability reporting:** Anthropic runs its security program through HackerOne. Do not disclose publicly; report with detailed reproduction steps and allow time to fix. `[S1]` `[S3]`
- **Secure-coding support in the product:** the security-guidance plugin (review and fix vulnerabilities as Claude writes code), the `/security-review` command (on-demand security pass over the current branch), the Claude Security plugin (codebase vulnerability scanning) and automated Code Review for PRs. `[S1]` `[S8]`

**Sources:** `[S1]` `[S3]` `[S4]` `[S5]` `[S6]` `[S8]`

---

## FAQ

<a id="q1"></a>
### `Q1` Is our code or are our prompts used to train Claude models?
**No, under commercial terms** (Team, Enterprise, API, third-party platforms, Claude Gov) — unless your organization expressly opts in, e.g. via the Development Partner Program, which an org admin must enable and which is first-party API only. On consumer plans (Free/Pro/Max) it depends on the user's own privacy setting. On the API side, the commitment is explicit: retained data is never used for model training without your permission.
→ Themes [`T2`](#t2--data-handling-retention-and-model-training) · Sources `[S2]` `[S5]`

<a id="q2"></a>
### `Q2` How long is our data kept?
Standard commercial retention is **30 days**. Consumer is 5 years with data-sharing on, 30 days with it off. Feedback transcripts are 5 years; shared survey transcripts up to 6 months; local Claude Code transcripts sit on the developer's disk in plaintext for 30 days by default. Organization-side stores have their own periods (Activity Feed 6 years; local and remote session transcripts 6 years by default).
→ Themes [`T2`](#t2--data-handling-retention-and-model-training) · Sources `[S2]` `[S5]`

<a id="q3"></a>
### `Q3` What exactly is ZDR, and can we just turn it on?
ZDR means prompts and responses are not stored at rest after the API response is returned. You **cannot** self-enable it: it is granted per organization by your Anthropic account team after eligibility review, and it is not part of the standard Enterprise plan. Critically, a **new organization under the same account does not inherit it**.
→ Themes [`T3`](#t3--zero-data-retention-and-regulated-workloads) · Sources `[S4]` `[S5]`

<a id="q4"></a>
### `Q4` What does ZDR *not* cover — i.e. where will we still be surprised?
claude.ai chat, Cowork, Claude Console/playground, Claude Managed Agents, Claude for Excel, consumer plans, user/seat administrative data, Claude Code analytics metadata, and anything processed by third-party tools or MCP servers. Stateful API features (Batch, Files, code execution) are not blocked but fall outside the arrangement. Under Claude Code ZDR, several features are disabled outright: Claude Code on the Web, Desktop cloud sessions, Claude Tag, Artifacts, `/feedback` `/bug` `/share`, and Remote Control.
→ Themes [`T3`](#t3--zero-data-retention-and-regulated-workloads) · Sources `[S4]` `[S5]`

<a id="q5"></a>
### `Q5` Which certifications does Anthropic hold, and how do we get the reports?
Compliance artifacts — including the SOC 2 Type 2 report and ISO 27001 certificate — are published through the **[Anthropic Trust Center](https://trust.anthropic.com)**, which the product documentation names as the place to obtain them; restricted documents are requested there. Go to the Trust Center for the authoritative, current list and scope rather than quoting a secondhand summary.
→ Themes [`T1`](#t1--governance-certifications-and-compliance) · Sources `[S1]` `[S3]`

<a id="q6"></a>
### `Q6` Can we process PHI / run a HIPAA workload?
Yes, via **HIPAA readiness** on the Claude API with a signed BAA — a different arrangement from ZDR, and the correct one for PHI (you do not need both). It is enforced at organization level and blocks non-eligible features with a `400`, so use a separate organization for non-HIPAA work. For Claude Code, a BAA extends to your API traffic through Claude Code **when ZDR is enabled** for that organization. HIPAA readiness is not available on Claude Platform on AWS.
→ Themes [`T3`](#t3--zero-data-retention-and-regulated-workloads) [`T1`](#t1--governance-certifications-and-compliance) · Sources `[S3]` `[S5]`

<a id="q7"></a>
### `Q7` What actually stops Claude Code from running a destructive command?
In Manual mode: read-only start, per-command approval, a working-directory write boundary, fail-closed matching for unmatched commands, command-injection detection that re-prompts even for previously allowlisted commands, built-in critical-path checks on `rm`/`rmdir` and a protected-paths list, and `eval`-class constructs that always require approval. Note that permission matching is an AST-based **gate, not a sandbox** — it does not reason about what a command will do to a given path.
→ Themes [`T6`](#t6--agent-permissions-and-the-approval-model) [`T5`](#t5--prompt-injection-and-untrusted-content) · Sources `[S1]` `[S7]`

<a id="q8"></a>
### `Q8` Does sandboxing solve prompt injection?
No. Sandboxing reduces **impact**, not likelihood. Anthropic states directly that any approach allowing network egress can still leak data the agent can read, and any writable project mount can still be modified; and that no system is completely immune. Proxy allowlists that don't terminate TLS can be bypassed by domain fronting. Layer controls: permissions + isolation + egress control + monitoring.
→ Themes [`T5`](#t5--prompt-injection-and-untrusted-content) [`T7`](#t7--isolation-and-sandboxing) · Sources `[S1]` `[S6]` `[S7]`

<a id="q9"></a>
### `Q9` How do we let Claude run unattended without it being reckless?
Never run `--dangerously-skip-permissions` outside a container, VM or the sandbox runtime — and run it as a non-root user (Claude Code refuses to start as root with that flag on Linux/macOS). Auto mode's classifier is a per-action control, not a boundary, so an isolation boundary is still defence in depth there. The built-in Bash sandbox alone is insufficient for unattended runs because MCP servers and hooks fall outside it. After unattended runs, review what stayed writable.
→ Themes [`T6`](#t6--agent-permissions-and-the-approval-model) [`T7`](#t7--isolation-and-sandboxing) · Sources `[S6]`

<a id="q10"></a>
### `Q10` How do we stop developers using personal accounts and bypassing our policies?
Deploy the `forceLoginMethod` and `forceLoginOrgUUID` managed settings to require that claude.ai logins belong to your organization. Without this, a personal-account session is not covered by your organization's ZDR arrangement or settings.
→ Themes [`T8`](#t8--identity-access-and-enterprise-administration) [`T3`](#t3--zero-data-retention-and-regulated-workloads) · Sources `[S4]` `[S8]`

<a id="q11"></a>
### `Q11` What leaves a developer's machine, and how do we turn it off?
Metrics (no code, prompts or file paths — `DISABLE_TELEMETRY=1`), error reports (redacted before leaving — `DISABLE_ERROR_REPORTING=1`), `/feedback` submissions including conversation history (`DISABLE_FEEDBACK_COMMAND=1`), and session-quality survey ratings (`CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY=1`). `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` covers these at once. Two exceptions need their own opt-outs: the WebFetch hostname safety check (`skipWebFetchPreflight`) and marketplace auto-install. On Bedrock/Google Cloud/Foundry/Claude Platform on AWS most of this is off by default.
→ Themes [`T2`](#t2--data-handling-retention-and-model-training) [`T9`](#t9--network-and-deployment-security) · Sources `[S2]`

<a id="q12"></a>
### `Q12` Are MCP servers and connectors vetted by Anthropic?
Connectors are reviewed against listing criteria before being added to the Anthropic Directory, but Anthropic **does not security-audit or manage any MCP server**. Treat MCP servers as third-party code you are responsible for: write your own or use trusted providers, restrict them centrally with managed MCP allow/deny lists, and remember they run outside the built-in Bash sandbox and outside ZDR/HIPAA coverage.
→ Themes [`T11`](#t11--supply-chain-mcp-and-vulnerability-reporting) · Sources `[S1]` `[S4]` `[S5]` `[S6]` `[S8]`

<a id="q13"></a>
### `Q13` How is web content handled, given it's the classic injection vector?
Web fetch uses an **isolated context window**; web search results are **summarized** rather than injected raw; network-fetching commands like `curl`/`wget` are not auto-approved; and WebFetch performs a hostname-only safety-blocklist check against `api.anthropic.com` before fetching. When building your own app, put fetched content in `tool_result` blocks, JSON-encode it, label its provenance, and screen it with a classifier before acting.
→ Themes [`T5`](#t5--prompt-injection-and-untrusted-content) [`T9`](#t9--network-and-deployment-security) · Sources `[S1]` `[S2]` `[S7]` `[S12]`

<a id="q14"></a>
### `Q14` What are the security properties of Claude Code on the web?
Isolated Anthropic-managed VM per session; network limited by default and configurable to disabled or a domain allowlist; GitHub auth via a secure proxy so your real token never enters the sandbox; git push restricted to the current branch; all operations logged for audit; VMs reclaimed after inactivity; sessions deletable, which permanently removes event data. If your org routes sessions to a self-hosted environment, isolation, egress and git credentials become yours to secure.
→ Themes [`T9`](#t9--network-and-deployment-security) · Sources `[S1]` `[S2]`

<a id="q15"></a>
### `Q15` How do we get Claude activity into our SIEM?
Use the **Compliance API** (`/v1/compliance/*`) for per-event records — Activity Feed, directory, effective settings, chat/file/project content and session transcripts — with a Compliance Access Key (full) or Admin API key (Activity Feed only). Use **OpenTelemetry** for live streaming telemetry to your own collector. The claude.ai audit-log CSV export is narrower (capped lookback, no content) and is not the right basis for an ongoing integration.
→ Themes [`T10`](#t10--monitoring-audit-and-compliance-operations) · Sources `[S13]` `[S1]`

<a id="q16"></a>
### `Q16` Can Anthropic retain our data even under ZDR?
Yes, in two cases: where required by law, and where content is flagged by automated trust-and-safety systems — in which case inputs and outputs may be retained for **up to 2 years**. Put this in your risk register; it is a documented, deliberate exception, not an edge case.
→ Themes [`T3`](#t3--zero-data-retention-and-regulated-workloads) [`T2`](#t2--data-handling-retention-and-model-training) · Sources `[S4]` `[S5]`

<a id="q17"></a>
### `Q17` Does it matter whether we use the Claude API directly or Bedrock / Google Cloud / Foundry?
Yes, materially. On the **Claude API, Claude Platform on AWS and Claude in Microsoft Foundry, Anthropic is the data processor** and the ZDR/HIPAA arrangements described here apply. On **Amazon Bedrock and Google Cloud's Agent Platform, the cloud provider is the data processor** — their retention and compliance policies govern, not these. Encryption-at-rest and default telemetry behaviour also differ per provider.
→ Themes [`T2`](#t2--data-handling-retention-and-model-training) [`T3`](#t3--zero-data-retention-and-regulated-workloads) · Sources `[S2]` `[S5]`

<a id="q18"></a>
### `Q18` We found a vulnerability in Claude Code. What now?
Do not disclose publicly. Report it through Anthropic's HackerOne program with detailed reproduction steps, and allow time for a fix before disclosure.
→ Themes [`T11`](#t11--supply-chain-mcp-and-vulnerability-reporting) · Sources `[S1]` `[S3]`

<a id="q19"></a>
### `Q19` What's the difference between a permission mode and a sandbox?
Permission modes decide **whether a tool call runs and whether you're asked first**. Isolation decides **what that call can reach once it runs**. They are complementary: when a mode stops asking you, the isolation boundary is what protects the system. Auto mode's classifier is a per-action control, not a boundary.
→ Themes [`T6`](#t6--agent-permissions-and-the-approval-model) [`T7`](#t7--isolation-and-sandboxing) · Sources `[S6]`

<a id="q20"></a>
### `Q20` Why can't we use certain models under ZDR?
Claude Fable 5.1, Mythos 5.1, Fable 5 and Mythos 5 are designated **Covered Models** requiring 30-day data retention, so they are unavailable under ZDR unless Anthropic expressly authorizes it. On the API a non-conforming request returns `400 invalid_request_error`. A ZDR organization can enable 30-day retention for one workspace to use them while the rest stay at zero retention.
→ Themes [`T3`](#t3--zero-data-retention-and-regulated-workloads) · Sources `[S4]` `[S5]`

<a id="q21"></a>
### `Q21` Can we block a prompt *before* it reaches the model?
Yes — **inference hooks** (beta) let your organization's AI security server receive each governed prompt before inference and deny it in real time. This is the inline control; the Compliance API and OpenTelemetry are after-the-fact and observational.
→ Themes [`T10`](#t10--monitoring-audit-and-compliance-operations) [`T5`](#t5--prompt-injection-and-untrusted-content) · Sources `[S13]`

<a id="q22"></a>
### `Q22` Can Claude check its own output for vulnerabilities?
Yes, with several product features: the **security-guidance plugin** reviews and fixes vulnerabilities as Claude writes code during a session; **`/security-review`** runs an on-demand security pass over the changes on the current branch; the **Claude Security plugin** scans a codebase for vulnerabilities; and **Code Review** does automated PR review for vulnerabilities and regressions. Treat these as additional review depth, not as a replacement for human review or your existing SAST/DAST.
→ Themes [`T11`](#t11--supply-chain-mcp-and-vulnerability-reporting) [`T5`](#t5--prompt-injection-and-untrusted-content) · Sources `[S1]` `[S8]`

---

## Source register

Status legend: **✅ fetched** = content was retrieved and read while drafting this page (2026-09-15). **🔗 reference** = canonical official URL cited by the fetched sources, but not directly retrievable from the drafting environment (egress-restricted); verify at the source before quoting.

| ID | Source | URL | Status |
|---|---|---|---|
| `S1` | Claude Code — Security | <https://code.claude.com/docs/en/security> | ✅ fetched |
| `S2` | Claude Code — Data usage | <https://code.claude.com/docs/en/data-usage> | ✅ fetched |
| `S3` | Claude Code — Legal and compliance | <https://code.claude.com/docs/en/legal-and-compliance> | ✅ fetched |
| `S4` | Claude Code — Zero data retention | <https://code.claude.com/docs/en/zero-data-retention> | ✅ fetched |
| `S5` | Claude API — API and data retention | <https://platform.claude.com/docs/en/manage-claude/api-and-data-retention> | ✅ fetched |
| `S6` | Claude Code — Choose a sandbox environment | <https://code.claude.com/docs/en/sandbox-environments> | ✅ fetched |
| `S7` | Agent SDK — Securely deploying AI agents | <https://code.claude.com/docs/en/agent-sdk/secure-deployment> | ✅ fetched |
| `S8` | Claude Code documentation index (permissions, managed settings, managed MCP, monitoring, plugins) | <https://code.claude.com/docs/llms.txt> | ✅ fetched |
| `S9` | Anthropic Usage Policy | <https://www.anthropic.com/legal/aup> | 🔗 reference |
| `S10` | Anthropic Transparency Hub | <https://www.anthropic.com/transparency> | 🔗 reference |
| `S11` | A CISO's guide to agentic AI | <https://claude.com/blog/ciso-guide-to-agentic-ai> | 🔗 reference |
| `S12` | Mitigate jailbreaks and prompt injections | <https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks> | ✅ fetched |
| `S13` | Compliance API | <https://platform.claude.com/docs/en/manage-claude/compliance-api> | ✅ fetched |
| `S14` | Claude Enterprise plan | <https://claude.com/solutions/enterprise> | 🔗 reference |
| `S15` | **Anthropic Trust Center** — certifications, sub-processors, security documentation, report requests | <https://trust.anthropic.com> | 🔗 reference |
| `S16` | Anthropic Privacy Center | <https://privacy.claude.com> | 🔗 reference |
| `S17` | Anthropic Responsible Scaling Policy | <https://www.anthropic.com/responsible-scaling-policy> | 🔗 reference |
| `S18` | Commercial Terms of Service | <https://www.anthropic.com/legal/commercial-terms> | 🔗 reference |
| `S19` | Consumer Terms of Service | <https://www.anthropic.com/legal/consumer-terms> | 🔗 reference |
| `S20` | Privacy Policy | <https://www.anthropic.com/legal/privacy> | 🔗 reference |
| `S21` | Sandbox runtime (`@anthropic-ai/sandbox-runtime`) | <https://github.com/anthropic-experimental/sandbox-runtime> | 🔗 reference |
| `S22` | Claude Code — Security vulnerability reporting (HackerOne) | <https://hackerone.com/4f1f16ba-10d3-4d09-9ecc-c721aad90f24/embedded_submissions/new> | 🔗 reference |

---

## Maintaining this page

1. **Every new claim needs a source tag.** If you cannot tag it, it does not go on the page.
2. **Re-verify quarterly, and on every Claude Code / API release that touches security defaults.** Update the *Last verified* date at the top and the Status column above.
3. **Keep the three indexes in sync.** A new theme needs rows in the [Theme index](#theme-index) and in at least one [interest](#interest-index); a new FAQ entry needs its `→ Themes … · Sources …` footer and an anchor.
4. **Keep IDs in parity with the Japanese page.** `T#` / `I#` / `Q#` / `S#` are shared with [Claude-Security.ja.md](Claude-Security.ja.md). Add an entry to one, add it to the other under the same ID.
5. **Numbers and product names drift** — retention periods, model designations, plan feature lists and policy versions change. Prefer linking to the source over restating it when a value is volatile.
6. **Do not paste NDA-restricted material** (e.g. the full SOC 2 Type II report) into this repository. Link to the Trust Center request flow instead.

*This page is an internal study/reference aid maintained in this repository. It is not an Anthropic publication and carries no warranty. For contractual or audit purposes, cite the primary sources above.*
