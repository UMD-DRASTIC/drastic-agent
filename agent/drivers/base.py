__copyright__ = "Copyright (C) 2016 University of Maryland"
__license__ = "GNU AFFERO GENERAL PUBLIC LICENSE, Version 3"


class BaseDriver(object):

    def __init__(self, settings):
        self.settings = settings

    ################################################################
    # Metrics
    ################################################################
    def free_space(self):
        return 0

    def used_space(self):
        return 0

    def resource_info(self):
        count, size, max_size, min_size = [0, 0, 0, 0]
        return count, size, max_size, min_size
