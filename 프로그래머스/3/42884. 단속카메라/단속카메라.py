def solution(routes):
    imp = []
    # 시작이랑 끝 크기 비교해서 정렬
    # for route in routes:
    #     s, e = route
    #     if s <= e:
    #         imp.append([s, e])
    #     else:
    #         imp.append([e, s])
            
    routes.sort() # 혹시 정렬 안되어 있을까봐
    
    cctv = 1
    idx = 0
    
    ds, de = -300000, 300000
    
    for ns, ne in routes:
        ds = ns
        
        if ns > de:
            de = ne
            cctv += 1
            continue
            
        if ns <= de:
            if de > ne:
                de = ne
            continue

    
    return cctv