from rapidfuzz import fuzz


def exact_match(name1, name2):
    """Check whether two normalized names are exactly equal."""
    return name1 == name2


def name_similarity(name1, name2):
    """Calculate fuzzy similarity between two business names."""
    if not name1 or not name2:
        return 0.0

    return fuzz.ratio(name1, name2) / 100.0


def token_similarity(name1, name2):
    """Compare names while ignoring word order."""
    if not name1 or not name2:
        return 0.0

    return fuzz.token_sort_ratio(name1, name2) / 100.0

def token_set_similarity(name1, name2):
    """Compare names based on shared words."""
    if not name1 or not name2:
        return 0.0

    return fuzz.token_set_ratio(name1, name2) / 100.0


def partial_similarity(name1, name2):
    """Compare partial matches between names."""
    if not name1 or not name2:
        return 0.0

    return fuzz.partial_ratio(name1, name2) / 100.0