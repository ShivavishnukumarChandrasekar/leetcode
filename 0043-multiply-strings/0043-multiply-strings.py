class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digits: list[str] = [str(x) for x in range(10)]

        n1: int = 0
        n2: int = 0

        for i in range(len(num1)):
            n1 += digits.index(num1[-(i + 1)]) * 10**i

        for i in range(len(num2)):
            n2 += digits.index(num2[-(i + 1)]) * 10**i

        return str(n1 * n2)