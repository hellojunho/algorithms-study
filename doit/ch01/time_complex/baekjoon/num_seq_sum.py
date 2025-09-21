n = int(input())

arr = [i for i in range(1, n+1)]

# print(arr)

start_index = 1
end_index = 1
count = 1
sum = 1

while end_index != n:
    if sum < n:
        end_index += 1
        sum += arr[end_index - 1]
    elif sum > n:
        sum -= arr[start_index - 1]
        start_index += 1
    else:
        count += 1
        end_index += 1
        sum += arr[end_index - 1]

print(count)