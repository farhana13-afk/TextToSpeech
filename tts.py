import pyttsx3

def read_text(text):
    engine = pyttsx3.init()
    #set voices properties
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    #synthesize speech and play
    engine.say(text)
    engine.runAndWait()

def read_text_file(file_name, startline =1, end_line =-1):
    engine = pyttsx3.init()

    with open(file_name, 'r') as file:
        lines= file.readlines()

    if(end_line == -1):
        end_line = len(lines)
    else:
        end_line = min(end_line, len(lines))
    selected_lines = lines[start_line-1: end_line]

    text = "".join(selected_lines)

    voices = engine.getProperty('voices')
    engine.setProperty('voice',  voices[3].id)

    engine.say(text)
    engine.runAndWait()

while True:
    choice = input("Enter 't' to input text: ")

    #if choice == 'f':
        #file_name = input("enter the file name: ")
       # start_line = int(input("enter the starting line number: "))
       # end_line_str = input("Enter the ending line number (or leave blank to read to end): ")


    if choice == 't':
        text = input("Enter the text: ")
        read_text(text)
    else:
        print("Invalid choice. Please enter again.")





