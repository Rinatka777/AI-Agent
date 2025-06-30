from functions.write_file import write_file

def run_tests():
    print("Test 1")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print("\n" + "="*60 + "\n")
    print("Test 2")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print("\n" + "="*60 + "\n")
    print("Test 3")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    run_tests()
