# Release process

How to cut a new release of `template-python`.

This is an internal-maintainer document. Users don't need to read it.

## Versioning

This repo follows [Semantic Versioning](https://semver.org). The
template's version is the **git tag**; there is no `VERSION` file.

A reminder of what each bump means in this repo:

| Bump | Trigger | Examples |
|---|---|---|
| **MAJOR** | Removing a feature, or a backwards-incompatible change to the *generated code's* shape (class layout, public method signatures), or a wire-protocol bump that breaks interop with prior peers. | Removing the `http` feature. Renaming a generated class users imported. |
| **MINOR** | New features (new `feature:` entries in `rules.yaml`), additive changes to existing generated code, new optional fields in adapters. | Adding `on_ready` to MQTT adapters. New `requires:` declarations. |
| **PATCH** | Bug fixes that don't change the generated public surface. | Fixing a template bug that produced broken Python. Updating a hardcoded JSON serialization flag. |

When in doubt, prefer the larger bump and explain in the changelog.

## Cutting a release

1. **Confirm the work is final.**

   ```bash
   git status                  # working tree clean
   task py:test_goldenmaster   # full goldenmaster suite green
   task py:test_generated      # regenerated suite green
   task diff                   # goldenmaster matches templates
   ```

2. **Promote the `[Unreleased]` section in `CHANGELOG.md`.**

   - Replace the `## [Unreleased]` heading with `## [X.Y.Z] - YYYY-MM-DD`.
   - Add a fresh empty `## [Unreleased]` block above it for the next cycle.
   - Verify each entry reads as user-facing (not commit-formatted).

3. **Commit the changelog promotion.**

   ```bash
   git add CHANGELOG.md
   git commit -m "release: vX.Y.Z"
   ```

4. **Tag and push.**

   ```bash
   git tag vX.Y.Z
   git push origin main
   git push origin vX.Y.Z
   ```

5. **Create a GitHub release.** Either manually via the Releases page or:

   ```bash
   gh release create vX.Y.Z \
     --title "vX.Y.Z" \
     --notes-from-tag
   ```

   GitHub will surface the tag's annotated message and the changelog entry.

6. **Bump the apigear CLI floor in `rules.yaml`** if this release relies
   on a CLI feature newer than the current `engines.cli` floor. Most
   releases don't need this; only bump when you have a concrete reason.

7. **Notify the [template registry](https://github.com/apigear-io/template-registry)**
   if the registry tracks specific tags rather than `main`.

## What `task install` pins to

`Taskfile.yaml` pins the `apigear` CLI it installs via `APIGEAR_VERSION`.
Bump this when a new CLI release ships and you want CI (and local
contributors) to pick it up. Do not change it as part of cutting a
template release — they're independent decisions.

## Notes on backwards compatibility

- The wire protocol of `olink` is owned by
  [`apigear-io/objectlink-core-python`](https://github.com/apigear-io/objectlink-core-python).
  When that package's protocol version changes, **read its release notes
  before bumping the version pinned in `templates/scaffold/requirements.txt.tpl`**.
  A wire-incompatible olink-core bump in this template implies a MAJOR
  bump here too.
- The MQTT topic and payload conventions are owned by this template
  (and matched by sister templates like `template-cpp17`). A change to
  topic structure or payload encoding is a MAJOR bump.
- Removing a feature listed in `rules.yaml` is always a MAJOR bump —
  users with that feature in their solution YAML will see "feature not
  found".
