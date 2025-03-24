"""
Ispišite sve prirodne brojeve manje od 100 koji su kvadrati nekoga drugoga prirodnog broja koristeći se petljom
while.
"""

broj = 1
while broj**2 < 100:
    print(f"{broj} => kvadrat {broj**2}")
    broj = broj + 1
