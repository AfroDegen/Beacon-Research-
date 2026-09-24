# compare.py


def compare_sources(
    ranked_domains,
    retrieved_domains
):

    ranked = set(ranked_domains)

    retrieved = set(retrieved_domains)

    overlap = ranked.intersection(retrieved)

    overlap_score = 0

    if len(retrieved) > 0:
        overlap_score = (
            len(overlap)
            / len(retrieved)
        )

    return {
        "matched": list(overlap),
        "only_ranked": list(
            ranked - retrieved
        ),
        "only_retrieved": list(
            retrieved - ranked
        ),
        "overlap_score": round(
            overlap_score * 100,
            2
        )
    }
