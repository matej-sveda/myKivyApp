import kivy
kivy.require("1.10.1")
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup

class CustomPopup(Popup):
    pass

class MainWidget(Widget):

    checkbox_is_active = False

    def checkbox_active(self, instance, value):
        if value == True:
            self.checkbox_is_active = True
        else:
            self.checkbox_is_active = False

    def open_consent_popup(self):
        consent_popup = CustomPopup()
        consent_popup.title = "Your personal data consent is needed before sending a message."
        consent_popup.open()

    def open_missing_popup(self):
        missing_popup = CustomPopup()
        missing_popup.title = "Some of the required information is missing."
        missing_popup.open()

    def send_msg(self):

        if self.ids.email.text == "" or self.ids.name.text == "" \
                                      or self.ids.msg_content.text == "":
            self.open_missing_popup()
        elif self.checkbox_is_active == True:
            msg = "Message from {1} ({0}): \n{2}\n\n"\
                .format(self.ids.email.text, self.ids.name.text, self.ids.msg_content.text)
            print(msg)
            return msg
        else:
            self.open_consent_popup()

class myKivyApp(App):

    def build(self):
        return MainWidget()

if __name__ == "__main__":
    myKivyApp().run()
