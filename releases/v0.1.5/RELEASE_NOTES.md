## DataCraft Studio 0.1.5 — Free Edition

A native Windows data workspace for eleven source types. Free forever, with no account and no telemetry.

## Download

Click **DataCraft-Studio-x64-setup.exe** on the GitHub release. That is the only file you need.

The installer includes the app-local Microsoft Visual C++ runtime files required by the database engines and the Microsoft WebView2 bootstrapper. Do not download or place DLL files manually.

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

## Verify the installer

SHA-256:

```text
63aeb346a7691a1281fa2fd5fab812896dace00f9207a3091891b6337c93c429
```

In PowerShell:

```powershell
Get-FileHash .\DataCraft-Studio-x64-setup.exe -Algorithm SHA256
```

If Windows SmartScreen warns about a new publisher, compare the hash first, then choose **More info → Run anyway**.

Found a bug? [Open an issue](https://github.com/elsayedsamyeid/datacraft-studio/issues/new?template=bug_report.yml).
