class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_h = len(matrix)
        matrix_w = len(matrix[0])
        hl, hr = 0, matrix_h - 1
        wl, wr = 0, matrix_w - 1
        while hl <= hr:
            half_h = (hl + hr) // 2
            if matrix[half_h][0] > target:
                hr = half_h - 1
            elif matrix[half_h][0] < target:
                if matrix[half_h][matrix_w-1] > target:
                    # find width
                    while wl <= wr:
                        half_w = (wl + wr) // 2
                        if matrix[half_h][half_w] > target:
                            wr = half_w - 1
                        elif matrix[half_h][half_w] < target:
                            wl = half_w + 1
                        else:
                            return True
                    return False
                elif matrix[half_h][matrix_w-1] < target:
                    hl = half_h + 1
                else:
                    return True
            else:
                return True
        return False
        