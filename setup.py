import os
import cx_Freeze
import sys
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Muhammad Faiq\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Muhammad Faiq\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("login.py", base = base, icon = "Icon")]

cx_Freeze.setup(
    name = "Attendance System Based on Facial Recognintion",
    options = {"build.exe" : {"pakages" : ["tkinter", "os"], "include_files":["Icon", "tcl86t.dll", "tk86t.dll", 'Photo_Sample', 'Database']}},
    version = 1.0,
    description = "Attesndance System Based on Facial Recognition | Developed By Muhammad Faiq",
    executables = executables,)