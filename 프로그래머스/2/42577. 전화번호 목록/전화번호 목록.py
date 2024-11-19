def solution(phone_book):
    """
    전화번호부에서 한 번호가 다른 번호의 접두어인지 확인하는 함수.

    매개변수:
    - phone_book: 문자열로 이루어진 전화번호 리스트.

    반환값:
    - 접두어 관계가 있으면 False 반환.
    - 접두어 관계가 없으면 True 반환.
    """

    # 1. 전화번호 리스트를 정렬. 정렬하면 접두어 관계가 있는 번호가 인접하게 배치됨.
    phone_book.sort()

    # 2. 정렬된 리스트에서 인접한 번호를 비교.
    for i in range(len(phone_book) - 1):
        
        # 현재 번호와 다음 번호의 첫 글자가 같다면 접두어 관계를 확인.
        if phone_book[i][0] == phone_book[i + 1][0]:
            l = len(phone_book[i]) # 현재 번호의 길이를 계산.
            
            # 다음 번호의 앞부분이 현재 번호와 같은지 확인.
            if phone_book[i] in phone_book[i + 1][:l]:
                return False  # 접두어 관계가 있으면 False 반환.

    # 3. 접두어 관계가 없으면 True 반환.
    return True
