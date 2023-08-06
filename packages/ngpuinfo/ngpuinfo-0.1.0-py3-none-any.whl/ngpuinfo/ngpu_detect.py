import subprocess
import xml.dom.minidom as dom

from ngpuinfo.ngpu import NGPU
from ngpuinfo.xml_parser import XmlParser


def detect():
    ret = subprocess.run(["nvidia-smi", "-q", "-x"], stdout=subprocess.PIPE)
    if ret.returncode == 0:
        try:
            xml_info = ret.stdout
            doc = dom.parseString(xml_info)
            numbers = int(XmlParser.get_text(doc.getElementsByTagName("attached_gpus")[0]))
            cuda_version = XmlParser.get_text(doc.getElementsByTagName("cuda_version")[0])
            gpu_nodes = doc.getElementsByTagName("gpu")
            gpus = []
            for node in gpu_nodes:
                gpus.append(parse_gpu_xml_node(node))
            list.sort(gpus, key=lambda item: item.id)
            return {
                "numbers": numbers,
                "cuda_version": cuda_version,
                "gpus": gpus
            }
        except Exception as e:
            print(e)
            return None
    else:
        return None


def parse_gpu_xml_node(node):
    name = XmlParser.get_text(node.getElementsByTagName("product_name")[0])
    uuid = XmlParser.get_text(node.getElementsByTagName("uuid")[0])
    uuid = uuid.strip()
    ret = subprocess.run(["nvidia-smi", "--query-gpu=index", "--format=csv,noheader", "--id=%s" % uuid], stdout=subprocess.PIPE)
    if ret.returncode == 0:
        id = int(ret.stdout.decode())
        return NGPU(id, name)
    raise ValueError("")
