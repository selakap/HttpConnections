import http.client

connection = http.client.HTTPSConnection("run.mocky.io")
connection.request("GET", "/v3/a96c84ac-9d40-41d5-847a-025122ba6615")
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))
print(response.read().decode())
print(response.getheaders())

for x in range(6):
    response = connection.getresponse()
    print("Status: {} and reason: {}".format(response.status, response.reason))
    print(response.read().decode())
    print(response.getheaders())

connection.close()

