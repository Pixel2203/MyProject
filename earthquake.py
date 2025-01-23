magnitude = int(input("Magnitude: "))


test = (
    "Micro" if magnitude < 2 else
    "Minor" if magnitude < 4 else
    "Light" if magnitude < 5 else
    "Moderate" if magnitude < 6 else
    "Strong" if magnitude < 7 else
    "Major" if magnitude < 8 else
    "Great"
)

instructions = {
    "Micro": "Passiert nix",
    "Minor": "Bitte festhalten",
    "Light": "Macht die Schotten dicht!",
    "Moderate": "Raff dich, ist halb so wild",
    "Strong": "Kellerkind",
    "Major": "Bete dass du überlebst",
    "Great": "Vallah, gib auf"
}
print("DANGER LEVEL: " , test)
print(instructions.get(test))


