from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConvertMilesKm(App):
    def build(self):
        Window.size = (200, 100)
        self.title = "Convert Miles Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate(self):
        print("Calculate")

    def up(self):
        print("Up")

    def down(self):
        print("Down")

ConvertMilesKm().run()
