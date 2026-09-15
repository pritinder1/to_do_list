# Brand assets

Both logos are the real thing, and both are also embedded directly in
`../index.html` as base64 data URIs, so the page renders correctly with no
external requests. The files here are the sources.

| File | Origin | Notes |
|---|---|---|
| `agma-logo-white.png` | `cdn.ymaws.com/agmaglobal.site-ym.com/resource/resmgr/do_not_delete/logo_white.png` | The white lockup AGMA serves in their own footer. Resized to 404x110, PNG8, 4.3KB. |
| `nav-associates-logo-white.png` | `navandassoc.com/wp-content/uploads/2025/12/brand-logo.png` | NAV's white knockout logo. Resized to 699x120, PNG8, 3.6KB. |

## Picking the right variants

AGMA serves two: `logo.png` (dark, for their white header) and
`logo_white.png` (for their navy footer). This page is dark, so it uses the
white one.

NAV's library holds several files whose light/dark naming is ambiguous. Sampling
the artwork colour over a black background (rather than the default white, which
makes every transparent PNG look white) showed:

| File | Artwork colour |
|---|---|
| `brand-logo.png` | near-white `#F0F0F0` |
| `logo-mb.png` | brand red `#63040C` |
| `logo-dark-2.png` | near-black |

So `brand-logo.png` is the white knockout, which is what the red credit band
needs. Both logos are white-on-transparent, so PNG8 with a two-entry palette is
lossless in practice and keeps them under 5KB each.

## Replacing them

Swap the file here, re-encode it as a data URI, and replace the matching
`src="data:image/png;base64,..."` in `index.html`. The header uses
`.mark__logo`, the footer the same class at a larger size, and the agency credit
uses `.credit__logo`.

## Generated assets

| File | How it was made |
|---|---|
| `favicon-32/64/180.png` | The globe dome lifted out of AGMA's own lockup, strokes dilated so they survive downscaling, centred on brand navy `#0B1D30`. The unmodified logo's hairlines turn to mush below about 48px. The 64px version is inlined in the page as a data URI; the 180px is the Apple touch icon. |
| `og-image.png` | 1200x630 share card: the real logo on the page's `#091420` ground with the hero line and a brand-blue rule. Rendered from HTML through headless Chromium, then palette-reduced. |

`og:image` and `twitter:image` currently point at the relative path
`assets/og-image.png`. Most scrapers require an absolute URL, so change these to
the full `https://.../assets/og-image.png` once the page has a real hostname.

## Member logo wall

`member-logos-sprite.png` is a single 2800x64 sprite holding all 14 member logos
in uniform 200x64 cells, taken from AGMA's own member rotator. It is embedded in
the page as a data URI and positioned with CSS, so the whole wall costs one
image and zero extra requests.

Cell order (left to right, `--i` 0 through 13):

| # | Member | # | Member |
|---|---|---|---|
| 0 | Siemens | 7 | HP |
| 1 | Amazon | 8 | Brand Alignment |
| 2 | HPE | 9 | IBM |
| 3 | MSU A-CAPP Center | 10 | Sideman & Bancroft |
| 4 | TD SYNNEX | 11 | Cisco |
| 5 | Rockwell Automation | 12 | Microsoft |
| 6 | Schneider Electric | 13 | Marvell |

Each tile is a `<li class="mlogo" style="--i:N" role="img" aria-label="...">`, so
the member name reaches assistive tech even though the logo is a background
image.

Logos render greyscale at 58% and come to full colour on hover. Note the filter
is `grayscale(1) opacity(.58)` with **no** `contrast()`: any contrast below 1
lifts the cell's white off pure white and draws a visible grey box behind every
logo.

To change the roster, rebuild the sprite with the same 200x64 cell size and keep
the `--i` indices in sync with the new order.

### Source files

The rotator images live at
`cdn.ymaws.com/agmaglobal.site-ym.com/resource/dynamic/rotator/`. The
`agmaglobal.org` path for the same files returns 403 to non-browser clients; the
CDN host serves them.
