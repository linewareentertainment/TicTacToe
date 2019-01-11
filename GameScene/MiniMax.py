''' Pseudocode for minimax algorithm

    minimax(state, depth, player)

        if(player = max) then
            best = [null, -infinity]
        else
            best = [null, +infinity]

        if(depth = 0 or gameover) then
            score = evaluate this state for player
            return [null, score]

        for each valid move m for player in state s do
            execute move m on s
            [move, score] = minimax(s, depth - 1, -player)
            undo move m on s

            if (player = max) then
                if score > best.score then best = [move, score]
            else
                if score < best.score then best = [move, score]

        return best
    end

'''

# System Imports
from math import inf as infinity
from random import choice

# 3rd party Imports
import pygame

# Local Imports
from GameScene import GameMechanics as game
from GameScene import BoardGraphics as gui

# 79 Character length ---------------------------------------------------------

MAX = +1
MIN = -1


def game_over(state):
    return game.is_game_over(state, MIN) or game.is_game_over(state, MAX)

def evaluate(state):
    if game.is_game_over(state, MAX):
        score = +1
    elif game.is_game_over(state, MIN):
        score = -1
    else:
        score = 0

    return score



def empty_cells(state):
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0: cells.append([x, y])
    return cells


# minimax(state, depth, player)
def minimax(state, depth, player):
    #     if(player = max) then
    #         best = [null, -infinity]
    #     else
    #         best = [null, +infinity]
    if player == MAX:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    #     if(depth = 0 or gameover) then
    #         score = evaluate this state for player
    #         return [null, score]
    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    #     for each valid move m for player in state s do
    #         execute move m on s
    #         [move, score] = minimax(s, depth - 1, -player)
    #         undo move m on s
    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        #         if (player = max) then
        #             if score > best.score then best = [move, score]
        #         else
        #             if score < best.score then best = [move, score]
        if player == MAX:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score

    #     return best
    return best


def ai_move(board, player):
    depth = len(empty_cells(board))
    if depth == 0 or game.is_game_over(board, player):
        return

    if depth == 9:
        x = choice([0,1,2])
        y = choice([0,1,2])
    else:
        move = minimax(board, depth, MAX)
        x, y = move[0], move[1]

    gui.drawMove(board, x, y, player)