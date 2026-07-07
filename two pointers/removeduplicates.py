class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


if __name__ == "__main__":
    nums = list(map(int, input("Enter sorted array: ").split()))

    sol = Solution()
    k = sol.removeDuplicates(nums)

    print("Unique Count:", k)
    print("Updated Array:", nums)