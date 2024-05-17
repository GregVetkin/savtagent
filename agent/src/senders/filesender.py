from .basesender    import DataSender
from ..data         import FileInfo


class FileInfoSender(DataSender):
    def send(fileinfo: FileInfo, receiver):
        receiver.save_fileinfo_data(fileinfo)