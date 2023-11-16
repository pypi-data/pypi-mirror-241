def mergeSort(A):
    if len(A) > 1:
            # divide
            m = len(A) // 2
            right = A[m:]
            left = A[:m]
            # conquer
            mergeSort(left)
            mergeSort(right)
            # combine
            i = 0; j = 0; n = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    A[n] = left[i]
                    i += 1
                else:
                    A[n] = right[j]
                    j += 1
                n += 1
            while i < len(left):
                A[n] = left[i]
                n += 1
                i += 1
            while j < len(right):
                A[n] = right[j]
                n += 1
                j += 1
    return A