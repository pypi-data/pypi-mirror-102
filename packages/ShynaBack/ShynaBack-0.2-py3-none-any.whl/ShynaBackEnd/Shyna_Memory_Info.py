import psutil
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path)

# TEST
# NOTE: did some changes to get_size method and would like to implement same in other classes as well
# Suggestion: Make a class for get_size method because conversion may need multiple time.


class MemoryInfo:
    system_memory = psutil.virtual_memory()
    swap_memory = psutil.swap_memory()
    details = {}
    factor = 1024

    def get_memory_info(self):
        try:
            self.details["Total Virtual"] = self.get_size(self.system_memory.total)
            self.details["Available Virtual"] = self.get_size(self.system_memory.available)
            self.details["Used Virtual"] = self.get_size(self.system_memory.used)
            self.details["Percentage Virtual"] = self.get_size(self.system_memory.percent)
            self.details["Total swap_memory"] = self.get_size(self.swap_memory.total)
            self.details["Free swap_memory"] = self.get_size(self.swap_memory.free)
            self.details["Used swap_memory"] = self.get_size(self.swap_memory.used)
            self.details["Percentage swap_memory"] = self.get_size(self.swap_memory.percent)
        except Exception as e:
            print(e)
        finally:
            return self.details

    def get_size(self, convert_bytes, suffix="B"):
        """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
        for unit in ["", "K", "M", "G", "T", "P"]:
            if convert_bytes < self.factor:
                return f"{convert_bytes:.2f}{unit}{suffix}"
            convert_bytes /= self.factor
