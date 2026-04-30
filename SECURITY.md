# Security policy

## Reporting a vulnerability

If you've found a security issue in the code this template generates, or in
the template itself, please do **not** file a public issue. Instead, open
a private vulnerability report through GitHub's "Report a vulnerability"
button on the
[Security tab](https://github.com/apigear-io/template-python/security)
of this repo.

We aim to acknowledge new reports within five working days and to keep
reporters updated as we triage and fix the issue.

## Scope

This template generates Python code. Security issues that fall in scope:

- Generated code that introduces an injection, deserialization, or
  authorization vulnerability in a default-safe usage path.
- Templates that produce code with hard-coded secrets or
  insecure-by-default configuration.
- Build / generation steps that could be exploited via crafted input
  (e.g. a malicious `module.yaml`).

Out of scope:

- Vulnerabilities in third-party dependencies that this template only
  declares (`paho-mqtt`, `pydantic`, `olink-core`, …) — please report
  those upstream.
- Network-protocol limitations the docs explicitly call out (e.g. the
  MQTT feature ships without TLS, auth, or reconnect/backoff guidance —
  see `docs/docs/features/mqtt.md`).
- Issues that require an attacker to first compromise the developer's
  machine that runs `apigear generate`.

## Supported versions

Security fixes are issued for the **latest minor release** of this
template. Older releases do not receive backports. Tag a fixed version of
the template in your generation pipeline (see `engines.cli` in
`rules.yaml`) and watch this repo's releases page for new versions.
