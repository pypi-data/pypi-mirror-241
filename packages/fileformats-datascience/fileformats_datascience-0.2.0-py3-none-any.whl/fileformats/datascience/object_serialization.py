from fileformats.generic import File
from fileformats.core.mixin import WithMagicNumber
from fileformats.application import Gzip


class ObjectSerialisation(File):
    iana_mime = None
    binary = True


class Pickle(WithMagicNumber, ObjectSerialisation):
    """Python's native byte-encoded serialization format"""
    ext = ".pkl"
    magic_number = "8004"


class Pickle__Gzip(Gzip[Pickle]):
    """Python pickle file that has been gzipped"""
    ext = "pkl.gz"
    alternate_exts = (".pklz",)
    iana_mime = "application/x-pickle+gzip"
