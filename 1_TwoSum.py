class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited={}
        for i in range(len(nums)):
            x=target-nums[i]
            if x in visited.keys():
                return [visited[x],i]
            else:
                visited[nums[i]]=i