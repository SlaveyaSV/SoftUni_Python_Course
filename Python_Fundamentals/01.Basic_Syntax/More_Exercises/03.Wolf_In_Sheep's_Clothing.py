animals = input().split(", ")

if animals[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    target_sheep = len(animals) - animals.index("wolf") - 1
    print(f"Oi! Sheep number {target_sheep}! You are about to be eaten by a wolf!")
