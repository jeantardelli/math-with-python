"""
A Nash equilibrium is a two-player strategic game – similar to the Prisoner's
dilemma – that represents a "steady state" in which every player sees the
"best possible" outcome. However, this doesn't mean that the outcome linked to
a Nash equilibrium is the best overall. Nash equilibria are more subtle than
this. An informal definition of a Nash equilibrium is as follows: an action
profile in which no individual player can improve their outcome, assuming
that all other players adhere to the profile.

It is possible to explore the notion of Nash equilibrium with the classic
game of rock-paper-scissors. The rules are as follows. Each player can choose
one of the options: rock, paper, or scissors. Rock beats scissors, but loses
to paper; paper beats rock, but loses to scissors; scissors beats paper, but
loses to rock. Any game in which both players make the same choice is a draw.
Numerically, we represent a win by +1, a loss by -1, and a draw by 0. From
this, we can construct a two-player game and compute Nash equilibria for this
game.

This module illustrates how to compute Nash equilibria for the classic game
of rock-paper-scissors.
"""
import numpy as np
import nashpy as nash

rps_p1 = np.array([
    [0, -1, 1], # rock payoff
    [1, 0, -1], # paper payoff
    [-1, 1, 0]  # scissors payoff
])

rps_p2 = rps_p1.transpose()
rps = nash.Game(rps_p1, rps_p2)
equilibria = rps.support_enumeration()

for p1, p2 in equilibria:
    print("Player 1: ", p1)
    print("Player 2: ", p2)
