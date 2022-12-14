#import modules

from tkinter import *
import os
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x450")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
    
    logo = PhotoImage(file=r"register.gif")
    Label(register_screen,text="").pack()
    Label(register_screen, image=logo).pack()
    mainloop()
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x450")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

    logo = PhotoImage(file=r"login.gif")
    Label(login_screen,text="").pack()
    Label(login_screen, image=logo).pack()
    mainloop()
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
    
    file = open(username_info+".txt", "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
# Implementing event on login button
check_login=0
username1=""
def login_verify():
    global username1
    global check_login
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if (username1+".txt") in list_of_files:
        file1 = open(username1+".txt", "r")
        verify = file1.read().splitlines()
        file1.close()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global check_login
    check_login=1
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("250x300")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=main_screen.destroy).pack()

    logo = PhotoImage(file=r"login_successful.gif")
    Label(login_success_screen,text="").pack()
    Label(login_success_screen, image=logo).pack()
    mainloop()
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Oops")
    password_not_recog_screen.geometry("250x450")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

    logo = PhotoImage(file=r"login_unsuccessful.gif")
    Label(password_not_recog_screen,text="").pack()
    Label(password_not_recog_screen, image=logo).pack()
    mainloop()
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Oops")
    user_not_found_screen.geometry("250x300")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

    logo = PhotoImage(file=r"login_unsuccessful.gif")
    Label(user_not_found_screen,text="").pack()
    Label(user_not_found_screen, image=logo).pack()
    mainloop()
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x300")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    logo = PhotoImage(file=r"welcome.gif")
    Label(main_screen,text="").pack()
    Label(main_screen, image=logo).pack()
    mainloop()
    
main_account_screen()

if check_login==1:
    from tkinter import *
    import time
    import datetime
    import random

    root =Tk()
    root.geometry("1350x750+0+0")
    root.title("Food Billing System")
    root.configure(background='blue')

    Tops = Frame(root,bg='blue',bd=20,pady=5,relief=RIDGE)
    Tops.pack(side=TOP)

    lblTitle=Label(Tops,font=('arial',60,'bold'),text='Food Billing System',bd=21,bg='orange',
                    fg='cornsilk',justify=CENTER)
    lblTitle.grid(row=0)


    ReceiptCal_F = Frame(root,bg='blue',bd=10,relief=RIDGE)
    ReceiptCal_F.pack(side=RIGHT)

    Buttons_F=Frame(ReceiptCal_F,bg='blue',bd=3,relief=RIDGE)
    Buttons_F.pack(side=BOTTOM)

    Cal_F=Frame(ReceiptCal_F,bg='orange',bd=6,relief=RIDGE)
    Cal_F.pack(side=TOP)

    Receipt_F=Frame(ReceiptCal_F,bg='orange',bd=4,relief=RIDGE)
    Receipt_F.pack(side=BOTTOM)

    MenuFrame = Frame(root,bg='orange',bd=10,relief=RIDGE)
    MenuFrame.pack(side=LEFT)
    Cost_F=Frame(MenuFrame,bg='orange',bd=4)
    Cost_F.pack(side=BOTTOM)
    Fruit_F=Frame(MenuFrame,bg='orange',bd=4)
    Fruit_F.pack(side=TOP)


    Fruit_F=Frame(MenuFrame,bg='orange',bd=4,relief=RIDGE)
    Fruit_F.pack(side=LEFT)
    Veg_F=Frame(MenuFrame,bg='orange',bd=4,relief=RIDGE)
    Veg_F.pack(side=RIGHT)
    ###################################################variables################################################

    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5=IntVar()
    var6=IntVar()
    var7=IntVar()
    var8=IntVar()
    var9=IntVar()
    var10=IntVar()
    var11=IntVar()
    var12=IntVar()
    var13=IntVar()
    var14=IntVar()
    var15=IntVar()
    var16=IntVar()

    DateofOrder = StringVar()
    Receipt_Ref = StringVar()
    PaidTax = StringVar()
    SubTotal = StringVar()
    TotalCost = StringVar()
    CostofVeg = StringVar()
    CostofFruit = StringVar()
    ServiceCharge = StringVar()

    text_Input = StringVar()
    operator = ""

    E_Grape = StringVar()
    E_Apple = StringVar()
    E_Strawberry = StringVar()
    E_Orange = StringVar()
    E_Pomogranete= StringVar()
    E_Mango = StringVar()
    E_Pineapple= StringVar()
    E_Lemon = StringVar()

    E_Tomato = StringVar()
    E_Broccoli = StringVar()
    E_Cauliflower = StringVar()
    E_Cabbage = StringVar()
    E_Carrot = StringVar()
    E_Potato = StringVar()
    E_Betroot = StringVar()
    E_Ladiesfinger = StringVar()

    E_Grape.set("0")
    E_Apple.set("0")
    E_Strawberry.set("0")
    E_Orange.set("0")
    E_Pomogranete.set("0")
    E_Mango.set("0")
    E_Pineapple.set("0")
    E_Lemon.set("0")

    E_Tomato.set("0")
    E_Broccoli.set("0")
    E_Cauliflower.set("0")
    E_Cabbage.set("0")
    E_Carrot.set("0")
    E_Potato.set("0")
    E_Betroot.set("0")
    E_Ladiesfinger.set("0")

    DateofOrder.set(time.strftime("%d/%m/%y"))

    ##########################################Function Declaration####################################################
    import tkinter
    def iExit():
        iExit=messagebox.askyesno("Exit Billing System","Confirm if you want to exit")
        if iExit > 0:
            root.destroy()
            return

    def Reset():

        PaidTax.set("")
        SubTotal.set("")
        TotalCost.set("")
        CostofVeg.set("")
        CostofFruit.set("")
        ServiceCharge.set("")
        txtReceipt.delete("1.0",END)


        E_Grape.set("0")
        E_Apple.set("0")
        E_Strawberry.set("0")
        E_Orange.set("0")
        E_Pomogranete.set("0")
        E_Mango.set("0")
        E_Pineapple.set("0")
        E_Lemon.set("0")

        E_Tomato.set("0")
        E_Broccoli.set("0")
        E_Cauliflower.set("0")
        E_Cabbage.set("0")
        E_Carrot.set("0")
        E_Potato.set("0")
        E_Betroot.set("0")
        E_Ladiesfinger.set("0")

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)

        DateofOrder.set(time.strftime("%d/%m/%y"))

        txtGrape.configure(state=DISABLED)
        txtApple.configure(state=DISABLED)
        txtStrawberry.configure(state=DISABLED)
        txtOrange.configure(state=DISABLED)
        txtPomogranete.configure(state=DISABLED)
        txtMango.configure(state=DISABLED)
        txtPineapple.configure(state=DISABLED)
        txtLemon.configure(state=DISABLED)
        txtTomato.configure(state=DISABLED)
        txtBroccoli.configure(state=DISABLED)
        txtCauliflower.configure(state=DISABLED)
        txtCabbage.configure(state=DISABLED)
        txtCarrot.configure(state=DISABLED)
        txtPotato.configure(state=DISABLED)
        txtBetroot.configure(state=DISABLED)
        txtLadiesfinger.configure(state=DISABLED)

    def CostofItem():
        Item1=float(E_Grape.get())
        Item2=float(E_Apple.get())
        Item3=float(E_Strawberry.get())
        Item4=float(E_Orange.get())
        Item5=float(E_Pomogranete.get())
        Item6=float(E_Mango.get())
        Item7=float(E_Pineapple.get())
        Item8=float(E_Lemon.get())
        Item9=float(E_Tomato.get())
        Item10=float(E_Broccoli.get())
        Item11=float(E_Cauliflower.get())
        Item12=float(E_Cabbage.get())
        Item13=float(E_Carrot.get())
        Item14=float(E_Potato.get())
        Item15=float(E_Betroot.get())
        Item16=float(E_Ladiesfinger.get())

        PriceofFruit =(Item1 * 13) + (Item2 * 10) + (Item3 * 20) + (Item4 * 10) + (Item5 * 11) + (Item6 * 17) + (Item7 * 14) + (Item8 * 8)

        PriceofVeg =(Item9 * 3) + (Item10 * 7) + (Item11 * 6) + (Item12 * 5) + (Item13 * 6) + (Item14 * 3) + (Item15 * 4) + (Item16 * 4)



        FruitPrice = "Rs",str('%.2f'%(PriceofFruit))
        VegPrice =  "Rs",str('%.2f'%(PriceofVeg))
        CostofVeg.set(VegPrice)
        CostofFruit.set(FruitPrice)
        SC = "Rs",str('%.2f'%(1.59))
        ServiceCharge.set(SC)

        SubTotalofITEMS = "Rs",str('%.2f'%(PriceofFruit + PriceofVeg + 1.59))
        SubTotal.set(SubTotalofITEMS)

        Tax = "Rs",str('%.2f'%((PriceofFruit + PriceofVeg + 1.59) * 0.15))
        PaidTax.set(Tax)

        TT=((PriceofFruit + PriceofVeg + 1.59) * 0.15)
        TC="Rs",str('%.2f'%(PriceofFruit + PriceofVeg + 1.59 + TT))
        TotalCost.set(TC)


    def chk_Grape():
        if(var1.get() == 1):
            txtGrape.configure(state = NORMAL)
            txtGrape.focus()
            txtGrape.delete('0',END)
            E_Grape.set("")
        elif(var1.get() == 0):
            txtGrape.configure(state = DISABLED)
            E_Grape.set("0")

    def chk_Apple():
        if(var2.get() == 1):
            txtApple.configure(state = NORMAL)
            txtApple.focus()
            txtApple.delete('0',END)
            E_Apple.set("")
        elif(var2.get() == 0):
            txtApple.configure(state = DISABLED)
            E_Apple.set("0")

    def chk_Strawberry():
        if(var3.get() == 1):
            txtStrawberry.configure(state = NORMAL)
            txtStrawberry.delete('0',END)
            txtStrawberry.focus()
        elif(var3.get() == 0):
            txtStrawberry.configure(state = DISABLED)
            E_Strawberry.set("0")

    def chk_Orange():
        if(var4.get() == 1):
            txtOrange.configure(state = NORMAL)
            txtOrange.delete('0',END)
            txtOrange.focus()
        elif(var4.get() == 0):
            txtOrange.configure(state = DISABLED)
            E_Orange.set("0")

    def chk_Pomogranete():
        if(var5.get() == 1):
            txtPomogranete.configure(state = NORMAL)
            txtPomogranete.delete('0',END)
            txtPomogranete.focus()
        elif(var5.get() == 0):
            txtPomogranete.configure(state = DISABLED)
            E_Pomogranete.set("0")

    def chk_Mango():
        if(var6.get() == 1):
            txtMango.configure(state = NORMAL)
            txtMango.delete('0',END)
            txtMango.focus()
        elif(var6.get() == 0):
            txtMango.configure(state = DISABLED)
            E_Mango.set("0")

    def chk_Pineapple():
        if(var7.get() == 1):
            txtPineapple.configure(state = NORMAL)
            txtPineapple.delete('0',END)
            txtPineapple.focus()
        elif(var7.get() == 0):
            txtPineapple.configure(state = DISABLED)
            E_Pineapple.set("0")

    def chk_Lemon():
        if(var8.get() == 1):
            txtLemon.configure(state = NORMAL)
            txtLemon.delete('0',END)
            txtLemon.focus()
        elif(var8.get() == 0):
            txtLemon.configure(state = DISABLED)
            E_Lemon.set("0")

    def chk_Tomato():
        if(var9.get() == 1):
            txtTomato.configure(state = NORMAL)
            txtTomato.delete('0',END)
            txtTomato.focus()
        elif(var9.get() == 0):
            txtTomato.configure(state = DISABLED)
            E_Tomato.set("0")

    def chk_Broccoli():
        if(var10.get() == 1):
            txtBroccoli.configure(state = NORMAL)
            txtBroccoli.delete('0',END)
            txtBroccoli.focus()
        elif(var10.get() == 0):
            txtBroccoli.configure(state = DISABLED)
            E_Broccoli.set("0")

    def chk_Cauliflower():
        if(var11.get() == 1):
            txtCauliflower.configure(state = NORMAL)
            txtCauliflower.delete('0',END)
            txtCauliflower.focus()
        elif(var11.get() == 0):
            txtCauliflower.configure(state = DISABLED)
            E_Cauliflower.set("0")

    def chk_Cabbage():
        if(var12.get() == 1):
            txtCabbage.configure(state = NORMAL)
            txtCabbage.delete('0',END)
            txtCabbage.focus()
        elif(var12.get() == 0):
            txtCabbage.configure(state = DISABLED)
            E_Cabbage.set("0")

    def chk_Carrot():
        if(var13.get() == 1):
            txtCarrot.configure(state = NORMAL)
            txtCarrot.delete('0',END)
            txtCarrot.focus()
        elif(var13.get() == 0):
            txtCarrot.configure(state = DISABLED)
            E_Carrot.set("0")

    def chk_Potato():
        if(var14.get() == 1):
            txtPotato.configure(state = NORMAL)
            txtPotato.delete('0',END)
            txtPotato.focus()
        elif(var14.get() == 0):
            txtPotato.configure(state = DISABLED)
            E_Potato.set("0")

    def chk_Betroot():
        if(var15.get() == 1):
            txtBetroot.configure(state = NORMAL)
            txtBetroot.delete('0',END)
            txtBetroot.focus()
        elif(var15.get() == 0):
            txtBetroot.configure(state = DISABLED)
            E_Betroot.set("0")

    def chk_Ladiesfinger():
        if(var16.get() == 1):
            txtLadiesfinger.configure(state = NORMAL)
            txtLadiesfinger.delete('0',END)
            txtLadiesfinger.focus()
        elif(var16.get() == 0):
            txtLadiesfinger.configure(state = DISABLED)
            E_Ladiesfinger.set("0")

    def Receipt():
        txtReceipt.delete("1.0",END)
        x=random.randint(10908,500876)
        randomRef= str(x)
        Receipt_Ref.set("Bill"+ randomRef)


        txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() +'\t'+ " "+DateofOrder.get() +'\n')
        txtReceipt.insert(END,'Items\t\t\t\t'+"Cost of Items \n")
        txtReceipt.insert(END,'Grape:\t\t\t\t\t' + E_Grape.get() +'\n')
        txtReceipt.insert(END,'Apple:\t\t\t\t\t'+ E_Apple.get()+'\n')
        txtReceipt.insert(END,'Strawberry:\t\t\t\t\t'+ E_Strawberry.get()+'\n')
        txtReceipt.insert(END,'Orange:\t\t\t\t\t'+ E_Orange.get()+'\n')
        txtReceipt.insert(END,'Pomogranete:\t\t\t\t\t'+ E_Pomogranete.get()+'\n')
        txtReceipt.insert(END,'Mango:\t\t\t\t\t'+ E_Mango.get()+'\n')
        txtReceipt.insert(END,'Pineapple:\t\t\t\t\t'+ E_Pineapple.get()+'\n')
        txtReceipt.insert(END,'Lemon:\t\t\t\t\t'+ E_Lemon.get()+'\n')
        txtReceipt.insert(END,'Tomato:\t\t\t\t\t'+ E_Tomato.get()+'\n')
        txtReceipt.insert(END,'Broccoli:\t\t\t\t\t'+ E_Broccoli.get()+'\n')
        txtReceipt.insert(END,'Cauliflower:\t\t\t\t\t'+ E_Cauliflower.get()+'\n')
        txtReceipt.insert(END,'Cabbage:\t\t\t\t\t'+ E_Cabbage.get()+'\n')
        txtReceipt.insert(END,'Carrot:\t\t\t\t\t'+ E_Carrot.get()+'\n')
        txtReceipt.insert(END,'Potato:\t\t\t\t\t'+ E_Potato.get()+'\n')
        txtReceipt.insert(END,'Betroot:\t\t\t\t\t'+ E_Betroot.get()+'\n')
        txtReceipt.insert(END,'Ladiesfinger:\t\t\t\t\t'+ E_Ladiesfinger.get()+'\n')
        txtReceipt.insert(END,'Cost of Fruits:\t\t\t\t\t'+ str(CostofFruit.get())+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
        txtReceipt.insert(END,'Cost of Veggies:\t\t\t\t'+ str(CostofVeg.get())+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
        txtReceipt.insert(END,'Service Charge:\t\t\t\t'+ ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")

        f=open(username1+".txt","a")
        f.write("\n")
        f.write("\n")
        f.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        f.write("\n")
        f.write('Receipt Ref:\t\t\t'+Receipt_Ref.get() +'\t'+ "  "+DateofOrder.get() +'\n')
        f.write("\n")
        f.write('Items\t\t\t\t'+"Cost of Items \n")
        f.write("\n")
        f.write('Grape:\t\t\t\t\t' + E_Grape.get() +'\n')
        f.write('Apple:\t\t\t\t\t'+ E_Apple.get()+'\n')
        f.write('Strawberry:\t\t\t'+"                  "+ E_Strawberry.get()+'\n')
        f.write('Orange:\t\t\t\t\t'+ E_Orange.get()+'\n')
        f.write('Pomogranete:\t\t\t'+"                  "+ E_Pomogranete.get()+'\n')
        f.write('Mango:\t\t\t\t\t'+ E_Mango.get()+'\n')
        f.write('Pineapple:\t\t\t\t\t'+ E_Pineapple.get()+'\n')
        f.write('Lemon:\t\t\t\t\t'+ E_Lemon.get()+'\n')
        f.write('Tomato:\t\t\t\t\t'+ E_Tomato.get()+'\n')
        f.write('Broccoli:\t\t\t\t\t'+ E_Broccoli.get()+'\n')
        f.write('Cauliflower:\t\t\t'+"                  "+ E_Cauliflower.get()+'\n')
        f.write('Cabbage:\t\t\t\t\t'+ E_Cabbage.get()+'\n')
        f.write('Carrot:\t\t\t\t\t'+ E_Carrot.get()+'\n')
        f.write('Potato:\t\t\t\t\t'+ E_Potato.get()+'\n')
        f.write('Ladiesfinger:\t\t\t'+"                  "+ E_Ladiesfinger.get()+'\n')
        f.write("\n")
        f.write('Service Charge:\t\t\t\t'+ ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")
        f.write("\n")
        f.close() 
    #########################################Fruit####################################################################
    Grape=Checkbutton(Fruit_F,text='Grape',variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                        bg='orange',command=chk_Grape).grid(row=0,sticky=W)
    Apple=Checkbutton(Fruit_F,text='Apple',variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                        bg='orange',command=chk_Apple).grid(row=1,sticky=W)
    Strawberry=Checkbutton(Fruit_F,text='Strawberry',variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                        bg='orange',command=chk_Strawberry).grid(row=2,sticky=W)
    Orange=Checkbutton(Fruit_F,text='Orange',variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                        bg='orange',command=chk_Orange).grid(row=3,sticky=W)
    Pomogranete=Checkbutton(Fruit_F,text='Pomogranete',variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                        bg='orange',command=chk_Pomogranete).grid(row=4,sticky=W)
    Mango=Checkbutton(Fruit_F,text='Mango',variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                        bg='orange',command=chk_Mango).grid(row=5,sticky=W)
    Pineapple=Checkbutton(Fruit_F,text='Pineapple',variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                        bg='orange',command=chk_Pineapple).grid(row=6,sticky=W)
    Lemon=Checkbutton(Fruit_F,text='Lemon',variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                        bg='orange',command=chk_Lemon).grid(row=7,sticky=W)
    ##############################################Fruit Entry###############################################################

    txtGrape = Entry(Fruit_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                            ,textvariable=E_Grape)
    txtGrape.grid(row=0,column=1)

    txtApple = Entry(Fruit_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                            ,textvariable=E_Apple)
    txtApple.grid(row=1,column=1)

    txtStrawberry = Entry(Fruit_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                            ,textvariable=E_Strawberry)
    txtStrawberry.grid(row=2,column=1)

    txtOrange= Entry(Fruit_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                            ,textvariable=E_Orange)
    txtOrange.grid(row=3,column=1)

    txtPomogranete = Entry(Fruit_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                            ,textvariable=E_Pomogranete)
    txtPomogranete.grid(row=4,column=1)

    txtMango = Entry(Fruit_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                            ,textvariable=E_Mango)
    txtMango.grid(row=5,column=1)

    txtPineapple = Entry(Fruit_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                            ,textvariable=E_Pineapple)
    txtPineapple.grid(row=6,column=1)

    txtLemon = Entry(Fruit_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                            ,textvariable=E_Lemon)
    txtLemon.grid(row=7,column=1)
    #############################################Veg######################################################################

    Tomato = Checkbutton(Veg_F,text="Tomato\t\t\t ",variable=var9,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='orange',command=chk_Tomato).grid(row=0,sticky=W)
    Broccoli = Checkbutton(Veg_F,text="Broccoli ",variable=var10,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='orange',command=chk_Broccoli).grid(row=1,sticky=W)
    Cauliflower = Checkbutton(Veg_F,text="Cauliflower ",variable=var11,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='orange',command=chk_Cauliflower).grid(row=2,sticky=W)
    Cabbage = Checkbutton(Veg_F,text="Cabbage ",variable=var12,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='orange',command=chk_Cabbage).grid(row=3,sticky=W)
    Carrot = Checkbutton(Veg_F,text="Carrot ",variable=var13,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='orange',command=chk_Carrot).grid(row=4,sticky=W)
    Potato = Checkbutton(Veg_F,text="Potato ",variable=var14,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='orange',command=chk_Potato).grid(row=5,sticky=W)
    Betroot = Checkbutton(Veg_F,text="Betroot ",variable=var15,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='orange',command=chk_Betroot).grid(row=6,sticky=W)
    Ladiesfinger = Checkbutton(Veg_F,text="Ladiesfinger ",variable=var16,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='orange',command=chk_Ladiesfinger).grid(row=7,sticky=W)
    ################################################Entry Box##########################################################
    txtTomato=Entry(Veg_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                            textvariable=E_Tomato)
    txtTomato.grid(row=0,column=1)

    txtBroccoli=Entry(Veg_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                            textvariable=E_Broccoli)
    txtBroccoli.grid(row=1,column=1)

    txtCauliflower=Entry(Veg_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                            textvariable=E_Cauliflower)
    txtCauliflower.grid(row=2,column=1)

    txtCabbage=Entry(Veg_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                            textvariable=E_Cabbage)
    txtCabbage.grid(row=3,column=1)

    txtCarrot=Entry(Veg_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                            textvariable=E_Carrot)
    txtCarrot.grid(row=4,column=1)

    txtPotato=Entry(Veg_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                            textvariable=E_Potato)
    txtPotato.grid(row=5,column=1)

    txtBetroot=Entry(Veg_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                            textvariable=E_Betroot)
    txtBetroot.grid(row=6,column=1)

    txtLadiesfinger=Entry(Veg_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                            textvariable=E_Ladiesfinger)
    txtLadiesfinger.grid(row=7,column=1)
    ###########################################ToTal Cost################################################################################
    lblCostofFruit=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Fruits\t',bg='orange',
                    fg='black',justify=CENTER)
    lblCostofFruit.grid(row=0,column=0,sticky=W)
    txtCostofFruit=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                            insertwidth=2,justify=RIGHT,textvariable=CostofFruit)
    txtCostofFruit.grid(row=0,column=1)

    lblCostofVeg=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Vegetables  ',bg='orange',
                    fg='black',justify=CENTER)
    lblCostofVeg.grid(row=1,column=0,sticky=W)
    txtCostofVeg=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                            insertwidth=2,justify=RIGHT,textvariable=CostofVeg)
    txtCostofVeg.grid(row=1,column=1)

    lblServiceCharge=Label(Cost_F,font=('arial',14,'bold'),text='Service Charge',bg='orange',
                    fg='black',justify=CENTER)
    lblServiceCharge.grid(row=2,column=0,sticky=W)
    txtServiceCharge=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                            insertwidth=2,justify=RIGHT,textvariable=ServiceCharge)
    txtServiceCharge.grid(row=2,column=1)
    ###########################################################Payment information###################################################

    lblPaidTax=Label(Cost_F,font=('arial',14,'bold'),text='\tPaid Tax',bg='orange',bd=7,
                    fg='black',justify=CENTER)
    lblPaidTax.grid(row=0,column=2,sticky=W)
    txtPaidTax=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                            insertwidth=2,justify=RIGHT,textvariable=PaidTax)
    txtPaidTax.grid(row=0,column=3)

    lblSubTotal=Label(Cost_F,font=('arial',14,'bold'),text='\tSub Total',bg='orange',bd=7,
                    fg='black',justify=CENTER)
    lblSubTotal.grid(row=1,column=2,sticky=W)
    txtSubTotal=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                            insertwidth=2,justify=RIGHT,textvariable=SubTotal)
    txtSubTotal.grid(row=1,column=3)

    lblTotalCost=Label(Cost_F,font=('arial',14,'bold'),text='\tTotal',bg='orange',bd=7,
                    fg='black',justify=CENTER)
    lblTotalCost.grid(row=2,column=2,sticky=W)
    txtTotalCost=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                            insertwidth=2,justify=RIGHT,textvariable=TotalCost)
    txtTotalCost.grid(row=2,column=3)

    #############################################RECEIPT###############################################################################
    txtReceipt=Text(Receipt_F,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
    txtReceipt.grid(row=0,column=0)


    ###########################################BUTTONS################################################################################
    btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Total',
                            bg='orange',command=CostofItem).grid(row=0,column=0)
    btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Receipt',
                            bg='orange',command=Receipt).grid(row=0,column=1)
    btnReset=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Reset',
                            bg='orange',command=Reset).grid(row=0,column=2)
    btnExit=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Exit',
                            bg='orange',command=iExit).grid(row=0,column=3)

    ###################################Calculator################################################################################




    def btnClick(numbers):
        global operator
        operator = operator + str(numbers)
        text_Input.set(operator)

    def btnClear():
        global operator
        operator = ""
        text_Input.set("")

    def btnEquals():
        try:
            global operator
            sumup = str(eval(operator))
            text_Input.set(sumup)
            operator = ""
        except:
            text_Input.set("error")
            operator=""



    txtDisplay=Entry(Cal_F,width=45,bg='white',bd=4,font=('arial',12,'bold'),justify=RIGHT,textvariable=text_Input)
    txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
    txtDisplay.insert(0,"0")


    btn7=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='7',
                            bg='orange',command=lambda:btnClick(7)).grid(row=2,column=0)
    btn8=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='8',
                            bg='orange',command=lambda:btnClick(8)).grid(row=2,column=1)
    btn9=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='9',
                            bg='orange',command=lambda:btnClick(9)).grid(row=2,column=2)
    btnAdd=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='+',
                            bg='orange',command=lambda:btnClick('+')).grid(row=2,column=3)

    btn4=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='4',
                            bg='orange',command=lambda:btnClick(4)).grid(row=3,column=0)
    btn5=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='5',
                            bg='orange',command=lambda:btnClick(5)).grid(row=3,column=1)
    btn6=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='6',
                            bg='orange',command=lambda:btnClick(6)).grid(row=3,column=2)
    btnSub=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='-',
                            bg='orange',command=lambda:btnClick('-')).grid(row=3,column=3)

    btn1=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='1',
                            bg='orange',command=lambda:btnClick(1)).grid(row=4,column=0)
    btn2=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='2',
                            bg='orange',command=lambda:btnClick(2)).grid(row=4,column=1)
    btn3=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='3',
                            bg='orange',command=lambda:btnClick(3)).grid(row=4,column=2)
    btnMulti=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='*',
                            bg='orange',command=lambda:btnClick('*')).grid(row=4,column=3)

    btn0=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='0',
                            bg='orange',command=lambda:btnClick(0)).grid(row=5,column=0)
    btnClear=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='C',
                            bg='orange',command=btnClear).grid(row=5,column=1)
    btnEqual=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='=',
                            bg='orange',command=btnEquals).grid(row=5,column=2)
    btnDiv=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='/',
                            bg='orange',command=lambda:btnClick('/')).grid(row=5,column=3)
    
    root.mainloop()
d={"Grape":[2,1,0,0,6,2,5,1],"Apple":[0,1,0,0,14,1,5,2],"Strawberry":[0,2,0,0,141,3,5],
       "Orange":[6,5,0,0,116,1,5,3],"Pomogranete":[0,1,0,0,15,2,5,3],"Mango":[73,4,0,0,204,3,20,8],
       "Pineapple":[2,2,0,0,132,3,10,5],"Lemon":[0,0,0,0,0,0,0,0],"Cherry":[26,2,0,0,17,2,0,2],
       "Guava":[21,3,0,0,628,2,10,9],"Tomato":[24,5,0,0,20,6,0,6],"Broccoli":[77,10,0,0,52,6,10,6],
       "Cauliflower":[0,0,0,0,0,0,0,0],"Cabbage":[23,43,0,0,772,28,45,34],
       "Carrot":[0,0,0,0,0,0,0,0],"Potato":[59,1,0,0,288,3,20,3],"Betroot":[1,1,0,0,7,4,5,5],
       "Ladiesfinger":[14,8,0,0,38,3,10,14],"Mushroom":[0,0,16,0,0,0,0,0],"Corn":[5,1,0,0,0,16,20,27]}

import matplotlib.pyplot as plt
import numpy as np
amount=[]
m=eval(input("list of eatables selected:"))
for i in m:
  s="amount of "+i+" bought:"
  amount.append(int(input(s)))

vita_a,cal,vita_d,vita_b12,vita_c,iron,vita_b6,magn=0,0,0,0,0,0,0,0
i=-1
for j in m:
  for k in d:
    if k==j:
      i+=1
      vita_a+=d[m[i]][0]*amount[i]*0.01
      cal=d[m[i]][1]*amount[i]*0.01
      vita_d+=d[m[i]][2]*amount[i]*0.01
      vita_b12+=d[m[i]][3]*amount[i]*0.01
      vita_c+=d[m[i]][4]*amount[i]*0.001
      iron+=d[m[i]][5]*amount[i]*0.01
      vita_b6+=d[m[i]][6]*amount[i]*0.01
      magn+=d[m[i]][7]*amount[i]*0.01  
valrd=[8,13,18,25,28,35,20,15]                            #vitamins and others required per week
valp=[vita_a,cal,vita_d,vita_b12,vita_c,iron,vita_b6,magn]
import matplotlib.pyplot as plt
x=np.arange(len(valp))
plt.bar(x,valp,color="red",width=0.35,label="amount of vitamin present")
plt.bar(x+0.35,valrd,color="blue",width=0.35,label="amount of vitamin required")
plt.xlabel("vitamins")
plt.ylabel("amounts")
plt.legend(loc="upper left")
plt.show()
import matplotlib.pyplot as plt
x=np.arange(len(valp))
plt.bar(x,valp,color="red",width=0.35,label="amount of vitamin present")
plt.bar(x+0.35,valrd,color="blue",width=0.35,label="amount of vitamin required")
plt.xlabel("vitamins")
plt.ylabel("amounts")
plt.legend(loc="upper left")
plt.show()

vits=["vita_a","cal","vita_d","vita_b12","vita_c","iron","vita_b6","magn"]
plt.bar(vits,valp,color=["red","b","g","k","yellow","purple","black","orange"])
plt.xlabel("NAME OF THE VITAMINS")
plt.ylabel("AMOUNT OF VITAMINS REQUIRED PER WEEK(IN MG)")
plt.show()

own=input("owner..access..")
if own=="password":
    weeks=["WEEK1","WEEK2","WEEK3","WEEK4","WEEK5"]
    month=input("month name:")+".txt"
    f=open(month,"r")
    profit=f.readlines()
    f.close()
    colr=["red","blue","green","purple","yellow"]
    plt.pie(profit,labels=weeks,colors=colr,autopct="%2.2f%%")
    plt.show()

    



    
