import sys

class Solution(object):
    min_steps = sys.maxint
    def rotation(self, ring, key, steps, ring_pos, key_pos):
        if key_pos == len(key):
            self.min_steps = steps if steps < self.min_steps else self.min_steps
            return 
        
        for number_of_rotations in xrange(len(ring)):
            clockwise_flag = False
            counter_flag = False
            # going clockwise
            clockwise_pos = (ring_pos + number_of_rotations) % len(ring)
            if ring[rotate_pos] == key[key_pos]:
                self.rotation(ring, key, steps + number_of_rotations + 1, clockwise_pos, key_pos + 1)

            # going counter clockwise
            counter_pos = (ring_pos - number_of_rotations) % len(ring)
            if ring[rotate_pos] == key[key_pos]:
                self.rotation(ring, key, steps + number_of_rotations + 1, counter_pos, key_pos + 1)

            if clockwise_flag and counter_flag:
                break

        return self.min_steps
    
    def findRotateSteps(self, ring, key):
        return self.rotation(self, ring, key, 0, 0, 0)


