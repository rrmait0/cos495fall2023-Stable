from kivy.config import Config

#Sets window size and restricts resizing
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '700')
Config.set('graphics', 'resizable', False)

import kivy
#import webbrowser
kivy.require('2.2.1')

from kivy.app import App
#from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
#from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

#class AppManager(ScreenManager):
 #   pass

#class MyApp(App):
 #   def build(self):
  #      screenManager = AppManager()

   #     initialScreen = InitialScreen(name="Initial Screen")
    #    signUpScreen = signUpScreen(name="Sign Up")

     #   screenManager.add_widget(initialScreen)
      #  screenManager.add_widget(signUpScreen)

       # return screenManager


# Layout for the background
class Background(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.016, 0.416, 0.22, 1)  # Green color
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)
    
    def update_rect(self, instance, value):
        self.rect.size = self.size
        self.rect.pos = self.pos

#Initial Screen
class initialScreen(App):
    def build(self):
        # Create the main layout as a FloatLayout
        layout = FloatLayout()

        # Implement the green background
        background = Background()

        # Implement the logo
        stablesLogo = Image(source='Stables Logo.png')
        stablesLogo.pos_hint = {'center_x': 0.25, 'top': 1.3}

        # Create a label for the title with gold text
        titleLabel = Label(text='[u]Stables[/u]', markup=True, font_size=120, font_name= "Comic", color=(1, 0.851, 0.106, 1))  # Gold color
        titleLabel.size_hint = (None, None)
        titleLabel.pos_hint = {'center_x': 0.55, 'top': 0.875}

        # Creates signup and login labels and binds to the switch function
        signUpText = Label(text='New here?', font_size=40, font_name="Comic", color=(1, 0.851, 0.106, 1))
        signUpText.size_hint = (None, None)
        signUpText.pos_hint = {'center_x': 0.4, 'top': 0.4}

        signUpLink = Label(text='[u][ref=sign up]Sign up[/ref][/u]', markup=True, font_size=40, font_name="Comic", color=(1, 0.851, 0.106, 1))
        signUpLink.bind(on_ref_press=lambda instance, value:self.switchScreen(instance, value, "signUpChoice"))
        signUpLink.size_hint = (None, None)
        signUpLink.pos_hint = {'center_x': 0.6, 'top': 0.4}

        loginText = Label(text='Have an account?    ', font_size=40, font_name="Comic", color=(1, 0.851, 0.106, 1))
        loginText.size_hint = (None, None)
        loginText.pos_hint = {'center_x': 0.4, 'top': 0.3}

        loginLink = Label(text='   [u][ref=login]Login[/ref][/u]', markup=True, font_size=40, font_name="Comic", color=(1, 0.851, 0.106, 1))
        loginLink.bind(on_ref_press=lambda instance, value:self.switchScreen(instance, value, "loginChoice"))
        loginLink.size_hint = (None, None)
        loginLink.pos_hint = {'center_x': 0.6, 'top': 0.3}

        

        # Create a text input for the username
#        username_input = TextInput(hint_text='Username', halign='center', multiline=False, font_size=18)
 #       username_input.size_hint = (None, None)
  #      username_input.size = (200, 30)
   #     username_input.pos_hint = {'center_x': 0.5, 'top': 0.6}
    #    username_input.padding = [0,4]

        # Create a text input for the password
#        password_input = TextInput(hint_text='Password', halign='center', multiline=False, password=True, font_size=18)
 #       password_input.size_hint = (None, None)
  #      password_input.size = (200, 30)
   #     password_input.pos_hint = {'center_x': 0.5, 'top': 0.55}
    #    password_input.padding = [0,4]

        # Create a gold login button with black background
#        login_button = Button(text='Login', size_hint=(None, None), size=(100, 50),
 #                             background_color=(0, 0, 0, 1), color=(1, 0.851, 0.106, 1))  # Gold color
  #      login_button.pos_hint = {'center_x': 0.5, 'top': 0.5}

        # Add widgets to the layout
        layout.add_widget(background)
        layout.add_widget(stablesLogo)
        layout.add_widget(titleLabel)
        layout.add_widget(signUpText)
        layout.add_widget(signUpLink)
        layout.add_widget(loginText)
        layout.add_widget(loginLink)
#        layout.add_widget(username_input)
 #       layout.add_widget(password_input)
  #      layout.add_widget(login_button)

        return layout
    
    #def open_link(self):
        # Define the URL you want to open
        #url = 'https://www.kysu.edu/index.php'
        
        # Open the URL in the default web browser
        #webbrowser.open(url)

        #login_button.bind(on_release=open_link)
    
    #Switches to the sign up / login screen
    def switchScreen(self, instance, value, screen):
        if screen == "signUpChoice":
            self.stop()
            signUpScreen().run()
        elif screen == "loginChoice":
            self.stop()
            loginScreen().run()

# Sign up screen
class signUpScreen(App):
    def build(self):
        # Create the main layout as a FloatLayout
        layout = FloatLayout()

        # Implement the green background
        background = Background()

        # Create an Account label
        createAccountLabel = Label(text='Create an Account', markup= True, font_size=80, font_name= "Comic", color=(1, 0.851, 0.106, 1))  # Gold color
        createAccountLabel.size_hint = (None, None)
        createAccountLabel.pos_hint = {'center_x': 0.5, 'top': 0.95}

        # First name input
        firstNameLabel = Label(text='First', markup= True, font_size=30, font_name= "Comic", color=(1, 0.851, 0.106, 1))  # Gold color
        firstNameLabel.size_hint = (None, None)
        firstNameLabel.pos_hint = {'center_x': 0.3, 'top': 0.83}

        firstNameInput = TextInput(hint_text='e.g. John', halign='center', multiline=False, font_size=18)
        firstNameInput.size_hint = (None, None)
        firstNameInput.size = (200, 30)
        firstNameInput.pos_hint = {'center_x': 0.3, 'top': 0.75}
        firstNameInput.padding = [0,4]

        # Last name input
        lastNameLabel = Label(text='Last', markup= True, font_size=30, font_name= "Comic", color=(1, 0.851, 0.106, 1))  # Gold color
        lastNameLabel.size_hint = (None, None)
        lastNameLabel.pos_hint = {'center_x': 0.7, 'top': 0.83}

        lastNameInput = TextInput(hint_text='e.g. Smith', halign='center', multiline=False, font_size=18)
        lastNameInput.size_hint = (None, None)
        lastNameInput.size = (200, 30)
        lastNameInput.pos_hint = {'center_x': 0.7, 'top': 0.75}
        lastNameInput.padding = [0,4]

        # Email address input
        emailLabel = Label(text='Email', markup= True, font_size=30, font_name= "Comic", color=(1, 0.851, 0.106, 1))  # Gold color
        emailLabel.size_hint = (None, None)
        emailLabel.pos_hint = {'center_x': 0.5, 'top': 0.73}

        emailInput = TextInput(hint_text='e.g. John.Smith@kysu.edu', halign='center', multiline=False, font_size=18)
        emailInput.size_hint = (None, None)
        emailInput.size = (400, 30)
        emailInput.pos_hint = {'center_x': 0.5, 'top': 0.65}
        emailInput.padding = [0,4]

        # Password input
        passwordLabel = Label(text='Password', markup= True, font_size=30, font_name= "Comic", color=(1, 0.851, 0.106, 1))  # Gold color
        passwordLabel.size_hint = (None, None)
        passwordLabel.pos_hint = {'center_x': 0.5, 'top': 0.63}

        passwordInput = TextInput(hint_text='e.g. JohnSmith123!', halign='center', multiline=False, font_size=18)
        passwordInput.size_hint = (None, None)
        passwordInput.size = (400, 30)
        passwordInput.pos_hint = {'center_x': 0.5, 'top': 0.55}
        passwordInput.padding = [0,4]

        # Re-enter password input
        rePasswordLabel = Label(text='Re-enter Password', markup= True, font_size=30, font_name= "Comic", color=(1, 0.851, 0.106, 1))  # Gold color
        rePasswordLabel.size_hint = (None, None)
        rePasswordLabel.pos_hint = {'center_x': 0.5, 'top': 0.53}

        rePasswordInput = TextInput(hint_text='e.g. JohnSmith123!', halign='center', multiline=False, font_size=18)
        rePasswordInput.size_hint = (None, None)
        rePasswordInput.size = (400, 30)
        rePasswordInput.pos_hint = {'center_x': 0.5, 'top': 0.45}
        rePasswordInput.padding = [0,4]

        # Security question dropdown
        securityQLabel = Label(text='Security Question', markup= True, font_size=30, font_name= "Comic", color=(1, 0.851, 0.106, 1))  # Gold color
        securityQLabel.size_hint = (None, None)
        securityQLabel.pos_hint = {'center_x': 0.5, 'top': 0.43}
        # Create a DropDown
        dropdown = DropDown()

        # Add items to the dropdown
        btn = Button(text="What was the name of your first pet?", size_hint_y=None, height=30)
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        btn2 = Button(text="What was the name of your mother?", size_hint_y=None, height=30)
        btn2.bind(on_release=lambda btn: dropdown.select(btn2.text))
        btn3 = Button(text="What is your hometown?", size_hint_y=None, height=30)
        btn3.bind(on_release=lambda btn: dropdown.select(btn3.text))
        btn4 = Button(text="What is your favorite color?", size_hint_y=None, height=30)
        btn4.bind(on_release=lambda btn: dropdown.select(btn4.text))
        btn5 = Button(text="What high school did you go to?", size_hint_y=None, height=30)
        btn5.bind(on_release=lambda btn: dropdown.select(btn5.text))
        dropdown.add_widget(btn)
        dropdown.add_widget(btn2)
        dropdown.add_widget(btn3)
        dropdown.add_widget(btn4)
        dropdown.add_widget(btn5)

        # Create Main button
        mainButton = Button(text='-Select One-', size_hint=(None, None))
        mainButton.pos_hint = {'center_x':0.5, 'top':0.34}
        mainButton.size = (300,30)

        mainButton.bind(on_release=dropdown.open)

        dropdown.pos_hint = {'center_x':0.5, 'top':0.305}

        # Bind the dropdown to the button
        dropdown.bind(on_select=lambda instance, x: setattr(mainButton, 'text', x))

        # Security question input
        securityAnswerLabel = Label(text='Security Question Answer', markup= True, font_size=30, font_name= "Comic", color=(1, 0.851, 0.106, 1))  # Gold color
        securityAnswerLabel.size_hint = (None, None)
        securityAnswerLabel.pos_hint = {'center_x': 0.5, 'top': 0.32}

        securityAnswerInput = TextInput(hint_text='Answer Here', halign='center', multiline=False, font_size=18)
        securityAnswerInput.size_hint = (None, None)
        securityAnswerInput.size = (400, 30)
        securityAnswerInput.pos_hint = {'center_x': 0.5, 'top': 0.24}
        securityAnswerInput.padding = [0,4]

        #Enter button
        enterButton = Button(halign='center', size_hint=(None, None), background_color=(0, 0, 0, 1))
        enterButton.size = (200,40)
        enterButton.pos_hint = {'center_x': 0.5, 'top': 0.18}

        #Creates text for button
        enterLabel = Label(text='[ref=enter]Enter[/ref]', markup = True, font_name = "Comic", font_size = 30, valign='middle', size_hint=(None, None), color=(1, 0.851, 0.106, 1))
        enterLabel.pos_hint = {'center_x': 0.5, 'top': 0.217}

        #Redirect to login page
        redirectToLogin = Label(text='[u][ref=login]Have an account?[/ref][/u]', markup=True, font_size=20, font_name="Comic", color=(1, 0.851, 0.106, 1))
        redirectToLogin.bind(on_ref_press=lambda instance, value: self.switchScreen(instance, value, "loginChoice"))
        redirectToLogin.size_hint = (None, None)
        redirectToLogin.pos_hint = {'center_x': 0.9, 'top': 0.10}

        # Adds widgets to the layout
        layout.add_widget(background)
        layout.add_widget(createAccountLabel)
        layout.add_widget(firstNameLabel)
        layout.add_widget(firstNameInput)
        layout.add_widget(lastNameLabel)
        layout.add_widget(lastNameInput)
        layout.add_widget(emailLabel)
        layout.add_widget(emailInput)
        layout.add_widget(passwordLabel)
        layout.add_widget(passwordInput)
        layout.add_widget(rePasswordLabel)
        layout.add_widget(rePasswordInput)
        layout.add_widget(securityQLabel)
        layout.add_widget(mainButton)
        layout.add_widget(securityAnswerLabel)
        layout.add_widget(securityAnswerInput)
        layout.add_widget(enterButton)
        layout.add_widget(enterLabel)
        layout.add_widget(redirectToLogin)

        def saveInfo(instance, value):
            userInfo = open("UserInformation", "w")
            firstName = firstNameInput.text
            lastName = lastNameInput.text
            email = emailInput.text
            password = passwordInput.text
            securityAnswer = securityAnswerInput.text
            userInfo.write(f"{firstName}\n")
            userInfo.write(f"{lastName}\n")
            userInfo.write(f"{email}\n")
            userInfo.write(f"{password}\n")
            userInfo.write(f"{securityAnswer}")
            self.stop()

        enterLabel.bind(on_ref_press= saveInfo)

        return layout
    
    def switchScreen(self, instance, value, screen):
        if screen == "loginChoice":
            self.stop()
            loginScreen().run()

# Sign up screen
class loginScreen(App):
    def build(self):
        # Create the main layout as a FloatLayout
        layout = FloatLayout()

        # Implement the green background
        background = Background()

        # Welcome Back label
        welcomeBackLabel = Label(text='Welcome Back!', markup= True, font_size=80, font_name= "Comic", color=(1, 0.851, 0.106, 1))  # Gold color
        welcomeBackLabel.size_hint = (None, None)
        welcomeBackLabel.pos_hint = {'center_x': 0.5, 'top': 0.95}

        # Email address input
        emailLabel = Label(text='Email', markup= True, font_size=30, font_name= "Comic", color=(1, 0.851, 0.106, 1))  # Gold color
        emailLabel.size_hint = (None, None)
        emailLabel.pos_hint = {'center_x': 0.5, 'top': 0.75}

        emailInput = TextInput(hint_text='e.g. John.Smith@kysu.edu', halign='center', multiline=False, font_size=18)
        emailInput.size_hint = (None, None)
        emailInput.size = (400, 30)
        emailInput.pos_hint = {'center_x': 0.5, 'top': 0.67}
        emailInput.padding = [0,4]

        # Password input
        passwordLabel = Label(text='Password', markup= True, font_size=30, font_name= "Comic", color=(1, 0.851, 0.106, 1))  # Gold color
        passwordLabel.size_hint = (None, None)
        passwordLabel.pos_hint = {'center_x': 0.5, 'top': 0.65}

        passwordInput = TextInput(hint_text='e.g. JohnSmith123!', halign='center', multiline=False, font_size=18)
        passwordInput.size_hint = (None, None)
        passwordInput.size = (400, 30)
        passwordInput.pos_hint = {'center_x': 0.5, 'top': 0.57}
        passwordInput.padding = [0,4]

        #Redirect to forgot password page
        forgotPass = Label(text='[u]Forgot password?[/u]', markup=True, font_size=20, font_name="Comic", color=(1, 0.851, 0.106, 1))
        forgotPass.size_hint = (None, None)
        forgotPass.pos_hint = {'center_x': 0.5, 'top': 0.56}

        #Enter button to go to dashboard
        loginButton = Button(halign='center', size_hint=(None, None), background_color=(0, 0, 0, 1))
        loginButton.size = (200,40)
        loginButton.pos_hint = {'center_x': 0.5, 'top': 0.38}

        #Creates text for button
        loginLabel = Label(text='Log In', markup = True, font_name = "Comic", font_size = 30, valign='middle', size_hint=(None, None), color=(1, 0.851, 0.106, 1))
        loginLabel.pos_hint = {'center_x': 0.5, 'top': 0.419}

        #Redirect to Sign Up page
        redirectToSignup = Label(text='[u][ref=sign up]Need to create an account?[/ref][/u]', markup=True, font_size=20, font_name="Comic", color=(1, 0.851, 0.106, 1))
        redirectToSignup.bind(on_ref_press=lambda instance, value: self.switchScreen(instance, value, "signUpChoice"))
        redirectToSignup.size_hint = (None, None)
        redirectToSignup.pos_hint = {'center_x': 0.5, 'top': 0.35}


        #Adds widgets to layout
        layout.add_widget(background)
        layout.add_widget(welcomeBackLabel)
        layout.add_widget(emailLabel)
        layout.add_widget(emailInput)
        layout.add_widget(passwordLabel)
        layout.add_widget(passwordInput)
        layout.add_widget(forgotPass)
        layout.add_widget(loginButton)
        layout.add_widget(loginLabel)
        layout.add_widget(redirectToSignup)

        return layout
    
    def switchScreen(self, instance, value, screen):
        if screen == "signUpChoice":
            self.stop()
            signUpScreen().run()

#Forgot Password screen
class forgotPass(App):
    def build(self):
        # Create the main layout as a FloatLayout
        layout = FloatLayout()

        # Implement the green background
        background = Background()






        layout.add_widget(background)

        return layout

# Starts application
if __name__ == '__main__':
    initialScreen().run()