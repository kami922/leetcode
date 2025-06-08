class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_set = set() # This set will store elements within the current window of size k

        for i, num in enumerate(nums):
            # If the current element is already in our window (set), it's a duplicate within k distance
            if num in window_set:
                return True

            # Add the current element to the window
            window_set.add(num)

            # If the window size exceeds k, remove the element that just "fell out" of the window
            # The element falling out is at index i - k
            if len(window_set) > k: # This condition implicitly checks if i >= k
                                    # For example, if k=3, for i=3, the window is nums[0], nums[1], nums[2], nums[3] (size 4).
                                    # At i=3, num=nums[3] is added, now window_set has 4 elements if unique.
                                    # The element at index i-k (which is 0) should be removed.
                window_set.remove(nums[i - k]) # This assumes k >= 1. If k=0, it's handled by other logic.

        return False # No duplicate found within k distance after checking all elements
