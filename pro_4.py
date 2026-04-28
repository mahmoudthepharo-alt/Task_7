class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Team:
    def __init__(self):
        self.members = []

    def add_player(self, player_object):
        self.members.append(player_object)
        print(f"{player_object.name} added to the team.")


team = Team()

while True:
    print("\n 1- Add Player \n 2- Exit ")

    choice = int(input("Choose an option: "))

    if choice == 1:
        name = input("Enter player name: ")
        score = int(input("Enter player score: "))
        player = Player(name, score)
        team.add_player(player)
        print("\nTeam Members:")
        for player in team.members:
            print(f"- {player.name}:{player.score}")

    elif choice == 2:
        print("Exit")
        break

    else:
        print("Invalid option, try again.")