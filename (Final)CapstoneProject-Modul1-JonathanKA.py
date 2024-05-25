#Data yang berisikan nama - nama disimpan menggunakan fungsi nested list digabungkan dengan dictionary
ContactList = [
    {'ContactID':1001,
     'Name': 'Andi Budiharjo',
     'Occupation': 'Manager',
     'Company Name': 'PT. Berkat Maju Bersama',
     'Website': '',
     'Email': 'AndiBudiharjo007@gmail.com'
    },
    {'ContactID': 1002,
     'Name': 'Magnus Carlsen',
     'Occupation': 'Chess Player',
     'Company Name': 'Play Magnus Group',
     'Website': 'https://playmagnusgroup.com/',
     'Email': 'magnus@chess24.com'
    },
    {'ContactID': 1003,
      'Name': 'Lewis Hamilton',
      'Occupation': 'Race Car Driver',
      'Company Name': 'Mercedes-AMG PETRONAS Formula One Team',
      'Website': 'https://www.mercedesamgf1.com/drivers/driver/lewis-hamilton',
      'Email': 'teamlh@lewishamilton.com'
    },
    {'ContactID': 1004,
     'Name': 'Taylor Swift',
     'Occupation': 'Artist',
     'Company Name': 'Taylor Swift Productions, Inc',
     'Website': 'https://www.taylorswift.com',
     'Email': 'taylorswift@umgstores.com'
    },
    {'ContactID': 1005,
     'Name': 'Christiano Ronaldo',
     'Occupation': 'Soccer Player',
     'Company Name': 'Al Nassr FC',
     'Website': 'https://www.cristianoronaldo.com',
     'Email': ''
    }
]
existingID = int()
i = int()

def SortByID(e):
    return e['ContactID']

#Fungsi untuk mencari Kontak. Digunakan dalam fungsi ModifyContact() dan DeleteContact()
def FindContactID():
    global i #--variable i dianggap sebagai global variable
    global existingID #--variable existingID dianggap sebagai global variable, sehingga meskipun dalam fungsi lain, existingID 
    existingID = int(input('\nPlease input an existing ContactID: '))   #--meminta user untuk menginput ContactID yang terekam didalam ContactList.
    for i in range(len(ContactList)):
        if existingID == ContactList[i]['ContactID']:   #--Komputer akan looping hingga menemukan COntactID yang sama dengan yang diinput oleh user.
            print(f'''\nContactID = {ContactList[i]['ContactID']}\nName = {ContactList[i]['Name']}\nOccupation = {ContactList[i]['Occupation']}\nCompany Name = {ContactList[i]['Company Name']}\nWebsite = {ContactList[i]['Website']}\nEmail = {ContactList[i]['Email']}''')
            return i, existingID
        if i-len(ContactList) == -1 and existingID != ContactList[i]['ContactID']:  #--kondisi IF apabila komputer telah selesai looping hingga data terakhir dan tidak menemukan COntactID yang diinput oleh user.
            print('\nThe data you are looking for does not exist')
            ModifyContact() #--kembali ke fungsi ModifyContact() - fungsi untuk mengedit kontak di dalam list.

#Fungsi digunakan dalam fungsi ModifyContact(). Fungsi ini digunakan untuk mengubah value dari Nama, Pekerjaan, Nama Perusahaan, Website, atau Email.    
def UpdateColumn(ColN):
    while True:
        editColN = input(f'Please input a new {ColN} for this contact: ')   #--komputer meminta user untuk memasukkan nilai yang baru untuk kolom terkait.
        for j in range(len(ContactList)):
            if editColN == ContactList[j][ColN]:    #--Menjalankan kondisi IF apabila value yang diinput oleh user sama dengan nilai sebelumnya.
                #--Komputer akan memberi tahu user bahwa value yang diinput sama dengan value sebelumnya. Apakah user tetap akan melanjutkan?
                asktochange_ColN = input(f'The {ColN} you entered is the same as the previous one. Continue?(yes/no)').lower()
                if asktochange_ColN == 'yes':   #--apabila user input 'yes' komputer akan menampilkan Detil kontak yang dipilih dengan tidak mengganti value apapun.
                    print(f'''\nContactID = {ContactList[i]['ContactID']}\nName = {ContactList[i]['Name']}\nOccupation = {ContactList[i]['Occupation']}\nCompany Name = {ContactList[i]['Company Name']}\nWebsite = {ContactList[i]['Website']}\nEmail = {ContactList[i]['Email']}''')
                    ModifyContact()
                if asktochange_ColN == 'no':    #--apabila user input 'no' maka komputer akan kembali menanyakan user untuk memberikan value baru untuk kolom terkait.
                    break
                else: #selain user input yes/no, komputer akan mengingatkan user untuk memberikan input yes/no.
                    print('Please input yes or no')
                    break
            if len(ContactList)-j == 1 and editColN != ContactList[j][ColN]:    #--apabila komputer telah selesai melakukan looping dan value yang diinput tidak sama
                #--Komputer akan menanyakan apakah user yakin untuk mengubah value dari kolom terkait.
                asktochange_ColN = input(f'Are you sure you want to change the {ColN} for this contact?(yes/no): ').lower()
                if asktochange_ColN == 'yes':   #--apabila user input 'yes', komputer akan mengganti value yang lama dengan value yang baru dan menampilkan detil kontak yang udah diubah sesuai request user.
                    ContactList[i][ColN] = editColN
                    print(f'''\nContactID = {ContactList[i]['ContactID']}\nName = {ContactList[i]['Name']}\nOccupation = {ContactList[i]['Occupation']}\nCompany Name = {ContactList[i]['Company Name']}\nWebsite = {ContactList[i]['Website']}\nEmail = {ContactList[i]['Email']}''')
                    print(f'The {ColN} for this contact has been successfully changed')
                    ModifyContact()
                if asktochange_ColN == 'no':    #--apabila user input 'no', komputer akan kembali ke menu 'Modify a Contact'.
                    ModifyContact()
                else:
                    print('Please input yes or no') #--mengingatkan user untuk memberikan input 'yes' atau 'no'
                    break
        
#Fungsi untuk menampilkan seluruh isi list kontak
def AllContacts():
    print('\n*************** Celebrity Contact Lists ***************\n=======================================================')
    for i in range(len(ContactList)):
        print(f'''
        |   |   ContactID = {ContactList[i]['ContactID']}
        |   |   Name = {ContactList[i]['Name']}
        |   |   Occupation = {ContactList[i]['Occupation']}
        |   |   Company Name = {ContactList[i]['Company Name']}
        |   |   Website = {ContactList[i]['Website']}
        |   |   Email = {ContactList[i]['Email']}''')

#Fungsi ViewContact() untuk melihat seluruh isi kontak atau melihat kontak per ContactID(Unique Value)
def ViewContact():
    while True:
        try:    #--mencegah user menginput non-integer
            viewContacts = int(input('''\nHere you can view every celebrities' contact lists or find a specific person by inputting his/her ContactID.\n1. View all contacts\n2. Find someone by ContactID\n3. Back to main menu\nWhat would you like to do?\t'''))
            break
        except ValueError:
            print("\nYou're not entering a number from the menu. Please choose the correct menu by inputting an integer.")
    while True:
        try:
            if viewContacts == 1 and len(ContactList) >= 1:#--memanggil menu 1 untuk melihat semua kontak dengan kondisi kontak (list) terisi
                AllContacts()
            elif viewContacts == 1 and len(ContactList) == 0:#--memanggil menu 1 dengan kondisi kontak (list) kosong
                print('Data does not exist')
            elif viewContacts == 2 and len(ContactList) >= 1:#--memanggil menu 2 - memilih kontak berdasarkan ContactID
                contactID = int(input('''\nInput a ContactID: '''))
                for i in range(len(ContactList)):
                    if contactID == ContactList[i]['ContactID']:    
                        print(f'''\nContactID = {ContactList[i]['ContactID']}\nName = {ContactList[i]['Name']}\nOccupation = {ContactList[i]['Occupation']}\nCompany Name = {ContactList[i]['Company Name']}\nWebsite = {ContactList[i]['Website']}\nEmail = {ContactList[i]['Email']}''')
                        break
                    elif i-len(ContactList) == -1 and contactID != ContactList[i]['ContactID']:#fungsi ini akan dijalankan ketika i sudah terulang sampai akhir dan contactID tidak sama dengan contactID dalam list.
                        while True:
                            askcreate = input('ContactID does not exist. Do you want to create a new contact? (yes/no)').lower()
                            if askcreate == 'yes':
                                AddContact()
                            elif askcreate == 'no':
                                break
                            else:
                                print('Input yes or no')
            elif viewContacts == 2 and len(ContactList) == 0:#--memanggil menu 2 - memilih kontak berdasarkan ContactID
                print('Data does not exist')
            elif viewContacts == 3:#kembali ke main menu
                MainMenu()
            else:
                print('\nPlease input the correct menu')
                ViewContact()
        except ValueError:
            print("\nYou're not entering a ContactID. Please input an exsiting ContactID.")
        while True: #--Setelah user memilih opsi pertama atau kedua, komputer menanyakan langkah user selanjutnya. Kembali ke view contacts atau kembali ke main menu?
            try:  #--mencegah user menginput non-integer.
                back = int(input("\n1. Back to 'View Contacts'\n2. Back to Main Menu\nWhat would you like to do next?\t"))
                while True:
                    if back == 1:
                        ViewContact()
                    elif back == 2:
                        while True:
                            cond = input('Go back to main menu? (yes/no)').lower()
                            if cond == 'yes':
                                MainMenu()
                            elif cond == 'no':
                                ViewContact()
                            else:
                                print('input yes or no')
                    else:
                        print('\nPlease Input the correct menu')
                        back = int(input("\n1. Back to 'View Contacts'\n2. Back to Main Menu\nWhat would you like to do next?\t"))
            except ValueError:
                print("\nYou're not entering a number from the menu. Please choose the correct menu by inputting an integer.")

#Fungsi AddContact() memperbolehkan user untuk menambahkankan contact kedalam list 'ContactList'
def AddContact():
    while True:
        try:
            addContactMenu = int(input('''\n1. Create new ContactID\n2. Back to Main Menu\nWhat would you like to do?\t'''))
            #menanyakan user untuk membuat kontak baru dengan menginput ContactID baru kedalam list atau kembali ke menu utama.
            if addContactMenu == 1:
                newID = int(input('\nPlease input a new ContactID: '))
                for i in range(len(ContactList)):
                    if newID == ContactList[i]['ContactID']:#Kondisi IF menjaga agar primary key yang ingin ditambahkan tidak double.
                        print('\nContactID already exist. Please input a new contactID.')
                        newID = int(input('Please input a new ContactID: '))
                    if i-len(ContactList) == -1 and newID != ContactList[i]['ContactID']:#kondisi IF untuk mengecek apakah primary key(ContactID) yang diinput user belum ditemukan di dalam list.
                        print('\n****Create a New Contact***\n===========================')#komputer memperbolehkan user untuk menambahkan detil kontak baru dengan Primary Key (ContactID) yang baru
                        print(f'ContactID: {newID}')
                        new_Name = input('Name: ')#user input detil kontak baru yang akan ditambahkan
                        new_Occupation = input('Occupation: ')
                        new_CompanyName = input('Company Name: ')
                        new_Website = input('Website: ')
                        new_Email = input('Email: ')
                        createnew = input('Are you sure you want to create this contact? (yes/no): ').lower()
                        while True:#Komputer menanyakan apakah user yakin akan membuat kontak baru dengan hasil inputan sebelumnya?
                            if createnew == 'yes':#Komputer menambahkan kontak tersebut ke dalam ContactList[].
                                ContactList.append({'ContactID': newID,
                                                    'Name': new_Name,
                                                    'Occupation': new_Occupation,
                                                    'Company Name': new_CompanyName,
                                                    'Website': new_Website,
                                                    'Email': new_Email})
                                ContactList.sort(key=SortByID)
                                print('Your new contact has been successfully created.\n')
                                AllContacts()#Komputer menampilkan seluruh isi kontak di dalam ContactList[]
                                break
                            if createnew == 'no':#Kembali ke menu AddContact
                                break
                            else:
                                print('\nPlease input yes or no')
                                createnew = input('Are you sure you want to create this contact? (yes/no): ').lower()
            elif addContactMenu == 2: #--Apabila user memilih opsi kedua, komputer akan kembali ke menu utama
                MainMenu()
            else:
                print('\nPlease input the correct menu.')
        except ValueError:
            print('\nPlease input an integer')

#Fungsi ModifyContact() adalah untuk mengubah informasi dari sebuah Kontak yang sudah ada didalam list
def ModifyContact():
    while True:
        try:
            #User dapat memilih untuk mengedit kontak dengan memilih ContactID yang sudah ada didalam kontak atau kembali ke menu utama.
            modContact = int(input('''\n1. Choose a ContactID to edit\n2. Back to Main Menu\nWhat would you like to do?\t'''))
            if modContact == 1: #--user memilih opsi 1 - mengedit kontak.
                FindContactID()
                asktoedit = input('Are you sure you want to update this contact?(yes/no): ').lower()
                if asktoedit == 'yes':
                    editcolumn = int(input('\nModify Contact Menu\n===================\n1. ContactID\n2. Name\n3. Occupation\n4. Company Name\n5. Website\n6. Email\nPlease choose the column name that you want to edit from the contact above:'))
                    if editcolumn == 1:
                        while True:
                            editContactID = int(input('\nPlease input a NEW value for the existing ContactID: '))
                            for j in range(len(ContactList)):
                                if editContactID == existingID:
                                    while True:
                                        sameID = input('The ContactID that you input for this contact has not been changed. Continue? (yes/no): ')
                                        if sameID == 'yes':
                                            print(f'\nThe ContactID for {ContactList[i]['Name']} has not been changed.')
                                            ModifyContact()
                                        if sameID == 'no':
                                            editContactID = int(input('Please input a NEW value for the existing ContactID: '))
                                            break
                                        else:
                                            print('\nPlease input yes or no')
                                elif editContactID == ContactList[j]['ContactID']:
                                    print('\nContactID already exist. Please input a NEW ContactID')
                                    break
                                elif j - len(ContactList) == -1 and editContactID != ContactList[j]['ContactID']:
                                    updatemakesure = input('Are you sure you want to update this data?(yes/no)')
                                    if updatemakesure == 'no':
                                        ModifyContact()
                                    if updatemakesure == 'yes':
                                        ContactList[i]['ContactID'] = editContactID
                                        ContactList.sort(key=SortByID)
                                        print(f'''
                                        ContactID = {ContactList[i]['ContactID']}
                                        Name = {ContactList[i]['Name']}
                                        Occupation = {ContactList[i]['Occupation']}
                                        Company Name = {ContactList[i]['Company Name']}
                                        Website = {ContactList[i]['Website']}
                                        Email = {ContactList[i]['Email']}''')
                                        done = print('Data successfully updated')
                                        ModifyContact()
                    if editcolumn == 2:
                        UpdateColumn('Name')
                    if editcolumn == 3:
                        UpdateColumn('Occupation')
                    if editcolumn == 4:
                        UpdateColumn('Company Name')
                    if editcolumn == 5:
                        UpdateColumn('Website')
                    if editcolumn == 6:
                        UpdateColumn('Email')
                    else:
                        print('Please input a correct menu option')
                if asktoedit == 'no':
                    ModifyContact()
                else:
                    print('Please input yes or no')
                    break
            if modContact == 2:
                MainMenu()
            else:
                print('Please input the correct menu.')
        except ValueError:
            print("\nPlease input a number/numbers.")

#Fungsi DeleteContact() adalah untuk menghapus kontak yang ada di dalam list ContactList
def DeleteContact():
    while True:
        try:
            delContact = int(input('''\n1. Choose a contactID to delete\n2. Back to Main Menu\nWhat would you like to do?\t'''))
            if delContact == 1:
                contactID = int(input('\nPlease input ContactID you want to delete: '))
                for i in range(len(ContactList)):
                    if contactID == ContactList[i]['ContactID']:
                        print(f'''\nContactID = {ContactList[i]['ContactID']}\nName = {ContactList[i]['Name']}\nOccupation = {ContactList[i]['Occupation']}\nCompany Name = {ContactList[i]['Company Name']}\nWebsite = {ContactList[i]['Website']}\nEmail = {ContactList[i]['Email']}''')
                        deletemenu = input('Contact found. Are you sure you want to delete this contact?(yes/no):  ')
                        while True:
                            if deletemenu == 'yes':
                                del ContactList[i]
                                print('\nThis Contact has been deleted.')
                                DeleteContact()
                            if deletemenu == 'no':
                                DeleteContact()
                            else: 
                                print('\nPlease input yes or no')
                                deletemenu = input('Contact found. Are you sure you want to delete this contact?(yes/no):  ')
                    elif i - len(ContactList) == -1 and contactID != ContactList[i]['ContactID']:
                        print('Contact not found. Please input an existing ContactID')
            elif delContact == 2:
                MainMenu()
            else:
                print('Please input the correct menu.')
        except ValueError:
            print('\nPlease input a number or numbers.')

#Main Menu
def MainMenu():
    while True:
        print('''
                ***Welcome to Your Very Own Celebrity Contact Generator!***
    ****Here you can view, update, and delete any famous celebrities' contact lists.****
    ====================================================================================
                    1. View Contacts
                    2. Add a Contact
                    3. Modify a Contact
                    4. Delete Contact
                    5. Exit
            ''')
        choose_menu = int(input('What would you like to do?\t'))
        if choose_menu == 1:
            ViewContact()
        if choose_menu == 2:
            AddContact()
        if choose_menu == 3:
            ModifyContact()
        if choose_menu == 4:
            DeleteContact()
        if choose_menu == 5:
            exit()

MainMenu()