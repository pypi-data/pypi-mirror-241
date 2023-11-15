# smbio
SMB protocol wrapper for python

## Installation

```bash
pip install smbio
```

## Usage

```python
import smbio

connector = smbio.Connector(
    url=r"\\localhost\Share",
    username="Username",
    password="StrongPa$$w0rd"
)

with (
    connector.connect() as conn,
    connector.mount(conn) as session,
    connector.tree(session) as tree,
    connector.open(tree, r"Directory\Subdirectory") as directory
):
    files = smbio.glob(connector, directory, recurse=False)
    for out in files:
        if out.is_directory:
            continue
        
        with (
            open(smbio.Path(out.path), mode="rb") as inp_file,
            connector.open(tree, out.path) as out_file
        ):
            out_file.write(inp_file.read())
```