class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        flightBookingCount = {}
        for booking in bookings:
            for temp in xrange(booking[0], booking[1] + 1):
                if temp not in flightBookingCount:
                    flightBookingCount[temp] = booking[2]
                else:
                    flightBookingCount[temp] += booking[2]
        sortedKeys = flightBookingCount.keys()
        for i in xrange(1,n+1):
            if i not in sortedKeys:
                sortedKeys.append(i)
                flightBookingCount[i] = 0
        sortedKeys = flightBookingCount.keys()
        sortedKeys.sort()
        return [flightBookingCount[i] for i in sortedKeys]


s = Solution()
print s.corpFlightBookings([[2,2,30],[2,2,45]], 2)
