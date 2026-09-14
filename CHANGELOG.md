# Changelog

All notable changes to DataCraft Studio are listed here.
Downloads for every version are on the [Releases](https://github.com/elsayedsamyeid/datacraft-studio/releases) page.

## [0.1.5] — 2026-09-15

First public release.

### Included

- **Eleven data sources:** PostgreSQL, SQL Server, MySQL / MariaDB, SQLite, DuckDB, MongoDB,
  Elasticsearch, CSV, Excel, JSON and Parquet. Unlimited connections.
- **Connections:** a connection form built for each engine, with connection testing.
  Passwords are stored in Windows Credential Manager.
- **Explorer:** browse databases, schemas, tables, columns, indexes and keys, or collections
  and inferred fields. Metadata is cached locally.
- **Query editor:** multiple query tabs with autocomplete based on the live schema, including
  alias scope, native column types and function signatures.
- **Result grid:** typed column headers, search within results, selection aggregates,
  density and column controls, paging, and a JSON viewer for nested values.
- **Export:** CSV and Excel files; copy as CSV, TSV, JSON or Markdown; complete large exports
  streamed to disk as CSV or NDJSON, optionally compressed.
- **Command palette** to find commands, connections and tables.
- **Header system meters** for CPU, memory, disk and network activity.
- Light and dark themes.
- **Optional sign-in:** Free needs no account. Signing in with a DataCraft Pro account
  unlocks Pro features in the same app. A Pro licence covers one computer at a time and works
  offline for up to three days between checks.

### Packages

- One Windows x64 installer (`.exe`) for everyone — Free and Pro are the same app.
- An `.msi` installer and a portable `.zip` for managed or no-install use.
- The installers include the app-local Visual C++ runtime and install WebView2 if it is missing.

[0.1.5]: https://github.com/elsayedsamyeid/datacraft-studio/releases/tag/v0.1.5
