from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        if str(node.text).count(delimiter) % 2 != 0:
            raise Exception(f"Odd number of delimiters found in node: {node}")
        if str(node.text).count(delimiter) == 0:
            new_nodes.append(node)
            continue
        else:
            parts = str(node.text).split(delimiter)
            for i, part in enumerate(parts):
                if i % 2 == 0 and part != "":
                    new_nodes.append(TextNode(part, TextType.TEXT))
                elif part != "":
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes