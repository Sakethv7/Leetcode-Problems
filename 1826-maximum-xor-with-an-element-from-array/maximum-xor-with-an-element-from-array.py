class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries = sorted((m, x, i) for i, (x, m) in enumerate(queries))
        ans = [-1]*len(queries)
        
        trie = {}
        k = 0
        for m, x, i in queries: 
            while k < len(nums) and nums[k] <= m: 
                node = trie
                val = bin(nums[k])[2:].zfill(32)
                for c in val: node = node.setdefault(int(c), {})
                node["#"] = nums[k]
                k += 1
            if trie: 
                node = trie
                val = bin(x)[2:].zfill(32)
                for c in val: node = node.get(1-int(c)) or node.get(int(c))
                ans[i] = x ^ node["#"]
        return ans 