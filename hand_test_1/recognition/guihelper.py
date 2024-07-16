import tkinter as tk
from tkinter import messagebox as msg
from tkinter import simpledialog


def show_info(message):
    msg.showinfo("Message", message)


def get_input(message):
    return simpledialog.askinteger("Input", message)


if __name__ == "__main__":

    print(get_input("Input"))
