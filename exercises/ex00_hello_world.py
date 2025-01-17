"""My first exercise in COMP110 ⸜(｡˃ ᵕ ˂ )⸝♡"""

__author__ = "730730083"


def greet(name: str) -> str:
    """A welcoming first function definition"""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))
