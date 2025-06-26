from functions.get_files_info import get_files_info

def run_tests():
    print("Test 1: get_files_info('calculator', '.')")
    print(get_files_info("calculator", "."))
    print("\n" + "="*60 + "\n")

    print("Test 2: get_files_info('calculator', 'pkg')")
    print(get_files_info("calculator", "pkg"))
    print("\n" + "="*60 + "\n")

    print("Test 3: get_files_info('calculator', '/bin')  # Should error (outside working directory)")
    print(get_files_info("calculator", "/bin"))
    print("\n" + "="*60 + "\n")

    print("Test 4: get_files_info('calculator', '../')  # Should error (outside working directory)")
    print(get_files_info("calculator", "../"))
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    run_tests()
