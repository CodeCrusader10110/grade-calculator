"""
TODO docstring
"""
import sys # temporary
from typing import Literal # may not need?
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
        self.__prompt_state: int = 0
        # 0 -> Enter total number of students
        # 1 -> Enter X score(s)
        # 2 -> Score calculation complete

        self.__label_defaults: dict[str, str] = {
            "prompt": "<b>Enter total number of students</b>",
            "validation": "",
            "student_count": "",
            "student_scores": "",
        }

        # Makes the initial score table invisible
        self.table_student_scores.setVisible(False)
        # self.table_student_scores.setRowCount(0)

        # Buttons
        self.button_enter.clicked.connect(self.button_enter_clicked)
        self.button_reset.clicked.connect(self.button_reset_clicked)
        self.button_quit.clicked.connect(self.close)

    # Widgets
    def label_prompt_write(self) -> None:
        """
        TODO docstring - unnecessary?
        """
        # self.label_prompt # something
        pass

    def button_enter_clicked(self) -> None:
        """
        TODO docstring
        """
        input = self.text_input.toPlainText()
        if self.__prompt_state == 0:
            # 0 -> Enter total number of students
            pass
        elif self.__prompt_state == 1:
            # 1 -> Enter X score(s)
            pass
        
        # Literally don't do anything if there's no active prompt at 2+

    def label_student_count_write(self) -> None:
        """
        TODO docstring - also maybe unnecessary
        """
        pass

    def label_student_scores_write(self) -> None:
        """
        TODO docstring - may not even use this but instead use the table
        """
        pass

    def table_student_scores_write(self, data: list[tuple]) -> None:
        """
        TODO docstring
        """

# table.setRowCount(n)          # Make space for n rows
# table.setColumnCount(n)       # Make space for n columns
# table.setHorizontalHeaderLabels(["Header1", "Header2"]) # top row text
# table.setItem(row, column, QTableWidgetItem("text")) # put something in a cell

        # set up headers?
        self.table_student_scores.setHorizontalHeaderLabels(
            ["Student", "Score", "Grade"]
        )

        # Enabling sorting must be done after setting up columns I guess?
        self.table_student_scores.setSortingEnabled(True)

        # write values?
        

    def button_reset_clicked(self) -> None:
        """
        TODO docstring
        """
        self.__prompt_state = 0

        self.label_prompt.setText(self.__label_defaults["prompt"])
        self.text_input.clear()
        self.label_input_validation.setText(self.__label_defaults["validation"])
        self.label_student_count.setText(self.__label_defaults["student_count"])
        self.label_student_scores.setText(
            self.__label_defaults["student_scores"]
        )

        self.table_student_scores.setRowCount(0)
        # Turn off sorting if it was enabled before, maybe bad practice?
        self.table_student_scores.setSortingEnabled(False)
        self.table_student_scores.setVisible(False)

    # Tools
    def input_students_validation(self) -> None:
        """
        TODO docstring
        """
        # self.label_input_validation.setText("something")
        pass

    def input_scores_validation(self) -> None:
        """
        TODO docstring
        """
        # self.label_input_validation.setText("something")
        pass

    # Grading logic
    def calc_grades():
        """
        This will probably need to receive data from the text input field and
        do a lot of the logic that exists in the old lab to determine grades,
        then return some string to be used in the output label.
        """
        pass
