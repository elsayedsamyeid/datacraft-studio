## DataCraft Studio 0.1.5 — Free edition

The first public release. A native Windows database studio for **PostgreSQL, SQL Server, MongoDB, Elasticsearch and CSV files**, with one explorer, one editor and one result grid. Free, no account.

### ⬇️ Which file do I need?

| File | Best for |
| --- | --- |
| **DataCraft-Studio-x64-setup.exe** | Most people. A standard installer |
| **DataCraft-Studio-x64.msi** | IT-managed machines and silent deployment |
| **DataCraft-Studio-x64-portable.zip** | No install. Extract the whole folder and run `DataCraft Studio.exe` |

Requires Windows 10 or 11, 64-bit.

### ✨ What's included

- **All five engines** with unlimited connections
- **Explorer** for schemas, tables, columns, indexes and keys, or collections and fields
- **Query editor** with autocomplete based on your live schema: alias scope, native types, function signatures
- **Result grid** with typed headers, search in results, selection aggregates, a JSON viewer for nested documents, and paging
- **Export** to CSV, JSON and the clipboard
- **Passwords in Windows Credential Manager**, never in profile files
- Header system meters, plus light and dark themes

### 🔐 Verify your download

```powershell
Get-FileHash .\DataCraft-Studio-x64-setup.exe -Algorithm SHA256
```

Compare the result with `SHA256SUMS.txt` attached below. If Windows SmartScreen warns about a new publisher, choose **More info → Run anyway** once the hash matches.

---

Found a bug? [Open an issue](https://github.com/elsayedsamyeid/datacraft-studio/issues/new?template=bug_report.yml).
