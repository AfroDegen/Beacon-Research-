# beacon.py

from config import QUERIES
from search import get_google_domains
from ai_sources import get_ai_sources
from compare import compare_sources


print("\n=== BEACON RESEARCH ===\n")

results = []

for query in QUERIES:

    print("\n--------------------")

    ranked = get_google_domains(query)

    print("\nGoogle Top Domains:")

    for d in ranked:
        print("-", d)

    retrieved = get_ai_sources(query)

    comparison = compare_sources(
        ranked,
        retrieved
    )

    print("\nRESULTS")

    print(
        "Overlap:",
        comparison["overlap_score"],
        "%"
    )

    print(
        "Matched:",
        comparison["matched"]
    )

    print(
        "Only Ranked:",
        comparison["only_ranked"]
    )

    print(
        "Only Retrieved:",
        comparison["only_retrieved"]
    )

    results.append(
        comparison["overlap_score"]
    )

print("\n====================")

average = sum(results) / len(results)

print(
    f"\nAverage Overlap: {average:.2f}%"
)
