# 길이 5까지 모든 모음으로 만들 수 있는 수를 만들어 리스트에 넣는다
# 리스트에서 몇번째인지 찾기
lst=[]

def solution(word):
    global lst
    answer = 0
    words=[]
    find_all(words)
    
    idx=0
    ans = lst.index(word)
    print(ans,'ans')
    for i in lst:
        if i == word:
            break
        idx+=1
    # print(idx)
    # ans = lst.find(word)
    # print(ans)
    return idx

def find_all(wrd):
    global lst
    vowel=['A','E','I','O','U']
    lst.append(''.join(chr for chr in wrd))
    if len(wrd)==5:
        return
    for i in range(5):
        wrd.append(vowel[i])
        find_all(wrd)
        wrd.pop()
        