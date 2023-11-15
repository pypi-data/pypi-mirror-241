import contextlib
import uuid
from typing import Generator

from smbprotocol.connection import Connection
from smbprotocol.open import Open
from smbprotocol.session import Session
from smbprotocol.tree import TreeConnect


class Connector:
    def __init__(self, url: str, username: str = None, password: str = None, encrypt: bool = True):
        """
        Connect to SMB.

        :param url: The full SMB share, this should be `\\\\server\\share`.
        :param username: Optional username to use for authentication, required if Kerberos is not used.
        :param password: Optional password to use for authentication, required if Kerberos is not used.
        :param encrypt: Whether to use encryption or not, Must be set to False if using an older SMB Dialect.
        """
        self.url = url
        url_split = [e for e in url.split('\\') if e]
        assert len(url_split) >= 2, "URL should specify the server and share to connect to."

        self.server = url_split[0]
        self.share = url_split[1]
        self.username = username
        self.password = password
        self.encrypt = encrypt

    @contextlib.contextmanager
    def connect(self) -> Generator[Connection, None, None]:
        conn = Connection(uuid.uuid4(), self.server)

        try:
            conn.connect()
            yield conn
        finally:
            conn.disconnect()

    @contextlib.contextmanager
    def mount(self, conn: Connection) -> Generator[Session, None, None]:
        session = Session(conn, username=self.username, password=self.password, require_encryption=self.encrypt)
        try:
            session.connect()
            yield session
        finally:
            session.disconnect()

    @contextlib.contextmanager
    def tree(self, session: Session) -> Generator[TreeConnect, None, None]:
        tree = TreeConnect(session, r"\\%s\%s" % (self.server, self.share))

        try:
            tree.connect()

            yield tree
        finally:
            tree.disconnect()

    @contextlib.contextmanager
    def open(self, tree: TreeConnect, path: str) -> Generator[Open, None, None]:
        f = Open(tree, path)

        try:
            yield f
        finally:
            f.close()
