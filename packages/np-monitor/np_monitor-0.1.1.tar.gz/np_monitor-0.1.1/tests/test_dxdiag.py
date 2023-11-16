import pathlib

from np_monitor import dxdiag


# def test_parse_dxdiag_output():
#     dxdiag_output = pathlib.Path("tests/dxdiag.xml").read_text()
#     assert dxdiag.bur(
#         dxdiag_output
#     ) == types.MonitorInfo(
#         "Dell U2412M (Digital)",
#         1920,
#         1200,
#     )