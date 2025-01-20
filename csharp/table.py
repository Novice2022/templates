from typing import Iterable, Any

class Table:
    @staticmethod
    def display(
        headers: tuple[str],
        values: tuple[Iterable[Any]]
    ) -> None:
        assert len(headers) == len(values),\
            "Amount of columns must be equal to "
        
        cross = '╬'
        vertical = {
            "top": '╦',
            "middle": '║',
            "bottom": '╩'
        }
        horrisontal = {
            "left": '╠',
            "middle": '═',
            "right": '╣'
        }
        corners = {
            "top-left": '╔',
            "top-right": '╗',
            "bottom-left": '╚',
            "bottom-right": '╝'
        }

        widths = [len(header) for header in headers]
        longest_column_length = max([len(column) for column in values])

        for i, column in enumerate(values):
            for value in column:
                widths[i] = max(widths[i], len(str(value)))

        print(
            corners["top-left"] +\
            vertical["top"].join(
                [horrisontal["middle"] * (width + 2) for width in widths]
            ) +\
            corners["top-right"]
        )

        print(vertical["middle"], end='')

        headers_row = ""
        for i, header in enumerate(headers):
            print(f" {header}{' ' * (widths[i] - len(header) + 1)}", end=vertical["middle"])
        print()
        
        print(
            horrisontal["left"] +\
            cross.join(
                [horrisontal["middle"] * (width + 2) for width in widths]
            ) +\
            horrisontal["right"]
        )

        for row in range(longest_column_length):
            print(vertical["middle"], end='')

            for i, column in enumerate(values):
                try:
                    value = column[row]
                except IndexError:
                    value = ''

                print(
                    f" {value}{' ' * (widths[i] - len(str(value)))}",
                    end=f" {vertical['middle']}"
                )

            print()

        print(
            corners["bottom-left"] +\
            vertical["bottom"].join(
                [horrisontal["middle"] * (width + 2) for width in widths]
            ) +\
            corners["bottom-right"]
        )


def main() -> None:
    x_vlaues = (0.1, 0.3, 0.4, 0.7, 1)

    s_values = []

    for x in x_vlaues:
        s = 0
        
        for k in range(1, 11):
            s += ((-1) ** k) * (x ** (2 * k - 1)) / (2 * k - 1) 
        
        s_values.append(round(s, 4))

    Table.display(("X", "S"), (x_vlaues, s_values))


if __name__ == "__main__":
    main()
