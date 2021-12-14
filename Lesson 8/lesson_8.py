class Animals:
    def __init__(self, alive_or_not=True):
        self.alive_or_not = alive_or_not

    def status(self):
        return self.alive_or_not


class Mammals(Animals):
    def __init__(self,age, alive_or_not=True, ):
        super().__init__(alive_or_not=alive_or_not)
        self.live_birth = True
        self.milk_feeding = True
        self.age = age

    def birth(self):
        print('Поздравляю с новым млекопитающим!')


class Human(Mammals):
    def __init__(self, name, male, age, alive_or_not=True):
        super().__init__(age, alive_or_not=alive_or_not)
        self.name = name
        self.male = male

    def say(self):
        print(f'Привет! Я {self.male}, мне {self.age} лет, а зовут меня {self.name}!')

    def birth(self):
        print("Ого! У меня появился ребенок!")


class Cat(Mammals):
    def __init__(self, name, male, character, age, alive_or_not=True):
        super().__init__(age, alive_or_not=alive_or_not)
        self.name = name
        self.male = male
        self.character = character
        self.night_vision = True

    def say(self):
        print("Мявк")

    def birth(self):
        print("Какой милый котенок!!! ☻")

    def sleap(self, hour):
        print(f"Тсс... Прошу, будь тише ближайшие {hour} часов. Котейка спать изволит!")


class Dog(Mammals):
    def __init__(self, name, male, aggressive, age, alive_or_not=True):
        super().__init__(age, alive_or_not=alive_or_not)
        self.name = name
        self.male = male
        self.aggressive = aggressive

    def say(self):
        print("Гафк")

    def birth(self):
        print("Какой прикольный щеночек !!! ☺")

    def bite(self):
        if self.aggressive:
            print(f"Будь осторожен! {self.name} может укусить!")
        else:
            print(f"Не бойся, {self.name} не кусается!")


class Student(Human):
    def __init__(self, name, male, age, number_of_homework_done=0, alive_or_not=True):
        super().__init__(name, male, age, alive_or_not=alive_or_not)
        self.number_of_homework_done = number_of_homework_done

    def report(self):
        print(f'{self.name} имеет {self.number_of_homework_done} сданных работ')

    def __eq__(self, other):
        return self.number_of_homework_done == other.number_of_homework_done

    def __ne__(self, other):
        return self.number_of_homework_done != other.number_of_homework_done

    def __gt__(self, other):
        return self.number_of_homework_done > other.number_of_homework_done

    def __lt__(self, other):
        return self.number_of_homework_done < other.number_of_homework_done

    def __ge__(self, other):
        return self.number_of_homework_done >= other.number_of_homework_done

    def __le__(self, other):
        return self.number_of_homework_done <= other.number_of_homework_done

print("Animals:")
ani = Animals()
print(ani.status())

print("\nMammals:")
mamm = Mammals(10)
print(mamm.status())
mamm.birth()

print("\nHuman:")
hum = Human("Василий", "мужчина", 12)
print(hum.status())
hum.say()
hum.birth()

print("\nCat:")
cat = Cat("Амния", "кошка", "спокойная", 3)
print(cat.status())
cat.say()
cat.sleap(6)
cat.birth()

print("\nDog:")
dog = Dog("Бобик", "пес", True, 5)
print(dog.status())
dog.say()
dog.bite()
dog.birth()
dog1 = Dog("Кроль", "собака", False, 6)
print(dog1.status())
dog1.say()
dog1.bite()
dog1.birth()

print("\nStudent:")
Tolya = Student("Толя", 'мужчина', 21, 13)
Vanya = Student("Ваня", 'мужчина', 20, 15)
Tolya.say()
Tolya.report()
Vanya.say()
Vanya.report()
print("\nСравнение по кол-ву ДЗ:\n"
     f"Толя < Ваня: {Tolya < Vanya}\n"
     f"Толя > Ваня: {Tolya > Vanya}\n"
     f"Толя <= Ваня: {Tolya <= Vanya}\n"
     f"Толя >= Ваня: {Tolya >= Vanya}\n"
     f"Толя == Ваня: {Tolya == Vanya}\n"
     f"Толя != Ваня: {Tolya != Vanya}")