class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        size = len(s1)

        for start in range(len(s2) - size + 1):
            end = start + size
            substring = s2[start:end]

            if Counter(substring) == target:
                return True

        return False

