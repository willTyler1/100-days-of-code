#problem 167 - TwoSum II - input array is sorted 
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        #Array sorted in increasing order. 
        #So increasing left will increase sum 
        #and decreasing right will decrease sum 
        test = numbers[left] + numbers[right]
        if test == target: 
            return [left+1, right+1]
        elif test < target:
            left += 1
        else: 
            right -= 1
            
      
      
#problem 283 - Move Zeros
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    #this is the index of the leftmost zero we find 
    leftZero = 0
    n = len(nums)
    for i in range(n):
        #basic idea: if leftZero is a zero and the iterator is not then swap them
        if nums[leftZero] == 0 and nums[i] != 0:
            nums[leftZero], nums[i] = nums[i], nums[leftZero]
        #if nums[leftZero] is not a zero then skip to the next index
        if nums[leftZero] != 0:
            leftZero += 1
            
            
            
#problem - 496 - Next Greater Element I
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    ans = []
    for i in range(len(nums1)):
        outerLeft, outerRight = 0, len(nums2) - 1
        outerSolved = 0
        while outerLeft <= outerRight and outerSolved == 0:
            if nums1[i] == nums2[outerLeft]:
                outerSolved = 1
                left, right = outerLeft, len(nums2) - 1
                solved = 0
                while left <= right and solved==0:
                    if nums2[left] > nums2[outerLeft]:
                        solved = 1
                        ans.append(nums2[left])
                    else: 
                        left += 1 
                if solved == 0:
                    ans.append(-1)
            else: 
                outerLeft += 1
    return ans
                    
