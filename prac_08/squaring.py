from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ Build the Kivy app from the kv file """
        Window.size = (600, 200)  # Set a larger window size for the layout
        self.title = "Square Number 2"  # Set the app title
        self.root = Builder.load_file('squaring.kv')  # Load the kv layout file
        return self.root

    def handle_calculate(self, value):
        """ Handle calculation and update the result in the label """
        try:
            # Convert input value to float and calculate the square
            result = float(value) ** 2
            # Update the result label with the squared number
            self.root.ids.output_label.text = str(result)
        except ValueError:
            # Handle invalid input gracefully (e.g., non-numeric input)
            self.root.ids.output_label.text = "Invalid input"

# Run the app
if __name__ == "__main__":
    SquareNumberApp().run()