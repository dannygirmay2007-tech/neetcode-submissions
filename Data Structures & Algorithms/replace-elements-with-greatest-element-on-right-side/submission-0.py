class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if (i+1) > len(arr)-1:
                arr[i] = -1
            else:
                new_arr = arr[i+1:]
                arr[i] = max(new_arr)
        return arr
            