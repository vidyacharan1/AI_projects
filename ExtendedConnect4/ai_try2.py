import random
import numpy as np
from typing import List, Tuple, Dict
from connect4.utils import get_pts, get_valid_actions, Integer


class AIPlayer:
    def __init__(self, player_number: int, time: int):
        """
        :param player_number: Current player number
        :param time: Time per move (seconds)
        """
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}:ai'.format(player_number)
        self.time = time
        # Do the rest of your implementation here
    
    def modify_board(self, pnum, state, action):
        (board, temp) = state
        (column_num, pop_move) = action
        if pop_move == False:
            i = len(board)-1
            while(i>=0):
                if(board[i][column_num]==0):
                    board[i][column_num] = pnum
                    break
                i-=1
        else:
            for i in range(len(board)-1, 0):
                board[i][column_num] = board[i-1][column_num]
            board[0][column_num] = 0
        return (board, temp)

    def max(self, state):
        print("This is max\n")
        valid_actions = get_valid_actions(self.player_number, state)
        pts = get_pts(self.player_number, state[0])
        ac = valid_actions[0]
        if(len(valid_actions)==1):
            return (pts, ac)
        for action in valid_actions:
            b = self.modify_board(self.player_number, state, action)
            (m1, a) = self.min(b)
            if m1 > pts:
                pts = m1
                ac = a
        return (pts, ac)
    
    def min(self, state):
        print("This is min\n")
        valid_actions = get_valid_actions(3-
        self.player_number, state)
        pts = get_pts(3-self.player_number, state[0])
        ac = valid_actions[0]
        if(len(valid_actions)==1):
            return (pts, ac)
        for action in valid_actions:
            b = self.modify_board(3-self.player_number, state, action)
            (m1, a) = self.max(b)
            if m1 < pts:
                pts = m1
                ac = a
        return (pts, ac)

    def get_intelligent_move(self, state: Tuple[np.array, Dict[int, Integer]]) -> Tuple[int, bool]:
        """
        Given the current state of the board, return the next move
        This will play against either itself or a human player
        :param state: Contains:
                        1. board
                            - a numpy array containing the state of the board using the following encoding:
                            - the board maintains its same two dimensions
                                - row 0 is the top of the board and so is the last row filled
                            - spaces that are unoccupied are marked as 0
                            - spaces that are occupied by player 1 have a 1 in them
                            - spaces that are occupied by player 2 have a 2 in them
                        2. Dictionary of int to Integer. It will tell the remaining popout moves given a player
        :return: action (0 based index of the column and if it is a popout move)
        """
        (m, ac) = self.max(state)
        return ac
        
        # curr_score = get_pts(self.player_number, state[0])
        # valid_actions = get_valid_actions(self.player_number, state)
        # for action in valid_actions:
        #     if(curr_score < get_pts(self.player_number, )):
        #         final_action = action
        # # Do the rest of your implementation here
        # return final_action
        
        raise NotImplementedError('Whoops I don\'t know what to do')

    def get_expectimax_move(self, state: Tuple[np.array, Dict[int, Integer]]) -> Tuple[int, bool]:
        """
        Given the current state of the board, return the next move based on
        the Expecti max algorithm.
        This will play against the random player, who chooses any valid move
        with equal probability
        :param state: Contains:
                        1. board
                            - a numpy array containing the state of the board using the following encoding:
                            - the board maintains its same two dimensions
                                - row 0 is the top of the board and so is the last row filled
                            - spaces that are unoccupied are marked as 0
                            - spaces that are occupied by player 1 have a 1 in them
                            - spaces that are occupied by player 2 have a 2 in them
                        2. Dictionary of int to Integer. It will tell the remaining popout moves given a player
        :return: action (0 based index of the column and if it is a popout move)
        """
        # Do the rest of your implementation here
        raise NotImplementedError('Whoops I don\'t know what to do')
