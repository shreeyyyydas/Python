import sys

def check_python_installation():
    print("Python is installed.")
    print("Python Version Info:")
    print("Version:", sys.version)
    print("Version Info Tuple:", sys.version_info)

if __name__ == "__main__":
    check_python_installation()
