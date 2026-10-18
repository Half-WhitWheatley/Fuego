import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextType, TextNode


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        old_nodes = [
            TextNode("Hello, world!", TextType.TEXT),
            TextNode("This is a **bold** text.", TextType.TEXT)
        ]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(new_nodes, [
            TextNode("Hello, world!", TextType.TEXT),
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT)
        ])
        
    def test_split_nodes_delimiter_no_delimiter(self):
        old_nodes = [
            TextNode("Hello, world!", TextType.TEXT),
            TextNode("This is a bold text.", TextType.TEXT)
        ]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(new_nodes, old_nodes)
        
    def test_split_nodes_delimiter_odd_delimiter(self):
        old_nodes = [
            TextNode("Hello, world!", TextType.TEXT),
            TextNode("This is a **bold text.", TextType.TEXT)
        ]
        delimiter = "**"
        text_type = TextType.BOLD
        with self.assertRaises(Exception):
            split_nodes_delimiter(old_nodes, delimiter, text_type)
            
    def test_split_nodes_delimiter_italics(self):
        old_nodes = [
            TextNode("Hello, world!", TextType.TEXT),
            TextNode("This is a _italic_ text.", TextType.TEXT)
        ]
        delimiter = "_"
        text_type = TextType.ITALIC
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(new_nodes, [
            TextNode("Hello, world!", TextType.TEXT),
            TextNode("This is a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT)
        ])
    
    def test_split_nodes_delimiter_multiple_delimiters(self):
        old_nodes = [
            TextNode("Hello, **world**! This is a **bold** text.", TextType.TEXT)
        ]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(new_nodes, [
            TextNode("Hello, ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode("! This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT)
        ])
        
    def test_split_nodes_delimiter_empty_text(self):
        old_nodes = [
            TextNode("", TextType.TEXT)
        ]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(new_nodes, old_nodes)
        
    def test_split_nodes_delimiter_code(self):
        old_nodes = [
            TextNode("This is a `code` snippet.", TextType.TEXT)
        ]
        delimiter = "`"
        text_type = TextType.CODE
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(new_nodes, [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" snippet.", TextType.TEXT)
        ])
        
    def test_split_nodes_delimiter_start_and_end(self):
        old_nodes = [
            TextNode("**bold** text.", TextType.TEXT)
        ]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(new_nodes, [
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT)
        ])