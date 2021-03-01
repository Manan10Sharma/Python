from datetime import datetime
now=datetime.now()
print("\t\tcurrent date and time ")
print("now:-",now)
dt_string=now.strftime("%D--%M--%Y  %H:%M:%S")
print("date and time:-",dt_string)
