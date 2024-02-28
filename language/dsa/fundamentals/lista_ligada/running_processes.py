import psutil

class Process:
    def __init__(self, pid, name, cpu_percent, memory_percent):
        self.pid = pid
        self.name = name
        self.cpu_percent = cpu_percent
        self.memory_percent = memory_percent
        self.next = None

class ListProcess:
    def __init__(self):
        self.head = None

    def insert_process(self, pid, name, cpu_percent, memory_percent):
        new_process = Process(pid, name, cpu_percent, memory_percent)
        if self.head == None:
            self.head = new_process
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_process

    def print_out(self):
        current = self.head
        while current:
            print(f"PID: {current.pid}, Name: {current.name}, CPU%: {self.formatter(current.cpu_percent)}, Memory%: {self.formatter(current.memory_percent)}")
            current = current.next

    def formatter(self, value):
        rounded_value = round(value, 2)
        formatted_value = "{:.2f}".format(rounded_value)
        return formatted_value

# Example of use:
process = psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])
list_process = ListProcess()
for p in process:
    list_process.insert_process(p.info['pid'],p.info['name'], p.info['cpu_percent'], p.info['memory_percent'])
list_process.print_out()