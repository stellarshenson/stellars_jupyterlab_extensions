<!-- Import workspace-level CLAUDE.md configuration -->
<!-- See /home/lab/workspace/.claude/CLAUDE.md for complete rules -->

# Project-Specific Configuration

This file extends workspace-level configuration with project-specific rules.

## Project Context

**stellars_jupyterlab_extensions** - Python metapackage aggregating all Stellars JupyterLab extensions.

**Technology Stack**:
- Python >= 3.10
- JupyterLab >= 4.0.0
- Hatchling build system
- PyPI distribution

**Package Dependencies** (30 Stellars extensions):
- jupyterlab_branding_extension
- jupyterlab_camunda_modeller_extension
- jupyterlab_colourful_tab_extension
- jupyterlab_doc_reader_extension
- jupyterlab_drawio_render_extension
- jupyterlab_export_markdown_extension
- jupyterlab_file_browser_sorting_extension
- jupyterlab_fit_image_size_extension
- jupyterlab_fold_all_code_extension
- jupyterlab_git_syntax_extension
- jupyterlab_github_markdown_alerts_extension
- jupyterlab_kernel_terminal_workspace_culler_extension
- jupyterlab_launcher_sections_extension
- jupyterlab_nb_venv_kernels_ui_extension
- jupyterlab_makefile_file_type_extension
- jupyterlab_markdown_insert_content_extension
- jupyterlab_mmd_to_png_extension
- jupyterlab_notifications_extension
- jupyterlab_open_in_terminal_extension
- jupyterlab_paste_content_as_markdown_extension
- jupyterlab_proxy_launcher_command_extension
- jupyterlab_refresh_view_extension
- jupyterlab_show_commands_reference_extension
- jupyterlab_tabular_data_viewer_extension
- jupyterlab_terminal_clipboard_extension
- jupyterlab_terminal_show_in_file_browser_extension
- jupyterlab_terraform_file_type_extension
- jupyterlab_trash_mgmt_extension
- jupyterlab_vscode_icons_extension
- jupyterlab_zip_extension

**Build Commands**:
- `make build` - Build the package
- `make install` - Install locally
- `make publish` - Publish to PyPI
