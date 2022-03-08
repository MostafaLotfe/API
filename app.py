import requests

# response = requests.get(
#     "https://www.nicepng.com//png/detail/70-702215_building-with-python-requests-python-requests-logo.png")

# print(type(response.json()))
# print(type(response.content))
# print(response.json())

# print('\n')

# print(response.json()['headers'])
# print(response.content)


#  Getting the image and Create it:
# ----------------------------------

# img_name = input("Enter the image name: ")
# img_url = input("Enter the image URL: ")
# img_name_with_its_extension = f"{img_name}.{img_url.split('.')[-1]}"
# response = requests.get(img_url)

# The image name with its extension : {img_name}.{img_url.split('.')[-1]}

# with open(img_name_with_its_extension, 'wb') as f:
#     f.write(response.content)        # Create image

url = "https://httpbin.org/get"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

response = requests.get(url, headers=headers)

print(response.headers)
