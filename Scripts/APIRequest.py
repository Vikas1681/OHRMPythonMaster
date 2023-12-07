import requests
# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context

uri ='https://reqres.in/api/users?page=2'
response=requests.get(uri,verify=False)
print(response.content)
