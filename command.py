from typing import List

class Command:
    name: str
    description: str
    capitalName: str
    version: float
    secret: bool
    def __init__(self, name: str, description: str, capitalName: str, version: float, secret: bool = False) -> None:
        self.name = name
        self.description = description
        self.capitalName = capitalName
        self.version = version
        self.secret = secret


    def run(self, argv: list[str]):
        underline = "=" * len(self.capitalName)
        print(self.capitalName)
        print(underline)

    
    def refresh(self):
        self.__init__()

    
    def parse_argv(self, argv):
    
        """
        Parses a list of arguments, grouping them based on quotation marks.

        Args:
        - argv (list of str): The arguments to parse.

        Returns:
        - list of str: The parsed arguments.
        """
        parsed_args = []
        current_arg = ""
        in_quotes = False

        for arg in argv:
            for char in arg:
                if char == '"' and not in_quotes:
                    # Start of a quoted argument
                    in_quotes = True
                    if current_arg:  # Add the current_arg if it's not empty
                        parsed_args.append(current_arg)
                        current_arg = ""
                elif char == '"' and in_quotes:
                    # End of a quoted argument
                    in_quotes = False
                    parsed_args.append(current_arg)
                    current_arg = ""
                else:
                    # Part of an argument
                    current_arg += char
            if not in_quotes and current_arg:
                # If we're not in quotes and there's a current_arg, it's a complete argument
                parsed_args.append(current_arg)
                current_arg = ""
            elif in_quotes:
                # If we're in quotes, add a space before the next part
                current_arg += " "

        # Add the last argument if there's any
        if current_arg:
            parsed_args.append(current_arg)

        return parsed_args


if __name__ == "__main__":
    cmd = Command(name="test", description="test", capitalName="test")
    argv = ['"geeks', 'for', 'geeks"', 'gek', 'gek', 'i']
    newArgv = cmd.parse_argv(argv=argv)
    print(newArgv)


