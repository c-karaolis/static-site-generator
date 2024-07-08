from textnode import TextNode


def main():
    text_node1 = TextNode("text1", "type1", "url1")
    text_node2 = TextNode("text2", "type2", "url2")
    text_node3 = TextNode("text1", "type1", "url1")
    print(text_node1 == text_node2)
    print(text_node1 == text_node3)
    print(text_node1)
    print(text_node2)
    print(text_node3)
    

main()