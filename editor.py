from ui.uimanager import UIManager
from text import Text

class TextEditor(object):
    """
    Editor main class. Implements basic functions of text editor.
    """

    def __init__(self, filename = None, text = None):
        self.TE_ui = UIManager('tk')
        self.TE_content = Text()

if __name__ == "__main__":
    t = TextEditor()