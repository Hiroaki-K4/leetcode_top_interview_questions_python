class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Handle edge cases
        if numerator == 0:
            return "0"

        result = []

        # Determine the sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        # Work with absolute values
        numerator, denominator = abs(numerator), abs(denominator)

        # Add the integral part
        result.append(str(numerator // denominator))
        remainder = numerator % denominator

        if remainder == 0:
            return "".join(result)

        # Add the decimal point
        result.append(".")

        # Map to store previously seen remainders
        remainder_map = {}

        while remainder != 0:
            if remainder in remainder_map:
                # Insert parentheses around the repeating part
                result.insert(remainder_map[remainder], "(")
                result.append(")")
                break

            # Store the current remainder position
            remainder_map[remainder] = len(result)

            # Compute the next digit
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(result)


if __name__ == "__main__":
    solution = Solution()
    numerator = 1
    denominator = 2
    print("Input: numerator = {0}, denominator = {1}".format(numerator, denominator))
    print("Output: {0}".format(solution.fractionToDecimal(numerator, denominator)))
    print()

    numerator = 2
    denominator = 1
    print("Input: numerator = {0}, denominator = {1}".format(numerator, denominator))
    print("Output: {0}".format(solution.fractionToDecimal(numerator, denominator)))
    print()

    numerator = 4
    denominator = 333
    print("Input: numerator = {0}, denominator = {1}".format(numerator, denominator))
    print("Output: {0}".format(solution.fractionToDecimal(numerator, denominator)))
