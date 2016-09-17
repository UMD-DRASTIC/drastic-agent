__copyright__ = "Copyright (C) 2016 University of Maryland"
__license__ = "GNU AFFERO GENERAL PUBLIC LICENSE, Version 3"

from pkg_resources import iter_entry_points
from agent import config


def load(name):
    entry_point = list(iter_entry_points(group='drivers', name=name))
    if not entry_point:
        raise ImportError(u"No driver called {}".format(name))

    settings = config.get_driver_settings(name)
    constructor = entry_point[0].load()
    return constructor(settings)


def driver_list():
    return [ep.name for ep in iter_entry_points(group='drivers', name=None)]
