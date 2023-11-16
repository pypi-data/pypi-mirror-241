import os
import pytest
import pathlib
import dotenv

dotenv.load_dotenv()

from np_monitor import remote


USERNAME = os.environ.get("NP_MONITOR_USERNAME")
PASSWORD = os.environ.get("NP_MONITOR_PASSWORD")
HOSTNAME = os.environ.get("NP_MONITOR_HOSTNAME")


@pytest.mark.internal
@pytest.mark.skipif(
    USERNAME is None,
    PASSWORD is None,
    HOSTNAME is None,
    reason="Required environment variables not present.",
)
def test_run_get_dxdiag(tmpdir):
    output_dir = pathlib.Path(tmpdir)
    remote.run_get_dxdiag(
        HOSTNAME,
        USERNAME,
        PASSWORD,
        output_dir,
    )

    xml_files = output_dir.glob("*.xml")
    assert len(list(xml_files)) == 1