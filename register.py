import os
import click_img


def reg(data):
    print(data)
    os.mkdir("images/" + data)
    click_img.start(data)


name = input("Enter the name of the person ")
reg(name)
