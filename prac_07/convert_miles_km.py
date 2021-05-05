from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConvertMilesKm(App):
    def build(self):
        Window.size = (1000, 500)
        self.title = "Convert Miles Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate(self):
        print("Calculate")

    def handle_increment(self, increment):
        miles = int(self.root.ids.input_number.text)
        miles = miles + increment
        self.root.ids.input_number.text = str(miles)


ConvertMilesKm().run()
