def solution(nums):
    len_nums = len(set(nums))         # 중복제거(같은종류는 같은번호)
    return min(len_nums, len(nums) // 2) # 중복제거한 nums랑 nums//2로 나눈값중 더 작은 값