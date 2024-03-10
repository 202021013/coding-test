def solution(data, ext, val_ext, sort_by):
    col = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    # 조건에 맞는 데이터 추출
    filtered_data = [item for item in data if item[col[ext]] < val_ext]
    
    # 정렬 기준에 따라 데이터 정렬
    sorted_data = sorted(filtered_data, key=lambda x: x[col[sort_by]])
    
    return sorted_data