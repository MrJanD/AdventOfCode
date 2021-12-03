with open("input", "r") as f:
    read_input_values = [ int(x) for x in f.read().split(",") ]

class Amplifier(object):
    def __init__(self, phase, input_values):
        self.phase = phase
        self.input = 0
        self.input_values = input_values.copy()
        self.outputStream = [0]
        self.index = 0
        self.operator_returned = 0
        self.input_next = False

    def get_next_input(self):
        if self.input_next:
            #self.input_next = not self.input_next
            return self.input
        else:
            self.input_next = not self.input_next
            return self.phase

    def solveOpcode(self, input):
        self.input = input
        elements = len(self.input_values)
        self.operator_returned = 0

        while self.index < elements and self.operator_returned != 4 and self.operator_returned != 99:
            self.operator_returned = self.operatorInterpreter()

    def operatorInterpreter(self):
        A, B, C, operator = self.getParameterModes()
        if operator == 99:
            return operator

        if C == 0:
            parameter1 = self.input_values[self.input_values[self.index + 1]]
        else:
            parameter1 = self.input_values[self.index + 1]

        # Operators 3 and 4 only support one parameter.
        if self.input_values[self.index + 2] < len(self.input_values):
            if B == 0:
                parameter2 = self.input_values[self.input_values[self.index + 2]]
            elif (self.index + 2) < len(self.input_values):
                parameter2 = self.input_values[self.index + 2]

        if (self.index + 3) < len(self.input_values):
            if A == 0:
                parameter3 = self.input_values[self.index + 3]
            else:
                parameter3 = self.input_values[self.index + 3]

        # 1: Addition
        if operator == 1:
            self.input_values[parameter3] = parameter1 + parameter2
            self.index += 4

        # 2: Multiplication
        if operator == 2:
            self.input_values[parameter3] = parameter1 * parameter2
            self.index += 4

        # 3: Write
        if operator == 3:
            self.input_values[self.input_values[self.index + 1]] = self.get_next_input()
            self.index += 2

        # 4: Print
        if operator == 4:
            self.outputStream.append(parameter1)
            self.index += 2

        # 5: Jump-If-True
        if operator == 5:
            if parameter1 != 0:
               self.index = parameter2
            else:
                self.index += 3

        # 6: Jump-If-False
        if operator == 6:
            if parameter1 == 0:
               self.index = parameter2
            else:
                self.index += 3

        # 7: Less Than
        if operator == 7:
            if parameter1 < parameter2:
                self.input_values[parameter3] = 1
            else:
                self.input_values[parameter3] = 0
            self.index += 4

        # 8: Equals
        if operator == 8:
            if parameter1 == parameter2:
                self.input_values[parameter3] = 1
            else:
                self.input_values[parameter3] = 0
            self.index += 4

        # 99: End of operation
        return operator

    def getParameterModes(self):
        ABC, DE = divmod(self.input_values[self.index], 100)
        AB, C = divmod(ABC, 10)
        A, B = divmod(AB, 10)
        return A, B, C, DE

def get_next_phase_sequence(current_phase_sequence_int):
    phase_sequence_list = get_phase_sequence_of(current_phase_sequence_int)
    part1 = True
    if current_phase_sequence_int > 50000:
        part1 = False
    while not validPhaseSetting(phase_sequence_list, part1):
        current_phase_sequence_int += 1
        phase_sequence_list = get_phase_sequence_of(current_phase_sequence_int)
    return current_phase_sequence_int, get_phase_sequence_of(current_phase_sequence_int)

def validPhaseSetting(list, part1):
    if part1:
        if 0 in list and 1 in list and 2 in list and 3 in list and 4 in list:
            return True
    else:
        if 5 in list and 6 in list and 7 in list and 8 in list and 9 in list:
            return True
    return False

def get_phase_sequence_of(current_phase_sequence_int):
    current_phase_sequence_str =  str(current_phase_sequence_int)
    phase_list = [int(i) for i in str(current_phase_sequence_int)]
    while len(phase_list) < 5:
        phase_list.insert(0, 0)
    return phase_list

def thrusters_output():
    outputs = []
    phase_sequence = 1234
    global read_input_values
    while phase_sequence <= 43210:
        phase_sequence, phase_list = get_next_phase_sequence(phase_sequence)

        amp_a = Amplifier(phase_list[0], read_input_values)
        amp_b = Amplifier(phase_list[1], read_input_values)
        amp_c = Amplifier(phase_list[2], read_input_values)
        amp_d = Amplifier(phase_list[3], read_input_values)
        amp_e = Amplifier(phase_list[4], read_input_values)

        amp_a.solveOpcode(0)
        amp_b.solveOpcode(amp_a.outputStream[-1])
        amp_c.solveOpcode(amp_b.outputStream[-1])
        amp_d.solveOpcode(amp_c.outputStream[-1])
        amp_e.solveOpcode(amp_d.outputStream[-1])

        outputs.append(amp_e.outputStream[-1])
        phase_sequence += 1

    print("Maximum output for thrusters: " + str(max(outputs)))

thrusters_output()

def thrusters_output_looped():
    outputs = []
    phase_sequence = 56789
    global read_input_values
    while phase_sequence <= 98765:
        phase_sequence, phase_list = get_next_phase_sequence(phase_sequence)

        amp_a = Amplifier(phase_list[0], read_input_values)
        amp_b = Amplifier(phase_list[1], read_input_values)
        amp_c = Amplifier(phase_list[2], read_input_values)
        amp_d = Amplifier(phase_list[3], read_input_values)
        amp_e = Amplifier(phase_list[4], read_input_values)

        while not amp_e.operator_returned == 99:
            amp_a.solveOpcode(0 + amp_e.outputStream[-1])
            amp_b.solveOpcode(amp_a.outputStream[-1])
            amp_c.solveOpcode(amp_b.outputStream[-1])
            amp_d.solveOpcode(amp_c.outputStream[-1])
            amp_e.solveOpcode(amp_d.outputStream[-1])

        outputs.append(amp_e.outputStream[-1])
        phase_sequence += 1

    print("Maximum output for thrusters with loop: " + str(max(outputs)))

thrusters_output_looped()
