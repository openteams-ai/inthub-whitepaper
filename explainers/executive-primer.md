# The Distributed AI Economy — An Executive Primer

*The argument in* The Distributed AI Economy *(Revision 9), for people who will decide
whether to act on it. Assumes you are expert in your own field and new only to this
vocabulary. Twenty minutes.*

---

## The argument in one paragraph

Your organisation is accumulating AI spend but not an AI asset. The context that makes AI
useful — your rules, your terminology, your standards for what "correct" looks like — is
being typed into vendor chat windows and discarded. The records of what AI decided on your
behalf sit on infrastructure you don't control. The paper's claim is that this is an
architectural problem rather than a procurement one, and that the fix is to make context,
capability, validation and evidence into **things you own, version and exchange** — the same
move software made when it standardised packages, and data made when it standardised
formats.

---

## 1. What you're actually buying today

Two problems, both structural.

**You are renting intelligence.** Questions go to someone else's infrastructure. Your data
travels with them, you can't inspect the reasoning, you can't reproduce a decision from six
months ago, and when the vendor changes the model your outputs change with it. None of that
is a complaint about quality. It's a statement about where the leverage sits.

**Your context evaporates on use.** Every organisation runs on knowledge that isn't written
down: which rules are non-negotiable, what "finished" means, how you speak to a regulator
versus a customer. Today someone explains all that to an AI, gets an answer, and closes the
window. Tomorrow a colleague explains it again, slightly differently. You are paying to
re-explain yourself indefinitely, and accumulating nothing that compounds.

The second problem is the more expensive one, and it's the one nobody is buying a solution
to.

---

## 2. The vocabulary, mapped from what you already say

You arrive at this fluent in the industry's language. The paper introduces six terms and —
usefully — states the difference in one line each. This table is from the paper itself.

| You know it as | The paper calls it | The difference |
|---|---|---|
| Skills | **Frames** | A skill with an owner — scoped, versioned, accountable to a named human |
| An agent harness | Part of a **Cog** | The harness is the loop; a Cog is what the loop ships as — model, context, tools and permissions, packaged so they can be installed and audited |
| An agent workflow | An **Op** | A workflow with a declared validation strategy: which checks run, where humans decide, what record is kept |
| Evals and guardrails | **Guards** | Evals that ship with the artifact — versioned and installable, run at declared points rather than bolted on afterwards |
| An agent trace | A **Track** | A trace you own: canonical, exportable, retained under your governance rather than the vendor's |
| An agent | A Cog engaged through an Op | Capability, engagement and identity kept separate, so the agent stays ownable and portable |

If a distinction in that table doesn't survive contact with your own operation, the term
hasn't earned its place. That is a fair test to apply as you read.

---

## 3. The central idea: employing agents, not building them

This is the part worth your attention, and it's what changed in Revision 9.

The industry has settled on the agent — a model in a loop, with tools, pursuing a goal.
Everyone ships one. The paper's position is that building agents is no longer the hard part:

> The hard problem in enterprise AI is no longer *building* an agent. It is *employing* one.

Employment is a different set of questions, and they are recognisably management questions:

- Who does this agent work for?
- Whose policies govern it?
- What may it touch, and under whose identity?
- How much autonomy has it been granted — and by whom?
- Who checks its work *before* the work has consequences?
- What record remains for the person accountable for the outcome?

Each piece of the architecture answers one of those. **Frames** are the context and policy it
works under. A **Cog** is the qualified hire, vetted before deployment. An **Op** is the
assignment, with deliverable and checkpoints defined. **Guards** check the work. **Gates**
set the autonomy budget — the boundary between what it may do alone and what needs a human.
**Tracks** are its personnel record. The **Intelligence Hub** is the workplace: identity,
tools, compute and memory inside your own perimeter.

The consequential design point is that autonomy is *granted per engagement, not per
platform*. A drafting task may run unattended; a payments task may require approval at every
step. Gartner's warning is that uniform governance across agents is precisely what fails, and
that **by 2027, 40% of enterprises will demote or decommission autonomous agents over
governance gaps found only after production incidents** (Gartner, May 2026). Tailoring
autonomy per task is what avoids being in that 40%.

---

## 4. Why the record matters more than it sounds

One technical fact with a large commercial consequence.

AI is not deterministic. Ask the same question twice and you can get two different answers.
This means **you cannot reconstruct what happened by re-running it.** With a spreadsheet you
re-run the calculation. Here, re-running gives you a fresh answer, not last quarter's.

So the execution record isn't a compliance nicety layered on afterwards. It's the only place
the information exists. If you didn't capture it, the reasoning behind a decision your
organisation made is gone.

Regulation is converging on the same requirement from the other direction: the EU AI Act
obliges high-risk systems to log events automatically and deployers to retain those logs, and
requires that a person can interpret, override or halt the system (Articles 12, 14 and 19).
Organisations that treat evidence as a first-class output satisfy that by construction.
Organisations that don't will retrofit it under time pressure.

---

## 5. Where the value settles when generation is free

The paper's sharpest commercial observation, and the one most worth arguing with:

> When generation is free, provenance is the product.

The reasoning: as generation gets cheap, code stops being scarce — anyone can produce a
plausible artifact this afternoon. What can't be generated on demand is *verification,
context and accountability*. A privacy check for a regulated industry is valuable because of
who stands behind it. A Frame is distilled expertise with a named, accountable owner. And a
workflow that has accumulated a thousand validated execution records is trustworthy in a way
an identical one generated this morning is not — because that record can only accumulate
through real, governed use.

If that holds, the durable asset isn't the AI. It's the accumulated, owned evidence that your
AI does what you say it does. That is also, not coincidentally, the thing you cannot buy
late.

---

## 6. Where this actually is today

Honest status, because the vocabulary is more mature than the implementation and you should
calibrate accordingly.

| Piece | Status |
|---|---|
| **Frames** — owned context | Draft specification published; tooling in use |
| **Cogs** — packaged AI workers | Draft specification published, under active discussion |
| **Ops** — supervised workflows | Designed; specification not yet written |
| **Guards, Gates, Tracks** — the accountability layer | Designed; newest part of the architecture, earliest in build |
| **Nebari** — the open infrastructure toolkit | Shipping |
| **Nebi** — reproducible environments | Shipping |
| **Intelligence Hub** — the deployment | Assembled per organisation; not an off-the-shelf product |

Read the paper as a proposed standard with a partial implementation behind it. The
accountability layer — the part that matters most in a regulated setting — is the newest and
least built. That is worth knowing before you plan around it, and it is also where an early
adopter has the most influence over how the standard turns out.

---

## 7. What to ask

Whatever you conclude about this architecture, these questions are useful against any AI
vendor. They're drawn from the failure modes the paper identifies.

1. **Where does our context live, and can we export it?** If the answer involves their
   infrastructure and no export path, you are renting and accumulating nothing.
2. **What record survives if we leave?** Ask to see one. Ask what format it's in.
3. **Can you reproduce a result from six months ago?** If the model has been updated and the
   old one isn't retained, the honest answer is no.
4. **Who grants the AI its permissions — you or us?** A system that arrives holding its own
   credentials is a supply-chain problem, whatever else it is.
5. **What checks run before output reaches a customer, and who wrote them?** "The model is
   very good" is not a check.
6. **Which decisions require a human, and can we change that boundary per task?** If autonomy
   is a global setting rather than a per-task one, you have the failure mode Gartner is
   describing.
7. **If we stop paying, what do we keep?** The most clarifying question on the list.

---

## 8. The whole thing, on one page

**The problem.** You're renting intelligence and discarding the context that makes it
valuable. Neither produces a compounding asset.

**The proposal.** Make four things into artifacts you own and can exchange: context
(Frames), workers (Cogs), workflows (Ops) and checks (Guards). Keep the evidence (Tracks)
inside your own perimeter. Run all of it on infrastructure you control (the Intelligence
Hub).

**The reframe.** Building agents is solved. Employing them — context, supervision, granted
authority, and a record — is not. That's the gap.

**The bet.** When generating capability is cheap, the scarce thing is provenance: verified,
owned evidence that the work is sound. Whoever holds the context, memory and history owns the
agent.

**The caveat.** The vocabulary is ahead of the implementation, most of all in the
accountability layer. Plan on that basis — and note that early participants shape standards
in a way later adopters cannot.
