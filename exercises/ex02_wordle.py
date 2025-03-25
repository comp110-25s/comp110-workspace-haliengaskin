"""Wordle exercise for class :P"""

__author__ = "730730083"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(answer: str, ltr: str) -> bool:
    """Check if user's letter guess is contained in the string."""
    assert len(ltr) == 1
    i: int = 0
    while i < len(answer):  # iterate through index of the word to check for a character
        if answer[i] == ltr:
            return True
        i += 1
    return False


def emojified(guess: str, answer: str) -> str:
    """Translates chars into corresponding emoji boxes."""
    assert len(guess) == len(answer), "Guess must be same length as secret"
    i: int = 0
    emoji: str = ""  # empty str to put emoji in
    while i < len(answer):  # assign correctness of the character to an emoji box color
        if guess[i] == answer[i]:
            emoji += GREEN_BOX
        elif contains_char(answer, guess[i]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        i += 1
    return emoji


def input_guess(ans_len: int) -> str:
    """Get the length of the target word"""
    guess = input(f"Enter a {ans_len} character word: ")
    while len(guess) != ans_len:
        guess = input((f"That wasn't {ans_len} chars! Try again: "))
    return guess


def main(secret: str) -> None:
    """Entrypoint of the program and main game loop."""
    max_turns: int = 6  # max amt of turns you can use
    turns_used: int = 1
    game_won: bool = False  # game starts out not being won
    var: int = len(secret)

    while turns_used <= max_turns and not game_won:
        print(f"=== Turn {turns_used}/{max_turns} ===")
        guess = input_guess(var)  # target word length assigned
        output = emojified(guess, secret)  # emojis for each char
        print(output)

        if turns_used == max_turns:  # run out of turns womp womp
            print("X/6 - Sorry, try again tomorrow!")

        if guess == secret:  # win the game if the correct word is guessed
            game_won = True
            print(f"You won in {turns_used}/{max_turns} turns!")
        else:
            turns_used += 1  # otherwise keep iterating


if __name__ == "__main__":
    main(secret="tigers")  # set a super secret target word
