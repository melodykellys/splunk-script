# Security Policy

## Supported versions

This repository is a small demonstration project. Security fixes, if any, are
applied to the latest state of the default branch; no previous releases are
currently designated as supported.

## Reporting a vulnerability

Please do not report suspected vulnerabilities in a public issue. If private
vulnerability reporting is enabled for this GitHub repository, use its
**Report a vulnerability** feature. Otherwise, contact the repository
maintainer through a private channel listed on their GitHub profile.

Include a description of the issue, its impact, steps to reproduce it, and any
suggested mitigation. Please avoid including real credentials or other
sensitive data in the report. The maintainer will acknowledge the report and
coordinate any fix and disclosure with the reporter. Please allow reasonable
time for investigation and remediation before any public disclosure.

## Security considerations

This demo currently disables TLS certificate verification in `app.py` and
stores the HEC token in the source file. Do not use it with real credentials
or sensitive data as-is. See the [README](README.md) for setup and security
limitations.