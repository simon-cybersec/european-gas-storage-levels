import sys
from AGSI_manager import getGasLevels


# --------- MAIN ---------
if __name__ == '__main__':
    ret = getGasLevels()
    sys.exit(ret)
