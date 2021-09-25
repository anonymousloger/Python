input_from_question = input()

def solution(input_from_question):
    num = list(map(int,input_from_question.split()))
    num.sort()
    return num[1]

print(solution(input_from_question))