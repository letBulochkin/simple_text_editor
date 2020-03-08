#importlib.import_module()

from importlib import import_module
#import backends.backend_tk

class UIManager(object):
    """
    Class designed to handle communication between TextEditor backend and UI-framework.
    """

    def __init__(self, uisystem):
        self.__ui_backends_available__ = ['tk']

        if uisystem in self.__ui_backends_available__:
            ui = import_module('ui.backends.backend_' + uisystem)
            print(type(ui))
            app = ui.SampleApp()
            app.mainloop()

        print(uisystem)