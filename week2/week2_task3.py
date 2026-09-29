phone_list = [
    {'make': 'Google', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

result = sorted(phone_list, key=lambda x: int(x['model']), reverse=True)

print(result)