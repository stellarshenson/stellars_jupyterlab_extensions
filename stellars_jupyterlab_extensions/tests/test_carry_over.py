import os
from pathlib import Path

import pytest

from stellars_jupyterlab_extensions import carry_over_settings

OLD = "jupyterlab_foo_extension"
NEW = "@stellarshenson/jupyterlab-foo-extension"
FILE = "plugin.jupyterlab-settings"


@pytest.fixture
def settings(tmp_path):
    path = tmp_path / "settings"
    path.mkdir()
    return path


@pytest.fixture
def labextensions(tmp_path):
    path = tmp_path / "labextensions"
    path.mkdir()
    return path


def save(settings_dir, folder, text, name=FILE):
    path = settings_dir / folder / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


def install(labextensions_dir, name=NEW):
    path = labextensions_dir / name
    path.mkdir(parents=True)
    (path / "package.json").write_text("{}")


def test_copies_when_target_is_installed(settings, labextensions):
    save(settings, OLD, "saved")
    save(settings, OLD, "other", name="other.jupyterlab-settings")
    save(settings, OLD, "not settings", name="notes.txt")
    install(labextensions)
    assert carry_over_settings(settings, [labextensions]) == [
        settings / NEW / "other.jupyterlab-settings",
        settings / NEW / FILE,
    ]
    assert (settings / NEW / FILE).read_text() == "saved"
    assert not (settings / NEW / "notes.txt").exists()


def test_target_found_in_a_later_labextension_dir(settings, labextensions, tmp_path):
    save(settings, OLD, "saved")
    install(labextensions)
    assert carry_over_settings(settings, [tmp_path / "absent", labextensions]) == [settings / NEW / FILE]


def test_no_copy_when_target_is_not_installed(settings, labextensions):
    save(settings, OLD, "saved")
    assert carry_over_settings(settings, [labextensions]) == []
    assert not (settings / "@stellarshenson").exists()


def test_third_party_folder_is_ignored(settings, labextensions):
    save(settings, "@jupyterlab/shortcuts-extension", "scoped")
    save(settings, "@jupyterlab", "scoped, directly in the folder")
    save(settings, "jupyterlab_git", "unscoped")
    # This target proves the "@" rule: only that rule keeps the "@jupyterlab" folder out.
    install(labextensions, "@stellarshenson/@jupyterlab")
    assert carry_over_settings(settings, [labextensions]) == []
    assert not (settings / "@stellarshenson").exists()


def test_existing_target_file_is_not_overwritten(settings, labextensions):
    save(settings, OLD, "old")
    save(settings, NEW, "new")
    install(labextensions)
    assert carry_over_settings(settings, [labextensions]) == []
    assert (settings / NEW / FILE).read_text() == "new"


def test_old_file_stays(settings, labextensions):
    old = save(settings, OLD, "saved")
    install(labextensions)
    carry_over_settings(settings, [labextensions])
    assert old.read_text() == "saved"


def test_dashed_folder_beats_underscored(settings, labextensions, monkeypatch):
    save(settings, OLD, "underscored")
    save(settings, OLD.replace("_", "-"), "dashed")
    install(labextensions)
    # A filesystem can list the dashed folder first without the sort, so the listing is forced to underscored first.
    glob = Path.glob
    monkeypatch.setattr(Path, "glob", lambda self, pattern: sorted(glob(self, pattern), reverse=True))
    assert carry_over_settings(settings, [labextensions]) == [settings / NEW / FILE]
    assert (settings / NEW / FILE).read_text() == "dashed"


def test_second_run_copies_nothing(settings, labextensions):
    save(settings, OLD, "saved")
    install(labextensions)
    carry_over_settings(settings, [labextensions])
    assert carry_over_settings(settings, [labextensions]) == []


def test_missing_settings_dir_copies_nothing(tmp_path, labextensions):
    assert carry_over_settings(tmp_path / "absent", [labextensions]) == []


@pytest.mark.skipif(os.geteuid() == 0, reason="root reads a folder with no permissions")
def test_unreadable_folder_does_not_stop_the_others(settings, labextensions, caplog):
    unreadable = save(settings, "jupyterlab_a_extension", "a").parent
    save(settings, "jupyterlab_b_extension", "b")
    install(labextensions, "@stellarshenson/jupyterlab-a-extension")
    install(labextensions, "@stellarshenson/jupyterlab-b-extension")
    unreadable.chmod(0)
    try:
        copied = carry_over_settings(settings, [labextensions])
    finally:
        unreadable.chmod(0o755)
    assert copied == [settings / "@stellarshenson/jupyterlab-b-extension" / FILE]
    assert "jupyterlab_a_extension" in caplog.text
