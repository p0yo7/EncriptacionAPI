# EncriptacionAPI

Se prenden server cliente y servidor
```
python server.py
```
```
python client.py
```
La ruta de la imagen ya esta definida para que sea apple.png
Se llama el cliente desde postman como post:
```
http://localhost:5000/image
```
Se utiliza el resultado como body completo para usar un get en el servidor
```
http://localhost:5001/image
```
Y se genera una imagen .png llamada result que contiene la imagen visible
