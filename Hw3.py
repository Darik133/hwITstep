class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def information(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}, Колір: {self.color}")

class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)

    def bark(self):
        print("Собака гавкає")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)

    def meow(self):
        print("Кіт міукає")

dog = Dog("Арчібальд", 6, "білий")
cat = Cat("Чупчік", 3, "чорний")

dog.information()
dog.bark()

cat.information()
cat.meow()
