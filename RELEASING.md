# Publishing a release

The application is built in the private source repository. This public repository
contains the website, user documentation, issue tracker and release notes.

## Prepare

1. In the private source repository, run `build.bat --test` from one reviewed
   source commit. The script builds the portable application and both installers.
2. For a signed release, install a trusted code-signing certificate in the Windows
   certificate store and set `DATACRAFT_SIGNING_THUMBPRINT` before running the build.
   The existing build script signs and verifies the app executable and both
   installers. Keep the certificate and its credentials out of this repository
   and GitHub issue attachments. Without the thumbprint, the build is unsigned.
3. Verify the finished installers on a clean Windows machine:

   ```powershell
   Get-AuthenticodeSignature .\DataCraft-Studio-x64-setup.exe | Format-List Status,SignerCertificate
   Get-AuthenticodeSignature .\DataCraft-Studio-x64.msi | Format-List Status,SignerCertificate
   ```

   Both statuses must be `Valid`, and the certificate publisher must be the
   expected DataCraft publisher. If signing is not yet available, describe the
   installers as unsigned in the release notes; do not claim verified publisher
   identity.
4. Package the portable EXE with its runtime DLLs, then generate SHA-256 checksums **after** signing and packaging. Add all three artifacts to
   `releases/vX.Y.Z/SHA256SUMS.txt` and include the setup EXE hash in
   `RELEASE_NOTES.md`. Checksums detect differences from the files you published;
   they do not identify the publisher.
5. Add a new `releases/vX.Y.Z` folder, update the changelog and roadmap, then run:

   ```powershell
   python scripts/check_release_version.py
   python scripts/check_release_version.py --check
   ```

6. Review the website, README and guide against the actual build. In particular,
   confirm the screenshots, Free and Pro features, Windows requirements, and
   direct download filename.

## Publish

1. Create the GitHub release from the matching version tag.
2. Attach the signed EXE and MSI (or state clearly if unsigned), portable ZIP,
   and `SHA256SUMS.txt`. Use `RELEASE_NOTES.md` as the release description.
3. Check the release page and direct download link in a signed-out browser.
4. Download each asset and compare its hash with `SHA256SUMS.txt`.
5. Check that the GitHub Pages website displays the new version and links to the
   correct latest release.

Do not replace assets under an existing version tag. Publish a new patch release
if a binary or its notes need correction.
