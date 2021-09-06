def add_space(words, length): 
    """creating new line with all the spaces needed"""
    length_of_words = 0
    for i in range(len(words)):
        length_of_words += len(words[i])
    all_spaces = length - length_of_words 
               
    while all_spaces > 0:
        for i in range(len(words)-1):
            words[i] += ' '
            all_spaces -= 1
            if all_spaces == 0:
                break
                
    new_line = ''.join(words)
    return(new_line)

new_text = ''
def write_new_lines(new_line):
    global new_text
    new_text += new_line + '\n'

with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

while True:
    num = input('Введите максимальное количество символов в строке (минимальное значение: 35)\n')
    try:
        num = int(num)
        if num < 35:
            print("Вы ввели неверное значение")
            continue
        else:
            break  
    except ValueError:
            print("Вы ввели неверное значение")
            continue
      
ind = 0

while ind in range(len(text)):

    if (ind+num) > len(text):
        line = text[ind : len(text)]
    else:
        line = text[ind : ind+num]

    if line.find('\n') != -1:

        if line.endswith('\n'):
            write_new_lines(line)
            ind += num
        else:    
            words = line.split('\n')
            last_word = len(words[-1])
            words = words[0].split(' ')
            
            if len(words) == 1:
                new_line = str(words[0])
                write_new_lines(new_line)
                ind += (len(new_line)+1)
            else:
                new_line = add_space(words, num)   
                write_new_lines(new_line)
                ind += (num - last_word)

    elif line.endswith(' '):
        words = line.strip().split(' ')
        new_line = add_space(words, num)   
        write_new_lines(new_line)
        ind += num
    
    else:
        words = line.split(' ')
        last_word = len(words[-1]) 
        
        if len(words) == 1:
                new_line = words[0]
                write_new_lines(new_line)
                ind += len(new_line)
        else:
            
            if (ind+num) < len(text):
                words.pop()
            else:
                pass 
            
            new_line = add_space(words, num)   
            write_new_lines(new_line)
            ind += (num - last_word)

with open('new_text.txt', 'w', encoding='utf-8') as f:
        f.write(new_text)