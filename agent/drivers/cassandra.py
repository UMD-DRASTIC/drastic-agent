import os
from drivers.base import BaseDriver

class Cassandra(BaseDriver):
    pass


    ################################################################
    # Metrics
    ################################################################

    def free_space(self):
        stats = os.statvfs(self.settings["STORAGE_ROOT"])
        return stats.f_frsize * stats.f_bavail

    def used_space(self):
        stats = os.statvfs(self.settings["STORAGE_ROOT"])
        size = stats.f_frsize * stats.f_blocks
        avail = stats.f_frsize * stats.f_bavail
        return size - avail

    def resource_info(self):
        return 0, 0, 0, 0