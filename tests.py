from functions.run_python import run_python_file
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.get_files_info import get_files_info

def run_tests():
    print("Test 1")
    print(get_file_content({'file_path': 'main.py'}))
    print("\n" + "="*60 + "\n")
    print("Test 2")
    print(write_file({'file_path': 'main.txt', 'content': 'hello'}))
    print("\n" + "="*60 + "\n")
    print("Test 3")
    print(run_python_file({'file_path': 'main.py'}))
    print("\n" + "="*60 + "\n")
    print("Test 4")
    print(get_files_info({'directory': 'pkg'}))
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    run_tests()
