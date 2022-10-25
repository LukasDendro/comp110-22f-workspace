"""Utilizing dictionaries for three functions."""
___author___ = "730565579"


def invert(items: dict[str, str]) -> dict[str, str]:
    """Given a dict the invert function will invert the keys and values into an inverted dict."""
    invert_dict: dict[str, str] = dict()
    for i in items:
        invert_dict[items[i]] = i
    if len(invert_dict) != len(items):
        raise KeyError("More than one of the same key encountered!")
    return invert_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Produces the favorite color based on frequency of color in dict."""
    num_colors: int = 0
    most_colors: int = 0 
    frequent_color: str = ""
    for i in colors:
        for item in colors:
            if colors[item] == colors[i]:
                num_colors += 1
        if num_colors > most_colors:
            most_colors = num_colors
            frequent_color = colors[i]
        num_colors = 0 
    return frequent_color


def count(xs: list[str]) -> dict[str, int]:
    """Counts the frequency of items in a list."""
    count_dict: dict[str, int] = dict()
    for i in xs:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict