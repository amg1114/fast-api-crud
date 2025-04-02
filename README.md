# Ejemplo CRUD con FastAPI

Una API simple para operaciones CRUD construida con FastAPI para gestionar artículos.

## 🌐 Despliegue en la nube
La API está desplegada en [Render](https://fast-api-crud-44cz.onrender.com/) 

- **Docs**: https://fast-api-crud-44cz.onrender.com/docs
- **API**: https://fast-api-crud-44cz.onrender.com/

## 💻 Ejecución local

Para ejecutar este proyecto localmente, sigue estos pasos:

1. **Requisitos previos**:
   - Python 3.7+ instalado
   - Gestor de paquetes pip

2. **Instalar dependencias**:
   ```bash
   pip install fastapi uvicorn
   ```

3. **Ejecutar la aplicación**:
   ```bash
   uvicorn main:app --reload
   ```

4. **Acceder a la API**:
   - Documentación interactiva: http://localhost:8000/docs
   - URL base de la API: http://localhost:8000

## 📚 Endpoints de la API

### Crear Artículo
- **Endpoint:** `POST /items/`
- **Descripción:** Añade un nuevo artículo al inventario
- **Cuerpo de la solicitud:**
  ```json
  {
    "id": 1,
    "name": "string",
    "category": "string",
    "description": "string",
    "price": 0.0,
    "quantity": 0,
    "image_url": "string"
  }
  ```

### Leer Artículo
- **Endpoint:** `GET /items/{item_id}`
- **Descripción:** Obtiene los detalles de un artículo específico
- **Parámetro de ruta:** `item_id` (entero)

### Actualizar Artículo
- **Endpoint:** `PUT /items/{item_id}`
- **Descripción:** Actualiza un artículo existente
- **Parámetro de ruta:** `item_id` (entero)
- **Cuerpo de la solicitud:** Igual que Crear Artículo

### Eliminar Artículo
- **Endpoint:** `DELETE /items/{item_id}`
- **Descripción:** Elimina un artículo del inventario
- **Parámetro de ruta:** `item_id` (entero)
- **Respuesta:**
  ```json
  {
    "message": "Artículo eliminado correctamente"
  }
  ```

## 📖 Documentación
La documentación interactiva está disponible en:
- `/docs` - Interfaz Swagger UI
- `/redoc` - Documentación ReDoc

Nota: Reemplaza `main` en el comando de ejecución si tu archivo Python tiene otro nombre.

---

# Autor

Johan Alejandro Moreno Gil [@amg1114](https://github.com/amg1114)