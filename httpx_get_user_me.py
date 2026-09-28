import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}
login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(login_response.status_code)
print(login_response.json())

access_payload = login_response_data['token']['accessToken']

access_response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers={"Authorization": f"Bearer {access_payload}"})
access_response_data = access_response.json()
print(access_response.status_code)
print(access_response.json())