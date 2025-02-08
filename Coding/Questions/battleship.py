"""
write a function that finds a ship and return its coordinates
"""
# This one is from some leetcode question: https://leetcode.com/problems/battleships-in-a-board/submissions/1536274622/ 
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        ship_coords = {}
        for i in range(len(board)):
            prev = None
            ship_coords[i] = []
            for j in range(len(board[i])):
                if board[i][j] == "X":
                    # Check to see prev tile's val
                    if prev == "." or prev == None:
                        prev_coords = ship_coords.get(i-1, [])
                        if j not in prev_coords:
                            # need to make sure the previous row didn't have a ship at the current j
                            count += 1

                    ship_coords[i].append(j)
                prev = board[i][j]
        return count