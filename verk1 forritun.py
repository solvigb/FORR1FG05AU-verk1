#Sölvi Geir Björnsson
#Dagsetning 06.09.18

#Liður 1, bý til breytu og bið um nafn notanda og prenta svo út texta með nafn notadans í textanum
nafn = input("Sláðu inn nafn þitt ")
print("Velkomin í áfangann FOR1A3U", nafn + " Þetta verður skemmtileg önn, ég hlakka til að læra forritun.")

#Liður 2, bý til breytu og bið notandan um kommutölu með 3 aukastöfum og prenta út kommuntöluna með 1 aukastaf
kommutala = float(input("Sláðu inn kommutölu með 3 aukastöfum "))
utkoma = (round(kommutala, 1))
print("Þú hefur valið töluna: ", utkoma)

#Liður 3, bý til breytur og bið notanda um 2 heilar tölur, margfaldar þær saman og prentar út útkomuna
print("Skráðu inn 2 heilar tölur til að margfalda saman")
num1 = int(input("Skráðu inn heila tölu "))
num2 = int(input("Skráðu inn heila tölu "))
sum = num1 * num2
print("Útkoma: ", sum)
#Liður 4, bý til breytu og bið notanda um 3 heilar tölur, margfaldar tölurnar saman og prentar út summuna
print("Skráðu inn 3 heilar tölur til að finna rúmmál kassa")
num3 = int(input("Skráðu inn hæð kassans "))
num4 = int(input("Skráðu inn lengd kassans "))
num5 = int(input("Skráðu inn breidd kassans "))
sum2 = num3num4num5
print("Rúmmál kassans er ", sum2)

#Liður 5, bý til breytur fyrir aldur notandans og pabba hans,
#reiknar hvað pabbi notendans var gamall þegar notandinn fæddist og prentar það út
print("Skráðu inn aldur þinn og pabba þíns til að finna út hvað pabbi þinn var gamall þegar þú fæddist")
aldur = int(input("Sláðu inn aldur þinn "))
aldur2 = int(input("Sláðu inn aldur pabba þíns "))
aldurSum = aldur2 - aldur
print("Þú fæddist þegar pabbi þinn var", aldurSum, "ára.")

#Liður 6, bý til breytur fyrir aldur einstaklingana, reikna meðalaldur þeirra og prenat það út
print("Skráðu aldur 3 einstaklinga til að finna meðalaldur þeirra")
aldur3 = int(input("Skráðu inn aldur á einstaklingi 1 "))
aldur4 = int(input("Skráðu inn aldur á einstaklingi 2 "))
aldur5 = int(input("Skráðu inn aldur á einstaklingi 3 "))
medalAldur = (aldur3 + aldur4 + aldur5)/3
print("Meðal aldur þeirra er", medalAldur)

#
print("Gaman að geta aðstoðað þig við þessa útreikninga", nafn)
