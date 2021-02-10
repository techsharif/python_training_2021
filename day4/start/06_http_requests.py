# # 01
# # requests
# # need pip
# # pip install requests
# import requests
# url = "http://www.google.com"
# response = requests.get(url)

# print(f"your request to {url} came back w/ status code {response.status_code}")

# print(response.text)



# # 02
# # header
# import requests
# url = "https://icanhazdadjoke.com/"
# response = requests.get(url, headers={"Accept": "application/json"})
# print(response.text)


# import requests
# url = "https://icanhazdadjoke.com/"
# response = requests.get(url, headers={"Accept": "application/json"})
# print(response.text)




# # 03
# # params
# import requests
# url = "https://icanhazdadjoke.com/search"

# response = requests.get(
# 	url, 
# 	headers={"Accept": "application/json"},
# 	params={"term": "cat"}
# )

# print(response.text)
