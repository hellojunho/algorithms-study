def solution(numbers, target):
    leaves = [0]
    count = 0
    
    for i in numbers:
        temp = []
        for j in leaves:
            temp.append(j + i)
            temp.append(j - i)
            
        leaves = temp
        
    for l in leaves:
        if l == target:
            count += 1
    
    return count
                

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))  # 5
# https://school.programmers.co.kr/learn/courses/30/lessons/431870