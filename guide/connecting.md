# Connecting to your data

Every data source uses the same flow: open **Connections**, create a connection, pick the
source, fill in its form, **test**, and save. The form adapts to the engine, so you only see
fields that apply. Fields marked **required** must be filled in; everything else has a sensible
default.

Passwords, API keys and other secrets go to **Windows Credential Manager**, never to the
connection profile.

**Jump to:** [PostgreSQL](#postgresql) · [SQL Server](#sql-server) · [MySQL / MariaDB](#mysql--mariadb) ·
[SQLite](#sqlite) · [DuckDB](#duckdb) · [MongoDB](#mongodb) · [Elasticsearch](#elasticsearch) ·
[CSV files](#csv-files) · [Excel, JSON and Parquet files](#excel-json-and-parquet-files)

---

## Databases

### PostgreSQL

| Field | Notes |
| --- | --- |
| **Host** *(required)* | Server name or IP address |
| **Port** *(required)* | Usually `5432` |
| **Database** *(required)* | The database to open |
| **Username** *(required)* | |
| Password | Stored in Credential Manager |
| **SSL mode** *(required)* | Match your server's TLS requirement |
| Root certificate | For verifying a server certificate signed by your own CA |
| Connection timeout, query timeout | In milliseconds |
| Minimum and maximum pool size | Connections kept open for this profile |
| Application name | Shown to the server, for example in `pg_stat_activity` |

### SQL Server

| Field | Notes |
| --- | --- |
| **Server** *(required)* | Server name or IP address |
| **Port** *(required)* | Usually `1433` |
| **Database** *(required)* | |
| **Authentication** *(required)* | How to sign in to the server |
| **Login** *(required)* | |
| Password | Stored in Credential Manager |
| Encrypt connection | Turn on when the server requires encryption |
| Trust server certificate | Only for servers with self-signed certificates you trust |
| Application name | Shown to the server |
| Query timeout | In milliseconds |

### MySQL / MariaDB

| Field | Notes |
| --- | --- |
| **Host** *(required)* | Defaults to `localhost` |
| **Port** *(required)* | Usually `3306` |
| **Database** *(required)* | |
| **Username** *(required)* | |
| Password | Negotiates `caching_sha2_password` or `mysql_native_password` with the server |
| **TLS mode** *(required)* | Defaults to verifying the server's certificate and host name |
| CA certificate | Shown when the TLS mode verifies the certificate |
| Connection timeout | Default 10 seconds |
| Query timeout | Default 60 seconds |
| Pool size | Connections kept open for this profile |

### SQLite

| Field | Notes |
| --- | --- |
| **Database file** *(required)* | For example `D:\data\app.sqlite` |
| Create when missing | Create a new, empty database if the file doesn't exist |

No user name or password—SQLite is a local file.

### DuckDB

| Field | Notes |
| --- | --- |
| **Database file** *(required)* | For example `D:\data\analytics.duckdb` |
| Create when missing | Create a new, empty database if the file doesn't exist |
| Worker threads | Default 4 |

No user name or password—DuckDB runs inside DataCraft.

---

## Document and search engines

### MongoDB

| Field | Notes |
| --- | --- |
| **Connection URI** *(required)* | For example `mongodb://host:27017` or a `mongodb+srv://` URI |
| Authentication database | Often `admin` |
| Username, password | Leave empty for servers without authentication |
| Replica set | Name of the replica set, if any |
| Read preference | Which members queries may read from |
| Use TLS, CA certificate | For encrypted connections |
| Connection timeout, operation timeout | In milliseconds |
| Maximum pool size | |

### Elasticsearch

| Field | Notes |
| --- | --- |
| **Endpoint** *(required)* | For example `https://localhost:9200` |
| Default index or alias | Opened by default in the editor |
| **Authentication** *(required)* | User name and password, API key, or Elastic Cloud ID |
| Verify TLS certificate | Keep on unless you use a certificate you trust but can't verify |
| CA certificate | For clusters signed by your own CA |
| Request timeout | In milliseconds |

---

## Files

File sources need no server, user name or password. Point DataCraft at a **folder** and every
matching file in it appears as a table you can query with SQL.

### CSV files

| Field | Notes |
| --- | --- |
| **Folder** *(required)* | Every `.csv`, `.tsv`, `.psv` and `.txt` file becomes an object |
| First row is a header | On by default |
| Delimiter | Comma, semicolon, tab or pipe |
| Quote character | Default `"` |
| Encoding | UTF-8, UTF-8 with BOM, Windows-1252 or ISO-8859-1 |
| Rows sampled for type inference | Default 1,000 (10–100,000). More rows infer column types more accurately but open files more slowly |

CSV folders support **writes** and **complete large exports**.

### Excel, JSON and Parquet files

| Source | Files included |
| --- | --- |
| **Excel workbooks** | `.xlsx`, `.xlsm`, `.xlsb`, `.xls`, `.ods` |
| **JSON files** | `.json`, `.jsonl`, `.ndjson` |
| **Parquet files** | `.parquet` |

| Field | Notes |
| --- | --- |
| **Folder** *(required)* | Every matching file in the folder becomes an object |
| Rows sampled for type inference | Default 1,000 (10–100,000) |

These sources are **read-only**. Column types are inferred from the data, and each column
shows that its type was inferred.

---

## Tips

- **Test before saving.** The test tells you whether the host, credentials and TLS settings work.
- **Timeouts** are the safety net for engines where a running query can't be stopped from the app.
- Connection problems? See [Troubleshooting → Connections](troubleshooting.md#connections).

[← User guide](README.md)
