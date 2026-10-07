from pathlib import Path


path = Path("guest.txt")

guest = input("What is the name of the guest you want to invite: ")


path.write_text(guest)




