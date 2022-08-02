import instaloader
import scraper
L = instaloader.Instaloader()

# login (username & password go here)
username = ""
password = ""
L.login(username, password)

# find out who isn't following back
profile = instaloader.Profile.from_username(L.context, username)

following_list = []
for user in profile.get_followees():
    following_list.append(user.username)

followers_list = []
for user in profile.get_followers():
    followers_list.append(user.username)

print("users not following back:")
for user in following_list:
    if user not in followers_list:
        print(user)
print("")

# find people with bad ratios
print("bad ratios:")
for i in range(0, 10):
    curr_user = following_list[i]
    arr = scraper.get_ratio(curr_user) # [followers, following]
    if arr[1] - arr[0] >= 100 or arr[0] / arr[1] <= 0.8:
        print(curr_user)