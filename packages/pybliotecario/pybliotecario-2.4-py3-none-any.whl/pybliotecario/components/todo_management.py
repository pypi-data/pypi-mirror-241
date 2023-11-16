"""
    Component to manage markdown-based todo lists
    The notes are referenced in the config file as

    [TODO]
    note_name = "/path/to/note.md"
    another_note = "/another/path/to/note.md"
"""

import logging

from pybliotecario.components.component_core import Component

log = logging.getLogger(__name__)


def _add_to_note(note, information):
    pass


class TodoManagement(Component):
    """
    Opens up a markdown note
    """

    section_name = "TODO"
    help_text = """ > TODO module
    /todo_list: list all todo lists
    /todo @todo_name <text>: append items to a list
    If no @todo_name is used, default to first or main list"""

    def __init__(self, telegram_object, configuration=None, **kwargs):
        super().__init__(telegram_object, configuration=configuration, **kwargs)
        self._todo_notes = dict(self.read_config_section())
        self.blocked = False

    def _select_note(self, note_selection_raw):
        """Select a note, if no note is selected, look for a main note"""
        if note_selection_raw.startswith("@"):
            note_selection = note_selection_raw.split(" ", 1)[0][1:]
        else:
            note_selection = None
        if note_selection is not None:
            return self._todo_notes.get(note_selection)
        if "main" in self._todo_notes:
            return self._todo_notes["main"]
        return list(self._todo_notes.values())[0]

    def telegram_message(self, msg):
        if not self.check_identity(msg) and not self._allow_everyone:
            self.blocked = True
            self.send_msg("You are not allowed to see or read TODOs")
        if not self.blocked and not self._todo_notes:
            self.send_msg("There are no TODO notes")
            self.blocked = True

        if self.blocked:
            return

        if msg.command == "todo_list":
            self.send_msg(" ".join(self._todo_notes.values()))
        elif msg.command == "todo":
            target_note = self._select_note(target_note_raw)


if __name__ == "__main__":
    import configparser
    from pathlib import Path
    import tempfile

    from pybliotecario.backend import TestUtil
    from pybliotecario.pybliotecario import logger_setup

    tmpdir = Path(tempfile.mkdtemp())
    tmptxt = tmpdir / "text.txt"

    config = configparser.ConfigParser()
    config["DEFAULT"] = {"main_folder": tmpdir, "token": "AAAaaa123", "chat_id": 453}
    config["TODO"] = {
        "test": "/home/jumax9/Documents/obsidian_notes/cajon_de_sastre/To Organizar.md"
    }
    logger_setup(tmpdir / "log.txt", debug=True)

    log.info("Testing the github component")
    test_util = TestUtil(communication_file=tmptxt)
#     args = ["--check_github_issues", "NNPDF/nnpdf"]
#     main(cmdline_arg=args, tele_api=test_util, config=config)
#     messages = tmptxt.read_text()
#     print("Results: ")
#     print(messages)
