# Brand assets

Drop AGMA's official assets here, then update the two `ASSET SLOT` blocks in
`../index.html` (header and footer).

Expected:

- `agma-logo.svg` — primary logo, light version, for the dark header/footer.
  SVG preferred. If only a raster exists, supply @2x PNG on a transparent
  background.
- `agma-logo-dark.svg` — optional dark version, if any band inverts later.
- `favicon.ico` / `icon-512.png` — optional.

The swap is one line per slot:

```html
<img class="mark__logo" src="assets/agma-logo.svg" alt="AGMA">
```

`.mark__logo` is already defined in the stylesheet (30px tall in the header,
28px in the footer, width auto).

## Current state

The page ships with a placeholder geometric mark that is NOT AGMA's official
logo. This session's network policy blocked `agmaglobal.org` and their CDN
`cdn.ymaws.com` (HTTP 403 at the egress proxy), so the real assets could not be
retrieved. Replace the placeholder before this is shown as brand work.
