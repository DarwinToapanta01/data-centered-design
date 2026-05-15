from flask import Blueprint, request, jsonify
from models.paper import Paper
from repository.repositorio_paper import RepositorioPaper

paper_bp = Blueprint('paper', __name__, url_prefix='/papers')
repositorio = RepositorioPaper()

@paper_bp.route('/', methods=['GET'])
def obtener_papers():
    papers = repositorio.obtener_todos()
    return jsonify([paper.get_diccionario() for paper in papers]), 200

@paper_bp.post("/")
def crear():
    datos = request.get_json()
    if not datos or not datos.get('titulo') or not datos.get('doi') or not datos.get('id_autor'):
        return jsonify({"error": "No se proporcionaron datos"}), 400

    nuevo_paper = Paper(
        titulo=datos['titulo'],
        doi=datos['doi'],
        id_autor=datos['id_autor']
    )
    repositorio.crear(nuevo_paper)

    return jsonify(nuevo_paper.get_diccionario()), 200

@paper_bp.put("/<int:id>")
def actualizar(id):
    paper = repositorio.obtener_por_id(id)
    if not paper:
        return jsonify({"error": "Paper no encontrado"}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({"error": "No se proporcionaron datos"}), 400

    if 'titulo' in datos:
        paper.titulo = datos['titulo']
    if 'doi' in datos:
        paper.doi = datos['doi']
    if 'id_autor' in datos:
        paper.id_autor = datos['id_autor']

    repositorio.actualizar()
    return jsonify(paper.get_diccionario()), 200

@paper_bp.delete("/<int:id>")
def eliminar(id):
    paper = repositorio.obtener_por_id(id)
    if not paper:
        return jsonify({"error": "Paper no encontrado"}), 404

    repositorio.eliminar(paper)
    return jsonify({"mensaje": f"Paper {id} eliminado correctamente"}), 200