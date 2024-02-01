from random import choice


def player_tip():
    tip_list = []
    while len(tip_list) < 6:
        try:
            x = (int(input("Choose number from 1 to 49:\n")))
            if x not in tip_list and x in range(1, 50):
                tip_list.append(x)
            else:
                print("Please choose different number")
        except ValueError:
            print("Invalid number, try again")
    return sorted(tip_list)


def computer_tip():
    range_list = list(range(1, 50))
    c_tip_list = []
    while len(c_tip_list) < 6:
        y = choice(range_list)
        c_tip_list.append(y)
        range_list.remove(y)
    return sorted(c_tip_list)


def lotto():
    player_list = player_tip()
    computer_list = computer_tip()
    matched = 0
    for tip in player_list:
        if tip in computer_list:
            matched += 1
    print(f"Player tips :\n {player_list}")
    print(f"Computer tips :\n {computer_list}")
    print(f"You guessed {matched} number/s")


if __name__ == '__main__':
    lotto()
