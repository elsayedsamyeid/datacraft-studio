## DataCraft Studio 0.1.6 — first public release

A native Windows data workspace for eleven source types. One app for everyone: free forever with no account, and Pro features unlock in the same app when you sign in with a DataCraft Pro account. No telemetry.

## Included

- PostgreSQL, SQL Server, MySQL / MariaDB, SQLite and DuckDB
- MongoDB and Elasticsearch
- CSV, Excel, JSON and Parquet files
- Provider-aware explorer and query editor
- Engine-aware autocomplete with snippets, previews and placeholders
- Unified result grid, JSON viewer, aggregates and export
- Unlimited connections, with passwords protected by Windows Credential Manager
- Optional sign-in: a Pro account unlocks Pro features on one computer at a time, and keeps working offline for up to three days between checks

## Getting Pro

Pro is available on request. In the app, open **Settings → Features → Plan** and choose **Sign in to unlock Pro** (sign-in opens in your browser), then [open a Pro request](https://github.com/elsayedsamyeid/datacraft-studio/issues/new?template=pro_request.yml) with your email partly hidden. Once Pro is enabled, sign out and sign in again.

## Download

Click **DataCraft-Studio-x64-setup.exe** below. That is the only file you need.

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
