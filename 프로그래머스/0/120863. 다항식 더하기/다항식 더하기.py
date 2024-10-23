def solution(_str):
    pl = _str.split()
    factor = 0
    const = 0

    for i in pl:
        if i.isdigit():
            const += int(i)
        else:
            if i == 'x':
                factor += 1
            elif len(i) > 1:
                factor += int(i[:-1])

    constant = f'{const}' if const != 0 else ''
    if factor == 0:
        answer = constant
    else:
        factors = f'{factor}x' if factor > 1 else 'x'
        answer = factors + ' + ' + constant if constant else factors
    return answer

