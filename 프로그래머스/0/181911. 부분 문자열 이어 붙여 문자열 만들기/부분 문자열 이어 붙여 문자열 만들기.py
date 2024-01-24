def solution(my_strings, parts):
    result = []

    for my_str, part in zip(my_strings, parts):
        start, end = part
        substring = my_str[start:end+1]
        result.append(substring)

    return ''.join(result)