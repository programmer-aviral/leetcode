class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        # Store reserved seats for each row
        for row, seat in reservedSeats:
            rows[row] = rows.get(row, 0) | (1 << seat)

        # Every completely empty row can fit 2 groups
        answer = (n - len(rows)) * 2

        for row, mask in rows.items():
            # Seats 2,3,4,5
            left = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)

            # Seats 4,5,6,7
            middle = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)

            # Seats 6,7,8,9
            right = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)

            if mask & left == 0:
                answer += 1
                if mask & right == 0:
                    answer += 1
            elif mask & middle == 0:
                answer += 1
            elif mask & right == 0:
                answer += 1

        return answer
