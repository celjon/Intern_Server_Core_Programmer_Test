# Вопрос №2: Циклический буфер с использованием списка и индексов
# Плюсы: полный контроль, гибкость.
# Минусы: больше работы по управлению индексами.


class CircularBufferList:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0

    def enqueue(self, item):
        if self.count == self.size:
            raise OverflowError("Buffer is full")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise IndexError("Buffer is empty")
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return item