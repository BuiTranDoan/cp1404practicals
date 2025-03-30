from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "David", "Eve"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.bind(on_touch_down=self.label_clicked)
            self.root.ids.labels_box.add_widget(temp_label)

    def label_clicked(self, instance, touch):
        """Handle label clicks."""
        if instance.collide_point(*touch.pos):
            self.status_text = f"You clicked on {instance.text}"

    def clear_all(self):
        """Clear all widgets that are children of the "labels_box" layout widget."""
        self.root.ids.labels_box.clear_widgets()

DynamicLabelsApp().run()