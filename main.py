from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install piLLOW
import random,os
from tkinter import messagebox
import tempfile
from time import strftime, time

class Bill_App:
    def __init__(self,root):
       self.root=root
       self.root.title("Timber Depot Billing Software")
       self.root.geometry("1530x800+0+0") 

       #=====================Variables=====================================================================================
       self.c_name=StringVar()
       self.c_phone=StringVar()
       self.invoice_no=StringVar()
       z=random.randint(1,9999)
       self.invoice_no.set(z)
       self.c_email=StringVar()
       self.search_bill=StringVar()
       self.product=StringVar()
       self.Height=IntVar()
       self.Size=IntVar()
       self.prices=IntVar()
       self.sqarefeet=IntVar()
       self.qty=IntVar()
       self.sub_total=StringVar()
       self.tax_input=StringVar()
       self.total=StringVar()

       #product Categories list
       self.Category=["Select Option","Teak","Neem","Jamun","Black Thuma","Nidra Ganneru","Saw Dust","Fire Wood"]
       self.subcatSawdust=["Select No Of Kg's","1kg","15kg","25kg","30kg"]
       self.price_1kg=1
       self.price_15kg=15
       self.price_25kg=25
       self.price_30kg=30
      
       self.subcatfirewood=["Select No Of Kg's","10kg","20kg","40kg","60kg"]
       self.fprice_10kg=30
       self.fprice_20kg=60
       self.fprice_40kg=120
       self.fprice_60kg=180
      
       self.Na=["Na"]
       self.subcatSizes=['Select size','5x4','5x3','4x3','5x1 1/2','13x1 1/2','9x1 1/2','4x1 3/4']
       self.subcatHeight=['Select Height','7','4','3','2','12']
      
       #image 1
       img=Image.open("C:\\Users\\V Kalyan\\OneDrive - Lovely Professional University\\PYTHON\\Python Project 1\\image\\ezgif-2-960a2f27a7de.gif")
       img=img.resize((500,130),Image.ANTIALIAS)
       self.photoimg=ImageTk.PhotoImage(img)
      
       lbl_img=Label(self.root,image=self.photoimg)
       lbl_img.place(x=0,y=0,width=500,height=130)
      
      
       #image 2
       img_1=Image.open("C:\\Users\\V Kalyan\\OneDrive - Lovely Professional University\\PYTHON\\python project\\image\\ezgif-2-37bb63f3ca12.gif")
       img_1=img_1.resize((500,130),Image.ANTIALIAS)
       self.photoimg_1=ImageTk.PhotoImage(img_1)
      
       lbl_img_1=Label(self.root,image=self.photoimg_1)
       lbl_img_1.place(x=500,y=0,width=500,height=130)
      

       #image 3
       img_2=Image.open("C:\\Users\\V Kalyan\\OneDrive - Lovely Professional University\\PYTHON\\python project\\image\\ezgif-2-7929970a8175.gif")
       img_2=img_2.resize((520,130),Image.ANTIALIAS)
       self.photoimg_2=ImageTk.PhotoImage(img_2)
      
       lbl_img_2=Label(self.root,image=self.photoimg_2)
       lbl_img_2.place(x=1000,y=0,width=520,height=130)
      
       lbl_title=Label(root,text="SKML TIMBER DEPOT AND SAW MILL",font=("times new roman",35,"bold"),bg="white",fg="red")
       lbl_title.place(x=0,y=130,width=1530,height=45)

       def time():
           string=strftime('%H:%M:%S %p')
           lbl.config(text=string)
           lbl.after(1000,time)

       lbl=Label(lbl_title,font=('times new roman',16,'bold'),background='white',foreground='blue')
       lbl.place(x=0,y=0,width=120,height=45)
       time()

       
      
       Main_Frame=Frame(root,bd=5,relief=GROOVE,bg="white")
       Main_Frame.place(x=0,y=175,width=1530,height=620)
      
       #customer LabelFrame
       cust_Frame=LabelFrame(Main_Frame,text="customer",font=("times new roman",12,"bold"),bg="white",fg="red")
       cust_Frame.place(x=10,y=5,width=350,height=140)
      
       lbl_mob=Label(cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
       lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)
      
       entry_mob=ttk.Entry(cust_Frame,textvariable=self.c_phone,font=("times new roman",10,"bold"),width=24)
       entry_mob.grid(row=0,column=1)
      
       lblCustName=Label(cust_Frame,text="Customer Name",font=('arial',12,'bold'),bg="white",bd=4)
       lblCustName.grid(row=1,column=0,stick=W,padx=5,pady=2)
      
       txtCustName=ttk.Entry(cust_Frame,textvariable=self.c_name,font=('arial',10,'bold'),width=24)
       txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)
      
      
       lblEmail=Label(cust_Frame,text="Email",font=('arial',12,'bold'),bg="white",bd=4)
       lblEmail.grid(row=2,column=0,stick=W,padx=5,pady=2)
      
       txtEmail=ttk.Entry(cust_Frame,textvariable=self.c_email,font=('arial',10,'bold'),width=24)
       txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
      
       #Product LabelFrame
       Product_Frame=LabelFrame(Main_Frame,text="product",font=("times new roman",12,"bold"),bg="white",fg="red")
       Product_Frame.place(x=370,y=5,width=620,height=140)
      
       #category
       self.lblCategory=Label(Product_Frame,text="Select Categories",font=('arial',12,'bold'),bg="white",bd=4)
       self.lblCategory.grid(row=0,column=0,stick=W,padx=5,pady=2)
      
       self.combo_Category=ttk.Combobox(Product_Frame,textvariable=self.product,value=self.Category,font=('arial',10,'bold'),width=24,state="readonly")
       self.combo_Category.current(0)
       self.combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
       self.combo_Category.bind("<<ComboboxSelected>>",self.categories)
    
       #Sizes
       self.lblSizes=Label(Product_Frame,text="Select Size",font=('arial',12,'bold'),bg="white",bd=4)
       self.lblSizes.grid(row=1,column=0,stick=W,padx=5,pady=2)
      
       self.comboSize=ttk.Combobox(Product_Frame,textvariable=self.Size,value=self.subcatSizes,font=('arial',10,'bold'),width=24,state="readonly")
       self.comboSize.current(0)
       self.comboSize.grid(row=1,column=1,sticky=W,padx=5,pady=2)
       self.comboSize.bind("<<ComboboxSelected>>",self.price)
      
       #Height
       self.lblHeight=Label(Product_Frame,text="Select Height",font=('arial',12,'bold'),bg="white",bd=4)
       self.lblHeight.grid(row=2,column=0,stick=W,padx=5,pady=2)
      
       self.comboHeight=ttk.Combobox(Product_Frame,textvariable=self.Height,value=self.subcatHeight,font=('arial',10,'bold'),width=24,state="readonly")
       self.comboHeight.current(0)
       self.comboHeight.grid(row=2,column=1,sticky=W,padx=5,pady=2)
      
       #Qty
       self.lblQty=Label(Product_Frame,text="Qty",font=('arial',12,'bold'),bg="white",bd=4)
       self.lblQty.grid(row=0,column=2,stick=W,padx=5,pady=2)
      
       self.comboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',10,'bold'),width=24)
       self.comboQty.grid(row=0,column=3,sticky=W,padx=5,pady=2)
      
       #Sqare Feet
       self.lblsqarefeet=Label(Product_Frame,text="ft^2",font=('arial',12,'bold'),bg="white",bd=4)
       self.lblsqarefeet.grid(row=1,column=2,stick=W,padx=5,pady=2)
      
       self.comboSqarefeet=ttk.Combobox(Product_Frame,textvariable=self.sqarefeet,font=('arial',10,'bold'),width=24,state="readonly")
       self.comboSqarefeet.grid(row=1,column=3,sticky=W,padx=5,pady=2)
       

       #Price
       self.lblprice=Label(Product_Frame,text="Price",font=('arial',12,'bold'),bg="white",bd=4)
       self.lblprice.grid(row=2,column=2,stick=W,padx=5,pady=2)
      
       self.comboprice=ttk.Combobox(Product_Frame,textvariable=self.prices,font=('arial',10,'bold'),width=24,state="readonly")
       self.comboprice.grid(row=2,column=3,sticky=W,padx=5,pady=2)

       #Middle Frame
       MiddleFrame=Frame(Main_Frame,bd=10)
       MiddleFrame.place(x=10,y=150,width=980,height=340)
      
       #image 4
       img_3=Image.open("C:\\Users\\V Kalyan\\OneDrive - Lovely Professional University\\PYTHON\\python project\\image\\ezgif-2-df8dc51c367f.gif")
       img_3=img_3.resize((490,340),Image.ANTIALIAS)
       self.photoimg_3=ImageTk.PhotoImage(img_3)
      
       lbl_img_3=Label(MiddleFrame,image=self.photoimg_3)
       lbl_img_3.place(x=0,y=0,width=490,height=340)
      
       #image 5
       img_4=Image.open("C:\\Users\\V Kalyan\\OneDrive - Lovely Professional University\\PYTHON\\python project\\image\\ezgif-2-c6f0df366335.gif")
       img_4=img_4.resize((490,340),Image.ANTIALIAS)
       self.photoimg_4=ImageTk.PhotoImage(img_4)
      
       lbl_img_4=Label(MiddleFrame,image=self.photoimg_4)
       lbl_img_4.place(x=490,y=0,width=500,height=340)
      
       #Search
       Search_Frame=Frame(Main_Frame,bd=2,bg="white")
       Search_Frame.place(x=1020,y=10,width=500,height=40)
      
       lblBill=Label(Search_Frame,font=('arial',12,'bold'),fg="white",bg="red",text="Bill Number")
       lblBill.grid(row=0,column=0,sticky=W,padx=1)
       
       txt_Entry_search=ttk.Entry(Search_Frame,font=('arial',10,'bold'),width=24)
       txt_Entry_search.grid(row=0,column=1,sticky=W,padx=2)
      
       Btnsearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
       Btnsearch.grid(row=0,column=2)
      
       #RightFrame Billing Area
       RightLabelFrame=LabelFrame(Main_Frame,text="Billing Area",font=("times new roman",12,"bold"),bg="white",fg="red")
       RightLabelFrame.place(x=1000,y=45,width=480,height=400)
      
       scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
       self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
       scroll_y.pack(side=RIGHT,fill=Y)
       scroll_y.config(command=self.textarea.yview)
       self.textarea.pack(fill=BOTH,expand=1)
      
       #Bill Counter LabelFrame
       Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
       Bottom_Frame.place(x=0,y=485,width=1520,height=125)
      
       lblSubTotal=Label(Bottom_Frame,text="Sub Total",font=('arial',12,'bold'),bg="white",bd=4)
       lblSubTotal.grid(row=0,column=0,stick=W,padx=5,pady=2)
      
       EntrySubTotal=ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=24)
       EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)
       
       lbl_tax=Label(Bottom_Frame,text="Gov Tax",font=('arial',12,'bold'),bg="white",bd=4)
       lbl_tax.grid(row=1,column=0,stick=W,padx=5,pady=2)
      
       txt_tax=ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=24)
       txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)
      
       lblAmountTotal=Label(Bottom_Frame,text="Total",font=('arial',12,'bold'),bg="white",bd=4)
       lblAmountTotal.grid(row=2,column=0,stick=W,padx=5,pady=2)
      
       txtAmountTotal=ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=24)
       txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)
      
       #Button Frame
       Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
       Btn_Frame.place(x=320,y=0)
      
       BtnAddtoCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To cart",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
       BtnAddtoCart.grid(row=0,column=0)
      
       Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
       Btngenerate_bill.grid(row=0,column=1)
      
       Btnsave=Button(Btn_Frame,command=self.Save_Bill,height=2,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
       Btnsave.grid(row=0,column=2)
      
       Btnprint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
       Btnprint.grid(row=0,column=3)
      
       Btnclear=Button(Btn_Frame,height=2,text="Clear",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
       Btnclear.grid(row=0,column=4)
      
       BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
       BtnExit.grid(row=0,column=5)
       self.welcome()

       self.l=[]
    #================Function Declaration===========================================
    def AddItem(self):
         Tax=1
         self.n=self.comboSize.get()
         self.m=self.comboHeight.get()
         self.k=self.qty.get()*self.m
         self.l.append(self.k)
         if self.product.get()=="":
               messagebox.showerror("Error","Please Select the product Name")
         else:
             self.textarea.insert(END ,f"\n{self.product.get()}\t\t{self.qty.get()}\t\t{self.k}")
             self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
             self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
             self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get=="":
             messagebox.showerror("Error","Please Add To cart product")
        else:
             text=self.textarea.get(10.0,(10.0+float(len(self.l))))
             self.welcome()
             self.textarea.insert(END,text)
             self.textarea.insert(END,"\n==================================================")
             self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
             self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
             self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.total.get()}")
             self.textarea.insert(END,"\n==================================================\n")



    def welcome(self):
          self.textarea.delete(1.0,END)
          self.textarea.insert(END,"\t WELCOME SKML TIMBER DEPOT")
          self.textarea.insert(END,f"\n Invoice Number:{self.invoice_no.get()}")
          self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
          self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
          self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

          self.textarea.insert(END,"\n==================================================")
          self.textarea.insert(END,f"\n Products\t\t\tft^2\t\tPrice")
          self.textarea.insert(END,"\n==================================================\n")

    def Save_Bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill ")
        if op>0:
            self.invoice_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.invoice_no.get())+".txt",'w')
            f1.write(self.invoice_data)
            op=messagebox.showinfo("Saved",f"Invoice No:{self.invoice_no.get()} Saved Successfully")
            f1.close()
    
    def iprint(self):
         q=self.textarea.get(1.0,"end-1c")
         filename=tempfile.mktemp('.txt')
         open(filename,'w').write(q)
         os.startfile(filename,"print")

    def find_bill(self):
        found="no"  
        for i in os.listdir("bills/"):
              if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                     self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if  found=="no":
             messagebox.showerror("Error","Invalid Bill No.")



    def categories(self,event=""):
          if self.combo_Category.get()=="Saw Dust":
                self.comboSize.config(values=self.subcatSawdust)
                self.comboSize.current(0)
       
          if self.combo_Category.get()=="Fire Wood":
              self.comboSize.config(values=self.subcatfirewood)
              self.comboSize.current(0)
          
          if self.combo_Category.get()=="Teak":
              self.comboSize.config(values=self.subcatSizes)
              self.comboSize.current(0)

          if self.combo_Category.get()=="Neem":
              self.comboSize.config(values=self.subcatSizes)
              self.comboSize.current(0)

          if self.combo_Category.get()=="Jamun":
              self.comboSize.config(values=self.subcatSizes)
              self.comboSize.current(0)        
          
          if self.combo_Category.get()=="Black Thuma":
              self.comboSize.config(values=self.subcatSizes)
              self.comboSize.current(0)
          
          if self.combo_Category.get()=="Nidra Ganneru":
              self.comboSize.config(values=self.subcatSizes)
              self.comboSize.current(0)
          
          if self.combo_Category.get()=="Fire Wood":
              self.comboHeight.config(values=self.Na)
              self.comboHeight.current(0)
        
          if self.combo_Category.get()=="Saw Dust":
              self.comboHeight.config(values=self.Na)
              self.comboHeight.current(0)
        
          if self.combo_Category.get()=="Teak":
              self.comboHeight.config(values=self.subcatHeight)
              self.comboHeight.current(0)
          
          if self.combo_Category.get()=="Neem":
              self.comboHeight.config(values=self.subcatHeight)
              self.comboHeight.current(0)
          
          if self.combo_Category.get()=="Jamun":
              self.comboHeight.config(values=self.subcatHeight)
              self.comboHeight.current(0)
          
          if self.combo_Category.get()=="Black Thuma":
              self.comboHeight.config(values=self.subcatHeight)
              self.comboHeight.current(0)
               
          if self.combo_Category.get()=="Nidra Ganneru":
              self.comboHeight.config(values=self.subcatHeight)
              self.comboHeight.current(0)
    
    def price(self,event=""):
          if self.comboSize.get()=="1kg":
              self.comboprice.config(value=self.price_1kg)
              self.comboprice.current(0)

          if self.comboSize.get()=="15kg":
              self.comboprice.config(value=self.price_15kg)
              self.comboprice.current(0)

          if self.comboSize.get()=="25kg":
              self.comboprice.config(value=self.price_25kg)
              self.comboprice.current(0)

          if self.comboSize.get()=="30kg":
              self.comboprice.config(value=self.price_30kg)
              self.comboprice.current(0)
           
          if self.comboSize.get()=="10kg":
              self.comboprice.config(value=self.fprice_10kg)
              self.comboprice.current(0)
              
          if self.comboSize.get()=="20kg":
              self.comboprice.config(value=self.fprice_20kg)
              self.comboprice.current(0)

          if self.comboSize.get()=="40kg":
              self.comboprice.config(value=self.fprice_40kg)
              self.comboprice.current(0)

          if self.comboSize.get()=="60kg":
              self.comboprice.config(value=self.fprice_60kg)
              self.comboprice.current(0)
      
              



          
    
     
     
      

     









if __name__=='__main__':
   root=Tk()
   object=Bill_App(root)
   root.mainloop()

      