class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        choice = []

        def backtrack(start):
            if len(choice) == k:
                result.append(choice[:])
                return

            left = start
            still_need = k - len(choice)

            if left > still_need:
                backtrack(start - 1)

            choice.append(start)
            backtrack(start - 1)
            choice.pop()

        backtrack(n)
        return result