# Security policy

DataCraft Studio handles database credentials and data, so security reports get priority.

## Reporting a vulnerability

**Please don't report security issues in a public GitHub issue.**

Use GitHub's private reporting instead: go to the **Security** tab of this repository and
choose **Report a vulnerability**. Include:

- the DataCraft Studio version (Settings → About) and your Windows version;
- the data source involved, if any;
- steps to reproduce, and what an attacker could achieve.

You'll get an acknowledgement within 5 working days. We'll keep you updated while the issue
is fixed, and credit you in the release notes if you'd like.

## Supported versions

Only the latest release receives security fixes. Please update before reporting.

## Verifying downloads

Only download DataCraft Studio from this repository's
[Releases](https://github.com/elsayedsamyeid/datacraft-studio/releases) page. The installer SHA-256 is printed directly in each release's notes. Before you run it, check:

```powershell
Get-FileHash .\DataCraft-Studio-x64-setup.exe -Algorithm SHA256
```
