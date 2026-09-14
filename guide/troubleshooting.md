# Troubleshooting

## Installing and starting

### "Windows protected your PC"

SmartScreen warns about software from a publisher it doesn't know yet. Before running the
installer, check it is the real file:

```powershell
Get-FileHash .\DataCraft-Studio-x64-setup.exe -Algorithm SHA256
```

Compare the result with the SHA-256 in the [release notes](https://github.com/elsayedsamyeid/datacraft-studio/releases/latest).
If it matches, choose **More info → Run anyway**. If it doesn't match, don't run it—download
again from this repository only.

### The portable app doesn't start

- Keep **every file** from the zip in the same folder. `DataCraft Studio.exe` needs the DLLs
  beside it.
- The portable package can't install **Microsoft WebView2**. If it's missing (rare on
  up-to-date Windows 10 and never on Windows 11), use the `.exe` installer instead.

### "The code execution cannot proceed … MSVCP140.dll was not found"

The runtime DLLs were separated from the app. Use the installer, or extract the whole portable
zip again without moving files out of the folder.

## Connections

### My password isn't remembered

Passwords are kept in **Windows Credential Manager**. If it's unavailable—for example on some
locked-down corporate machines—passwords last only until you close the app. Check that
Credential Manager opens from the Control Panel for your Windows account.

### The connection test fails

- Check host, port and firewall access from this computer (for example with `Test-NetConnection host -Port 5432`).
- Check TLS settings: a server that requires encryption needs the matching SSL or encryption
  option, and a self-signed certificate needs its CA certificate or the trust option.
- See the fields for your engine in [Connecting to your data](connecting.md).

### There's no Stop button while a query runs

Stopping a running query is offered only for data sources whose drivers support cancellation.
For the others, the query runs until the server finishes or its timeout is reached—set a query
timeout on the connection if you need a limit.

### The explorer or autocomplete looks out of date

Select the connection or object in **Explorer** and press <kbd>F5</kbd> to refresh its metadata.

## Sign-in and Pro

### The sign-in page doesn't open

DataCraft opens sign-in in your default web browser. Check that a default browser is set in
**Windows Settings → Apps → Default apps**, then try **Sign in to unlock Pro** again.

### Sign-in finishes in the browser but the app isn't signed in

- **Verify your email.** Accounts with an unverified email can't sign in—use the link in the
  verification email, then sign in again.
- If the browser asks to open **DataCraft Studio**, allow it: that's how the browser hands the
  sign-in back to the app.
- Finish sign-in within 10 minutes of starting it, and start it again if you waited longer.

### "This Pro licence is now in use on another device"

You signed in on another computer, so the licence moved there. To use Pro here again, sign in
again from **Settings → Features → Plan**. The licence moves back.

### "This Pro licence has moved between devices too often recently"

To prevent sharing, a licence can only move a limited number of times in a period. Sign out on
the other computer with **Sign out this device**, or [open a Pro request](https://github.com/elsayedsamyeid/datacraft-studio/issues/new?template=pro_request.yml)
if you replaced a computer.

### My account was upgraded, but the app still shows Free

1. **Restart** DataCraft Studio—the plan is read when the app starts.
2. Open **Settings → Features → Plan** and check you're signed in with the **same email** that
   was upgraded.
3. Make sure the computer is **online**. If the app has been offline for more than three days,
   Pro pauses until it can check in.

### A Pro feature says "This is a DataCraft Pro feature"

The app is running as Free right now: you're signed out, offline for more than three days,
your sign-in expired, or the licence moved to another computer. Open **Settings → Features → Plan**
to see which, and sign in again.

## Resetting DataCraft Studio

To start completely fresh:

1. Close the app, and sign out first if you use Pro (**Sign out this device**).
2. Uninstall it from **Windows Settings → Apps → Installed apps**.
3. Delete these folders:
   - `%APPDATA%\DataCraft Studio` — connections, workspace, query drafts, metadata cache
   - `%LOCALAPPDATA%\com.datacraft.studio` — interface preferences
4. Open **Credential Manager → Windows Credentials** and remove the DataCraft entries.

> Deleting `%APPDATA%\DataCraft Studio` removes your saved connections and workspace. Back it
> up first if you might want them.

## Still stuck?

[Open a bug report](https://github.com/elsayedsamyeid/datacraft-studio/issues/new?template=bug_report.yml)
with your version, plan, data source and the exact error text. See [SUPPORT.md](../SUPPORT.md).

[← User guide](README.md)
