class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i]) # 현재 위치에서 가장 멀리갈 수 있는 인덱스

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
