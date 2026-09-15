# AGMA Global — homepage concept demo

A single-file, dependency-free homepage concept for AGMA, the Alliance for Gray
Market and Counterfeit Abatement.

Open `index.html` directly in a browser, or serve the directory. No build step.

## Design direction

Dark-first "forensic lab" treatment. The brand's actual job is telling real from
fake, so the hero is an authentication terminal that cycles real-shaped
inspection records and their verdicts.

| Token | Value | Role |
|---|---|---|
| Ink | `#0A0E17` | Page ground |
| Panel | `#131A28` | Raised surfaces |
| Dossier paper | `#ECEEF2` | Alternating light bands |
| Authentic teal | `#2FD4C0` | The single accent, all primary actions |
| Suspect coral | `#FF6B4A` | Semantic threat only, never decorative |
| Mute | `#8A94A8` | Blue-biased neutral |

Typefaces: **Archivo** (variable width, institutional display), **Public Sans**
(body — the US federal design system face, fitting a D.C. non-profit that
partners with CBP), **IBM Plex Mono** (serials, part numbers, verdicts).

Sections alternate ink and paper bands so the generous vertical rhythm reads as
distinct chapters rather than dead space.

## Implementation notes

- Deliberately single-theme. Every background and color is painted explicitly,
  so the page holds on either host ground.
- Nothing is visibility-gated behind JavaScript. The first inspection record is
  in the markup, and the stat figures are their final values; JS only enhances.
- Working mobile nav below 980px, with the primary CTA relocated into the menu.
- No horizontal overflow at 375px (verified).
- `prefers-reduced-motion` stops the scanline and record cycling.

## Brand assets

The page ships with a **placeholder** geometric mark. It is not AGMA's official
logo. `agmaglobal.org` and their CDN `cdn.ymaws.com` were both blocked (HTTP
403) by this environment's egress proxy, so the real assets could not be
retrieved.

Two `ASSET SLOT` comments in `index.html` mark where the real logo goes, and
`.mark__logo` is already styled for it. See `assets/README.md`.

## Content provenance

All organizational facts are drawn from public sources: founding year and
founding members, the four threat domains, the CBP Donations Acceptance Program
partnership, published white paper titles, and the $900B combined member
revenue figure. Trade statistics are from the OECD and EUIPO report *Mapping
Global Trade in Fakes 2025*.

Inspection records in the hero are illustrative and labelled as such. Part
numbers are invented, not real SKUs. This is an unofficial concept demo and is
marked as one in the page footer.
