# grade-calculator

An improved version of Lab 2 that follows better practices and has an interactable GUI

## MVC structure reminder
* **Model** - Creating and customizing your application window (main.py)
* **View** - Contains code for the user interface (gui.py)
* **Controller** - Contains logic code that makes your application work (logic.py)

## other reminders
```
pip freeze > requirements.txt
```

```
pyuic6 -x gui.ui -o gui.py 
```

```
pyinstaller --onefile -w --icon=icon.png main.py
```

Official PyQt6 docs: https://www.riverbankcomputing.com/static/Docs/PyQt6/designer.html