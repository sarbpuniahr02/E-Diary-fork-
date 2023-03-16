Tasks = []
Days = []
name=[];
contact=[];
index=[];
#f=open("pwd1.txt", "x")
#p=open("username.txt", "x")
#q=open("name.txt","x")
#r=open("contact.txt","x")
print()
def my_function():
        print("1-calendar");
        print("2-Address Book");
        print("3-Planner");
        print("4-Password Manager");
        print("5-Wishlist ");
        print("6-Exit ");







def calendar():
    mm = int(input("Enter the month(1/2/3/4/5/6/7/8/9/10/11/12): "))
    yy = int(input("Enter the year: "))
    
    month ={1:'January', 2:'February', 3:'March', 
            4:'April', 5:'May', 6:'June', 7:'July',
            8:'August', 9:'September', 10:'October',
            11:'November', 12:'December'}
    
    # code below for calculation of odd days
    day =(yy-1)% 400
    day = (day//100)*5 + ((day % 100) - (day % 100)//4) + ((day % 100)//4)*2
    day = day % 7
    
    nly =[31, 28, 31, 30, 31, 30, 
        31, 31, 30, 31, 30, 31]
    ly =[31, 29, 31, 30, 31, 30, 
        31, 31, 30, 31, 30, 31]
    s = 0
    
    if yy % 4 == 0:
        for i in range(mm-1):
            s+= ly[i]
    else:
        for i in range(mm-1):
            s+= nly[i]
    
    day += s % 7
    day = day % 7
    
    # variable used for white space filling 
    # where date not present
    space =''
    space = space.rjust(2, ' ')
    
    # code below is to print the calendar
    print(month[mm], yy)
    print('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')
    
    if mm == 9 or mm == 4 or mm == 6 or mm == 11: 
        for i in range(31 + day):
            
            if i<= day:
                print(space, end =' ')
            else:
                print("{:02d}".format(i-day), end =' ')
                if (i + 1)% 7 == 0:
                    print()
    elif mm == 2:
        if yy % 4 == 0:
            p = 30
        else:
            p = 29
            
        for i in range(p + day):
            if i<= day:
                print(space, end =' ')
            else:
                print("{:02d}".format(i-day), end =' ')
                if (i + 1)% 7 == 0:
                    print() 
    else:
        for i in range(32 + day):
            
            if i<= day:
                print(space, end =' ')
            else:
                print("{:02d}".format(i-day), end =' ')
                if (i + 1)% 7 == 0:
                    print()







def Address_Book():
    def add_contact():
        fname=input("Enter Name: ").upper();
        phone=input("Enter Phone Number: ")
        if len(phone)==10:

            with open('name.txt' , 'a') as f :
                f.write(fname + " | ")
    
            with open('contact.txt' , 'a') as f :
                f.write(phone + " | ")
            print("Contact added successfully!!")
            f=open("name.txt","r")
            p=open("contact.txt","r")
            name_data=p.read()
            contact_data=f.read()
            name=name_data.split(" | ")
            contact=contact_data.split(" | ")
            name.pop()
            contact.pop()
        
        else:
            print("please try again with a valid phone number of 10 digits!!")
        
    def edit_contact(change,a):
        f=open("name.txt","r")
        p=open("contact.txt","r")
        name_data=f.read()
        contact_data=p.read()
        name=name_data.split(" | ")
        contact=contact_data.split(" | ")
        if change=='0':
            new_name=input("Enter new name: ").upper()
            name[index[a]]=new_name
            file=open('name.txt' , 'w')
            for nam in name:
                if nam!='':
                    file.write(nam+" | ")
            file.close()
            index.clear()
        elif change=='1':
            number=input("Enter new phone number: ")
            if len(number)==10:
                contact[index[a]]=number
                file2=open('contact.txt','w')
                for c in contact:
                    if c !='':
                        file2.write(c+" | ")
                file2.close()
            else:
                print("please try again with a valid phone number of 10 digits!!")
            index.clear()
        elif change=='2':
            new_name=input("Enter new name: ").upper()
            number=input("Enter new phone number: ")
            if len(number)==10:
                name[index[a]]=new_name
                contact[index[a]]=number
                file=open('name.txt' , 'w')
                file2=open('contact.txt','w')
                for nam in name:
                    if nam!='':
                        file.write(nam+" | ")
                file.close()
                for c in contact:
                    if c !='':
                        file2.write(c+" | ")
                file2.close()
            else:
                print("please try again with a valid phone number of 10 digits!!")
            index.clear()
            
    def edit_contact_check():
        f=open("name.txt","r")
        p=open("contact.txt","r")
        name_data=f.read()
        contact_data=p.read()
        name=name_data.split(" | ")
        contact=contact_data.split(" | ")
        if len(name)>0:
            edit=input("Enter contact name that you want to edit: ").upper()
            found=search_contact(edit)
            if found==0:
                x=input("do you want to add the contact to contact list?(y/n): ").upper()
                if x=='Y':
                    add_contact()
            elif found==1:
                change=input("A.press 0 to edit name"+"\nB.press 1 to edit phone number"+"\nC. press 2 to edit both details"+"\nEnter your choice: ")
                # y=edit_find_num(num);
                edit_contact(change,0)
            elif found>1:
                num=input("Found multiple records with same name enter phone number of the contact name that you want to edit: ")
                y=edit_find_num(num);
                if y==None:
                    return;
                change=input("A.press 0 to edit name"+"\nB.press 1 to edit phone number"+"\nC. press 2 to edit both details"+"\nEnter your choice: ")
                edit_contact(change,y)
        else:
            print("0 ---record present in contact list")
            d=input("do you want to add contact in contact list(y/n): ").upper()
            if d=='Y':
                add_contact()
                
    def remove_contact():
        f=open("name.txt","r")
        p=open("contact.txt","r")
        name_data=f.read()
        contact_data=p.read()
        name=name_data.split(" | ")
        contact=contact_data.split(" | ")
        remove=input("Enter name of contact that you want to remove: ").upper()
        found=search_contact(remove)
        if found==0:
            print("Contact not present in the list")
        elif found==1:
            k=input("do you want to delete the record(y/n)?: ").upper()
            if k=='Y':
                contact.pop(index[0])
                name.pop(index[0])
                file=open('name.txt' , 'w')
                file2=open('contact.txt','w')
                for nam in name:
                    if nam!='':
                        file.write(nam+" | ")
                file.close()
                for c in contact:
                    if c !='':
                        file2.write(c+" | ")
                file2.close()
                index.clear()
                print("record deleted successfully!!")
        elif found>1:
            num=input("Found multiple records with same name enter phone number of the contactname that you want to delete: ")
            y=edit_find_num(num);
            if y==None:
                return;
            else:
                k=input("do you want to delete the record(y/n)?: ").upper()
                if k=='Y':
                    contact.pop(index[y])
                    name.pop(index[y])
                    file=open('name.txt' , 'w')
                    file2=open('contact.txt','w')
                    for nam in name:
                        if nam!='':
                            file.write(nam+" | ")
                    file.close()
                    for c in contact:
                        if c !='':
                            file2.write(c+" | ")
                    file2.close()
                    index.clear()
                    print("record deleted successfully!!")

    def view_contact():
        f=open("name.txt","r")
        p=open("contact.txt","r")
        name_data=f.read()
        contact_data=p.read()
        name=name_data.split(" | ")
        contact=contact_data.split(" | ")
        i = 0
        while i < len(name)-1:    
            print(i+1,"Name- "+name[i]+"\t""\t"+"Phone no-",contact[i])
            i = i + 1

    def display(k,j):
        f=open("name.txt","r")
        p=open("contact.txt","r")
        name_data=f.read()
        contact_data=p.read()
        name=name_data.split(" | ")
        contact=contact_data.split(" | ")
        print(j,"Name- "+name[k]+"\t""\t"+"Phone no-",contact[k])
        index.append(k)

    def search_contact(nam):
        p=open("name.txt","r")
        name_data=p.read()
        name=name_data.split(" | ")
        j=0
        for i in range(len(name)-1):
            if nam==name[i]:
                j+=1
                display(i,j);
        print(j,"-----record found from contact list")
        return j

    def edit_find_num(num):
        f=open("contact.txt","r")
        contact_data=f.read()
        contact=contact_data.split(" | ")
        for i in range(len(index)):
            if num==contact[index[i]]:
                return index[i]
        else:
            print("The number you entered is not in contact list.")
            index.clear()
                
    def my_function():
            print("0-Add Contact");
            print("1-Edit Contact");
            print("2-Remove Contact");
            print("3-View Contact");
            print("4-Search Contact");
            print("5-Exit ");
            
    def check():
        task=int(input("enter task number to be performed: "));
        if task==0 :
            print("task selected: Add contact");
            add_contact();
        elif task==1 :
            print("task selected: Edit contact");
            p=open("name.txt","r")
            name_data=p.read()
            name=name_data.split(" | ")
            if len(name)>1:
                edit_contact_check();
            else:
                print("0 ----record present in contact list")
        elif task==2 :
            print("task selected: Remove contact");
            p=open("name.txt","r")
            name_data=p.read()
            name=name_data.split(" | ")
            if len(name)>1:
                remove_contact();
            else:
                print("0 ----record present in contact list")
        elif task==3:
            p=open("name.txt","r")
            name_data=p.read()
            name=name_data.split(" | ")
            print("task selected: View contact");
            if len(name)>1:
                view_contact();
            else:
                print("0 ----record present in contact list")
        elif task==4:
            print("task selected: Search contact");
            p=open("name.txt","r")
            name_data=p.read()
            name=name_data.split(" | ")
            if len(name)>1:
                nam=input("Enter contactname you want to search: ").upper()
                search_contact(nam);
            else:
                print("0 ----record present in contact list")
        elif task==5:
            return task;
    while True : 
        my_function()
        x=check();
        if x==5:
            print("Exited Successfully!!!");
            break;
        print("\n")







def Planner():
    select=int(input("press 0 to add task"+"\npress 1 to search task"+"\nEnter choice(0/1): "))
    if select==0:
        num = int(input("Number of entries: "))
        if num>0:
            for i in range(num):
                Task = input("Task: ")
                Day = input("Day: ") # for convert to int => int(input("Day: "))
            
                Tasks.append(Task)
                Days.append(Day)
            print("\nTask\t\t\tDay\n")
            for i in range(num):
                print("{}\t\t\t{}".format(Tasks[i], Days[i]))
    elif select==1:
        d=0
        search_term = input("\nEnter search term: ")
        print("Search result:")
        for i in range(len(Tasks)):
            if search_term==Tasks[i]:
                d=1
                index = Tasks.index(search_term)
                Day = Days[index]
                print("Task: {}, Day: {}".format(search_term, Day))
        if d==0:
            print("Task Not Found")
    else:
        print("Invalid Choice Please Choose a valid choice!!")





def Password_manager():
    master_pwd = input("What is the master password?")
    while True :
        mode = input("Would you like to add a new password or existing ones(view , add , quit)?")
        if mode == "quit" :
            break
        if mode == "view" :
            view()
        elif mode == "add" :
            add()
        else:
            print("Invalid mode")
            continue
    
def view():
    f=open("pwd1.txt","r")
    p=open("username.txt","r")
    name_data=p.read()
    pwd_data=f.read()
    name=name_data.split(" | ")
    password=pwd_data.split(" | ")
    i = 0
    while i < len(name)-1:    
        print("user: "+name[i]+ " password: " + password[i])
        i = i + 1
def add():
    name = input('Account name:')
    pwd = input ("Password:")

    with open('pwd1.txt' , 'a') as f :
        f.write(pwd + " | ")
    
    with open('username.txt' , 'a') as f :
        f.write(name + " | ")





def wishes_list():
    print(" Sometimes things become possible if we want them bad enough " )
    
    def print_list():
        print("Here are your wishes:")
        for a in range(len(wish_list)):
            print(wish_list[a])

    wish_list = []
    wish = ("")
    n = int (input("Number of entries: "))
    for i in range(n):
        wish = input("Please enter wish {}:".format(i + 1))
        wish_list.append(wish)
    print_list()








def check():
    task=int(input("enter task number to be performed: "));
    if task==1 :
        print("task selected: calendar ");
        calendar();
    elif task==2 :
        print("task selected: Address Book ");
        Address_Book();
    elif task==3 :
        print("task selected: Planner");
        Planner();
    elif task==4 : 
        print("task selected: Password Manager");
        Password_manager();
    elif task==5 :
        print("task selected: Wishlist");
        wishes_list();
    elif task==6:
        return task;
while True : 
    my_function()
    x=check();
    if x==6:
        print("Exited Successfully!!!");
        break;
    print("\n")