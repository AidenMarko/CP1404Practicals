from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

class ConvertMilesKm(App):
    message = StringProperty()

    def build(self):
        Window.size = (1000, 500)
        self.title = "Convert Miles Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate(self):
        miles = self.root.ids.input_number.text
        if miles.isnumeric():
            km = int(self.root.ids.input_number.text) * 1.6
            self.message = str(km)
        else:
            miles = 0
            self.root.ids.input_number.text = str(miles)

    def handle_increment(self, increment):
        miles = self.root.ids.input_number.text
        if miles.isnumeric():
            miles = int(miles) + increment
            self.root.ids.input_number.text = str(miles)
        else:
            miles = 0
            self.root.ids.input_number.text = str(miles)


ConvertMilesKm().run()
