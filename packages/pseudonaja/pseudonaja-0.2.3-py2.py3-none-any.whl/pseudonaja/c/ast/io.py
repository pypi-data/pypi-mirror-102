from . import node
from . import misc
from pseudonaja.c.PSymbolTable import Array
import pseudonaja.c.PInterpreter as pcint

class Input(node.Node):

    def __init__(self, variable, lineno):

        super().__init__(lineno)
        self.__identifier = variable

    def interpret(self):

        name = self.__identifier.name

        # Check to see if the variable has been declared
        if name in pcint.PInterpreter.symbols:

            val = input()
            while val == "":
                val = input()

            # Get the variable from the symbol table
            var = pcint.PInterpreter.symbols[name]

            val = misc.type_cast(var.type, val)

            if isinstance(var, Array):
                var[self.__identifier.idx] = val
            else:
                var.value = val
        else:
            raise SyntaxError(f"Error: symbol '{name}' undefined on line {self.lineno}")

class Output(node.Node):

    def __init__(self, args, lineno):

        super().__init__(lineno)

        self.__args = args

    def interpret(self):

        for arg in self.__args:
            print(arg.interpret(), end=" ")

        print()
