#Author: Joar Warholm
#Date: 2024-09-18

print("Ei-23 genrep praktiskt prov ht24 ")
amount_res = int(input("Hur många resistanser? "))
resistances = []
pararell = []
for i in range(amount_res):
    resistance = float(input(f"Resistans {i + 1}: "))
    resistances.append(resistance)
    para = 1/resistance
    pararell.append(1/resistance)
serie_resistance = sum(resistances)
pararell_resistance = sum(pararell)
print(pararell)
print(f"Serieresistans: {serie_resistance}")
print(f"Pararellresistans: {1/pararell_resistance}")



