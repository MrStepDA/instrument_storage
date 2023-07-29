from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder


kv = '''
MDTextField:
    size_hint_x: .7
    hint_text: 'Введите номер продукта (и нажмите Enter)'
    pos_hint: {"center_x": .4, "center_y": .9}
'''


class Example(MDApp):
    def build(self):
        return Builder.load_string(kv)


class Test(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return (
            MDScreen(
                MDBottomNavigation(
                    MDBottomNavigationItem(
                        MDLabel(
                            text='Загрузить',
                            halign='center',
                        ),
                        name='screen 1',
                        text='Загрузить',
                        icon='download',
                    ),
                    MDBottomNavigationItem(
                        MDLabel(
                            text='Выгрузить',
                            halign='center',
                        ),
                        name='screen 2',
                        text='Выгрузить',
                        icon='upload',
                    ),
                    MDBottomNavigationItem(
                        name='screen 3',
                        text='Информация',
                        icon='information-outline',
                    ),
                    selected_color_background="orange",
                    text_color_active="lightgrey",
                )
            )
        )


Test().run()
