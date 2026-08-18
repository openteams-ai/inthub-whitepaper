# The Distributed AI Economy

**Intelligence Hubs, Frames, Cogs, Ops, and the Accountability Plane**

This repository is the master source for the OpenTeams whitepaper describing the architecture of a scalable, distributed AI economy — three layers (Infrastructure, Execution, Economy) with a cross-cutting accountability plane — and the shared abstractions (Frames, Cogs, Ops, Guards, Gates, Tracks) that let many parties build to it.

> Frames guide the work. Cogs perform the work. Ops orchestrate the work. Guards verify the work. Gates decide whether the work proceeds. Tracks make the work accountable.

The paper covers the shift from rented to owned intelligence, the Intelligence Hub as the organizational deployment (built on the open-source ecosystem, with Nebari as OpenTeams' flagship contribution and Nebi as the reproducibility and distribution mechanism), the Frame / Cog / Op execution model, the Guards / Gates / Tracks accountability plane, the four-class marketplace, and the economy of products around the Hub — with a Desktop/Web Application as the worked example.

## Repository layout

| Path | Contents |
|---|---|
| `whitepaper.md` | The whitepaper source of truth (Markdown) — versions are carried by git tags, not the filename |
| `media/` | Figure images referenced by the source (`image1` = architecture overview, `image2` = validation lifecycle, `image3` = the AI stack) |
| `briefs/` | `executive-brief.md` — two-page summary source (formatted output on releases) |
| `explainers/` | Audience-specific walkthroughs of the paper — executive, technical, and plain-English primers |
| `GLOSSARY.md` | Canonical terminology — the authoritative definitions all materials should cite |
| `MESSAGING.md` | Approved short-form messaging variants by audience |
| `SOURCES.md` | Claims register — every statistical claim mapped to its verified source |
| `tools/` | `make_diagrams.py` — regenerates the figures in `media/` |
| `outputs/` | Locally generated formatted output (.docx, .pdf) — git-ignored; published as release assets instead |

## Releases

Formatted output files are attached to tagged releases rather than committed to the branch. Versions are git tags (the current tag is **v9**); download the .docx and .pdf from the corresponding [release](../../releases). The revision line inside the document is bumped as part of each release.

## Revision workflow

1. Edit `whitepaper.md` (bump the in-document revision line) and update `media/` if figures change.
2. If terminology changed — a concept added, renamed, or redefined — update `explainers/` to match. The "A Note on Vocabulary" table in the paper is the quickest way to see whether anything moved.
3. Regenerate the .docx and .pdf output files into `outputs/`.
4. Commit and push the source changes, then tag and publish:

   ```bash
   git tag v10 && git push --tags
   gh release create v10 outputs/Intelligence_Hub_Whitepaper.docx outputs/Intelligence_Hub_Whitepaper.pdf --title "Revision 10" --notes "Summary of changes"
   ```

## Status

OpenTeams working document. Revision 9, August 2026.
