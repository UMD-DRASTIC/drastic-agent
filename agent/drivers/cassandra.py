import os
from drivers.base import BaseDriver
from indigo.models.resource import Resource


class Cassandra(BaseDriver):

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
        # TODO: FIX ME!!!!! Iterating through all the resources won't
        # scale very well.
        total = 0
        total_size = 0
        min_size = 1000000
        max_size = 0
        for resource in Resource.objects.all():
            total += 1
            total_size += resource.size
            min_size = min(min_size, resource.size)
            max_size = max(max_size, resource.size)

        return total, total_size / total, max_size, min_size
