SIZES = [
    { "id": 1, "carets": 0.5, "price": 405 },
    { "id": 2, "carets": 0.75, "price": 782 },
    { "id": 3, "carets": 1, "price": 1470 },
    { "id": 4, "carets": 1.5, "price": 1997 },
    { "id": 5, "carets": 2, "price": 3638 }
  ]

def get_all_sizes():
    return SIZES
    
# Function with a single parameter
def get_single_size(id):
    # Variable to hold the found size, if it exists
    requested_size = None

    # Iterate the SIZES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for size in SIZES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if size["id"] == id:
            requested_size = size

    return requested_size
def create_size(size):
    """Method docstring."""
    # Get the id value of the last size in the list
    max_id = SIZES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the size dictionary
    size["id"] = new_id

    # Add the size dictionary to the list
    SIZES.append(size)

    # Return the dictionary with `id` property added
    return size
def delete_sizes(id):
    """Method docstring."""
    # Initial -1 value for sizes index, in case one isn't found
    sizes_index = -1

    # Iterate the SIZES list, but use enumerate() so that you
    # can access the index value of each item
    for index, sizes in enumerate(SIZES):
        if sizes["id"] == id:
            # Found the sizes. Store the current index.
            sizes_index = index

    # If the sizes was found, use pop(int) to remove it from list
    if sizes_index >= 0:
        SIZES.pop(sizes_index)
def update_size(id, new_size):
    """Method docstring."""
    # Iterate the SIZES list, but use enumerate() so that
    # you can access the index value of each item.
    for index, size in enumerate(SIZES):
        if size["id"] == id:
            # Found the size. Update the value.
            SIZES[index] = new_size
            break