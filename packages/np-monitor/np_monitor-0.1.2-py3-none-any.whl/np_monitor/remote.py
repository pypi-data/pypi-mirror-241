import time
import fabric
import pathlib


def run_get_dxdiag(
    host: str,
    user: str,
    password: str,
    output_dir: pathlib.Path, 
) -> pathlib.Path:
    """
    Notes
    -----
    - Assumes a windows host
    """
    with fabric.Connection(
        host=host,
        user=user,
        connect_kwargs={
            "password": password,
        },
    ) as con:
        dxdiag_filename = f"{int(time.time())}.xml"
        dxdiag_cmd = f"dxdiag -x {dxdiag_filename}"
        result = con.run(dxdiag_cmd, hide=True, warn=False)
        if not result.ok:
            raise Exception(
                "Unexpected result from remote command: %s" % dxdiag_cmd)
        
        output_filepath = (output_dir / dxdiag_filename).as_posix()
        con.get(
            dxdiag_filename,
            local=output_filepath,
        )
        return output_filepath