# game_score.py

name = input("Enter player name: ")

games = int(input("Enter number of games played: "))
total_score = int(input("Enter total score: "))

average = total_score / games

print("\nPlayer:", name)
print("Games Played:", games)
print("Total Score:", total_score)
print("Average Score:", average)
