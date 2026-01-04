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
                rows.append(list(line))

        rolls_just_removed = 0
        while True:

            accessible_roll = 0

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
                            accessible_roll += 1
                            rows[i][j] = "."
                            rolls_removed += 1
                            rolls_just_removed += 1


            for i in range(len(rows)):
                print("".join(rows[i]))
            print("")
            scan_time += 1
            if rolls_just_removed == 0:
                break
            else:
                rolls_just_removed = 0 # Reset for next scan

        print(f"Number of scans through the entire grid: {scan_time}")
        return rolls_removed


    def remove_rolls_better(self, input_path: str):
        pass

if __name__ == "__main__":
    sol = Solution()
    p1_res = sol.printing(input_path="../problem_descriptions/day_four_input.txt")
    # p1_res = sol.printing(input_path="../problem_descriptions/day_four_input_test.txt")
    # print(f"Number of rolls accessible by a forklift: {p1_res}")

    p2_res = sol.remove_rolls(input_path="../problem_descriptions/day_four_input.txt")
    # p2_res = sol.remove_rolls(input_path="../problem_descriptions/day_four_input_test.txt")
    print(f"Total number of rolls removed: {p2_res}")