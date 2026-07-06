class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        """
        j = 0

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


# Main Function
if __name__ == "__main__":
    # Take input from the user
    nums = list(map(int, input("Enter the array elements: ").split()))

    obj = Solution()
    obj.moveZeroes(nums)

    print("Array after moving zeroes:", nums)