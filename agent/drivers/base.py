


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
        count, size, max_size = 0, 0, 0
        return count, size, max_size

