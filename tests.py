from functions.get_files_infos import get_files_infos

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
