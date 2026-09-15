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

## Membership application form

A demo form at `#apply`. It validates client side (required fields, email
shape, at least one threat selected), shows inline errors that say how to fix
them, and swaps to a confirmation with a generated reference number.

Nothing is transmitted or stored. No backend, no network call, no persistence,
and the page says so in two places. To make it real, post the form payload to
whichever system owns membership intake.

## Agency credit

A `.credit` band above the footer credits NAV & Associates, using their own
brand colours taken from their site's stylesheet (read through the WordPress
connector, since the site itself is not reachable from this session):

| Token | Value |
|---|---|
| Primary red | `#9E010C` |
| Deep red | `#63040B` |
| Solid red accent | `#8B020C` |
| Ink | `#19272B` |
| Pale tint | `#FFC4C8` |

The band reuses their signature radial red gradient. The wordmark is set in
type: their logo file could not be downloaded (see below), so drop
`assets/nav-associates-logo.png` in and swap `.credit__name` when available.

## Brand assets

The header and footer use AGMA's real logo, referenced at its live URL:

```
https://cdn.ymaws.com/agmaglobal.site-ym.com/resource/resmgr/do_not_delete/logo_white.png
```

This is the white version their own site serves in its footer, so it is the
correct variant for this page's dark ground. It loads normally when the page is
served from any ordinary host.

If the image cannot load, a small script swaps in the `.mark__fallback`
wordmark, so the header never renders empty. That fallback is what appears
inside the claude.ai artifact preview, whose content security policy blocks all
third-party images by design. To make the logo appear there too, save the file
into `assets/` and point `.mark__logo` at it, or inline it as a data URI.

The NAV & Associates credit is set in type rather than their logo. Their media
library holds several candidate files (`logo-light4.png`, `logo-light-3.png`,
`brand-logo.png`) but the light/dark naming is ambiguous and the files could not
be viewed from this session, so a wrong pick risked an invisible logo on the red
band.

## Content provenance## Content provenance

All organizational facts are drawn from public sources: founding year and
founding members, the four threat domains, the CBP Donations Acceptance Program
partnership, published white paper titles, and the $900B combined member
revenue figure. Trade statistics are from the OECD and EUIPO report *Mapping
Global Trade in Fakes 2025*.

Inspection records in the hero are illustrative and labelled as such. Part
numbers are invented, not real SKUs. This is an unofficial concept demo and is
marked as one in the page footer.
