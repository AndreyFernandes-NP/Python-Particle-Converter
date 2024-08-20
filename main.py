import re
import tkinter as tk
from tkinter import filedialog
from timeit import default_timer as timer

root = tk.Tk()
root.withdraw()

def askforfile():
    file_path = filedialog.askopenfilename()  
    return file_path

input("Startup finished, press ENTER to start the conversion.")

file_dir = askforfile()
marca_dagua = ["### CONVERTER OF THE CONVERTER MADE BY R4IN\n", "### SPAGHETTI CODE SENT REGARDS\n\n"]

with open("converted_particles.mcfunction", 'w') as rw:
        rw.write(marca_dagua[0])
        rw.write(marca_dagua[1])
        pass

start_t = timer()

try:
    
    try:
        with open(file_dir, 'r') as f:
            for line in f:
                if "#" in line:
                    continue
                if line == "\n":
                    continue
                split_line = line.split()
                val = []
                cval = []

                for x in split_line:
                    if not re.search('[a-zA-Z]', x):
                        val.append(x)

                    else:
                        cval.append(x)

                resulted_command = f"particle {cval[1]}{{color:[{val[0]},{val[1]},{val[2]}],scale:{val[3]}}} {val[4]} {val[5]} {val[6]} {val[7]} {val[8]} {val[9]} {val[10]} {val[11]} {cval[2]} {cval[3]} \n"
            
                with open("converted_particles.mcfunction", 'a') as nf:
                    nf.write(resulted_command)

    except ValueError as e:
        raise(e)
            
except FileNotFoundError as e:
   raise(e)

end_t = timer()

print(f"\nCONVERSION ELAPSED TIME: {(end_t - start_t):.2f} second(s)")
input("PRESS ENTER TO LEAVE.")