# tg-chatbot-template

Template of telegram chat bot based on the pyTelegramBotAPI module

## Purpose

This is a template for telegram chat bots which creates hierarchical menu from plain text file (menu.txt).

## How to use
1. Just edit the `menu.txt` file according to the rules described below in the _Structure of the_ `menu.txt` _file Section_ in order to desribe your chatbot's multi-level menu. If your text file with a description of your chatbot's menu has another name (not `menu.txt`), you need to correct `MENU_FN` variable in `main.py`.
2. Assign your telegram chatbot's token to `TOKEN` variable in `main.py`. The token you can obtain via BotFather bot.

## Structure of the menu.txt file

Each menu item is separated by a line starting with '=' symbol. <br>
The first line of each menu item must contain a hierarchical level of this menu item and a name of menu item. The name will be displayed as a button of chat bot menu (ReplyKeyboardMarkup, according to the official Telegram Bot API). The level must consist of digits and periods: 1. is a root level, 1.1 and 1.2 are sub-levels of root level 1., 1.2.1 is a sub-level of level 1.2, and so on.<br>
The body of each menu item must be enclosed in curly brackets. This is a text which will be shown when this menu item is selected by user. The body may be multiple lines.

## Credit to developers of the module(s) used in this script

This script has been written using [`pyTelegramBotApi` module](https://github.com/eternnoir/pyTelegramBotAPI) by [eternnoir](https://github.com/eternnoir).
