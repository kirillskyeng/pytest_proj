def get_val(collection, key, default='git'):
    if key in collection:
        return collection[key]
    return default

