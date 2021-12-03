import intcode

with open("input", "r") as f:
    read_input_values = [ int(x) for x in f.read().split(",") ]

amp = intcode.Intcode(read_input_values)
amp.solveOpcode(1)
print("BOOST keycode (Input: 1): " + str(amp.output_stream))
amp.reset()
amp.solveOpcode(2)
print("BOOST keycode (Input: 2): " + str(amp.output_stream))
