class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A

        m = len(A)
        n = len(B)

        half = (m + n + 1) // 2

        l, r = 0, m

        while True:

            i = (l + r) // 2

            j = half - i

            A_left = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i] if i < len(A) else float("inf")

            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < len(B) else float("inf")

            if A_left <= B_right and A_right >= B_left:
                if (m + n) % 2 == 1:
                    return max(A_left, B_left)

                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2

            
            elif A_left > B_right:
                r = i - 1

            else:
                l = i + 1

 
            # [1, 3, 8]       [1]       [3, 8]
            # [2, 5, 9, 10]   [2, 5, 9] [10]

            # [1, 3]  [8, 10]
            # [2, 5]  [9, 10]













        