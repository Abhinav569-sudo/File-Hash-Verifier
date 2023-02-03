import sys
import hashlib


def hashfile(file):
    # An arbitrary (but fixed) buffer size (change accordingly).
    # 65536 = 65536 bytes = 64 kilobytes
    buff_size = 65536

    # Initializing the sha256() method.
    sha256 = hashlib.sha256()

    # Open the file provided as the first commandline argument.
    with open(file, 'rb') as f:
        while True:
            # Reading data = buff_size from the file and saving it in a variable.
            data = f.read(buff_size)

            # True if EOF = 1
            if not data:
                break

            # Passing that data to that sha256 hash
            # function (updating the function with that data)
            sha256.update(data)

    # sha256.hexdigest() hashes all the input
    # data passed to the sha256() via sha256.update()
    # Acts as a finalized method, after which
    # all the input data gets hashed hexdigest()
    # hashes the data, and returns the output
    # in hexadecimal format
    return sha256.hexdigest()


# Calling the hashfile() function to obtain hashes of the files,
# and saving the result in a variable
f1_hash = hashfile(sys.argv[1])
f2_hash = hashfile(sys.argv[2])

# Doing the primitive string comparison to check the hashes
if f1_hash == f2_hash:
    print("Both files are same.")
    print(f"Hash: {f1_hash}")

else:
    print("Files are different.")
    print(f"Hash of the file 1: {f1_hash}")
    print(f"Hash of the file 2: {f2_hash}")
