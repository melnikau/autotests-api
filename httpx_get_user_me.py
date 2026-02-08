import httpx

login_payload = {
  "email": "a.melnikau@example.com",
  "password": "Pass123"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Status code: ", login_response.status_code)
print("Login response: ", login_response_data)


client = httpx.Client(headers={"Authorization": f'Bearer {login_response_data['token']['accessToken']}'})

user_me_response = client.get("http://localhost:8000/api/v1/users/me")
user_me_response_data = user_me_response.json()
print("Status code: ", user_me_response.status_code)
print("User_me response: ", user_me_response_data)