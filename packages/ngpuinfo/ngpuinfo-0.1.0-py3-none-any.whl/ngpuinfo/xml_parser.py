import xml.dom.minidom as dom


class XmlParser(object):

    @classmethod
    def get_text(cls, node: dom.Node):
        if node.nodeType == dom.Node.TEXT_NODE:
            return node.data
        elif node.nodeType == dom.Node.ELEMENT_NODE:
            if len(node.childNodes) == 1:
                child = node.firstChild
                if child.nodeType == dom.Node.TEXT_NODE:
                    return child.data
        raise ValueError("Not Text Node.")
