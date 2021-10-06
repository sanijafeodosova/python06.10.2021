import os
#os.remove('aste.txt') - Izdzēš failu
if os.path.exists("kastes.txt"):
    os.rename("kastes.txt", "kastite.txt")
else:
    print("Fails neeksistē")