class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = list(accumulate(reversed(piles)))[::-1]

        @cache
        def best(i: int, m: int) -> int:  # mover's max take from piles[i:]
            if i + 2 * m >= n:
                return suffix[i]  # grab everything
            return suffix[i] - min(best(i + x, max(m, x)) for x in range(1, 2 * m + 1))

        return best(0, 1)