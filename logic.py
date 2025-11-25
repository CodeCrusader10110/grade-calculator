"""
TODO docstring
"""
from typing import Literal
from PyQt6.QtWidgets import QDialog
from gui import Ui_Dialog

# HTML codes for adjusting text output - for input validation failures, or
# otherwise making text in Labels pretty
# Bold:                     <b>text</b>
# Underline:                <u>text</u>
# Color:                    <span style="color:#ff0000">text</span>
# Bold, color:              <b><span style="color:#00ff00">text</span></b>
# Bold, underline, color:   <b><u><span style="color:#ff3333">text</span></u></b>

class GuiLogic(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        """
        TODO docstring
        """
        super().__init__(parent) # creates an empty QDialog object (a widget)
        self.setupUi(self) # fills above object with defined widgets in gui.py

        # Tracks where the program is at to determine how text input should be
        # validated and where it should be sent to for the various questions, or
        # for when the program is complete to tell user to reset
        self.__state: int = 0

        # Maybe good?
        # self.__defaults: dict = {
        #     'label_one': self.label_one.txt()
        # }


        # Every method needs to have a connection with the corresponding widget
        self.button_enter.clicked.connect(self.button_enter_clicked)

        # self.button_reset.clicked.connect(self.button_reset_clicked)

        # Quit button doesn't require entire method
        self.button_quit.clicked.connect(self.close)

    # def _capture_defaults(self) -> dict:
    #     """
    #     not sure if this will be the way we end up saving defaults for reset
    #     button but we'll see
    #     """
    #     # return {
    #     #     "label_one" : self.label_one.text(),
    #     #     "label_two" : self.label_two.text(),
    #     #     # etc
    #     # }
    #     pass

    # Widget logic
    def label_prompt_update(self) -> None:
        """
        TODO docstring
        """
        pass

    def button_enter_clicked(
            self,
            logic_state = Literal['student_count', 'scores']
        ) -> None:
        """
        TODO docstring
        """
        self.label_text_validation.setText("Enter button was clicked")

    def label_student_count_update(self) -> None:
        """
        TODO docstring
        """
        pass

    def label_student_scores_update(self) -> None:
        """
        TODO docstring
        """
        pass

    def button_reset_clicked(self) -> None:
        """
        TODO docstring
        """
        pass

    # Tools
    def input_students_validation(self) -> None:
        """
        TODO docstring
        """
        pass

    def input_scores_validation(self) -> None:
        """
        TODO docstring
        """
        pass

    # Grading logic
    def calc_grades():
        """
        This will probably need to receive data from the text input field and
        do a lot of the logic that exists in the old lab to determine grades,
        then return some string to be used in the output label.
        """
        pass