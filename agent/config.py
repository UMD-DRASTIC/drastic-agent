"""
Configuration for the indigo agent.  Loads the agent.ini file specified
in AGENT_CONFIG and makes the values available to the server.
"""
import os
import sys

class Configuration(object):

    def __init__(self, *args, **kwargs):
        self.config = {}

        loc = os.environ.get(u"AGENT_CONFIG")
        if not loc:
            raise Exception(u"Unable to find AGENT_CONFIG env var")
        if not os.path.exists(loc):
            raise Exception(u"Unable to find the config file at '{}".format(loc))

        execfile(loc, globals(), self.config)

    def get_driver_settings(self, name):
        return self.config.get(u'{}_CONFIG'.format(name.upper()), {})