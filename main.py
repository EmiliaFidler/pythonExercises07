# Exercises 07

# 01
def create_file(filename):
    names = ['Olivia', 'Liam', 'Emma', 'Noah', 'Sophia', 'Mason', 'Ava', 'James', 'Emma', 'Benjamin']
    # creating file and using modus 'write' for the names, seperated by commas
    with open(filename, 'w') as file:
        file.write(', '.join(names))


create_file('names.txt')


# 02
def transform_to_row(input_file: str, output_file: str):
    with open(input_file, 'r') as file:
        # reads the entire file and return its content as a single string
        content = file.read()
    # strip for removing white space and split for splitting into strings
    # list comprehension method: names = [name.strip() for name in content.split(',')]
    names = []
    for name in content.split(','):
        names.append(name.strip())

    with open(output_file, 'w') as file:
        file.write('\n'.join(names))


transform_to_row('names.txt', 'names_transformed.txt')


# 03
def add_greeting(input_file: str, output_file: str):
    with open(input_file, 'r') as file:
        # readlines = it reads all the lines
        lines = file.readlines()
    # list comprehension:
    names = [name.strip() for name in lines]
    names_with_greetings = ["Hello " + name for name in names]

    with open(output_file, 'w') as file:
        file.write('\n'.join(names_with_greetings))


add_greeting('names_transformed.txt', 'names_with_greetings.txt')


# 04
def strip_greeting(input_file: str, output_file: str):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    # list comprehension:
    # first strip to remove new line, second strip to remove greeting
    names = [line.strip().strip('Hello ') for line in lines]

    with open(output_file, 'w') as file:
        file.write('\n'.join(names))


strip_greeting('names_with_greetings.txt', 'names_stripped.txt')


# 05
def combine_files(file1: str, file2: str, output_file: str):
    with open(file1, 'r') as file:
        lines1 = file.readlines()

    with open(file2, 'r') as file:
        lines2 = file.readlines()

    if not len(lines1) == len(lines2):
        print('Error: Only files with the same amount of lines are supported.')
        return  # guard clause (Klaus the Guardian)

    lines_combined = []
    for i in range(len(lines1)):
        lines_combined.append(f"{lines1[i].strip()} {lines2[i].strip()}")

    with open(output_file, 'w') as file:
        file.write('\n'.join(lines_combined))


combine_files('names_with_greetings.txt', 'names_stripped.txt', 'names_combined.txt')
