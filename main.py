import random 

zbozi = ["sýr", "rajče","kukuřice", "šunka", "pizza", "rukola", "oliva", "brambory", "smetana", "salám"]
for i in range(11):
    osoba1 = random.choice(zbozi)
    print(f"kupme {osoba1}")
    osoba2 = random.choice(zbozi)
    print(f"Ne kupme {osoba2}")