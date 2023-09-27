import os

# Specify the directory of your Python project.
project_directory = '/home/harry/Documents/ai2cyber/'

# Specify the output file where the concatenated content will be saved.
output_file = 'concatenated_code.py'

# Function to concatenate the contents of all Python files in a directory.


def concatenate_python_files(directory, output_file):
    with open(output_file, 'w') as output:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as input_file:
                        output.write(input_file.read())
                        # Add a newline separator between files
                        output.write('\n')


# Concatenate Python files in the specified project directory.
concatenate_python_files(project_directory, output_file)

print(f'Concatenated code saved to {output_file}')
