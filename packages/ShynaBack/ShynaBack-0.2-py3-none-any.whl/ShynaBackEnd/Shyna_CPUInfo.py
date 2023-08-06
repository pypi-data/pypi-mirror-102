import psutil

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path)

class CPUInfo:
    """
    {'Physical cores': 2, 'Total cores': 4, 'Max Frequency': '1800.0Mhz', 'Min Frequency': '800.0Mhz',
    'Current Frequency': '1704.576Mhz', 'Core 1': '22.4%', 'Total CPU Usage': 0.0, 'Core 2': '14.7%',
    'Core 3': '100.0%', 'Core 4': '21.2%'}
    """
    details = {}
    cpu_freq = psutil.cpu_freq()

    def get_cpu_details(self):
        try:
            # let's print CPU information
            print("=" * 40, "CPU Info", "=" * 40)
            # number of cores
            self.details['Physical cores'] = psutil.cpu_count(logical=False)
            self.details['Total cores'] = psutil.cpu_count(logical=True)
            # CPU frequencies
            self.details["Max Frequency"] = str(self.cpu_freq.max) + "Mhz"
            self.details["Min Frequency"] = str(self.cpu_freq.min) + "Mhz"
            self.details["Current Frequency"] = str(self.cpu_freq.current) + "Mhz"
            # CPU usage
            print("CPU Usage Per Core:")
            for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                self.details["Core " + str(int(i) + 1)] = str(percentage) + "%"
                self.details["Total CPU Usage"] = psutil.cpu_percent()
        except Exception as e:
            print(e)
        finally:
            return self.details
