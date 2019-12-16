import random

class Show():
    def present(self):
        self.state = [1,0,0]
        random.shuffle(self.state)
        
        return len(self.state)
    def unravel(self, player_choice):
        possible_reveals = []
        for i in enumerate(self.state):
            if i[0]!=player_choice and not i[1]:
                possible_reveals.append(i[0])
        return random.choice(possible_reveals)
    def declare(self, player_choice):
        return self.state[player_choice]

def switch_decision(player_choice, wrong_door):
    return set(range(3)).difference([player_choice, wrong_door]).pop()

def play_game(switching = False):
    this_show = Show()
    choices = this_show.present()
    player_choice = random.randint(0, choices-1)
    wrong_door = this_show.unravel(player_choice)
    if switching:
        return this_show.declare(switch_decision(player_choice, wrong_door))
    else:
        return this_show.declare(player_choice)

def model(n, switching = False):
    attempts, wins = 0, 0
    for i in range(n):
        attempts+=1
        wins+=int(play_game(switching))
    return (wins/attempts)*100

print(model(100000, True))