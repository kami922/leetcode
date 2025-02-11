class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        lenOfTimeArr = len(startTime)
        count = 0
        for index in range(0,lenOfTimeArr):
            if queryTime >= startTime[index] and queryTime <= endTime[index]:
                count += 1
        return count
        