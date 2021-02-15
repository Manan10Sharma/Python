from datetime import datetime
now=datetime.now()
print("\t\t#current date and time ")
print("now:-",now)
dt_string=now.strftime("%D--%M--%Y  %H:%M:%S")
print("date and time:-",dt_string)
print("\t\t\tprogram finished...")
