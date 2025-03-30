from kivy.app import App
from kivy.lang import Builder

# Load the Kv file
KV = Builder.load_file("box_layout.kv")

class BoxLayoutDemo(App):
    def build(self):
        return KV  # Return the loaded Kv layout

    def handle_greet(self):
        """Update the label text with a greeting."""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        """Clear the input field and reset the label."""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''

if __name__ == '__main__':
    BoxLayoutDemo().run()