
# UNIQUE INPUTS
# THREE INPUTS
inputs  = [1.2, 5.1, 2.1]

# WEIGHTSS
# THREE INPUTS
weights = [3.1, 2.1, 8.7]

# BIAS 
# EVERY UNIQUE NEURON HAS A UNIQUE BIAS
bias = 3

# OUTPUTS
# OUTPUT = SUM-OF(INPUTS * WEIGHTS) + BIAS
outputs =  inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias

# PRINTING OUTPUTS
print(f"outputs: {outputs}" )



