
print("Today's prises of our producy__")
print("Chal 1KG prise $80")
#Dal 1KG prise $30
#Ata 1 KG prise $25
#Moyda 1 KG prise $40
#Suji 1 KG prise $15
print("Dal 1KG prise $30")
print("")
print("")
print("")

#Imput's by staff
name =  input ( "Name: " )
chal=  input  ("Chal(KG): ")
dal=  input ("Dal(KG): ")
ata=  input  ("Ata(KG): ")
moyda=  input  ("Moyda(KG): ")
suji=  input  ("Suji(KG): ")
discount = input ("Discount percentage: ")

#Changing input to int formate---------------------------
chal = int (chal)
dal = int (dal)
ata = int (ata)
moyda = int (moyda)
suji = int (suji)
discount = int (discount)

#Math_function-------------------------------------------
total_primary = (chal * 80) + (dal * 30) + (ata * 25) + (moyda * 40) + (suji * 15)
total_medium = float (total_primary)

# main discount(discount_medium)---total_final
discount_medium = ( discount / 100 ) * total_medium
total_final = total_medium - discount_medium

#output_code-----------------------------------------
print (".")
print (".")
print (".")
print ("Welcome to Sakib Groceries.")
print ("Today is", discount,"%  off on all products!!!")
print ("Enjoy Shopping !")
print (".")
print ("Today you bought: ")
print (str(chal) + "KG Chal")
print (str(dal) + "KG Dal")
print (str(ata) + "KG Ata")
print (str(moyda)+ "KG Moyda")
print (str(suji)+ "KG Suji")
print (".")
print  ("Total Prise: " "$" +str(total_medium))
print ("Discount: " "$" + str(discount_medium))
print ("Pay us: " "$" ,total_final, ",Please.")
print ("See you next time " , name, "!!")

input ("Press enter to close_")
