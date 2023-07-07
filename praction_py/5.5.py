code, size, mem_limit=map(int,(input("code, size, mem_limit").split()))
    # initialize memory and pointer
memory = [0] * mem_limit
pointer = 0

# loop through each command
cmd_pointer = 0
while cmd_pointer < size:
    cmd = code[cmd_pointer]
    
    # command 0: move pointer right
    if cmd == 0:
        pointer += 1
        if pointer >= mem_limit:
            print("Error: pointer out of memory limit")
            break 
    
    # command 1: move pointer left
    elif cmd == 1:
        pointer -= 1
        if pointer < 0:
            print("Error: pointer underflow")
            break
    
    # command 2: increment current cell
    elif cmd == 2:
        memory[pointer] += 1
    
    # command 3: decrement current cell
    elif cmd == 3:
        memory[pointer] -= 1
    
    # command 4: output current cell
    elif cmd == 4:
        print(memory[pointer])
    
    # command 5: input to current cell
    elif cmd == 5:
        memory[pointer] = ord(input()[0])
    
    # command 6: start loop
    elif cmd == 6:
        if memory[pointer] == 0:
            depth = 1
            while depth > 0:
                cmd_pointer += 1
                if code[cmd_pointer] == 6:
                    depth += 1
                elif code[cmd_pointer] == 7:
                    depth -= 1
    
    # command 7: end loop
    elif cmd == 7:
        if memory[pointer] != 0:
            depth = 1
            while depth > 0:
                cmd_pointer -= 1
                if code[cmd_pointer] == 7:
                    depth += 1
                elif code[cmd_pointer] == 6:
                    depth -= 1
    
    # invalid command
    else:
        print("Error: invalid command")
        break
    
    cmd_pointer += 1
