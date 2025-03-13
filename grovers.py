from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2)

qc.h([0, 1])

qc.cz(0, 1) 

qc.h([0, 1])
qc.x([0, 1]) 
qc.h(1)
qc.cx(0, 1)
qc.h(1)
qc.x([0, 1])
qc.h([0, 1])

qc.measure_all()

simulator = Aer.get_backend('aer_simulator')
compiled_circuit = transpile(qc, simulator)

job = simulator.run(compiled_circuit)
result = job.result()

counts = result.get_counts()
print(counts)

qc.draw('mpl')
plot_histogram(counts).show()
plt.show() 