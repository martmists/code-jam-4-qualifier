"""
A GUI application for a rocketship launch control panel.
This application is built on tkinter. See the official
documentation and linked resources here:
    https://docs.python.org/3/library/tkinter.html

Requirements:
    Python 3.
"""
import time
import tkinter as tk


class RocketShipControlPanel(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.pilot = None
        self.pilot_label = None
        self.password = None
        self.password_label = None
        self.launch_button = None

        self.countdown = None
        self.iter = 0

        self.password_value = tk.StringVar()
        self.pilot_value = tk.StringVar()

    def create_form(self):
        """
        Create the input fields, labels,
        and buttons when called.
        """

        self.pilot_label = tk.Label(
            self,
            text="Pilot: ",
        )
        self.pilot = tk.Entry(
            self,
            width=30,
            textvariable=self.pilot_value
        )
        self.pilot_label.pack(side=tk.TOP)
        self.pilot.pack(side=tk.TOP)

        self.password_label = tk.Label(
            self,
            text="Password: "
        )
        self.password = tk.Entry(
            self,
            width=30,
            show="*",
            textvariable=self.password_value
        )
        self.password_label.pack(side=tk.TOP)
        self.password.pack(side=tk.TOP)

        self.launch_button = tk.Button(
            self,
            text="Launch",
            # command=self.do_countdown_task  # Uncomment this and comment do_countdown to get the one from the task
            command=self.do_countdown,
            bg="teal",
            fg="white"
        )
        self.launch_button.pack(side=tk.BOTTOM)

    def do_countdown_task(self):
        """
        Do_countdown as the task explains cause I like mine better lol idk
        """

        if self.password_value.get() and self.pilot_value.get() and self.iter <= 3:
            if self.countdown is None:
                self.countdown = tk.Label(self, text="3")
                self.countdown.pack()

            next_text = ["3", "2", "1", "LIFTOFF!"][self.iter]
            self.iter += 1

            self.countdown.configure(text=next_text)

    def do_countdown(self):
        """
        When the user clicks the login button, this callback
        is invoked. Make it do a countdown. The first time
        it is clicked, the button text should change to "3".
        The next time to "2", then to "1", and then to "LIFTOFF!".

        If the username or the password are blank, this
        callback should not do anything.

        Note: This is my own take on the countdown, for the task, see line 66 and do_countdown_task
        """

        if self.password_value.get() and self.pilot_value.get() and self.iter == 0:
            self.iter = 1  # Successive presses wont work anymore
            self.countdown = tk.Label(self, text="3")
            self.countdown.pack()

            for i in range(3):
                self.countdown.configure(text=str(3-i))
                self.update()
                time.sleep(1)

            self.countdown.configure(text="LIFTOFF!")


if __name__ == "__main__":
    root = tk.Tk()
    app = RocketShipControlPanel(master=root)
    app.create_form()
    app.mainloop()
