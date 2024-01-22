import hashlib

def hash_text(text):
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    return sha256_hash

def process_file(input_file, output_file):
    with open(input_file, 'r') as input_file:
        project_list = input_file.read().splitlines()

    hashed_projects = [hash_text(project) for project in project_list]

    with open(output_file, 'w') as output_file:
        for hashed_project in hashed_projects:
            output_file.write(hashed_project + '\n')


input_file_path = 'distributed-projects.txt'
output_file_path = 'distributed-sha.txt'

process_file(input_file_path, output_file_path)

print(f"Hashed values saved to {output_file_path}")
