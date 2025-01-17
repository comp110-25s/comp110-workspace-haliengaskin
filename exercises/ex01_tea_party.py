"""A program to help me plan the most epic tea party ever."""

__author__: str = "730730083"


# main_planner function
def main_planner(guests: int) -> None:
    """Asks for the amount of party guests."""
    print("A Cozy Tea Party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    return None


# tea_bags function
def tea_bags(people: int) -> int:
    """Finds the # of guests and plans for each guest to have 2 tea bags."""
    return people * 2


# treats function
def treats(people: int) -> int:
    """Finds the # of guests and plans for each one to have 1.5 treats."""
    return int(tea_bags(people) * 1.5)


# cost function
def cost(tea_count: int, treat_count: int) -> float:
    """Finds total cost for treats and tea."""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
