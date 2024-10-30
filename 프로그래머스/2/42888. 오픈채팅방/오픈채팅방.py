def solution(record):
    id_name = {}
    messages = []
    result = []
    
    # record를 ' ' 기준으로 나눈 후 id와 message를 list에 저장, id_name에 id: name 저장
    for rec in record:
        rec = rec.split()
        messages.append((rec[0], rec[1]))
        
        if rec[0] != 'Leave': # leave이면 index out range
            id_name[rec[1]] = rec[2]
    
    # message를 확인하고 해당 아이디의 닉네임을 id_name에서 출력 
    for message, id_ in messages:
        if message == 'Enter':
            result.append(id_name[id_] + '님이 들어왔습니다.')
            
        elif message == 'Leave':
             result.append(id_name[id_] + '님이 나갔습니다.')

    return result