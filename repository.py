DATABASE = {
    "metals": [
    {
      "id": 1,
      "metal": "Sterling Silver",
      "price": 12.42
    },
    {
      "id": 2,
      "metal": "14K Gold",
      "price": 736.4
    },
    {
      "id": 3,
      "metal": "24K Gold",
      "price": 1258.9
    },
    {
      "id": 4,
      "metal": "Platinum",
      "price": 795.45
    },
    {
      "id": 5,
      "metal": "Palladium",
      "price": 1241
    }
  ], 
  "orders": [
    {
            "id": 1,
            "metalId": 3,
            "sizeId": 2,
            "styleId": 3,
            "optionId": 1,
            "typeId": 2,
            "timestamp": 1614659931693
        }
  ],
  "sizes": [
    { "id": 1, "carets": 0.5, "price": 405 },
    { "id": 2, "carets": 0.75, "price": 782 },
    { "id": 3, "carets": 1, "price": 1470 },
    { "id": 4, "carets": 1.5, "price": 1997 },
    { "id": 5, "carets": 2, "price": 3638 }
  ],
  "styles": [
    { "id": 1, "style": "Classic", "price": 500 },
    { "id": 2, "style": "Modern", "price": 710 },
    { "id": 3, "style": "Vintage", "price": 965 }
  ]
}


def all(resource):
    """For GET requests to collection"""
    return DATABASE[resource]


def retrieve(resources, id):
    """For GET requests to a single resource"""
    requested_resource = None

    for resource in DATABASE[resources]:
        if resource["id"] == id:
            requested_resource = resource.copy()

    return requested_resource


def create(resource, new_resource):
    """For POST requests to a collection"""
    max_id = DATABASE[resource][-1]["id"]

    new_id = max_id + 1

    new_resource["id"] = new_id

    DATABASE[resource].append(new_resource)

    return new_resource


def update(resources, id, new_resource):
    """For PUT requests to a single resource"""
    for index, resource in enumerate(DATABASE[resources]):
        if resource["id"] == id:
            DATABASE[resources][index] = new_resource
            break


def delete(resources, id):
    """For DELETE requests to a single resource"""
    resource_index = -1

    for index, resource in enumerate(DATABASE[resources]):
        if resource["id"] == id:
            resource_index = index

    if resource_index >= 0:
        DATABASE[resources].pop(resource_index)