# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Reconstructed from the repository history on 2026-10-26. Releases before 1.0.41 have no record in this repository. Versions whose only change was a publish or metadata bump, with no change to the dependency list, are listed as Publish.

## [1.1.16] - 2026-10-30

### Added

- Settings carry-over - at server start, a server extension copies saved settings from the old folder of each renamed extension (`jupyterlab_foo_extension`) to its scoped folder (`@stellarshenson/jupyterlab-foo-extension`) once the scoped extension is installed; it never overwrites a file in the scoped folder and it leaves the old files in place

## [1.1.14] - 2026-10-29

### Added

- `jupyterlab_bookmarks_manager_extension` - bookmarks side panel for web pages, files and terminal sessions, with folders, tab-menu and drag-to-add, and the `jupyterlab-bookmarks` command line

### Notes

- The dependency is unpinned, so an install resolves the extension's latest published release, 0.7.78

## [1.1.13] - 2026-10-25

### Added

- `jupyterlab_workspace_manager_extension` - replaces the Running Terminals and Kernels panel with one accordion section per workspace, carrying that workspace's tabs, terminals, kernels and language servers, and ships the `jupyterlab-workspace` command

### Notes

- The dependency is unpinned, so an install resolves the extension's latest published release, 0.8.17

## [1.1.12] - 2026-10-19

### Changed

- `jupyterlab_show_commands_reference_extension` replaced by `jupyterlab_commands_extension`, which carries the `jupyterlab-commands` CLI; the old name receives no further releases

## [1.1.11] - 2026-10-12

### Added

- `jupyterlab_device_bridge_extension` - browser serial ports and USB devices inside the lab container

## [1.1.10] - 2026-09-29

### Added

- `jupyterlab_galaxahub_motd_extension` - message of the day tab for labs spawned by a GalaxaHub hub

## [1.1.9] - 2026-09-28

### Added

- `jupyterlab_advanced_html_viewer_extension` - HTML viewer with marks, comments and a notes panel stored in the file

## [1.1.8] - 2026-09-21

### Added

- `jupyterlab_advanced_paste_content_extension` - writes a pasted screenshot or file into the current folder and hands the receiving surface a reference to it

## [1.1.7] - 2026-09-06

### Publish

- Republished after the 1.1.6 catalogue update, with no change to the dependency list

## [1.1.6] - 2026-09-06

### Added

- `jupyterlab_advanced_markdown_viewer_extension` - live Markdown preview that follows the file on disk and marks inserted and removed text

## [1.1.5] - 2026-08-08

### Changed

- `jupyterlab_claude_code_extension` and `jupyterlab_codex_extension` replaced by `jupyterlab_ai_code_assistants_extension`, which consolidates the assistant panels behind one provider registry

## [1.1.4] - 2026-07-25

### Added

- `jupyterlab_codex_extension` - Codex panel, later superseded by the consolidated assistants extension
- `jupyterlab_resource_monitor_extension` - cgroup-aware memory and CPU indicators with a kernel usage panel

## [1.1.3] - 2026-07-22

### Removed

- `jupyterlab_mermaid_latest_extension` - removed after repeated trouble, one day after it was added

## [1.1.2] - 2026-07-15

### Added

- `jupyterlab_passkey_extension` - WebAuthn bridge that exposes the browser's authenticator to terminals, scripts and AI agents

## [1.1.1] - 2026-06-10

### Publish

- Published the 1.1.0 build, with no change to the dependency list

## [1.1.0] - 2026-06-10

### Changed

- The GitHub Actions build workflow validates the built wheel's metadata with `pkginfo` instead of `pip install --dry-run`, which could not resolve the full dependency list in CI

## [1.0.51] - 2026-06-09

### Added

- `jupyterlab_voice_capture_extension` - browser microphone audio over an authenticated websocket to a server-side FIFO

## [1.0.50] - 2026-06-01

### Added

- `jupyterlab_edit_markdown_at_content_extension` - jump from the rendered Markdown into the editor at the line being read

## [1.0.49] - 2026-05-31

### Added

- `jupyterlab_advanced_image_viewer_extension` - image viewer with zoom, pan and arrow-key navigation

## [1.0.48] - 2026-05-29

### Added

- `jupyterlab_mermaid_latest_extension` - latest Mermaid renderer

## [1.0.47] - 2026-05-28

### Added

- `jupyterlab_share_files_extension` - shares and upload requests from a side panel

## [1.0.46] - 2026-05-24

### Added

- `jupyterlab_drag_and_drop_path_extension` - drag a file or folder onto a terminal, Python file or notebook to insert its path

## [1.0.45] - 2026-05-05

### Publish

- Package metadata updated after the 1.0.44 publish, with no change to the dependency list

## [1.0.44] - 2026-04-30

### Added

- `jupyterlab_claude_code_extension` - Claude Code panel, later superseded by the consolidated assistants extension
- `jupyterlab_basic_terminal_extension` - shell-less utility terminals that close their tab when the process exits

## [1.0.43] - 2026-04-16

### Publish

- Post-publish bump after 1.0.42, with no change to the dependency list

## [1.0.42] - 2026-04-16

### Added

- `jupyterlab_export_svg_as_png_extension` - copy or export SVG graphics as PNG

### Removed

- `jupyterlab_mmd_to_png_extension` - replaced by the SVG export extension

## [1.0.41] - 2026-04-04

### Added

- The dependency set first recorded in this repository: 30 extensions, from `jupyterlab_branding_extension` to `jupyterlab_zip_extension`, including `jupyterlab_mmd_to_png_extension` and the old `jupyterlab_show_commands_reference_extension` name
