class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define bounds for 32-bit integer range
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -(2 ** 31)

        # Handle edge case: division by zero or overflow
        if divisor == 0:
            raise ValueError("Division by zero is undefined.")
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX  # Overflow case

        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with positive values for simplicity
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        # Subtract divisor repeatedly using bit manipulation
        while dividend >= divisor:
            current_divisor, num_divisors = divisor, 1
            while dividend >= (current_divisor << 1):
                current_divisor <<= 1
                num_divisors <<= 1
            dividend -= current_divisor
            quotient += num_divisors

        # Apply the sign
        if negative:
            quotient = -quotient

        # Clamp the result within the 32-bit integer range
        return max(INT_MIN, min(INT_MAX, quotient))


if __name__ == "__main__":
    solution = Solution()
    dividend = 10
    divisor = 3
    print("Input: dividend = {0}, divisor = {1}".format(dividend, divisor))
    print("Output: {0}".format(solution.divide(dividend, divisor)))
    print()

    dividend = 7
    divisor = -3
    print("Input: dividend = {0}, divisor = {1}".format(dividend, divisor))
    print("Output: {0}".format(solution.divide(dividend, divisor)))
