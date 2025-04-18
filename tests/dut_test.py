import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def or_test(dut):
    """Test the OR gate with all input combinations."""
    a = (0, 0, 1, 1)
    b = (0, 1, 0, 1)
    y = (0, 1, 1, 0)

    for i in range(4):
        dut.a.value = a[i]
        dut.b.value = b[i]
        await Timer(1, units='ns')
        assert dut.y.value == y[i], f"OR gate failed at iteration {i}, got {dut.y.value}, expected {y[i]}"
        print(f"Test {i}: a={a[i]}, b={b[i]}, y={dut.y.value} (expected {y[i]})")
    print("OR gate test passed")
