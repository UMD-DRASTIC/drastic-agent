"""
Iterate through all of the modules in the plugins folder
and check the plugin module to see if it can handle a
given resource
"""
__copyright__ = "Copyright (C) 2016 University of Maryland"
__license__ = "GNU AFFERO GENERAL PUBLIC LICENSE, Version 3"


import pkgutil
import importlib


def run_plugins(resource):
    ran = []
    for _, name, ispkg in pkgutil.iter_modules(['agent/plugins']):
        if not ispkg:
            continue

        try:
            print("Loading {} plugin".format(name))
            m = importlib.import_module("agent.plugins.{}.plugin".format(name))
            f = m.can_handle_resource(resource)
            if f:
                print(u"Running {} plugin".format(name))
                f(resource)
                ran.append(name)
        except Exception, e:
            # TODO: Log the loading problem
            print e

    return ran
