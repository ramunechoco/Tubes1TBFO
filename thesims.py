class Stat:
	def __init__(self, energy, hygiene, fun):
		self.energy = energy
		self.hygiene = hygiene
		self.fun = fun

	def Printer(stat):
		print("Energy:",stat.energy)
		print("Hygiene:",stat.hygiene)
		print("Fun:",stat.fun)

def Copy(temp):
	stat = Stat(temp.energy,temp.hygiene,temp.fun)
	return stat

def Checker(temp,data):
		if (temp.energy > 15) or (temp.energy < 0):
			print("Aksi tidak valid")
		elif (temp.hygiene > 15) or (temp.hygiene < 0):
			print("Aksi tidak valid")
		elif (temp.fun > 15) or (temp.fun < 0):
			print("Aksi tidak valid")
		else:
			data.energy = temp.energy
			data.hygiene = temp.hygiene
			data.fun = temp.fun
			data.Printer()

def TidurSiang(stat):
	temp = Copy(stat)
	temp.energy = stat.energy + 10
	Checker(temp,stat)

def TidurMalam(stat):
	temp = Copy(stat)
	temp.energy = stat.energy + 15
	Checker(temp,stat)

def MakanHamburger(stat):
	temp = Copy(stat)
	temp.energy = stat.energy + 5
	Checker(temp,stat)

def MakanPizza(stat):
	temp = Copy(stat)
	temp.energy = stat.energy + 10
	Checker(temp,stat)

def MakanSteak(stat):
	temp = Copy(stat)
	temp.energy = stat.energy + 15
	Checker(temp,stat)

def MinumAir(stat):
	temp = Copy(stat)
	temp.hygiene = stat.hygiene - 5
	Checker(temp,stat)

def MinumKopi(stat):
	temp = Copy(stat)
	temp.hygiene = stat.hygiene - 10
	temp.energy = stat.energy + 5
	Checker(temp,stat)

def MinumJus(stat):
	temp = Copy(stat)
	temp.hygiene = stat.hygiene - 5
	temp.energy = stat.energy + 10	
	Checker(temp,stat)
	
def BuangAirKecil(stat):
	temp = Copy(stat)
	temp.hygiene = stat.hygiene + 5
	Checker(temp,stat)
	
def BuangAirBesar(stat):
	temp = Copy(stat)
	temp.hygiene = stat.hygiene + 10
	temp.energy = stat.energy - 5
	Checker(temp,stat)

def SosialisasiKafe(stat):
	temp = Copy(stat)
	temp.fun = stat.fun + 15
	temp.hygiene = stat.hygiene + 5
	temp.energy = stat.energy - 10
	Checker(temp,stat)

def Medsos(stat):
	temp = Copy(stat)
	temp.fun = stat.fun + 10
	temp.energy = stat.energy - 10
	Checker(temp,stat)

def MainKomputer(stat):
	temp = Copy(stat)
	temp.fun = stat.fun + 15
	temp.energy = stat.energy - 10
	Checker(temp,stat)

def Mandi(stat):
	temp = Copy(stat)
	temp.hygiene = stat.hygiene + 15
	temp.energy = stat.energy - 5
	Checker(temp,stat)

def CuciTangan(stat):
	temp = Copy(stat)
	temp.hygiene = stat.hygiene + 5
	Checker(temp,stat)

def Musik(stat):
	temp = Copy(stat)
	temp.fun = stat.fun + 10
	temp.energy = stat.energy - 5
	Checker(temp,stat)

def MembacaKoran(stat):
	temp = Copy(stat)
	temp.fun = stat.fun + 5
	temp.energy = stat.energy - 5
	Checker(temp,stat)

def MembacaNovel(stat):
	temp = Copy(stat)
	temp.fun = stat.fun + 10
	temp.energy =stat.energy - 5
	Checker(temp,stat)

stats = Stat(10,0,0)

while ((stats.hygiene > 0) or (stats.energy > 0) or (stats.fun > 0)) and ((stats.hygiene < 15) or (stats.energy < 15) or (stats.fun < 15)):
	print("Apa yang ingin Anda lakukan kali ini?")
	act = input()
	if (act == "Tidur Siang"):
		TidurSiang(stats)
	elif (act == "Tidur Malam"):
		TidurMalam(stats)
	elif (act == "Makan Hamburger"):
		MakanHamburger(stats)
	elif (act == "Makan Pizza"):
		MakanPizza(stats)
	elif (act == "Makan Steak and Beans"):
		MakanSteak(stats)
	elif (act == "Minum Air"):
		MinumAir(stats)
	elif (act == "Minum Kopi"):
		MinumKopi(stats)
	elif (act == "Minum Jus"):
		MinumJus(stats)
	elif (act == "Buang Air Kecil"):
		BuangAirKecil(stats)
	elif (act == "Buang Air Besar"):
		BuangAirBesar(stats)
	elif (act == "Bersosialisasi ke Kafe"):
		SosialisasiKafe(stats)
	elif (act == "Bermain Media Sosial"):
		Medsos(stats)
	elif (act == "Bermain Komputer"):
		MainKomputer(stats)
	elif (act == "Mandi"):
		Mandi(stats)
	elif (act == "Cuci Tangan"):
		CuciTangan(stats)
	elif (act == "Mendengarkan Musik di Radio"):
		Musik(stats)
	elif (act == "Membaca Koran"):
		MembacaKoran(stats)
	elif (act == "Membaca Novel"):
		MembacaNovel(stats)
	elif (act == "F"):
		break
	else:
		print("Aksi tidak diterima! Silakan coba lagi")
	print("Ingin keluar? Ketik 'Keluar'")
else:
	if (stats.hygiene == 15) and (stats.energy == 15) and (stats.fun == 15):
		print('Congratulations!')
	elif (stats.hygiene == 0) and (stats.energy == 0) and (stats.fun == 0):
		print('Press F for Respect')