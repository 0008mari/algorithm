def solution(s):
    answer = 0
    complenlist = []   # 길이의 리스트 
    for length in range(1, len(s)//2+1):
        # length는 끊어서 검사할 단위
        # 1단계 - 개수대로 자르기 
        cuts = [s[i:i+length] for i in range(0, len(s), length)]
        # 2단계 - 압축하기
        compressed = ""
        i=0
        while(i<len(cuts)):
            count = 0
            for j in range(i, len(cuts)):
                if cuts[i] != cuts[j]:
                    break
                else:
                    count += 1
            if count == 1:
                countstring = ""
            else:
                countstring = str(count)
            compressed = compressed + countstring + cuts[i]
            i += count
        complenlist.append(len(compressed))
    # 압축 길이의 리스트에서 최솟값의 인덱스를 answer로
    answer = min(complenlist)

    return answer


s = input()
print(solution(s))