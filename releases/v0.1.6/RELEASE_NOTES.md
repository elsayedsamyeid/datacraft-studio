## DataCraft Studio 0.1.6

A reliability update. Free and Pro are still one app: free forever with no account, and Pro unlocks when you sign in with a DataCraft Pro account. No telemetry.

## What's fixed

- **PostgreSQL reconnects by itself.** A connection dropped by the network, a firewall or a server restart now recovers on your next action. Before, every refresh failed with "Failed" until you reconnected by hand.
- **The explorer stays where you put it.** Expanding a node no longer scrolls the tree down to the selected object.
- **A clean first run.** A fresh installation no longer reopens query tabs left behind by an earlier one.

## What's changed

- **MongoDB:** a simpler collection picker and result view in the query editor.
- **Dashboards** are no longer offered while the feature is reworked. Provider health is unchanged.

Full history: [CHANGELOG.md](https://github.com/elsayedsamyeid/datacraft-studio/blob/main/CHANGELOG.md).

## Download

Click **DataCraft-Studio-x64-setup.exe** below. That is the only file you need; it upgrades an existing installation in place and keeps your connections.

Also attached: **DataCraft-Studio-x64.msi** for managed installs, and **DataCraft-Studio-x64-portable.zip** to run without installing (keep every file in the folder together).

**Requires:** Windows 10 or 11, 64-bit. The installers include the Visual C++ runtime and install WebView2 if it is missing.

## Verify the installer

SHA-256 of **DataCraft-Studio-x64-setup.exe**:

```text
b4690eb5a3cfb4d939649e8d2ee0bcbb3d80a9d051935d17bd0e7cc17fff8d90
```

Checksums for all three files are in **SHA256SUMS.txt**. In PowerShell:

```powershell
Get-FileHash .\DataCraft-Studio-x64-setup.exe -Algorithm SHA256
```

The installers are not code signed yet. If Windows SmartScreen warns about a new publisher, compare the hash first, then choose **More info → Run anyway**.

Found a bug? [Open an issue](https://github.com/elsayedsamyeid/datacraft-studio/issues/new?template=bug_report.yml).
