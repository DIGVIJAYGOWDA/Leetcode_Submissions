class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        total = [0] * (4 * n)
        squares = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right):
            if left <= start and end <= right:
                length = end - start + 1
                squares[node] = (squares[node] + 2 * total[node] + length) % MOD
                total[node] = (total[node] + length) % MOD
                lazy[node] += 1
                return

            mid = (start + end) // 2

            if lazy[node]:
                val = lazy[node]
                for child, l, r in (
                    (2 * node, start, mid),
                    (2 * node + 1, mid + 1, end)
                ):
                    length = r - l + 1
                    squares[child] = (
                        squares[child] + 2 * val * total[child]
                        + val * val * length
                    ) % MOD
                    total[child] = (total[child] + val * length) % MOD
                    lazy[child] += val

                lazy[node] = 0

            if left <= mid:
                update(2 * node, start, mid, left, right)

            if right > mid:
                update(2 * node + 1, mid + 1, end, left, right)

            total[node] = (total[2 * node] + total[2 * node + 1]) % MOD
            squares[node] = (squares[2 * node] + squares[2 * node + 1]) % MOD

        last = {}
        ans = 0

        for i, num in enumerate(nums):
            previous = last.get(num, -1)
            update(1, 0, n - 1, previous + 1, i)
            ans = (ans + squares[1]) % MOD
            last[num] = i

        return ans