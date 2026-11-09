import heapq
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        tree = [0] + [1] * k

        for i in range(1, k + 1):
            j = i + (i & -i)
            if j <= k:
                tree[j] += tree[i]

        # Get prefix sum
        def query(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & -i
            return s

        # Update availability
        def update(i, val):
            while i <= k:
                tree[i] += val
                i += i & -i

        # Find kth available server
        def find_kth(rank):
            idx = 0
            bit = 1 << (k.bit_length() - 1)

            while bit:
                nxt = idx + bit

                if nxt <= k and tree[nxt] < rank:
                    idx = nxt
                    rank -= tree[nxt]

                bit >>= 1

            return idx

        busy = []
        count = [0] * k

        for i in range(len(arrival)):

            # Release completed servers
            while busy and busy[0][0] <= arrival[i]:
                finish, server = heapq.heappop(busy)
                update(server + 1, 1)

            # Preferred server
            start = i % k

            # Available servers before the preferred server
            before = query(start)

            # Total available servers
            total = query(k)

            if total == 0:
                continue

            # Find next available server with circular wrapping
            if total > before:
                rank = before + 1
            else:
                rank = 1

            server = find_kth(rank)

            # Assign request
            count[server] += 1

            update(server + 1, -1)

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        # Find busiest servers
        max_count = max(count)

        return [i for i in range(k) if count[i] == max_count]