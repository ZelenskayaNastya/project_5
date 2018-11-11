file_str = input('Enter name of file: ')
try:
    find_line_str = open(file_str, 'r')
    with find_line_str as f_in:
        with open ('output.txt', 'w') as f_out:
            text = f_in.read()
            text = text.upper()
            text_str = text.find(',')
            for i in text:
                if i == 'А':
                    i = i.replace('А', '1')
                    f_out.write(i)
                if i == 'Б':
                    i = i.replace('Б', '2')
                    f_out.write(i)
                if i == 'В':
                    i = i.replace('В', '3')
                    f_out.write(i)
                if i == 'Г':
                    i = i.replace('Г', '4')
                    f_out.write(i)
                if i == 'Д':
                    i = i.replace('Д', '5')
                    f_out.write(i)
                if i == 'Е':
                    i = i.replace('Е', '6')
                    f_out.write(i)
                if i == 'Ё':
                    i = i.replace('Ё', '7')
                    f_out.write(i)
                if i == 'Ж':
                    i = i.replace('Ж', '8')
                    f_out.write(i)
                if i == 'З':
                    i = i.replace('З', '9')
                    f_out.write(i)
                if i == 'И':
                    i = i.replace('И', '/')
                    f_out.write(i)
                if i == 'Й':
                    i = i.replace('Й', '+')
                    f_out.write(i)
                if i == 'К':
                    i = i.replace('К', '=')
                    f_out.write(i)
                if i == 'Л':
                    i = i.replace('Л', '+=')
                    f_out.write(i)
                if i == 'М':
                    i = i.replace('М', '!+')
                    f_out.write(i)
                if i == 'Н':
                    i = i.replace('Н', '-')
                    f_out.write(i)
                if i == 'О':
                    i = i.replace('О', '№')
                    f_out.write(i)
                if i == 'П':
                    i = i.replace('П', '%')
                    f_out.write(i)
                if i == 'З':
                    i = i.replace('Р', ':')
                    f_out.write(i)
                if i == 'С':
                    i = i.replace('С', '№!')
                    f_out.write(i)
                if i == 'Т':
                    i = i.replace('Т', '№+№')
                    f_out.write(i)
                if i == 'У':
                    i = i.replace('У', ';')
                    f_out.write(i)
                if i == 'Х':
                    i = i.replace('Х', '(')
                    f_out.write(i)
                if i == 'Ц':
                    i = i.replace('Ц', ')')
                    f_out.write(i)
                if i == 'Ч':
                    i = i.replace('Ч', '(;)')
                    f_out.write(i)
                if i == 'Ш':
                    i = i.replace('Ш', '.-.')
                    f_out.write(i)
                if i == 'Щ':
                    i = i.replace('Щ', '.-.')
                    f_out.write(i)
                if i == 'Ъ':
                    i = i.replace('Ъ', '%-%')
                    f_out.write(i)
                if i == 'Ъ':
                    i = i.replace('Ъ', '!-!')
                    f_out.write(i)
                if i == 'Ь':
                    i = i.replace('Ь', '%№%')
                    f_out.write(i)
                if i == 'Э':
                    i = i.replace('Э', '!+!')
                    f_out.write(i)
                if i == 'Ю':
                    i = i.replace('Ю', '?')
                    f_out.write(i)
                if i == 'Я':
                    i = i.replace('Я', '+=+')
                    f_out.write(i)
                if i == ' ':
                    i = i.replace(' ', ' ')
                    f_out.write(i)
                if i == ',':
                    i = i.replace(',', ',')
                    f_out.write(i)
                if i == '!':
                    i = i.replace('!', '!')
                    f_out.write(i)
except FileNotFoundError:
    print('File {} not faund.'.format(file_str))






