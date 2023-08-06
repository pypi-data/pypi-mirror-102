"""
napari-STPT reads zarr files and displays them
"""
import sys
#from napari_stpt.napari_stpt import NapariSTPT
from napari_stpt import NapariSTPT

#print('Test entry point napari1')
#if __name__ == "__main__":
#    print('Test entry point napari2')
#napari_stpt.NapariSTPT().main(sys.argv[1:])

def main():
    print('inside main')
    nap = NapariSTPT()
    nap.main()

if __name__ == "__main__":
    main()