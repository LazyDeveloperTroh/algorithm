import re
def solution(new_id):
    print(new_id)
    new_id = new_id.lower()                                 # 1
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)            # 2
    new_id = re.sub('\.+', '.', new_id)                     # 3
    new_id = re.sub('^[.]|[.]$', '', new_id)                # 4
    new_id = "a" if len(new_id) == 0 else new_id[:15]       # 56
    new_id = re.sub('^[.]|[.]$', '', new_id)
    while len(new_id) < 3:                                  
        new_id = new_id + new_id[len(new_id)-1]             #7

    answer = new_id
    return answer

print(solution("z-+.^."))