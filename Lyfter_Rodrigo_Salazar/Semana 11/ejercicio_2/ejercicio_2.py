class Person():
	def __init__(self, name):
		print(f"Ha nacido una persona llamada {name}!")
		self.name = name
		self.age = 0
		
class Bus():
	def __init__(self):
		self.max_passengers = 15
		self.passengers = []
    
	def add_passengers(self,person):
		if len(self.passengers) < self.max_passengers:
			self.passengers.append(person.name)
		else:
			print("El bus esta lleno no puede agregar más pasajeros")
	
	def remove_passenger (self):
		if len(self.passengers) > 0:
			person_to_remove = input("A quein deseas bajar del bus? ")
			if person_to_remove in self.passengers:
				self.passengers.remove(person_to_remove)
			else:
				print(person_to_remove + " no esta en el bus")


bus = Bus()
continue_running = True
while(continue_running):
	try:
		user_input = input("Escriba y si desea agregar personas, n si desea salir o s para sacar a una persona del bus: ").lower()

		if user_input == "n":
			continue_running = False

		elif user_input == "y":
			name = input("Ingrese el nombre de la persona a ingresar al bus: ")
			person = Person(name)
			bus.add_passengers(person)
			print(bus.passengers)

		elif user_input == "s":
			bus.remove_passenger()
		else:
			raise ValueError
	except ValueError as exception:
		print("Favor solo usar y o n, cualquier otro valor no es permitido")

		
		




		
