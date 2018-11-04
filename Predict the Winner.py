class Solution:
    def winner(self, nums, s, e, turn):
        if s == e:
            return turn * nums[s]
        route1 = turn * nums[s] + self.winner(nums, s + 1, e, -turn)
        route2 = turn * nums[e] + self.winner(nums, s, e - 1, -turn)

        return max(turn * route1, turn * route2)

    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return self.winner(nums, 0, len(nums) - 1, 1) >= 0
