import psutil
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path)

# TODO: make the return type more decent. each dictionary item can be split in list and then use that list.


class DiskInfo:
    partitions = psutil.disk_partitions()
    details = {}
    factor = 1024

    def get_size(self, custom_bytes, suffix="B"):
        """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
        for unit in ["", "K", "M", "G", "T", "P"]:
            if custom_bytes < self.factor:
                return f"{custom_bytes:.2f}{unit}{suffix}"
            custom_bytes /= self.factor

    def get_disk_info(self):
        try:
            for partition in self.partitions:
                self.details[str(partition.device)+'device'] = partition.device
                self.details[str(partition.device)+'mountpoint'] = partition.mountpoint
                self.details[str(partition.device)+'file system type'] = partition.fstype
                try:
                    partition_usage = psutil.disk_usage(partition.mountpoint)
                except PermissionError:
                    continue
                self.details[str(partition.device)+'Total Size'] = self.get_size(partition_usage.total)
                self.details[str(partition.device)+'Used'] = self.get_size(partition_usage.used)
                self.details[str(partition.device)+'Free'] = self.get_size(partition_usage.free)
                self.details[str(partition.device)+'Percentage'] = self.get_size(partition_usage.percent)
        except Exception as e:
            print(e)
        finally:
            return self.details
