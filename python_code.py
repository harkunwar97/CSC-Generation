inputJson = [
    {
      "name": "Accessories",
      "id": 1,
      "parent_id": 20,
    },
    {
      "name": "Watches",
      "id": 57,
      "parent_id": 1
    },
    {
      "name": "Men",
      "id": 20,
      "parent_id": None
    },
    {
      "name": "Outfit",
      "id": 40,
      "parent_id": 30
    },
    {
      "name": "Women",
      "id": 30,
      "parent_id": None
    },
    {
      "name": "Trans",
      "id": 67,
      "parent_id": None
    }
  ]

def find_all_childs(parent_id, inputJson, my_json):
    for i in inputJson:
        if i.get('parent_id') == parent_id:
            my_json.append(i)
            find_all_childs(i.get('id'), inputJson, my_json)
    return my_json

def sortCategoriesForInsert(inputJson):
    properJsonOutput = []
    for j in inputJson:
        if j.get('parent_id') == None:
            properJsonOutput.append(j)
            find_all_childs(j.get('id'), inputJson, properJsonOutput)
    return properJsonOutput

sortCategoriesForInsert(inputJson)