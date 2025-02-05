"""File to define River class!"""

__author__ = "730575328"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """This is my river docstring!"""
    
    day: int
    bears: list
    fish: list
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """This is my river docstring!"""
        new_bear: list[Bear] = []
        new_fish: list[Fish] = []
        
        new_fish = self.fish
        new_bear = self.bears

        for x in new_bear:
            if x.age > 5: 
                new_bear.remove(x)
        print(new_bear)

        for x in new_fish:
            if x.age > 3: 
                new_fish.remove(x)
        print(new_fish)

        self.fish = new_fish
        self.bear = new_bear
        return None

    def remove_fish(self, amount: int):
        """This is my river docstring!"""
        x: int = 0 
        while x < amount: 
            self.fish.pop(x)
            x += 1

        return None

    def bears_eating(self):
        """This is my river docstring!"""
        for x in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                x.eat
        return None
    
    def check_hunger(self):
        """This is my river docstring!"""
        hungry_bear: list[Bear]

        hungry_bear = self.bears

        for y in hungry_bear:
            if y.hunger_score < 0:
                hungry_bear.remove(y)
            
        self.bears = hungry_bear
        return None
        
    def repopulate_fish(self):
        """This is my river docstring!"""
        adult_fish: int = len(self.fish)
        baby_fish: int = ((adult_fish // 2) * 4)
        y: int = 1

        for animal_fish in self.bears:
            while y <= baby_fish:
                self.fish.append(animal_fish)
                y += 1
        return None
    
    def repopulate_bears(self):
        """This is my river docstring!"""
        adult_bears: int = len(self.bears)
        baby_bears: int = adult_bears // 2
        y: int = 1

        for bear_animal in self.bears:
            while y <= baby_bears:
                self.bears.append(bear_animal)
                y += 1
        return None
    
    def view_river(self):
        """This is my river docstring!"""
        y: int = len(self.fish)
        z: int = len(self.bears)
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {y}")
        print(f"Bear population: {z}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """This is my river docstring!"""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()