import telebot
from errors import *

# CONSTANTS
DIGITS_AND_DOT = set([str(digit) for digit in range(10)]) | set('.')
MENU_FN = "menu_.txt"  # menu filename
TOKEN = "insert your token from BotFather bot"
DEFAULT_TEXT = "your query is processing..."

menu = dict()
bot = telebot.TeleBot(TOKEN)


class MenuItem():
    @classmethod
    def make_menu_item(cls, header: str, body: str = ""):
    '''This class method is a constructor of MenuItem instace from two
lines of text: header must contain a hierarchical level of the menu item 
and the menu item's name devided by a space, and body may contain a text
which will be shown if this menu item is selected.
    '''		
    body: str = body.strip("{}")
    delim: int = header.index(" ")
    lvl, name = header[:delim], header[delim + 1:].strip()
    return cls(level=lvl, name=name, text=body)

    def __init__(self, level: str, name: str, children=None, text=''):
        global menu
        if set(level).issubset(DIGITS_AND_DOT): # menu item level must contain digits and periods only
            self.level = level
        else:
            raise MenuEntryLevelError(str(level))
            self.level = None
        self.name = name
        if not children:
            self.children = []
        else:
            self.children = children
        if text == "":
            text = DEFAULT_TEXT
        self.text = text
        self.keyboard = None
        if str(self.level) in menu.keys():
            raise DuplicateMenuEntryError(str(self.level))
        menu[self.level] = self # each menu item adds itself to the global dictionary 'menu'
        # if menu item is a child of another menu item, it will be appended to children list:
        if self.level:
            levels = self.level.split(".")
            if levels[-1] == "":
                levels.pop()
            if len(levels) > 1:
                levels.pop()
                superior: str = ".".join(levels) + "."
                menu[superior].children.append(self) 
		
    def make_keyboard(self):
        if self.children:
            keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                                         resize_keyboard=True, 
                                                         row_width=1,)
            buttons: list = list(map(telebot.types.KeyboardButton,
                                     [child.name for child in self.children]))
            keyboard.add(*buttons)
            self.keyboard = keyboard
        else:
            self.keyboard = None # If a menu item has no children a keyboard is not necessary

    def show_submenu(self, message):
        if self.keyboard:
            bot.send_message(message.chat.id, self.text, 
                             reply_markup=self.keyboard)
            bot.register_next_step_handler(message, self.handler)
        else:
            markup = telebot.types.ReplyKeyboardRemove(selective=False)
            bot.send_message(message.chat.id, self.text, reply_markup=markup, parse_mode="html")

    def handler(self, message):
        if self.keyboard:
            selected_menu_item =self.children[[child.name.strip()
                                               for child in self.children].index(message.text)]
            selected_menu_item.show_submenu(message)


def read_menu_file(menu_filename=MENU_FN):
    with open(menu_filename, "r", encoding="utf8") as f:
        header = ""
        body = ""
        lines = []
        for line in f:
            if line.startswith("="):
                header = lines[0]
                body = "".join(lines[1:])
                l: int = body.find("{")
                r: int = body.rfind("}")
                body = body[l:r + 1]
                menu = MenuItem.make_menu_item(header, body)
                header = ""
                body = ""
                lines = []
            else:
                lines.append(line)

@bot.message_handler(commands = ['start'])
def root_menu_entry(message):
    menu_entry = menu['1.']
    menu_entry.show_submenu(message)


if __name__ == '__main__':
    read_menu_file()
    for __, entry in menu.items():
        entry.make_keyboard()
    bot.infinity_polling()
