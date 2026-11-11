class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if need1==0 and need2==0:
            return 0
        both=min(need1,need2)
        total=both*min(costBoth,cost1+cost2)
        need1-=both
        need2-=both
        if (need1>0):
            total+=need1*min(cost1,costBoth)
        elif (need2>0):
            total+=need2*min(cost2,costBoth)
        return total