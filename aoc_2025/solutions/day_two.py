import regex
import math

class Solution:
    def __init__(self):
        pass

    def invalid_ID_sum(self, input_path: str) -> int:
        ids = []
        result = 0
        with open(input_path) as infile:
            ids = infile.readline().split(",")
            for id_range in ids:
                match = regex.match(r"(\d+)-(\d+)", id_range)
                result += self.invalid_id_sum_range(int(match.group(1)), int(match.group(2)))
        return result

    # Look for sum of invalid IDs in [left, right] range
    def invalid_id_sum_range(self, left: int, right: int) -> int:
        result = 0
        # Invalid rule: Look for any ID which is made only of some sequence of digits repeated twice
        # If left and right has the same number of digits and left has odd number of digits => Guaranteed no invalid ID
        if len(str(left)) == len(str(right)) and len(str(left)) % 2 == 1:
            return 0
        # Reducing search space
        elif len(str(left)) % 2 == 1:  # If left has odd number of digits, start at the smallest number with even digits
            left = 10 ** (len(str(left)))
        elif len(str(right)) % 2 == 1: # Same as above, except start at the biggest number with even digits
            right = 10 ** (len(str(right))-1) - 1
        # Now to check for invalid IDs
        # Start at the left side's first half of the digits 995995 // 1000
        cur_potential_invalid_half = left // 10 ** (len(str(left)) // 2)
        cur_potential_invalid = cur_potential_invalid_half + cur_potential_invalid_half *  10 ** (len(str(cur_potential_invalid_half)))

        # Now while loop blin
        while cur_potential_invalid <= right:
            if cur_potential_invalid >= left:
                result += cur_potential_invalid
            cur_potential_invalid_half += 1
            cur_potential_invalid = cur_potential_invalid_half + cur_potential_invalid_half *  10 ** (len(str(cur_potential_invalid_half)))

        return result

    def invalid_ID_sum_modified_rule(self, input_path: str) -> int:
        ids = []
        result = 0
        with open(input_path) as infile:
            ids = infile.readline().split(",")
            for id_range in ids:
                match = regex.match(r"(\d+)-(\d+)", id_range)
                result += self.invalid_id_sum_range_modified(int(match.group(1)), int(match.group(2)))
                print("")
        return result

    def invalid_id_sum_range_modified(self, left: int, right: int) -> int:
        result = 0
        # Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So,
        # 12341234 (1234 two times), 123123123 (123 three times),
        # 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

        cur_pot_inval_repeat = 1
        cur_pot_inval = 11
        generated_set = set()
        while True:
            # There are "2D" increments.
            # 1) Within the repeat pattern:
            #   - Increase the number of repetitions
            #   - Check if new generated number is already computed in a set check
            #   - Check if new generated number is bigger than right
            # 2) Until it is bigger than right:
            #   There are 2 sub paths here....
            #   2.1) Increase value of repeated patterns...., then restart the repetition process
            #   2.2) Initiate the new repeat pattern, increasing number of digits in the repeat pattern. (vertical increment)
            #        Get minimum number of repetitions

            if left <= cur_pot_inval <= right and cur_pot_inval not in generated_set:
                print(f"Invalid ID within range {left}-{right}: {cur_pot_inval}")
                result += cur_pot_inval
                generated_set.add(cur_pot_inval)
            # Repeat more
            cur_pot_inval = int(f"{cur_pot_inval}{cur_pot_inval_repeat}")

            if cur_pot_inval > right:
                if len(str(cur_pot_inval_repeat + 1)) == len(str(cur_pot_inval_repeat)):
                    cur_pot_inval_repeat += 1
                else:
                    cur_pot_inval_repeat = 1 * (10 ** (len(str(cur_pot_inval_repeat))))
                    if len(str(cur_pot_inval_repeat)) * 2 > len(str(right)):  # If the newest repeat number is definitely bigger than the right, break off the loop entirely
                        break
                # Restart the repetition process. Find the minimum repeated value that is bigger >= left, and SHOULD REPEAT AT LEAST TWICE!
                tmp = ""
                for _ in range(max(2, math.ceil(len(str(left)) / len(str(cur_pot_inval_repeat))))):
                    tmp += f"{cur_pot_inval_repeat}"
                cur_pot_inval = int(tmp)

        return result

if __name__ == "__main__":
    solution = Solution()
    invalid_sum = solution.invalid_ID_sum("../problem_descriptions/day_two_input.txt")
    # invalid_sum = solution.invalid_ID_sum("../problem_descriptions/day_two_input_test.txt")
    print(f"Solution for part 1: {invalid_sum}")

    # 69553832728 too high. Might have repetitions, or something outside of range gets added into the result
    invalid_sum_modified_rule = solution.invalid_ID_sum_modified_rule("../problem_descriptions/day_two_input.txt")
    # invalid_sum_modified_rule = solution.invalid_ID_sum_modified_rule("../problem_descriptions/day_two_input_test.txt")
    print(f"Solution for part 2: {invalid_sum_modified_rule}")