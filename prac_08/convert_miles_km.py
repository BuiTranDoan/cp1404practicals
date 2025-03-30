from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_CONVERSION = 1.60934


class MilesToKmApp(App):
    result = StringProperty("0.0 km")  # This will bind to the result label

    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Miles to Kilometers Converter"
        return Builder.load_file('convert_miles_km.kv')

    def handle_conversion(self, miles):
        """ Convert miles to kilometers and update the result label """
        try:
            miles = float(miles)
            km = miles * MILES_TO_KM_CONVERSION
            self.result = f"{km:.2f} km"
        except ValueError:
            self.result = "0.0 km"  # Handle invalid input

    def handle_increment(self, increment):
        """ Increment or decrement the miles value by 1 """
        try:
            miles = float(self.root.ids.miles_input.text)
        except ValueError:
            miles = 0
        miles += increment
        self.root.ids.miles_input.text = str(miles)
        self.handle_conversion(miles)


if __name__ == '__main__':
    MilesToKmApp().run()