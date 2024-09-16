# Вопрос №2: Циклический буфер с использованием deque
# Плюсы: простота использования, встроенные оптимизации.
# Минусы: меньше контроля над структурой.


from collections import deque

class CircularBufferDeque:
    def __init__(self, size):
        self.buffer = deque(maxlen=size)

    def enqueue(self, item):
        if len(self.buffer) == self.buffer.maxlen:
            raise OverflowError("Buffer is full")
        self.buffer.append(item)

    def dequeue(self):
        if not self.buffer:
            raise IndexError("Buffer is empty")
        return self.buffer.popleft()