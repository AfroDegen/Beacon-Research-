# ai_sources.py


def get_ai_sources(query):

    print(f"\nQUERY: {query}")

    print(
        "Paste AI cited domains separated by commas:"
    )

    raw = input("> ")

    domains = [
        d.strip()
        for d in raw.split(",")
        if d.strip()
    ]

    return domains
