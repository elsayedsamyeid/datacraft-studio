## DataCraft Studio 0.1.5

A native Windows data workspace for eleven source types. One app for everyone: free forever with no account, and Pro features unlock in the same app when you sign in with a DataCraft Pro account. No telemetry.

## Download

Click **DataCraft-Studio-x64-setup.exe** on the GitHub release. That is the only file you need.

Also attached: **DataCraft-Studio-x64.msi** for managed installs, and **DataCraft-Studio-x64-portable.zip** to run without installing (keep every file in the folder together).

The installers include the app-local Microsoft Visual C++ runtime files required by the database engines and the Microsoft WebView2 bootstrapper. Do not download or place DLL files manually.

**Requires:** Windows 10 or 11, 64-bit.

## Included

- PostgreSQL, SQL Server, MySQL / MariaDB, SQLite and DuckDB
- MongoDB and Elasticsearch
- CSV, Excel, JSON and Parquet files
- Provider-aware explorer and query editor
- Engine-aware autocomplete with snippets, previews and placeholders
- Unified result grid, JSON viewer, aggregates and export
- Unlimited connections
- Credentials protected by Windows Credential Manager
- Optional sign-in: a Pro account unlocks Pro features on one computer at a time, and keeps working offline for up to three days between checks

## Getting Pro

Pro is available on request. In the app, open **Settings → Features → Plan** and choose **Sign in to unlock Pro** (sign-in opens in your browser), then [open a Pro request](https://github.com/elsayedsamyeid/datacraft-studio/issues/new?template=pro_request.yml) with your email partly hidden. Once Pro is enabled, restart the app.

## Verify the installer

SHA-256 of **DataCraft-Studio-x64-setup.exe**:

```text
e2cf663170f0a4953ad3c7736fe9275e6638181c61e36615aa1c255ce4f917b9
```

Checksums for all three files are in **SHA256SUMS.txt**.

In PowerShell:

```powershell
Get-FileHash .\DataCraft-Studio-x64-setup.exe -Algorithm SHA256
```

If Windows SmartScreen warns about a new publisher, compare the hash first, then choose **More info → Run anyway**.

Found a bug? [Open an issue](https://github.com/elsayedsamyeid/datacraft-studio/issues/new?template=bug_report.yml).
