from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine, inspect
from user import User
from address import Address
from cars import Car
from pprint import pprint

metadata_obj = MetaData()


DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)

inspector = inspect(engine)


# Punto 2 - Ejercicios ORM
user_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
    schema="orm_week_5"
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("orm_week_5.users.id"), nullable=False), 
    Column("email_address", String, nullable=False),
    schema="orm_week_5"
)

cars_table = Table(
    "cars",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("orm_week_5.users.id"), nullable=True), # Los autos pueden no tener usuario
    Column("make", String, nullable=False),  # Marca del auto
    Column("model", String, nullable=False),  # Modelo del auto
    Column("year", Integer),  # Año del auto
    Column("license_plate", String(20), unique=True),  # Placa/matrícula
    Column("color", String(30)),  # Color del auto
    schema="orm_week_5"
)


# Punto 3 - Ejercicios ORM
if not inspector.has_table("users", schema="orm_week_5"):
    print("La tabla 'users' no existe. Creando...")
    user_table.create(engine)
    print("✓ Tabla 'users' creada exitosamente.")
else:
    print("✓ La tabla 'users' ya existe.")

if not inspector.has_table("address", schema="orm_week_5"):
    print("La tabla 'address' no existe. Creando...")
    address_table.create(engine)
    print("✓ Tabla 'address' creada exitosamente.")
else:
    print("✓ La tabla 'address' ya existe.")

if not inspector.has_table("cars", schema="orm_week_5"):
    print("La tabla 'cars' no existe. Creando...")
    cars_table.create(engine)
    print("✓ Tabla 'cars' creada exitosamente.")
else:
    print("✓ La tabla 'cars' ya existe.")

user = User(user_table, engine, cars_table) 
address = Address(address_table, engine)
car = Car(cars_table, engine)

# Punto 4 - Ejercicios ORM
    #Punto a
#User methods
#user.insert_user("Genaro", "Genaro Brenes")
#user.update_user("name", "Nil",{"name": "Fairlie", "fullname": "Fairlie Janousek"})
#print(user.delete_user("id", 7))
    
    #Punto b
#address.insert_address(4,"rodsal16@gmail.com")
#address.update_address("id", "1", {"email_address": "patrickstar@gmail.com"})
#address.delete_address("id", "1")

    #Punto c 
#car.insert_car("1","Mercedes benz", "GLA-200", "2016", "RYC-321","negro")
#car.insert_car_without_user("Jeep", "Wrangler", "2020", "JHS456", "negro")
#car.update_car("model", "Rav4", {"color": "blanco"})
#car.delete_car("model", "Rav4")

    #Punto d
#car.assign_user_to_car("2","HER453")

    #punto e
#user_select = user.select_users()
#pprint(user_select)

    #Punto f
#address_select = address.select_addresses()
#pprint(address_select)

    #Punto g
#car_select = car.select_cars()
#pprint(car_select)

#Ejercicios Extra Punto 1
#car_select_null = car.select_cars_without_user()
#pprint(car_select_null)

# Ejercicios Extra Punto 2 - Usuarios con más de un carro
#users_multiple_cars = user.assign_more_than_1_car()
#pprint(users_multiple_cars)








