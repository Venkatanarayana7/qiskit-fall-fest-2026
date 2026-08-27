
# LECTURE 3: QUANTUM GATES & CIRCUITS : BUILDING YOUR FIRST QUANTUM COMPUTATION

---

## PART A: WHAT ARE QUANTUM GATES?

### Section 1: From Classical Gates to Quantum Gates

*"Team, in classical computing, we use logic gates to manipulate bits. You've probably learned about AND, OR, NOT, XOR gates in your CSE courses."*

**Classical Gates:**

| Gate | Input | Output | Description |
|------|-------|--------|-------------|
| NOT | 0 | 1 | Flips the bit |
| NOT | 1 | 0 | Flips the bit |
| AND | 0,0 | 0 | 1 only if both inputs are 1 |
| AND | 1,1 | 1 | 1 only if both inputs are 1 |
| OR | 0,0 | 0 | 1 if either input is 1 |
| OR | 1,0 | 1 | 1 if either input is 1 |

**Quantum Gates:**

Quantum gates are the quantum equivalent of classical gates. They operate on qubits, transforming their quantum states.

But there's a key difference: **quantum gates must be reversible**.

**Why Reversible?**

In classical computing, some gates are irreversible. The AND gate, for example, takes two inputs and produces one output. If I tell you the output is 0, can you tell me what the inputs were? No, it could be (0,0), (0,1), or (1,0). Information is lost.

In quantum mechanics, information cannot be lost (according to the laws of physics). Every quantum gate must be **reversible**, meaning you can reconstruct the input from the output.

**The Mathematical Representation:**

Quantum gates are represented by **unitary matrices**. A unitary matrix U has the property:

U†U = I (where U† is the conjugate transpose of U, and I is the identity matrix)

Don't panic if you don't fully understand this. The key point is: quantum gates are **reversible transformations** that can be represented as matrices.

**Applying a Gate:**

When you apply a gate to a qubit, you're essentially **multiplying the qubit's state vector by the gate's matrix**:

|ψ'⟩ = U|ψ⟩

Where:
- |ψ⟩ is the initial state
- U is the gate's matrix
- |ψ'⟩ is the final state

**On the Bloch Sphere:**

Applying a quantum gate is like **rotating the state vector on the Bloch sphere**. Different gates rotate the vector in different directions and by different amounts.

This is the beautiful intuition: quantum computation is just **a series of rotations on the Bloch sphere** (for a single qubit) or in higher-dimensional spaces (for multiple qubits).

---

### Section 2: The Key Properties of Quantum Gates

*"Let me explain the three properties that all quantum gates must satisfy."*

**Property 1: Reversibility**

Every quantum gate is reversible. If you apply a gate U to a state |ψ⟩ to get |ψ'⟩, you can apply the inverse gate U† to get back |ψ⟩:

|ψ'⟩ = U|ψ⟩
U†|ψ'⟩ = U†U|ψ⟩ = I|ψ⟩ = |ψ⟩

**Property 2: Linearity**

Quantum gates are linear transformations. This means:

U(α|0⟩ + β|1⟩) = αU|0⟩ + βU|1⟩

This is crucial: the gate acts on each part of the superposition independently. This is what allows quantum parallelism.

**Property 3: Unitarity**

Quantum gates preserve the total probability. If |ψ⟩ is a valid quantum state (probabilities sum to 1), then U|ψ⟩ is also a valid quantum state.

This means: |α|² + |β|² = 1 → |α'|² + |β'|² = 1 (after applying U)

**Why These Properties Matter:**

These properties ensure that quantum gates are:
1. **Physically realizable**: They correspond to actual operations that can be performed on quantum systems
2. **Information-preserving**: No quantum information is lost
3. **Predictable**: The output is a valid quantum state

---

## PART B: SINGLE-QUBIT GATES

### Section 1: The Pauli Gates (X, Y, Z)

*"Let's start with the three most fundamental quantum gates, the Pauli gates, named after physicist Wolfgang Pauli."*

**The Pauli-X Gate (Quantum NOT):**

The X gate is the quantum equivalent of the classical NOT gate. It flips |0⟩ to |1⟩ and |1⟩ to |0⟩.

| Input | Output |
|-------|--------|
| |0⟩ | |1⟩ |
| |1⟩ | |0⟩ |

**Matrix Representation:**

X = [0  1]
    [1  0]

**On the Bloch Sphere:**

The X gate rotates the state vector by 180° around the X-axis. It flips the north pole to the south pole and vice versa.

**In Qiskit:**

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.x(0)  # Apply X gate to qubit 0
```

**The Pauli-Y Gate:**

The Y gate rotates the state vector by 180° around the Y-axis. It's similar to X but also adds a phase.

| Input | Output |
|-------|--------|
| |0⟩ | i|1⟩ |
| |1⟩ | −i|0⟩ |

**Matrix Representation:**

Y = [0  −i]
    [i   0]

**In Qiskit:**

```python
qc.y(0)  # Apply Y gate to qubit 0
```

**The Pauli-Z Gate (Phase Flip):**

The Z gate rotates the state vector by 180° around the Z-axis. It doesn't change the measurement probabilities of |0⟩ and |1⟩, but it flips the phase.

| Input | Output |
|-------|--------|
| |0⟩ | |0⟩ |
| |1⟩ | −|1⟩ |

**Matrix Representation:**

Z = [1   0]
    [0  −1]

**In Qiskit:**

```python
qc.z(0)  # Apply Z gate to qubit 0
```

**Why Z Matters:**

The Z gate is subtle. If you apply Z to |1⟩, you get −|1⟩. The measurement probability is still 100% |1⟩, but the phase is flipped. This phase difference matters when qubits interfere.

**Summary Table:**

| Gate | Matrix | Effect on |0⟩ | Effect on |1⟩ | Bloch Rotation |
|------|--------|---------------|---------------|----------------|
| X | [0 1; 1 0] | |1⟩ | |0⟩ | 180° around X-axis |
| Y | [0 −i; i 0] | i|1⟩ | −i|0⟩ | 180° around Y-axis |
| Z | [1 0; 0 −1] | |0⟩ | −|1⟩ | 180° around Z-axis |

---

### Section 2: The Hadamard Gate (H) : Creating Superposition

*"The Hadamard gate is the most important single-qubit gate for quantum computing. It creates superposition."*

**What It Does:**

The Hadamard gate transforms the computational basis states into equal superpositions:

H|0⟩ = (|0⟩ + |1⟩)/√2 = |+⟩
H|1⟩ = (|0⟩ − |1⟩)/√2 = |−⟩

**Matrix Representation:**

H = (1/√2) [1   1]
           [1  −1]

**On the Bloch Sphere:**

The Hadamard gate rotates the state vector:
- From the North Pole (|0⟩) to the +X point on the equator (|+⟩)
- From the South Pole (|1⟩) to the −X point on the equator (|−⟩)

**Why Hadamard Is Special:**

The Hadamard gate is its own inverse: H·H = I (identity matrix). This means:

H|+⟩ = H((|0⟩ + |1⟩)/√2) = |0⟩
H|−⟩ = H((|0⟩ − |1⟩)/√2) = |1⟩

This property is extremely useful for quantum algorithms. Applying H twice brings you back to where you started.

**In Qiskit:**

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.h(0)  # Apply Hadamard to qubit 0
```

**The Magic of Hadamard:**

When you apply H to n qubits (each initially in |0⟩), you create a superposition of all 2ⁿ possible states:

H|0⟩ ⊗ H|0⟩ ⊗ ... ⊗ H|0⟩ = (1/√(2ⁿ)) Σ |i⟩

For n=3:
H|000⟩ = (|000⟩ + |001⟩ + |010⟩ + |011⟩ + |100⟩ + |101⟩ + |110⟩ + |111⟩) / √8

All 8 states have equal probability (1/8). This is how quantum computers achieve exponential parallelism.

---

### Section 3: The Phase Gates (S and T)

*"The S and T gates add phase to qubits without changing the measurement probabilities."*

**The S Gate (Phase Gate):**

The S gate adds a 90° phase:

| Input | Output |
|-------|--------|
| |0⟩ | |0⟩ |
| |1⟩ | i|1⟩ |

**Matrix Representation:**

S = [1  0]
    [0  i]

**The T Gate (π/8 Gate):**

The T gate adds a 45° phase:

| Input | Output |
|-------|--------|
| |0⟩ | |0⟩ |
| |1⟩ | e^(iπ/4)|1⟩ |

**Matrix Representation:**

T = [1       0]
    [0  e^(iπ/4)]

**Why Phase Gates Matter:**

Phase gates are essential for:
1. Creating arbitrary quantum states
2. Implementing quantum algorithms like Quantum Fourier Transform
3. Building feature maps for quantum machine learning

**In Qiskit:**

```python
qc.s(0)  # Apply S gate to qubit 0
qc.t(0)  # Apply T gate to qubit 0
```

---

### Section 4: Rotation Gates (Rx, Ry, Rz)

*"The rotation gates allow you to rotate the state vector by any angle, not just 90° or 180°."*

**The Rx Gate (Rotation around X-axis):**

Rx(θ) rotates the state vector by angle θ around the X-axis:

Rx(θ) = cos(θ/2)I − i·sin(θ/2)X

**The Ry Gate (Rotation around Y-axis):**

Ry(θ) rotates the state vector by angle θ around the Y-axis:

Ry(θ) = cos(θ/2)I − i·sin(θ/2)Y

**The Rz Gate (Rotation around Z-axis):**

Rz(φ) rotates the state vector by angle φ around the Z-axis:

Rz(φ) = e^(−iφ/2) [1       0]
                  [0  e^(iφ)]

**Why Rotation Gates Matter:**

These are the most flexible single-qubit gates. With Rx, Ry, and Rz, you can create any arbitrary single-qubit state. They're essential for:
- Building variational quantum circuits (ansatz)
- Creating feature maps that encode data
- Implementing arbitrary unitary operations

**In Qiskit:**

```python
import numpy as np
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.rx(np.pi/2, 0)  # Rotate by π/2 around X-axis
qc.ry(np.pi/3, 0)  # Rotate by π/3 around Y-axis
qc.rz(np.pi/4, 0)  # Rotate by π/4 around Z-axis
```

**Special Cases:**

Note that the Pauli gates are special cases of rotation gates:
- X = Rx(π)
- Y = Ry(π)
- Z = Rz(π)
- H = Ry(π/2) followed by Rz(π) (approximately)
- S = Rz(π/2)
- T = Rz(π/4)

---

### Check Your Understanding : Single-Qubit Gates

Answer these questions:

1. **What does the X gate do?**
   *Hint: It's the quantum NOT.*

2. **What does the H gate do to |0⟩?**
   *Hint: It creates equal superposition.*

3. **What does the Z gate do to |1⟩?**
   *Hint: It flips the phase.*

4. **What is the matrix for the X gate?**
   *Hint: It's a 2×2 matrix with 0s on the diagonal and 1s off-diagonal.*

5. **What is the difference between X and Rx(θ)?**
   *Hint: X rotates by exactly 180°, Rx rotates by any angle.*

6. **What does the S gate do?**
   *Hint: It adds a 90° phase.*

7. **How many single-qubit gates do you need to create any arbitrary single-qubit state?**
   *Hint: Three rotation gates (Rx, Ry, Rz) are sufficient.*

---

## PART C: MULTI-QUBIT GATES

### Section 1: The CNOT Gate (Controlled-NOT)

*"The CNOT gate is the most important multi-qubit gate. It creates entanglement between qubits."*

**What It Does:**

The CNOT gate operates on two qubits: a **control qubit** and a **target qubit**.

- If the control qubit is |0⟩, nothing happens to the target
- If the control qubit is |1⟩, the X gate is applied to the target (flipping it)

**Truth Table:**

| Control | Target (input) | Target (output) |
|---------|----------------|-----------------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Matrix Representation:**

CNOT = [1  0  0  0]
       [0  1  0  0]
       [0  0  0  1]
       [0  0  1  0]

**In Qiskit:**

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.cx(0, 1)  # CNOT with control=0, target=1
# Or equivalently:
qc.cnot(0, 1)
```

**Why CNOT Matters:**

CNOT is the gate that creates **entanglement**. When you apply H to the control qubit and then CNOT, you create the Bell state:

1. Start with |00⟩
2. Apply H to qubit 0: → (|00⟩ + |10⟩)/√2
3. Apply CNOT (control=0, target=1): → (|00⟩ + |11⟩)/√2

This is the Bell state, the simplest entangled state. The two qubits are now correlated: if you measure the first qubit as 0, the second is definitely 0; if the first is 1, the second is definitely 1.

**Visualizing CNOT:**

Think of CNOT as a "controlled X". It's like an if-else statement in Python:

```python
if control == 1:
    target = NOT(target)  # Flip the target
else:
    target = target  # Do nothing
```

But remember: in quantum computing, the control qubit can be in **superposition**. So the CNOT acts on all components of the superposition simultaneously.

---

### Section 2: Other Multi-Qubit Gates

**The SWAP Gate:**

The SWAP gate exchanges the states of two qubits:

| Input | Output |
|-------|--------|
| |00⟩ | |00⟩ |
| |01⟩ | |10⟩ |
| |10⟩ | |01⟩ |
| |11⟩ | |11⟩ |

**In Qiskit:**

```python
qc.swap(0, 1)  # Swap qubits 0 and 1
```

**The Toffoli Gate (CCNOT):**

The Toffoli gate is a controlled-controlled-NOT. It has two control qubits and one target:

- If both controls are |1⟩, flip the target
- Otherwise, do nothing

**Truth Table (partial):**

| Control 1 | Control 2 | Target (input) | Target (output) |
|-----------|-----------|----------------|-----------------|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

**In Qiskit:**

```python
qc.ccx(0, 1, 2)  # Toffoli with controls=0,1 and target=2
```

**The Controlled-Z Gate (CZ):**

The CZ gate applies the Z gate to the target if the control is |1⟩:

**In Qiskit:**

```python
qc.cz(0, 1)  # CZ with control=0, target=1
```

**The Controlled-H Gate (CH):**

The CH gate applies the H gate to the target if the control is |1⟩:

**In Qiskit:**

```python
qc.ch(0, 1)  # CH with control=0, target=1
```

---

### Section 3: Creating Entanglement : The Bell State

*"Now let me show you how to create entanglement, the 'spooky action at a distance' that Einstein talked about."*

**The Recipe:**

To create the Bell state (|00⟩ + |11⟩)/√2:

1. Start with two qubits in |00⟩
2. Apply H to the first qubit (creates superposition)
3. Apply CNOT with first qubit as control and second as target (creates entanglement)

**Step by Step:**

**Step 1:** |ψ⟩ = |00⟩

**Step 2:** Apply H to qubit 0:
|ψ⟩ = (|0⟩ + |1⟩)/√2 ⊗ |0⟩
    = (|00⟩ + |10⟩)/√2

**Step 3:** Apply CNOT (control=0, target=1):
If qubit 0 is |0⟩: qubit 1 stays |0⟩ → |00⟩
If qubit 0 is |1⟩: qubit 1 flips to |1⟩ → |11⟩

Final state: |ψ⟩ = (|00⟩ + |11⟩)/√2

**The Result:**

This is an entangled state. If you measure qubit 0 and get 0, qubit 1 is definitely 0. If you measure qubit 0 and get 1, qubit 1 is definitely 1. The qubits are correlated.

**In Qiskit:**

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2, 2)
qc.h(0)      # Hadamard on qubit 0
qc.cx(0, 1)  # CNOT with control=0, target=1
qc.measure([0, 1], [0, 1])  # Measure both qubits
```

**Running the Circuit:**

```python
from qiskit import Aer, execute

simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print(counts)
# Expected output: {'00': ~512, '11': ~512}
```

You should see approximately 50% "00" and 50% "11". This demonstrates entanglement: the qubits are always correlated (both 0 or both 1), never anti-correlated.

---

### Check Your Understanding : Multi-Qubit Gates

Answer these questions:

1. **What does the CNOT gate do?**
   *Hint: It flips the target if the control is 1.*

2. **How do you create a Bell state?**
   *Hint: Apply H then CNOT.*

3. **What is the Bell state equation?**
   *Hint: It's (|00⟩ + |11⟩)/√2.*

4. **What does the SWAP gate do?**
   *Hint: It exchanges two qubits.*

5. **What is the Toffoli gate?**
   *Hint: It's a controlled-controlled-NOT.*

6. **If you measure a Bell state and get "00", what would you get if you measured again immediately?**
   *Hint: The state has collapsed, so you'd get the same result.*

7. **Why is CNOT important for quantum computing?**
   *Hint: It creates entanglement.*

---

## PART D: BUILDING YOUR FIRST QUANTUM CIRCUIT

### Section 1: The Circuit Structure

*"Now let me show you how to build complete quantum circuits in Qiskit."*

**The Basic Structure:**

A quantum circuit consists of:
1. **Quantum registers** (qubits): Where quantum operations happen
2. **Classical registers** (bits): Where measurement results are stored
3. **Gates**: Operations applied to qubits
4. **Measurements**: Extracting classical information from qubits

**In Qiskit:**

```python
from qiskit import QuantumCircuit

# Create a circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Apply gates
qc.h(0)      # Hadamard on qubit 0
qc.cx(0, 1)  # CNOT on qubits 0 and 1

# Measure
qc.measure([0, 1], [0, 1])  # Measure qubits 0 and 1 into classical bits 0 and 1

# Draw the circuit
print(qc.draw())
```

**Output:**

```
     ┌───┐     ┌─┐   
q_0: ┤ H ├──■──┤M├───
     └───┘┌─┴─┐└╥┘┌─┐
q_1: ─────┤ X ├─╫─┤M├
          └───┘ ║ └╥┘
c_0: ═══════════╩══╬═
                  ║ 
c_1: ══════════════╩═
```

**Understanding the Diagram:**

- `q_0` and `q_1` are the quantum registers (qubits)
- `c_0` and `c_1` are the classical registers (bits)
- `H` is the Hadamard gate
- `X` (inside a box) is the CNOT target
- `■` is the CNOT control
- `M` is measurement
- Lines show the flow of quantum operations

---

### Section 2: Complete Example : Bell State with Simulation

*"Let me walk you through a complete example with code, simulation, and analysis."*

```python
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Step 1: Create the circuit
qc = QuantumCircuit(2, 2)

# Step 2: Apply gates
qc.h(0)      # Superposition on qubit 0
qc.cx(0, 1)  # Entanglement between qubits 0 and 1

# Step 3: Measure
qc.measure([0, 1], [0, 1])

# Step 4: Simulate
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)

# Step 5: Display results
print("Circuit:")
print(qc.draw())
print("\nMeasurement Results:")
print(counts)
print(f"\nProbability of 00: {counts.get('00', 0) / 1024:.3f}")
print(f"Probability of 11: {counts.get('11', 0) / 1024:.3f}")
print(f"Probability of 01: {counts.get('01', 0) / 1024:.3f}")
print(f"Probability of 10: {counts.get('10', 0) / 1024:.3f}")

# Step 6: Plot histogram
plot_histogram(counts)
plt.show()
```

**Expected Output:**

```
Circuit:
     ┌───┐     ┌─┐   
q_0: ┤ H ├──■──┤M├───
     └───┘┌─┴─┐└╥┘┌─┐
q_1: ─────┤ X ├─╫─┤M├
          └───┘ ║ └╥┘
c_0: ═══════════╩══╬═
                  ║ 
c_1: ══════════════╩═

Measurement Results:
{'00': 512, '11': 512}

Probability of 00: 0.500
Probability of 11: 0.500
Probability of 01: 0.000
Probability of 10: 0.000
```

**What This Shows:**

- The circuit creates a Bell state (|00⟩ + |11⟩)/√2
- When measured, you get "00" 50% of the time and "11" 50% of the time
- You never get "01" or "10" , the qubits are always correlated

---

### Section 3: A More Complex Circuit : 3-Qubit GHZ State

*"Let me show you a more impressive circuit: the GHZ state (Greenberger-Horne-Zeilinger state)."*

**The GHZ State:**

The GHZ state is an entangled state of 3 qubits:

|GHZ⟩ = (|000⟩ + |111⟩)/√2

**The Circuit:**

1. Apply H to qubit 0
2. Apply CNOT with control=0, target=1
3. Apply CNOT with control=1, target=2

**In Qiskit:**

```python
qc = QuantumCircuit(3, 3)
qc.h(0)      # Superposition on qubit 0
qc.cx(0, 1)  # Entangle qubits 0 and 1
qc.cx(1, 2)  # Entangle qubits 1 and 2
qc.measure([0, 1, 2], [0, 1, 2])
```

**Expected Results:**

After simulation, you should see approximately 50% "000" and 50% "111". All three qubits are correlated.

**Why This Matters for QML:**

In quantum machine learning, you'll use circuits with multiple qubits and multiple layers of gates. Understanding how to build and analyze circuits with 3+ qubits is essential.

---

### Section 4: Reading Circuit Diagrams

*"As you build more complex circuits, you'll need to read circuit diagrams. Let me explain the symbols."*

**Common Gate Symbols:**

| Symbol | Gate | Description |
|--------|------|-------------|
| `H` | Hadamard | Creates superposition |
| `X` | Pauli-X | Quantum NOT |
| `Y` | Pauli-Y | Bit and phase flip |
| `Z` | Pauli-Z | Phase flip |
| `S` | Phase | 90° phase |
| `T` | T gate | 45° phase |
| `Rx(θ)` | Rotation X | Arbitrary rotation around X |
| `Ry(θ)` | Rotation Y | Arbitrary rotation around Y |
| `Rz(θ)` | Rotation Z | Arbitrary rotation around Z |
| `●` | Control | Control point for controlled gates |
| `⊕` | Target | Target of CNOT |
| `M` | Measurement | Measures qubit into classical bit |

**Reading a Circuit:**

Read circuits from left to right:
1. Leftmost operations happen first
2. Rightmost operations happen last
3. Each horizontal line represents a qubit
4. Vertical lines represent multi-qubit gates

**Example: Understanding the Bell State Circuit**

```
     ┌───┐     ┌─┐   
q_0: ┤ H ├──■──┤M├───
     └───┘┌─┴─┐└╥┘┌─┐
q_1: ─────┤ X ├─╫─┤M├
          └───┘ ║ └╥┘
```

Reading left to right:
1. Apply H to q_0 (creates superposition)
2. Apply CNOT with control=q_0, target=q_1 (creates entanglement)
3. Measure q_0 and q_1

---

### Check Your Understanding : Building Circuits

Answer these questions:

1. **How do you create a quantum circuit with 3 qubits and 3 classical bits in Qiskit?**
   *Hint: Use QuantumCircuit(3, 3).*

2. **What does the `■` symbol represent in a circuit diagram?**
   *Hint: It's the control point of a CNOT gate.*

3. **What does the `⊕` symbol represent?**
   *Hint: It's the target of a CNOT gate.*

4. **How do you measure qubits in Qiskit?**
   *Hint: Use qc.measure().*

5. **What is the GHZ state for 3 qubits?**
   *Hint: It's (|000⟩ + |111⟩)/√2.*

6. **In a circuit diagram, do you read from left to right or right to left?**
   *Hint: Left to right.*

7. **What simulator should you use for measurement statistics?**
   *Hint: qasm_simulator.*

---

## PART E: PRACTICE EXERCISES

### Exercise 1: Bell State

**Goal:** Create a Bell state and verify entanglement.

```python
from qiskit import QuantumCircuit, Aer, execute

# Your code here
qc = QuantumCircuit(2, 2)

# Create Bell state
qc.h(0)      # Superposition
qc.cx(0, 1)  # Entanglement
qc.measure([0, 1], [0, 1])

# Simulate
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)

print(counts)
# Expected: {'00': ~512, '11': ~512}
```

**Check Your Understanding:**
- Why do you only see "00" and "11", not "01" or "10"?
- What would happen if you measured qubit 0 only, not qubit 1?

---

### Exercise 2: Superposition of All States

**Goal:** Create equal superposition of all 8 states using 3 qubits.

```python
qc = QuantumCircuit(3, 3)

# Apply H to all 3 qubits
qc.h(0)
qc.h(1)
qc.h(2)
qc.measure([0, 1, 2], [0, 1, 2])

# Simulate
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)

print(counts)
# Expected: All 8 states with approximately equal probability
```

**Check Your Understanding:**
- How many states should you see?
- What is the probability of each state?

---

### Exercise 3: X Gate and Measurement

**Goal:** Apply X gate to flip a qubit and verify.

```python
qc = QuantumCircuit(1, 1)

# Flip |0⟩ to |1⟩
qc.x(0)
qc.measure(0, 0)

# Simulate
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)

print(counts)
# Expected: {'1': 1024} (all measurements are 1)
```

**Check Your Understanding:**
- Why do you get "1" 100% of the time?
- What would happen if you applied H before X?

---

### Exercise 4: Hadamard and Z Gate

**Goal:** Apply H, then Z, then H and observe the effect.

```python
qc = QuantumCircuit(1, 1)

qc.h(0)  # Superposition
qc.z(0)  # Phase flip
qc.h(0)  # Back from superposition
qc.measure(0, 0)

# Simulate and observe results
```

**Check Your Understanding:**
- What do you expect to see?
- Hint: H·Z·H = X (this is a fundamental identity)
- So this circuit should give |1⟩ 100% of the time

---

## LECTURE 3 SUMMARY

*"Team, let me summarize what you've learned today."*

**Part A: Quantum Gates Overview**

- Quantum gates are unitary (reversible) transformations
- They rotate qubits on the Bloch sphere
- They're represented by matrices
- Applied to qubits via matrix multiplication

**Part B: Single-Qubit Gates**

- X gate: Quantum NOT (flips |0⟩ ↔ |1⟩)
- Y gate: Similar to X but with phase
- Z gate: Phase flip
- H gate: Creates superposition
- S gate: 90° phase
- T gate: 45° phase
- Rx(θ), Ry(θ), Rz(θ): Arbitrary rotations

**Part C: Multi-Qubit Gates**

- CNOT: Controlled-NOT (creates entanglement)
- SWAP: Exchanges qubits
- Toffoli: Controlled-controlled-NOT
- Bell state: (|00⟩ + |11⟩)/√2 (created with H + CNOT)

**Part D: Building Circuits**

- QuantumCircuit(n_qubits, n_bits) creates a circuit
- qc.gate_name(qubit) applies a gate
- qc.measure(qubits, bits) measures
- qc.draw() visualizes the circuit
- Aer.get_backend('qasm_simulator') simulates
- execute(qc, simulator, shots=N) runs the circuit

**Part E: Practice**

- You can now create Bell states, GHZ states, and arbitrary superpositions
- You can simulate circuits and analyze measurement results
- You understand circuit diagrams

---

## VIDEO RESOURCES FOR LECTURE 3

Watch these videos to reinforce your understanding.

**Video 1: "Quantum Gates Explained"**
- *Search on YouTube:* "Quantum gates explained Bloch sphere rotations"
- *Why watch:* Visualizes how gates rotate qubits on the Bloch sphere
- *Focus on:* Understanding the geometric interpretation

**Video 2: "CNOT Gate and Entanglement"**
- *Search on YouTube:* "CNOT gate entanglement quantum computing"
- *Why watch:* Shows how CNOT creates entanglement
- *Focus on:* Understanding the controlled operation

**Video 3: "Qiskit Tutorial for Beginners"**
- *Search on YouTube:* "Qiskit tutorial first quantum circuit"
- *Why watch:* Walks through building your first circuit
- *Focus on:* Following along with the code

**Video 4: "Quantum Circuit Diagrams"**
- *Search on YouTube:* "Quantum circuit diagram symbols explained"
- *Why watch:* Explains the notation used in circuit diagrams
- *Focus on:* Learning the symbols for different gates

**Video 5: "Bell State and GHZ State"**
- *Search on YouTube:* "Bell state GHZ state quantum entanglement"
- *Why watch:* Shows examples of entangled states
- *Focus on:* Understanding the correlation between qubits

---

## HOMEWORK ASSIGNMENT : BEFORE LECTURE 4

**Task 1: Watch the Videos**
Watch all five videos listed above. Take notes on anything confusing.

**Task 2: Run the Practice Exercises**

Run all four practice exercises from Part E. Experiment with:
- Changing the number of shots
- Adding more gates
- Applying gates to different qubits

**Task 3: Create Your Own Circuit**

Create a circuit that:
1. Starts with 2 qubits in |00⟩
2. Applies H to both qubits
3. Applies CNOT with control=0, target=1
4. Measures both qubits

Run it and explain the results.

**Task 4: Matrix Multiplication Practice**

For the following, calculate the result (you can do this by hand or with Python):

1. X|0⟩ = ?
2. X|1⟩ = ?
3. H|0⟩ = ?
4. H|1⟩ = ?
5. Z|1⟩ = ?

**Task 5: Document Your Learning**

Update your README with what you learned in this lecture. Include:
- Summary of single-qubit gates
- Summary of multi-qubit gates
- Code examples for Bell state and GHZ state
- Circuit diagrams

**Task 6: Team Discussion**

Meet with your teammates and discuss:
- Can you explain the Bell state to someone else?
- Can you read a circuit diagram?
- What questions do you still have about quantum gates?
- How do you think gates will be used in quantum machine learning?

---

## WHAT'S NEXT : LECTURE 4 PREVIEW

*"In our next lecture, we will dive deeper into entanglement and interference, the two phenomena that give quantum computing its power."*

**Lecture 4 Topics:**

- Entanglement: A deeper understanding
- Quantum interference: How quantum algorithms amplify correct answers
- The Deutsch-Jozsa algorithm (your first quantum algorithm!)
- More Qiskit practice
- Introduction to quantum parallelism

**Why Lecture 4 Matters:**

- Entanglement is the "secret sauce" of quantum computing
- Interference is how quantum algorithms actually work
- The Deutsch-Jozsa algorithm is the simplest quantum algorithm that demonstrates quantum advantage
- You'll start thinking about how to design quantum algorithms, not just circuits

---

**END OF LECTURE 3**
