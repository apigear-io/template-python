# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html);
commit messages follow [Conventional Commits](https://conventionalcommits.org).

## [Unreleased]

### Fixed

- MQTT: generated `__on_<op>_resp` sink handlers no longer raise
  `KeyError` on duplicate deliveries (QoS-2 retransmits, pytest
  teardown). The pending-call lookup now uses `pop(callId, None)`.

## [2.0.0] - 2026-04-30

### Removed

- **BREAKING — `http` feature.** It was non-functional (server adapter routed
  requests to Pydantic state models with no `impl` wiring; client dropped
  operation return values; class-name filters were inconsistent across
  `shared.py`, `routes.py`, and `client.py`) and lacked a cross-technology peer
  in other ApiGear templates. A future release may reintroduce HTTP — likely as
  HTTP + SSE so properties and signals can be modeled — designed around the
  `impl`-based service-adapter pattern that `olink` and `mqtt` use. Users with
  `features: [http]` in their solution YAML will now see the feature as
  unknown; remove the entry to migrate.

### Added

- MQTT: `on_ready` event on client and service adapters; fires once all
  required topic subscriptions have been confirmed by the broker.
- MQTT: subscription ID and message ID exposed on `subscribe_for_*` callbacks
  so user code can correlate operations with their adapters.
- MQTT: `on_disconnected` event hook on `BaseClient`; fires whenever paho's
  network loop detects a disconnect.
- olink: protocol bump to [`olink-core`
  v0.4.0](https://github.com/apigear-io/objectlink-core-python/releases/tag/v0.4.0)
  (safety hardening, per-instance state, always-send invoke reply, new
  `olink_unlinked` source method). Wire-compatible with v0.3.x peers.
- olink: generated sinks now expose `_set_` methods for read-only properties
  so `olink_on_init` can set their initial values from the server.

### Changed

- **MQTT: `clean_start=True` on every (re)connect**, plus an explicit
  re-subscribe loop in `__on_connect`. Subscriptions made before a transient
  TCP disconnect now survive paho-mqtt's auto-reconnect — previously they were
  silently dropped because the broker discarded the session and the on-connect
  handler didn't re-issue SUBSCRIBE. Mirrors the C++ template's reconnect
  lifecycle.
- Python floor standardized at **≥ 3.11** across docs, scaffold README, and
  CI. Goldenmaster CI matrix tests against 3.11, 3.12, and 3.13.
- CI workflows refreshed: `actions/checkout@v4`, `actions/setup-python@v5`,
  `actions/setup-go@v5`, `arduino/setup-task@v2`. Removes the soon-to-be-
  removed Node 16 runtime dependency.
- `apigear` CLI pinned to `v0.50.2` in `Taskfile.yaml` via an
  `APIGEAR_VERSION` variable, instead of tracking `@latest`.

### Fixed

- MQTT: latent positional-args bug in `client.connect_async()` — `clean_start`
  was being passed as `bind_port` (the boolean `False == 0` matched the
  default and hid it). Now uses keyword arguments; also unblocks
  `clean_start=True`.
- MQTT: reject `NaN`/`Inf` in JSON payloads via `allow_nan=False` so malformed
  values fail loudly rather than producing non-standard JSON literals.
- MQTT: array parameter handling in signal emission and array return-value
  unpacking on remote calls.
- MQTT: server adapter now removes its subscriptions on destruction.
- olink: generated code for sources with array properties no longer breaks
  Python parsing.
- Goldenmaster `requirements.txt` now lists `vector3d`, used by extern types.

### Documentation

- Filled in remaining `TBD` placeholders in the features overview for `api`,
  `scaffold`, `olink`, and `mqtt`.
- Sharpened the MQTT experimental caveat with an explicit gap list (no TLS,
  no auth/ACL guidance, minimal error handling, no reconnect/backoff strategy
  documented, no QoS strategy guidance) and a link to the issue tracker.
- Rewrote `templates/scaffold/README.md` (the README every generated project
  ships with) — Python ≥ 3.11 callout, project layout, run instructions per
  enabled feature, no empty headings, no broken links.
- Fixed folder-tree diagrams in quickstart and features overview
  (`implementation` → `impl`, removed `CMakeLists.txt` C++ leftover, added
  missing scaffold files).
- Reconciled `stubs` (legacy term) → `scaffold` (actual feature flag in
  `rules.yaml`).

### Internal / CI

- Added a session-scope pytest fixture in `templates/conftest.py` (raw,
  shipped only when the `mqtt` feature is enabled) that clears retained MQTT
  messages at session start. Eliminates the "passes in CI, fails locally on
  second run" pattern that came from broker state leaking across pytest
  invocations.
- Fixed duplicate `actions/checkout` step in all three workflows (a `@v3`
  call with submodules followed by a `@v4` call without — the second
  silently dropped the `apigear/test-apis` submodule).
- Removed unused org-level secrets (`WOLFGANG_REPO_PACKAGE_READ`,
  `APIGEAR_REPOS`) and `GOPRIVATE` from workflow envs. All dependencies are
  public; the auto-injected `GITHUB_TOKEN` is sufficient.
- Fixed `task ci` (referenced nonexistent task names: `test`, `py:install`,
  `py:test`).

## [1.0.0]

Initial stable release of the Python SDK template, providing `api`,
`scaffold`, `test_helpers`, `olink`, and `mqtt` features for generating
typed Python clients and servers from ApiGear interface descriptions. See
the [features overview](docs/docs/features/features.md) for what each
feature generates.
