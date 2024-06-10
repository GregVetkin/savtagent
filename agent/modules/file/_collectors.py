import hashlib

from pathlib            import Path
from models             import BaseCollector
from ._models           import FileInfo



class FileInfoCollector(BaseCollector):
    def __init__(self, path, hash_alg=None):
        self._path       = path
        self._hash_alg   = hash_alg


    def _calculate_hash(self):
        hash_func = hashlib.new(self._hash_alg)
        with open(self._path, 'rb') as f:
            chunk = f.read(8192)
            while chunk:
                hash_func.update(chunk)
                chunk = f.read(8192)
        return hash_func.hexdigest()


    def collect(self) -> FileInfo:
        file        = Path(self._path)
        file_stats  = file.stat()
        file_hash   = self._calculate_hash() if self._hash_alg else ""
    
        return FileInfo(
            path    = self._path,
            name    = file.name,
            hash    = file_hash,
            size    = file_stats.st_size,
            uid     = file_stats.st_uid,
            gid     = file_stats.st_gid,
            atime   = file_stats.st_atime,
            ctime   = file_stats.st_ctime,
            mtime   = file_stats.st_mtime,
        )
