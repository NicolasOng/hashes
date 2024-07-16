import hashlib

def read_string_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def hash_file_contents(file_path):
    contents = read_string_from_file(file_path)
    hash_object = hashlib.sha256(contents.encode())
    hash_hex = hash_object.hexdigest()
    return hash_hex

file_path = "files/2024-07-13.md"
print(f"File contents: {read_string_from_file(file_path)}")
print(f"SHA-256 hash: {hash_file_contents(file_path)}")

'''
files/2024-07-13.md: 7c05edfc9447820f4ea4a7328685c0e8f12600bba588e2ed096208187dcb16ce
'''
