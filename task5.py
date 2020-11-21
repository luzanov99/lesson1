#task5
places={"city": "Москва", "temperature": "20"}
print(places["city"])
places["temperature"]=int(places["temperature"])-5
print(places)
places.get("country", "Россия")
places["country"] = "Россия"
places["date"] = "27.05.2019"
print(len(places))