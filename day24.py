def parse(text):
    inputs_txt, gates_txt = text.split("\n\n")
    return {i[0]: int(i[1]) for i in (i.split(": ") for i in inputs_txt.split("\n"))}, {
        g[4]: (g[0], g[1], g[2]) for g in (g.split(" ") for g in gates_txt.split("\n"))
    }


def run_gate(inputs, gates, gate):
    if gate in gates:
        i1, op, i2 = gates[gate]
        v1 = run_gate(inputs, gates, i1)
        v2 = run_gate(inputs, gates, i2)
        if op == "AND":
            return v1 & v2
        elif op == "OR":
            return v1 | v2
        elif op == "XOR":
            return v1 ^ v2
        else:
            raise RuntimeError(f"unhandled op: {op} for gate: {gate}")
    elif gate in inputs:
        return inputs[gate]
    else:
        raise RuntimeError("gate not found: " + gate)


def run_circuit(inputs, gates):
    values = {}
    for n, v in inputs.items():
        values[n] = v
    output = 0

    for gate in gates:
        if gate[0] == "z":
            v = run_gate(inputs, gates, gate)
            output |= v << int(gate[1:])
    return output


def fix_gates(inputs, gates):
    gates["z10"], gates["gpr"] = gates["gpr"], gates["z10"]
    gates["z21"], gates["nks"] = gates["nks"], gates["z21"]
    gates["z33"], gates["ghp"] = gates["ghp"], gates["z33"]
    gates["krs"], gates["cpm"] = gates["cpm"], gates["krs"]
    x = 0
    y = 0
    z = 0
    for i, v in inputs.items():
        if i[0] == "x":
            x |= v << int(i[1:])
        elif i[0] == "y":
            y |= v << int(i[1:])
    for gate in gates:
        if gate[0] == "z":
            v = run_gate(inputs, gates, gate)
            z |= v << int(gate[1:])
    mask = 2**10 - 1
    print(
        f"x: {x:46b}{x >> 40 & mask : 07b}{x >> 30 & mask : 011b}{x >> 20 & mask : 011b}{x >> 10 & mask : 011b}{x & mask: 011b}"
    )
    print(
        f"y: {y:46b}{y >> 40 & mask : 07b}{y >> 30 & mask : 011b}{y >> 20 & mask : 011b}{y >> 10 & mask : 011b}{y & mask: 011b}"
    )
    print(
        f"z: {z:46b}{z >> 40 & mask : 07b}{z >> 30 & mask : 011b}{z >> 20 & mask : 011b}{z >> 10 & mask : 011b}{z & mask: 011b}"
    )
    print(
        f"c: {x+y:46b}{x+y >> 40 & mask : 07b}{x+y >> 30 & mask : 011b}{x+y >> 20 & mask : 011b}{x+y >> 10 & mask : 011b}{x+y & mask: 011b}"
    )
    return ",".join(sorted(["z10", "gpr", "z21", "nks", "z33", "ghp", "krs", "cpm"]))


if __name__ == "__main__":
    with open("day24.txt") as f:
        inputs, gates = parse(f.read().strip())
    test_inputs, test_gates = parse(
        """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""
    )

    print(run_circuit(test_inputs, test_gates))
    print(run_circuit(inputs, gates))
    print(fix_gates(inputs, gates))
