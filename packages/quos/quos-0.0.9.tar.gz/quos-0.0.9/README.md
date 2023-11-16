# Quos package

Quos package simplifies plotting and simulating a quantum computing circuit employing oscillatory qubits.

### To install

    pip install matplotlib
    pip install quos

### To upgrade

    pip install --upgrade quos

### To open information page

    import quos
    quos.qdoc()

## To plot a circuit

    import quos
    quos.qplt('1,3,0|H,1,1|X,2,1|Z,3,2|Y,4,2|C,1,3,X,3,3|K,4,3|Rx 30,2,4|R 30 30 60,3,4|Cd,4,5,H,3,6|Ph 15,1,5|Pp 45,2,5|Ry 45,4,6|Sw,1,6,Sw,2,6|S,4,4|Rz 15,1,7|T,3,7|V,4,7|O,a,8|iSw,1,9,iSw,4,9|M,a,10')

- Q0 (qubit 0) on qubit other than 3 at time 0
- Q0 (qubit 1) on qubit 3 at time 0
- H (Hadamard gate) on qubit 1 at time 1
- X (Pauli X gate) on qubit 2 at time 1
- Z (Pauli Z gate) on qubit 3 at time 2
- Y (Pauli Y gate) on qubit 4 at time 2
- C (control point) on qubit 1 at time 3 controlling
- X (Pauli X gate) on qubit 3 at time 3
- K (Komparator gate) on qubit 4 at time 3
- Rx (rotation by 30 around X) on qubit 2 at time 4
- R (rotation by 30 30 60 around X Y Z) on qubit 3 at time 4
- Cd (reverse control point) on qubit 4 at time 5 controlling
- H (Hadamard gate) on qubit 3 at time 6
- Ph (global phase gate by 15) on qubit 1 at time 5
- Pp (phase gate for second state by 45) on qubit 2 at time 5
- Ry (rotation by 45 around Y) on qubit 4 at time 6
- Sw (swap) qubit 1 at time 6 with qubit 2 at time 6
- S (S gate) on qubit 4 at time 4
- Rz (rotation by 15 around Z) on qubit 1 at time 7
- T (T gate) on qubit 3 at time 7
- V (V gate) on qubit 4 at time 7
- O (Observer gate) on all qubits at time 8
- iSw (imaginary swap) qubit 1 at time 9 with qubit 4 at time 9
- M (Measurement gate) on all qubits at time 10

## Gates included

- Qubits
- 0: qubit in state 0
- 1: Qubit in state 1

- Individual gates
- I: Identity
- T: T (Pi/8 phase gate)
- Ph: Global phase gate
- Pp: Phase gate for second state
- H: Hadamard
- X: (Pauli) X gate
- Y: (Pauli) Y gate
- Z: (Pauli) Z gate
- Rx: Rotation around X
- Ry: Rotation around Y
- Rz: Rotation around Z
- R: Rotation around arbitrary axis
- V: V (sqrt X) phase
- S: S (sqrt Z) phase

- Interactive gates
- C: Controls another gate
- Cd: Reverse-controls another gate
- Sw: Swaps with another gate
- iSw: Imaginary swaps with another gate

- Measurement related
- M: Measurement gate
- O: Observation gate
- K: Komparator (Comparator) gate

## Note

These gates may work for qudits as well as qubits.

### Version History

- 0.0.1 2023-11-07 Initial release
- 0.0.2 2023-11-07 Minor corrections
- 0.0.3 2023-11-07 Minor corrections
- 0.0.4 2023-11-07 Minor corrections
- 0.0.5 2023-11-09 Removed dependancy on networkx package
- 0.0.6 2023-11-09 Enabled plotting of CNOT gate
- 0.0.7 2023-11-10 Enabled arguments and plotting of qubits
- 0.0.8 2023-11-14 Enabled several other gates
- 0.0.9 2023-11-15 Enabled measurement gates
