#problem 704 - Binary Search
def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right: 
        # double slash is integer division. 
        # this is left + half dist from left to right. 
        pivotPt = left + (right - left) // 2
        if nums[pivotPt] == target: 
            return pivotPt 
        if target < nums[pivotPt]:
            right = pivotPt - 1
        else:
            left = pivotPt + 1
    return -1
      
     
#problem 278 - First Bad Version
def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    left, right = 1, n
    while left < right: 
        pivot = left + (right - left) // 2
        if isBadVersion(pivot): 
            #first bad version is either pivot or lower
            right = pivot
        else:
            #first bad version is higher than pivot so left becomes pivot
            left = pivot + 1
    return left
  
  
#problem 35 - Search Insert Position
def searchInsert(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1 
    while left <= right: 
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            return pivot 
        if target < nums[pivot]:
            right = pivot -1
        else: 
            left = pivot + 1
    return left
  
  
