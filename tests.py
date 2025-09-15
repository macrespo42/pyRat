from functions.get_files_infos import get_files_infos
from functions.get_file_content import get_file_content
from functions.write_file import write_file


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


def test_write_file():
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))


if __name__ == "__main__":
    test_write_file()
