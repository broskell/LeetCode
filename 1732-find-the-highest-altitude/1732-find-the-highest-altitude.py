class Solution(object):
    def largestAltitude(self, gain):
        high, netGain = 0, 0

        for i, altitude in enumerate(gain):
            netGain += altitude
            high = max(high, netGain)
        return high