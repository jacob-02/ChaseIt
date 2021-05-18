import os
import click_img
import sheet

a = sheet.write('0', "Sheet1!C1:C2")


def reg(data):
    print(data)
    os.mkdir("images/" + data)
    click_img.start(data)

    global a
    a = sheet.read("Sheet1!C1:C2")
    consumer_column = "Sheet1!A" + str(a) + ":A" + str(a + 1)

    sheet.write(data, consumer_column)

    a += 1


name = input("Enter the name of the person ")
reg(name)
