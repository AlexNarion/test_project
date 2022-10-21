
board_play = list(range(1,10))

def draw_board(board_play):
    print ("-" * 13)
    for i in range(3):
        print ("|", board_play[0+i*3], "|", board_play[1+i*3], "|", board_play[2+i*3], "|")
        print ("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Ход 1 игрока, вы ставите - " + player_token+" ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Ошибка. Введено неверное число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board_play[player_answer-1]) not in "XO"):
                board_play[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта ячейчка занята")
        else:
            print ("Неверное число. Введите число от 1 до 9 чтобы сходить.")

def check_win(board_play):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board_play[each[0]] == board_play[each[1]] == board_play[each[2]]:
            return board_play[each[0]]
    return False

def main(board_play):
    counter = 0
    win = False
    while not win:
        draw_board(board_play)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board_play)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board_play)

main(board_play)