import hashlib

def hash_text(text):
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    return sha256_hash

cipher_dictionary = {
    "apache": hash_text("apache"),
    "firefox": hash_text("firefox"),
    "linux": hash_text("linux"),
}

def find_key_of_hash(input_hash, dictionary):
    for tool, hashed_value in dictionary.items():
        if input_hash == hashed_value:
            return tool
    return None

user_input_hash = input("Enter a SHA-256 hash: ")

found_tool = find_key_of_hash(user_input_hash, cipher_dictionary)

if found_tool:
    print(f"The hash corresponds to: {found_tool}")
else:
    print("No matching hash found.")
