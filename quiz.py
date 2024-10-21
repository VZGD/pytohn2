# Frågesport med tre frågor och fyra alternativ för varje
def frågesport():
    poäng = 0

    # Fråga 1
    print("Fråga 1: Hur lång är Joel?")
    print("1. 170 cm")
    print("2. 175 cm")
    print("3. 180 cm")
    print("4. 185 cm")
    svar = input("Skriv ditt svar (1-4): ")
    
    if svar == "2":
        print("Rätt svar!")
        poäng += 1
    else:
        print("Fel svar. Det rätta svaret är 175 cm.")

    # Fråga 2
    print("\nFråga 2: Hur gammal är Melvin?")
    print("1. 16 år")
    print("2. 18 år")
    print("3. 20 år")
    print("4. 22 år")
    svar = input("Skriv ditt svar (1-4): ")

    if svar == "2":
        print("Rätt svar!")
        poäng += 1
    else:
        print("Fel svar. Det rätta svaret är 18 år.")

    # Fråga 3
    print("\nFråga 3: Vart bor Melvin?")
    print("1. Göteborg")
    print("2. Malmö")
    print("3. Stockholm")
    print("4. Uppsala")
    svar = input("Skriv ditt svar (1-4): ")

    if svar == "3":
        print("Rätt svar!")
        poäng += 1
    else:
        print("Fel svar. Det rätta svaret är Stockholm.")

    # Resultat
    print(f"\nDu fick {poäng} av 3 rätt!")

# Kör frågesporten
frågesport()
