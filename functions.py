FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of  #this is a docstring
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

# print(help(get_todos()))


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


print(__name__)
if __name__ == '__main__':        #ce se afla in if se executa doar local / nu va fi executat cand este importat
    print('Hello from functions')
    print(get_todos())

# print(_name) afiseaza __main__ in fisierul.py unde
# exista secventa if name == main, iar in alt fisier.py unde a
# fost importat functions va afisa numele fisierului.py (functions)

# ce se afla in secventa if _name_ == "_main_" va fi rulat doar
# atunci cand functions.py este executat direct, nu si atunci cand
# este importat in alt fisier.py