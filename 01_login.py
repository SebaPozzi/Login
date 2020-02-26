# Programa para crear usuario y logearse #import tkinter
from tkinter import *
from tkinter import messagebox

def Click_Ace(EntUsu,EntCon):
    if Control_Null(EntUsu,"usuario")==True:
        return
    if Control_Null(EntCon,"contraseña")==True:
        return
    try:
        f= open("usuarios.txt","r")
    except IOError:
        messagebox.showinfo("","El usuario ingresado no existe")
        return
    LisLin = list(f.readlines())
    f.close()
    UsuExi=0
    for n in range(0,len(LisLin),2):
        if LisLin[n].lower().strip()==EntUsu.get().lower().strip():
            UsuExi=1
    if UsuExi==0:
        messagebox.showinfo("","El usuario ingresado no existe")
    else:
        if LisLin[n+1].lower().strip()!=EntCon.get().lower().strip():
            messagebox.showinfo("","La contraseña ingresada no es correcta")
        else:
            messagebox.showinfo("","Bienvenido al sistema")
    
def Click_Cre():
    WinCre =Toplevel()
    WinCre.title("Crear usuario nuevo")
    WinCre.configure(background="mint cream")
    Cre_Nue_Prompt(WinCre)

def Log_In_Prompt():
    LabUsu = Label(root, text="Usuario",anchor="w",width=40)
    LabUsu.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    LabUsu.config(font=("Consolas", 12), bg="mint cream", fg="medium blue")

    EntUsu = Entry(root, width=20, bg="white")
    EntUsu.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
    EntUsu.config(font=("Consolas", 12),width=40)

    LabCon = Label(root, text="Contraseña",anchor="w",width=40)
    LabCon.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
    LabCon.config(font=("Consolas", 12), bg="mint cream", fg="medium blue")

    EntCon = Entry(root, width=20, bg="white", show="●")
    EntCon.grid(row=4, column=0, padx=10, pady=10, columnspan=2)
    EntCon.config(font=("Consolas", 12),width=40)

    ButAce = Button(root, text="Aceptar", width=7, command=lambda: Click_Ace(EntUsu,EntCon))
    ButAce.grid(row=5, column=0,padx=10, pady=10)

    ButCre = Button(root, text="Crear usuario", width=13, command=Click_Cre)
    ButCre.grid(row=5, column=1,padx=10, pady=10)

def Cre_Nue_Prompt(WinCre):
    LabUsuNue = Label(WinCre, text="Genere su nombre de usuario",anchor="w",width=40)
    LabUsuNue.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    LabUsuNue.config(font=("Consolas", 12), bg="mint cream", fg="medium blue")

    EntUsuNue = Entry(WinCre, width=20, bg="white")
    EntUsuNue.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
    EntUsuNue.config(font=("Consolas", 12),width=40)

    EntUsuNue.focus_set()

    LabConNue1 = Label(WinCre, text="Genere una contraseña",anchor="w",width=40)
    LabConNue1.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
    LabConNue1.config(font=("Consolas", 12), bg="mint cream", fg="medium blue")

    EntConNue1 = Entry(WinCre, width=20, bg="white", show="●")
    EntConNue1.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
    EntConNue1.config(font=("Consolas", 12),width=40)

    LabConNue2 = Label(WinCre, text="Repita su contraseña",anchor="w",width=40)
    LabConNue2.grid(row=4, column=0, padx=10, pady=10, columnspan=2)
    LabConNue2.config(font=("Consolas", 12), bg="mint cream", fg="medium blue")

    EntConNue2 = Entry(WinCre, width=20, bg="white", show="●")
    EntConNue2.grid(row=5, column=0, padx=10, pady=10, columnspan=2)
    EntConNue2.config(font=("Consolas", 12),width=40)

    ButAceNue = Button(WinCre, text="Aceptar", width=7, command=lambda: Click_Ace_Nue(EntUsuNue,EntConNue1,EntConNue2,WinCre))
    ButAceNue.grid(row=6, column=0,padx=10, pady=10,columnspan=2)

    #WinCre.focusforce()

def Click_Ace_Nue(EntUsuNue,EntConNue1,EntConNue2,WinCre):
    if Control_Null(EntUsuNue,"usuario")==True:
        return
    if Control_Null(EntConNue1,"contraseña")==True:
        return
    if Control_Null(EntConNue2,"validación de contraseña")==True:
        return
    UsuExi=0
    try:
        f= open("usuarios.txt","r")
        existe=True
        #Comparar el usuario con los existentes
        LisLin = list(f.readlines())
        for n in range(0,len(LisLin),2):
            if LisLin[n].lower().strip()==EntUsuNue.get().lower().strip():
                UsuExi=1
        f.close()
    except IOError:
        existe=False
    if UsuExi==1:
        messagebox.showinfo("","El usuario ingresado ya existe")
        return
    #Chequear los requisitos de la contraseña
    if len(EntConNue1.get())<4:
        messagebox.showinfo("","La contraseña debe tener al menos cuatro caracteres")
        return
    #Comparar las dos contraseñas entre sí
    if EntConNue1.get().lower().strip()!=EntConNue2.get().lower().strip():
        messagebox.showinfo("","Las dos entradas de la contraseña deben coincidir")
        return
    #Crear el usuario
    if existe == 0:
        f= open("usuarios.txt","w+")
        f.write(EntUsuNue.get())
        f.write("\n" + EntConNue1.get())
    else:
        f= open("usuarios.txt","a+")
        f.write("\n" + EntUsuNue.get())
        f.write("\n" + EntConNue1.get())
    WinCre.destroy()
    messagebox.showinfo("","El usuario ha sido creado")
        #EntUsu.focus_set()

def Control_Null(ent,txt):
    if ent.get() == "":
        messagebox.showinfo("Error","No ha ingresado " + txt)
        return True
    else:
        return False


# MAIN ALGORITHM
root = Tk()
root.title("Log In")
root.configure(background="mint cream")

Log_In_Prompt()

root.mainloop()