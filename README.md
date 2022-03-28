# tg-chatbot-template
Template of telegram chat bot based on the pyTelegramBotAPI module

## Purpose
This is a template for telegram chat bots which creates hierarchical menu from plain text file (menu.txt).

## Structure of menu.txt file
Each menu item is separated by a line starting with '=' symbol. <br>
The first line of each menu item must contain a hierarchical level of this menu item and a name of menu item. The name will be displayed as a button of chat bot menu (ReplyKeyboardMarkup, according to the official Telegram Bot API). The level must consist of digits and periods: 1. is a root level, 1.1 and 1.2 are sub-levels of root level 1., 1.2.1 is a sub-level of level 1.2, and so on.<br>
The body of each menu item must be enclosed in curly brackets. This is a text which will be shown when this menu item is selected by user. The body may be multiple lines.
