"""
Configuration for the drastic agent.  Loads the agent.ini file specified
in AGENT_CONFIG and makes the values available to the server.
"""
__copyright__ = "Copyright (C) 2016 University of Maryland"
__license__ = "GNU AFFERO GENERAL PUBLIC LICENSE, Version 3"


import os


class Configuration(object):

    def __init__(self, *args, **kwargs):
        self.config = {}

        loc = os.environ.get(u"AGENT_CONFIG")
        if not loc:
            raise Exception(u"Unable to find AGENT_CONFIG env var")
        if not os.path.exists(loc):
            raise Exception(u"Unable to find the config file at '{}'".format(loc))

        execfile(loc, globals(), self.config)

    def get_driver_settings(self, name):
        return self.config.get(u'{}_CONFIG'.format(name.upper()), {})
