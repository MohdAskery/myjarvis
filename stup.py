import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Mohd Askery Malik\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Mohd Askery Malik\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("jarvis.py", base=base, icon="favicon.ico")]


cx_Freeze.setup(
    name = "jarvis",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["lisning.wav","reco.wav","C:\\Users\Mohd Askery Malik\\Desktop\myjarvis\\music\\ALAN WALKER FADED.mp3",'tcl86t.dll','tk86t.dll']}},
    version = "0.01",
    description = "jarvis  Application By Mohd Askery",
    executables = executables
    )