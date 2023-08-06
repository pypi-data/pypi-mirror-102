import os

def safeopen(file, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    if mode not in ("w", "w+", "wb+") or not os.path.exists(file):
        return open(file, mode, buffering, encoding, errors, newline, closefd, opener)

    if "\\" in file or "/" in file:
        orig_dir_index = max(file.rfind("\\"), file.rfind("/")) + 1
        orig_dir = file[:orig_dir_index]
        orig_file = file[orig_dir_index:]
    else:
        orig_dir = ""
        orig_file = file

    if "." not in orig_file:
        orig_name = orig_file
        orig_ext = ""
    else:
        ext_index = orig_file.rfind(".")
        orig_name = orig_file[:ext_index]
        orig_ext = orig_file[ext_index:]

    file_copy_counter = 0
    current_dir = os.listdir(orig_dir) if orig_dir else os.listdir(".")
    while True:
        file_copy_counter += 1
        new_file = f"{orig_dir}{orig_name}_({file_copy_counter}){orig_ext}"
        if new_file not in current_dir:
            break

    return open(new_file, mode, buffering, encoding, errors, newline, closefd, opener)
