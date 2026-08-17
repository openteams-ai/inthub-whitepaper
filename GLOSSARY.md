# Glossary — Canonical Terminology

This file is the authoritative definition set for the Distributed AI Economy whitepaper and every document derived from it. Decks, briefs, web copy, and future revisions should cite or copy these definitions rather than re-paraphrase them.

> Frames guide the work. Cogs perform the work. Ops orchestrate the work. Guards verify the work. Gates decide whether the work proceeds. Tracks make the work accountable.

## The canonical relationship

**Nebari is OpenTeams' flagship open-source contribution to the AI infrastructure ecosystem. Nebi is the reproducibility and distribution mechanism. The Intelligence Hub is a customer-specific assembly of open-source and proprietary components that OpenTeams integrates, governs, and maintains.**

Nebari is a contribution, not the platform. The platform is standards and open source. An Intelligence Hub is not "a Nebari deployment."

## Core terms

**Frame** — A scoped, text-based artifact (a file or folder of files using an open protocol) that carries the cultural and operational context within which work happens: rules, terminology, goals, style, norms, skills, tool specifications, prompts, architecture descriptions, business process details, and Output Guards to be run on results. Frames are scoped, inheritable, composable, shareable, discoverable, and **owned** — each Frame is accountable to a human or group of humans who intentionally manage it.

**Cog** — A discrete, AI-powered worker; the atomic unit of AI work in the system. A Cog encapsulates a model (possibly specialized), a context that includes one or more Frames, the skills, tools, and APIs it may use, and its governance parameters. Cogs are the key artifact distributed by Nebi and can include all the code, dependencies, and weights needed to generate an output from an input. Harnesses (including graph-centric ones), skills, tools, retrieval scaffolds, and evaluation hooks are *capabilities a Cog builder uses* to specialize a Cog — internal implementation details of the Cog, not competitors to it. Cogs are how agentic capability is modularized, specialized, and made developable by many parties.

**Op** — An *agentic app*: an orchestrated, supervised AI workflow that maps onto how knowledge workers describe their job ("Close the books," "Review this vendor for fraud"). An Op composes Cogs, applies Frames, coordinates through a supervising model, includes human-in-the-loop checkpoints, and carries a Nebi-compatible manifest and a declared Validation Strategy. Ops are versioned, installable, Frame-oriented, supervised, triggerable, self-contained, and composable.

**Agent** — The industry's word for a model in a loop with tools and a goal; in this architecture, a runtime phenomenon deliberately unbundled: the *capability* is a Cog, the *engagement* is an Op, and the *continuing actor* — identity, credentials, memory, history — is held by the Hub. Precisely: **an agent is a Cog engaged through an Op, given identity and memory by the Hub.** Kept separable, agents stay ownable, auditable, and portable.

**Guard** — Installable, versioned test and verification code that confirms the output of AI is in line with the standards and guidelines of the organization: a reusable verification-and-protection component that checks whether Cog or Op work is correct, safe, policy-compliant, and ready for use. Categories include Algorithmic, Source-Grounding, Consensus, Expert, Policy & Safety, Regression & Drift, and Outcome Guards. Frames can declare associated Guards; every Op must declare its Guards.

**Gate** — A decision point in an Op where the results of one or more Guards determine what happens next: continue, pause, request human approval, escalate to an expert, retry with a different Cog, run additional validation, or stop. Guards check; Gates decide.

**Track** — The durable evidence record of an Op or Cog execution: Frames applied, Cogs invoked, Guards run, Gate decisions, sources consulted, human approvals, and outputs produced. Tracks are the evidence substrate of accountable AI. Unlike Frames, Cogs, Ops, and Guards, **Tracks are not marketplace artifacts** — they are retained under the governance boundary of the Hub that produced them and produced only when required by audits or regulators.

**Accountability Plane** — The cross-cutting validation capability formed by Guards, Gates, and Tracks. Not a fourth layer beside Infrastructure, Execution, and Economy, but a plane that cuts across all three.

**Validation Strategy** — The part of every Op's contract that declares which Guards are used, where Gates occur, what Tracks are retained and for how long, and when human or expert review is required. An Op is not complete unless it declares how its work will be verified.

**Horizontal AI / Vertical AI** — Horizontal AI is application capability many industries can use (an accounting Op, an HR Op); vertical AI is the organization-specific specialization that makes a solution work against one company's standard operating procedures. Both live at the application layer. The architecture makes vertical specialization portable: a horizontal Op becomes vertical when it picks up an organization's Frames, is checked by its Guards, and leaves Tracks under its governance.

**Products around the Hub** — The second economy of the architecture: Hub experience applications (a desktop/web application among them), compute and model management, Track stores and audit, Gate and review consoles, Op and Cog builders, Guard libraries, specialized Ops for a segment or organization, and integration and operations services — built by many parties, open and commercial, and integrated into an organization's owned Hub. No single vendor supplies them, by design.

## Infrastructure terms

**Intelligence Infrastructure** — What company information technology (IT) infrastructure evolves into in the AI transformation: the owned, controlled, and governed systems through which an organization applies intelligence to its work. An organization's Intelligence Hub is its Intelligence Infrastructure made concrete. The justification is intimacy: applied, accountable intelligence must be intimate with the organization's most important data, and that intimacy is only safe when the organization owns and controls both the data and the intelligence.

**Ownership and control** — Always paired in this paper. Ownership without control is a title deed to a system someone else operates; control without ownership is stewardship that can be revoked. The architecture argues for both — of data, context, models, workflows, evidence, and the infrastructure that binds them.

**Intelligence Hub** — A sovereign, governed deployment inside an organization's own infrastructure perimeter that integrates models, data, business systems, workflows, and the organization's accumulated Frames, Cogs, Ops, and Guards into a unified AI control plane. Each Hub is a customer-specific assembly built on the organization's existing infrastructure; there is no central Hub, no mandatory platform, no shared tenant.

**Organizational Memory** — The Hub's persistent context substrate, holding both *intentional, human-accountable* context (Frames) and *emergent* context (records of Cog and Op activity, including Gates and Tracks). It belongs to the organization that produced it and cannot be rented or outsourced.

**Nebari** — OpenTeams' flagship open-source contribution to the AI infrastructure ecosystem (nebari.dev): a modular, composable stack for deploying, managing, and scaling AI infrastructure reproducibly.

**Nebi** — The reproducibility and distribution mechanism: the installation foundation for the Intelligence Hub that defines how environments, models, dependencies, Frames, Cogs, Ops, and Guards are specified, versioned, packaged, and deployed.

**Desktop/Web Application** — The canonical (pre-product-name) term for one product around the Hub: an application through which knowledge workers interact with their Intelligence Hub — combining Frames, conversing with Cogs, running Ops, seeing Guard status and Gate prompts, and sharing context. It is the paper's worked example of the products-around-the-Hub category, not the category itself. Use this exact phrase; do not vary it.

**The Marketplace** — Layer 3: the distributed economy in which Frames, Cogs, Ops, Guards, and future artifact classes are published, discovered, installed, and exchanged across Intelligence Hubs. Tracks are not exchanged.

## Usage rules

- Four exchanged artifact classes: Frames, Cogs, Ops, Guards (and more over time). Tracks are records, not marketplace artifacts.
- "Three-layer architecture with a cross-cutting accountability plane" — never "four layers."
- Formatted .docx/.pdf builds of the whitepaper are "formatted output," not "derivatives."
- The category is **accountable enterprise AI**.
- Say "own and control" (or "owned and controlled"), not "own" alone, when describing what organizations keep. Frame the transformation as IT → Intelligence Infrastructure.
- Participation is described as offering, contributing, and promoting open standards — never as owning or defining them. "Open standards we promote," "open source we contribute," "products built by many."
- The paper argues for an ecosystem; OpenTeams appears as one participant (contributor, integrator, reseller, super-node), not the center.
- Do not present the Desktop/Web Application as *the* product; it is one of many products around the Hub.
- Do not define agents away; unbundle them. "The industry built the agent. The Intelligence Hub is where agents are employed."
