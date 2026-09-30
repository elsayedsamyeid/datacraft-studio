<div align="center">

<img src="assets/brand-mark.svg" width="96" height="96" alt="DataCraft Studio">

# DataCraft Studio

### One workspace for every data source you use.

Explore, query and understand relational databases, document stores, search engines,<br>
spreadsheets and local files—in one native Windows app, without sending your data anywhere.

[![Download for Windows](https://img.shields.io/badge/Download-Windows%20x64-2563eb?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/elsayedsamyeid/datacraft-studio/releases/latest/download/DataCraft-Studio-x64-setup.exe)
&nbsp;
[![Latest release](https://img.shields.io/github/v/release/elsayedsamyeid/datacraft-studio?style=for-the-badge&label=Latest&color=0f172a)](https://github.com/elsayedsamyeid/datacraft-studio/releases/latest)
&nbsp;
[![Downloads](https://img.shields.io/github/downloads/elsayedsamyeid/datacraft-studio/total?style=for-the-badge&label=Downloads&color=0f172a)](https://github.com/elsayedsamyeid/datacraft-studio/releases)

**Free forever** · **No account for Free** · **No telemetry** · **11 data sources**

[Website](https://elsayedsamyeid.github.io/datacraft-studio/) ·
[User guide](guide/README.md) ·
[Free & Pro](#free-and-pro) ·
[Roadmap](ROADMAP.md) ·
[Support](SUPPORT.md) ·
[Privacy](PRIVACY.md)

<br>

<img src="assets/social-card.png" alt="The real DataCraft Studio Free and Pro workspaces shown side by side." width="1200">

</div>

<br>

> [!NOTE]
> **Official release repository.** Installers, documentation and issue tracking live here; the proprietary source code does not. Every release is published with SHA-256 checksums.

## Your first result

1. [Download the Windows installer](https://github.com/elsayedsamyeid/datacraft-studio/releases/latest/download/DataCraft-Studio-x64-setup.exe) and open DataCraft Studio. Free needs no account.
2. Add a PostgreSQL connection in **Connections** and choose **Test**. The [connection guide](guide/connecting.md) covers all eleven sources.
3. Open a query tab with **Ctrl+T**, run a query with **Ctrl+Enter**, then explore or export the result.

<a href="guide/getting-started.md"><img src="assets/screenshots/hero-results-light.png" alt="A PostgreSQL query and its result grid in DataCraft Studio" width="900"></a>

[Follow the first-query guide →](guide/getting-started.md)

## Why DataCraft Studio

| | |
| --- | --- |
| 🔌 **Connect broadly** | Eleven source types—SQL, NoSQL, search, analytical engines, spreadsheets and files—through one consistent connection flow. |
| 🧠 **Autocomplete that knows your engine** | Suggestions come from the live schema: native column types, aliases, procedures, MongoDB fields and Elasticsearch clauses. |
| 📊 **One grid for every shape of data** | Rows, documents, search hits and file lines land in the same grid with the same tools. |
| ⚡ **Native, not a JVM** | A Rust core and a native window. It starts like a desktop app and needs no Java runtime. |
| 🔒 **Private by design** | No telemetry. Free needs no account. Database passwords stay in Windows Credential Manager. |
| 🎯 **No dead buttons** | Each engine declares what it can do, and the interface shows only the actions that work. |

## Supported data sources

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?style=flat-square)
![MySQL / MariaDB](https://img.shields.io/badge/MySQL%20%2F%20MariaDB-00758F?style=flat-square&logo=mysql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-0F80CC?style=flat-square&logo=sqlite&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-FFC700?style=flat-square&logo=duckdb&logoColor=black)
![MongoDB](https://img.shields.io/badge/MongoDB-00A35C?style=flat-square&logo=mongodb&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?style=flat-square&logo=elasticsearch&logoColor=white)
![CSV](https://img.shields.io/badge/CSV%20files-16A34A?style=flat-square)
![Excel](https://img.shields.io/badge/Excel%20workbooks-15803D?style=flat-square)
![JSON](https://img.shields.io/badge/JSON%20files-334155?style=flat-square)
![Parquet](https://img.shields.io/badge/Parquet%20files-7C3AED?style=flat-square)

| Source | Kind | Source | Kind |
| --- | --- | --- | --- |
| **PostgreSQL** | Relational | **SQL Server** | Relational |
| **MySQL / MariaDB** | Relational | **SQLite** | Embedded relational |
| **DuckDB** | Analytical | **MongoDB** | Document |
| **Elasticsearch** | Search | **CSV files** | Delimited files |
| **Excel workbooks** | Spreadsheet | **JSON files** | Document files |
| **Parquet files** | Columnar files |  |  |

How to connect each one: [Connecting to your data](guide/connecting.md).

<img src="assets/providers-history.png" alt="DataCraft Studio showing its eleven-source connection picker and cross-provider Query History." width="1200">

## See it working

Every image here is the real application.

### Autocomplete that understands your engine

Completion follows the active connection and dialect—not a generic word list. It groups snippets, objects, columns and keywords, previews the selected item, and guides you through placeholders without leaving the keyboard.

<img src="assets/autocomplete-providers.png" alt="Four DataCraft Studio autocomplete panels showing SQL Server T-SQL, PostgreSQL SQL, MongoDB aggregation pipelines and Elasticsearch Query DSL." width="1200">

### One grid for every shape of data

- **Typed column headers**, straight from the engine
- **Selection aggregates**: count, sum, average, min and max as you select
- **Search within loaded results** without running the query again
- **Nested objects and arrays** shown inline, opened in a JSON viewer with one click
- **Export** to CSV or Excel, copy as CSV, TSV, JSON or Markdown, and stream complete large exports to disk

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/screenshots/json-viewer-dark.png">
  <img src="assets/screenshots/json-viewer-light.png" alt="A nested MongoDB profile object opened in the JSON viewer over the result grid.">
</picture>

### Visual query building, shaped to every engine *(Pro)*

SQL Server and PostgreSQL share a relational visual builder; Elasticsearch gets a Query DSL builder and MongoDB a document-first Find builder. Build visually, preview the generated query, then save or run it.

<img src="assets/query-builders.png" alt="Four DataCraft Studio Pro Query Builder panels showing SQL Server, PostgreSQL, Elasticsearch and MongoDB." width="1200">

<details>
<summary><b>More screenshots</b>: PostgreSQL, Elasticsearch, CSV</summary>
<br>

**PostgreSQL results**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/screenshots/hero-results-dark.png">
  <img src="assets/screenshots/hero-results-light.png" alt="PostgreSQL query results with typed headers.">
</picture>

**Elasticsearch hits**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/screenshots/results-elasticsearch-dark.png">
  <img src="assets/screenshots/results-elasticsearch-light.png" alt="Elasticsearch hits in the result grid.">
</picture>

**A folder of CSV files, queried like a database**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/screenshots/results-csv-dark.png">
  <img src="assets/screenshots/results-csv-light.png" alt="CSV file contents in the result grid.">
</picture>

</details>

## Download

### [Download DataCraft Studio for Windows →](https://github.com/elsayedsamyeid/datacraft-studio/releases/latest/download/DataCraft-Studio-x64-setup.exe)

| Package | Best for |
| --- | --- |
| [`DataCraft-Studio-x64-setup.exe`](https://github.com/elsayedsamyeid/datacraft-studio/releases/latest/download/DataCraft-Studio-x64-setup.exe) | **Most people.** Installs WebView2 if it's missing. |
| [`DataCraft-Studio-x64.msi`](https://github.com/elsayedsamyeid/datacraft-studio/releases/latest/download/DataCraft-Studio-x64.msi) | Managed or scripted installs. |
| [`DataCraft-Studio-x64-portable.zip`](https://github.com/elsayedsamyeid/datacraft-studio/releases/latest/download/DataCraft-Studio-x64-portable.zip) | Running without installing. Keep every file in the folder together. |

**Requirements:** Windows 10 or 11, 64-bit. The installers include the Visual C++ runtime—nothing else to install.

**Verify your download** against the SHA-256 in the release notes. This checks that the file matches the published release; it does not verify who published it. The v0.1.5 installers are not code signed.

Check the file hash in PowerShell:

```powershell
Get-FileHash .\DataCraft-Studio-x64-setup.exe -Algorithm SHA256
```

> Windows SmartScreen may warn about a new publisher. After checking the hash, choose **More info → Run anyway**.

## Quick start

1. **Install** and open DataCraft Studio.
2. **Add a connection** in **Connections**, fill in the form for your engine, and **test** it.
3. **Browse** databases, tables and fields in the **Explorer**.
4. **Query**: press <kbd>Ctrl</kbd>+<kbd>T</kbd> for a new tab, write a query, and press <kbd>Ctrl</kbd>+<kbd>Enter</kbd> to run it.

Full walkthrough: [Getting started](guide/getting-started.md) · Shortcuts: [Keyboard shortcuts](guide/keyboard-shortcuts.md)

## Free and Pro

**One app for everyone.** Use it free with no account. When you need visual building, durable workspaces and end-to-end data workflows, sign in with a DataCraft Pro account and Pro unlocks in the same app—no second installer, and your settings stay as they are.

<img src="assets/pro-workflows.png" alt="DataCraft Studio Pro showing the Workspace manager and Migration designer." width="1200">

| | Free | Pro *(on request)* |
| --- | :---: | :---: |
| All eleven data sources, unlimited connections | ✅ | ✅ |
| Metadata explorer and database search | ✅ | ✅ |
| Query editor with engine-aware autocomplete | ✅ | ✅ |
| Command palette | ✅ | ✅ |
| Result grid, JSON viewer, aggregates | ✅ | ✅ |
| Export to CSV and Excel, large streamed exports | ✅ | ✅ |
| Light and dark themes, system meters | ✅ | ✅ |
| Visual query builders for SQL, MongoDB and Elasticsearch | | ✅ |
| Query history and saved workspace | | ✅ |
| Guided data import wizard | | ✅ |
| Data migration between engines | | ✅ |
| Dashboards and provider health | | ✅ |
| AI assistant with your choice of model provider | | ✅ |

Free isn't a trial and has no time limit.

### How to get Pro

Pro is available on request while pricing is finalised.

1. In the app, open **Settings → Features → Plan** and choose **Sign in to unlock Pro**. Sign-in opens in your browser—DataCraft never sees your password. Create an account there if you need one, and verify your email.
2. [Open a Pro request](https://github.com/elsayedsamyeid/datacraft-studio/issues/new?template=pro_request.yml). Issues are public, so give your email partly hidden (for example `s****@gmail.com`).
3. Once Pro is enabled on your account, restart DataCraft Studio. **Settings → Features → Plan** shows **Pro**.

One computer at a time, works offline for up to three days between checks. Details: [Pro and accounts](guide/pro-and-accounts.md).

## Documentation

| Guide | What's inside |
| --- | --- |
| [Getting started](guide/getting-started.md) | Install, first connection, first query, export |
| [Connecting to your data](guide/connecting.md) | The connection form for each of the eleven sources |
| [Pro and accounts](guide/pro-and-accounts.md) | Signing in, the one-computer licence, offline use, signing out |
| [Keyboard shortcuts](guide/keyboard-shortcuts.md) | Editor, tabs, explorer, results and the command palette |
| [Troubleshooting](guide/troubleshooting.md) | Installer warnings, sign-in problems, resetting the app |

## FAQ

<details>
<summary><b>Is Free really free?</b></summary>
<br>
Yes. No time limit, no connection limit and no account. All eleven data sources are included, because a free tool that locks out your data isn't much use.
</details>

<details>
<summary><b>Do I need an account?</b></summary>
<br>
Not for Free. An account is only used to unlock Pro, and sign-in happens in your browser, so the app never sees your password.
</details>

<details>
<summary><b>Does DataCraft collect data about me?</b></summary>
<br>
No. There is no telemetry. Without an account, DataCraft only connects to the data sources you add. If you sign in for Pro, it also contacts the DataCraft account service to confirm your plan. See <a href="PRIVACY.md">PRIVACY.md</a>.
</details>

<details>
<summary><b>Where are my database passwords stored?</b></summary>
<br>
In Windows Credential Manager. They are never written to connection profiles or log files.
</details>

<details>
<summary><b>What about macOS and Linux?</b></summary>
<br>
Only Windows is published today. Watch this repository (<b>Watch → Custom → Releases</b>) to hear when other platforms ship. See the <a href="ROADMAP.md">roadmap</a>.
</details>

<details>
<summary><b>Is it open source?</b></summary>
<br>
No. DataCraft Studio is free to use but closed source. This repository publishes releases and documentation, and hosts the issue tracker. See <a href="LICENSE.md">LICENSE.md</a>.
</details>

## Support and feedback

- 📖 **How do I…?** Start with the [user guide](guide/README.md) and [troubleshooting](guide/troubleshooting.md).
- 🐛 **Found a bug?** [Open a bug report](https://github.com/elsayedsamyeid/datacraft-studio/issues/new?template=bug_report.yml)
- 💡 **Missing something?** [Request a feature](https://github.com/elsayedsamyeid/datacraft-studio/issues/new?template=feature_request.yml)
- ⭐ **Want Pro?** [Request Pro](https://github.com/elsayedsamyeid/datacraft-studio/issues/new?template=pro_request.yml)
- 🔐 **Security issue?** Report it privately—see [SECURITY.md](SECURITY.md)

If DataCraft Studio helps you, **star the repository**—it helps other developers find it.

---

<sub>© 2026 Sayed Masry. DataCraft Studio is free to use under the terms in <a href="LICENSE.md">LICENSE.md</a>. See also <a href="PRIVACY.md">PRIVACY.md</a> and <a href="CODE_OF_CONDUCT.md">CODE_OF_CONDUCT.md</a>. PostgreSQL, SQL Server, MySQL, MariaDB, SQLite, DuckDB, MongoDB, Elasticsearch, Excel and Parquet are trademarks of their respective owners; they are named only to identify the data sources DataCraft connects to, and no affiliation or endorsement is implied.</sub>
