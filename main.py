main.pyfrom kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window

Window.clearcolor = (0.05,0.05,0.05,1)

APP_NAME = "Salman Secure Gallery"
PASSWORD = "1234"

# -------- Splash Screen -------- #

class SplashScreen(Screen):

    def on_enter(self):
        Clock.schedule_once(self.goto_lock, 2)

    def goto_lock(self, dt):
        self.manager.current = "lock"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout()
        layout.add_widget(Label(
            text=APP_NAME,
            font_size=30,
            color=(1,1,1,1)
        ))

        self.add_widget(layout)

# -------- Lock Screen -------- #

class LockScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        self.label = Label(
            text="🔐 Enter Password",
            font_size=24
        )

        from kivy.uix.textinput import TextInput
        self.input = TextInput(password=True, multiline=False)

        from kivy.uix.button import Button
        btn = Button(text="Enter")

        btn.bind(on_press=self.check_password)

        layout.add_widget(self.label)
        layout.add_widget(self.input)
        layout.add_widget(btn)

        self.add_widget(layout)

    def check_password(self, instance):

        if self.input.text == PASSWORD:
            self.manager.current = "gallery"
        else:
            self.label.text = "❌ Wrong Password"

# -------- Gallery Dummy Screen -------- #

class GalleryScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout()
        layout.add_widget(Label(
            text="🎉 App Ready For APK Build",
            font_size=20
        ))

        self.add_widget(layout)

# -------- App -------- #

class SalmanSecureGallery(App):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(LockScreen(name="lock"))
        sm.add_widget(GalleryScreen(name="gallery"))

        return sm

SalmanSecureGallery().run()
