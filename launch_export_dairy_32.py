import subprocess

# Path to 32-bit Python interpreter
py32_path = r"C:\Python38-32\python.exe"

# Path to the actual export logic (to be run by 32-bit Python)
script_path = r"C:\Users\admin\PycharmProjects\PythonProject\export_diary.py"

# Launch it
subprocess.run([py32_path, script_path])
