class Solution:
    def __init__(self):
        pass

    def sum_max_joltage(self, input_path):
        result = 0

        banks = []
        with open(input_path) as infile:
            while bank := infile.readline():
                banks.append(bank.strip())

        for bank in banks:
            max_joltage_line = self.find_max_joltage(bank)
            result += max_joltage_line

        return result

    def find_max_joltage(self, bank_line: str):
        result = 0
        if len(bank_line) <= 1:
            return 0

        l = 0
        for r in range(1, len(bank_line)):
            jolt = int(f"{bank_line[l]}{bank_line[r]}")
            result = max(result, jolt)

            if bank_line[r] > bank_line[l]:
                # Potentially new max joltage, move l to r
                l = r
        return result

    def sum_max_joltage_beat_static_friction(self, input_path):
        result = 0

        banks = []
        with open(input_path) as infile:
            while bank := infile.readline():
                banks.append(bank.strip())

        for bank in banks:
            max_joltage_line = self.find_max_joltage_sf(bank)
            result += max_joltage_line

        return result

    def find_max_joltage_sf(self, bank_line: str):
        result = ""

        # Turning on 12 batteries.
        # First choice, within [0, len(bank_line) - 1 - 11] (Leave at least 11 digits left to be found)
        digits_left = 11
        l, r = 0, (len(bank_line)-1) - digits_left
        max_index_window = -1
        max_joltage_window = 0
        while digits_left >= 0:
            while l <= r:
                if max_joltage_window < int(bank_line[l]):
                    max_joltage_window = int(bank_line[l])
                    max_index_window = l
                l += 1
            result += f"{max_joltage_window}"
            # Move start of window to find the next digit to be after the currently found max digit
            l = max_index_window + 1
            digits_left -= 1
            r = (len(bank_line) - 1) - digits_left
            max_joltage_window = 0  # Reset

        return int(result)

if __name__ == "__main__":
    sol = Solution()

    max_joltage = sol.sum_max_joltage("../problem_descriptions/day_three_input.txt")
    # max_joltage = sol.sum_max_joltage("../problem_descriptions/day_three_input_test.txt")
    print(f"Solution for part 1: {max_joltage}")

    max_joltage = sol.sum_max_joltage_beat_static_friction("../problem_descriptions/day_three_input.txt")
    # max_joltage = sol.sum_max_joltage_beat_static_friction("../problem_descriptions/day_three_input_test.txt")
    print(f"Solution for part 2: {max_joltage}")