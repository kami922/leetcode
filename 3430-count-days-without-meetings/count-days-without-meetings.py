class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        l, r = meetings[0][0], meetings[0][1]
        for i in range(len(meetings)):
            if r >= meetings[i][0]:
                r = max(meetings[i][1], r)
            else:
                days -= r - l + 1
                l, r = meetings[i][0], meetings[i][1]
        return days - (r - l + 1)
        