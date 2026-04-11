class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        #The number of bits that are different between two numbers is known as the Hamming Distance.
        #We can find this by calculating c xor k and counting the number of set bits (1s) in the result.
        current_xor = 0
        for num in nums :
            current_xor ^= num

        diff = current_xor ^ k

        return bin(diff).count('1')