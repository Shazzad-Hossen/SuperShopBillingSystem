from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Super Shop Billing System")
        bg_color="#D4E157"
        title=Label(self.root,text="Super Shop Billing System",bd=12,relief=GROOVE,fg="white",bg=bg_color,font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #==========Variables=============================================================================================================
        #==========cosmetics===============
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_spray=IntVar()
        self.hair_gell=IntVar()
        self.body_losan=IntVar()
        #=========Grocery=============
        self.rice=IntVar()
        self.oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        #==========Cold Drinks==============
        self.coca_cola=IntVar()
        self.seven_up=IntVar()
        self.sprite=IntVar()
        self.pepsi=IntVar()
        self.pran_frooto=IntVar()
        self.frutika=IntVar()
        #=========Total Product Price and Vat Variable=============
        self.cosmetics_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drinks_price=StringVar()


        self.cosmetics_vat=StringVar()
        self.grocery_vat=StringVar()
        self.cold_drinks_vat=StringVar()


        #========= Customer================

        self.c_name=StringVar()
        self.c_phone=StringVar()

        self.bill_no=StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()














        #Customer Details Frame=================================================================================
        F1=LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),fg="#E65100",bg=bg_color)
        F1.place(x=0,y=70,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="#4E342E",font=("times new roman",15,"bold")).grid(row=0,column=0,pady=5)
        cname_text=Entry(F1,width=20,textvariable=self.c_name,font="arial 15",bd=2,relief=SOLID).grid(row=0,column=1,pady=5)

        cphn_lbl = Label(F1, text="Customer Phone No", bg=bg_color, fg="#4E342E",font=("times new roman", 15, "bold")).grid(row=0, column=2, pady=5)
        cphntext = Entry(F1, width=20,textvariable=self.c_phone, font="arial 15", bd=2, relief=SOLID).grid(row=0, column=3, pady=5)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="#4E342E",font=("times new roman", 15, "bold")).grid(row=0, column=4, pady=5)
        c_bill_text = Entry(F1, width=20, textvariable=self.search_bill,font="arial 15", bd=2, relief=SOLID).grid(row=0, column=5, pady=5)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=2,font="arial 12 bold").grid(row=0,column=6,padx=70,pady=10)

        #Cosmetics Details Frame=========================================================================================================================================
        F2 = LabelFrame(self.root, text="Cosmetics", font=("times new roman", 15, "bold"), fg="#E65100",bg=bg_color)
        F2.place(x=1, y=150, height=380,width=280)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=0,column=0,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="#4E342E").grid(row=1, column=0, pady=10, sticky="w")
        Face_cream_txt = Entry(F2,textvariable=self.face_cream , width=10, font=("times new roman", 16, "bold"), bd=2, relief=SOLID).grid(row=1, column=1,padx=10, pady=10)


        Face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="#4E342E").grid(row=2, column=0, pady=10, sticky="w")
        Face_w_txt = Entry(F2, width=10,textvariable=self.face_wash , font=("times new roman", 16, "bold"), bd=2, relief=SOLID).grid(row=2, column=1,padx=10, pady=10)

        Hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="#4E342E").grid(row=3, column=0, pady=10, sticky="w")
        Hair_s_txt = Entry(F2, width=10,textvariable=self.hair_spray , font=("times new roman", 16, "bold"), bd=2, relief=SOLID).grid(row=3, column=1,padx=10, pady=10)

        Hair_g_lbl = Label(F2, text="Hair Gell", font=("times new roman", 16, "bold"), bg=bg_color, fg="#4E342E").grid(row=4, column=0, pady=10, sticky="w")
        Hair_g_txt = Entry(F2, width=10, textvariable=self.hair_gell ,font=("times new roman", 16, "bold"), bd=2, relief=SOLID).grid(row=4, column=1,padx=10, pady=10)



        Body_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color, fg="#4E342E").grid(row=5, column=0, pady=10, sticky="w")
        Body_lbl_txt = Entry(F2, width=10,textvariable=self.body_losan , font=("times new roman", 16, "bold"), bd=2, relief=SOLID).grid(row=5, column=1,padx=10, pady=10)

        #Grocery Product Details Frame======================================================================================================================================
        F3 = LabelFrame(self.root, text="Grocery", font=("times new roman", 15, "bold"), fg="#E65100",bg=bg_color)
        F3.place(x=281, y=150, height=380,width=280)

        g1_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=0,column=0,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice ,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl = Label(F3, text="Oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="#4E342E").grid(row=1, column=0, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.oil ,font=("times new roman", 16, "bold"), bd=2, relief=SOLID).grid(row=1, column=1,padx=10, pady=10)


        g3_lbl = Label(F3, text="Daal ", font=("times new roman", 16, "bold"), bg=bg_color, fg="#4E342E").grid(row=2, column=0, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10,textvariable=self.daal , font=("times new roman", 16, "bold"), bd=2, relief=SOLID).grid(row=2, column=1,padx=10, pady=10)

        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color, fg="#4E342E").grid(row=3, column=0, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10,textvariable=self.wheat , font=("times new roman", 16, "bold"), bd=2, relief=SOLID).grid(row=3, column=1,padx=10, pady=10)

        g5_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="#4E342E").grid(row=4, column=0, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10,textvariable=self.sugar , font=("times new roman", 16, "bold"), bd=2, relief=SOLID).grid(row=4, column=1,padx=10, pady=10)



        g6_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color, fg="#4E342E").grid(row=5, column=0, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10, textvariable=self.tea ,font=("times new roman", 16, "bold"), bd=2, relief=SOLID).grid(row=5, column=1,padx=10, pady=10)

        #Cold Drinks Details Frame=====================================================================================================================================================
        F4 = LabelFrame(self.root, text="Cold Drinks", font=("times new roman", 15, "bold"), fg="#E65100",bg=bg_color)
        F4.place(x=561, y=150, height=380,width=280)

        c1_lbl = Label(F4,text="Coca Cola",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=0,column=0,pady=10,sticky="w")
        c1_txt = Entry(F4,width=10,textvariable=self.coca_cola ,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl = Label(F4, text="7up", font=("times new roman", 16, "bold"), bg=bg_color, fg="#4E342E").grid(row=1, column=0, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10,textvariable=self.seven_up , font=("times new roman", 16, "bold"), bd=2, relief=SOLID).grid(row=1, column=1,padx=10, pady=10)


        c3_lbl = Label(F4, text="Sprite ", font=("times new roman", 16, "bold"), bg=bg_color, fg="#4E342E").grid(row=2, column=0, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10,textvariable=self.sprite , font=("times new roman", 16, "bold"), bd=2, relief=SOLID).grid(row=2, column=1,padx=10, pady=10)

        c4_lbl = Label(F4, text="Pepsi", font=("times new roman", 16, "bold"), bg=bg_color, fg="#4E342E").grid(row=3, column=0, pady=10, sticky="w")
        c4_txt = Entry(F4, width=10,textvariable=self.pepsi , font=("times new roman", 16, "bold"), bd=2, relief=SOLID).grid(row=3, column=1,padx=10, pady=10)

        c5_lbl = Label(F4, text="Pran Frooto", font=("times new roman", 16, "bold"), bg=bg_color, fg="#4E342E").grid(row=4, column=0, pady=10, sticky="w")
        c5_txt = Entry(F4, width=10,textvariable=self.pran_frooto , font=("times new roman", 16, "bold"), bd=2, relief=SOLID).grid(row=4, column=1,padx=10, pady=10)



        c6_lbl = Label(F4, text="Frutika", font=("times new roman", 16, "bold"), bg=bg_color, fg="#4E342E").grid(row=5, column=0, pady=10, sticky="w")
        c6_txt = Entry(F4, width=10, textvariable=self.frutika ,font=("times new roman", 16, "bold"), bd=2, relief=SOLID).grid(row=5, column=1,padx=10, pady=10)

        # Bill Area=====================================================================================================================================

        F5 = Frame(self.root, bd=2, relief=SOLID)
        F5.place(x=841, y=150, height=380,width=508)
        bill_title=Label(F5,text="Bill Area",font="ariel 15 bold",bd=1,relief=SOLID).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #Bottom Frame==============================================================================================================
        F6 = LabelFrame(self.root, text="Bill Menu", font=("times new roman", 15, "bold"), fg="#E65100", bg=bg_color)
        F6.place(x=1, y=530, height=170, relwidth=1)
        m1_lbl=Label(F6,text="Total Cosmetics Price",bg=bg_color,fg="#283593",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetics_price ,font="arial 10 bold",bd=2,relief=SOLID).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="#283593",font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price ,font="arial 10 bold", bd=2, relief=SOLID).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", bg=bg_color, fg="#283593",font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18,textvariable=self.cold_drinks_price , font="arial 10 bold", bd=2, relief=SOLID).grid(row=2, column=1, padx=10, pady=1)


        c1_lbl=Label(F6,text=" Cosmetics Vat",bg=bg_color,fg="#283593",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetics_vat ,font="arial 10 bold",bd=2,relief=SOLID).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl = Label(F6, text=" Grocery Vat", bg=bg_color, fg="#283593",font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18,textvariable=self.grocery_vat , font="arial 10 bold", bd=2, relief=SOLID).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text=" Cold Drinks Vat", bg=bg_color, fg="#283593",font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18,textvariable=self.cold_drinks_vat , font="arial 10 bold", bd=2, relief=SOLID).grid(row=2, column=3, padx=10, pady=1)

        btn_F= Frame(F6,bd=2,relief=SOLID)
        btn_F.place(x=750,width=580, height=105)



        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",pady=27,width=10,font="arial 14 bold").grid(row=0,column=0,padx=5,pady=5)
        gbill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=27,width=13,font="arial 14 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",pady=27,width=9,font="arial 14 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",pady=27,width=9,font="arial 14 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        self.c_s  =self.soap.get()*40
        self.c_fc =self.face_cream.get() * 120
        self.c_fw =self.face_wash.get() * 60
        self.c_hg =self.hair_gell.get() * 140
        self.c_hs =self.hair_spray.get() * 180
        self.c_bl =self.body_losan.get() * 180
        self.total_cosmetics_price=float(self.c_s +self.c_fc +self.c_fw +self.c_hg +self.c_hs +self.c_bl)
        self.c_vat = round((self.total_cosmetics_price * 0.05), 2)
        self.cosmetics_price.set(str(self.total_cosmetics_price)+"\tBDT")
        self.cosmetics_vat.set(str(round((self.total_cosmetics_price * 0.05), 2)) + "\tBDT")


        self.g_r=self.rice.get() * 80
        self.g_o=self.oil.get() * 180
        self.g_d=self.daal.get() * 60
        self.g_w=self.wheat.get() * 240
        self.g_s=self.sugar.get() * 45
        self.g_t=self.tea.get() * 250



        self.total_grocery_price = float(self.g_r+self.g_o+self.g_d+self.g_w+self.g_s+self.g_t)

        self.gr_vat = round((self.total_grocery_price * 0.05), 2)
        self.grocery_price.set(str(self.total_grocery_price)+"\tBDT")
        self.grocery_vat.set(str(round((self.total_grocery_price * 0.05), 2)) + "\tBDT")

        self.cd_c=self.coca_cola.get() * 60
        self.cd_7=self.seven_up.get() * 60
        self.cd_s=self.sprite.get() * 50
        self.cd_p=self.pepsi.get() * 45
        self.cd_pf=self.pran_frooto.get() * 40
        self.cd_f=self.frutika.get() * 65
        self.total_cold_drinks_price = float(self.cd_c + self.cd_7 + self.cd_s + self.cd_p + self.cd_pf + self.cd_f )


        self.cd_vat=round((self.total_cold_drinks_price * 0.05),2)
        self.cold_drinks_price.set( str(self.total_cold_drinks_price)+"\tBDT")
        self.cold_drinks_vat.set(str(round((self.total_cold_drinks_price * 0.05),2))+"\tBDT")

        self.Total_bill=float(
            self.total_cosmetics_price+
            self.total_grocery_price+
            self.total_cold_drinks_price+
            self.gr_vat+
            self.c_vat+
            self.cd_vat
                              )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\tSuper Shop Billing System\n\n")
        self.txtarea.insert(END,f"\n Bill Number    : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name  : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone No       : {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n============================================================")
        self.txtarea.insert(END, f"\n Product\t\t\tQTY\t\t\tPrice")
        self.txtarea.insert(END, f"\n============================================================")





    def bill_area(self):
        if self.c_name.get()=="" or  self.c_phone.get()=="":
            messagebox.showerror("Error","Customer Name and Phone No.  field can't be empty")
        elif self.cosmetics_price.get()=="0.0\tBDT" and self.grocery_price.get()=="0.0\tBDT" and self.cold_drinks_price.get()=="0.0\tBDT":
            messagebox.showerror("Error", "No Product has been selected")

        else:
            self.welcome_bill()

            if self.soap.get() != 0:
                self.txtarea.insert(END, f" \n Bath Soap\t\t\t{self.soap.get()}\t\t\t{self.c_s}\tBDT")
            if self.face_cream.get() != 0:
                self.txtarea.insert(END, f" \n Face Cream\t\t\t{self.face_cream.get()}\t\t\t{self.c_fc}\tBDT")
            if self.face_wash.get() != 0:
                self.txtarea.insert(END, f" \n Face Wash\t\t\t{self.face_wash.get()}\t\t\t{self.c_fw}\tBDT")
            if self.hair_gell.get() != 0:
                self.txtarea.insert(END, f" \n Hair Gell\t\t\t{self.hair_gell.get()}\t\t\t{self.c_hg}\tBDT")
            if self.hair_spray.get() != 0:
                self.txtarea.insert(END, f" \n Hair Spray\t\t\t{self.hair_spray.get()}\t\t\t{self.c_hs}\tBDT")
            if self.body_losan.get() != 0:
                self.txtarea.insert(END, f" \n Body Lotion\t\t\t{self.body_losan.get()}\t\t\t{self.c_bl}\tBDT")

            if self.rice.get() != 0:
                self.txtarea.insert(END, f" \n Rice\t\t\t{self.rice.get()}\t\t\t{self.g_r}\tBDT")
            if self.oil.get() != 0:
                self.txtarea.insert(END, f" \n Oil\t\t\t{self.oil.get()}\t\t\t{self.g_o}\tBDT")
            if self.daal.get() != 0:
                self.txtarea.insert(END, f" \n Daal\t\t\t{self.daal.get()}\t\t\t{self.g_d}\tBDT")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f" \n Wheat\t\t\t{self.wheat.get()}\t\t\t{self.g_w}\tBDT")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f" \n Sugar\t\t\t{self.sugar.get()}\t\t\t{self.g_s}\tBDT")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f" \n Tea\t\t\t{self.tea.get()}\t\t\t{self.g_t}\tBDT")

            if self.coca_cola.get() != 0:
                self.txtarea.insert(END, f" \n Coca Cola\t\t\t{self.coca_cola.get()}\t\t\t{self.cd_c}\tBDT")
            if self.seven_up.get() != 0:
                self.txtarea.insert(END, f" \n Seven Up\t\t\t{self.seven_up.get()}\t\t\t{self.cd_7}\tBDT")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f" \n Sprite\t\t\t{self.sprite.get()}\t\t\t{self.cd_s}\tBDT")
            if self.pepsi.get() != 0:
                self.txtarea.insert(END, f" \n Pepsi\t\t\t{self.pepsi.get()}\t\t\t{self.cd_p}\tBDT")
            if self.pran_frooto.get() != 0:
                self.txtarea.insert(END, f" \n Pran Frooto\t\t\t{self.pran_frooto.get()}\t\t\t{self.cd_pf}\tBDT")
            if self.frutika.get() != 0:
                self.txtarea.insert(END, f" \n Frutika\t\t\t{self.frutika.get()}\t\t\t{self.cd_f}\tBDT")

            self.txtarea.insert(END, f"\n____________________________________________________________")
            if self.cosmetics_vat.get() != "0.0\tBDT":
                self.txtarea.insert(END, f"\n Cosmetic Vat\t\t\t\t\t\t{self.cosmetics_vat.get()}")
            if self.grocery_vat.get() != "0.0\tBDT":
                self.txtarea.insert(END, f"\n Grocery Vat\t\t\t\t\t\t{self.grocery_vat.get()}")
            if self.cold_drinks_vat.get() != "0.0\tBDT":
                self.txtarea.insert(END, f"\n Cold Drinks Vat\t\t\t\t\t\t{self.cold_drinks_vat.get()}")
            self.txtarea.insert(END, f"\n____________________________________________________________")
            self.txtarea.insert(END, f"\n\n Total Bill\t\t\t\t\t\t{self.Total_bill}\tBDT")
            self.txtarea.insert(END, f"\n____________________________________________________________")
            self.save_bill()


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data = self.txtarea.get('1.0',END)
            f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f" bill No. {self.bill_no.get()} saved successfully")
        else:
            return



    def find_bill(self):
        present="no"

        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:

                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"

        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to clear data?")
        if op>0:
            # ==========cosmetics===============
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_spray.set(0)
            self.hair_gell.set(0)
            self.body_losan.set(0)
            # =========Grocery=============
            self.rice.set(0)
            self.oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            # ==========Cold Drinks==============
            self.coca_cola.set(0)
            self.seven_up.set(0)
            self.sprite.set(0)
            self.pepsi.set(0)
            self.pran_frooto.set(0)
            self.frutika.set(0)
            # =========Total Product Price and Vat Variable=============
            self.cosmetics_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.cosmetics_vat.set("")
            self.grocery_vat.set("")
            self.cold_drinks_vat.set("")

            # ========= Customer================

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()



    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()



root=Tk()
obj=Bill_App(root)
root.mainloop()