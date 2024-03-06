from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_dict = defaultdict(list)

    # 각 장르별로 노래 정보를 저장
    for i in range(len(genres)):
        genre = genres[i]
        play_count = plays[i]
        genre_dict[genre].append((i, play_count))

    # 재생 횟수가 많은 장르 순서대로 정렬
    sorted_genres = sorted(genre_dict.keys(), key=lambda genre: sum(song[1] for song in genre_dict[genre]), reverse=True)

    # 각 장르별로 노래를 재생 횟수 내림차순, 고유 번호 오름차순으로 정렬하여 최대 2개씩 answer에 추가
    for genre in sorted_genres:
        songs = sorted(genre_dict[genre], key=lambda song: (song[1], -song[0]), reverse=True)
        answer.extend([song[0] for song in songs[:2]])

    return answer
