from . import cow
from sys import argv
def main(): print(cow(" ".join(argv[1:])))
if __name__ == "__main__": main()