<!-- Import workspace-level CLAUDE.md configuration -->
<!-- See /home/lab/workspace/.claude/CLAUDE.md for complete rules -->

# Project-Specific Configuration

This file extends workspace-level configuration with project-specific rules.

## Project Context

**stellars_jupyterlab_extensions** - Python metapackage aggregating all Stellars JupyterLab extensions.

**Technology Stack**:
- Python >= 3.9
- JupyterLab >= 4.0.0
- Hatchling build system
- PyPI distribution

**Package Dependencies** (all Stellars extensions):
- jupyterlab_close_all_tabs_extension
- jupyterlab_doc_reader_extension
- jupyterlab_fit_image_size_extension
- jupyterlab_github_markdown_alerts_extension
- jupyterlab_makefile_file_type_extension
- jupyterlab_markdown_insert_content_extension
- jupyterlab_mmd_to_png_extension
- jupyterlab_notifications_extension
- jupyterlab_refresh_view_extension
- jupyterlab_tabular_data_viewer_extension
- jupyterlab_terminal_show_in_file_browser_extension
- jupyterlab_vscode_icons_extension
- jupyterlab_zip_extension

**Build Commands**:
- `make build` - Build the package
- `make install` - Install locally
- `make publish` - Publish to PyPI
