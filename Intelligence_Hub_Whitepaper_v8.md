  
**WHITEPAPER**

**The Distributed AI Economy:**

**Intelligence Hubs, Frames, Cogs, Ops, and the Accountability Plane**

*How a Three-Layer Architecture — Infrastructure, Execution, and Economy — with Cross-Cutting Validation* *enables Context-Sharing, Capability Exchange, and Accountable Intelligence*

July 2026  |  Confidential  |  Revision 8

# **Executive Summary**

The next decade of enterprise AI will be defined by which organizations successfully deploy, govern, and exchange their AI capabilities as owned operational infrastructure. The shift is already underway: enterprises are moving from renting intelligence through black-box APIs to owning it through sovereign, reproducible, and auditable deployments.

OpenTeams, built on an open-source ecosystem that includes Nebari, provides the infrastructure, abstractions, and marketplace layer that makes this shift possible at scale. This whitepaper describes the three-layer architecture at the heart of that vision, with a particular focus on how organizational context (the culture, terminology, and norms that fuel the ROI of AI) is captured, shared, and exchanged through a new class of artifacts and concepts.

* Infrastructure — OpenTeams assembles open-source and proprietary components into **customer-specific Intelligence Hubs** building on existing infrastructure the organization already relies on.  Nebari is OpenTeams’ flagship open-source infrastructure contribution that provides a reference architecture for some and a foundational platform for others.  Nebi provides the reproducibility and distribution mechanism for modular deployment of digital artifacts. This modular deployment is critical to a distributed AI infrastructure.

* Execution — Frames, Cogs, and Ops: Frames carry human-accountable organizational context and norms; Cogs are specialized AI workers that are oriented by those Frames; Ops are installable AI-infused workflows that document business processes, coordinating Cogs and standardizing human oversight.

* Economy — A distributed ecosystem and marketplace where Ops, Cogs, Frames, and Guards are published, discovered, installed, and exchanged across a network of Intelligence Hubs and the humans and organizations they serve

A cross-cutting accountability plane spans all three layers providing the critical step of  **Validation**. Frames inject accountable context into AI work; **Guards** verify that the resulting work is correct, safe, and policy-compliant; **Gates** are process check-points were decisions are made about whether work proceeds, pauses, escalates, or stops; and **Tracks** preserve the evidence needed for audit, learning, and trust. Every Op declares a Validation Strategy so that AI-generated work becomes accountable operational intelligence rather than unverifiable output.

| Plane / Layer | Core Units | What It Does |
| :---- | :---- | :---- |
| **Layer 1 — Infrastructure** | Intelligence Hub · Nebari · Nebi | Own, deploy, and integrate AI as sovereign infrastructure |
| **Layer 2 — Execution** | Frames · Cogs · Ops | Carry context, perform work, orchestrate outcomes |
| **Accountability Plane (cross-cutting)** | Guards · Gates · Tracks | Verify work, decide whether it proceeds, record evidence |
| **Layer 3 — Economy** | The Marketplace | Discover, exchange, and monetize artifacts across Hubs |

![][image1]

*Figure 1 — Three layers plus the cross-cutting Accountability Plane.*

Together, these three layers create something the enterprise AI market does not yet have: a principled path from infrastructure to outcome, with an economy of context, capability, and execution that scales as the network grows. This document also identifies the essential initial interface that brings this entire system to the people who must use it — a Desktop/Web Application that lets knowledge workers in every organization interact with their own Intelligence Hub to combine Frames, converse with Frame-oriented Cogs, run Ops, and share organizational context with internal and external collaborators.

The market opportunity is now well-quantified by independent research. McKinsey estimates sovereign AI could represent a $500–$600 billion market by 2030, driven by use cases in regulated industries and the public sector (McKinsey, December 2025). At the same time, PwC's 29th Global CEO Survey (January 2026, n=4,454) finds that 56% of CEOs report zero financial impact from AI and only 12% achieve both cost and revenue benefits. The gap between AI investment and AI outcome is the structural problem that OpenTeams' three-layer architecture is designed to close.

# **1\.  The Problem: Rented Intelligence Is Fragile, and Context Leaks Away**

Enterprise AI adoption is trapped in a paradox. Organizations understand that AI is strategically important, yet most remain dependent on vendor-controlled, black-box systems such as Codex, Claude Code/Cowork, Grok, or Gemini that they cannot inspect, reproduce, audit, or own. And even when they can deploy capable AI, they cannot capture and propagate the organizational context — the rules, terminology, goals, style, and norms — that turn generic AI into specialized, valuable work. The consequences result in delayed deployment of aligned and accountable intelligence across their organization.

| Failure Mode | Root Cause | Business Impact |
| :---- | :---- | :---- |
| Vendor lock-in | APIs controlled by third parties | Strategic dependency; cost unpredictability |
| Security Leaks | Data leaves the organization | Loss of competitive moat, intellectual property, plus regulatory risk in healthcare, finance, government |
| Execution opacity | No visibility into model behavior | Inability to audit decisions or reproduce results |
| Integration fragility | No standard for how AI plugs into workflows | High integration cost; frequent breakage |
| Value leakage | Capabilities cannot be shared or monetized | No mechanism for exchanging AI work |
| Context dissipation | No portable container for organizational rules, terminology, norms, skills, tools, prompts, and processes | Repetitive re-setup; brand and policy drift; context that fueled ROI does not stay with the organization that produced it |
| Governance vacuum | No mature framework for autonomous AI accountability or risk thresholds | Only 1 in 5 organizations has mature agent governance (Deloitte 2026); 56.4% surge in AI incidents in 2024 (Stanford HAI); 43% lack any formal AI governance policy (PEX 2025/26) |
| Talent scarcity | Insufficient internal AI expertise; advanced infrastructure skill concentrated in a few firms | Insufficient worker skills cited as the \#1 barrier to AI integration (McKinsey State of AI 2025); only 20% of companies report high preparedness on talent (Deloitte 2026\) |

The root cause is architectural: the market lacks a standard model for what an owned AI deployment looks like, how AI capabilities are packaged into executable units, and — critically — how the cultural and contextual knowledge of the organization is encoded, inherited, shared, and exchanged. Without these standards, enterprises cannot own intelligence. They can only rent it and risk potential exposures without suitable auditability.

Two market voices have framed this gap with unusual clarity. Microsoft CEO Satya Nadella, speaking at WEF Davos 2026: "If you're not able to embed the tacit knowledge of the firm in a set of weights in a model that you control, by definition you have no sovereignty. That means you're leaking enterprise value to some model somewhere." Vista Equity Partners CEO Robert F. Smith, whose firm owns more than $100 billion of enterprise software, has been blunter: "I'm shocked that CEOs haven't done a good job preserving sovereignty and dominion. They were on an ARR race, chasing growth in a way that they've leaked intellectual property." A Microsoft CEO and a major enterprise software owner saying the same thing from different vantage points is the strongest available validation of the architectural problem.

# **2\.  The Vision: A Distributed Economy of Owned Intelligence**

OpenTeams' vision is a world in which every organization — enterprise, government, research institution, or startup — has its own Intelligence Hubs: sovereign, governed environments that integrate the organization’s data, legacy applications, AI-native workflows, policies, and models within its own infrastructure perimeter — appropriately virtualized, spanning private cloud and edge — into an owned operational intelligence system.

Independent research validates this approach as both necessary and architecturally achievable. Brookings Institution, in its February 2026 analysis "Is AI Sovereignty Possible?", concludes that "full-stack AI sovereignty is structurally infeasible for almost any country — meaning the market for trusted platform intermediaries is permanent, not transitional." Stanford HAI's AI Index 2026 identifies four objectives that countries and enterprises pursue through sovereign AI: cultural autonomy, national security, economic competitiveness, and regulatory oversight, each of which maps directly to capabilities the Intelligence Hub architecture provides. McKinsey's March 2026 framing closes the loop: "Ultimately, sovereign AI is not about full-stack independence. It is an ecosystem play. Those who orchestrate coherent systems, where sovereignty is applied deliberately at critical control points, will turn infrastructure into trusted capabilities and turn trusted capabilities into scaled outcomes."

These Hubs which provide segmented areas of integrated expertise and collaboration for each organization that deploys them do not have to remain isolated. They can connect with each other as a drawbridge connects walled castles so that appropriate derived results from the AI explorations can flow and enable coordinated collaboration as managed by the policies of the organizations that are accountable for the data they manage.   Our vision and roadmap includes at least four specific artifacts that can be versioned, managed, and exchanged across these digital pathways:

* Frames — scoped artifacts that carry organizational context, terminology, norms, skills, tool expectations, prompts, architecture, and process details.  These can be authored, inherited across scopes, and shared with internal teams or external partners

* Cogs — the potentially specialized AI workers that perform discrete tasks within an organization, oriented by the Frames that apply to them.  These can be explored, configured, specialized, and managed both within the Hub's control plane and connected to via the Desktop/Web Application.  These are reproducible, modular, self-contained cognitive workers, or agents.

* Ops — installable, versioned programs of AI-influenced or AI-driven work.  These can be published and installed by enterprises, automating business processes that combine Cogs oriented by specific Frames and accountable to human oversight.

* Guards – installable, versioned test and verification code that confirms the output of AI is in line with standards and guidelines of the organization.

| The Three-Layer Thesis |
| :---- |
| Layer 1 — Infrastructure:  The open-source AI ecosystem (Nebari prominent among many tools) assembled by OpenTeams into each organization's Intelligence Hub (the deployment), with reproducibility ensured by Nebi or other reproducibility tool. |
| Layer 2 — Execution:  Frames (shared context) \+ Cogs (AI workers) \+ Ops (installable programs) |
| Layer 3 — Economy:  The ecosystem, community sharing mechanism, and marketplace mechanisms where Frames, Cogs, Ops, and Guards can be shared and exchanged between Hubs |
| Accountability Plane — Validation:  Guards (verification components) \+ Gates (decision points) \+ Tracks (evidence records) — one plane cutting across all three layers to make AI work verifiable, governable, and auditable |
|  |
| "We don't just provide infrastructure. We define how AI context, work, validation, and outcomes are packaged, executed, verified, and exchanged." |

There is a useful analogy in the emerging category of AI-native “software factories.” Companies in this emerging category have built software factories that orchestrate the full software development lifecycle — capturing requirements, architecture decisions, and structured context upstream, then feeding that context to AI agents so they produce consistent, governed, maintainable software rather than ad-hoc code. The insight is sound: the value is not in raw generation, but in the structured context and governance that surround it.

OpenTeams is building something adjacent but more fundamental: an Intelligent Ops Factory. Where a software factory produces software products, the Intelligent Ops Factory produces, and continuously maintains standard operating procedures for the company in a fabric of independent, Accountable Intelligence Hubs, each populated with the Frames, Cogs, and Ops that a specific organization or division needs. The output is not an application; it is operational intelligence and automated operations that the organization owns.

**The future is not software alone. It is accountable and intelligent operations built on software, data, models, and governed context.**

Critically, OpenTeams is not building “the Intelligence Hub to rule them all.”  While we do have a public intelligence Hub as a reference and example for small organizations that cannot yet build their own, our vision is not to create one central Hub.  There is not a mandatory platform that all users must flow to. OpenTeams is committed to a distributed fabric of owned intelligence and we build modular capability including open-source infrastructure as well as  the Frame, Cog, Op, and Guard open-source standards.  We also build Nebari and Nebi and a Desktop/Web Application that serves as a gateway to the company Hub.  This enables each organization to rapidly assemble and maintain its own Intelligence Hub, with its own Frames, Cogs, and Ops, accessed through a Desktop/Web Application its people configure for internal use. The result is a fabric of sovereign Hubs, each fully owned by the organization that operates it, interoperating through shared open standards rather than through a shared owner.  OpenTeams is eager to provide maintenance and support for anyone’s Hub so that ownership of an intelligence Hub does not have to correlate with technical or AI engineering expertise.

This is where OpenTeams' role becomes clear. The open-source AI ecosystem is vast, fast-moving, and fragmented — model servers, vector databases, orchestration frameworks, observability tooling, identity systems, and far more, each evolving rapidly, each with several competing options. Few organizations have the time or the in-house expertise to assemble these into a coherent, governed, production-grade Intelligence Hub on their own. OpenTeams is the concierge to that ecosystem: one accountable partner responsible for selection, integration, hardening, maintenance, and evolution. We ensure your Intelligence Hub is built well, built right, and kept current, positioning your organization for full participation in the distributed AI economy with complete ownership of your data and your intelligence.

# **3\.  Layer 1: Infrastructure**

Layer 1 is infrastructure: the foundation on which Accountable Intelligence is built. It comprises three things — the open-source AI ecosystem that OpenTeams draws on (with Nebari as our flagship contribution), the Nebi reproducibility layer that makes deployments durable and portable, and the client-specific Intelligence Hub itself, the organizational deployment where it all comes together. The throughline across all three is that no single tool is the infrastructure. The infrastructure is the disciplined assembly of many open-source tools, perhaps including Nebari or components of Nebari, into a coherent whole the organization owns.

The canonical relationship is worth stating once and holding to throughout: **Nebari is OpenTeams’ flagship open-source contribution to the AI infrastructure ecosystem. Nebi is the reproducibility and distribution mechanism. The Intelligence Hub is a customer-specific assembly of open-source and proprietary components that OpenTeams integrates, governs, and maintains.**

## **3.1  Nebari — A Modular Open-Source Stack for AI**

Nebari (https://nebari.dev) is an open-source ecosystem for deploying, managing, and scaling AI infrastructure in a reproducible and governed way. Since June of 2025, the project has rearchitected its core into a modular, composable open-source stack for AI. At its foundation is a layer called nebari-infrastructure-core, on top of which sit more than fifteen software packs at varying levels of maturity. These packs provide capabilities ranging from the Jupyter-based data-science use case that was the original goal of Nebari classic, to serving open-weight LLMs and GenAI chat. What began as a collection of tools for data science and distributed machine learning on clusters has grown into a composable stack that brings high-level AI applications and lower-level infrastructure components together under a consistent, reproducible standard.

Within the scope it covers, Nebari standardizes:

* Compute and environment management across cloud and on-premise infrastructure

* Model deployment and versioning with reproducibility built in

* Tooling interoperability and integration patterns across the AI/ML ecosystem

* Role-based access control, audit logging, and governance primitives

Crucially, Nebari is open-source and additive.  Most organizations will already be using some parts of Nebari as the software is a curated set of open-source components, published in a modular way — even if they obtain those components some other way. The collection of tools distributed in Nebari can be used à la carte and added to any existing infrastructure choices. The same dynamic that made NumPy the universal array standard (and made the rest of the scientific Python ecosystem possible) applies here: when the infrastructure layer is open, trust compounds and adoption accelerates. Travis Oliphant, the original creator of NumPy and a co-founder of Anaconda, brings exactly this institutional credibility and ecosystem-building experience to the Nebari project. Dharhas Pothina, who has been guiding Nebari's development for the past six years, brings deep experience deploying open source in the enterprise and in government to open-source projects.

It is important to be precise about Nebari's place in the architecture. Nebari is OpenTeams' company-backed contribution to the open-source AI ecosystem — but it is one contribution among the many tools that the ecosystem offers. An Intelligence Hub is not “a Nebari deployment.” It is a purpose-built assembly of the right open-source components for a specific organization, in which Nebari may play a useful role but rarely the only one. This distinction is what keeps OpenTeams honest as an ecosystem concierge rather than a single-product vendor, and it is what guarantees that an organization's Hub reflects its actual needs rather than any one project's roadmap.

The strategic case for an open standard is now broadly validated by the market. The Open Source Initiative's 2026 State of Open Source Report (n=700+ practitioners) finds that avoiding vendor lock-in has emerged as one of the leading drivers of open source adoption — cited by 55% of respondents, a 68% year-over-year increase. Separate software-composition analyses have long found open-source components in the overwhelming majority of commercial codebases (Black Duck OSSRA). Industry analysis from January 2026 puts it directly: "Open standards for AI will be essential because they allow the entire ecosystem to inspect, test, and harden the protocols agents use. When those interfaces are closed or proprietary, you end up with blind spots." Nebari extends this proven open-source pattern to AI infrastructure precisely as the market is demanding it.

## **3.2  Nebi — The Packaging and Reproducibility Layer**

Nebi is the installation foundation for the Intelligence Hub that handles definition, installation, and lifecycle management of complex deployable environments. Nebari is OpenTeams’ flagship open-source contribution to the AI infrastructure ecosystem; Nebi is its contribution to reproducibility and distribution — the mechanism by which AI environments, models, dependencies, Frames, Cogs, Ops, and Guards are specified, versioned, and deployed with full reproducibility.

Nebi's role in the architecture is foundational:

* It defines the common format by which Frames, Cogs, Ops, and Guards can be packaged for distribution

* It manages dependencies and environment snapshots so that an Op installed in one Hub behaves identically (within generative AI limits) to the same Op installed in another

* It enables versioned rollout and rollback of AI systems, contextual Frames, and the Cogs that depend on them

* It provides the installation primitive and reproducibility guardrails that makes the marketplace technically possible

Because Nebi can package anything the open-source community creates, Nebi is the bridge between the open-source ecosystem’s varied standards and the Frame / Cog / Op / Guard ecosystem. Without Nebi, these artifacts would be application-layer agreements without infrastructure-layer enforcement. With Nebi, reproducibility is guaranteed by construction.

## **3.3  The Accountable Intelligence Hub — The Organizational Deployment**

An Intelligence Hub is a particular configuration of open source components that are deployed inside an organizational perimeter. Based (potentially) on Nebari and packaged or distributed with Nebi, it is the concrete realization of the standard: a running system that integrates models, data, business systems, workflows, and the organization's accumulated Cogs and Frames into a unified, governed AI control plane.

The personalized Enterprise Intelligence Hub is the centerpiece of the overall architecture. It is what enables owned intelligence and accountability.  It is where Frames are made manifest and connected to a Cog. It is where Cogs are referenced, installed, configured, and run against organizational Frames. It is where Ops orchestrate Cogs to deliver business outcomes. It is where an organization's AI capabilities live. And it is what connects an organization outward to the marketplace, both as a consumer of Frames, Cogs, Ops, and Guards published by others and, over time, as a publisher of its own.

Key characteristics of an Intelligence Hub:

* Operates inside the organization's own infrastructure perimeter (cloud, on-premise, or hybrid)

* Integrates with existing enterprise systems and applications (ERP, CRM, data warehouses, APIs)

* Enforces organizational governance policies on model behavior and data access

* Stores, versions, and manages the inheritance graph of organizational Frames

* Provides full auditability of AI actions and decisions

* Stores and governs Tracks — the durable evidence records of AI work — for audit, learning, and accountability

* Connects bidirectionally to the emerging OpenTeams marketplace for Frame, Cog, Op, and Guard discovery and publication

No two Intelligence Hubs are identical, and that is by design. Each is assembled for a specific organization from the open-source ecosystem and their existing data and compute architecture. Every  company already has models, data systems, and compliance requirements along with existing infrastructure. OpenTeams does not ask anyone to migrate to a new platform.  OpenTeams acts as the concierge to the assembly of their personalized Intelligence Hub offering key concepts, technologies, and management to enable AI ownership  OpenTeams is an accountable partner who provides guidance and labor.  We can help select, integrate, harden, and maintain the right open-source components, potentially including (parts of) Nebari into a Hub that is built well, built right, and wholly owned by the organization. This single accountable partnership is what turns a sprawling open-source ecosystem into a dependable, production-grade deployment.

The on-premise hybrid enterprise market — the deployment surface for Intelligence Hubs — is sized by Deloitte at over $50 billion in 2026 (TMT Predictions, November 2025). Deloitte's State of AI in the Enterprise 2026 (n=3,235 senior leaders) further finds that 77% of enterprises now factor an AI solution's country of origin into vendor selection, and 58% build their AI stacks primarily with local vendors. McKinsey frames the architectural requirement precisely: "An effective sovereign ecosystem is not necessarily one in which everything is built domestically — it is one in which key control points are sovereign by design" (March 2026). The Intelligence Hub is the realization of exactly this design principle.

Data interoperability is itself an independently validated pain point. PwC's 2026 Digital Trends in Operations Survey (n=767) reports that 87% of operations leaders say poor data quality has hampered their progress in achieving value from digital initiatives. McKinsey's March 2026 analysis adds the prescription: "Localization keeps data inside, but it does not automatically make data usable. Strong sovereign ecosystems build data products and sharing mechanisms." The Intelligence Hub is the data integration surface that makes this possible — connecting to ERP, CRM, data lakes, and knowledge bases through Nebi, with governance applied at the data access layer.

## **3.4 Organizational Memory — The Hub's Persistent Context Layer**

Organizational Memory is the persistent context substrate of the Intelligence Hub and used by the Ops and Cogs to create organizational coherency and alignment. It is what turns the Hub from a server-side deployment of AI tools into a compound learning system that accumulates and applies the organization's accumulated context, interactions, and outcomes over time.

This concept is implied throughout the architecture but warrants explicit treatment. Frames give the organization a way to encode *intentional and human-accountable* context — what they have chosen to make explicit and shareable with defined granularity.  Cogs and Ops generate *emergent* context encapsulating what actually happens when AI work is performed. Organizational Memory is where both kinds of context live, accumulate, and become available to future work.  Guards, Gates, and Tracks are also part of the full organizational memory which is the foundation of the internal knowledge base that organizational intelligence acts upon.

#### **A Continuum of Implementations**

Organizational Memory is a capability and a concept – not a single product. It can be implemented along a wide continuum of sophistication, and organizations should adopt the level that matches their needs and maturity:

**At the simplest end**, Organizational Memory could be a structured collection of Frame files in a version-controlled directory. Frames capture the organization's accumulated context; the version history captures how it has evolved. Many organizations will start here, but most will not find this sufficient.

**At the most sophisticated end**, Organizational Memory may include:

* Full conversational records of every Cog interaction across the organization  
* Semantic retrieval over those records so future Cogs can be informed by what came before  
* Structured records of every Op execution — its inputs, outputs, and human-in-the-loop decisions (Gates and Tracks)  
* Knowledge graphs connecting concepts, decisions, people, and outcomes  
* Existing knowledge bases, business information, and existing data in existing ERP systems.  
* Time-aware retrieval that distinguishes recent context from historical context

Most organizations will sit somewhere along this continuum, and their position should evolve over time as needs and capabilities mature.

#### **Implementation Approaches**

The Intelligence Hub does not prescribe a particular technology for Organizational Memory.  It creates integration points and governance hooks for whatever is chosen. Organizations can compose their Organizational Memory from any combination of:

* **Versioned Frame repositories** — Git, GitHub, or GitLab for managing collections of Frame files or just object storage. The simplest and most universally applicable approach.  
* **Knowledge bases and wikis** — Confluence, Notion, or Obsidian, or just directories of files for structured organizational knowledge that Frames reference and Cogs consume.  
* **Vector databases for semantic retrieval** — Chroma, Weaviate, Qdrant, Milvus, or PostgreSQL with pgvector for storing and retrieving Cog interactions and organizational documents by semantic similarity.  
* **Specialized AI memory frameworks** — Mem0, Letta, or Zep, designed specifically for managing AI-system memory; LangChain and LlamaIndex memory modules for integration with broader pipelines.  
* **Observability and tracing platforms** — LangSmith, Phoenix (Arize), or Helicone for capturing and structuring the full history of AI interactions.  
* **Knowledge graphs** — Neo4j, ArangoDB, or similar tools for representing the relationships between concepts, decisions, and outcomes within the organization.  
* **Data lakes and warehouses** — Snowflake, Databricks, Iceberg, BigQuery, or PostgreSQL as durable substrates for long-term retention of AI-related organizational data.

A typical configuration combines several of these: An object-store database for Frame versioning, a vector database for semantic retrieval over Cog conversations, and an observability platform for capturing Op executions including Tracks. The Intelligence Hub provides the unified interface that lets these capabilities serve the organization as a coherent memory layer rather than disconnected silos.

#### **Governance and the Boundary**

Organizational Memory is among the most sensitive capabilities of the Intelligence Hub. It captures what the organization has thought, decided, and discussed with AI assistance. Strong governance is therefore essential:

* Access controls that distinguish who can read what within the memory  
* Retention policies aligned with regulatory and compliance requirements  
* Anonymization or redaction capabilities for sensitive content  
* Audit trails that record who accessed memory and when  
* The ability to forget — to remove specific memories when required by policy, law, or individual request

The fact that Organizational Memory lives inside the Intelligence Hub, under the organization's governance perimeter, is what distinguishes it from third-party AI memory services that retain context on vendor infrastructure. **Organizational Memory belongs to the organization that produced it.** That is the whole point. Its essential connection to the organization is why each organization must build and implement their own Intelligence Hub.  It cannot be rented or bought from a vendor.  Particular components and portions can be maintained by service providers and vendors, but the organization’s specific set of Intelligence Hubs will increasingly define the essence of the organization and cannot be outsourced.  Contractors, vendors, and companies can and will be brought in to enrich, refine, improve, and support the maintenance of the organization’s intelligence Hubs including its memory infrastructure.

# **4\.  Layer 2: Execution — Frames, Cogs, and Ops**

## **4.1  The Insight: From Models to Work**

The critical gap in enterprise AI today is not at the model layer. Foundation models are powerful and improving rapidly. **The gap is at the execution layer: how do you take a capable model and turn it into a reliable, auditable, governable unit of work that a real enterprise can deploy, manage, and trust? And, equally important, how do you make sure that the organizational context that fuels the ROI of AI stays with the organization that produced and enriched it, rather than dissipating into prompt-engineering one-offs and vendor-side conversation logs?**

This is the problem that Frames, Cogs, and Ops solve together. They form a layered execution model that bridges infrastructure to outcome, with context preserved at every level.

The execution gap is now well-documented across multiple independent sources. McKinsey finds that 72% of enterprises have sovereign AI on their roadmap but only 13% are on track to execute (December 2025). PwC's 29th Global CEO Survey shows only 12% of CEOs report both cost AND revenue benefit from AI; 56% report no benefit at all (January 2026, n=4,454). CEOs with strong AI foundations are three times more likely to report meaningful financial returns. Deloitte's State of AI in the Enterprise 2026 finds only 34% of organizations are genuinely reimagining their business with AI, and only 1% describe themselves as AI-mature. The structural answer is not better models — it is governed, installable, Frame-aware execution. This is precisely what Ops, Cogs, and Frames are built to provide.

| The Progression of Value |
| :---- |
| **Models** predict tokens. |
| **Frames** orient humans and Cogs to shared context, terminology, and norms. |
| **Cogs** perform specialized AI work under Frames, skills, tools, memory, permissions, and Guards. |
| **Ops** orchestrate outcomes with human oversight. |
| Each layer adds structure and purpose, and enables distributed governance, autonomy, and accountability. |
| **A Running Example — The Vendor Fraud Review Op** |
| An accounts-payable analyst launches a single Op: **Vendor Fraud Review**. Everything the rest of this paper describes happens inside it. |
| **Frames:**  the Company Policy Frame, the Procurement Rules Frame, and a Fraud Detection Methodology Frame orient every step. |
| **Cogs:**  an Invoice Extraction Cog, a Vendor Risk Cog, and an Anomaly Summary Cog perform the discrete AI work. |
| **Guards and Gates:**  Schema, Source, Privacy, and Consensus Guards check the work; low confidence or high vendor risk routes the case to a human reviewer before any vendor is flagged. |
| **Track:**  the full execution record — Frames applied, Guards run, Gates passed, approvals given — is retained for audit and regulatory review. |
| The example returns in the Cog and Op definitions below, at the Gates of Section 5, and as a complete Op manifest in Section 5.6. |

## **4.2  How Frames, Cogs, and Ops relate to "Agents"**

The term "AI agent" is increasingly overloaded and carries significant risk connotations. Typical capabilities traditionally called agents are a combination of two or more the elements explored here.  Frames, Cogs, and Ops provide agentic capability with more granularly defined concepts that can be deployed in billions of compound AI systems across the world. **Frames, Cogs, and Ops deliver the automation power of AI agents with the governance guarantees real organizations require. Their use signals that the organization is relying on the OpenTeams brand promise of ensuring that the organizational context that fuels the value of AI stays governed and managed by the organization.**

The data on agent deployment without governance is now stark. Only 1 in 5 organizations has a mature governance model for autonomous AI agents (Deloitte State of AI in the Enterprise 2026). AI incidents surged 56.4% in 2024 to a record 233 (Stanford HAI AI Index 2025). Only 43% of organizations have any formal AI governance policy at all (PEX Report 2025/26). Industry analysts now warn that in 2026, regulators and courts will begin clarifying responsibility when AI systems act with limited human oversight — and that in healthcare, AI governance "will no longer differentiate vendors; it will determine whether systems can be deployed at all" (Dataversity, February 2026). The Frame, Cog, and Op architecture is built precisely for this regulatory environment.

## **4.3  Frames — Shared Cultural Alignment**

A Frame is a scoped, text-based artifact — a file or folder of files using an open protocol — that carries the cultural and operational context within which work happens. Every organization has implicit context: brand voice, technical terminology, regulatory constraints, departmental conventions, team norms, project goals. Today, this lives in style guides, wikis, Slack history, onboarding documents, and the heads of senior employees. When AI is brought to bear without this context, the organization must re-explain itself in every interaction, and the resulting work suffers — generic, inconsistent, and disconnected from how the organization actually operates.

Frames make this context explicit, portable, inheritable, nestable, and shareable. A Frame is read by humans, applied by Cogs, and portions exchanged across organizational boundaries when appropriate. Frames are first-class artifacts: they live independently of Cogs and Ops and can be authored, discovered, exchanged, and inherited on their own.

A Frame typically carries a mix of cultural context (the why and what of the work) and the concrete artifacts that operationalize that context (the how and with what):

* Rules — what is and is not acceptable behavior within the scope

* Terminology — the words, names, and definitions specific to the organization, function, or project

* Goals — what success looks like; what outcomes are valued

* Style — tone of voice, formatting conventions, brand expression

* Norms — implicit expectations about how work gets done

* Skills — named capabilities the work depends on

* Tool specifications — Nebi (or similar) spec files that document the tools the Frame expects to be available

* Output Guards – Validation tools (See Section 5\) to be run to verify the AI produces what is intended.

* Prompts — reusable prompt fragments to be loaded into Cog context

* Architecture descriptions — relevant software and system context that orients the work

* Business process details — the procedural backbone that the work follows

Frames are characterized by  essential properties:

| Property | What It Means | Why It Matters |
| :---- | :---- | :---- |
| Scoped | Each Frame applies to a defined scope: organization, department, team, project, role, or relationship | Context applies where it should, and not where it shouldn't |
| Inheritable | A child Frame inherits and extends a parent Frame (project inherits department inherits company) | Organizational hierarchy is reflected in context propagation; the chain of authority is auditable |
| Composable | Multiple Frames can be combined for a given work session | A user can layer company \+ department \+ project \+ ad-hoc context as the work requires |
| Shareable | Frames can be shared internally with colleagues or selectively externally with partners, vendors, and customers | Context flows where collaboration requires; reviewed subsets protect what should remain internal |
| Discoverable | Frames can be published to internal libraries, communities of practice, and open registries where others find and adopt them | Context portability extends beyond direct relationships; the vast majority of Frames spread through community adoption rather than commercial sale |
| Owned | Each Frame is owned by and **accountable to** a human or a group of humans that intentionally manage it. | Frames are a slice of direct human accountability in the context and is fundamental to creating accountable intelligence. |

### One of the critical things that Frames can do is define a Validation or Verification tool (a Guard) that must be called and pass on the output of the system.

### **Why Frames Are a Distinct Architectural Layer**

It would be tempting to think of Frames as just "prompts" or "system messages" or just “skills” or snippets that an AI provider could provide through an API. This understates what Frames are and the important conceptual role they play in accountability and governance.  A Frame is not a prompt; it is an organizational artifact governed by the organization that owns it. Frames are versioned, audited, owned, inherited, and exchanged. They embody competitive intelligence, regulatory knowledge, brand identity, and operational doctrine. They are the cultural commons of the organization, made explicit and portable, but also protectable and governed and something worth preserving within a private cognitive context and not just shared with a rented intelligence.

Concretely, an organization might maintain Frames such as:

* A Brand Voice Frame published by the marketing function, used by every Cog that drafts external communications

* A Healthcare Compliance Frame maintained by the legal team, automatically incorporated into any Cog touching patient data, and pointing to a Guard that must be run after every output.

* A Q4 Sales Playbook Frame shared across the sales organization for the duration of the quarter

* An External Vendor Frame, with selectively-shared sections, given to a procurement partner so their AI work aligns with the organization's expectations

* A Pharma R\&D Compliance Frame published by an industry consortium and adopted by hundreds of pharmaceutical companies for use in their Hubs

### **Frames in Practice: Five Example Use Cases**

Beyond the architectural definition, Frames can address specific human alignment problems that every organization faces — and that AI traditionally makes worse, not better. OpenTeams itself uses Frames across these dimensions, and we expect every organization adopting an Intelligence Hub will find similar opportunities to use Frames to facilitate collaborative efficiency: 

**1\.  Internal alignment across the company.** Every organization accumulates implicit context such as vocabulary, values, brand voice, and operating norm. This implicit context grows faster than any onboarding program can capture. Today that context lives in style guides, wikis, Slack archives, and the heads of senior employees, where new hires cannot easily reach it and AI systems cannot effectively be oriented by it. OpenTeams maintains a Company Frame that codifies its vocabulary, brand voice, strategic narrative, and core values. Every division, team, project, and individual Frame inherits from it. Every Cog conversation an OpenTeams employee has, and every Op an OpenTeams employee launches, is oriented by it. Brand and policy alignment compounds with use. 

**2\.  Aligning sister companies and ecosystem peers.** OpenTeams operates within an ecosystem of related organizations that share strategic direction without sharing corporate boundaries. By publishing Product Direction Frames, OpenTeams gives these sister organizations' teams and AI workers access to the latest product thinking, roadmap, vocabulary, and positioning. The alignment travels through the relationship; the corporate boundaries remain intact. What used to require quarterly all-hands and an inevitable lag in shared understanding becomes a single artifact that everyone inherits and updates in place.

**3\.  Keeping open-source communities aligned.** Open-source communities depend on alignment — shared vocabulary, contribution conventions, technical standards, project governance. By publishing Community Frames, project maintainers give every contributor (and every AI worker assisting a contributor) the context needed to participate without first reading every wiki page and Slack archive. Nebari, the broader Python AI ecosystem, and adjacent communities stand to benefit substantially from this mode of coordination — and OpenTeams will lead by publishing Community Frames for the projects we steward.

**4\.  The foundation of partner engagement.** Every external relationship at OpenTeams — system integrators, technology partners, channel resellers, customer engagements — can begin with a Partner Frame. The partner installs the Frame; their teams and their AI workers immediately operate in OpenTeams' vocabulary, against OpenTeams' definitions of success, with OpenTeams' brand voice when appropriate. Partner engagement becomes architecturally repeatable instead of reinvented relationship by relationship. The Frame is the contract of context.

**5\.  How we message to investors.** Investor communication is the highest-leverage messaging an organization produces. OpenTeams maintains an Investor Frame that codifies the strategic narrative, the financial vocabulary, the proof points, and the voice for investor audiences. Pitch decks, briefings, follow-up conversations, and investor-facing AI work all inherit from it. The risk of message drift at scale, where different team members tell subtly different versions of the company's story, becomes structurally less likely. The Investor Frame keeps the narrative coherent across every surface where it appears.

These five use cases share a pattern. Each begins with a coordination problem that scales painfully — internally, across ecosystems, externally. Each is currently addressed (when at all) through ad-hoc documents, repeated meetings, and the slow propagation of tribal knowledge. Each is solved cleanly by a Frame: a single, versioned, inherited, shareable artifact that carries the right context wherever it needs to go. This is what we mean when we say Frames are infrastructure for organizational alignment.

The Frame protocol — an open specification for how these artifacts are structured — is the standard that makes this exchange possible. Just as Nebari standardizes infrastructure and Nebi standardizes packaging, the Frame protocol and concept standardizes cultural alignment. Together they form the open foundation on which the entire distributed AI economy can be built.

## **4.4  Cogs — AI Workers Oriented by Frames**

A Cog is a discrete, AI-powered worker. It is the atomic unit of AI work within the system. A Cog encapsulates:

* A model that may be tailored or specialized for a set of tasks (e.g., document classification, data extraction, code review, customer response generation, accounting recommendations, marketing acumen)

* A context, including one or more Frames, that orients the model to a particular kind of work within the right organizational culture

* The skills, tools, and APIs it has access to

* Its governance parameters: what data it may access, what actions it may take, what requires human approval

Cogs are the key artifact distributed by Nebi and can include all the code (plus dependencies) and all the weights needed to generate an output from an input. Because a Cog is both the context and the model, but models with their large numbers of weights can be very large, there are typically three different types of Cogs:  (1) A model-heavy COG which deploys the foundation model that can generate tokens based on inputs, (2) A context-heavy COG which focuses on the data and context to be sent to the model which is pointed to (either via dependency or an API end-point, and (3) a combined model and context COG – a complete isolated AI worker with everything needed to respond to inputs oriented by the stored context. 

Context management is central to Cog construction and operation — arguably the discipline that most determines a Cog's usefulness. Every Cog needs a context within which to operate: the body of information that orients its underlying model toward the right work, in the right way, for the right organization. Frames are the foundation of that context — they carry the durable, governed, shareable cultural and operational knowledge the Cog must respect. But a Cog's working context is typically much richer than its Frames alone. It can include retrieved documents, relevant slices of Organizational Memory, recent conversation history, tool outputs, real-time data, and task-specific instructions assembled at invocation time. Deciding what the model sees, in what order, and under what constraints is a first-class engineering concern. Frames make the foundational layer of that context portable, governed, and reusable; the rest is assembled around them. **A well-constructed Cog is, in large part, a well-managed context.**

Cogs are important because they are the level at which AI behavior becomes auditable and governable, much like a worker. Rather than asking "what did the model do?", an organization can ask "what did this Cog do, with what inputs, under which Frames, and what was the outcome?" This specificity — combined with the Frames that orient the Cog — is what makes Cogs deployable in regulated industries and high-stakes workflows.

The productivity case for governed AI workers is now backed by peer-reviewed academic research. The NBER study "Generative AI at Work" (Brynjolfsson, Li, and Raymond) examined 5,179 customer-support agents in a randomized study and found a 14% average productivity gain from AI-assisted work — with a 34% improvement for novice and low-skilled workers. As the authors note, AI "disseminates the best practices of more able workers and helps newer workers move down the experience curve." NBER Working Paper 34984 (March 2026, n=750 executives) finds that labor productivity gains from AI are positive, vary across sectors, and are expected to strengthen in 2026 — with the largest effects concentrated in high-skill services and finance. Cogs operationalize these findings within a governance-and-context layer that the underlying models do not provide on their own.

Cogs are not generally intended to be standalone agents, though they can be in simple circumstances. They can be interacted with directly for debugging, validation, analysis, maintenance, or simple operations. Normally, they operate within the context of an Op, which provides the coordination logic, the workflow structure, the goal-oriented looping, the validation functions, and the human oversight framework. A Cog produces an output from a model (or a collection of other Cogs); an Op combines this with other layers of the compute ecosystem in a human-led process that does the right thing with the outputs of Cogs — all of it shaped by the Frames that apply.

In the running example, the Vendor Fraud Review Op coordinates three Cogs — invoice extraction, vendor risk scoring, and anomaly summarization — each oriented by the same procurement Frames, each individually auditable, and none of them trusted blindly: their work is checked by the Guards described in Section 5\.

## **4.5  Ops — Orchestrated AI Workflows**

An Op is the application of the distributed AI economy. It is the orchestrated, supervised AI workflow that a human at the keyboard usually invokes or launches.  This is the automation at the highest level that maps onto how knowledge workers think about doing their job. "Close the books." "Onboard this customer." "Qualify this lead." "Draft this campaign." "Review this vendor for fraud." Each of those is an Op.

An Op is composed of:

* One or more Cogs — the AI workers performing discrete cognitive tasks, each carrying their own embedded Frames

* Additional Frames applied at the workflow level — context that orients the Op as a whole, beyond what individual Cogs already carry

* A supervising model that may coordinate Cog execution, sequences and parallelizes work, and handles unexpected conditions

* Human-in-the-loop feedback points where reviewers approve, refine, or redirect the AI work at meaningful checkpoints

* **A declared Validation Strategy** — the Guards the Op applies, the Gates that determine whether work proceeds, and the Track it preserves for audit (see Section 5\)

* Integration logic for connecting to enterprise systems, data lakes, and APIs

* A Nebi-compatible manifest that specifies dependencies, environment requirements, and configuration parameters

Ops are designed to be invoked through any interface the user already finds natural:

* As an application icon clicked from the Desktop/Web Application launcher

* As a command typed into a CLI or chat interface

* As a button pressed or a link followed within the Intelligence Hub or other integrated business application

* As a scheduled job triggered by time, event, or external system

The Op abstraction is what makes the marketplace possible at the outcome layer. Because an Op is self-contained, versioned, and installable via Nebi, it can be authored once and deployed into any Intelligence Hub that implements the standards needed — automatically picking up the local Frames that apply. This is analogous to how an NPM or pip package is authored once and installed across millions of environments, but for supervised, Frame-aware AI workflows rather than software libraries — and adapted at install time to the consuming organization's culture and norms through Frames.

The market trajectory validates this architectural bet directly. Deloitte's TMT Predictions 2026 anticipates that "there will also likely be agent marketplaces, where internal and external agents get published and businesses can discover and integrate new capabilities dynamically. This interaction layer has the potential to provide significant value, and there is likely to be considerable competition around it." Deloitte Tech Trends 2026 adds the design principle: "The competitive advantage lies with organizations that redesign end-to-end processes to enhance agent capabilities, not those that layer agents onto legacy workflows." Ops are designed to be exactly this kind of redesigned end-to-end primitive — and 74% of companies plan to deploy agentic AI within two years (Deloitte, 2026), giving the Op marketplace its initial demand curve.

| Characteristic | What It Means | Why It Matters |
| :---- | :---- | :---- |
| Versioned | Every Op has a version identifier and changelog | Reproducibility; safe rollout and rollback |
| Installable | Deployed via Nebi into any compliant Hub or Desktop/Web Application | Marketplace distribution at scale |
| Frame-oriented | Declares the Frames it requires or applies, and inherits those embedded in its Cogs | Same Op adapts to many organizations' contexts |
| Supervised | A coordinating model orchestrates Cog execution; humans approve and refine at defined checkpoints | Sophisticated workflows remain governable and auditable |
| Triggerable | Invoked as an icon, command, button, or scheduled job | Fits every human and automated invocation context |
| Self-contained | Includes all Cogs, supervising logic, integration specs, and Frame declarations | No environment-specific dependencies |
| Composable | Ops can invoke other Ops as sub-routines | Complex workflows from simple building blocks |

# **5\.  The Accountability Plane — Guards, Gates, and Tracks**

If Frames are how accountable humans inject context into AI work, Validation is how the results of that work are verified. Every AI-assisted workflow must answer two questions: *what context should guide this work*, and *how do we know the result can be trusted*? Frames answer the first question. Guards, Gates, and Tracks answer the second. Together they form the accountability plane of the architecture — not a fourth layer beside the other three, but a plane that cuts across all of them.

This layer is essential because AI systems do not merely produce documents or answers. They increasingly influence decisions, trigger workflows, update systems, summarize evidence, recommend actions, and coordinate work across people and software. Without validation, AI-generated work remains fragile and difficult to trust. With validation, it becomes operational intelligence. The distributed AI economy cannot scale on generation alone — in enterprise, government, healthcare, finance, and legal environments, AI output must be more than useful. It must be verifiable, governable, auditable, and accountable.

The validation gap is well documented. AI incident reports are rising sharply, yet standardized responsible-AI evaluations remain rare even among major model developers (Stanford HAI AI Index 2025). McKinsey’s analysis of the resulting "gen AI paradox" reaches the same conclusion from the enterprise side: nearly eight in ten companies have deployed generative AI, yet roughly the same share report no material impact on earnings, and fewer than 10 percent of use cases ever make it past the pilot stage. The remedy that analysis prescribes is precisely this layer — comprehensive evaluation of agent pipelines, embedded policy controls, ethical guardrails, and audit mechanisms (McKinsey, "Seizing the Agentic AI Advantage," June 2025).

Validation operates during both Frame construction, Cog development and Op execution. Frames can attach a validation code that must be run. Cogs are validated before they are deployed. Ops declare a validation strategy before they are run: the Guards they use, the Gates that determine whether work can proceed, and the Tracks they preserve for audit, learning, and accountability.

| The Accountability Plane at a Glance |
| :---- |
| **Guards** — reusable verification and protection components that check whether the output or action of a Cog or Op is correct, safe, policy-compliant, and ready for use. |
| **Gates** — decision points where the results of one or more Guards determine whether work proceeds, pauses, escalates to human or expert review, retries, or stops. |
| **Tracks** — durable evidence records of what happened: the Frames applied, Cogs invoked, Guards run, Gates passed or failed, humans who approved, sources consulted, and outputs produced. |
| "Frames guide the work. Cogs perform the work. Ops orchestrate the work. Guards verify the work. Gates decide whether the work proceeds. Tracks make the work accountable." |

## **5.1  Guards — Verification and Protection Components**

A **Guard** is a reusable verification and protection component that checks whether the output or action of a Cog or Op is correct, safe, policy-compliant, and ready for use.

Guards are broader than traditional software tests. Some Guards are deterministic and algorithmic. Some are probabilistic. Some compare the outputs of multiple independent Cogs. Some require human or expert review. Some run before work begins; others run while the work is in progress or after an Op completes. A Guard can check:

* whether the right Frames were applied;

* whether the output conforms to a required schema;

* whether the answer is grounded in approved sources;

* whether a proposed action violates policy;

* whether sensitive data is being exposed;

* whether independent Cogs disagree;

* whether confidence is too low for autonomous action;

* whether a human expert must review the output;

* whether the system is drifting from previously validated behavior.

Guards make validation explicit, reusable, composable, and shareable. Just as Frames can be authored and exchanged as context artifacts, Guards can be authored and shared as validation artifacts. Over time, open-source communities, enterprises, regulators, consultancies, and domain experts can publish Guard libraries for specific domains and risks — a **Schema Guard** that validates output structure, a **Source Guard** that checks claims against approved material, a **Policy Guard** that checks organizational and regulatory rules, a **Privacy Guard** that detects prohibited disclosure, a **Consensus Guard** that compares independent Cogs, a **Drift Guard** that detects degradation across versions and time, and an **Expert Guard** that routes sampled or high-risk outputs to human review.

The key principle is that Frames can declare associated Guards, but **every Op should declare its Guards**. Validation should not be an afterthought added by policy teams after deployment. It should be part of the Frame and Op design.

## **5.2  Gates — Decision Points for Approval, Escalation, and Control**

A **Gate** is a decision point in an Op where the results of one or more Guards determine what happens next. Guards check. Gates decide.

A Gate may allow the Op to continue, pause the workflow, request human approval, escalate to an expert, retry with a different Cog, run additional validation, or stop the Op entirely. For example:

* If a Source Guard finds unsupported claims, the Op pauses and requests revision.

* If a Confidence Guard reports low confidence, the Op routes the output to human review.

* If a Privacy Guard detects sensitive information, the Op stops before external transmission.

* If a Consensus Guard finds strong disagreement between Cogs, the Op escalates to an expert.

* If all required Guards pass, the Op proceeds to the next step.

Gates are especially important because not all validation failures are the same. Some failures require correction. Some require review. Some require escalation. Some require termination. Gates encode those operational decisions into the workflow itself. In the running Vendor Fraud Review example, a low extraction confidence or a high vendor-risk score is not a failure state — it is a Gate decision that routes the case to a human reviewer before any vendor is flagged.

This makes Ops safer and more accountable. A high-risk Op does not simply "run AI." It proceeds through defined Gates that reflect organizational policy, regulatory exposure, and the acceptable level of autonomy for that task.

Formal Gates are also what regulation now expects. The EU AI Act’s human-oversight requirements for high-risk systems — anticipated under the AI Omnibus political agreement for December 2027 (standalone high-risk systems) and August 2028 (AI embedded in regulated products) — mandate that a natural person can correctly interpret an output, decide not to use it, disregard, override, or reverse it, or intervene and stop the system (Regulation (EU) 2024/1689, Article 14). A Gate is the architectural point where those powers are actually exercised, and the Track is where their exercise is recorded.

## **5.3  Tracks — Durable Evidence Records**

A **Track** is the durable record of an Op or Cog execution. It captures what happened, what context was used, what Cogs were invoked, what Guards ran, which Gates were passed or failed, what sources were consulted, what humans approved, and what final outputs or actions were produced. Tracks are the evidence substrate of accountable AI. A Track may include:

* the Op that was run, the Cogs invoked, and the Frames applied;

* the input data and source references used;

* the model versions and configuration parameters;

* the Guards executed, their results, and confidence scores;

* the Gates passed, failed, or escalated;

* human approvals, edits, or overrides;

* final outputs or actions taken;

* timestamps, user identity, permissions, and system environment;

* links to related Organizational Memory entries.

Tracks serve several purposes:

* **Auditability** — an organization can reconstruct why a decision was made.

* **Governance** — compliance teams can verify that required procedures were followed.

* **Learning** — corrections and human reviews become signals for improving Frames, Cogs, Ops, and Guards.

* **Debugging** — developers can understand why an Op failed or behaved unexpectedly.

* **Trust** — users and customers can see that AI work was not merely generated, but validated.

The Track is not just a log file. It is a structured accountability artifact. It is how the Intelligence Hub remembers what happened and turns operational experience into organizational learning. Unlike Frames, Cogs, Ops, and Guards, Tracks are usually not exchanged; they are retained under the governance boundary of the Hub that produced them and only produced when required by audits or regulators.

Tracks are also a regulatory requirement in the making. The same EU AI Act requires high-risk AI systems to be technically capable of automatically recording events over their lifetime, and requires deployers to retain those logs (Regulation (EU) 2024/1689, Articles 12 and 19). Organizations that adopt Tracks as a first-class artifact satisfy such obligations by construction rather than by retrofit.

## **5.4  Validation Across the Op Lifecycle**

Validation occurs throughout the Op lifecycle, not only at the end. Each Op declares a validation strategy that matches its risk profile across four stages:

| Stage | Core Question | Example Guards and Gates |
| :---- | :---- | :---- |
| **Pre-flight** | Is this Op allowed and properly configured? | Permission checks, required Frame checks, data authorization checks, model availability checks |
| **In-flight** | Is the work staying within policy and expected bounds? | Tool-use checks, privacy checks, confidence checks, policy checks, intermediate human review Gates |
| **Post-run** | Is the output correct, useful, safe, and ready for action? | Source grounding, schema validation, expert sampling, consensus checks, final approval Gates |
| **Continuous** | Is quality improving, degrading, or drifting over time? | Regression tests, drift detection, benchmark suites, incident reviews, sampled expert audits |

![][image2]

*Figure 2 — Validation across the Op lifecycle: Guards check, Gates decide, Tracks record.*

A low-risk drafting Op may rely on simple format checks and user review. A high-risk fraud detection Op may require source grounding, multiple independent Cogs, expert sampling, and a complete Track retained for years. A clinical, legal, financial, or public-sector Op may require formal Gates before any recommendation can become an action.

This lifecycle model aligns with the structure of the NIST AI Risk Management Framework — govern, map, measure, and manage — and its Generative AI Profile, which many organizations already use to organize exactly these controls (NIST AI RMF 1.0, January 2023; NIST-AI-600-1, July 2024). Declaring Guards, Gates, and Tracks per Op is how that framework becomes executable rather than aspirational.

## **5.5  Seven Categories of Guards**

The following categories help structure the validation ecosystem. The strongest Guards are algorithmic, because they can directly verify correctness; the most business-meaningful are Outcome Guards, because they validate value rather than mere technical correctness. Most Ops will combine several categories.

| Category | What It Verifies | Example Checks |
| :---- | :---- | :---- |
| **Algorithmic** | Outputs against deterministic rules or known results | Generated code passes tests; SQL executes; invoice totals reconcile; JSON conforms to schema |
| **Source-Grounding** | Claims are supported by approved evidence | Factual claims link to authorized documents; cited passages actually support the conclusion; summaries do not contradict the evidence |
| **Consensus** | Agreement across independent Cogs, prompts, models, or execution paths | Three Cogs classify a document and two must agree; outlier extractions flagged; a verifier Cog reviews another Cog’s output |
| **Expert** | Human or known-expert judgment on sampled or high-risk outputs | Periodic expert sampling of 5% of outputs; mandatory review of high-risk classifications; approval before external communication |
| **Policy & Safety** | Work stays inside allowed boundaries | No external release of private data; no unapproved tools or sources; no action outside the user’s permissions; brand, legal, and ethical constraints respected |
| **Regression & Drift** | Updates have not changed behavior in unacceptable ways | Golden test sets after model updates; rising error rates detected; a new Frame that degrades performance is flagged |
| **Outcome** | The Op produces the intended business result | Fraud detection reduces false positives; onboarding time decreases; legal review catches more contract risks; cost falls without added risk |

Policy and Safety Guards connect directly to Frames, because many of the policies and constraints they enforce are encoded in Frames. Consensus and Expert Guards are most valuable when truth is uncertain, interpretive, or probabilistic. Regression and Drift Guards are what maintain trust over time as models, Frames, and Ops evolve.

## **5.6  The Validation Strategy: Part of Every Op’s Contract**

Every Op declares a **Validation Strategy**: which Guards are used, where Gates occur, what Tracks are retained, and when human review is required. A Validation Strategy answers questions such as:

* What must be checked before the Op runs, and which Frames, Cogs, tools, and data sources are authorized?

* What outputs require algorithmic validation, and what claims require source grounding?

* When is consensus among independent Cogs required?

* When is human or expert review required, and what risk thresholds trigger escalation?

* What evidence must be preserved in the Track, and how long must it be retained?

* How are failures, corrections, and overrides fed back into Organizational Memory?

Formal standards point in the same direction. ISO/IEC 42001 — the first international AI management-system standard — requires organizations to manage AI across its full lifecycle, subject it to independent audit, and continually improve it (ISO/IEC 42001:2023). A declared Validation Strategy is how an Op makes those management-system obligations concrete and machine-checkable.

This makes validation part of the Op’s contract. **An Op is not complete unless it declares how its work will be verified.** The running Vendor Fraud Review example makes this concrete as a validation-aware Op manifest:

**The Running Example as a Validation-Aware Op Manifest (Sketch)**

op:  
  name: vendor-fraud-review  
  frames:  
    \- company-policy  
    \- procurement-rules  
    \- fraud-detection-methodology  
  cogs:  
    \- invoice-extraction-cog  
    \- vendor-risk-cog  
    \- anomaly-summary-cog  
  guards:  
    preflight:  
      \- required-frame-guard  
      \- permission-guard  
      \- data-source-authorization-guard  
    in\_flight:  
      \- tool-use-policy-guard  
      \- sensitive-data-guard  
      \- confidence-guard  
    post\_run:  
      \- schema-guard  
      \- source-grounding-guard  
      \- consensus-guard  
      \- expert-sampling-guard  
  gates:  
    \- if: confidence \< 0.80  
      then: human\_review\_required  
    \- if: consensus\_disagreement \> 0.25  
      then: expert\_review\_required  
    \- if: sensitive\_data\_detected  
      then: stop\_and\_escalate  
    \- if: vendor\_risk \== high  
      then: human\_approval\_required  
  track:  
    retain\_for: 7\_years  
    include:  
      \- frames\_used  
      \- cogs\_invoked  
      \- source\_documents  
      \- guard\_results  
      \- gate\_decisions  
      \- human\_approvals  
      \- final\_output

## **5.7  How Validation Completes the Architecture**

Validation does not sit outside the Intelligence Hub architecture. It completes it.

**Frames and Guards.** Frames define the context, rules, goals, terminology, norms, and constraints that should guide the work. Guards verify that the work remained faithful to those Frames. A Healthcare Compliance Frame may define rules about patient data; a Privacy Guard checks whether those rules were followed during an Op.

**Cogs and Guards.** Cogs perform discrete AI work; Guards check whether that work is reliable, safe, and acceptable. Some Guards may themselves be implemented as Cogs, especially when validation requires interpretation rather than deterministic checking. A Contract Review Cog may produce a risk summary; a Source Guard checks whether the summary is grounded in the contract text, and a Legal Expert Guard samples high-risk outputs for review.

**Ops and Gates.** Ops orchestrate Cogs to produce business outcomes; Gates define the points where validation results determine whether the Op proceeds, pauses, escalates, or stops. An Op that drafts a customer communication may proceed automatically when all Guards pass, but route to human review when brand or regulatory risk is detected.

**Tracks and Organizational Memory.** Tracks preserve the execution record of validated work. Over time, Tracks become part of the Organizational Memory described in Section 3.4. They show what happened, which decisions were made, what worked, what failed, and how humans corrected or approved AI-generated work. This creates a learning loop:

| The Accountability Loop |
| :---- |
| 1\.  Frames orient work.    2\.  Cogs perform work.    3\.  Ops orchestrate work. |
| 4\.  Guards validate work.    5\.  Gates control action.    6\.  Tracks preserve evidence. |
| 7\.  Organizational Memory learns from the results.    8\.  Frames, Cogs, Ops, and Guards improve. |

## **5.8  Validation as an Open-Source Opportunity**

Validation is one of the best opportunities for open-source contribution inside the Intelligence Hub ecosystem. Open-source communities can create Guard libraries, benchmark suites, prompt-injection test harnesses, source-grounding validators, schema and format Guards, domain-specific compliance Guards, red-team datasets, expert sampling frameworks, drift monitoring tools, Track schemas, evidence-record viewers, and audit and governance dashboards. The need is concrete: prompt injection now tops the OWASP Top 10 security risks for large-language-model applications, and community-built test harnesses and Guards are the natural response (OWASP Top 10 for LLM Applications, November 2024).

This is strategically important because trust cannot be built by OpenTeams alone. Trust compounds when the ecosystem can inspect, improve, and share the validation tools themselves. **Open Guards can become to accountable AI what open test frameworks became to software quality.**

# **6\.  Layer 3: The Marketplace — Frames, Cogs, Ops, Guards, and more.**

## **6.1  Four Classes of Exchanged Artifact**

The marketplace is built around four classes of exchanged artifact, each with its own dynamics:

* Ops — orchestrated, supervised AI workflows that deliver outcomes with defined accountability.  Typically these will be collected into service as software subject to subscription, usage, or outcome-based commercial arrangements.

* Cogs — AI workers that can be specialized to specific subject areas of work and therefore be deployed more easily at scale to the tasks at hand.  These can be rented, purchased, given away, or provided under usage or subscription arrangements.

* Frames — scoped artifacts that carry organizational context. The vast majority of Frames will be shared freely within the organization and between the organizations that need them. A smaller number might be offered commercially as expertise to deploy under a licensed arrangement. 

* Guards — reusable validation components that verify and protect AI work. Many will be published openly by communities and domain experts; specialized commercial Guard libraries can encode regulated-industry expertise — a healthcare community’s HIPAA Privacy Guard, a financial-services consortium’s KYC Source Guard, a legal technology group’s Contract Citation Guard, an open-source community’s Prompt Injection Guard.

This is a key architectural decision of the OpenTeams vision. Rather than building the ecosystem and marketplace around a single class of artifact — say, just Ops, or just models — OpenTeams builds the marketplace around multiple classes – initially these four classes that actually constitute an accountable AI economy: the work, the workers, the context that orients them, and the validation that makes them trustworthy. Each class has its own publishers, its own audience, and its own dynamics.

The Frame side of the economy is primarily about coordination and shared abstraction, not transaction. Communities of practice publish Frames so members can align on terminology and methods. Industry consortia publish Frames that encode best practices. Open-source ecosystems publish Frames that make it easy to adopt their tools and conventions. Within organizations, departments and teams publish Frames so that work flows consistently across people, partners, and AI systems. The marketplace is where this sharing happens at scale — most of it free, some of it commercial, all of it organized around the open Frame protocol.

The Guard side of the economy reinforces trust across the other three classes: an Op that ships with well-known, community-vetted Guards is easier to adopt than one that asks to be taken on faith. Tracks, by contrast, will rarely be exchanged. They contain sensitive operational evidence and should stay governed inside the Intelligence Hub that produced them, while anonymized or aggregated Track data can inform quality rankings, benchmark results, and marketplace trust signals.

| Artifact | Role | Exchanged? |
| :---- | :---- | :---- |
| **Frames** | Carry organizational context | Yes — mostly shared freely; some commercial |
| **Cogs** | Perform governed AI work | Yes — rented, purchased, or subscribed |
| **Ops** | Orchestrate outcomes | Yes — service-as-software arrangements |
| **Guards** | Verify and protect the work | Yes — open-source and commercial libraries |
| **Tracks** | Preserve execution evidence | No — retained under Hub governance |

The broader industry trajectory validates the Op-as-marketplace-primitive model. Gartner (cited in Deloitte TMT Predictions 2026\) projects that by 2030, at least 40% of enterprise SaaS spend will shift toward usage-, agent-, or outcome-based pricing. AlixPartners' 2026 Enterprise Software Predictions adds that "established software companies must now consider dismantling the pricing models their businesses were built to deliver." Ops are designed from the start for this pricing model — discrete, supervised, outcome-aligned units of AI work rather than seat-based access to undifferentiated capability.

## **6.2  The Network Flywheel**

The Intelligence Hub and Frame / Cog / Op / Guard architecture creates a compounding platform flywheel:

| The Growth Engine |
| :---- |
| 1\.  More Intelligence Hubs deployed create a larger addressable market for Frame, Cog, Op, and Guard publishers. |
| 2\.  More Frames, Cogs, Ops, and Guards available make each new Hub deployment more valuable. |
| 3\.  More Hub deployments generate more data on what works, raising artifact quality across the ecosystem. |
| 4\.  Better artifacts strengthen the marketplace, which drives more Hub deployments. |
| Each cycle deepens the moat. The flywheel is self-reinforcing. |

This is the economic architecture that differentiates OpenTeams from pure infrastructure providers (who capture only deployment value) and from pure marketplace platforms (who have no infrastructure contribution). The combination of open-source trust (Nebari, Nebi, and the standards around them), portable Frames as containers for organizational context, governed Cogs, installable Ops, reusable Guards, and retained Tracks creates a platform that is difficult to replicate and more valuable with every participant that engages.

The structural forces behind sovereign AI are larger than any single company's strategy. The Financial Times (March 14, 2026\) noted that "deglobalisation — which is in effect what this is, however rational — is expensive for individual countries, but a windfall for their suppliers." Nvidia's revenue from sovereign customers reached $30 billion in fiscal 2025, 14% of its total. Stanford HAI's AI Index 2026 documents $581.7 billion in global corporate AI investment in 2025 — a 130% year-over-year increase. The capital that will fund this flywheel is already in motion. The architectural question is which platform captures the compounding value as the spending shifts toward sovereign deployments.

## **6.3  Who Participates**

| Participant | Role in the Ecosystem | Value Received |
| :---- | :---- | :---- |
| Enterprises | Deploy Intelligence Hubs; author Frames; install Ops, Cogs, and external Frames | Owned AI capabilities; preserved organizational context; compliance; reduced integration cost |
| AI Developers | Build and publish Ops and Cogs | Revenue; distribution; market access |
| Domain Experts | Author Frames that capture expertise; configure Cogs; define workflow logic for Ops | Influence and recognition through widely-adopted Frames; community contribution; optional commercial offerings |
| Communities & Consortia | Publish open Frames that codify shared methodologies, vocabularies, and standards for their domain | Member alignment; ecosystem cohesion; influence on industry direction |
| Consultancies & Agencies | Publish methodology Frames — most as open community contributions, some as commercial offerings | Brand recognition; client adoption of shared methods; optional revenue from commercial Frames |
| System Integrators | Deploy and customize Hubs; build bespoke Ops and Frames | Services revenue; recurring relationships |
| Open-Source Contributors | Extend Nebari, Nebi, and the Frame protocol as well as Cog and Op standards stored in Nebari. | Reputation; ecosystem participation; influence over the standard |
| Guard Publishers & Validation Experts | Author and maintain Guards; define Gate policies and benchmark suites; audit Tracks and validation practice | Revenue and recognition; influence over validation standards; trust across the ecosystem |
| Regulators & Standards Bodies | Publish rules, schemas, test profiles, or reference Guards that codify regulatory expectations | Higher, measurable compliance; visibility into how rules are applied in practice |

# **7\.  The Human Gateway: The Intelligence Hub Desktop/Web Application**

## **7.1  Why a Desktop/Web Application Is Not Optional**

The three-layer architecture described above is technically coherent and economically sound. But architecture alone does not create adoption. The critical product that makes the Intelligence Hub tangible, accessible, and compelling to the people who must use it every day is a Desktop/Web Application (with web access where appropriate).

This is not a "nice-to-have" product enhancement. The Desktop/Web Application is the primary interface through which the entire system becomes real for end users. Without it, Intelligence Hubs are server-side configurations that require engineering expertise to operate. With it, any knowledge worker in an organization can combine the Frames that orient their work, converse with AI Cogs that already understand their context, run pre-configured Ops to automate their processes, and share organizational context with internal teammates and external partners.

## **7.2  The Target User: Knowledge Workers**

The Desktop/Web Application is designed for the people who do the daily operational work of modern organizations — sales, marketing, project success, accounting, legal, HR, IT, and the other back-office and shared-service functions that keep enterprises running. These users:

* Operate inside well-defined organizational contexts — their function, their team, their accounts, their projects

* Apply organizational norms, terminology, and policies to every task they touch

* Need AI augmentation that respects those contexts — not generic AI that has to be re-oriented at the start of every interaction

* Routinely share context across organizational boundaries — with partners, vendors, customers, and external collaborators

* Are not engineers and cannot be expected to configure, manage, update, or operate Hubs, Ops, or Cogs at the configuration layer

For these users, the Desktop/Web Application provides a unified surface where Frames, Cogs, and Ops come together to enable specialized work — without requiring the user to understand the architecture beneath them.

## **7.3  Memory in the Desktop/Web Application: Local Context and Organizational Awareness**

At the heart of the Desktop/Web Application is a personal local memory that absorbs the user's active Frames. When a user joins an organization, they inherit the Company Frame. When they join a department, the Department Frame layers on top. When they join a project, the Project Frame composes further. The user can install additional Frames from the marketplace (a regulatory Frame for their industry, a brand voice Frame from a partner agency), and they can author personal Frames for the way they themselves prefer to work.

This combination — the user's personal, inherited, installed, and authored Frames — is held in the Desktop/Web Application's local memory and becomes the contextual substrate that orients every AI interaction. A conversation with a Cog automatically inherits this context. An Op launched from the application runs against this context. The user does not need to re-explain who they are, who their company is, or how their team works. The context is already there.

Beyond the user's own Frames and personal interactions, the Desktop/Web Application opens a permissioned window into the broader Organizational Memory described in Section 3.4. Each user sees a scoped slice of the Hub's accumulated context — the past Cog conversations they have had, the Op executions they have run, the relevant interactions of their team or department where access is granted, and the documents, knowledge-base entries, and structured records their role authorizes them to retrieve. This means the Desktop/Web Application is not just a personal workspace; it is the user's access point to what the organization has already learned through prior AI work that touches their domain.

The boundary between Local Memory (private to the user) and Organizational Memory (shared, governed by the Hub) is policy-controlled. A user working on a sales account might see their own past conversations, their team's account history, and broader organizational context about that customer — but not material from accounts they do not own. A clinician might see protocols and prior patient summaries within their assigned care team, but not records outside it. The Hub's access controls, retention policies, anonymization rules, and audit trails apply uniformly whether the user is querying their own memory or drawing on the organization's.

This dual pattern — personal Local Memory plus a permissioned view of Organizational Memory — is what lets a single conversation with a Cog carry both who the user is (their Frames, their preferences, their history) and what the organization knows (the accumulated context their role can reach). The user does not have to choose between personal productivity and organizational learning. The Desktop/Web Application provides both, simultaneously.

Local memory remains private to the user by default. Frames can be promoted from Local Memory back to the Hub, shared with teammates, or selectively shared with external partners — but the user controls that boundary. Access to Organizational Memory, conversely, is governed by Hub-level policy: the user does not grant or revoke their own access, but their reach into the shared memory is fully visible, auditable, and reversible by the Hub's administrators.

## **7.4  The Three Modes of AI Engagement**

Through the Desktop/Web Application, users can engage with AI in three complementary modes:

### **Mode 1 — Applications (Ops)**

A dedicated tab presents pre-configured Ops as visual icons, like an application launcher. Users click an Op icon to run an automated process: generate a quarterly board report, draft a customer onboarding plan, reconcile expense reports, run a quarterly compliance review, or launch the Vendor Fraud Review from the running example. Ops are the "buttons that do the job" — discrete, repeatable units of organizational work, each optionally picking up the user's active Frames or configured to only use the pre-loaded Frames.

### **Mode 2 — Conversations (Cogs)**

A chat surface where users have natural-language conversations with Cogs that have been oriented by their currently-active Frames. This is the iterative workspace: ask a question, get domain-aware help, draft a document, debug a problem, brainstorm an approach. Because the Cog inherits the user's combined Frame context, the conversation already knows the company's brand voice, the department's terminology, the project's goals, the appropriate tools that ensure the outputs are preserved.  This is done without the user having to set the stage.

### **Mode 3 — Cog Library**

Users can also load specific Cogs directly for specialized tasks — running a Cog as a standalone tool when they need its specific capability without the conversational layer. This is useful for analysis, validation, debugging, one-off specialized work, and exploring what Cogs exist in the Hub or the marketplace.

## **7.5  Frame Management: Composition and Sharing**

The Desktop/Web Application's most distinctive capability is Frame management. Users can:

* Install Frames from the marketplace, their organization's internal Frame library, or external partners who have shared them

* Combine multiple Frames for a given work session, such as company \+ department \+ project \+ ad-hoc context layered together, with the application managing the inheritance graph

* Author new Frames or extend existing ones, capturing the context they want to make repeatable

* Share Frames internally with colleagues, or externally with partners, vendors, and customers using selective field-level controls so internal-only sections stay internal

* Provide feedback on Frames in the form of both scores on particular concepts in the Frame with a 6 point scale (-10, \-1, \-0, \+0, \+1, \+10) or via suggested changes to the Frame that are sent back to the accountable author for review.

* Publish Frames back to the organization's library, a community board, a particular user, the open marketplace, or both

This makes the Desktop/Web Application both a  productivity surface and a context exchange.  It is the place where organizational alignment is made portable. A sales representative can share a Sales Methodology Frame with a partner to align them on terminology and stages. A marketing director can publish a Brand Voice Frame to every external agency that the company works with. A legal team can issue a Vendor Compliance Frame that every supplier's AI tooling automatically respects.

## **7.6  Intelligence Hub Health and Governance**

For users with administrative privileges, the Desktop/Web Application is also the operational dashboard for the Intelligence Hub itself:

* Real-time view of Hub resource utilization and model serving status

* Audit log browser: full history of AI actions, human interventions, Frame applications, and data accesses

* Policy management: define and update governance rules that apply across all Frames, Ops, and Cogs

* User and role management: control who can install Frames, configure Cogs, run Ops, and review outputs

## **7.7  Making Validation Visible: Guards, Gates, and Tracks in the User Experience**

The Desktop/Web Application is also where validation becomes visible to the people who rely on it — without overwhelming them. Knowledge workers should not need to understand Guard configuration to benefit from it. The application surfaces validation naturally:

* **Guard status** — show which Guards passed, failed, or require review for any Op run or Cog output

* **Gate prompts** — request human approval directly in the workflow when a Gate requires a decision

* **Track view** — let authorized users inspect the execution record behind any result

* **Confidence and risk indicators** — summarize at a glance whether output is safe to use

* **Correction workflow** — let users correct AI output and feed that correction into Organizational Memory

* **Validation badges** — indicate that an Op, Cog, Frame, or Guard has passed a defined validation standard

For ordinary users, the language stays simple: "This Op passed all required Guards." "This result needs expert review." "A Track has been saved for audit." For administrators and compliance teams, the same surface exposes deeper views — Guard configuration, Gate thresholds, Track retention policies, sampling rates, drift reports, and validation failure trends — extending the governance dashboard described in Section 7.6.

The cost of skipping this is now quantified. Gartner predicts that by 2027, 40% of enterprises will demote or decommission autonomous AI agents due to governance gaps identified only after production incidents occur (Gartner, May 2026). The implication is direct: agentic systems need Guards, approval Gates, audit Tracks, and incident-response mechanisms before they scale — not after.

## **7.8  The Desktop/Web Application as a Market Development Tool**

Beyond its operational value, the Desktop/Web Application plays a crucial strategic role in market development. The adoption of a new infrastructure standard — whether Linux, Python, or Kubernetes — always depends on a compelling end-user experience. The Desktop/Web Application is that experience for the Intelligence Hub ecosystem.

* Lowers the barrier to Hub deployment by making configuration visual and guided rather than requiring deep engineering expertise

* Accelerates Frame, Cog, Op, and Guard adoption by making discovery intuitive — users browse the marketplace the way they browse an app store

* Creates a feedback loop: usage data from the Desktop/Web Application informs Frame and Op quality rankings, surfaces unmet needs, and guides developer investment

* Enables the Applied AI Society and credentialing programs to use the Desktop/Web Application as a hands-on training environment

* Demonstrates the platform's value proposition in enterprise sales contexts — nothing closes a deal faster than a working demo of a knowledge worker doing their job, with AI, under the right Frames

## **7.9  Technical Architecture**

The Desktop/Web Application is built as a cross-platform native application (macOS, Windows, Linux), with web access where appropriate, connecting to the user's Intelligence Hub via local or network API. Key architectural characteristics:

* Local-first: the application can operate with full functionality against a local Hub even when a remote Hub and/or marketplace is not reachable

* Hub-agnostic: the same application works against any standards-compliant Intelligence Hub, regardless of where it is deployed

* Nebi-integrated: Frame, Cog, Op, and Guard installation and lifecycle management are handled natively through the Nebi client

* Marketplace-connected: browsing and discovery connect to the OpenTeams marketplace API when network access is available

* Local-memory-backed: the user's combined Frame context is held locally for privacy, performance, and offline operation

* **Validation-aware**: Guard status, Gate decisions, and Track views are surfaced natively in the user experience

* Extensible: a plugin architecture allows Op developers to provide custom configuration UIs for their Cogs, surfaced natively within the Desktop/Web Application

# **8\.  Ecosystem Strategy: Nebari, Nebi, and the Startup Ecosystem**

## **8.1  Open Source as the Trust Foundation**

The Intelligence Hub marketplace only works if participants trust that an Op installed in one Hub will behave the same way in another, that a Frame inherited by one Cog will be interpreted the same way by another, and that the protocols on which all of this depends are stable and open. That trust is grounded in open source including Nebari. Because Nebari is open-source, its specification is publicly auditable including the definitions and patterns exposed as Frame, Cogs, and Ops.  While Nebari is initially company-backed so that it can be nurtured and improved with a focused approach, it has already started to establish itself as a community-governed standard so that multiple stakeholders can contribute to its development. This is the same dynamic that helped make Python the default language of modern AI development.  The openness amplifies the trust that proprietary alternatives can struggle to provide.

Nebari's open-source nature also creates an important flywheel for the marketplace itself. As more organizations deploy Intelligence Hubs using components of Nebari, the standard becomes more deeply entrenched. Frame, Cog, Op, and Guard publishers gain access to every Hub in the network. The standard's adoption is self-reinforcing, and OpenTeams — as the primary steward and commercial entity behind Nebari — captures some of the value of those network effects through enterprise services, marketplace fees, and direct ecosystem participation with our own Cogs and Ops.

## **8.2  Nebi as the Distribution Mechanism**

Nebi is what turns the marketplace from a concept into a mechanism. It answers the question: "How does a Frame, Cog, Op, or Guard actually get distributed?” The answer is Nebi, an environment management tool that handles the full lifecycle from specification to deployment to update to removal.

Nebi's importance in the OpenTeams economy is analogous to pip's importance in the Python ecosystem or npm's importance in the JavaScript ecosystem. It is the distribution plumbing that developers, organizations, and end users can rely on, freeing them to focus on authoring and using Frames, Cogs, Ops, and Guards rather than on the mechanics of deployment.

Nebi also plays a trust role. When a Frame, Cog, Op, or Guard is installed via Nebi, the environment ensures that all dependencies are resolved and pinned, and the installation is logged. Every deployment is fully auditable — an important guarantee for regulated industries.

## **8.3  The Startup Ecosystem**

One of the most significant long-term opportunities in this architecture is the startup ecosystem that the Intelligence Hub movement engenders.  Just as Kubernetes created a generation of cloud-native startups that built on top of the container orchestration standard, Nebari and Nebi create the foundation for a generation of deeply specialized, domain-expert-filled AI businesses that use Intelligence Hubs, publish vertical Ops, Cogs, and Guards, and — uniquely — publish Frames that monetize accumulated organizational and industry knowledge.

A domain expert in healthcare informatics can deploy their specific Nebari Hub, build Ops and Cogs specialized to clinical workflows, and publish a HIPAA Compliance Frame that any healthcare organization can adopt. Most of these Frames will be shared openly to align an industry around best practices; a smaller number may be offered commercially. A consultancy can publish its methodology as a Frame — earning influence and brand recognition through adoption, with optional commercial variants. A law firm can publish a Contract Review Frame that codifies its expertise in a form clients and partners can adopt. The same pattern applies across energy, agriculture, legal, financial services, government, and beyond.

This vertical specialization — enabled by the open standard and the four-class marketplace — is what ultimately drives the platform to scale. OpenTeams does not need to build every vertical Frame, Cog, Op, or Guard. It needs to build the infrastructure and marketplace that makes it economically attractive for domain experts to build them themselves.

McKinsey quantifies the opportunity directly: "Use cases in the public sector and regulated industries could drive up to 40 percent of AI workloads to sovereign environments" (December 2025). For domain-expert startups, this is the addressable market — concentrated in exactly the verticals where Frame-based context capture and Op-based execution governance create the most value. Hugging Face's Spring 2026 State of Open Source notes that "for researchers, developers, companies, and governments, open source remains a foundational layer for building, evaluating, and governing AI systems" — meaning the Nebari foundation is also the foundation on which the vertical-specialist ecosystem can build without lock-in friction.

# **9\.  Competitive Positioning**

The combination of Nebari, Intelligence Hubs, Frames, Cogs, Ops, the Guards, Gates, and Tracks of the accountability plane, and the Desktop/Web Application creates a competitive position that is difficult to replicate from any single direction:

| Competitor Type | What They Offer | What They Lack |
| :---- | :---- | :---- |
| Foundation Model Providers (OpenAI, Anthropic, Google) | Powerful models via API | Infrastructure standard; execution layer; portable context (Frames); marketplace; sovereignty |
| Cloud AI Platforms (AWS SageMaker, Azure ML) | Managed model deployment | Open standard; Frame-based context portability; Op/Cog ecosystem; marketplace; desktop experience |
| Agent Frameworks (LangChain, AutoGen) | Agent orchestration libraries | Infrastructure; governance; installable packages; enterprise trust; context-sharing protocol |
| Enterprise Software Vendors (Salesforce, ServiceNow) | Vertical AI features | Open standard; extensibility; cross-domain Frame/Op marketplace; sovereign deployment |
| OpenTeams \+ Nebari | All three layers plus the validation that spans them: infra \+ execution (Frames, Cogs, Ops) \+ validation (Guards, Gates, Tracks) \+ economy | — |

The most defensible moat in this architecture is the compounding of four reinforcing advantages: open-source trust (Nebari and Nebi), portable organizational context (Frames), accountable execution (Guards, Gates, and Tracks), and marketplace network effects (the four-class economy). Each reinforces the others. Trust drives Hub adoption. Hub adoption drives Frame, Cog, Op, and Guard publication. The Frame catalog locks in cultural alignment that is hard to replicate elsewhere. The combined catalog drives marketplace value. Marketplace value drives more Hub deployments. Validated Ops accumulate Tracks, and Tracks compound into demonstrable trust that no competitor can copy. This is a flywheel that compounds over time and becomes increasingly difficult to displace.

The competitive position is sharpened by the scale of the enterprise readiness gap. PwC finds that 88% of global CEOs are not achieving meaningful AI returns. Deloitte finds only 1% of organizations describe themselves as AI-mature. McKinsey finds only 13% of enterprises with sovereign AI on their roadmap are on track to execute. No foundation model provider, cloud platform, agent framework, or enterprise SaaS vendor offers the combination of open standard, execution layer with portable context, and marketplace economy that closes this gap. The category is open precisely because no incumbent is structurally configured to fill it.

# **10\.  Strategic Roadmap**

The timing is driven by structural forces beyond OpenTeams' control. The EU AI Act is already phasing in, with governance, transparency, and enforcement obligations arriving before many high-risk obligations fully apply; the AI Omnibus political agreement points to a revised implementation timeline for many high-risk obligations — December 2027 for many standalone high-risk systems and August 2028 for high-risk systems embedded in regulated products — with fines reaching €35 million or 7% of global turnover per violation (Regulation 2024/1689). This strengthens the case for building validation, logging, human oversight, and auditability into AI infrastructure now rather than retrofitting them later. In the United States, over 1,100 AI-related bills were introduced across 45 states in 2025 alone, creating a fragmented but rapidly activating compliance surface. McKinsey notes that "sovereign cloud and AI migrations typically take three to four years — driven not by technology limitations but by the organizational work required to move regulated workloads" (March 2026). Organizations that begin now will have working infrastructure during the regulatory window; those that wait will be assembling under pressure.

| Phase | Focus | Key Milestones |
| :---- | :---- | :---- |
| Phase 1 (Now – 6 months) | Infrastructure \+ Execution foundation | Hub deployment hardened; Nebi packaging standard defined; Frame protocol published; first Ops, Cogs, Frames, and Guards built; Desktop/Web Application released |
| Phase 2 (6 – 18 months) | Marketplace emergence | Public marketplace live for Frames, Cogs, Ops, and Guards; 50+ Ops and 100+ Frames available; Desktop/Web Application general availability; first vertical ecosystems (health, energy, legal); initial open-source Guard libraries published |
| Phase 3(18 – 36 months) | Network effects \+ ecosystem | 1,000+ deployed Hubs; 500+ Ops and 2,000+ Frames; consultancies, communities of practice, and domain experts actively publishing Frames and Guards for shared alignment; Applied AI Society credentialing; international Hub networks |

# **11\.  Conclusion: The Infrastructure for the Intelligence Economy**

The Intelligence Economy is not a metaphor. It is the inevitable next stage of enterprise computing: a world in which AI capabilities are owned, deployed, exchanged, and governed as core operational infrastructure — and in which the organizational context that makes AI valuable is itself a first-class artifact that can be authored, inherited, shared, and exchanged.

OpenTeams, built with and for open source, is building the infrastructure for this economy. Nebari forms a foundation of open-source capability that may be deployed into private infrastructure or used as a reference architecture to adapt the tools already installed so that the company retains ownership of their future. The Intelligence Hubs are the organizational loci of owned and accountable AI conceptually stitching together an AI-native organization.  Frames are the portable context slices that provide the rules, terminology, goals, style, and norms that make AI work specialized rather than generic. Cogs are the specialized and governed AI workers that provide the AI capability integrating context and model. Ops are the installable, exchangeable units of AI-driven work that combine Cogs and Frames into business outcomes, protected by Guards, Gates, and Tracks. Nebi is the distribution mechanism that makes all of these technically possible to exchange easily and generally without reliance on a single company.  And the Desktop/Web Application is the product that OpenTeams develops to make everything accessible to everyday knowledge workers who must ultimately use and trust it — sales, marketing, project success, accounting, legal, HR, IT, and the rest of the operational backbone of every modern organization are the first customers.

Accountable AI requires more than context and automation. It requires validation. Frames give AI work the right context. Cogs perform specialized tasks. Ops orchestrate those tasks into outcomes. **Guards** verify that the work is correct, safe, and policy-compliant. **Gates** are formal steps in the process that determine when human approval or expert review is required. **Tracks** preserve the evidence of what happened. Together, these concepts turn AI from a generator of plausible output into a system of accountable operational intelligence.

This is not a vision built on hope. It is built on the same pattern that Travis Oliphant and his team have executed before: create the open standards, drive adoption through trust and ecosystem participation, and capture some of the commercial value of the network that forms around it while encouraging massive commercial value to accrue to others around the same standards. SciPy standardized computational science, NumPy standardized arrays. Anaconda standardized distribution of the Python data science stack. Nebari is helping standardize reproducible AI infrastructure, Nebi makes all artifacts easily distributable, and the Frame, Cog, Op, and Guard marketplace is the economy that forms on top.

| The Opportunity in One Sentence |
| :---- |
| OpenTeams is building the Linux \+ App Store for accountable enterprise AI — |
| where Intelligence Hubs are the owned enterprise deployments, |
| Nebari anchors the open-source infrastructure ecosystem OpenTeams assembles into each Hub, |
| Nebi makes every artifact reproducible and distributable, |
| Frames carry the shared culture and context, Cogs perform the work, |
| Ops orchestrate the outcomes they deliver together, |
| Guards and Gates verify and control the work, Tracks preserve the evidence, |
| and the Desktop/Web Application makes it all usable by the human at work. |

OpenTeams  |  nebari.dev  |  Confidential — July 2026  |  Revision 8

# **Sources**

Statistical claims and direct quotations throughout this whitepaper are drawn from the following publicly available reports, surveys, and analyses. Citations are listed by publisher and date with stable links. Entries whose precise publication could not be independently re-verified at the time of writing are marked.

1\.  McKinsey & Company. "The Sovereign AI Agenda: Moving from Ambition to Reality." December 18, 2025\. [https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/tech-forward/the-sovereign-ai-agenda-moving-from-ambition-to-reality](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/tech-forward/the-sovereign-ai-agenda-moving-from-ambition-to-reality)

2\.  McKinsey & Company. "Sovereign AI: Building Ecosystems for Strategic Resilience and Impact." March 2026\. [https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/sovereign-ai-building-ecosystems-for-strategic-resilience-and-impact](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/sovereign-ai-building-ecosystems-for-strategic-resilience-and-impact)

3\.  PwC. "29th Global CEO Survey: Leading Through Uncertainty in the Age of AI." January 2026 (n=4,454 CEOs, 95 countries). [https://www.pwc.com/gx/en/issues/c-suite-insights/ceo-survey.html](https://www.pwc.com/gx/en/issues/c-suite-insights/ceo-survey.html)

4\.  Deloitte. "TMT Predictions 2026: The AI Gap Narrows but Persists." November 2025\. [https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions.html](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions.html)

5\.  Deloitte. "The State of AI in the Enterprise 2026." 2026 (n=3,235 senior leaders). [https://www.deloitte.com/global/en/issues/generative-ai/state-of-ai-in-enterprise.html](https://www.deloitte.com/global/en/issues/generative-ai/state-of-ai-in-enterprise.html)

6\.  Deloitte. "Tech Trends 2026." December 2025\. [https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends.html](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends.html)

7\.  PwC. "2026 Digital Trends in Operations Survey." February 2026 (n=767 operations executives). [https://www.pwc.com/us/en/services/consulting/business-transformation/library/digital-trends-operations-survey.html](https://www.pwc.com/us/en/services/consulting/business-transformation/library/digital-trends-operations-survey.html) \[Attribution corrected from Deloitte in earlier revisions.\]

8\.  Stanford HAI. "AI Index Report 2025." April 2025\. [https://hai.stanford.edu/ai-index/2025-ai-index-report](https://hai.stanford.edu/ai-index/2025-ai-index-report)

9\.  Stanford HAI. "AI Index Report 2026." April 2026\. [https://hai.stanford.edu/ai-index/2026-ai-index-report](https://hai.stanford.edu/ai-index/2026-ai-index-report)

10\.  Brookings Institution. "Is AI Sovereignty Possible? Balancing Autonomy and Interdependence." February 2026\. [https://www.brookings.edu/articles/is-ai-sovereignty-possible-balancing-autonomy-and-interdependence/](https://www.brookings.edu/articles/is-ai-sovereignty-possible-balancing-autonomy-and-interdependence/)

11\.  OpenLogic by Perforce, with the Open Source Initiative. "2026 State of Open Source Report." 2026 (n=700+ practitioners). [https://www.perforce.com/resources/opl/2026-state-of-open-source-report](https://www.perforce.com/resources/opl/2026-state-of-open-source-report)

12\.  Financial Times. "Sovereign AI Is a Bet on the Economies of Anti-Scale." March 14, 2026\. Republished by the AI Commission: [https://aicommission.org/2026/03/sovereign-ai-is-a-bet-on-the-economies-of-anti-scale/](https://aicommission.org/2026/03/sovereign-ai-is-a-bet-on-the-economies-of-anti-scale/)

13\.  World Economic Forum, Davos 2026\. Remarks by Satya Nadella (Microsoft). Coverage: The Register, "Microsoft CEO: AI Sovereignty Isn’t Where It Runs, It’s Who Controls It," January 21, 2026\. [https://www.theregister.com/2026/01/21/nadella\_ai\_sovereignty\_wef/](https://www.theregister.com/2026/01/21/nadella_ai_sovereignty_wef/)

14\.  Hugging Face. "State of Open Source on Hugging Face: Spring 2026." March 2026\. [https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)

15\.  NBER (Brynjolfsson, Li, and Raymond). "Generative AI at Work." Working Paper 31161\. [https://www.nber.org/papers/w31161](https://www.nber.org/papers/w31161)

16\.  NBER (Baslandze et al.). "Artificial Intelligence, Productivity, and the Workforce: Evidence from Corporate Executives." Working Paper 34984, March 2026 (n=750 executives). [https://www.nber.org/papers/w34984](https://www.nber.org/papers/w34984)

17\.  PEX Network. "PEX Report 2025/26: Global State of Process Excellence." 2025/26. [https://www.processexcellencenetwork.com/business-transformation/reports/pex-report-global-state-process-excellence](https://www.processexcellencenetwork.com/business-transformation/reports/pex-report-global-state-process-excellence)

18\.  Dataversity. "AI Governance in 2026: Is Your Organization Ready?" February 2026\. [https://www.dataversity.net/articles/ai-governance-in-2026-is-your-organization-ready/](https://www.dataversity.net/articles/ai-governance-in-2026-is-your-organization-ready/)

19\.  AlixPartners. "2026 Enterprise Software Technology Predictions Report." December 2025\. [https://www.alixpartners.com/insights/enterprise-software-technology-predictions-report-2026/](https://www.alixpartners.com/insights/enterprise-software-technology-predictions-report-2026/)

20\.  Gartner. "SaaS Pricing Model Projections," as cited in Deloitte TMT Predictions 2026\. [https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions.html](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions.html)

21\.  Robert F. Smith, Vista Equity Partners. Public remarks on enterprise software sovereignty, 2025\. Coverage: [https://www.privatemarketsinsights.com/post/vista-s-robert-smith-on-ai-revolution-in-enterprise-software](https://www.privatemarketsinsights.com/post/vista-s-robert-smith-on-ai-revolution-in-enterprise-software)

22\.  European Union. "Regulation (EU) 2024/1689 (EU AI Act)." In force August 2024; obligations phasing in through 2028, with the AI Omnibus political agreement pointing to a revised high-risk timeline. [https://eur-lex.europa.eu/eli/reg/2024/1689/oj](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)

23\.  US State Legislatures. "AI Legislation Tracking, 2025–2026" (1,100+ bills across 45 states). National Conference of State Legislatures: [https://www.ncsl.org/technology-and-communication/artificial-intelligence-2025-legislation](https://www.ncsl.org/technology-and-communication/artificial-intelligence-2025-legislation)

24\.  LinuxInsider. "Open Source in 2026: AI, Funding Pressure, and Licensing Battles" (quoting Nadav Cornberg, Eve Security, on open standards for AI agents). January 5, 2026\. [https://www.linuxinsider.com/story/open-source-in-2026-faces-a-defining-moment-177630.html](https://www.linuxinsider.com/story/open-source-in-2026-faces-a-defining-moment-177630.html)

25\.  NIST. "AI Risk Management Framework (AI RMF 1.0)," January 2023; and "Generative Artificial Intelligence Profile (NIST-AI-600-1)," July 2024\. [https://www.nist.gov/itl/ai-risk-management-framework](https://www.nist.gov/itl/ai-risk-management-framework)

26\.  European Union. "EU AI Act, Articles 12 (Record-Keeping), 14 (Human Oversight), and 19 (Automatically Generated Logs)." Enforcement and transparency obligations from August 2026; high-risk obligations anticipated under the AI Omnibus political agreement for December 2027 (standalone Annex III systems) and August 2028 (AI embedded in regulated products). [https://artificialintelligenceact.eu/article/12/](https://artificialintelligenceact.eu/article/12/)

27\.  ISO/IEC. "ISO/IEC 42001:2023 — Information Technology — Artificial Intelligence — Management System." December 2023\. [https://www.iso.org/standard/81230.html](https://www.iso.org/standard/81230.html)

28\.  OWASP Foundation. "OWASP Top 10 for LLM Applications 2025." November 2024\. [https://owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

29\.  McKinsey & Company (QuantumBlack). "Seizing the Agentic AI Advantage." June 2025\. [https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage](https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage)

30\.  Gartner. "Gartner Says Applying Uniform Governance Across AI Agents Will Lead to Enterprise AI Agent Failure." Press release, May 26, 2026\. [https://www.gartner.com/en/newsroom/press-releases/2026-05-26-gartner-says-applying-uniform-governance-across-ai-agents-will-lead-to-enterprise-ai-agent-failure](https://www.gartner.com/en/newsroom/press-releases/2026-05-26-gartner-says-applying-uniform-governance-across-ai-agents-will-lead-to-enterprise-ai-agent-failure)

31\.  Black Duck (formerly Synopsys Software Integrity Group). "Open Source Security and Risk Analysis (OSSRA) Report," annual. [https://www.blackduck.com/resources/analyst-reports/open-source-security-risk-analysis.html](https://www.blackduck.com/resources/analyst-reports/open-source-security-risk-analysis.html)

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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>