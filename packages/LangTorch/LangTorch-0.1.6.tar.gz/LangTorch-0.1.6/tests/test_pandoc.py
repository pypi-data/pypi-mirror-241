import logging
import sys


sys.path.append("../src")
from langtorch import Text, TextTensor, TextModule
from langtorch import Session
import unittest
import numpy as np
import torch
import json
from typing import Any, List, Tuple, Union
import pypandoc

class TestMarkupLanguages(unittest.TestCase):

    def setUp(self):
        # This setup could include common initializations for all tests
        pass

    def test_markdown(self):
        input_text = "# My Markdown Heading\n\nSome paragraph texts.\n\n- numbered list item 1\n- numbered list item 2\n- numbered list item 3"
        expected_output = input_text
        output = pypandoc.convert_text(input_text, 'json', format='md')
        text_obj = Text.from_pandoc_json(output)
        assert output is None, str(output)+str(text_obj.items())
        self.assertEqual(text_obj.keys(), ['header_h1', 'p'])

    def test_html(self):
        input_text = "<h1>My HTML Heading</h1><p>Some paragraph texts.</p>"
        expected_output = input_text
        output = pypandoc.convert_text(input_text, 'json', format='html')
        text_obj = Text.from_pandoc_json(output)
        assert output is None, str(output)+str(text_obj.items())
        self.assertEqual(text_obj.keys(), ['header_h1', 'p'])
        self.assertEqual(str(text_obj), expected_output)

    # Add more tests for each markup language...

    def test_latex(self):
        input_text = "\\section{My LaTeX Heading}\n\nSome paragraph texts."
        expected_output = input_text
        output = pypandoc.convert_text(input_text, 'json', format='tex')
        text_obj = Text.from_pandoc_json(output)
        self.assertEqual(str(text_obj), expected_output)

    # ...and so on for other markup languages.




if __name__ == '__main__':
    unittest.main()
