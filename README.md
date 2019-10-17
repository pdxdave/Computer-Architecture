# Computer Architecture

## Project

* [Implement the LS-8 Emulator](ls8/)

## Task List: add this to the first comment of your Pull Request

### Day 1: Get `print8.ls8` running

- [ ] Inventory what is here
- [ ] Implement the `CPU` constructor
- [ ] Add RAM functions `ram_read()` and `ram_write()`
- [ ] Implement the core of `run()`
- [ ] Implement the `HLT` instruction handler
- [ ] Add the `LDI` instruction
- [ ] Add the `PRN` instruction

### Day 2: Add the ability to load files dynamically, get `mult.ls8` running

- [ ] Un-hardcode the machine code
- [ ] Implement the `load()` function to load an `.ls8` file given the filename
      passed in as an argument
- [ ] Implement a Multiply instruction (run `mult8.ls8`)




Objective challenge:
How would you perform an NOR operation between two numbers x and y if you didn’t have an NOR operator? How could you use the other bitwise operators to the same effect?

How would you perform an XOR operation between two numbers x and y if you didn’t have an XOR operator? How could you use the other bitwise operators to the same effect?

What is the result of 11011111 NOR 00010111?

```
  spaced for easier reading.

  1 1 0 1 1 1 1 1
  0 0 0 1 0 1 1 1
  ---------------

```

What is the result of 10101010 XOR 11110000?
```
  spaced for easier reading.  
  XOR is only true if one or the other is true, not both.

  1 0 1 0 1 0 1 0
^ 1 1 1 1 0 0 0 0
  ---------------
  0 1 0 1 1 0 1 0
```


What is the result of 11011 AND 101?

### Day 3: Stack

- [ ] Implement the System Stack and be able to run the `stack.ls8` program

### Day 4: Get `call.ls8` running

- [ ] Implement the CALL and RET instructions
- [ ] Implement Subroutine Calls and be able to run the `call.ls8` program

### Stretch

- [ ] Add the timer interrupt to the LS-8 emulator
- [ ] Add the keyboard interrupt to the LS-8 emulator
- [ ] Write an LS-8 assembly program to draw a curved histogram on the screen
