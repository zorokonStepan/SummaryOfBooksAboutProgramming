import math
from io import StringIO


def show_tree(tree, total_width=36, fill=' '):
    """Красивый вывод дерева."""
    output = StringIO()
    last_row = -1

    for i, n in enumerate(tree):
        row = int(math.floor(math.log(i + 1, 2))) if i else 0

        if row != last_row:
            output.write('\n')

        columns = 2 ** row
        col_width = int(math.floor(total_width / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row

    print(output.getvalue())
    print('-' * total_width)
    print()


if __name__ == "__main__":
    show_tree([19, 9, 4, 10, 11])
