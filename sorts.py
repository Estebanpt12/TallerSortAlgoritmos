class SortingAlgorithms:

    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    @staticmethod
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return SortingAlgorithms.quicksort(left) + middle + SortingAlgorithms.quicksort(right)

    @staticmethod
    def stooge_sort(arr, l=0, h=None):
        if h is None:
            h = len(arr) - 1
        if l >= h:
            return arr
        if arr[l] > arr[h]:
            arr[l], arr[h] = arr[h], arr[l]
        if h - l + 1 > 2:
            t = (h - l + 1) // 3
            SortingAlgorithms.stooge_sort(arr, l, h - t)
            SortingAlgorithms.stooge_sort(arr, l + t, h)
            SortingAlgorithms.stooge_sort(arr, l, h - t)
        return arr

    @staticmethod
    def pigeonhole_sort(arr):
        min_val = min(arr)
        max_val = max(arr)
        size = max_val - min_val + 1
        holes = [0] * size
        
        for x in arr:
            holes[x - min_val] += 1
        
        sorted_arr = []
        for i in range(size):
            while holes[i] > 0:
                sorted_arr.append(i + min_val)
                holes[i] -= 1
        return sorted_arr

    @staticmethod
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = SortingAlgorithms.merge_sort(arr[:mid])
        right = SortingAlgorithms.merge_sort(arr[mid:])
        
        return SortingAlgorithms.merge(left, right)

    @staticmethod
    def merge(left, right):
        sorted_arr = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        return sorted_arr

    @staticmethod
    def bitonic_sort(arr, up=True):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = SortingAlgorithms.bitonic_sort(arr[:mid], True)
        right = SortingAlgorithms.bitonic_sort(arr[mid:], False)
        
        return SortingAlgorithms.bitonic_merge(left + right, up)

    @staticmethod
    def bitonic_merge(arr, up):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        for i in range(mid):
            if (arr[i] > arr[i + mid]) == up:
                arr[i], arr[i + mid] = arr[i + mid], arr[i]
        
        left = SortingAlgorithms.bitonic_merge(arr[:mid], up)
        right = SortingAlgorithms.bitonic_merge(arr[mid:], up)
        
        return left + right
