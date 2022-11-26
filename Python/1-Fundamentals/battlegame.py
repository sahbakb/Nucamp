wizard = 'wizard'
elf = 'elf'
human = 'human'
orc = 'orc'

exit = False

while exit == False:
    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    orc_hp = 300
    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 100
    dragon_hp = 300
    dragon_damage = 50

    while True:
        print("1) "+wizard.capitalize())
        print('2) '+elf.capitalize())
        print('3) '+human.capitalize())
        print('4) '+orc.capitalize())
        print("5) Exit")
        character = input("Choose your character: ")
        if character == '1' or character.lower() == wizard:
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif character == '2' or character.lower() == elf:
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif character == '3' or character.lower() == human:
            character = human
            my_damage = human_damage
            my_hp = human_hp
            break
        elif character == '4' or character.lower() == orc:
            character = orc
            my_damage = orc_damage
            my_hp = orc_hp
            break
        elif character == '5' or character.lower() == 'exit':
            exit = True
            break
        else:
            print("Unknown character!")
            print("")

    if exit == True:
        break

    print("Your character: "+character)
    print("Health: ", my_hp)
    print("Damage: ", my_damage)

    while True:
        dragon_hp = dragon_hp - my_damage
        print("The " + character + " damaged the dragon!")
        print("Dragon Health: ", dragon_hp)
        print(" ")
        if dragon_hp <= 0:
            print("Dragon lost the battle!")
            print("")
            break

        my_hp = my_hp - dragon_damage
        print("Dragon damaged the " + character)
        print(character + " Health:", my_hp)
        print(" ")
        if my_hp <= 0:
            print(character+" lost the battle!")
            print("")
            break
    play_again = input("Would like to play again?(Y/N): ")
    if play_again == 'y' or play_again == 'Y':
        continue
    else:
        exit = True
