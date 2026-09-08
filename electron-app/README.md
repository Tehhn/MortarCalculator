# Fire Mission Plotter — desktop app

A native Electron build of the calculator: a real window, its own taskbar
icon, no browser required, works fully offline (fonts are bundled locally).

## Run it from source

```
cd electron-app
npm install
npm start
```

## Build a Windows .exe yourself

```
cd electron-app
npm install
npx electron-builder --win portable --x64
```

The output lands in `electron-app/dist/FireMissionPlotter-portable.exe` —
a single portable executable, no installer, no admin rights needed. Just
copy it anywhere on a Windows machine and double-click it.

Building the Windows target from Linux/Mac requires Wine (for icon/resource
embedding); building on Windows itself needs nothing extra. The included
GitHub Actions workflow (`.github/workflows/build-electron.yml`) builds it
on a real `windows-latest` runner on every push to `main` that touches
`electron-app/`, and uploads the `.exe` as a downloadable workflow artifact
— no local setup required. Trigger it manually from the **Actions** tab
(`Build Fire Mission Plotter Desktop App` → **Run workflow**) any time.
