# Claude Code Journal

This journal tracks substantive work on documents, diagrams, and documentation content.

---

1. **Task - Initialize project configuration**: Set up .claude directory with CLAUDE.md (project config) and JOURNAL.md, added KOLOMOLO badge to README.md, created .gitignore from extension template, created package structure with __init__.py to fix hatchling build<br>
    **Result**: Project now builds and installs successfully via `make install`

2. **Task - Add GitHub workflows**: Created `.github/workflows/build.yml` (multi-Python CI) and `check-links.yml` (documentation link checker), added GitHub Actions badge and self-deprecating humor to README<br>
    **Result**: CI infrastructure ready for GitHub

3. **Task - Add extension links and publish**: Added GitHub repository links to all 13 extensions in README, published v1.0.3 to PyPI<br>
    **Result**: Package live at https://pypi.org/project/stellars-jupyterlab-extensions/1.0.3/

4. **Task - Add new extensions**: Added jupyterlab_colourful_tab_extension, jupyterlab_export_markdown_extension, and jupyterlab_terraform_file_type_extension to metapackage (now 16 extensions total)<br>
    **Result**: Updated pyproject.toml dependencies and README with GitHub links

5. **Task - Bump Python requirement**: Changed minimum Python version from 3.9 to 3.10 due to jupyterlab_colourful_tab_extension requiring >=3.10<br>
    **Result**: Updated pyproject.toml, README, and CI workflow matrix

6. **Task - Add more extensions** (v1.0.10): Added jupyterlab_fold_all_code_extension and jupyterlab_launcher_navigate_to_kernel_extension to metapackage (now 18 extensions total)<br>
    **Result**: Published v1.0.10 to PyPI

7. **Task - Add drawio extension** (v1.0.13): Added jupyterlab_drawio_render_extension, temporarily disabled jupyterlab_launcher_navigate_to_kernel_extension<br>
    **Result**: Published v1.0.13 to PyPI with 18 active extensions

8. **Task - Re-enable launcher extension**: Re-enabled jupyterlab_launcher_navigate_to_kernel_extension<br>
    **Result**: Now 19 active extensions

9. **Task - Add new extensions** (v1.0.17): Added jupyterlab_file_browser_sorting_extension, jupyterlab_nb_venv_kernels_ui_extension, jupyterlab_trash_mgmt_extension; renamed launcher extension to nb_venv_kernels_ui<br>
    **Result**: Now 21 extensions total

10. **Task - Remove close_all_tabs extension** (v1.0.19): Removed jupyterlab_close_all_tabs_extension from metapackage<br>
    **Result**: Published v1.0.19 to PyPI with 20 extensions

11. **Task - Add show_commands_reference extension** (v1.0.21): Added jupyterlab_show_commands_reference_extension to metapackage<br>
    **Result**: Published v1.0.21 to PyPI with 21 extensions

12. **Task - Add launcher_sections extension** (v1.0.26): Added jupyterlab_launcher_sections_extension to metapackage<br>
    **Result**: Published v1.0.26 to PyPI with 23 extensions

13. **Task - Add camunda_modeller extension** (v1.0.34): Added jupyterlab_camunda_modeller_extension to metapackage<br>
    **Result**: Now 24 extensions total

14. **Task - Add six new extensions** (v1.0.40): Added jupyterlab_branding_extension, jupyterlab_git_syntax_extension, jupyterlab_open_in_terminal_extension, jupyterlab_paste_content_as_markdown_extension, jupyterlab_proxy_launcher_command_extension, and jupyterlab_terminal_clipboard_extension to metapackage<br>
    **Result**: Now 30 extensions total. Fixed stale extension count in README (13 -> 30), synced __init__.py version, updated .claude/CLAUDE.md with full extension list and Python >=3.10

15. **Task - Add drag_and_drop_path extension** (v1.0.46): Added jupyterlab_drag_and_drop_path_extension to metapackage<br>
    **Result**: Now 33 extensions total

16. **Task - Fix CI and bump minor version** (v1.1.0): Fixed GitHub Actions build workflow - replaced `pip install --dry-run` with `pkginfo` wheel metadata validation since dry-run fails resolving 33+ extension dependencies in CI. Bumped version from 1.0.51 to 1.1.0<br>
    **Result**: Build workflow should now pass. Added jupyterlab_edit_markdown_at_content_extension in same cycle

17. **Task - Repoint to consolidated AI assistants extension** (v1.1.5): Replaced claude/codex extension dependencies with `jupyterlab_ai_code_assistants_extension`, published v1.1.5 to PyPI<br>
    **Result**: Standalone `jupyterlab_claude_code_extension` and `jupyterlab_codex_extension` retired - superseded by `jupyterlab_ai_code_assistants_extension` 0.6.15, which consolidates Claude Code, Codex, Kimi and Gemini panels behind one provider registry (kimi was never listed here). Swapped the two deps in `pyproject.toml`, added README bullet naming the consolidated extension as superseding the standalones. Installing the metapackage now delivers one consolidated extension instead of per-assistant panels; standalone repos carry superseded notices in their READMEs.

18. **Task - Add the advanced Markdown viewer extension** (v1.1.6): Added `jupyterlab_advanced_markdown_viewer_extension` to the dependency list and the README catalogue<br>
    **Result**: **Trigger**: the extension reached its first release with the live preview complete - an open rendered Markdown document follows the file on disk without a reload, added text is typed in on a green background, removed text stands red before it is deleted, and the document tab carries a dot and a pulsing icon while changes arrive. Added the package name to `dependencies` in `pyproject.toml` in alphabetical order after the advanced image viewer, and a README bullet in the same position naming the repository and the behaviour. Installing the metapackage now delivers the live preview together with the other Markdown extensions it was surveyed against (edit-at-content, export, alerts, insert-content). No version pin: the metapackage tracks the latest release of every extension.

19. **Task - Add the advanced paste content extension** (v1.1.8): Added `jupyterlab_advanced_paste_content_extension` to the dependency list and the README catalogue<br>
    **Result**: **Trigger**: the extension reached its first public release, 1.0.1 on PyPI and npm. It is a frontend-and-server extension that intercepts a paste, writes the payload into the current folder as a real file, and hands the receiving surface a reference instead of an inline blob - an image link in markdown, a quoted name in a code cell so it drops into `plt.imread()`, the bare name in a text file or a terminal. The terminal branch resolves the shell's own working directory server-side from `/proc/<pid>/cwd` instead of using the folder of the last opened document. Added the package name to `dependencies` in `pyproject.toml` in alphabetical order after `jupyterlab_advanced_markdown_viewer_extension`, and a README catalogue bullet in the same position. No version pin: the metapackage tracks the latest release of every extension. Now 42 extensions, published as 1.1.8 to PyPI.

20. **Task - Add the advanced HTML viewer extension** (v1.1.9): Added `jupyterlab_advanced_html_viewer_extension` to the dependency list and the README catalogue<br>
    **Result**: **Trigger**: the extension reached its first public release, 1.0.1 on PyPI and npm. It is a frontend-and-server extension that opens `.html` files, trusts and refreshes a page as the built-in HTML Viewer does, and carries the marks, comments and notes panel of the advanced Markdown viewer, with the notes stored in the HTML file as comments so an AI agent reading the file reads and answers them. Only text written in the file takes a comment: script output, iframe, object and embed content is refused. Added the package name to `dependencies` in `pyproject.toml` in alphabetical order before `jupyterlab_advanced_image_viewer_extension`, and a README catalogue bullet in the same position. No version pin: the metapackage tracks the latest release of every extension. Now 43 extensions, published as 1.1.9 to PyPI.

21. **Task - Add the GalaxaHub motd extension in its own README section** (v1.1.9): Added `jupyterlab_galaxahub_motd_extension` to the dependency list and a new README section, Galaxa Ecosystem Extensions<br>
    **Result**: **Trigger**: the extension reached its first public release, 0.8.4 on PyPI and npm. It opens a Message of the day tab on lab start with the user's GalaxaHub welcome entries and the broadcasts sent to the user, and only when the hub holds a message for that user; without a hub it opens nothing. It is the first extension in the metapackage that needs a GalaxaHub hub, so the README gained a separate `## Galaxa Ecosystem Extensions` section after the general catalogue, with one sentence saying these extensions show nothing outside a hub-spawned lab. Package name added to `dependencies` in `pyproject.toml` in alphabetical order after `jupyterlab_fold_all_code_extension`. No version pin. Not published: the version stays 1.1.9 until a release is approved.

22. **Task [Short] - Publish with the GalaxaHub motd extension** (v1.1.10): Released the metapackage to PyPI as 1.1.10<br>
    **Result**: Ships entry 21: `jupyterlab_galaxahub_motd_extension` in `dependencies` (43 packages) and the Galaxa Ecosystem Extensions README section. Uploaded 2026-09-29 19:10 UTC from commit `cf2feb2`. No pins, so an install resolves the motd extension's current release, 0.8.10.

23. **Task - Add the device bridge extension** (v1.1.10): Added `jupyterlab_device_bridge_extension` to the dependency list and the README catalogue<br>
    **Result**: Requested on 2026-10-12, the day of the extension's first release. It bridges serial (COM) ports and USB devices of the browser's computer into the lab container through Web Serial and WebUSB, so terminal programs and AI agents program and read microcontroller boards. Package name added to `dependencies` in `pyproject.toml` in alphabetical order after `jupyterlab_colourful_tab_extension` (44 packages, no duplicates, the TOML parses), one bullet added to `README.md` under Included Extensions at the same position. No version pin. `pip index versions` shows 0.6.18 on PyPI, its only release, so an install resolves it. Its own README states that it is tested with simulated devices and with no physical board. Not published: the version stays 1.1.10 until a release is approved.

24. **Task [Short] - Publish with the device bridge extension** (v1.1.11): Released the metapackage to PyPI as 1.1.11<br>
    **Result**: Ships entry 23: `jupyterlab_device_bridge_extension` in `dependencies` (44 packages) and its README entry under Included Extensions. No pins, so an install resolves the device bridge's current release, 0.6.20.

25. **Task - Rename the commands extension dependency** (v1.1.12): Replaced `jupyterlab_show_commands_reference_extension` with `jupyterlab_commands_extension` and released the metapackage<br>
    **Result**: The commands reference extension was renamed on PyPI, npm and GitHub when it gained the `jupyterlab-commands` CLI, which lets agents and scripts run allowed JupyterLab commands in the browser; its first release under the new name is 1.0.16. The old name receives no further releases, so the metapackage had to depend on the new one. Updated `dependencies` in `pyproject.toml`, the README catalogue and the extension list in `.claude/CLAUDE.md`, and moved the entry to its alphabetical slot after `jupyterlab_colourful_tab_extension` in all three. The README bullet now names the CLI as well as the reference tab. No version pin, so an install resolves 1.0.16.

26. **Task - Add the workspace manager extension** (v1.1.13): Added `jupyterlab_workspace_manager_extension` to the dependency list and the README catalogue<br>
    **Result**: Requested 2026-10-25, the day the extension's blue-first palette was pushed as `1f5e6dc` at version 0.8.18. It replaces the Running Terminals and Kernels panel with one accordion section per workspace - colour strip, optional purpose, age and counts, that workspace's tabs, terminals, kernels and language servers - and ships the `jupyterlab-workspace` CLI. Package name added to `dependencies` in alphabetical order after `jupyterlab_vscode_icons_extension` (45 packages, no duplicates, the TOML parses), one README bullet at the same position. No version pin. `pip index versions` shows 0.8.17 on PyPI and npm, so an install resolves 0.8.17; 0.8.18 is committed but never published.

27. **Task - Changelog added, lint made real** (v1.1.13): Added `CHANGELOG.md` and ran ruff, closing the two SKIP rows of the 1.1.13 release report<br>
    **Result**: The metapackage kept no changelog, so the 1.1.13 report skipped that step; `CHANGELOG.md` now carries the 1.1.13 section and the Keep a Changelog header. Ruff was absent from the machine, so 0.17.2 went into `~/.local`; `ruff format --check` reports the files already formatted and `ruff check` passes with no findings. No new PyPI version: a changelog does not ship in the wheel, so republishing would add nothing for an install. Then rebuilt it retroactively from the 33-commit history: 25 sections from 1.0.41, the repository's first commit, through 1.1.13, each dependency change read from the `pyproject.toml` diff at that commit, and the publish-only or metadata bumps marked as Publish.

28. **Task - Add the bookmarks extension** (v1.1.14): Added `jupyterlab_bookmarks_manager_extension` to the dependency list and the README catalogue, released the metapackage<br>
    **Result**: Requested 2026-10-29. The extension puts web pages, files and terminal sessions into one side panel of four sections - Links, Files, Sessions and Recent Proxy - with folders, adding a tab from its context menu or by dragging it onto the panel, a ribbon on a bookmarked tab, and the `jupyterlab-bookmarks` CLI. Added the package to `dependencies` alphabetically after `jupyterlab_basic_terminal_extension` (46 packages, no duplicates, the TOML parses) and one README bullet at the same position. No version pin: `jupyterlab_bookmarks_manager_extension` 0.7.78 is on PyPI, so an install resolves it. Also added the 1.1.14 section to the uncommitted `CHANGELOG.md`, which entered the same commit. Published to PyPI as 1.1.14.

29. **Task - Settings carry-over to scoped ids** (v1.1.15): Added a server extension that copies saved settings from the old extension ids to the scoped `@stellarshenson` ids at server start<br>
    **Result**: Scoped npm names change every plugin id, so settings saved under `jupyterlab_foo_extension` stop applying after the upgrade. `carry_over_settings` in `stellars_jupyterlab_extensions/__init__.py` copies `*.jupyterlab-settings` files to `@stellarshenson/jupyterlab-foo-extension` once that extension's `package.json` exists in a labextensions folder, so the extensions can release in any order. It never overwrites a file in the scoped folder and leaves old files, so a downgrade finds them; a failure logs a warning and the server starts. `jupyter-config/server-config/` and `pyproject.toml` shared-data enable it; `build.yml` runs `pytest --pyargs` from the installed wheel. Verified by run `wf_f8a671f0-b37`, recorded in `/home/lab/workspace/private/jupyterlab/tmp/workflows/settings-carry-over/`: `verify-2.json` verdict pass, 10 of 10 tests, the JupyterLab settings API returned the carried value. Work is in the working tree: not committed, not pushed, not released.

30. **Task - Require Python 3.12** (v1.1.17): raised the minimum Python to 3.12 on the owner's decision<br>
    **Result**: `requires-python` in `pyproject.toml` moved to `>=3.12`, the classifiers for Python 3.10 and 3.11 are removed, and the `build.yml` matrix runs only Python 3.12. The extensions this metapackage installs declare the same minimum, so on an older Python pip would otherwise install this package with extensions from before the scoped npm rename. The version floors of its dependencies are not changed.
