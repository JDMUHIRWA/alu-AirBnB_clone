# AirBnB clone - The console 🏠🏠

![65f4a1dd9c51265f49d0](https://github.com/Ronnie5562/alu-AirBnB_clone/assets/110787129/9f3f3ede-75d4-44fc-a1b3-7a71152e9633)


# AirBnB Clone Project
## Project Description
This project is an implementation of an AirBnB clone, featuring a command-line interpreter for managing AirBnB objects. The project includes various classes such as User, State, City, Place, Amenity, and Review, all inheriting from a base class named BaseModel. Additionally, an abstracted storage engine (File Storage) is provided for serialization and deserialization of instances.

**Command Interpreter**
The command interpreter allows users to perform operations on AirBnB objects through a shell-like interface. Users can create new objects, retrieve objects from storage, perform operations, update attributes, and destroy objects.

How to Start the Command Interpreter
To start the command interpreter, run the following command:

```$ ./console.py```
How to Use the Command Interpreter
Once in interactive mode, the prompt (hbnb) indicates that the interpreter is ready to receive commands. Use documented commands (type help <topic>) such as EOF, help, and quit.

## Examples
**Interactive Mode**
```
$ ./console.py
(hbnb) create User
(hbnb) show User 1234-5678-9012
(hbnb) update User 1234-5678-9012 email "user@example.com"
```

**Non-Interactive Mode**
```
$ echo "create User" | ./console.py
$ echo "show User 1234-5678-9012" | ./console.py
$ echo "update User 1234-5678-9012 email 'user@example.com'" | ./console.py
```

## Authors 
## 
## [`Jean de Dieu Muhirwa Harerimana`](https://www.linkedin.com/in/jean-de-dieu-muhirwa-harerimana-215551262/)