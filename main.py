from datetime import datetime
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

class ScreenMain(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (.1, .1, .9, 1)
        boxlayout = BoxLayout(orientation="vertical", spacing=20, padding=[10])
        label = Label(text='МЕНЮ',
                      font_size=40,
                      font_name='Montserrat-Black.ttf',
                      color=[0, 2, 3, 1],
                      size_hint=(.5, .25),
                      pos_hint={'center_x': .5, 'center_y': .5})
        boxlayout.add_widget(label)
        button_new_event = Button(
            text="Добавить событие",
            font_name='Montserrat-SemiBold.ttf',
            background_color=[0, 1.5, 3, 1],
            size_hint=[0.3, 0.1],
            pos_hint={'center_x': .5, 'center_y': .5},
            on_press=self._on_press_button_new_event,
        )
        boxlayout.add_widget(button_new_event)
        button_my_events = Button(
            text="Мои события",
            font_name='Montserrat-SemiBold.ttf',
            background_color=[0, 1.5, 3, 1],
            size_hint=[0.3, 0.1],
            pos_hint={'center_x': .5, 'center_y': .5},
            on_press=self._on_press_button_my_events,
        )
        boxlayout.add_widget(button_my_events)
        img = Image(source='Logo2.png',
                    size_hint=(1, .25),
                    pos_hint={'center_x': .5, 'center_y': .5})
        boxlayout.add_widget(img)
        self.add_widget(boxlayout)
    def _on_press_button_new_event(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'add_event'

    def _on_press_button_my_events(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'my_events'

class AddEvent(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])
        boxlayout1 = BoxLayout(orientation="horizontal", spacing=5, padding=[10])
        label1 = Label(text='Название события:',
                      font_size=16,
                      font_name='Montserrat-Regular.ttf',
                      color=[0, 2, 3, 1],
                      size_hint=(.5, .25),
                      pos_hint={'center_x': .5, 'center_y': .5})
        boxlayout1.add_widget(label1)
        self.event = TextInput(
            multiline=False, halign="right", font_size=16, size_hint=(.5, .15),pos_hint={'center_x': .5, 'center_y': .5}
        )
        boxlayout1.add_widget(self.event)
        boxlayout.add_widget(boxlayout1)
        boxlayout2 = BoxLayout(orientation="horizontal", spacing=5, padding=[10])
        label2 = Label(text='Дата события:',
                       font_size=16,
                       font_name='Montserrat-Regular.ttf',
                       color=[0, 2, 3, 1],
                       size_hint=(.5, .25),
                       pos_hint={'center_x': .5, 'center_y': .5})
        boxlayout2.add_widget(label2)
        self.date = TextInput(text="год.месяц.день",
            multiline=False, halign="right", font_size=16, size_hint=(.5, .15),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        boxlayout2.add_widget(self.date)
        boxlayout.add_widget(boxlayout2)
        button_new_pasword = Button(
            text="Добавить событие",
            font_name='Montserrat-SemiBold.ttf',
            background_color=[0, 1.5, 3, 1],
            size_hint=[0.3, 0.1],
            pos_hint={'center_x': .5, 'center_y': .5},
            on_press=self._on_press_button_add_event,
        )
        boxlayout.add_widget(button_new_pasword)
        button_back = Button(
            text="Назад в меню",
            font_name='Montserrat-SemiBold.ttf',
            background_color=[0, 1.5, 3, 1],
            size_hint=[0.3, 0.1],
            pos_hint={'center_x': .5, 'center_y': .5},
            on_press=self._on_press_button_back,
        )
        boxlayout.add_widget(button_back)
        self.add_widget(boxlayout)
    def _on_press_button_back(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_screen'

    def _on_press_button_add_event(self, *args):
        check = False
        try:
            if self.date.text[4] == '.' and self.date.text[7] == '.' and int(self.date.text[:4])>=int(str(datetime.date(datetime.today()))[:4])\
                    and (int(self.date.text[5:7])>=1 and int(self.date.text[5:7])<=12):
                if (int(self.date.text[5:7])==1 or int(self.date.text[5:7])==3 or int(self.date.text[5:7])==5 or int(self.date.text[5:7])==7 or int(self.date.text[5:7])==8 or int(self.date.text[5:7])==10 or int(self.date.text[5:7])==12)\
                        and (int(self.date.text[8:])>=1 and int(self.date.text[8:])<=31):
                    check = True
                elif int(self.date.text[5:7])==2:
                    if int(self.date.text[:4])%4==0 and (int(self.date.text[8:])>=1 and int(self.date.text[8:])<=29):
                        check = True
                    elif int(self.date.text[8:])>=1 and int(self.date.text[8:])<=28:
                        check = True
                elif (int(self.date.text[5:7]) == 4 or int(self.date.text[5:7]) == 6 or int(self.date.text[5:7]) == 9
                    or int(self.date.text[5:7]) == 11) and (int(self.date.text[8:]) >= 1 and int(self.date.text[8:]) <= 30):
                    check = True
                else:
                    print(self.date.text[5:7])
                if check==True:
                    ev = datetime(int(self.date.text[:4]), int(self.date.text[5:7]), int(self.date.text[8:]))
                    my_file = open("events.txt", "a", encoding='utf-8')
                    my_file.write(self.event.text + ", " + str(ev) + '\n')
                    my_file.close()
                else:
                    print('неправильный чек')
            else:
                self.date.text = 'Вы плохо знаете даты'
        except:
            self.date.text = 'Неправильно введен формат (гггг.мм.дд)'



class MyEvents(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])
        self.event = TextInput(
            multiline=False, halign="right", font_size=16, size_hint=(.8, .9),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        inFile = open('events.txt', 'r', encoding='utf-8').readlines()
        events = []
        for line in inFile:
            event = line.split(', ')[0], line.split(', ')[1]
            events.append(event)
        for i in range(0, len(events)):
            now = datetime.today()
            ev = datetime(int((events[i][1])[:4]), int((events[i][1])[5:7]), int((events[i][1])[8:10]))
            d = ev - now
            text = self.event.text
            self.event.text = text + '\n' + events[i][0] + ': {} дней'.format(d.days)
        boxlayout.add_widget(self.event)
        button_update = Button(
            text="Обновить",
            font_name='Montserrat-SemiBold.ttf',
            background_color=[0, 1.5, 3, 1],
            size_hint=[0.3, 0.1],
            pos_hint={'center_x': .5, 'center_y': .5},
            on_press=self._on_press_button_update,
        )
        boxlayout.add_widget(button_update)
        button_back = Button(
            text="Назад в меню",
            font_name='Montserrat-SemiBold.ttf',
            background_color=[0, 1.5, 3, 1],
            size_hint=[0.3, 0.1],
            pos_hint={'center_x': .5, 'center_y': .5},
            on_press=self._on_press_button_back,
        )
        boxlayout.add_widget(button_back)
        self.add_widget(boxlayout)
    def _on_press_button_back(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_screen'
    def _on_press_button_update(self, *args):
        self.manager.transition.direction = 'right'
        self.event.text=""
        inFile = open('events.txt', 'r', encoding='utf-8').readlines()
        events = []
        for line in inFile:
            event = line.split(', ')[0], line.split(', ')[1]
            events.append(event)
        for i in range(0, len(events)):
            now = datetime.today()
            ev = datetime(int((events[i][1])[:4]), int((events[i][1])[5:7]), int((events[i][1])[8:10]))
            d = ev - now
            text = self.event.text
            self.event.text = text + '\n' + events[i][0] + ': {} дней'.format(d.days)

class HowManyDaysToApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenMain(name='main_screen'))
        sm.add_widget(AddEvent(name='add_event'))
        sm.add_widget(MyEvents(name='my_events'))
        return sm
if __name__ == "__main__":
    HowManyDaysToApp().run()