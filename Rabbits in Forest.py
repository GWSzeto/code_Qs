# 781. Rabbits in Forest
class Solution:
    def numRabbits(self, answers):
        other_rabbits = {}
        total = 0
        for ans in answers:
            if ans == 0:
                total += 1
            elif ans not in other_rabbits:
                other_rabbits[ans] = ans
                total += ans + 1
            else:
                other_rabbits[ans] -= 1
                if other_rabbits[ans] == 0:
                    del other_rabbits[ans]
		
        return total