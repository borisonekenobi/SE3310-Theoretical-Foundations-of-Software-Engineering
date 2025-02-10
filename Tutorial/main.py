import graphviz

file_name = 'a0_q1'
dot_file_path = 'a0_q1.dot'
output_format = 'png'


def main():
    with open(dot_file_path, 'r') as file:
        dot_data = file.read()

    graph = graphviz.Source(dot_data)
    graph.render(filename=file_name, format=output_format, cleanup=True)

    print('Graph has been saved to {}.{}'.format(file_name, output_format))


if __name__ == '__main__':
    main()
