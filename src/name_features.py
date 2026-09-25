from name_matching import (
    exact_match,
    name_similarity,
    token_similarity,
    token_set_similarity,
    partial_similarity
)


def get_name_features(name1, name2):
    """Generate name-matching features for a pair of businesses."""

    return {
        "name_exact": int(exact_match(name1, name2)),
        "name_similarity": name_similarity(name1, name2),
        "name_token_similarity": token_similarity(name1, name2),
        "name_token_set_similarity": token_set_similarity(name1, name2),
        "name_partial_similarity": partial_similarity(name1, name2),
    }