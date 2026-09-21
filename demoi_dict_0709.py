#item = {}
item = {
    "title": "shooes",
    "color": "black",
    "size": 42,
    "supplers": ["OOO..","OAO..."]
}
#print(type(item))
#item["title"] = "Hat"
#item["brand"] = "Reebok"
#print(item["color"])
#print(item)

#for key in item:
#    print(key)

#перебор пары ключ, значение
#for key, value in item.items():
#    print(value)

#for key in items.keys():
#    print(key)

#print(item)

people = {
    "name": "Ivan",
    "age": 34,
    "address": {
        "city": "Moscow",
        "street": "Lenina 64",
        "apartment": "20"
    },
    "children": [
        {
        "name": "Petr",
        "age": 7
        },
        {
          "name": "Anna",
            "age": 12
        }
    ]

}
#print(people["children"][0]["name"])
#print(people.items())
print(people.get("name"))
print(people["name"])
print(people.get("job", "not found"))