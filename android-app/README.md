# Fire Mission Plotter — Android app

A native Android build of the calculator (via Capacitor): a real app icon,
runs full-screen with no browser UI, works offline.

## Get the APK (no local Android setup needed)

This repo builds it for you on GitHub Actions, since the Android SDK and
Gradle need real internet access to Google's Maven repo:

1. On GitHub, open the **Actions** tab.
2. Select **"Build Fire Mission Plotter Android APK"**.
3. Click **Run workflow** (pick the branch with this folder).
4. When it finishes, open the run and download the `FireMissionPlotter-android`
   artifact — unzip it to get `app-debug.apk`.

## Install it on your phone

The APK is a debug build (self-signed, not through the Play Store), so
Android will warn about installing from an unknown source — that's expected
for a personal-use app:

1. Copy `app-debug.apk` to your phone (email it to yourself, use a cloud
   drive, or `adb install app-debug.apk` over USB).
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
