from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        is_empty = self._data == []
        if not is_empty:
            return self._data.pop(0)
        else:
            return None

    def search(self, index):
        length = len(self._data)
        if index < 0 or index >= length:
            raise IndexError("Índice Inválido ou Inexistente")
        else:
            return self._data[index]
