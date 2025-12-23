import regex

class Solution:
    def __init__(self):
        pass

    def password_rotation(self, input_path: str):
        instructions = []
        with open(input_path) as f:
            while line := f.readline().strip("\n"):
                instructions.append(line)
        zero_occurrences = 0
        current_position = 50
        for rotation in instructions:
            match = regex.match(r"(\w)(\d+)", rotation)
            direction = match.group(1)
            dials = int(match.group(2))

            if direction == "L":
                current_position = (current_position - dials) % 100
            elif direction == "R":
                current_position = (current_position + dials) % 100

            if current_position == 0:
                zero_occurrences += 1

        # Count the number of time the dial reverts to 0
        # Dial starts at 50
        return zero_occurrences

    def password_rotation_method_wack(self, input_path: str):
        instructions = []
        with open(input_path) as f:
            while line := f.readline().strip("\n"):
                instructions.append(line)

        zero_occurrences, zeros_passed = 0, 0
        current_position, raw_position = 50, 50

        print(f"Starting dial_position: {current_position}")
        for rotation in instructions:
            match = regex.match(r"(\w)(\d+)", rotation)
            direction = match.group(1)
            dials = int(match.group(2))

            zeros_passed = dials // 100
            physical_dials = dials % 100

            if direction == "L":
                raw_position = current_position - physical_dials
            elif direction == "R":
                raw_position = current_position + physical_dials

            # If reaches to 0 in or go out of dial range in less than 100 steps, that means 1 zero has been passed
            # Disqualify if current position is already at 0 to prevent case where it will erroeneously count
            # step from 0 to negative as passing 0
            if current_position > 0 and 0 < physical_dials < 100 and (raw_position <= 0 or raw_position >= 100):
                zeros_passed += 1
            current_position = raw_position % 100

            zero_occurrences += zeros_passed
            print(f"Instruction: {rotation}, cur_pos: {current_position}, "
                  f"raw_position: {raw_position}, Zeros passed: {zeros_passed}")
        # Count the number of time the dial reverts to 0, and the number of times the dial points to 0 during
        # its rotation to the new dial position
        # Dial starts at 50
        return zero_occurrences

# 5695 failed. > 6000 is too high. 5100 is too low
if __name__ == "__main__":
    sol = Solution()
    password = sol.password_rotation("../problem_descriptions/day_one_p1_input.txt")
    print(f"Solution to part 1: {password}")
    password_new_method = sol.password_rotation_method_wack("../problem_descriptions/day_one_p1_input.txt")
    # password_new_method = sol.password_rotation_method_wack("../problem_descriptions/day_one_p1_input_test.txt")
    print(f"Solution to part 2 using method 0x434C49434B: {password_new_method}")