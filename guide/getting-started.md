# Getting started

From download to your first query in a few minutes.

## 1. Install

Download from the [latest release](https://github.com/elsayedsamyeid/datacraft-studio/releases/latest):

| Package | Use it when |
| --- | --- |
| `DataCraft-Studio-x64-setup.exe` | You want the normal install. **Recommended.** |
| `DataCraft-Studio-x64.msi` | You deploy software with Group Policy or scripts. |
| `DataCraft-Studio-x64-portable.zip` | You can't install software. Extract it and run `DataCraft Studio.exe`. |

- **Requirements:** Windows 10 or 11, 64-bit.
- The installers include the Visual C++ runtime and install Microsoft WebView2 if it's missing.
- The **portable** package needs WebView2 to be present already (it is on Windows 11 and on
  up-to-date Windows 10). Keep every file in the extracted folder together—the app needs the
  DLLs beside it.
- If SmartScreen shows **Windows protected your PC**, [verify the checksum](troubleshooting.md#windows-protected-your-pc),
  then choose **More info → Run anyway**.

## 2. Add a connection

1. Open **Connections** from the navigation rail on the left.
2. Create a new connection and pick your data source.
3. Fill in the form. Each engine has its own fields—see [Connecting to your data](connecting.md).
4. **Test** the connection, then save it.

Passwords and API keys are saved to **Windows Credential Manager**, never to the profile file.

## 3. Explore

Open **Explorer** to browse databases, schemas, tables, views, columns, indexes and keys—or
collections, indices and inferred fields for document and search engines.

- Press <kbd>Enter</kbd> on a connection to connect or disconnect it.
- Press <kbd>F5</kbd> to refresh the selected item.
- Press <kbd>Shift</kbd>+<kbd>F10</kbd> (or right-click) for the actions available on an object.

Metadata is cached locally, so the tree and autocomplete are fast the next time.

## 4. Run a query

1. Press <kbd>Ctrl</kbd>+<kbd>T</kbd> to open a query tab for the active connection.
2. Write your query. Press <kbd>Ctrl</kbd>+<kbd>Space</kbd> for suggestions from the live
   schema.
3. Press <kbd>Ctrl</kbd>+<kbd>Enter</kbd> to run. If you've selected text, only the selection runs.

For data sources that support it, the **Run** button turns into **Stop** while a query is running.

## 5. Work with results

- Select cells to see **count, sum, average, min and max** in the status bar.
- Search within the loaded rows without re-running the query.
- Click a nested object or array to open it as formatted JSON.
- <kbd>Ctrl</kbd>+<kbd>C</kbd> copies the selection; <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>C</kbd> copies it with headers.
- Right-click to copy as **CSV, TSV, JSON or Markdown**.

## 6. Export

- **Export to a file** as **CSV** or **Excel (.xlsx)**.
- **Export a complete result set** that is too large for the grid. For data sources that
  support bulk reads, DataCraft streams the full source to disk in parts—CSV or NDJSON,
  optionally compressed with gzip or zstd—with a `manifest.json` describing the export.
  Large exports run in the background and can be paused, resumed or cancelled.

## Next steps

- Learn the [keyboard shortcuts](keyboard-shortcuts.md).
- Open the command palette with <kbd>Ctrl</kbd>+<kbd>K</kbd> to find anything.
- Need visual query building, history, import, migration or dashboards? See [Pro and accounts](pro-and-accounts.md).

[← User guide](README.md)
