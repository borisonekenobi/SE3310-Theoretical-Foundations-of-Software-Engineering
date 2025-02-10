import os
import graphviz

output_format = 'png'


def main():
    for file_path in os.listdir('./'):
        if file_path.endswith('.dot'):
            file_name = os.path.basename(file_path)
            name = os.path.splitext(file_name)[0]

            with open(file_name, 'r') as file:
                dot_data = file.read()

            graph = graphviz.Source(dot_data)
            graph.render(filename=name, format=output_format, cleanup=True)

            print('Graph has been saved to {}.{}'.format(file_name, output_format))


if __name__ == '__main__':
    main()
