# # friends = ["a", "b", "c"]
# # gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]
# friends = ["muzi", "ryan", "frodo", "neo"]
# gifts = ["muzi frodo", "ryan neo", "frodo neo", "muzi neo", "muzi frodo"]

# def solution(friends, gifts):

#     give = {friend: [] for friend in friends}
#     take = {friend: [] for friend in friends}
#     for gift in gifts:
#         a, b = gift.split()
#         give[a].append(b)
#         take[b].append(a)


#     # print(give)
#     # print(take)
    
#     for f in friends:
#         if f in give[f] and f in take[f]:


    
#     return 1

# if __name__ == "__main__":
#     print(solution(friends, gifts))  # 3