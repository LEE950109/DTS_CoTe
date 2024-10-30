def solution(record):
    id_name = {}
    messages = []
    result = []

    for rec in record:
        rec = rec.split()
        messages.append((rec[0], rec[1]))
        
        if rec[0] != 'Leave':
            id_name[rec[1]] = rec[2]

    for message, id_ in messages:
        if message == 'Enter':
            result.append(id_name[id_] + '님이 들어왔습니다.')
            
        elif message == 'Leave':
             result.append(id_name[id_] + '님이 나갔습니다.')

    return result