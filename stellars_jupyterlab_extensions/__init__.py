"""Stellars JupyterLab Extensions metapackage.

Installs all Stellars JupyterLab extensions as dependencies, and copies saved
settings from the old extension ids to the scoped ids at server start.
"""

import logging
import os
import shutil
from pathlib import Path

__version__ = "1.1.16"

log = logging.getLogger(__name__)


def carry_over_settings(settings_dir, labextension_dirs):
    """Copy saved settings of installed renamed extensions to the scoped id and return the new files."""
    settings_dir = Path(settings_dir)
    copied = []
    # Sorted order puts a dashed folder before an underscored one, and "-" names are the newer id, so the dashed copy wins.
    for folder in sorted(settings_dir.glob("[!@]*")):
        target = "@stellarshenson/" + folder.name.replace("_", "-")
        if not any(os.path.exists(os.path.join(d, target, "package.json")) for d in labextension_dirs):
            continue
        try:
            # listdir, because pathlib's glob hides an unreadable folder instead of raising OSError.
            for name in sorted(os.listdir(folder)):
                destination = settings_dir / target / name
                if name.endswith(".jupyterlab-settings") and not destination.exists():
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(folder / name, destination)
                    copied.append(destination)
        except OSError as error:
            log.warning("Settings carry-over failed for %s: %s", folder, error)
    return copied


def _jupyter_server_extension_points():
    return [{"module": "stellars_jupyterlab_extensions"}]


def _load_jupyter_server_extension(server_app):
    from jupyter_core.paths import jupyter_path

    # No failure here may stop the server, even with reraise_server_extension_failures set.
    try:
        # The linked LabApp trait holds c.LabApp.user_settings_dir, else JUPYTERLAB_SETTINGS_DIR, else <config dir>/lab/user-settings.
        lab = server_app.extension_manager.extension_points["lab"].app
        for path in carry_over_settings(lab.user_settings_dir, jupyter_path("labextensions")):
            server_app.log.info("Carried over saved settings to %s", path)
    except Exception as error:
        server_app.log.warning("Settings carry-over skipped: %r", error)
