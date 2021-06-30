import sys


logfile=None
def runstr(code):
    global logfile
    accumulator=None
    input_buffer=""
    loop_stack=[] #the loop stack contains all the IPs after the [
    if_else_stack=[] #the if else stack contains all the conditionals to make sure {} work correctly
    IP=0
    while(IP<len(code)):
        #the codene is the char that is associated with a command
        codene=code[IP] 
        if (codene==" " or codene=="\n" or codene=="\t"): 
            pass
            
            
        elif (codene=="&"):
            return accumulator%256
        
        
        elif (codene=="*"):
            #Pop the break stack
            loop_stack.pop()
            #Jump to the end of the loop
            bracket_count=0
            while(code[IP]!="]"):
                if (code[IP]=="{"):
                    bracket_count+=1
                elif (code[IP]=="}"):
                    bracket_count-=1
                IP+=1
            #Make sure you don't leave any undealt with } in the stack
            if_else_stack.pop(bracket_count)
            
            
        elif (codene=="#"):
            IP+=1
            #If it's a number
            if (code[IP]=="$"):
                IP+=1
                if (code[IP]=="$"):
                    accumulator=ord("$") #not sure why I put this special case here. Just use $24
                
                elif code[IP].isdigit():
                    #Aggregate the digits
                    numstr=""
                    while IP < len(code) and code[IP].isdigit():
                        numstr+=code[IP]
                        IP+=1
                    IP-=1 #This nullifies the IP+=1 at the end of the loop
                    #Convert it to int and plop it into the accumulator
                    accumulator=int(numstr)
                        
                else:
                    print("Not a valid Number at {}".format(IP))
                    sys.exit(47)
            else: #char
                accumulator=ord(code[IP])
                
                
        elif (codene=="["):
            loop_stack.append(IP+1) 
            
            
        elif (codene=="]"):
            IP=loop_stack[-1]
            continue
            
            
        elif (codene==";"):
            try:
                if (len(input_buffer)==0):
                    input_buffer=input("")+"\n"
                    
            
                accumulator=ord(input_buffer[0])
                input_buffer=input_buffer[1:]
            except EOFError: #0 is EOF, because why not
                accumulator=0
                
                
        elif (codene==","):
            print(chr(accumulator),end="")
            
            
        elif (codene==":"):
            try:
                accumulator=int(input())
            except EOFError:
                accumulator=0
                
                
        elif (codene=="."):
            print(accumulator,end="")
            
            
        #conditional
        elif (codene=="@"):
            IP+=1
            #get the number to compare to (chars are converted to their Ascii/UTF-8 value)
            comparnum=None
            if (code[IP]=="$"):
                IP+=1
                if (code[IP]=="$"):
                    comparnum=ord("$")
                else:
                    numstr=""
                
                    while IP < len(code) and code[IP].isdigit():
                        numstr+=code[IP]
                        IP+=1
                    comparnum=int(numstr)
            else:
                comparnum=ord(code[IP])
                IP+=1
            #this bracket is required. So check for it.     
            if (code[IP]=="{"):
                if (comparnum==accumulator):
                    #Push a True so } will know that it might have to skip a {} clause
                    if_else_stack.append(True)
                            
                else:   
                    #skip the {} clause
                    bracket_count=1                 
                    while(bracket_count>0):
                        IP+=1
                        if (code[IP]=="{"):
                            bracket_count+=1
                        elif (code[IP]=="}"):
                            bracket_count-=1
                    IP+=1
                  
                    if (code[IP]=="{"):
                        #Push a False so } will know that it doesn't have to skip a {} clause
                        if_else_stack.append(False)
                    else:
                        #nullify the IP+=1 at the end
                        IP-=1 
                    
                    
            else:
                print("Bracket Required after @")  
                sys.exit(47)      
                
                
        elif codene=="}":
            state=if_else_stack.pop()
            #if the previous conditional was True and there is a { ahead
            if(state and code[IP+1]=="{"):
                #skip the clause
                IP+=2
                bracket_count=1
                while(bracket_count>0):
                    IP+=1
                    if (code[IP]=="{"):
                        bracket_count+=1
                    elif (code[IP]=="}"):
                        bracket_count-=1
                        
                        
        elif codene=="{": #comment
            #just skip the clause
            bracket_count=1
            IP+=1
            while(bracket_count>0):
                IP+=1
                if (code[IP]=="{"):
                    bracket_count+=1
                elif (code[IP]=="}"):
                    bracket_count-=1
                    
                    
        #debug info, puts accumulator and IP in a logfile
        elif codene=="d":
            if logfile==None:
                logfile=open ("sophie.log","w")
            logfile.write("accumulator: "+str(accumulator)+"\nIP: "+str(IP)+"\n\n")
            
            
        else: #any other char
            print("Invalid codene {}".format( codene))
            sys.exit(47)
        IP+=1
    
    return accumulator%256


#Return Sophie code to print a given string
def generate_print(string):
    code=""
    for c in string:
        code+="#"+c+","
    return code


#Return Sophie code to check for a given string
def generate_test(string):
    code=""
    end=""
    for c in string:
        code+=";@"+c+"{"
        end+="}"
    return code+end


if __name__=="__main__":
    if (sys.argv[1]=="-p"):
        print(generate_print(sys.argv[2]))
    elif(sys.argv[1]=="-t"):
        print(generate_test(sys.argv[2]))
    else:
        sys.exit(runstr(open(sys.argv[1]).read()))
    sys.exit(0)
