import unittest
from console import HBNBCommand


class TestHNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command intepreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)
