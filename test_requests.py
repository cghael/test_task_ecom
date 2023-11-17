import requests


url = 'http://127.0.0.1:8000/get_form'

# Test Case 1: Valid data
valid_data = {'feedback_date': '2023-11-17', 'participant_name': 'Lolkek', 'comments': 'cheburek'}
response = requests.post(url, data=valid_data)
print('Valid data:', response.json())

# Test Case 2: Invalid date format
invalid_date_data = {'feedback_date': '17 november 2023', 'participant_name': 'Lolkek', 'comments': 'cheburek'}
response = requests.post(url, data=invalid_date_data)
print('Invalid date format:', response.json())

# Test Case 3: Invalid phone format
invalid_phone_data = {'user_name': 'Pipa', 'user_email': 'test@test.com', 'register_date': '2023-11-17', 'phone_number': '+78889993322'}
response = requests.post(url, data=invalid_phone_data)
print('Invalid phone format:', response.json())

# Test Case 4: Empty text format
invalid_text_data = {'user_name': '', 'user_email': 'test@test.com', 'register_date': '2023-11-17', 'phone_number': '+7 888 999 33 22'}
response = requests.post(url, data=invalid_text_data)
print('Empty text format:', response.json())

# Test Case 5: Invalid email format
empty_email_data = {'user_name': 'Test', 'user_email': 'test@test', 'register_date': '2023-11-17', 'phone_number': '+7 888 999 33 22'}
response = requests.post(url, data=empty_email_data)
print('Invalid email format:', response.json())

# Test Case 6: Invalid all formats
empty_all_data = {'user_name': '', 'user_email': 'test@test', 'register_date': '20231117', 'phone_number': '+7 888 999 33 225'}
response = requests.post(url, data=empty_all_data)
print('Invalid all formats:', response.json())

# Test Case 7: Template not found
not_found_data = {'feedback_date': '2023-11-17', 'participant_name': 'Lolkek'}
response = requests.post(url, data=not_found_data)
print('Template not found:', response.json())