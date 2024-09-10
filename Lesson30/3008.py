class Queue:
    
    def __init__(self, *values: int): 
        self.values = values

    def append(self, *values: int):
        self.values = (*self.values, *values)

    def copy(self) -> 'Queue':
        return Queue(*self.values)

    def pop(self) -> int:
        if not self.values:  
            raise IndexError("empty")
        value, self.values = self.values[0], self.values[1:]
        return value

    def extend(self, queue: 'Queue'):
        self.values = (*self.values, *queue.values)

    def next(self) -> 'Queue':
        return Queue(*self.values[1:]) if self.values else Queue()  

    def add(self, other: 'Queue') -> 'Queue':
        if not isinstance(other, Queue):
            return NotImplemented
        return Queue(*self.values, *other.values)

    def __add__(self, other: 'Queue') -> 'Queue':  
        return self.add(other)

    def __iadd__(self, other: 'Queue') -> 'Queue':  
        if not isinstance(other, Queue):
            return NotImplemented
        self.extend(other)
        return self

    def __eq__(self, other: 'Queue') -> bool:  
        if not isinstance(other, Queue):
            return NotImplemented
        return self.values == other.values

    def __str__(self) -> str: 
        return f"[{' -> '.join(map(str, self.values))}]" if self.values else "[]"

    def rshift(self, n: int) -> 'Queue':
        return Queue(*self.values[n:]) if n < len(self.values) else Queue()


