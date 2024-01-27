import numpy as np
from qiskit import *

#create a quantum circuit having a register of three qubits
circ = QuantumCircuit(3)

# Add a H gate on quibit 0
circ.h(0)

#Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circ.cx(0, 1)

#Add a CX (CNOT) gate on control qubit 0 and target qubit 2
circ.cx(0, 2)

#Plot the circut and save it to a file for viewing
circ.draw(filename="mycircuit.txt")