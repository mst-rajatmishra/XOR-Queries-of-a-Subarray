from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        
        # Step 1: Compute the prefix XOR array
        prefixXOR = [0] * n
        prefixXOR[0] = arr[0]
        for i in range(1, n):
            prefixXOR[i] = prefixXOR[i - 1] ^ arr[i]
        
        # Step 2: Process each query using the prefix XOR array
        result = []
        for left, right in queries:
            if left == 0:
                result.append(prefixXOR[right])
            else:
                result.append(prefixXOR[right] ^ prefixXOR[left - 1])
        
        return result