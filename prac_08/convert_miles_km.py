from kivy.app import App
from kivy.lang import Builder
MILES_TO_KM_CONVERSION = 1.60934


class MilesToKmApp(App):
    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Miles to Kilometers Converter"
        return Builder.load_file('convert_miles_km.kv')

    def handle_conversion(self):
        """ Convert miles to kilometers and update the result label """
        convert_miles = self.get_validated_miles()
        miles_to_km = convert_miles * MILES_TO_KM_CONVERSION
        self.root.ids.output_label.text = str(miles_to_km) # Handle invalid input

    def handle_increment(self, change):
        """ Increment or decrement the miles value by 1 """
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_conversion()

    def get_validated_miles(self):
        """
        get text input from text entry widget, convert to float
        :return: 0 if error, float version of text if valid
        """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

MilesToKmApp().run()