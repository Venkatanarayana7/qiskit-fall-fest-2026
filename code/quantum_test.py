# Modern Qiskit 1.x Code
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Step 1: Create a circuit with 1 quantum bit (qubit) and 1 normal classical bit
qc = QuantumCircuit(1, 1)

# Step 2: Apply a Hadamard gate to put the qubit into superposition
qc.h(0)

# Step 3: Measure the qubit and store the result in the classical bit
qc.measure(0, 0)

# Step 4: Set up the modern simulator backend
simulator = AerSimulator()

# Step 5: Run the circuit 1,024 times and get the results
job = simulator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts(qc)

# Step 6: Print out the text-based circuit diagram and the data
print("Circuit Visual Representation:")
print(qc.draw())

print("\nResults (How many times we got 0 vs 1):")
print(counts)

print(f"\nProbability of getting 0: {counts.get('0', 0) / 1024:.3f}")
print(f"Probability of getting 1: {counts.get('1', 0) / 1024:.3f}")
