## Sophie
Sophie (Hebrew for "Finite") is an esoteric programming language designed to **not** be Turing Complete. Instead being equivalent to a Finite State Machine. I feel Finite State Machines are underappreciated. 

### Instructions


    [] - loop until break
    * - break loop
    . - output accumultor as number
    : - input number to accumulator
    , - output accumulator as char
    ; - input char to accumulator
    @c{}{} - if accumulator is c, do the first {} otherwise do the second {} (second {} optional)
    @$n{}{} - if accumulator is n, do the first {} otherwise do the second {} 
    #c - load char constant c into accumulator 
    #$n - load number constant n into accumulator 
    & - halt
    
    ("$$" for '$')
    
Instructions may be changed or added. Currently all number input can only be positive but that might also change. 

### Example Programs
cat - repeats whatever input is given to it  
creaturey vs. mimi - a Truttle1 style RPG battle (I had to generate this using a python script, you can't really avoid repitition in FSMs)  
fizzbuzz - This doesn't increment automatically (because that's impossible), it only recieves a number in unary and echos "Fizz", "Buzz" or "FizzBuzz" accordingly    
fizzbuzz2 - same as fizzbuzz but it receives input in Arabic numerals.  
hw - A Hello World Program.
truth_machine - If inputted with 0, outputs 0. If inputted with 1, outputs 1 in an endless loop.   
xor - Recieves 2 numbers as input and xors them (If the number is higher than 1 it is treated as a 1)      
yes - outputs "y" until the program terminates


  

 
  
