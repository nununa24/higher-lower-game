import art
import game_data
import random

print(art.logo)
A = random.choice(game_data.data)
control = True
score = 0
while control:
    print('Compare A:',A['name'],',',A['description'],',',A['country'])
    print(art.vs)
    B = random.choice(game_data.data)
    if A == B:
        B = random.choice(game_data.data)
    print('Against B:',B['name'],',',B['description'],',',B['country'])
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if (A['follower_count'] > B['follower_count'] and choice == 'A') or (A['follower_count'] < B['follower_count'] and choice == 'B'):
        score += 1
        print(art.logo)
        print(f"You're right! Current score:{score}")
        A = B
    else:
        print(f"Sorry, that's wrong. Final score:{score}")
        control = False
