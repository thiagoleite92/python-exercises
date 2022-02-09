import requests

# for _ in range(15):
	# response = requests.get('https://www.cloudflare.com/rate-limit-test/')
	# print(response.status_code)

try:
	response = requests.get('http://httpbin.org/delay/10', timeout=2)
except requests.Timeout:
	response = requests.get('http://httpbin.org/delay/1', timeout=2)
finally:
	print(response.status_code)
