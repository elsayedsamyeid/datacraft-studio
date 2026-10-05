# Privacy

DataCraft Studio is built so your data stays yours. This page explains exactly what the app
stores, what it sends, and to whom.

**In short:** no telemetry, no analytics, no ads. Free needs no account and talks only to the
data sources you add. Pro sign-in shares the minimum needed to confirm your plan.

## What stays on your computer

| Data | Where |
| --- | --- |
| Connection profiles (host names, database names, options) | `%APPDATA%\DataCraft Studio` |
| Database passwords, API keys and AI provider keys | Windows Credential Manager |
| Query tabs, drafts, workspace, history | `%APPDATA%\DataCraft Studio` |
| Cached schema metadata for the explorer and autocomplete | `%APPDATA%\DataCraft Studio\metadata-cache` |
| Interface preferences | `%LOCALAPPDATA%\com.datacraft.studio` |
| Pro sign-in session (if you sign in) | Windows Credential Manager |
| Your account's display details and last plan check (if you sign in) | `%APPDATA%\DataCraft Studio\account-profile.json` |

None of this is uploaded anywhere.

## What the app sends, and to whom

### The data sources you configure

Queries and metadata requests go directly from your computer to the databases, search
clusters and files you connect to. DataCraft has no server in between.

### The DataCraft account service — only if you sign in

Signing in is optional and used only to unlock Pro. It uses an account service operated for
DataCraft by **Auth0 (Okta)**. Sign-in happens in your web browser on the account page, so the
DataCraft app never sees your password.

When you sign in, and when the app re-checks your plan, it sends and the account service stores:

- your email address, name and whether your email is verified;
- your plan (Free or Pro);
- an **anonymous device identifier** — a one-way hash of a random ID created on your computer.
  It contains no hardware serials, computer name or IP-derived information;
- for Pro licences, the date each device was first and last seen, and when the licence moved
  between devices.

This is used only to enforce one Pro licence per person. Your databases, queries, results and
connection details are **never** sent.

### The AI assistant — Pro, only if you use it

The AI assistant sends your prompt, and only the query, result or error context you choose to
include, **directly** to the model provider you configure (for example OpenAI or Anthropic),
using your own API key. That provider's privacy terms apply. DataCraft does not see or relay it.

## What DataCraft does not do

- No telemetry, crash reporting or usage analytics.
- No tracking of which features you use or which databases you open.
- No selling or sharing of account data.
- No automatic update checks in the current version; you download new releases yourself.

## Your choices

- **Use Free without an account.** Nothing is sent beyond your own data sources.
- **Sign out** from your profile with **Sign out this device**. This ends the session and removes
  the local sign-in data from this computer.
- **Delete your account data:** [open an issue](https://github.com/elsayedsamyeid/datacraft-studio/issues/new?template=pro_request.yml)
  asking for account deletion, with your email partly hidden (for example `s****@gmail.com`).
  Do not post your full email address.
- **Remove everything local:** uninstall the app, then delete `%APPDATA%\DataCraft Studio` and
  `%LOCALAPPDATA%\com.datacraft.studio`, and remove the DataCraft entries in Windows Credential
  Manager.

## Changes

If this changes, the new version is published here and noted in the
[changelog](CHANGELOG.md). The policy that applies is the one shipped with your version.
