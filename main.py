import re

tekst = "Tutaj mamy przykładowy tekst zawierający frazę dom15, którą chcemy odnaleźć, dom15."
wzorzec = r"dom15"  # Wzorzec dopasowujący dokładnie 'dom15'
wzorzec_wiele = r'\b\w{5,}\b'
# Jeśli potrzebujesz dopasować tylko słowa zawierające 
# litery (bez cyfr czy podkreśleń), możesz zmodyfikować 
# wzorzec, np. używając [a-zA-Z]{5,} zamiast \w{5,}.

wynik_wiele = re.findall(wzorzec_wiele, tekst)
print(wynik_wiele)

wynik = re.search(wzorzec, tekst)

if wynik:
    print("Znaleziono frazę:", wynik.group())
    print("Ilość wystąpień w tekście:", len(re.findall(wzorzec, tekst)))
else:
    print("Fraza nie została znaleziona.")



# Przykładowy tekst zawierający adresy e-mail
tekst = "Kontakt: jan.kowalski@example.com, anna.nowak@domena.org oraz info@firma.pl, Tutaj mamy przykładowy tekst zaw"

# Wzorzec wyrażenia regularnego do dopasowania adresów e-mail:
# \b       - granica słowa
# [\w.-]+  - jedna lub więcej liter, cyfr, podkreśleń, kropek lub myślników
# @        - znak @
# [\w.-]+  - jedna lub więcej liter, cyfr, podkreśleń, kropek lub myślników
# \.       - kropka
# \w+      - jedna lub więcej liter lub cyfr
# \b       - granica słowa
# zapis wzorca poprzedzając go r (raw) pozwala interpretować tekst dosłownie
# bez r trzeba by robić uwielnienie od \ w postaci \\
wzorzec = r'\b[\w.-]+@[\w.-]+\.\w+\b'

# Znajdujemy wszystkie adresy e-mail w tekście
emails = re.findall(wzorzec, tekst)

print("Znalezione adresy e-mail:", emails)
