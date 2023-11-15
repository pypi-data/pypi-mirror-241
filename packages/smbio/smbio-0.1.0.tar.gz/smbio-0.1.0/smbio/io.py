from smbprotocol.file_info import FileAttributes, FileInformationClass
from smbprotocol.open import Open, ImpersonationLevel, DirectoryAccessMask, ShareAccess, CreateDisposition, \
    CreateOptions

from smbio.connector import Connector
from smbio.file_entry import FileEntry


def write(file: Open, data: bytes) -> int:
    return file.write(data)


def glob(c: Connector, directory: Open, pattern: str = "*", recurse: bool = True) -> list[FileEntry]:
    # We create a compound request that does the following;
    #     1. Opens a handle to the directory
    #     2. Runs a query on the directory to list all the files
    #     3. Closes the handle of the directory
    # This is done in a compound request, so we send 1 packet instead of 3 at the expense of more complex code.
    query = (
        directory.create(
            ImpersonationLevel.Impersonation,
            DirectoryAccessMask.FILE_LIST_DIRECTORY,
            FileAttributes.FILE_ATTRIBUTE_DIRECTORY,
            ShareAccess.FILE_SHARE_READ | ShareAccess.FILE_SHARE_WRITE,
            CreateDisposition.FILE_OPEN,
            CreateOptions.FILE_DIRECTORY_FILE,
            send=False
        ),
        directory.query_directory(
            pattern,
            FileInformationClass.FILE_DIRECTORY_INFORMATION,
            send=False
        ),
        directory.close(False, send=False)
    )

    query_reqs = directory.tree_connect.session.connection.send_compound(
        [x[0] for x in query],
        directory.tree_connect.session.session_id,
        directory.tree_connect.tree_connect_id,
        related=True
    )

    # Process the result of the create and close request before parsing the files.
    query[0][1](query_reqs[0])
    query[2][1](query_reqs[2])

    # Parse the queried files and repeat if the entry is a directory and recurse=True. We ignore . and .. as they are
    # not directories inside the queried dir.
    entries = []
    ignore_entries = [".".encode('utf-16-le'), "..".encode('utf-16-le')]
    for file_entry in query[1][1](query_reqs[1]):
        if file_entry['file_name'].value in ignore_entries:
            continue

        fe = FileEntry(directory.file_name, file_entry)
        entries.append(fe)

        if fe.is_directory and recurse:
            dir_path = r"%s\%s" % (directory.file_name, fe.name) if directory.file_name != "" else fe.name
            with c.open(directory.tree_connect, dir_path) as d:
                entries += glob(c, d, pattern, recurse)

    return entries
