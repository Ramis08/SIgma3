class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50  # 0-100, 100 - сытый
        self.energy = 50  # 0-100, 100 - выспался
        self.happiness = 50  # 0-100, 100 - счастлив
        
    def eat(self):
        self.hunger = min(100, self.hunger + 30)
        print(f"{self.name} поел(-а). Сытость: {self.hunger}.")
        
    def sleep(self):
        self.energy = min(100, self.energy + 40)
        print(f"{self.name} поспал(-а). Энергия: {self.energy}.")
        
    def play(self):
        if self.energy >= 20 and self.hunger >= 20:
            self.happiness = min(100, self.happiness + 30)
            self.energy -= 20
            self.hunger -= 20
            print(f"{self.name} поиграл(-а). Счастье: {self.happiness}, энергия: {self.energy}, сытость: {self.hunger}.")
        else:
            print(f"{self.name} слишком голоден или устал, чтобы играть.")
            
    def status(self):
        print(f"Питомец {self.name} ({self.species}): Сытость: {self.hunger}, Энергия: {self.energy}, Счастье: {self.happiness}.")
        
# Класс Студент
class Student:
    def __init__(self, name):
        self.name = name
        self.money = 100  # Начальные деньги
        self.knowledge = 50  # 0-100, 100 - отлично учится
        self.energy = 50  # 0-100, 100 - выспался
        self.happiness = 50  # 0-100, 100 - счастлив
        
    def work(self):
        if self.energy >= 20:
            self.money += 50
            self.energy -= 20
            print(f"{self.name} поработал(-а). Деньги: {self.money}, энергия: {self.energy}.")
        else:
            print(f"{self.name} слишком устал(-а), чтобы работать.")
            
    def study(self):
        if self.energy >= 20:
            self.knowledge = min(100, self.knowledge + 30)
            self.energy -= 20
            self.happiness -= 10
            print(f"{self.name} поучился(-ась). Знания: {self.knowledge}, энергия: {self.energy}, счастье: {self.happiness}.")
        else:
            print(f"{self.name} слишком устал(-а), чтобы учиться.")
            
    def rest(self):
        if self.money >= 20:
            self.happiness = min(100, self.happiness + 30)
            self.energy = min(100, self.energy + 20)
            self.money -= 20
            print(f"{self.name} отдохнул(-а). Счастье: {self.happiness}, энергия: {self.energy}, деньги: {self.money}.")
        else:
            print(f"{self.name} не хватает денег на отдых.")
            
    def live_one_year(self):
        for day in range(1, 366):
            print(f"\nДень {day}:")
            if self.money < 20:
                print(f"У {self.name} мало денег. Идет на работу.")
                self.work()
            elif self.knowledge < 40:
                print(f"У {self.name} проблемы с успеваемостью. Начинает учиться.")
                self.study()
            elif self.happiness < 50:
                print(f"У {self.name} плохое настроение. Решает отдохнуть.")
                self.rest()
            else:
                print(f"{self.name} чувствует себя хорошо. Решает учиться или работать для развития.")
                self.study() if self.knowledge < 80 else self.work()
                
            if self.energy < 20:
                print(f"{self.name} слишком устал(-а). Идет спать.")
                self.energy = 100
                
    def status(self):
        print(f"Студент {self.name}: Деньги: {self.money}, Знания: {self.knowledge}, Энергия: {self.energy}, Счастье: {self.happiness}.")

pet = Pet("Барсик", "Кот")
student = Student("Иван")

student.live_one_year()

student.status()

pet.status()
pet.play()
pet.eat()
pet.sleep()
pet.status()
