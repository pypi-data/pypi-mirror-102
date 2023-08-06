import os
import platform
import aldemsubs.config as config


def test_initialize():

    cfg = config.ConfigHandler()

    assert all(cfg[key] == config.DEFAULTS[key] for key in cfg)
    assert cfg.keys() == config.DEFAULTS.keys()

    if os.name == 'posix':
        cfgpath = "./testconfig.ini"
    elif platform.system() == 'Windows':
        cfgpath = os.path.expandvars("%cd%\\testconfig_windows.ini")

    cfg = config.ConfigHandler(cfgpath)
    assert cfg.keys() == config.DEFAULTS.keys()
    assert not all(cfg[key] == config.DEFAULTS[key] for key in cfg)
    assert cfg["db_file_path"] == "/tmp/aldemsubstest.sqlite"
