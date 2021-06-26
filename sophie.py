import sys


def runstr(code):
    accumulator = None
    input_buffer = ""
    loop_stack = []
    if_else_stack = []
    #global accumulator, input_buffer,loop_stack,BreakSkip
    IP = 0
    
    while IP < len(code):
        codene = code[IP]
        if codene in " \n\t":
            pass
        elif codene == "&":
            return accumulator
        elif codene == "*":
            loop_stack.pop()
            bracket_count=0
            while code[IP] != "]":
                if code[IP] == "{":
                    bracket_count += 1
                elif code[IP] == "}":
                    bracket_count -= 1
                IP += 1
            if_else_stack.pop(bracket_count)
        elif codene == "#":
            IP += 1
            if code[IP] == "$":
                IP += 1
                if code[IP] == "$":
                    accumulator = ord("$")
                elif code[IP].isdigit():
                    numstr = ""
                    while IP < len(code) and code[IP].isdigit():
                        numstr += code[IP]
                        IP += 1
                    IP -= 1
                    accumulator = int(numstr)
                else:
                    print("Not a valid Number at {}",IP)
                    sys.exit(47)
            else:
                accumulator = ord(code[IP])
        elif codene == "[":
            loop_stack.append(IP + 1)
        elif codene == "]":
            IP = loop_stack[-1]
            continue
        elif codene == ";":
            try:
                if len(input_buffer) == 0:
                    input_buffer = input("") + "\n"

                accumulator = ord(input_buffer[0])
                input_buffer = input_buffer[1:]
            except EOFError:
                accumulator = 0
        elif codene == ",":
            print(chr(accumulator), end="")
        elif codene == ":":
            try:
                accumulator = int(input())
            except EOFError:
                accumulator = 0
        elif codene == ".":
            print(accumulator)
        elif codene == "@":
            IP += 1
            comparnum = None
            if code[IP] == "$":
                IP += 1
                if code[IP] == "$":
                    comparnum = ord("$")
                else:
                    numstr = ""
                
                    while IP < len(code) and code[IP].isdigit():
                        numstr += code[IP]
                        IP += 1
                    comparnum = int(numstr)
            else:
                comparnum = ord(code[IP])
                IP += 1
            if code[IP] == "{":
                if comparnum == accumulator:
                    if_else_stack.append(True)
                    """else:
                        if(IP+1<len(code) and code[IP+1]=="{"):
                            IP+=2
                            bracket_count=1
                            while(bracket_count>0):
                                IP+=1
                                if (code[IP]=="{"):
                                    bracket_count+=1
                                elif (code[IP]=="}"):
                                    bracket_count-=1
                                    """
                else:   
                    bracket_count = 1                 
                    while bracket_count > 0:
                        IP += 1
                        if code[IP] == "{":
                            bracket_count += 1
                        elif code[IP] == "}":
                            bracket_count -= 1
                    IP += 1
                    if code[IP] == "{":
                        if_else_stack.append(False)
                    else:
                        IP -= 1 #make sure it runs
            else:
                print("Bracket Required after @")  
                sys.exit(47)      
        elif codene == "}":
            state = if_else_stack.pop()
            if state and code[IP + 1] == "{":
                IP += 2
                bracket_count = 1
                while bracket_count > 0:
                    IP += 1
                    if code[IP] == "{":
                        bracket_count += 1
                    elif code[IP] == "}":
                        bracket_count -= 1
        else: #any other char
            print("Invalid codene {}".format(codene))
            sys.exit(47)
        
        IP += 1
    return accumulator


def generate_print(string):
    code = ""
    for c in string:
        code += "#" + c + ","
    return code


def generate_test(string):
    code = end = ""
    for c in string:
        code += ";@" + c + "{"
        end += "}"
    return code + end


if __name__ == "__main__":
    if sys.argv[1] == "-p":
        print(generate_print(sys.argv[2]))
    elif sys.argv[1] == "-t":
        print(generate_test(sys.argv[2]))
    else:
        sys.exit(runstr(open(sys.argv[1]).read()))
    sys.exit(0)
