import os

project_directory = '/home/harry/Documents/ai2cyber/'

output_file = 'concatenated_code.py'


def concatenate_python_files(directory, output_file):
    with open(output_file, 'w') as output:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as input_file:
                        output.write(input_file.read())
                        output.write('\n')


concatenate_python_files(project_directory, output_file)

print(f'Concatenated code saved to {output_file}')
