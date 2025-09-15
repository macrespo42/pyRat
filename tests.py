from functions.get_files_infos import get_files_infos
from functions.get_file_content import get_file_content


def test_get_files_infos():
    print("Result for current directory: ")
    print(get_files_infos("calculator", "."))
    print("\n\n")

    print("Result for 'pkg' directory:")
    print(get_files_infos("calculator", "pkg"))
    print("\n\n")

    print("Result for '/bin' directory: ")
    print(get_files_infos("calculator", "/bin"))
    print("\n\n")

    print("Result for '../' directory: ")
    print(get_files_infos("calculator", "../"))


def test_get_file_content():
    print(get_file_content("calculator", "main.py"))
    print("\n\n")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("\n\n")
    print(get_file_content("calculator", "/bin/cat"))
    print("\n\n")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    test_get_file_content()
