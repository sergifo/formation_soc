# est ce que le serveur est en maintenance
serv_maint = input("est ce que le serveur est en maintenance ?  repondez oui ou non")
serv_maint = serv_maint.lower()
maint = bool(serv_maint == "oui")
print(f"le serveur est en maintenance :{maint}")


