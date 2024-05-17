import hashlib

from pathlib            import Path
from .basecollector     import DataCollector
from ..data             import FileInfo



class FileInfoCollector(DataCollector):
    def __init__(self, path, hash_alg=None):
        self.path       = path
        self.hash_alg   = hash_alg


    def get_file_hash(self):
        hash_func = hashlib.new(self.hash_alg)
        with open(self.path, 'rb') as f:
            chunk = f.read(8192)
            while chunk:
                hash_func.update(chunk)
                chunk = f.read(8192)
    
        return hash_func.hexdigest()


    def collect(self) -> FileInfo:
        file = Path(self.path)
        file_stats = file.stat()

        file_hash = self.get_file_hash() if self.hash_alg else ""
    
        file_info = FileInfo(
            path    = self.path,
            name    = file.name,
            hash    = file_hash,
            size    = file_stats.st_size,
            uid     = file_stats.st_uid,
            gid     = file_stats.st_gid,
            atime   = file_stats.st_atime,
            ctime   = file_stats.st_ctime,
            mtime   = file_stats.st_mtime,
        )
        return file_info
