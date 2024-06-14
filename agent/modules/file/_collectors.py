import hashlib
import re
import os
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


class FileRegexCollector(BaseCollector):
    def __init__(self, filepath, pattern) -> None:
        self._filepath  = filepath
        self._pattern   = pattern

    def _pattern_verification(self):
        try:
            regex = re.compile(self._pattern)
        except re.error:
            return False
        else:
            return True

    def _file_verification(self):
        return os.path.exists(self._filepath) and os.path.isfile(self._filepath)

    def _txt_regex(self):
        coincidences = []
        with open(self._filepath, 'r') as file:
            for line in file:
                matches = re.findall(line)
                if matches:
                    for match in matches:
                        coincidences.append(match)
        return coincidences

    def _pdf_regex(self):
        pass
        raise Exception(f"Формат файла .pdf не поддерживается.")
    
    def _docx_regex(self):
        pass
        raise Exception(f"Формат файла .docx не поддерживается.")
    
    def _xlsx_regex(self):
        pass
        raise Exception(f"Формат файла .xlsx не поддерживается.")
    
    def _odt_regex(self):
        pass
        raise Exception(f"Формат файла .odt не поддерживается.")
    

    def collect(self):
        if not self._file_verification:
            raise Exception(f"Файл {self._filepath} не найден.")
        
        if not self._pattern_verification:
            raise Exception(f"Некорректное регулярное выражение: {self._pattern}")
        
        fileformat = os.path.splitext(self._filepath)[1]

        if fileformat == '.txt':
            return self._txt_regex()
        elif fileformat == '.odt':
            return self._odt_regex()
        elif fileformat == '.docx':
            return self._docx_regex()
        elif fileformat == '.pdf':
            return self._pdf_regex()
        elif fileformat == '.xlsx':
            return self._xlsx_regex()
        else:
            raise Exception(f"Формат файла {fileformat} не поддерживается.")