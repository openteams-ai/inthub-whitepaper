# The Distributed AI Economy

**Intelligence Hubs, Frames, Cogs, Ops, and the Accountability Plane**

This repository is the master source for the OpenTeams whitepaper describing a three-layer architecture — Infrastructure, Execution, and Economy — with a cross-cutting validation plane that makes AI work accountable.

> Frames guide the work. Cogs perform the work. Ops orchestrate the work. Guards verify the work. Gates decide whether the work proceeds. Tracks make the work accountable.

The paper covers the shift from rented to owned intelligence, the Intelligence Hub as the organizational deployment (built on the open-source ecosystem, with Nebari as OpenTeams' flagship contribution and Nebi as the reproducibility and distribution mechanism), the Frame / Cog / Op execution model, the Guards / Gates / Tracks accountability plane, the four-class marketplace, and the Desktop/Web Application that brings the system to knowledge workers.

## Repository layout

| Path | Contents |
|---|---|
| `Intelligence_Hub_Whitepaper_v8.md` | The whitepaper source of truth (Markdown) |
| `media/` | Figure images referenced by the source (`image1` = architecture overview, `image2` = validation lifecycle) |
| `GLOSSARY.md` | Canonical terminology — the authoritative definitions all materials should cite |
| `MESSAGING.md` | Approved short-form messaging variants by audience |
| `SOURCES.md` | Claims register — every statistical claim mapped to its verified source |
| `tools/` | `make_diagrams.py` — regenerates the figures in `media/` |
| `outputs/` | Locally generated formatted output (.docx, .pdf) — git-ignored; published as release assets instead |

## Releases

Formatted output files are attached to tagged releases rather than committed to the branch. The current revision is **v8** — download the .docx and .pdf from the [Releases](../../releases) page.

## Revision workflow

1. Edit `Intelligence_Hub_Whitepaper_v8.md` (rename per revision as appropriate) and update `media/` if figures change.
2. Regenerate the .docx and .pdf output files into `outputs/`.
3. Commit and push the source changes, then tag and publish:

   ```bash
   git tag v9 && git push --tags
   gh release create v9 outputs/*.docx outputs/*.pdf --title "Revision 9" --notes "Summary of changes"
   ```

## Status

OpenTeams working document. Revision 8, July 2026.
