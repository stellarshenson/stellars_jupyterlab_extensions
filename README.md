# Stellars JupyterLab Extensions

[![GitHub Actions](https://github.com/stellarshenson/stellars_jupyterlab_extensions/actions/workflows/build.yml/badge.svg)](https://github.com/stellarshenson/stellars_jupyterlab_extensions/actions/workflows/build.yml)
[![PyPI version](https://img.shields.io/pypi/v/stellars_jupyterlab_extensions.svg)](https://pypi.org/project/stellars_jupyterlab_extensions/)
[![Total PyPI downloads](https://static.pepy.tech/badge/stellars_jupyterlab_extensions)](https://pepy.tech/project/stellars_jupyterlab_extensions)
[![JupyterLab 4](https://img.shields.io/badge/JupyterLab-4-orange.svg)](https://jupyterlab.readthedocs.io/en/stable/)
[![Brought To You By KOLOMOLO](https://img.shields.io/badge/Brought%20To%20You%20By-KOLOMOLO-00ffff?style=flat)](https://kolomolo.com)

Metapackage that installs all Stellars JupyterLab extensions in one command. Because typing 30+ separate `pip install` commands was getting tedious, and copy-paste is a skill best reserved for StackOverflow answers.

## Installation

```bash
pip install stellars_jupyterlab_extensions
```

## Included Extensions

- **[jupyterlab_advanced_html_viewer_extension](https://github.com/stellarshenson/jupyterlab_advanced_html_viewer_extension)** - HTML viewer that trusts and refreshes a page as the built-in one does, with marks in six colours, comments and a notes panel stored in the HTML file itself; only text written in the file takes a comment
- **[jupyterlab_advanced_image_viewer_extension](https://github.com/stellarshenson/jupyterlab_advanced_image_viewer_extension)** - Interactive image viewer with wheel-zoom, drag-pan, and arrow-key folder navigation
- **[jupyterlab_advanced_markdown_viewer_extension](https://github.com/stellarshenson/jupyterlab_advanced_markdown_viewer_extension)** - Live Markdown preview: an open rendered document follows the file on disk without a reload, changes typed in on green, removed text shown red before it goes, a tab cue while changes arrive
- **[jupyterlab_advanced_paste_content_extension](https://github.com/stellarshenson/jupyterlab_advanced_paste_content_extension)** - Paste a screenshot or a file and it lands as a real file in the current folder, with the receiving surface given a reference to it instead of an inline blob - an image link in markdown, a quoted name in a code cell, the bare name in a terminal
- **[jupyterlab_ai_code_assistants_extension](https://github.com/stellarshenson/jupyterlab_ai_code_assistants_extension)** - AI code assistant side panels (Claude Code, Codex, Kimi, Gemini) behind one provider registry - sessions, forks, colours, and per-assistant launch modes; supersedes the standalone claude/codex/kimi extensions
- **[jupyterlab_basic_terminal_extension](https://github.com/stellarshenson/jupyterlab_basic_terminal_extension)** - Launch shell-less utility terminals that auto-close their tab when the underlying process exits
- **[jupyterlab_bookmarks_extension](https://github.com/stellarshenson/jupyterlab_bookmarks_extension)** - Bookmarks side panel for web pages, files and terminal sessions, with folders, tab-menu and drag-to-add, and a `jupyterlab-bookmarks` command line
- **[jupyterlab_branding_extension](https://github.com/stellarshenson/jupyterlab_branding_extension)** - Custom main area logo via server-side configuration
- **[jupyterlab_camunda_modeller_extension](https://github.com/stellarshenson/jupyterlab_camunda_modeller_extension)** - Model BPMN diagrams and open Camunda BPMN files
- **[jupyterlab_colourful_tab_extension](https://github.com/stellarshenson/jupyterlab_colourful_tab_extension)** - Assign pastel colours to tabs for visual identification
- **[jupyterlab_commands_extension](https://github.com/stellarshenson/jupyterlab_commands_extension)** - Commands reference tab with every command ID and its arguments, plus the `jupyterlab-commands` CLI that agents and scripts use to run allowed commands in the browser
- **[jupyterlab_core_patches_extension](https://github.com/stellarshenson/jupyterlab_core_patches_extension)** - All ten core patches in one extension, with one switch per patch in Settings that applies on the next reload, replacing the ten separate fix packages
- **[jupyterlab_device_bridge_extension](https://github.com/stellarshenson/jupyterlab_device_bridge_extension)** - Bridge serial (COM) ports and USB devices of the browser's computer into the JupyterLab container through Web Serial and WebUSB, so terminal programs and AI agents can program and read microcontroller boards
- **[jupyterlab_doc_reader_extension](https://github.com/stellarshenson/jupyterlab_doc_reader_extension)** - Open DOCX and RTF documents directly in JupyterLab
- **[jupyterlab_drag_and_drop_path_extension](https://github.com/stellarshenson/jupyterlab_drag_and_drop_path_extension)** - Drag a file or folder onto a terminal, Python file, or notebook to insert its path
- **[jupyterlab_drawio_render_extension](https://github.com/stellarshenson/jupyterlab_drawio_render_extension)** - View Draw.io diagrams directly in JupyterLab
- **[jupyterlab_edit_markdown_at_content_extension](https://github.com/stellarshenson/jupyterlab_edit_markdown_at_content_extension)** - Jump from rendered markdown preview into the editor at the exact line you were reading
- **[jupyterlab_export_markdown_extension](https://github.com/stellarshenson/jupyterlab_export_markdown_extension)** - Export markdown to PDF, DOCX, and HTML
- **[jupyterlab_export_svg_as_png_extension](https://github.com/stellarshenson/jupyterlab_export_svg_as_png_extension)** - Copy or export SVG graphics as high-quality PNG with configurable DPI and theme-aware rendering
- **[jupyterlab_file_browser_sorting_extension](https://github.com/stellarshenson/jupyterlab_file_browser_sorting_extension)** - LC_COLLATE=C (ASCIIbetical) sorting for file browser
- **[jupyterlab_fit_image_size_extension](https://github.com/stellarshenson/jupyterlab_fit_image_size_extension)** - Auto-scale images to fit view while preserving original size for smaller images
- **[jupyterlab_fold_all_code_extension](https://github.com/stellarshenson/jupyterlab_fold_all_code_extension)** - Fold/unfold all code cells in notebooks
- **[jupyterlab_git_syntax_extension](https://github.com/stellarshenson/jupyterlab_git_syntax_extension)** - Syntax highlighting for git configuration files (.gitignore, .gitmodules, .gitattributes, .gitconfig)
- **[jupyterlab_github_markdown_alerts_extension](https://github.com/stellarshenson/jupyterlab_github_markdown_alerts_extension)** - GitHub-style alert blocks in Markdown
- **[jupyterlab_kernel_terminal_workspace_culler_extension](https://github.com/stellarshenson/jupyterlab_kernel_terminal_workspace_culler_extension)** - Auto-cull idle kernels, terminals, and sessions
- **[jupyterlab_launcher_sections_extension](https://github.com/stellarshenson/jupyterlab_launcher_sections_extension)** - Custom section icons for launcher via YAML config
- **[jupyterlab_nb_venv_kernels_ui_extension](https://github.com/stellarshenson/jupyterlab_nb_venv_kernels_ui_extension)** - UI for nb_venv_kernels to navigate to kernel, register and unregister and scan for kernels
- **[jupyterlab_makefile_file_type_extension](https://github.com/stellarshenson/jupyterlab_makefile_file_type_extension)** - Makefile syntax highlighting and file type registration
- **[jupyterlab_markdown_insert_content_extension](https://github.com/stellarshenson/jupyterlab_markdown_insert_content_extension)** - Insert reusable content blocks with auto TOC generation
- **[jupyterlab_notifications_extension](https://github.com/stellarshenson/jupyterlab_notifications_extension)** - Secure API endpoint for JupyterLab notifications
- **[jupyterlab_open_in_terminal_extension](https://github.com/stellarshenson/jupyterlab_open_in_terminal_extension)** - Open folder in terminal via file browser context menu
- **[jupyterlab_passkey_extension](https://github.com/stellarshenson/jupyterlab_passkey_extension)** - Generic WebAuthn bridge exposing the browser's passkey to terminal and CLI clients on the Jupyter server
- **[jupyterlab_paste_content_as_markdown_extension](https://github.com/stellarshenson/jupyterlab_paste_content_as_markdown_extension)** - Paste clipboard content as markdown, converting HTML from web pages and documents
- **[jupyterlab_proxy_launcher_command_extension](https://github.com/stellarshenson/jupyterlab_proxy_launcher_command_extension)** - Launch jupyter-server-proxy via modal dialog
- **[jupyterlab_refresh_view_extension](https://github.com/stellarshenson/jupyterlab_refresh_view_extension)** - Refresh file content preserving scroll position
- **[jupyterlab_resource_monitor_extension](https://github.com/stellarshenson/jupyterlab_resource_monitor_extension)** - Cgroup-aware memory and CPU indicators in the status bar with a kernel usage panel, replacing `jupyter-resource-usage`
- **[jupyterlab_share_files_extension](https://github.com/stellarshenson/jupyterlab_share_files_extension)** - Side-panel shares (file drops) and requests (upload inboxes), link-shareable to any browser
- **[jupyterlab_tabular_data_viewer_extension](https://github.com/stellarshenson/jupyterlab_tabular_data_viewer_extension)** - Enhanced CSV/TSV, XLSX, Parquet viewer
- **[jupyterlab_terminal_clipboard_extension](https://github.com/stellarshenson/jupyterlab_terminal_clipboard_extension)** - Clipboard integration for terminal sessions via OSC 52 interception
- **[jupyterlab_terminal_show_in_file_browser_extension](https://github.com/stellarshenson/jupyterlab_terminal_show_in_file_browser_extension)** - Show terminal working directory in file browser
- **[jupyterlab_terraform_file_type_extension](https://github.com/stellarshenson/jupyterlab_terraform_file_type_extension)** - Terraform/HCL syntax highlighting and file type recognition
- **[jupyterlab_trash_mgmt_extension](https://github.com/stellarshenson/jupyterlab_trash_mgmt_extension)** - Trash panel with storage display, restore, and empty bin
- **[jupyterlab_voice_capture_extension](https://github.com/stellarshenson/jupyterlab_voice_capture_extension)** - Stream browser-captured microphone audio over an authenticated websocket to a server-side FIFO, exposing the mic to terminal apps in mic-less containers
- **[jupyterlab_vscode_icons_extension](https://github.com/stellarshenson/jupyterlab_vscode_icons_extension)** - VSCode file icons for JupyterLab file browser
- **[jupyterlab_workspace_manager_extension](https://github.com/stellarshenson/jupyterlab_workspace_manager_extension)** - Replace the Running Terminals and Kernels panel with one section per workspace: colour strip, purpose, age and counts, one section open at a time, with that workspace's tabs, terminals, kernels and language servers, plus the `jupyterlab-workspace` command
- **[jupyterlab_zip_extension](https://github.com/stellarshenson/jupyterlab_zip_extension)** - Archive compression and extraction in File Browser

## Galaxa Ecosystem Extensions

Extensions for labs that a GalaxaHub hub spawns. In any other lab they install without error and show nothing.

- **[jupyterlab_galaxahub_motd_extension](https://github.com/stellarshenson/jupyterlab_galaxahub_motd_extension)** - Message of the day tab with the user's welcome entries and the broadcasts sent to the user, which opens on lab start only when the hub has a message for the user

## Requirements

- JupyterLab >= 4.0.0
- Python >= 3.10
