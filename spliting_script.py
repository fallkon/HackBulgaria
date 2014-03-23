from subprocess import call
import inspect  #function for getting functions names and source
import solution  #solutions file
#biblioteki dlia vibora i razdela na podzada4i 

al_F = inspect.getmembers(solution, inspect.isfunction) #gets functions names

for func_name in al_F:

    source_of_func = inspect.getsourcelines(func_name[1]) #gets the source of the functions
    call(["mkdir", func_name[0]]) #makes directories
    solution_file = open(func_name[0] + "/solution.py", "w")
    for line in source_of_func[0]:
        solution_file.write(line) #filles the solution file
    solution_file.close();
    call(["touch", func_name[0] + "/test.py"])
    print("making dir --"+ func_name[0] + "\n")
