def print_hash(value) -> None:
    try:
        hash_ = hash(value)
        print(f"Hash for '{value}' is {hash_}")
    except TypeError:
        print(f"Object of type {type(value)} is unhashable")


s = "Python Bootcamp"
print_hash(s)
