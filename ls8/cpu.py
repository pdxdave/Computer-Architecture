"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""


    def __init__(self):
        """Also add properties for any internal registers you need, e.g. `PC`."""
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0

    def ram_read(self, MAR):
        """ should accept the address to read and return the value stored there."""
        return self.ram


    def ram_write(self, MAR):
        """should accept a value to write, and the address to write it to."""
        return self.ram

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations. Arithmetic Logic Unit.  OK, addition, subtraction, multiplication goes here """

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == 'MUL':
            self.reg[reg_a] += self.reg[reb_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """This code above requires the implementation of three instructions: LDI, PRN, HLT. values from cheat sheet"""
        """IR, the Instruction Register. This can just be a local variable in run()."""
        """Run the CPU."""
        HLT = 0b00000001             """ Halt the CPU (and exit the emulator)."""
        LDI = 0b10000010             """ Set the value of a register to an integer."""
        PRN = 0b1000111              """ Print numeric value stored in the given register."""
        PUSH = 0b01000101            """ Push the value in the given register on the stack. Think I'll need a method for this"""
        POP = 0b01000110             """ Pop the value at the top of the stack into the given register. Think I'll need a method for this"""
        CALL = 0b01010000            """ Calls a subroutine (function) at the address stored in the register. """
        RET = 0b00010001             """ Return from subroutine. """
        MUL = 0b10100010             """ Multiply the values in two registers together and store the result in registerA. """