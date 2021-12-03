with open("input", "r") as f:
    read_input_values = [ int(x) for x in f.read().split(",") ]

class Amplifier(object):
    def __init__(self, phase, input_values):
        self.input_and_phase = [phase, 0]
        self.input_and_phase_index = 0
        self.input_values = input_values.copy()
        self.outputStream = [0]
        self.amplifier_halted_by_opcode = False

    def solveOpcode(self, input):
        self.input_and_phase[1] = input
        self.index = 0
        elements = len(self.input_values)

        while self.index < elements and not self.amplifier_halted_by_opcode:
            self.operatorInterpreter()

    def operatorInterpreter(self):
        A, B, C, operator = self.getParameterModes()

        if C == 0:
            parameter1 = self.input_values[self.input_values[self.index + 1]]
        else:
            parameter1 = self.input_values[self.index + 1]

        # Operators 3 and 4 only support one parameter.
        if operator < 3 or operator > 4:
            if B == 0:
                parameter2 = self.input_values[self.input_values[self.index + 2]]
            else:
                parameter2 = self.input_values[self.index + 2]

            if operator < 3 or operator > 6:
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
            self.input_values[self.input_values[self.index + 1]] = self.input_and_phase[self.input_and_phase_index]
            self.input_and_phase_index += 1
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
        if operator == 99:
            self.amplifier_halted_by_opcode = True

    def getParameterModes(self):
        ABC, DE = divmod(self.input_values[self.index], 100)
        AB, C = divmod(ABC, 10)
        A, B = divmod(AB, 10)
        return A, B, C, DE

class Phase_Generator(object):
    def __init__(self, lowest_phase_int):
        self.current_phase_sequence_int = lowest_phase_int
        self.upper_list = False
        if lowest_phase_int > 50000:
            self.upper_list = True

    def get_next_phase_sequence(self):
        phase_sequence_list = self.get_phase_sequence_of()
        while not self.validPhaseSetting(phase_sequence_list):
            self.current_phase_sequence_int += 1
            phase_sequence_list = self.get_phase_sequence_of()
        return phase_sequence_list

    def validPhaseSetting(self, list):
        if self.upper_list == True:
            if 5 in list and 6 in list and 7 in list and 8 in list and 9 in list:
                return True
        else:
            if 0 in list and 1 in list and 2 in list and 3 in list and 4 in list:
                return True
        return False

    def get_phase_sequence_of(self):
        current_phase_sequence_str =  str(self.current_phase_sequence_int)
        phase_list = [int(i) for i in str(self.current_phase_sequence_int)]
        while len(phase_list) < 5:
            phase_list.insert(0, 0)
        return phase_list

def thrusters_output():
    outputs = []
    phase_generator = Phase_Generator(1234)
    global read_input_values
    while phase_generator.current_phase_sequence_int <= 43210:
        phase_list = phase_generator.get_next_phase_sequence()

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
        phase_generator.current_phase_sequence_int += 1

    print("Maximum output for thrusters: " + str(max(outputs)))

thrusters_output()

def thrusters_output_looped():
    outputs = []
    phase_generator = Phase_Generator(56789)
    global read_input_values
    while phase_generator.current_phase_sequence_int <= 98765:
        phase_list = phase_generator.get_next_phase_sequence()

        amp_a = Amplifier(phase_list[0], read_input_values)
        amp_b = Amplifier(phase_list[1], read_input_values)
        amp_c = Amplifier(phase_list[2], read_input_values)
        amp_d = Amplifier(phase_list[3], read_input_values)
        amp_e = Amplifier(phase_list[4], read_input_values)       
        
        while not amp_e.amplifier_halted_by_opcode:
            amp_a.solveOpcode(0 + amp_e.outputStream[-1])
            amp_c.solveOpcode(amp_b.outputStream[-1])
            amp_d.solveOpcode(amp_c.outputStream[-1])
            amp_b.solveOpcode(amp_a.outputStream[-1])
            amp_e.solveOpcode(amp_d.outputStream[-1])
            
        outputs.append(amp_e.outputStream[-1])
        phase_generator.current_phase_sequence_int += 1

    print("Maximum output for thrusters with loop: " + str(max(outputs)))

thrusters_output_looped()

