class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        ans= sum(distance)
        s = min(start, destination)
        m = max(start, destination)
        s_d = sum(distance[s:m])
        return min(s_d, ans-s_d)