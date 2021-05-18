import os
import click_img
import sheet


# a = sheet.write('1', "Sheet1!C1:C2")


def reg(data):
    print(data)
    os.mkdir("images/" + data)
    click_img.start(data)

    global a
    a = (sheet.read("Sheet1!C1:C2")[0])
    print((a[0]))
    consumer_column = "Sheet1!A0" + ":A" + str(int(a[0]) + 1)

    sheet.write(data, consumer_column)

    a[0] += str(int(a[0]) + 1)
    sheet.write(str(a), "Sheet1!C1:C2")


name = input("Enter the person's name")
reg(name)
