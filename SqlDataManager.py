import os

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.button.button import MDFillRoundFlatIconButton
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast

from SqlDataManagement import CreateConnection
import ConfigManager as cm
import constants as c

KV = '''
<ContentNavigationDrawer>

    MDList:

        OneLineListItem:
            text: "Screen 1"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 1"

        OneLineListItem:
            text: "Screen 2"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 2"


MDScreen:

    MDTopAppBar:
        pos_hint: {"top": 1}
        elevation: 4
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"
                
                MDFillRoundFlatIconButton:
                    icon: "android"
                    text: "Add to database"
                    pos_hint: {'right': 1, 'bottom': 1}
                    on_release: app.CreateConnection(app.database)

                MDRoundFlatIconButton:
                    text: "Open manager"
                    icon: "folder"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release: app.file_manager_open()

            MDScreen:
                name: "scr 2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Example(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
        )

    def build(self):
        theme_style = cm.getConfigObject(c.CONFIG_PATH, "theme")
        color_style = cm.getConfigObject(c.CONFIG_PATH, "color")
        self.theme_cls.primary_palette = color_style
        self.theme_cls.theme_style = theme_style

        return Builder.load_string(KV)
    
    def file_manager_open(self):
        self.file_manager.show(os.path.expanduser("~"))
        self.manager_open = True

    def select_path(self, path: str):
        '''
        It will be called when you click on the file name
        or the catalog selection button.

        :param path: path to the selected directory or file;
        '''
        
        jsonObject = cm.getConfig(c.CONFIG_PATH)
        cm.modifyConfig(c.CONFIG_PATH, jsonObject, "sqlPath", path)

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def CreateConnection(self, db_file):        
        CreateConnection(db_file)

Example().run()
