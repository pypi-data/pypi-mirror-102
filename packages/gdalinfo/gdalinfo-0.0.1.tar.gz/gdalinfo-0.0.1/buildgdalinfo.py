from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef(
    """
typedef void *GDALDatasetH;

typedef enum {
    GA_ReadOnly = 0,
    GA_Update = 1
} GDALAccess;

void GDALAllRegister (void);

GDALDatasetH GDALOpen (const char *pszFilename, GDALAccess eAccess);
void GDALClose (GDALDatasetH);

typedef struct GDALInfoOptions GDALInfoOptions;
typedef struct GDALInfoOptionsForBinary GDALInfoOptionsForBinary;
GDALInfoOptions *GDALInfoOptionsNew (char** papszArgv, GDALInfoOptionsForBinary* psOptionsForBinary);
void GDALInfoOptionsFree (GDALInfoOptions *psOptions);

char *GDALInfo (GDALDatasetH hDataset, const GDALInfoOptions *psOptions);

void VSIFree (void *);   // free gdalinfo string with vsifree

typedef int CPLErrorNum;
CPLErrorNum CPLGetLastErrorNo (void);
const char* CPLGetLastErrorMsg (void);
"""
)

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source(
    "_gdalinfo",
    """
     #include "gdal/gdal_utils.h"   // the C header of the library
""",
    libraries=["gdal"],
)  # library name, for the linker

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)