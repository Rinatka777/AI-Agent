from functions.run_python import run_python_file

def run_tests():
    print("Test 1")
    print(run_python_file("calculator", "main.py"))
    print("\n" + "="*60 + "\n")
    print("Test 2")
    print(run_python_file("calculator", "tests.py"))
    print("\n" + "="*60 + "\n")
    print("Test 3")
    print(run_python_file("calculator", "../main.py"))
    print("\n" + "="*60 + "\n")
    print("Test 4")
    print(run_python_file("calculator", "nonexistent.py"))
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    run_tests()
