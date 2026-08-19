class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """

        # Store reserved seats for only the rows that matter
        rows = {}

        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        # Every completely empty row can fit 2 families
        ans = (n - len(rows)) * 2

        # Check rows having reserved seats
        for seats in rows.values():

            left = all(seat not in seats for seat in [2, 3, 4, 5])
            middle = all(seat not in seats for seat in [4, 5, 6, 7])
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            if left and right:
                # Can place one family on each side
                ans += 2

            elif left or middle or right:
                # Can place one family
                ans += 1

        return ans