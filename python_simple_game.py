
import random


choice_list = ['R', 'S', 'P']
player_no_of_wins = 0
computer_no_of_wins = 0

def get_players_inputs(player, computer):
    return (player, computer)



while True:
    print('enter R, S or P to play')
    player_choice = input('enter your choice: ')
    computer_choice = random.choice(choice_list)
    if player_choice not in choice_list and player_choice != 'stop':
        print('you must choose either R, S or P to play this game')
        continue
    if player_choice == computer_choice:
        print('this is a tie')
        #get_players_inputs(player_choice, computer_choice)
    if player_choice == 'R' and computer_choice == 'P':
        print(f'your choice: {player_choice} \ncomputer choice: {computer_choice}')
        computer_no_of_wins += 1
        print('computer wins', computer_no_of_wins, 'times')

    elif player_choice == 'P' and computer_choice == 'R':
        player_no_of_wins+=1
        print('you win', player_no_of_wins, 'times')

    if player_choice == 'P' and computer_choice == 'S':
        print(f'your choice: {player_choice} \ncomputer choice: {computer_choice}')
        computer_no_of_wins += 1
        print('computer wins', computer_no_of_wins, 'times')

    elif player_choice == 'S' and computer_choice == 'P':
        player_no_of_wins += 1
        print('you win', player_no_of_wins, 'times')

    if player_choice == 'S' and computer_choice == 'R':
        print(f'your choice: {player_choice} \ncomputer choice: {computer_choice}')
        computer_no_of_wins += 1
        print('computer wins', computer_no_of_wins, 'times')

    elif player_choice == 'R' and computer_choice == 'S':
        player_no_of_wins += 1
        print('you win', player_no_of_wins, 'times')
    elif player_choice == 'stop':
        if player_no_of_wins > 0 or computer_no_of_wins >0:
            player_no_of_wins += 1
            computer_no_of_wins += 1
            print('you won:', player_no_of_wins, 'times','\n','computer won:', computer_no_of_wins, 'times')
        else:
            print('thank you! you can still play again')




