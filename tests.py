from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def run_tests():
    print("Test 1")
    print(get_file_content("calculator", "lorem.txt"))
    print("\n" + "="*60 + "\n")
    print("Test 2")
    print(get_file_content("calculator", "main.py"))
    print("\n" + "="*60 + "\n")
    print("Test 3")
    print(get_file_content("calculator", "pkg/calculator.py"))  
    print("\n" + "="*60 + "\n")
    print("Test 4")
    print(get_file_content("calculator", "/bin/cat"))
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    run_tests()
