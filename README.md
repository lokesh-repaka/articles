# 🛡️ Enterprise AI Governance & Security Architecture Series

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Articles](https://img.shields.io/badge/Articles-Published-success.svg)](articles/)
[![Keycloak](https://img.shields.io/badge/IAM-Keycloak_24+-red.svg)](https://www.keycloak.org/)
[![SPIFFE/SPIRE](https://img.shields.io/badge/Zero--Trust-SPIFFE%2FSPIRE-blueviolet.svg)](https://spiffe.io/)
[![Policy-as-Code](https://img.shields.io/badge/Policy--Engine-Open_Policy_Agent-green.svg)](https://www.openpolicyagent.org/)

> A curated, engineering-first repository of deep-dive architectural guides, real-world failure analyses, production blueprints, and hands-on implementations for securing and governing Autonomous AI Agents in enterprise environments.

---

## 📚 Articles & Architecture Guides

| # | Article Title | Core Focus | Architecture & Code | Status |
| :-: | :--- | :--- | :---: | :-: |
| **01** | [**The Missing Guardrail in AI: Why "Prompt Rules" Won't Save You and How Identity Governance Protects Production**](articles/01-ai-and-identity-governance/README.md) | AI Governance fundamentals, Replit DB drop & OpenAI sandbox escape postmortems, Keycloak Human IAM, SPIFFE/SPIRE Workload Identity, OPA policy gates. | [Companion Code](articles/01-ai-and-identity-governance/code/) | ✅ Published |
| **02** | **Deterministic Safety: Designing Multi-Tier Guardrails and Jailbreak Defense for Agentic Tool-Use** | LLM Guardrails, NeMo Guardrails, Tool-calling sanitization, and output verification pipelines. | Coming Soon | 📝 Planned |
| **03** | **Zero-Trust Workload Attestation for Multi-Agent Systems in Kubernetes** | Advanced SPIRE Server/Agent deployment, kernel-level PID/cgroup attestation, and mTLS mesh for autonomous agents. | Coming Soon | 📝 Planned |
| **04** | **Enterprise Identity Lifecycle (JML) & Separation of Duties (SoD) in Agentic Workflows** | Event-driven Joiner-Mover-Leaver automation with Keycloak events, Kafka triggers, and privilege creep prevention. | Coming Soon | 📝 Planned |

---

## 🚀 Quick Navigation: Featured Article

### Article 01: The Missing Guardrail in AI & Identity Governance
👉 **[Read the Full Article Here](articles/01-ai-and-identity-governance/README.md)**

#### Key Takeaways:
* **Natural language is not an authorization boundary:** Telling an AI *"DO NOT touch production"* in a system prompt is advice, not governance.
* **The Highway Analogy:** AI Model = The Driver; AI Governance = Guardrails, traffic lights, speed limits, police, and licensing.
* **The Two Halves of Identity:** 
  * **Human IAM:** Keycloak (Realms, Client Roles, JML Lifecycle, SoD).
  * **Workload Identity:** SPIFFE/SPIRE (Zero-trust attestation, short-lived SVIDs, Workload vs. Logical Agent identity).
* **Deterministic Policy Gates:** Mechanically blocking destructive actions (`DROP`, `DELETE`) with Open Policy Agent before reaching production data.

---

## 🛠️ Companion Hands-On Labs

Each article in this repository includes fully reproducible, production-style companion code under its respective `code/` directory.

To run the Article 01 laboratory (Keycloak + PostgreSQL + OPA + FastAPI AI Backend):

```bash
cd articles/01-ai-and-identity-governance/code
docker-compose up -d
```

---

## 📂 Repository Organization

```text
├── .gitignore                                 <-- Ignores *.excalidraw, logs, system files
├── README.md                                  <-- Master series index & roadmap
└── articles/
    ├── 01-ai-and-identity-governance/
    │   ├── README.md                          <-- Comprehensive technical article
    │   ├── images/                            <-- Hand-drawn & vector architectural diagrams
    │   │   ├── ai_governance_safety_highway.jpg
    │   │   ├── ai_incidents_infographic.jpg
    │   │   ├── identity_lifecycle_and_iga.png
    │   │   ├── keycloak_human_identity_governance.png
    │   │   └── spiffe_spire_workload_identity.png
    │   └── code/                              <-- Runnable companion implementation
    │       ├── docker-compose.yml
    │       ├── main.py
    │       └── policies/
    │           └── governance.rego
    └── 02-upcoming-topic/                     <-- Future articles follow the same modular pattern
```

---

## 👤 Author

**Lokesh Repaka**  
*AI Engineering, Enterprise Architecture & AI Governance*  
* [GitHub Profile](https://github.com/lokesh-repaka)

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).
