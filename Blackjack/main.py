############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.










# 2 개의 랜덤 카드 값의 시작 핸드를 사용자와 컴퓨터 모두에 적용하십시오.

# 컴퓨터 나 사용자에게 블랙 잭이있는시기를 감지하십시오. ( 에이스 + 10 가치 카드 ).

# 컴퓨터에 블랙 잭이 있으면 사용자에게 블랙 잭 (이 있어도 )이 손실됩니다. 사용자가 블랙 잭을 받으면 컴퓨터에 블랙 잭 (이없는 한 )을 얻습니다.

# 카드 값을 기준으로 사용자와 컴퓨터의 점수를 계산하십시오.

# 에이스가 그려지면 11로 계산하십시오. 그러나 총계가 21을 초과하면 에이스를 1로 계산하십시오.

# 컴퓨터의 첫 번째 카드를 사용자에게 공개하십시오.

# 사용자 점수가 21을 초과하거나 사용자 또는 컴퓨터가 블랙 잭을 받으면 게임이 즉시 종료됩니다.

# 다른 카드를 받으려면 사용자에게 문의하십시오.

# 사용자가 완료되고 더 이상 카드를 더 이상 그리지 않으려면 컴퓨터를 재생하십시오. 점수가 16을 넘지 않는 한 컴퓨터는 계속 카드를 뽑아야합니다.

# 사용자와 컴퓨터 점수를 비교하고 그것이 승리, 손실 또는 추첨인지 확인하십시오.

# 게임이 끝날 때 플레이어와 컴퓨터의 최종 핸드와 점수를 인쇄하십시오.

# 게임이 끝나면 사용자에게 다시 게임을하고 싶은지 물어보십시오. 새로 시작하려면 콘솔을 비 웁니다.

import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

my_cards = []
com_cards = []

def deal_card(deck):
  return deck.append(random.choice(cards))

def calculate_deck(deck):
  sum = 0
  have_ace = False
  for card in deck:
    if card == 11:
      have_ace = True
    sum += card
    
  if sum > 21:
    if have_ace:
      sum -= 10
      
  return sum

deal_card(my_cards)
deal_card(com_cards)
game_state = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
while game_state == "y":
  deal_card(my_cards)
  deal_card(com_cards)

  sum_my_cards = calculate_deck(my_cards)
  sum_com_cards = calculate_deck(com_cards)

  if sum_com_cards == 21:
    print("You lose")
    break

  if sum_my_cards == 21:
    print("You Win")
    break

  print(f"You: {my_cards}")
  print(f"COM: {com_cards[0]}")
  
  game_state = input("more card? y/n?")

if sum_my_cards == sum_com_cards:
  os.system('cls')
  print("Draw")
elif sum_my_cards > sum_com_cards:
  os.system('cls')
  print("Win")
elif sum_my_cards < sum_com_cards:
  os.system('cls')
  print("Lose")
  
print(f"You: {my_cards}")
print(f"COM: {com_cards}")