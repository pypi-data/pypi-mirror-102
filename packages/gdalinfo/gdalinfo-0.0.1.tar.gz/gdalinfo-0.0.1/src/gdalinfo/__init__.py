"""
A cffi binding to gdalinfo.
"""

from _gdalinfo import ffi, lib
import json

lib.GDALAllRegister()


class GDALException(Exception):
    def __init__(self):
        Exception.__init__(
            self,
            lib.CPLGetLastErrorNo(),
            ffi.string(lib.CPLGetLastErrorMsg()).decode("utf-8"),
        )


def info(path):
    """
    Return gdalinfo json for file at path.
    """
    dataset = lib.GDALOpen(str(path).encode("utf-8"), lib.GA_ReadOnly)
    if dataset == ffi.NULL:
        raise GDALException()

    try:
        options = ffi.gc(
            lib.GDALInfoOptionsNew(
                [ffi.new("char[]", arg) for arg in b"-json -mdd all".split()]
                + [ffi.NULL],
                ffi.NULL,
            ),
            lib.GDALInfoOptionsFree,
        )
        info = ffi.gc(lib.GDALInfo(dataset, options), lib.VSIFree)
        if info == ffi.NULL:
            raise GDALException()
    finally:
        lib.GDALClose(dataset)

    return json.loads(ffi.string(info).decode("utf-8"))
