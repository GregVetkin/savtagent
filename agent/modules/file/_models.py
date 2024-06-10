from dataclasses import dataclass


@dataclass
class FileInfo:
    path:       str     = ""
    name:       str     = ""
    hash:       str     = ""
    size:       int     = 0
    uid:        int     = 0
    gid:        int     = 0
    atime:      float   = 0
    ctime:      float   = 0
    mtime:      float   = 0

