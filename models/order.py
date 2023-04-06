class Order():
    """Method docstring."""
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, metalId, styleId, typeId, sizeId, optionId, timestamp):
        """Method docstring."""
        self.id = id
        self.metalId = metalId
        self.styleId = styleId
        self.typeId = typeId
        self.sizeId = sizeId
        self.optionId = optionId
        self.timestamp = timestamp