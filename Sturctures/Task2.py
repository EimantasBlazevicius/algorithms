import abc
from collections import deque
import time


class Client(abc.ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @abc.abstractmethod
    def __str__(self):
        pass


class Woman(Client):
    def __str__(self):
        return f"Madam {self.first_name} {self.last_name}"


class Man(Client):
    def __str__(self):
        return f"Mr {self.first_name} {self.last_name}"


class Child(Client):
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class FifoList:
    def __init__(self):
        self.internal_list = []

    def append(self, data):
        self.internal_list.append(data)

    def pop(self):
        return self.internal_list.pop(0)


class CashRegister:
    def __init__(self):
        self.queue = FifoList()

    def add_client(self, client: Client):
        # print(f"The {client} have joined the queue")
        self.queue.append(client)

    def process(self) -> Client:
        happy_customer = self.queue.pop()
        # print(f"The {happy_customer} left the store and moved to Abudabi")


class FasterCashRegister(CashRegister):

    def __init__(self):
        super().__init__()
        self.queue = deque()

    def process(self):
        happy_customer = self.queue.popleft()
        # print(f"The {happy_customer} left the store and moved to Abudabi")


client1 = Woman("Anna", "Johnson")
client2 = Man("John", "Smith")
client3 = Child("Chris", "Novak")

# cr = FasterCashRegister()
# cr.add_client(client1)
# cr.add_client(client2)
# cr.add_client(client3)
#
# cr.process()
# cr.process()
# cr.process()

start1 = time.perf_counter()
cr = CashRegister()
for _ in range(100000):
    cr.add_client(client1)
for _ in range(100000):
    cr.process()
finish1 = time.perf_counter()
result1 = round(finish1-start1, 5)
# ------------------------------------------------
start2 = time.perf_counter()
fcr = FasterCashRegister()
for _ in range(100000):
    fcr.add_client(client1)
for _ in range(100000):
    fcr.process()
finish2 = time.perf_counter()
result2 = round(finish2-start2, 5)

print(f"Normal version ran in {result1}, the faster deque version ran in {result2}")


