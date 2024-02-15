def solution(sizes):
    max_width = 0
    max_height = 0

    for wid, hei in sizes:
        max_width = max(max_width, max(wid, hei))
        max_height = max(max_height, min(wid, hei))

    answer = max_width * max_height
    return answer

