"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Fish older than 3 and bears older than 5 die (remove from river)."""
        fish_alive: list[Fish] = [fish for fish in self.fish if fish.age <= 3]
        self.fish = fish_alive

        bears_alive: list[Bear] = [bear for bear in self.bears if bear.age <= 5]
        self.bears = bears_alive

    def bears_eating(self):
        """Each bear eats 3 fish IF there are <=5 fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:  # are there at least 5 fish
                self.remove_fish(3)  # take 3 fish from river
                bear.eat(3)  # feed it to bear :P

    def check_hunger(self):
        bears_alive: list[Bear] = [bear for bear in self.bears if bear.hunger_score > 0]
        self.bears = bears_alive

    def repopulate_fish(self):
        """Fish fabricate four fish following."""
        num_nows = (len(self.fish) // 2) * 4  # for every two fish, add four fish
        for _ in range(num_nows):
            self.fish.append(Fish())

    def repopulate_bears(self):
        """Two bears love each other very much and create 1 cub."""
        num_cubs = len(self.bears) // 2  # for every two bears, add one cub
        for _ in range(num_cubs):
            self.bears.append(Bear())  # add a new bear to river

    def view_river(self):
        print(
            (
                f"~~~ Day {self.day}: ~~~\n"
                f"Fish population: {len(self.fish)}\n"
                f"Bear population: {len(self.bears)}"
            )
        )

    def one_river_day(self):
        """Simulate one day of life in the river"""
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
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        """Remove a specified number of fish from the river."""
        self.fish = self.fish[amount:]
