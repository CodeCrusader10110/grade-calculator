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
pyuic6 -x <filename>.ui -o <filename>.py
```

```
pyinstaller --onefile -w --icon=icon.png main.py
```