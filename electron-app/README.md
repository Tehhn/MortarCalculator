# Mortar Distance Calculator — desktop app

A native Electron build of the calculator: a real window, its own taskbar
icon, no browser required, works fully offline (fonts are bundled locally).

## Run it from source

```
cd electron-app
npm install
npm start
```

## Build it yourself

```
cd electron-app
npm install
npx electron-builder --win zip --x64
```

The output is `electron-app/dist/Mortar Distance Calculator-1.0.0-win.zip`.
Unzip it anywhere and run `Mortar Distance Calculator.exe` inside — no
installer, no admin rights needed.

**Why a zip instead of a single portable .exe:** electron-builder's
"portable" target wraps the app in a self-extracting NSIS stub, which a lot
of antivirus engines (including Windows Defender/SmartScreen) flag on
heuristics alone — self-extracting archives are a common malware delivery
shape, so the wrapper itself gets flagged even though the app inside is
harmless. A plain zip has no such wrapper, so it doesn't trip that
heuristic. If Windows still shows a SmartScreen prompt the first time you
run the exe (common for any new, unsigned app with no download history
yet), click **More info → Run anyway** — that's Windows being cautious
about an unrecognized publisher, not a detection of anything malicious.

Building the Windows target from Linux/Mac requires Wine (for icon/resource
embedding); building on Windows itself needs nothing extra. The included
GitHub Actions workflow (`.github/workflows/build-electron.yml`) builds it
on a real `windows-latest` runner on every push to `main` that touches
`electron-app/`, and uploads the zip as a downloadable workflow artifact —
no local setup required. Trigger it manually from the **Actions** tab
(`Build Mortar Distance Calculator Desktop App` → **Run workflow**) any time.
