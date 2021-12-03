class Intcode(object):
    def __init__(self, input_values):
        self.input = 0
        self.original_input_values = input_values
        self.input_values = self.to_dictionary(self.original_input_values)
        self.input_range = len(input_values)
        self.outputStream = []
        self.index = 0
        self.operator_returned = 0
        self.input_next = False
        self.relative_base = 0

    def reset(self):
        self.input = 0
        self.input_values = self.to_dictionary(self.original_input_values)
        self.input_range = len(self.input_values)
        self.outputStream = []
        self.index = 0
        self.operator_returned = 0
        self.input_next = False
        self.relative_base = 0

    def to_dictionary(self, input_values):
        res_dct = {i: input_values[i] for i in range(len(input_values))}
        return res_dct

    def get_value(self, value_index):
        if value_index in self.input_values:
            return self.input_values[value_index]
        else:
            return 0

    def set_value(self, value_index, value):
        self.input_values[value_index] = value

    def solveOpcode(self, input):
        self.input = input
        elements = len(self.input_values)
        self.operator_returned = 0

        while self.index < elements and self.operator_returned != 99:
            self.operator_returned = self.operatorInterpreter()

    def operatorInterpreter(self):
        A, B, C, operator = self.getParameterModes()
        if operator == 99:
            return operator

        # Parameter1 should always be readable.
        if C == 0:
            parameter1 = self.get_value(self.get_value(self.index + 1))
        elif C == 1:
            parameter1 = self.get_value(self.index + 1)
        elif C == 2:
            parameter1 = self.get_value(self.relative_base + self.get_value(self.index + 1))

        # Operators 3 and 4 only support one parameter. Therefore, it is not sure, wether the input is long enough.
        if self.parameters_required(operator) >= 2:
            if B == 0:
                parameter2 = self.get_value(self.get_value(self.index + 2))
            elif B == 1:
                parameter2 = self.get_value(self.index + 2)
            elif B == 2:
                parameter2 = self.get_value(self.relative_base + self.get_value(self.index + 2))

        if self.parameters_required(operator) >= 3:
            if A == 0:
                #parameter3 = self.get_value(self.get_value(self.index + 3))
                parameter3 = self.get_value(self.index + 3)
            elif A == 1:
                raise Exception("Parameter 3 shall never be in immediate mode!")
            elif A == 2:
                #parameter3 = self.get_value(self.relative_base + self.get_value(self.index + 3))
                parameter3 = self.relative_base + self.get_value(self.index + 3)

        # 1: Addition
        if operator == 1:
            self.set_value(parameter3, parameter1 + parameter2)
            self.index += 4

        # 2: Multiplication
        elif operator == 2:
            self.set_value(parameter3, parameter1 * parameter2)
            self.index += 4

        # 3: Write
        elif operator == 3:
            to_write = self.input
            position = self.get_value(self.index + 1)
            if C == 0:
                self.set_value(position, to_write)
            elif C == 2:
                self.set_value(self.relative_base + position, to_write)
            self.index += 2

        # 4: Print
        elif operator == 4:
            self.outputStream.append(parameter1)
            self.index += 2

        # 5: Jump-If-True
        elif operator == 5:
            if parameter1 != 0:
                self.index = parameter2
            else:
                self.index += 3

        # 6: Jump-If-False
        elif operator == 6:
            if parameter1 == 0:
                self.index = parameter2
            else:
                self.index += 3

        # 7: Less Than
        elif operator == 7:
            if parameter1 < parameter2:
                self.set_value(parameter3, 1)
            else:
                self.set_value(parameter3, 0)
            self.index += 4

        # 8: Equals
        elif operator == 8:
            if parameter1 == parameter2:
                self.set_value(parameter3, 1)
            else:
                self.set_value(parameter3, 0)
            self.index += 4

        # 9: Opcode 9 adjusts the relative base by the value of its only parameter. The relative base increases (or decreases, if the value is negative) by the value of the parameter.
        elif operator == 9:
            self.relative_base += parameter1
            self.index += 2

        # 99: End of operation
        else:
            self.index += 1

        return operator

    def getParameterModes(self):
        ABC, DE = divmod(self.get_value(self.index), 100)
        AB, C = divmod(ABC, 10)
        A, B = divmod(AB, 10)
        return A, B, C, DE

    def parameters_required(self, operator):
        par_req = 3
        if operator == 3 or operator == 4:
            par_req = 1
        if operator == 5 or operator == 6:
            par_req = 2
        return par_req