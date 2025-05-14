class Person():
	def __init__(self, name, age):
		print(f"Ha nacido una persona llamada {name}!")
		self.name = name
		self.age = age
		
class Bus():
	def __init__(self):
		self.max_passengers = 15
		self.passengers = []
    
	def add_passengers(self,person):
		if len(self.passengers) < self.max_passengers:
			self.passengers.append(person)
		else:
			print("El bus esta lleno no puede agregar más pasajeros")
	
	def remove_passenger (self):
		if len(self.passengers) > 0:
			person_to_remove = input("A quein deseas bajar del bus? ")
			for passenger in  self.passengers:
				if person_to_remove == passenger.name:
					passenger_to_remove = True
					self.passengers.remove(passenger)
					break
				else:
					passenger_to_remove = False
			if passenger_to_remove == False:
				print(person_to_remove + " no esta en el bus")


bus = Bus()
continue_running = True
while(continue_running):
	try:
		user_input = input("Escriba y si desea agregar personas, n si desea salir, s para sacar a una persona del bus" \
		"o i para imprimir las personas que estan en el bus: ").lower()

		if user_input == "n":
			continue_running = False

		elif user_input == "y":
			name = input("Ingrese el nombre de la persona a ingresar al bus: ")
			try:
				age = int(input("Ingrese la edad de " + name + ": "))
			except ValueError:
				age = 0
				print ("La edad es invalida porque no es un número entero, se asigno la edad en 0 por defecto")
			person = Person(name,age)
			bus.add_passengers(person)

		elif user_input == "s":
			bus.remove_passenger()
		
		elif user_input == "i":
			for passenger in bus.passengers:
				print("Pasajero: ")
				print("Nombre: " + passenger.name + " - Eddad: " + str(passenger.age))

		else:
			raise ValueError
	except ValueError as exception:
		print("Favor solo usar y o n, cualquier otro valor no es permitido")

		
		




		
