
from quakemapfilereader import QuakeMapFileReader

def main():
    
    qmfr = QuakeMapFileReader()
    qmf = qmfr.readQuakeMapFile("maps/ad_sepulcher.map")

    print(qmf)

if __name__ == "__main__":
    main()

