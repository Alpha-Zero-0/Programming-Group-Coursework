import tkinter as tk
from tkcalendar import Calendar

class InputDailyTab:
    def __init__(self, parent):
        self.parent = parent

        # ----- Input Section -----
        input_frame = tk.LabelFrame(self.parent, text="Input", padx=10, pady=10)
        input_frame.pack(side=tk.TOP, fill="x", padx=10, pady=5)

        # Screen Time Entry
        tk.Label(input_frame, text="Screen Time:").grid(row=0, column=0, sticky="w")
        self.entry_screen_time = tk.Entry(input_frame, width=10)
        self.entry_screen_time.grid(row=0, column=1, padx=5, pady=5)

        # Productivity Goal Entry
        tk.Label(input_frame, text="Productivity Goal:").grid(row=1, column=0, sticky="w")
        self.entry_productivity_goal = tk.Entry(input_frame, width=10)
        self.entry_productivity_goal.grid(row=1, column=1, padx=5, pady=5)

        # Productivity Time Entry
        tk.Label(input_frame, text="Productivity Time:").grid(row=2, column=0, sticky="w")
        self.entry_productivity_time = tk.Entry(input_frame, width=10)
        self.entry_productivity_time.grid(row=2, column=1, padx=5, pady=5)

        # Timer Buttons for Productivity
        timer_frame = tk.Frame(input_frame)
        timer_frame.grid(row=3, column=0, columnspan=2, pady=5)
        self.btn_go = tk.Button(timer_frame, text="Go", command=self.start_productivity_timer)
        self.btn_go.pack(side=tk.LEFT, padx=5)
        self.btn_stop = tk.Button(timer_frame, text="Stop", command=self.stop_productivity_timer)
        self.btn_stop.pack(side=tk.LEFT, padx=5)

        # ----- Calendar within the Input Section -----
        # Create a frame for the calendar widget
        calendar_frame = tk.Frame(input_frame)
        calendar_frame.grid(row=4, column=0, columnspan=2, pady=10)

        # Initialize the Calendar widget
        self.calendar = Calendar(calendar_frame, selectmode="day", year=2025, month=4, day=1)
        self.calendar.pack()

        # Button to get the selected date from the calendar
        self.btn_get_date = tk.Button(calendar_frame, text="Get Date", command=self.get_date)
        self.btn_get_date.pack(pady=5)

        # ----- Daily Total Section -----
        daily_total_frame = tk.LabelFrame(self.parent, text="Daily Total", padx=10, pady=10)
        daily_total_frame.pack(side=tk.TOP, fill="x", padx=10, pady=5)

        # Daily Screen Time
        tk.Label(daily_total_frame, text="Screen Time: 00:00").grid(row=0, column=0, sticky="w")
        self.btn_clear_screen = tk.Button(daily_total_frame, text="Clear", command=self.clear_screen_time)
        self.btn_clear_screen.grid(row=0, column=1, padx=5, pady=5)

        # Daily Productivity Time
        tk.Label(daily_total_frame, text="Productivity Time: 00:00").grid(row=1, column=0, sticky="w")
        self.btn_clear_productivity = tk.Button(daily_total_frame, text="Clear", command=self.clear_productivity_time)
        self.btn_clear_productivity.grid(row=1, column=1, padx=5, pady=5)

    def start_productivity_timer(self):
        # Start the productivity timer logic (to be implemented)
        print("Starting productivity timer... (to be implemented)")

    def stop_productivity_timer(self):
        # Stop the productivity timer logic (to be implemented)
        print("Stopping productivity timer... (to be implemented)")

    def clear_screen_time(self):
        # Reset the daily screen time (to be implemented)
        print("Clearing daily screen time... (to be implemented)")

    def clear_productivity_time(self):
        # Reset the daily productivity time (to be implemented)
        print("Clearing daily productivity time... (to be implemented)")

    def get_date(self):
        # Retrieve the selected date from the calendar widget
        selected_date = self.calendar.get_date()
        print("Selected date:", selected_date)
