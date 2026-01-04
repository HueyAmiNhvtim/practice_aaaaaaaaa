from collections import deque

class Solution:
    def __init__(self):
        pass

    def printing(self, input_path: str):
        accessible_roll = 0

        rows = []
        rows_display = []
        with open(input_path) as f:
            while line := f.readline().strip():
                rows.append(line)

        for i in range(len(rows)):
            row = rows[i]
            rows_display.append(list(row))

            for j in range(len(row)):
                obj = row[j]
                if obj == "@":
                    adjacent_rolls = -1 # Offset by 1 since checking all 9 cells will reach the target cell itself being checked
                    # Check all 9 cells (including the target)
                    for row_to_check in range(i-1, i+2):
                        for adjacent_index in range(j-1, j+2):
                            if 0 <= row_to_check < len(rows) and 0 <= adjacent_index < len(rows[row_to_check]) and rows[row_to_check][adjacent_index] == "@":
                                adjacent_rolls += 1
                    if adjacent_rolls < 4:
                        accessible_roll += 1
                        rows_display[-1][j] = "X"

        # for i in range(len(rows_display)):
        #     print("".join(rows_display[i]))
        return accessible_roll

    # This is a rather naive way, involving scanning the entire grid constantly
    # until it is no longer possible to remove rolls
    def remove_rolls(self, input_path: str):
        rolls_removed = 0
        scan_time = 0
        rows = []
        with open(input_path) as f:
            while line := f.readline().strip():
                gridded_line = list(line)
                rows.append(gridded_line)


        rolls_just_removed = 0
        while True:
            for i in range(len(rows)):
                print("".join(rows[i]))
            print("")

            for i in range(len(rows)):
                row = rows[i]
                for j in range(len(row)):
                    obj = row[j]
                    if obj == "@":
                        adjacent_rolls = -1  # Offset by 1 since checking all 9 cells will reach the target cell itself being checked
                        # Check all 9 cells (including the target)
                        for row_to_check in range(i - 1, i + 2):
                            for adjacent_index in range(j - 1, j + 2):
                                if 0 <= row_to_check < len(rows) and 0 <= adjacent_index < len(rows[row_to_check]) and \
                                        rows[row_to_check][adjacent_index] == "@":
                                    adjacent_rolls += 1
                        if adjacent_rolls < 4:
                            rows[i][j] = "."
                            rolls_removed += 1
                            rolls_just_removed += 1

            scan_time += 1
            if rolls_just_removed == 0:
                break
            else:
                rolls_just_removed = 0 # Reset for next scan

        print(f"Number of scans through the entire grid: {scan_time}")
        return rolls_removed

    # Somehow even worse than the above...................
    def remove_rolls_better(self, input_path: str):
        rolls_removed = 0
        scan_time = 0
        rows = []
        visited = []

        # Representing the relative position of up, left, down, right of adjacent cells for any cell in a grid
        d_row = [-1, 0, 1, 0]
        d_col = [0, -1, 0, 1]

        with open(input_path) as f:
            while line := f.readline().strip():
                gridded_line = list(line)
                rows.append(gridded_line)
                visited.append([False for _ in range(len(gridded_line))])

        # Breadth-First-Search utilizing a queue
        visiting_queue = deque()
        visiting_queue.append((0, 0))
        visited[0][0] = True

        while True:
            for i in range(len(rows)):
                print("".join(rows[i]))
            print("")

            rolls_just_removed = 0
            while visiting_queue:
                cell = visiting_queue.popleft()
                removed = self._is_removable(rows, cell[0], cell[1])
                if removed:
                    rolls_removed += 1
                    rolls_just_removed += 1

                # Add adjacent nodes to the queue
                for i in range(len(d_row)):
                    adj_node = (cell[0] + d_row[i], cell[1] + d_col[i])
                    if self._is_valid(visited, adj_node[0], adj_node[1]):
                        visiting_queue.append(adj_node)
                        visited[adj_node[0]][adj_node[1]] = True

            scan_time += 1

            if rolls_just_removed == 0:
                break
            # Reset
            visiting_queue = deque()
            visiting_queue.append((0, 0))
            for i in range(len(visited)):
                for j in range(len(visited[i])):
                    visited[i][j] = False

        print(f"Number of scans through the entire grid: {scan_time}")
        return rolls_removed

    def _is_valid(self, visited, row, col):
        if (row < 0 or col < 0) or (row >= len(visited) or col >= len(visited[0])):
            return False
        return not visited[row][col]

    def _is_removable(self, grid, row, col):
        obj = grid[row][col]
        if obj == "@":
            adjacent_rolls = -1  # Offset by 1 since checking all 9 cells will reach the target cell itself being checked
            # Check all 9 cells (including the target)
            for row_to_check in range(row - 1, row + 2):
                for adjacent_index in range(col - 1, col + 2):
                    if 0 <= row_to_check < len(grid) and 0 <= adjacent_index < len(grid[row_to_check]) and \
                            grid[row_to_check][adjacent_index] == "@":
                        adjacent_rolls += 1
            if adjacent_rolls < 4:
                grid[row][col] = "."
                return True
            else:
                return False
        else:
            return False # Already removed or just no roll there in the first place.

if __name__ == "__main__":
    sol = Solution()
    p1_res = sol.printing(input_path="../problem_descriptions/day_four_input.txt")
    # p1_res = sol.printing(input_path="../problem_descriptions/day_four_input_test.txt")
    # print(f"Number of rolls accessible by a forklift: {p1_res}")

    # p2_res = sol.remove_rolls(input_path="../problem_descriptions/day_four_input.txt")
    p2_res = sol.remove_rolls(input_path="../problem_descriptions/day_four_input_test.txt")
    print(f"Total number of rolls removed: {p2_res}")

    p2_res_better = sol.remove_rolls_better(input_path="../problem_descriptions/day_four_input.txt")
    # p2_res_better = sol.remove_rolls_better(input_path="../problem_descriptions/day_four_input_test.txt")
    print(f"Total number of rolls removed: {p2_res_better}")