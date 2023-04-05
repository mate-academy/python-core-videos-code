class Point:
    def __new__(cls, *args, **kwargs) -> "Point":
        print("1. Creating new instance of Point")
        return super().__new__(cls)

    def __init__(self, x, y) -> None:
        print("2. Initializing the new instance of Point")
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"x={self.x}, y={self.y}"


if __name__ == '__main__':
    point = Point(10, 20)
    print(point)
