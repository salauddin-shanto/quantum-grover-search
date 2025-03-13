# Grover's Algorithm: Quantum Search Implementation

## Introduction

Grover's algorithm is a quantum search algorithm that provides a quadratic speedup compared to classical search algorithms. It is particularly useful for searching an unsorted database of `N` elements in approximately `O(√N)` time, whereas classical algorithms require `O(N)` time. 

In this project, we implement a simple version of Grover’s algorithm using Qiskit on a two-qubit quantum circuit. Our goal is to find the marked state `|11⟩` using quantum superposition and phase inversion.

## Implementation

### Steps of the Algorithm:

1. **Superposition Initialization**: We apply Hadamard gates to both qubits to create an equal superposition of all possible states.
2. **Oracle**: The oracle marks the target state (`|11⟩`) by applying a controlled-Z (`CZ`) gate that flips its phase.
3. **Diffusion Operator**: This step amplifies the probability of measuring the correct state by inverting the amplitudes around their mean.
4. **Measurement**: Finally, all qubits are measured to observe the most probable state.

### Code:

```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2)

qc.h([0, 1])

qc.cz(0, 1)  # Controlled-Z gate flips the phase of |11⟩

qc.h([0, 1])  # Apply Hadamard again
qc.x([0, 1])  # Apply X (bit-flip)
qc.h(1)       # Apply H on qubit 1
qc.cx(0, 1)   # Apply CNOT (controlled-X)
qc.h(1)       # Apply H on qubit 1
qc.x([0, 1])  # Apply X again
qc.h([0, 1])  # Apply Hadamard again

qc.measure_all()

simulator = Aer.get_backend('aer_simulator')
compiled_circuit = transpile(qc, simulator)

job = simulator.run(compiled_circuit)
result = job.result()

counts = result.get_counts()
print(counts)

# Draw the circuit
qc.draw('mpl')
plot_histogram(counts).show()
plt.show()
```
## Results
### Quantum Circuit Representation

The following figure shows the quantum circuit for Grover’s algorithm.
![groverss11](https://github.com/user-attachments/assets/7ecde23a-317a-4533-9e05-99c6b4df6d2e)


### Measurement Results
The histogram below represents the measurement results, where the marked state `|11⟩` has the highest probability.
![grovers12](https://github.com/user-attachments/assets/3d8ba9eb-f4b1-41fb-9806-0fe3ffd7a903)

## Conclusion

This implementation successfully demonstrates Grover’s search algorithm on a two-qubit system. The quantum circuit marks the `|11⟩` state, and after applying the diffusion operator, the probability of measuring `|11⟩` is maximized. This small-scale demonstration can be extended to larger databases by increasing the number of qubits and iterations.

## References

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [Grover’s Algorithm - Quantum Computing](https://quantum-computing.ibm.com/)


