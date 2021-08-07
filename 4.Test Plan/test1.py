from tkinter import*
from tkinter.ttk import*
import pandas
root=Tk()                      
root.title("WELCOME")
root.geometry("600x500+350+150") 
root.resizable(0,0)

excel_data_df = pandas.read_excel("Barley_Import.xlsx",sheet_name='Sheet1')
#text.insert('end',excel_data_df)
print(excel_data_df.loc[,"Year"])
        '''if(ph_value1 == 0 or  ec_value1==0 or  oc_value1==0 or caco3_value1==0 or n_value1==0 or k_value1 == 0 or b_value1 == 0 or p_value1==0 or cu_value1 == 0 or zn_value1==0 or mn_value1==0 or fe_value1==0 or s_value1==0 or mg_value1==0 or ca_value1==0):
        messagebox.showinfo("Please checkout", "please fill all the field")
        #after_prediction()
        #pred_window(ph1,ph2,ec1,ec2,oc1,oc2,caco31,caco32,n1,n2,p1,p2,b1,b2,k1,k2)'''
        '''elif(type(ph_value1)!= int  or  type(ec_value1)!= int or  type(oc_value1)!= int or type(caco3_value1)!= int or type(n_value1)!= int  or type(k_value1)!= int or type(p_value1)!=int or type(b_value1)!=int or type(ca_value1)!=int or type(mg_value1)!=int or type(s_value1)!=int or type(fe_value1)!=int or type(mn_value1)!=int or type(zn_value1)!=int or type(cu_value1)!=int):
        messagebox.showinfo("Please checkout","please enter the Integer values")
        #after_prediction()
        #pred_window(ph1,ph2,ec1,ec2,oc1,oc2,caco31,caco32,n1,n2,p1,p2,b1,b2,k1,k2)'''
    
        '''print(1)
        #l1=Label(after_prediction_page1,text= ph_value1).pack()
        print(ph_value1,ec_value1,oc_value1,caco3_value1,n_value1,k_value1,b_value1,p_value1)
        data1 = [[ph_value1,ec_value1,oc_value1,caco3_value1,n_value1,k_value1,b_value1,p_value1]]
        print(data1)
        #prediction_module(ph_value1,ph_value2,ec_value1,ec_value2,oc_value1,oc_value2,caco3_value1,caco3_value2,k_value1,k_value2,p_value1,p_value2,n_value1,n_value2,b_value1,b_value2)
        '''
