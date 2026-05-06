class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROWS = len(boxGrid)
        COLS = len(boxGrid[0])
        
        # Step 1: Physical Simulation (Apply Gravity horizontally first)
        # We process each row independently to move stones to the right
        for row in boxGrid:
            # 'empty_pos' is the rightmost available slot for a stone
            empty_pos = COLS - 1
            for j in range(COLS - 1, -1, -1):
                if row[j] == '#':
                    # Move stone to the furthest empty position
                    row[j], row[empty_pos] = '.', '#'
                    empty_pos -= 1
                elif row[j] == '*':
                    # Obstacle resets the available empty position
                    empty_pos = j - 1
                elif row[j] == '.':
                    # Do nothing, but don't move empty_pos
                    pass

        # Step 2: Geometric Transformation (90-degree clockwise rotation)
        # In matrix terms: result[j][i] = original[ROWS - 1 - i][j]
        # Using Python's zip and reverse for a clean, pointer-free rotation
        return [list(reversed(col)) for col in zip(*boxGrid)]        