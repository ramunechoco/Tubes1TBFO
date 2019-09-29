def Checker(num,var):
	if (num < 0) or (num > 15):
		print('Aksi tidak valid')
	else:
		var = num

def TidurSiang(energy):
	ret = energy + 10
	Checker(ret,energy)

def TidurMalam(energy):
	ret = energy + 15
	Checker(ret,energy)

def MakanHamburger(energy):
	ret = energy + 5
	Checker(ret,energy)

def MakanPizza(energy):
	ret = energy + 10
	Checker(ret,energy)

def MakanSteak(energy):
	ret = energy + 15
	Checker(ret,energy)

def MinumAir(energy):
	ret = hygiene - 5
	Checker(ret,energy)

def MinumKopi(energy,hygiene):
	ret1 = hygiene - 10
	ret2 = energy + 5
	Checker(ret,energy)
	Checker(ret,hygiene)

def MinumJus(energy,hygiene):
	ret1 = hygiene - 5
	ret2 = energy + 10	
	Checker(ret,energy)
	Checker(ret,hygiene)
	
def BuangAirKecil(hygiene):
	ret = hygiene + 5
	Checker(ret,hygiene)
	
def BuangAirBesar(hygiene,energy):
	ret1 = hygiene + 10
	ret2 = energy - 5
	Checker(ret,energy)
	Checker(ret,hygiene)
