import random

def test_monty_hall_problem(number_of_games):
  ### Plays the Monty Hall game a number of times, and returns a tuple containing the win rates of switch and not switch

  def play_game(switch):
    ### Returns True if you won, and false if you loose

    prize_door = random.randint(1, 3)
    door_chosen = random.randint(1, 3)

    if switch:
      if prize_door == door_chosen:
        return False
      else:
        return True

    else:
      if prize_door == door_chosen:
        return True
      else:
        return False

  def play_multiple_games(number_of_games):
    ### Plays the game the ammount of times requested and returns the ammount os wins for each strategy 

    winsSwitching = 0
    winsNotSwitching = 0
    for i in range(number_of_games):
      if play_game(True):
        winsSwitching += 1

    for i in range(number_of_games):
      if play_game(False):
        winsNotSwitching += 1

    return (winsSwitching, winsNotSwitching)

  winsSwitching, winsNotSwitching = play_multiple_games(number_of_games)

  switchWinRate = (winsSwitching / number_of_games) * 100
  noSwitchWinRate = (winsNotSwitching / number_of_games) * 100

  return (switchWinRate, noSwitchWinRate)  

switchWinRate, noSwitchWinRate = test_monty_hall_problem(10000)

print(f'Win rate switching: {switchWinRate}')
print(f'Win rate not switching: {noSwitchWinRate}')
