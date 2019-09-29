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

def medsos(fun, energy):
	ret1 = fun + 10
	ret2 = energy - 10
	Checker(ret1,fun)
	Checker(ret2,energy)

def main_komputer(fun, energy):
	ret1 = fun + 15
	ret2 = energy - 10
	Checker(ret1,fun)
	Checker(ret2,energy)

def mandi(hygiene, energy):
	ret1 = hygiene + 15
	ret2 = energy - 5
	Checker(ret1,hygiene)
	Checker(ret2,energy)

def cuci_tangan(hygiene):
	ret = hygiene + 5
	Checker(ret,hygiene)

def musik(fun, energy):
	ret1 = fun + 10
	ret2 = energy - 5
	Checker(ret1,fun)
	Checker(ret2,energy)

def membaca_koran(fun, energy):
	ret1 = fun + 5
	ret2 = energy - 5
	Checker(ret1,fun)
	Checker(ret2,energy)

def membaca_novel(fun, energy):
	ret1 = fun + 10
	ret2 = energy - 5
	Checker(ret1,fun)
	Checker(ret2,energy)