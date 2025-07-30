import keyboard as k
import threading
import tkinter as tk
from tkinter.simpledialog import askstring
import time, pyperclip
from utils.tools import bring_cmd_to_front
from llm.openai import ask_openai

system_prompt = "You are a honest and knowledgaeble assistant."

def search_openai():
    
    #retrieve highlighted text (if any)
    search_content = get_text()

    def run_popup():
        root = tk.Tk()
        root.withdraw()
        ques = askstring("Input","How can I help?")

        if not ques:
            return
        
        # consolidate user input + highlighted text
        user_prompt = ques + '\n' + search_content

        bring_cmd_to_front()
        print('-------------------------------------------------------------')
        print(user_prompt)

        # call openai api
        ans = ask_openai(system_prompt, user_prompt)

        # print results
        print(ans)
        print('-------------------------------------------------------------')

        root.destroy()

    threading.Thread(target=run_popup).start()

def get_text():
    #retrieve highlighted text
    k.press_and_release('ctrl+c')
    time.sleep(0.2)
    return pyperclip.paste()

k.add_hotkey('ctrl+1', search_openai, suppress=True)

k.wait('esc')