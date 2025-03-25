"""This is a dictionary."""

__author__: str = "730730083"

sent: list[str] = ["i", "am", "the", "best", "coder"]


def invert(diction: dict[str, str]) -> dict[str, str]:
    """Returns the inverse of a given dictionary."""
    inv: dict[str, str] = dict()
    for key in diction:
        if diction[key] in inv:
            raise KeyError(f"Oops there's a double: {diction[key]}")
        inv[diction[key]] = key
    return inv


def count(li: list[str]) -> dict[str, int]:
    """Returns the amount of times a value appears in a list."""
    ct: dict[str, int] = dict()
    i = 0

    while i < len(li):
        # iterate through list one at a time
        hold: str = li[i]
        # print(hold)
        amt: int = 0
        j = 0

        while j < len(li):
            # compare hold vs iter vals of list, amt+1 when hold==val
            if hold == li[j]:
                amt += 1
            j += 1
        ct[hold] = amt
        i += 1
    return ct


def favorite_color(di: dict[str, str]) -> str:
    """Returns the most favorite color in the world."""
    ccs: dict[str, int] = count(list(di.values()))
    max_count = max(ccs.values())
    if max_count == 1:
        return "no repeats"
    fav: str = max(ccs, key=lambda k: ccs[k])
    return fav


def bin_len(li: list[str]) -> dict[int, set[str]]:
    """Makes dict where key is length of string & value is string set of that length."""
    bin: dict[int, set[str]] = dict()

    for s in li:
        length = len(s)
        if length not in bin:
            bin[length] = set()
        bin[length].add(s)

    return bin


print(bin_len(sent))
