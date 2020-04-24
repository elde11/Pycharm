# with open("blalblb.txt") as f:
#   read_file = f.read()
#    print(read_file)
##
# print(f.read())


class OurOpen:
    def __init__(self, file_path):
        self._file_path = file_path

    def __enter__(self):
        print('Im enter')
        self.file = open(self._file_path)
        return  file

    def __exit__(self, _, _1, _2):
        self.file.close()
        print("I'm Exit")


with OurOpen("blabla.txt") as f:
    print("Im inside with")
    print(f)
    print(f.read())
