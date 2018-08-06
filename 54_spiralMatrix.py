class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        # length of rows
        m = len(matrix)
        k = 0

        # Edge case handling
        if m == 0:
            return []

        # length of columns
        n = len(matrix[0])
        l = 0

        # result storing list
        result = []
        while k < m and l < n:

            # top row
            for i in range(l, n):
                result.append(matrix[k][i])
            k += 1

            # left column
            for i in range(k, m):
                result.append(matrix[i][n - 1])
            n -= 1

            # bottom row
            if k < m:
                for i in range(n - 1, l - 1, -1):
                    result.append(matrix[m - 1][i])
                m -= 1

            # left column
            if l < n:
                for i in range(m - 1, k - 1, -1):
                    result.append(matrix[i][l])
                l += 1
        return result
