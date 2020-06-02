import requests
from bs4 import BeautifulSoup
import tkinter as tk

cases = []
# website is https://www.nytimes.com/interactive/2020/us/connecticut-coronavirus-cases.html
request = requests.get("https://www.nytimes.com/interactive/2020/us/connecticut-coronavirus-cases.html")
soup = BeautifulSoup(request.text, 'html.parser')
numbers = soup.find_all(class_="count svelte-9rb9hv")
for number in numbers:
    cases.append(number.find(class_="num svelte-9rb9hv").get_text())

# assigns each variable to a spot in the list
totalCases = cases[0]
deaths = cases[1]



# creates GUI with the info
root = tk.Tk()
T = tk.Text(root, height=2, width=30)
T.pack()
T.insert(tk.END, "Total Cases: {}\nTotal Deaths: {}\n".format(totalCases, deaths))
tk.mainloop()