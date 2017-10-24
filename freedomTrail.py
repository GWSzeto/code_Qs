class Solution(object):
    def findRotateSteps(self, ring, key):
        def dist(start, end):
            return min(abs(end - start), len(ring) - abs(end - start))

        char_pos = {}
        for ind, char in enumerate(ring):
            if char in char_pos: char_pos[char].append(ind)
            else: char_pos[char] = [ind]

        starting_pos = {0:0}
        for char in key:
            next_pos = {}
            for target_pos in char_pos[char]:
                next_pos[target_pos] = float('inf')
                for start_pos in starting_pos:
                    next_pos[target_pos] = min(next_pos[target_pos], dist(start_pos, target_pos) + starting_pos[start_pos])
            starting_pos = next_pos

        return min(starting_pos.values()) + len(key)
