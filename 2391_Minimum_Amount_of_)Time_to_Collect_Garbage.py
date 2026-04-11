class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        #Calculate total number of characters --> Total time to pick the garbage
        #Find the last index where 'M', 'P' and 'G' occur
        #Use prefix_sum to calculate time
        travel_prefix = [0] * (len(travel) + 1)
        for i in range(len(travel)):
            travel_prefix[i + 1] = travel_prefix[i] + travel[i]
        
        total_time = 0
        last_indices = {'M': 0, 'P': 0, 'G': 0}
        
        for i, house in enumerate(garbage):
            total_time += len(house)
            

            for char in house:
                last_indices[char] = i
                

        for char in last_indices:
            last_house_idx = last_indices[char]
            total_time += travel_prefix[last_house_idx]
            
        return total_time