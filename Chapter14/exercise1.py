import os


def sed(pattern, replacement, fileread, filewrite):
    fin_file_read = open(fileread, encoding="utf-8")
    string_file_read = fin_file_read.read()

    fin_file_write = open(filewrite, "w", encoding="utf-8")

    string_file_read = string_file_read.replace(pattern, replacement)
    fin_file_write.write(string_file_read)

    fin_file_read.close()
    fin_file_write.close()


pattern = "2"
replacement = "5"

file_read = r".\Chapter14\file_read.txt"
file_write = r".\Chapter14\file_write.txt"
sed(pattern=pattern, replacement=replacement, fileread=file_read, filewrite=file_write)
