# ✨ Parcial Final ✨ 

Se centro principalmente en solucion de la problematica asociada con la aerolinea que pretende llevar mascotas en vuelos. Solicitando construir un desarrollo funcional que permita a los usuarios reservar y comprar vuelos en los que sus mascotas son lo principal. Cualquier Usuario puede conectarse al sistema , ver vuelos disponibles y hacer reservas para viajar con su mascota y finalizar la compra, de la misma forma tambien se puede consultar la cantidad de mascotas que ya tienen un boleto comprado en el vuelo.


# ✨ Características Principales ✨

  🏠 Interfaz desplegable y disponible para su uso: Navegacion intuitiva y facil de usar.
  
  📱 Registro para Usuarios y mascotas de los Usuarios: Se puede crear, editar, buscar y eliminar los registrso. 
  
  ✈️​ Gestion de los vuelos: Se pueden reservar vuelos segun la disponibilidad y consultar informacion genereal.
  
  🗃️ Múltiples Persistencias: Soporte para CSV, SQLite y PostgreSQL (en servidor de clever).
  
  👥​🐕 Tipado de Usuario y Mascotas: Sistema de clasificación por destino, mascota, raza.
  
  📊 Documentación: Se registra cada parte del proycto, y como fue su desarrollo.


# 🌟​ Estilo y Funcionalidades 🌟​

​💙​✅ Versión Pre parcial.

  -Planteamiento de los registros.
 
  -Diseño para el desplegable.
  
  -Planteamiento para la consultas de vuelos.
  
  -Planteamiento para la reserva de los vuelos.

💙​✅ Versión Construcion en parcial.

  -Desplegable funcional.
  
  -Uso funcional para ambos registros.
  
  -Operaciones de base de datos
  
  -Consultas y reservas para vuelos funcionales.
  
  -Estructuracion de proyecto completa.
  

# 👔​ Modelado de las entidades 👔​

📊 Diagrama de Entidades.

![imagen](https://github.com/user-attachments/assets/072820fd-8398-4962-bb4f-74eb7cfe6019)

⚙️​ Modelo Principal

@startuml

actor Usuario

actor Administrador

Usuario --> (Registrar usuario)

Usuario --> (Registrar mascota)

Usuario --> (Consultar vuelos disponibles)

Usuario --> (Reservar vuelo para mascota)

Usuario --> (Consultar mis mascotas)

Usuario --> (Consultar mis reservas)

(Registrar mascota) --> (Registrar usuario) : <>

(Reservar vuelo para mascota) --> (Consultar vuelos disponibles) : <>

(Consultar mis reservas) --> (Consultar mis mascotas) : <>

Administrador --> (Crear vuelo)

@enduml


# 🚧​ Estructura de Proyecto ​🚥​

📊​ Modelos 

- Modelo Mascotas.
  
![imagen](https://github.com/user-attachments/assets/58f7ee24-523f-4dac-b1aa-bbbe73353d75)

- Modelo Usuarios.
  
![imagen](https://github.com/user-attachments/assets/4d20ae05-ffc8-41c9-a433-be5a25cf3587)

- Modelo Vuelos.

![imagen](https://github.com/user-attachments/assets/f8842b72-b9b6-4eda-bf8d-879c3d3dc05c)


💹​ Operaciones

- Operaciones Mascotas.
  
![imagen](https://github.com/user-attachments/assets/7c7136ec-25d3-43d8-86af-ead77fd4cccd)

- Operaciones Usuarios.
  
![imagen](https://github.com/user-attachments/assets/e6773cd7-dc0a-411b-a0e3-9b3953d6c85e)

- Operaciones Vuelos.

![imagen](https://github.com/user-attachments/assets/4fe99d98-f1e8-42cd-bc08-0590d987c149)


📡​ Conexion

➿​ Router


# 📉​ Diagrama de Casos de Uso 📉​

Parcial Final/
│
├── main.py
├── requirements.txt
├── README.md

├── test_main.http
│
├── models/
│ ├── init.py
│ ├── models_mascotas.py
│ ├── models_users.py
│ ├── models_vuelos.py
│
├── operations/
│ ├── init.py
│ ├── operations_mascotas.py
│ ├── operations_users.py
│ ├── operations_vuelos.py
│
├── conections/
│ ├── init.py
│ ├── Conección_db.py
│
└── pycache/


# 📈 Diagrama de Clases 📈 

🧔​ Registro Usuario

![imagen](https://github.com/user-attachments/assets/8d894fcf-ff95-49a7-85b9-dc450a80994d)

🐈‍⬛​ Registro Mascota 

![imagen](https://github.com/user-attachments/assets/ed0f24b1-7a01-44ed-aaff-286550c80725)

🚀​ Registro Vuelos

![imagen](https://github.com/user-attachments/assets/60e10dd9-af30-4b0f-9ef7-e1d9ac075aed)


