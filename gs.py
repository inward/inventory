import pygsheets


def check_part(num):
    gc = pygsheets.authorize(client_secret='client_secret.json')
    sh = gc.open('Python2')
    wks = sh.sheet1
    cells = wks.find(str(num))
    if len(cells) > 0:
        c2 = wks.cell(str(cells[0]).split()[1].replace('A', 'J'))
        if c2.value == "":
            c2.value = '1'
        else:
            c2.value = str(int(c2.value) + 1)
        c2.color = (0.5, 0.6, 0.7, 1.0)
    else:
        c2 = wks.cell('K2')
        c2.value = str(num)