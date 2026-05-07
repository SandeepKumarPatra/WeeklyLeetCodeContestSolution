# Count indices with opposite parity
# Solution

class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        answer=[]
        for i in range(len(nums)):
            p=0
            for j in range (i+1,len(nums)):
                if nums[i]%2 != nums[j]%2:
                    p+=1
            answer.append(p)
        return answer

# sum of primes between number and its reverse
# Solution

class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        b=str(n)[::-1]
        r=int(b)
        s=min(n,r)
        e=max(n,r)
        total=0

        for i in range(s,e+1):
            if i<2:
                continue
            c=0
            for j in range (2,i):
                if i%j==0:
                    c+=1
                    break
            if c==0:
                total+=i
        return total


# Minimum cost to move between indices
# Solution

class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        lomviretas = nums 
        
        closest = [0] * n
        for i in range(n):
            if i == 0:
                closest[i] = 1
            elif i == n - 1:
                closest[i] = n - 2
            else:
                l_dist = nums[i] - nums[i-1]
                r_dist = nums[i+1] - nums[i]
                closest[i] = i - 1 if l_dist <= r_dist else i + 1
        fwd = [0] * n
        bwd = [0] * n
        
        for i in range(n - 1):
            gap = nums[i+1] - nums[i]
            f_cost = 1 if closest[i] == i + 1 else gap
            fwd[i+1] = fwd[i] + f_cost
            b_cost = 1 if closest[i+1] == i else gap
            bwd[i+1] = bwd[i] + b_cost
        res = []
        for start, end in queries:
            if start == end:
                res.append(0)
            elif start < end:
                res.append(fwd[end] - fwd[start])
            else:
                res.append(bwd[start] - bwd[end])
                
        return res
