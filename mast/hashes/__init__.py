import hashlib


def _get_file_hash(filename, obj):
    """Given filename, returns the hash of the file as a string containing
    only hexadecimal digits. The algorithm used depends on the value passed
    to obj, which should be a  constructor for a hash algorithm available
    through hashlib. Convenience functions for the constructors which are
    always present are provided and listed here:

        get_md5
        get_sha1
        get sha224
        get_sha256
        get_sha384
        get_sha512

    More may be available depending on your version of OpenSSL, but these are
    always present."""
    _hash = obj()
    with open(filename, 'rb') as fin:
        _buffer = fin.read(65536)
        while len(_buffer) > 0:
            _hash.update(_buffer)
            _buffer = fin.read(65536)
    return _hash.hexdigest()


def get_md5(filename):
    """Return the md5 hash of filename"""
    return _get_file_hash(filename, hashlib.md5)


def get_sha1(filename):
    """Return the sha1 hash of filename"""
    return _get_file_hash(filename, hashlib.sha1)


def get_sha224(filename):
    """Return the sha224 hash of filename"""
    return _get_file_hash(filename, hashlib.sha224)


def get_sha256(filename):
    """Return the sha256 hash of filename"""
    return _get_file_hash(filename, hashlib.sha256)


def get_sha384(filename):
    """Return the sha384 hash of filename"""
    return _get_file_hash(filename, hashlib.sha384)


def get_sha512(filename):
    """Return the sha256 hash of filename"""
    return _get_file_hash(filename, hashlib.sha512)
