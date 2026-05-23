class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        if not logs:
            return [0] * k

        res = [0] * k
        users_active_map = defaultdict(set)
        for user_id, active_minute in logs:
            users_active_map[user_id].add(active_minute)
        
        for user_id, minute_list in users_active_map.items():
            res[len(minute_list) - 1] += 1
        return res