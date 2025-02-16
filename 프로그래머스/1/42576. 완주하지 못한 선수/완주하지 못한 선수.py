from collections import Counter

def solution(participant, completion):
    """완주하지 못한 선수들의 이름이 담긴 배열을 return 하는 함수
    parameter:
        participant: 마라톤에 참여한 선수들의 이름이 담긴 배열
        completion: 완주한 선수들의 이름이 담긴 배열 
    """
    # 1. 마라톤의 참여한 선수들의 이름이 담긴 배열 - 완주한 선수들의 이름이 담긴 배열 (동명이인 주의)
    p_counter = Counter(participant)
    c_counter = Counter(completion)

    result = list((p_counter - c_counter).elements())
    
    return next(iter(result), None)