# This is a Rock Paper and Scissor game.

import random

rock = "rock"

paper = "paper"

scissor = "scissor"

selections = [rock, paper, scissor]

choice = input('Select one: ')

npc = random.choice(selections)

print(npc)

