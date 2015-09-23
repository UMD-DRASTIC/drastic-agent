import os
import sys
from os.path import join, getsize
from drivers.base import BaseDriver


class Disk(BaseDriver):

    ################################################################
    # Metrics
    ################################################################
    def free_space(self):
        stats = os.statvfs(self.settings["ROOT"])
        return stats.f_frsize * stats.f_bavail

    def used_space(self):
        stats = os.statvfs(self.settings["ROOT"])
        size = stats.f_frsize * stats.f_blocks
        avail = stats.f_frsize * stats.f_bavail
        return size - avail

    def resource_info(self):
        total_size = 0
        total_count = 0
        max_size, min_size = 0, sys.maxint

        for root, dirs, files in os.walk(self.settings["ROOT"]):
            for name in files:
                sz = getsize(join(root, name))
                total_size += sz
                max_size = max(max_size, sz)
                if sz != 0:
                    min_size = min(min_size, sz)
            total_count += len(files)
        return total_count, total_size / total_count, max_size, min_size
