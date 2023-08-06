if __name__ == "__main__":
    import sys
    import gdalinfo
    import pprint

    pprint.pprint(gdalinfo.info(sys.argv[1]))