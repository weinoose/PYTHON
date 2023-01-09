import json

# # #

file = open("followers.json", "r")

followers_l = []
following_l = []

followers = json.loads(file.read())
file.close()

for i in followers["relationships_followers"]:
    with open('followers.txt','w',encoding='UTF-8') as file:
        followers_l.append(i["string_list_data"][0]["value"])

file = open("following.json", "r")

following = json.loads(file.read())
file.close()

for i in following["relationships_following"]:
    with open('following.txt','w',encoding='UTF-8') as file:
        following_l.append(i["string_list_data"][0]["value"])

# # #

print("\nAccounts that you've followed but not get followed back:")
t0 = 0
for j in following_l:
    if j not in followers_l:
        print(j)
        t0 += 1
print(f'Total amount of: {t0}')

print("\nAccounts that you've followed you but you did not get followed back him/her:")
t0 = 0
for j in followers_l:
    if j not in following_l:
        print(j)
        t0 += 1
print(f'Total amount of: {t0}')