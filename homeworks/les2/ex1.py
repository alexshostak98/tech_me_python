users = (
    {
        'name': 'Jon',
        'surname': 'Smith',
        'age': 6
    },
    {
        "name": "Bill",
        "surname": "Suns",
        "age": 20
    }
)

templates = (
    "{name} {surname} закончил школу",
    "{name} {surname} скоро пойдет в школу"
)
result = templates[not users[0]['age'] > 7]
print(result.format(name=users[0]['name'], surname=users[0]['surname']))
