module dut_test(
    input wire a,
    input wire b,
    output wire y
);
    dut xor_gate_inst(  // Corrected module instantiation
        .a(a),
        .b(b),
        .y(y)
    );

    initial begin  // Fixed 'initial' block syntax
        $dumpfile("waves.vcd");  // Corrected quotes
        $dumpvars(0, dut_test);  // Fixed incorrect system task
    end
endmodule
