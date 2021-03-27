"""
Game theory is a branch of mathematics concerned with the analysis of
decision-making and strategy. It has applications in economics, biology, and
behavioral science. Many seemingly complex situations can be reduced to a
relatively simple mathematical game that can be analyzed in a systematic way
to find "optimal" solutions.

A classic problem in game theory is the prisoner's dilemma, which, in its
original form, is as follows: two co-conspirators are caught and must decide
whether to remain quiet or to testify against the other. If both remain quiet,
they both serve a 1-year sentence; if one testifies but the other does not, the
testifier is released and the other serves a 3-year sentence; and if both
testify against one another, they both serve a 2-year sentence. What should each
conspirator do? It turns out that the best choice each conspirator can make,
given any reasonable distrust of the other, is to testify. Adopting this
strategy, they will either serve no sentence or a 2-year sentence maximum


For example purposes, let's consider the following table as the possible
payoffs from a simple two-player game based on which programming language
to use:

    Player1/Player2    C    Python
        C            3 / 1   2 / 3
      Python         2 / 1   2 / 4

If the players agree on a language, then they write the code at the speed they
predicted (P1: Python 4; C 1 - P2: Python 2; C: 3), but if they disagree,
then the productivity of the faster programmer is reduced by 1.

This module illustrates how to construct an object in Python to represent this
simple two-player game, and then perform some elementary analysis regarding the
outcomes of the this game.
"""
import numpy as np
import nashpy as nash

player1 = np.array([[3, 2], [2, 2]])
player2 = np.array([[1, 3], [1, 4]])
dilemma = nash.Game(player1, player2)

print(dilemma[[1, 0], [1, 0]])  # [1 3]
print(dilemma[[1, 0], [0, 1]])  # [2 3]
print(dilemma[[0, 1], [1, 0]])  # [1 2]
print(dilemma[[0, 1], [0, 1]])  # [2 4]

print(dilemma[[0.1, 0.9], [0.5, 0.5]]) # [2.05, 2.45]
