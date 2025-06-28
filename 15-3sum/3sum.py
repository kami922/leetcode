class Solution:
    def threeSum(self,nums):
        """
        Finds all unique triplets in the array nums which give the sum of zero.

        Args:
            nums: A list of integers.

        Returns:
            A list of lists, where each inner list is a unique triplet [a, b, c] such that a + b + c == 0.
        """
        # Step 1: Sort the input array.
        # Sorting is crucial for two main reasons:
        # 1. It allows us to use the two-pointer technique efficiently.
        # 2. It makes handling duplicate triplets much easier.
        nums.sort()

        # Get the length of the sorted array.
        n = len(nums)

        # Initialize an empty list to store the unique triplets that sum to zero.
        res = []

        # Step 2: Iterate through the array with the first pointer 'i'.
        # We iterate up to n - 2 because we need at least two more elements (left, right)
        # after 'i' to form a triplet.
        for i in range(n - 2):
            # Optimization: Skip duplicate values for the first element (nums[i]).
            # If the current nums[i] is the same as the previous nums[i-1],
            # it means we would find the same triplets again, so we skip it.
            # This check is only done if i > 0 to avoid an IndexError for nums[-1].
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 3: Initialize two pointers, 'left' and 'right', for the remaining subarray.
            # 'left' starts just after 'i'.
            # 'right' starts at the very end of the array.
            left, right = i + 1, n - 1

            # Step 4: Use the two-pointer technique to find pairs that sum to -nums[i].
            # The loop continues as long as the left pointer is to the left of the right pointer.
            while left < right:
                # Calculate the current sum of the triplet (nums[i] + nums[left] + nums[right]).
                s = nums[i] + nums[left] + nums[right]

                # Case 1: Sum is zero. We found a valid triplet.
                if s == 0:
                    # Add the triplet to our result list.
                    res.append([nums[i], nums[left], nums[right]])

                    # Move both pointers inwards to look for other potential triplets.
                    # We move them by one first, then handle duplicates.
                    left += 1
                    right -= 1

                    # Optimization: Skip duplicate values for 'left' pointer.
                    # After finding a triplet, if the new nums[left] is the same as
                    # the previous nums[left - 1], increment 'left' again to avoid duplicate triplets.
                    # This continues as long as left is still less than right.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Optimization: Skip duplicate values for 'right' pointer.
                    # Similarly, if the new nums[right] is the same as
                    # the previous nums[right + 1], decrement 'right' again.
                    # This continues as long as left is still less than right.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # Case 2: Sum is less than zero.
                # This means the sum is too small. To increase the sum, we need a larger number.
                # Since the array is sorted, we move the 'left' pointer to the right.
                elif s < 0:
                    left += 1
                # Case 3: Sum is greater than zero.
                # This means the sum is too large. To decrease the sum, we need a smaller number.
                # Since the array is sorted, we move the 'right' pointer to the left.
                else:  # s > 0
                    right -= 1

        # Step 5: Return the list of all unique triplets that sum to zero.
        return res
