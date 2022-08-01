def print_hash(value) -> None:
    try:
        hash_ = hash(value)
        print(f"Hash for '{value}' is {hash_}")
    except TypeError:
        print(f"Object of type {type(value)} is unhashable")


value_to_hash = input("Enter value to be hashed: ")
print_hash(value_to_hash)
