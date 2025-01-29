"""This program will help you plan a cozy tea party. It will ask the user for the number of guests expected to be attending and calculate the quantity of tea bags needed, the number of treats to accompany the tea, and the expected cost of the party based on this number."""

__author__: str = "730718944"


def main_planner(guests: int) -> None:
    """This function will print out the number of tea bags, treats, and the cost of the tea party based on the number of guests."""
    tea_count = tea_bags(people=guests)
    treat_count = treats(people=guests)
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_count))
    print("Treats: " + str(treat_count))
    print("Cost: $" + str(cost(tea_count=tea_count, treat_count=treat_count)))


def tea_bags(people: int) -> int:
    """This function will calculate the number of tea bags needed based on the number of guests."""
    return people * 2


def treats(people: int) -> int:
    """This function will calculate the number of treats needed based on the number of teas guests are expected to drink."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """This function will calculate the cost of tea bags and treats combined."""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
