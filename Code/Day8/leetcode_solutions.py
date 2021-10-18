#977 - Squares of a Sorted Array
def sortedSquares(self, nums: List[int]) -> List[int]:
    #using two pointer approach. Comparing absolute values.
    n = len(nums)
    left,right = 0, n - 1
    result = [0] * n
    resultIndex = n - 1
    while right >= 0 and resultIndex >=0:
        if abs(nums[left]) > abs(nums[right]):
            result[resultIndex] = nums[left] ** 2
            left += 1
        else: 
            result[resultIndex] = nums[right] ** 2
            right -= 1
        resultIndex -= 1
    return result
  
  
#189 - Rotate Array
def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n
    #reverse entire list
    self.reverse(nums, 0, n-1)
    #unreverse 0 to (k mod n)-1 positions in list
    self.reverse(nums, 0, k-1)
    #unreverse k mod n to n positions in list
    self.reverse(nums, k, n-1)
  def reverse(self, nums: List[int], left: int, right: int) -> None:
    while left < right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1
