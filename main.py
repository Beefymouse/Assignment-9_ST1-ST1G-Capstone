import tkinter
from tkinter import *


def predict_price(year, engine, power):
    import pandas as pd
    data = pd.DataFrame(data=[[year, engine, power]],
                        columns=['Year', 'Engine', 'Power'])

    import pickle
    with open('Final_RFR_Model.pkl', 'rb') as fileReadStream:
        rfr = pickle.load(fileReadStream)
        fileReadStream.close()

    return str(int(rfr.predict(data.values)*100000)*0.018)


# predicted_price = (predict_price(2016, 2000, 140.3)*100000)
# print(predicted_price)

# Root
root = Tk()
# Window Title
root.title('Used Car Price Prediction')
# Window Size
root.geometry('700x200')

# Frames
sub_frame = tkinter.Frame(root)
sub_frame.grid(row=2, column=2)
frame1 = tkinter.Frame(root)
frame1.grid(row=1, column=2)
frame2 = tkinter.Frame(sub_frame)
frame2.grid(row=2, column=1)
frame3 = tkinter.Frame(sub_frame)
frame3.grid(row=2, column=2)
frame4 = tkinter.Frame(sub_frame)
frame4.grid(row=2, column=3)

# Labels
label_main_title = tkinter.Label(frame1, text='Used Car Price Prediction',
                                 font='Arial, 16',
                                 border=True,
                                 fg='#1E2019')
label_main_title.pack(padx=5, pady=5)

label_data_title = tkinter.Label(frame3, text='Data',
                                 font='Arial, 16',
                                 border=True,
                                 fg='#1E2019')
label_data_title.grid(padx=5, pady=5, row=1, column=1)

label_engine = tkinter.Label(frame2, text='Engine in CC : ',
                             font='Arial, 14',
                             border=True,
                             fg='#1E2019')
label_engine.grid(padx=5, pady=5, row=1, column=1)
label_power = tkinter.Label(frame2, text='Power in bhp : ',
                            font='Arial, 14',
                            border=True,
                            fg='#1E2019')
label_power.grid(padx=5, pady=5, row=2, column=1)
label_year = tkinter.Label(frame2, text='Year of Model : ',
                           font='Arial, 14',
                           border=True,
                           fg='#1E2019')
label_year.grid(padx=5, pady=5, row=3, column=1)
label_price = tkinter.Label(frame4, text='Price in AUD : ',
                            font='Arial, 14',
                            border=True,
                            fg='#1E2019')
label_price.grid(padx=5, pady=5, row=1, column=1)
# Entries
entry_engine = tkinter.Entry(frame2)
entry_engine.grid(padx=5, pady=5, row=1, column=2)
entry_power = tkinter.Entry(frame2)
entry_power.grid(padx=5, pady=5, row=2, column=2)
entry_year = tkinter.Entry(frame2)
entry_year.grid(padx=5, pady=5, row=3, column=2)
# Read Only
entry_Price = tkinter.Entry(frame4)
entry_Price.grid(padx=5, pady=5, row=2, column=1)


# List Box
def update_listbox():
    list1 = [f'Engine : {entry_engine.get()} CC',
             f'Power: {entry_engine.get()} bhp',
             f'Year: {entry_year.get()}']
    lst_box.delete(0, tkinter.END)
    for item in list1:
        lst_box.insert('end', item)


lst_box = tkinter.Listbox(frame3, height=5, font='Arial, 12')
lst_box.grid(column=1, row=2, pady=0, padx=10)
update_listbox()


# Commands
def return_prediction():
    entry_Price.configure(state='normal')
    entry_Price.delete(0, tkinter.END)
    entry_Price.insert(tkinter.END, f'$ {predict_price(entry_year.get(), entry_engine.get(), entry_power.get())}')
    entry_Price.configure(state='readonly')


# Buttons
input_data = tkinter.Button(frame2, font='Arial, 12', text='Input Data', command=update_listbox)
input_data.grid(column=1, row=4, pady=5, padx=5)
predict = tkinter.Button(frame4, font='Arial, 12', text='Calculate Price', command=return_prediction)
predict.grid(column=1, row=3, pady=5, padx=5)
# Main Loop
root.mainloop()
