import requests

def get_ratio(user):
    
    numbers = "0123456789"
    url = "http://www.instagram.com/" + user
    response = requests.get(url).text

    followers_str = ""
    followers_str_trimmed = ""
    start = response.find("edge_followed_by")
    for i in range(start, start + 40):
        followers_str += response[i]
    for i in range(0, len(followers_str)):
        if followers_str[i] in numbers:
            followers_str_trimmed += followers_str[i]

    following_str = ""
    following_str_trimmed = ""
    start = response.find("edge_follow\\")
    for i in range(start, start + 40):
        following_str += response[i]
    for i in range(0, len(following_str)):
        if following_str[i] in numbers:
            following_str_trimmed += following_str[i]

    return [int(followers_str_trimmed), int(following_str_trimmed)]