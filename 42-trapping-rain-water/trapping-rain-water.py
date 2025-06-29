class Solution:
    def trap(self,height: list[int]) -> int:
        """
        Computes how much rainwater can be trapped after raining, given an
        elevation map represented by a list of non-negative integers,
        using a two-pointer approach. The width of each bar is 1.

        Args:
            height: A list of non-negative integers representing the elevation map.

        Returns:
            The total amount of water that can be trapped.
        """
        n = len(height)

        # Edge case: If there are less than 3 bars, no water can be trapped.
        if n < 3:
            return 0

        # Initialize two pointers, one at the beginning and one at the end.
        left = 0
        right = n - 1

        # Initialize variables to keep track of the maximum height encountered
        # from the left and from the right.
        left_max = 0
        right_max = 0

        # Initialize the total trapped water.
        total_trapped_water = 0

        # Iterate while the left pointer is less than the right pointer.
        while left < right:
            # If the height at the left pointer is less than the height at the right pointer,
            # it means the water level at the current 'left' position will be limited
            # by the 'left_max'.
            if height[left] < height[right]:
                # If the current bar's height is greater than or equal to the
                # maximum seen so far from the left, update left_max. No water
                # can be trapped at this position if it forms a new maximum.
                if height[left] >= left_max:
                    left_max = height[left]
                # Otherwise, water can be trapped. The amount is (left_max - current_height).
                else:
                    total_trapped_water += left_max - height[left]
                # Move the left pointer to the right.
                left += 1
            # If the height at the right pointer is less than or equal to the height at the left,
            # it means the water level at the current 'right' position will be limited
            # by the 'right_max'.
            else:
                # If the current bar's height is greater than or equal to the
                # maximum seen so far from the right, update right_max. No water
                # can be trapped at this position if it forms a new maximum.
                if height[right] >= right_max:
                    right_max = height[right]
                # Otherwise, water can be trapped. The amount is (right_max - current_height).
                else:
                    total_trapped_water += right_max - height[right]
                # Move the right pointer to the left.
                right -= 1

        # Return the total calculated trapped water.
        return total_trapped_water
            