from tkinter import Tk, Label, Button, Entry, Text, messagebox


def saveData():
    global file_name_entry, encryption_text_data
    
   
    file_name = file_name_entry.get()

   
    with open(file_name + ".txt", "w") as file:
        
        data = encryption_text_data.get("1.0", "end-1c")
        
  
        ciphercode = encrypt('your_key', data.encode())
        
      
       
        hex_ciphercode = ciphercode.hex()
        
        
        print(hex_ciphercode)
        
        
        file.write(hex_ciphercode)
    
   
    file_name_entry.delete(0, 'end')
    
    
    encryption_text_data.delete('1.0', 'end')
    
    
    messagebox.showinfo("Success", "Data successfully encrypted and stored in file!")


def startEncryption():
    global file_name_entry, encryption_text_data
    
    
    root_encryption = Tk()
    root_encryption.title("Encryption Window")
    
    
    root_encryption.config(bg="#f0f0f0")
    
    
    heading_label = Label(root_encryption, text="Encryption Window", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
    heading_label.pack(pady=10)
    
    
    file_name_label = Label(root_encryption, text="File Name: ", bg="#f0f0f0")
    file_name_label.pack(pady=5)
    
   
    file_name_entry = Entry(root_encryption, width=30)
    file_name_entry.pack(pady=5)
    
   
    encryption_text_data = Text(root_encryption, height=10, width=50)
    encryption_text_data.pack(pady=5)
    
   
    btn_create = Button(root_encryption, text="Create", bg="#4CAF50", border=0, command=saveData, padx=10, pady=5)
    btn_create.pack(pady=10)
    
    root_encryption.mainloop()


def encrypt(key, message):
    
    pass


def decrypt(key, encrypted_message):
    
    pass


if __name__ == "__main__":
    startEncryption()
