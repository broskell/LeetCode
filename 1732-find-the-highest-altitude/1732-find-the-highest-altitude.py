class Solution(object):
    def largestAltitude(self, gain):
        high, netGain = 0, 0

        for altitude in gain:
            netGain += altitude
            high = max(high, netGain)
        return high