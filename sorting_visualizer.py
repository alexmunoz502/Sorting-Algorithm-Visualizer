# Author:
# Date:
# Description:
import tkinter as tk
from tkinter import E, W, ttk
import random
import time


class Application:
    def __init__(self):
        # Class Attributes
        self.number_list = list()
        self.max_number = 1
        self.sorting_algorithms = {
            "Bubble Sort": self.bubble_sort,
            "Insertion Sort": self.insertion_sort
        }

        # GUI Initialization
        # Root
        self.root = tk.Tk()
        self.root.geometry("325x425")

        # Canvas
        self.canvas_height = 225
        self.canvas_width = 300
        self.tk_canvas = tk.Canvas(self.root, height=self.canvas_height, width=self.canvas_width, bd=1, relief="solid")
        self.tk_canvas.grid(row=0, columnspan=3, padx=8, pady=8)

        # List Control
        #   o   List Range
        self.label_list_range = tk.Label(self.root, text="List range: ")
        self.label_list_range.grid(row=1, column=0, sticky=W, padx=8)

        self.list_range_entry_box = tk.Entry(self.root)
        self.list_range_entry_box.grid(row=1, column=2, sticky=E, padx=8)

        #   o   List Size
        self.label_list_size = tk.Label(self.root, text="List size: ")
        self.label_list_size.grid(row=2, column=0, sticky=W, padx=8)

        self.list_size_entry_box = tk.Entry(self.root)
        self.list_size_entry_box.grid(row=2, column=2, sticky=E, padx=8)

        #   o   Generate List Button
        self.generate_list_button = tk.Button(self.root, text="Generate New List", command=self.generate_list)
        self.generate_list_button.grid(row=3, column=2, sticky=E, padx=8)

        # Algorithm Control
        #   o   Sorting Algorithm
        self.label_sorting_algorithm = tk.Label(self.root, text="Sorting Algorithm: ")
        self.label_sorting_algorithm.grid(row=4, column=0, sticky=W, padx=8)

        self.combobox_algorithms = ttk.Combobox(self.root, values=["Bubble Sort", "Insertion Sort"])
        self.combobox_algorithms.set("Bubble Sort")
        self.combobox_algorithms.grid(row=4, column=2, sticky=E, padx=8)

        #   o   Sort Time Multiplier
        self.label_sort_time_multiplier = tk.Label(self.root, text="Sort Time Multiplier: ")
        self.label_sort_time_multiplier.grid(row=5, column=0, sticky=W, padx=8)

        self.timer_slider = tk.Scale(self.root, from_=1, to=10, orient=tk.HORIZONTAL)
        self.timer_slider.set(5)
        self.timer_slider.grid(row=5, column=2, sticky=E, padx=8)

        #   o   Sort List Button
        self.sort_button = tk.Button(self.root, text="Sort", command=self.sort_command)
        self.sort_button.grid(row=6, column=2, sticky=E, padx=8)

    @property
    def sorting_algorithm(self):
        return self.sorting_algorithms[self.combobox_algorithms.get()]

    @property
    def bar_width(self):
        return self.canvas_width / len(self.number_list)

    @property
    def bar_height(self):
        return self.canvas_height / self.max_number

    @property
    def tick_time(self):
        time_multiplier = self.timer_slider.get()
        return 1 / (time_multiplier**100)

    def start(self):
        self.root.mainloop()

    def generate_list(self):
        try:
            range_max = int(self.list_range_entry_box.get())
            number_of_elements = int(self.list_size_entry_box.get())
            self.number_list = [random.randint(1, range_max) for _ in range(number_of_elements)]
            self.set_max()
            self.display_list_bars()
        except ValueError:
            print("User tried to generate list using invalid list size or length specifier.")

    def clear_canvas(self):
        self.tk_canvas.delete("all")

    def set_max(self):
        self.max_number = self.number_list[0]
        for number in self.number_list:
            if number > self.max_number:
                self.max_number = number

    def display_list_bars(self, highlight_bar=None):
        self.clear_canvas()
        for i, num in enumerate(self.number_list):
            # Establish Rectangle Dimensions
            x1 = i * self.bar_width
            y1 = self.canvas_height
            x2 = (i + 1) * self.bar_width
            y2 = self.canvas_height - (num * self.bar_height)

            # Create Rectangle
            color = 'blue' if highlight_bar != i else 'gold'
            self.tk_canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

    def bubble_sort(self):
        list_length = len(self.number_list)
        for i in range(list_length):
            for j in range(0, list_length - i - 1):
                # display current step
                self.display_list_bars(highlight_bar=j)
                self.root.update()
                time.sleep(self.tick_time)
                # resolve current step
                if self.number_list[j] > self.number_list[j + 1]:
                    self.number_list[j], self.number_list[j + 1] = self.number_list[j + 1], self.number_list[j]

    def insertion_sort(self):
        list_length = len(self.number_list)
        for i in range(1, list_length):
            current_position = i
            current_value = self.number_list[i]
            while current_position>0 and self.number_list[current_position-1]>current_value:
                # display current step
                self.display_list_bars(highlight_bar=current_position)
                self.root.update()
                time.sleep(self.tick_time)
                # resolve current step
                self.number_list[current_position] = self.number_list[current_position-1]
                current_position -= 1
            self.number_list[current_position] = current_value


    def sort_command(self):
        self.sorting_algorithm()
        self.display_list_bars()


if __name__ == "__main__":
    sv = Application()
    sv.start()