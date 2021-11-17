#%%

from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

circuit = QuantumCircuit(2,2)
circuit.x(0)
circuit.h(1)
circuit.measure([0,1],[0,1])
circuit.draw()

# %%
backend = Aer.get_backend('qasm_simulator')
results = execute(circuit, backend).result()
counts = results.get_counts()
print(counts)
plot_histogram(counts)