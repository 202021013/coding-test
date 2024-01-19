import collections
def solution(participant, completion):
    par_di = collections.Counter(participant)
    com_di = collections.Counter(completion)
    
    for key, value in par_di.items():
        if value - com_di.get(key, 0) != 0:
            return key