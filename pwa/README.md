# Fire Mission Plotter — installable app

This folder is a self-contained Progressive Web App (PWA): the same mortar
range/bearing calculator, packaged with a manifest and offline service
worker so it installs as a real app icon on desktop and mobile.

## 1. Host it (one-time)

A PWA needs to be served over HTTPS from a real URL — installability and
the offline service worker don't work from a local `file://` path.

A GitHub Actions workflow is already included at
`.github/workflows/deploy-pwa.yml`. To turn it on:

1. Merge this branch into `main`.
2. In the repo on GitHub: **Settings → Pages → Build and deployment →
   Source → GitHub Actions**.
3. Push to `main` (or run the workflow manually from the Actions tab).
   It publishes the `pwa/` folder to
   `https://<your-github-username>.github.io/<repo-name>/`.

Any other static host (Netlify, Vercel, Cloudflare Pages, your own server)
works too — just serve the contents of this folder as-is.

## 2. Install it

**Desktop (Windows/Mac/Linux, Chrome/Edge/Brave):**
Open the hosted URL, then click the install icon in the address bar (or the
"Install app" button on the page) → **Install**. It opens in its own
window with its own icon, no browser chrome.

**Android (Chrome):**
Open the URL → menu (⋮) → **Install app** (or **Add to Home screen**).

**iPhone/iPad (Safari):**
Open the URL → Share button → **Add to Home Screen**. Safari doesn't
support the install prompt banner, but the result is the same: a home
screen icon that opens full-screen.

Once installed, the app works offline (the calculator itself needs no
network — only the two Google Fonts need connectivity the first time).
