# Explainers

Three walkthroughs of [the whitepaper](../whitepaper.md), for three different readers. They
are not drafts of each other — each answers a different question, and each is meant to stand
alone. Pick one; you should not need the others.

| Explainer | For | Answers | Length |
|---|---|---|---|
| [Executive Primer](executive-primer.md) | Decision-makers, industry | *What does this change for us?* | ~20 min |
| [Technical Primer](technical-primer.md) | Engineers and AI builders | *How does this actually work?* | ~30 min |
| [Plain-English Primer](plain-english-primer.md) | Everyone else | *What do these words mean?* | ~40 min |

**Executive Primer** opens on the consequence rather than the vocabulary, maps the paper's
six terms onto the language you already hear from vendors, and closes with questions worth
asking any AI supplier. Assumes you are expert in your own field and new only to this subject.

**Technical Primer** builds each concept from the problem it solves, anchored to things you
already know — deterministic functions, subclassing, CI, packaging, SQL injection. Assumes a
first-year CS background and nothing more.

**Plain-English Primer** teaches the whole vocabulary from zero using a single sustained
analogy: running an office and employing people. No computing background required.

## Relationship to the other documents here

- [`whitepaper.md`](../whitepaper.md) is the source of truth. Where an explainer and the paper
  disagree, the paper wins and the explainer is wrong.
- [`GLOSSARY.md`](../GLOSSARY.md) holds the canonical definitions. Explainers paraphrase for
  their audience; they do not redefine.
- [`briefs/executive-brief.md`](../briefs/executive-brief.md) is a two-page *summary* — what
  the paper says. The Executive Primer is an *explainer* — what it means and why the
  vocabulary exists. Different jobs.

## Maintenance

Explainers drift when the paper revises. Each states the revision it was written against in
its opening lines. When the paper changes materially — new or renamed concepts, a changed
definition — the explainers need a pass, and the "Note on Vocabulary" table in the paper is
the fastest place to check whether anything moved.

These are written to be read as Markdown. Formatted output, if wanted, is produced the same
way as the rest of the repository's output rather than by separate tooling.
