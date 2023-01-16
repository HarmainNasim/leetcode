class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #generate a hashmap
        prevMap= {} #it is prevMap because it will contain all elements 
                    #before the current index element (val:index)
        #iterate thru every val in array
        for i, n in enumerate(nums):
            diff= target -n
            if diff in prevMap:
                return prevMap[diff], i
            prevMap[n]=i
            
