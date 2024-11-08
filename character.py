
name1 = input()
attack1 = input()
defense1 = input()

name2 = input()
attack2 = input()
defense2 = input()

name3 = input()
attack3 = input()
defense3 = input()

character1 = (attack1, defense1)
character2 = (attack2, defense2)
character3 = (attack3, defense3)

array = [
    [(name1), (character1)],
    [(name2), (character2)],
    [(name3), (character3)]
]

print(array)

attack = array[0]
for item in array[1:]:
    if int(item[1][0]) > int(attack[1][0]):
        attack = item

defense = array[0]
for item in array[1:]:
    if int(item[1][1]) > int(defense[1][1]):
        defense = item

print("Attack", attack[0], attack[1][0])
print("Defense", defense[0], defense[1][1])
