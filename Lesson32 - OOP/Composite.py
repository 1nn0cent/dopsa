from abc import ABC, abstractmethod

class FileSystemElement(ABC):
    @abstractmethod
    def display(self, indent=""):
        """Метод для отображения содержимого."""
        pass

    @abstractmethod
    def get_size(self):
        """Метод для получения размера файла или директории."""
        pass

class File(FileSystemElement):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def display(self, indent=""):
        print(f"{indent}File: {self.name} ({self.size} bytes)")

    def get_size(self):
        return self.size

class Directory(FileSystemElement):
    def __init__(self, name: str):
        self.name = name
        self.elements = []

    def add(self, element: FileSystemElement):
        self.elements.append(element)

    def display(self, indent=""):
        print(f"{indent}Directory: {self.name}")
        for element in self.elements:
            element.display(indent + "  ")

    def get_size(self):
        total_size = 0
        for element in self.elements:
            total_size += element.get_size()
        return total_size


def main():
    root = Directory("root")
    home = Directory("home")
    user = Directory("user")

    file1 = File("file1.txt", 100)
    file2 = File("file2.txt", 200)
    file3 = File("file3.txt", 300)

    root.add(home)
    home.add(user)
    user.add(file1)
    user.add(file2)
    root.add(file3)

    root.display()
    print(f"\nTotal size: {root.get_size()} bytes")

if __name__ == "__main__":
    main()
