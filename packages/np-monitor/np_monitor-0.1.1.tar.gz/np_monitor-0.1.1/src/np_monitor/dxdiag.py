import re
import xml


def extract(tree: xml.etree.ElementTree, path: [str]) -> [any]:
    found = tree.find(path.pop(0))
    if len(path) < 1:
        return found
    
    return extract(found, path)



def extract_monitor_info(dxdiag_output: str):
    """Extracts monitor info from dxdiag output.
    
    Parameters
    ----------
    dxdiag_output : str
        Contents of dxdiag
    
    Returns
    -------
    MonitorInfo
        Tuple of manufacturer name, width, and height.
    """
    loaded = xml.etree.ElementTree.fromstring(
        dxdiag_output
    )
    display_devices = loaded.find("DisplayDevices")
    display_device = display_devices.find("DisplayDevice")
    current_mode = display_device.find("CurrentMode")
    monitor_model = display_device.find("MonitorModel")
    found = re.search(
        r"(\d*)\sx\s(\d*)\s\(",
        current_mode.text,
    )
    return MonitorInfo(
        monitor_model.text,
        int(found[1]),
        int(found[2]),
    )
    

def extract_sound_info(dxdiag_output: str):
    loaded = xml.etree.ElementTree.fromstring(
        dxdiag_output,
    )
    for child in loaded.iter():
        print(child)
        print(child.tag, child.attrib)


def extract_monitor_info(dxdiag_output: str):
    """Extracts monitor info from dxdiag output.
    
    Parameters
    ----------
    dxdiag_output : str
        Contents of dxdiag
    
    Returns
    -------
    MonitorInfo
        Tuple of manufacturer name, width, and height.
    """
    loaded = xml.etree.ElementTree.fromstring(
        dxdiag_output
    )
    display_devices = loaded.find("DisplayDevices")
    display_device = display_devices.find("DisplayDevice")
    current_mode = display_device.find("CurrentMode")
    monitor_model = display_device.find("MonitorModel")
    found = re.search(
        r"(\d*)\sx\s(\d*)\s\(",
        current_mode.text,
    )
    return MonitorInfo(
        monitor_model.text,
        int(found[1]),
        int(found[2]),
    )