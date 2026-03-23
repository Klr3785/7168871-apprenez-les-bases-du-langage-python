nombre1 = input("Entrer un nombre :")
nombre2 = input("Entrer un nombre :")

if not nombre1.isnumeric() or not nombre2.isnumeric():
  print("Les nombres doivent être des nombres entier.")
raise SystemExit("Fin du programme")

nombre1 = int(nombre1)
nombre2 = int(nombre2)

operation =  input ("Entrer l'opération souhaitée :") 

if not operation = ["+", "-", "*", "/"]:
  print("L'opération n'est pas valide.")
raise SystemExit("Fin du programme")

if operation == "+" :
  resultat = nombre1 + nombre2
elif operation == "-":
  resultat = nombre1 + nombre2
elif operation == "*":
  resultat = nombre1 * nombre2
elif operation == "/":
  if nombre2=0:
    print("Il est impossible de diviser un nombre par zéro.")
    raise SystemExit("Fin du programme") 
  resultat = round(nombre1 / nombre2)
  
print(f "Le résultat est" {resultat} ".")

