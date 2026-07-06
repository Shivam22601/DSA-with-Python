class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


def main():
    m = int(input("Enter number of elements in first array: "))
    arr1 = list(map(int, input("Enter sorted elements of first array: ").split()))

    n = int(input("Enter number of elements in second array: "))
    arr2 = list(map(int, input("Enter sorted elements of second array: ").split()))

    # Add extra space in nums1
    nums1 = arr1 + [0] * n

    sol = Solution()
    sol.merge(nums1, m, arr2, n)

    print("Merged Array:", nums1)


if __name__ == "__main__":
    main()