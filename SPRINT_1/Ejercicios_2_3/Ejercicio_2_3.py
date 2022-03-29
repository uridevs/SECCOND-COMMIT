from argon2 import PasswordHasher #utilizamos directamente la librería argon2-cffi para hashear con argon2

ph = PasswordHasher()
users = []

#función que hashea la contraseña
def pass_hasher(pwd):
	pwd_to_hash = pwd
	pwd_hashed = ph.hash(pwd)
	return pwd_hashed


'''función que comprueba si la contraseña coincide con la hasheada'''
def pass_checker(pwd_hashed, pwd):
	try:
		ph.verify(pwd_hashed, pwd)
		return True
	except:
		return False


'''función que comprueba si el usuario ya existe'''
def check_if_user(mail):
	if any(mail in user for user in users):
		return True
	else:
		return False


'''función que registra al usuario si no está ya registrado'''
def register(mail, pwd):
	if not check_if_user(mail):
		user_pwd_hashed = pass_hasher(pwd)
		users.append([mail,user_pwd_hashed])
		print(f"{mail} fue registrado con éxito")
		return True
	else:
		print(f"{mail} ya está registrado, introduzca otro correo o inicie sesion")
		return False

#función que gestiona el Login según las indicaciones recibidas
def login(mail,pwd):
	if check_if_user(mail):
		for user in users:
			if user[0]==mail:
				user_pwd_hashed=user[1]
				if pass_checker(user[1],pwd):
					return 1
				else:
					return -2
	else:
		return -1



register("manolito@gmail.com", "Manolito123")
register("manol2to12@gmail.com", "jaja123")
register("minanolito33@yopmail.com", "asdf123")
register("manolito@gmail.com", "Manolito123")
register("pachon12@gmail.com", "jojo123")



print(login("manolito@gmail.com", "Manolito123"))

