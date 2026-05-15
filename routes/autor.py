from flask import Blueprint, request, jsonify
from models.autor import Autor
from repository.repositorio_autor import RepositorioAutor

autor_bp = Blueprint('autor', __name__, url_prefix='/autores')
repositorio = RepositorioAutor()

@autor_bp.route('/', methods=['GET'])
def obtener_autores():
    autores = repositorio.obtener_todos()
    return jsonify([autor.get_diccionario() for autor in autores]), 200

@autor_bp.post("/")
def crear():
    datos = request.get_json()
    if not datos or not datos.get('nombre'):
        return jsonify({"error": "No se proporcionaron datos"}), 400

    nuevo_autor = Autor(nombre=datos['nombre'])
    repositorio.crear(nuevo_autor)

    return jsonify(nuevo_autor.get_diccionario()), 200

@autor_bp.put("/<int:id>")
def actualizar(id):
    autor = repositorio.obtener_por_id(id)
    if not autor:
        return jsonify({"error": "Autor no encontrado"}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({"error": "No se proporcionaron datos"}), 400

    if 'nombre' in datos:
        autor.nombre = datos['nombre']
    if 'pais' in datos:
        autor.pais = datos['pais']

    repositorio.actualizar()
    return jsonify(autor.get_diccionario()), 200

@autor_bp.delete("/<int:id>")
def eliminar(id):
    autor = repositorio.obtener_por_id(id)
    if not autor:
        return jsonify({"error": "Autor no encontrado"}), 404

    repositorio.eliminar(autor)
    return jsonify({"mensaje": f"Autor {id} eliminado correctamente"}), 200