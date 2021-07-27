class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = int(1e9)
        nums.sort()
        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sumVal = num + nums[left] + nums[right]
                if abs(target - sumVal) < abs(closest):
                    closest = target - sumVal
                if sumVal > target:
                    right -= 1
                else:
                    left += 1
            if closest == 0:
                break
        return target - closest