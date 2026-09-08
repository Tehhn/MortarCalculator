# Mortar Distance Calculator — Android app

A native Android build of the calculator (via Capacitor): a real app icon,
runs full-screen with no browser UI, works offline.

## One-time setup: add signing secrets (do this once)

Without this, the CI build falls back to a **debug-signed** APK. Debug
builds use Android's well-known, publicly shared debug key, which Google
Play Protect specifically flags on newer phones — the exact "isn't safe /
doesn't include the latest privacy protections" warning (or an outright
install block) that shows up when you try to sideload one. A real,
unique signing key avoids that.

Claude generated a release keystore for this app and sent it to you
separately (`release.keystore`) along with 4 values. **Save that file
somewhere safe — if it's lost, this app can never be updated under the
same signature again (you'd have to uninstall the old copy first for
every future update).**

Add these as repo secrets: **Settings → Secrets and variables → Actions →
New repository secret** (create all 4):

| Secret name | Value |
|---|---|
| `ANDROID_KEYSTORE_BASE64` | base64 contents of `release.keystore` (see below) |
| `ANDROID_KEYSTORE_PASSWORD` | the store password Claude gave you |
| `ANDROID_KEY_ALIAS` | `mortarcalc` |
| `ANDROID_KEY_PASSWORD` | same as the store password |

To get the base64 value for `ANDROID_KEYSTORE_BASE64`, run this wherever
you saved the file, then paste the output as the secret's value:

```
base64 -w0 release.keystore   # macOS: base64 -i release.keystore
```

Once all 4 secrets exist, every future run of the Android workflow
automatically builds a **release** APK signed with this key instead of a
debug one — no other changes needed.

## Get the APK (no local Android setup needed)

This repo builds it for you on GitHub Actions, since the Android SDK and
Gradle need real internet access to Google's Maven repo:

1. On GitHub, open the **Actions** tab.
2. Select **"Build Mortar Distance Calculator Android APK"**.
3. Click **Run workflow** (pick the branch with this folder).
4. When it finishes, open the run and download the
   `MortarDistanceCalculator-android` artifact — unzip it to get
   `app-release.apk` (or `app-debug.apk` if the signing secrets above
   aren't set up yet).

## Install it on your phone

This isn't distributed through the Play Store, so Android will still show
an "install from unknown sources" prompt regardless of signing — that's
expected for any sideloaded app and is different from the debug-signature
warning above:

1. Copy the APK to your phone (email it to yourself, use a cloud drive, or
   `adb install app-release.apk` over USB).
2. Open the file on the phone. If prompted, allow your file manager/browser
   to **install unknown apps**.
3. Tap **Install**.

## Build it yourself

Requires Node.js, a JDK, and the Android SDK/Gradle:

```
cd android-app
npm install
npx cap sync android
cd android
./gradlew assembleDebug
```

Output: `android-app/android/app/build/outputs/apk/debug/app-debug.apk`.
Building a signed `assembleRelease` locally needs the same
`ANDROID_KEYSTORE_PATH` / `ANDROID_KEYSTORE_PASSWORD` / `ANDROID_KEY_ALIAS`
/ `ANDROID_KEY_PASSWORD` environment variables the CI workflow uses.
