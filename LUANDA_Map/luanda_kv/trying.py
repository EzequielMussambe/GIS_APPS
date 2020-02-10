from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.theming import ThemeManager

Builder.load_string('''
#:import Window kivy.core.window.Window

#:set color_shadow [0, 0, 0, .2980392156862745]


<MyMDTextFieldRound@MDTextFieldRound>
    size_hint_x: None
    normal_color: color_shadow
    active_color: color_shadow


<TextFields@Screen>
    name: 'textfields'

    canvas:
        Color:
            rgba: 0, 0, 0, .2
        Rectangle:
            pos: self.pos
            size: self.size

    ScrollView:

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            padding: dp(48)
            spacing: dp(15)

            MyMDTextFieldRound:
                hint_text: 'Empty field'

            MyMDTextFieldRound:
                icon_left: 'email'
                hint_text: 'Field with left icon'

            MyMDTextFieldRound:
                icon_left: 'key-variant'
                icon_right: 'eye-off'
                hint_text: 'Field with left and right icons'

            MDTextField:
                hint_text: 'mode = "rectangle"'
                mode: "rectangle"

            MDTextField:
                input_filter: "int"
                hint_text: "Numeric field"

            MDTextField:
                hint_text: "No helper text"

            MDTextField:
                hint_text: "Helper text on focus"
                helper_text: "This will disappear when you click off"
                helper_text_mode: "on_focus"

            MDTextField:
                hint_text: "Persistent helper text"
                helper_text: "Text is always here"
                helper_text_mode: "persistent"

            Widget:
                size_hint_y: None
                height: dp(5)

            MDTextField:
                id: text_field_error
                hint_text: "Helper text on error (Hit Enter with  two characters here)"
                helper_text: "Two is my least favorite number"
                helper_text_mode: "on_error"

            MDTextField:
                hint_text: "Max text length = 10"
                max_text_length: 10

            MDTextField:
                hint_text: "required = True"
                required: True
                helper_text_mode: "on_error"

            MDTextField:
                multiline: True
                hint_text: "Multi-line text"
                helper_text: "Messages are also supported here"
                helper_text_mode: "persistent"

            MDTextField:
                hint_text: "color_mode = 'accent'"
                color_mode: 'accent'

            MDTextField:
                hint_text: "color_mode = 'custom'"
                color_mode: 'custom'
                helper_text_mode: "on_focus"
                helper_text: "Color is defined by 'line_color_focus' property"
                line_color_focus: self.theme_cls.opposite_bg_normal

            MDTextField:
                hint_text: "disabled = True"
                disabled: True

            MDTextFieldRect:
                size_hint: None, None
                size: Window.width - dp(40), dp(30)
                pos_hint: {'center_y': .5, 'center_x': .5}
''')


class Example(MDApp):
    title = "Example Text Fields"
    main_widget = None

    def build(self):
        return Factory.TextFields()

    def show_password(self, field, button):
        '''
        Called when you press the right button in the password field
        for the screen TextFields.

        instance_field: kivy.uix.textinput.TextInput;
        instance_button: kivymd.button.MDIconButton;

        '''

        # Show or hide text of password, set focus field
        # and set icon of right button.
        field.password = not field.password
        field.focus = True
        button.icon = "eye" if button.icon == "eye-off" else "eye-off"


Example().run()