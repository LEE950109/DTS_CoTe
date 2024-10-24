def solution(dots):
    x1, y1 =dots.pop()
    for i in range(3):
        copy_dots = dots.copy()
        x2, y2 = copy_dots.pop(i)
        x3, y3 = copy_dots[0]
        x4, y4 = copy_dots[1]

        inc1 = (y1 - y2)/(x1 - x2)
        inc2 = (y3 - y4)/(x3 - x4)
        print(f"({x1, y1}, {x2, y2}, {x3, y3}, {x4, y4})")

        if inc1 == inc2:
            return 1
    return 0
