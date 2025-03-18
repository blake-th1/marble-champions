#MyNameIs(what)MyNameIs(Who)myNameIsChikaChikaSlimShady
from kivy.uix.behaviors import TouchRippleBehavior
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDRectangleFlatButton

# used for most MD apps
from kivymd.app import MDApp
#Used to reference the widgets in .kv and keep the positions
from kivy.uix.floatlayout import FloatLayout
#Used for changing screens
from kivy.uix.screenmanager import ScreenManager, Screen
#used to set screen size
from kivy.core.window import Window

#example Android screen size
Window.size = (412, 896)


#class for each screen and its' canvas
class HomeScreen(Screen):
    pass
    class HomeScreenCanvas(FloatLayout):
        pass

class LobbyScreen(Screen):
    pass
    class LobbyScreenCanvas(FloatLayout):
        pass

class FightScreen(Screen):
    pass
    class FightScreenCanvas(FloatLayout):
        pass

class MarbleChampionsApp(MDApp):
    def build(self):
        #Light Mode
        #self.theme_cls.primary_palette = "Blue"
        #self.theme_cls.primary_hue = "A700"
        #self.theme_cls.theme_style = "Light"

        #Dark Mode
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.theme_style = "Dark"

        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(LobbyScreen(name='lobby'))
        self.sm.add_widget(FightScreen(name='fight'))
        return self.sm

    def go_home(self):
        self.sm.current = 'home'

if __name__ == '__main__':
    MarbleChampionsApp().run()