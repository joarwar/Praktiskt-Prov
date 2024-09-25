#Author: Joar Warholm
#Date: 2024-09-25

print("Välkommen till praktiskt prov för Inbyggda System 2 ")

print(" Vilka tabeller vill du beräkna? \n")

tal_input = input("Ange siffra/tal med mellanrum. ")

if tal_input == "":
    exit()

split_list = tal_input.split()

end_list = []
for x in split_list:
    for y in range(10):
        multi = int(x) * (y + 1)
        end_list.append(f"{x} * {y + 1} = {multi}")

amount = len(split_list)

for i in range(amount * 10):
    print(end_list[i])
