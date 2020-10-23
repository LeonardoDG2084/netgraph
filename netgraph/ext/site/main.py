from flask import Blueprint, current_app, render_template, request, redirect
from netgraph.ext.site.controllers import create_indice, get_all_indices, get_total_docs, delete_indice, search_connections, graphviz_generate

bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    # For 
    indices = get_all_indices()
    return render_template("index.html", indices=indices)

@bp.route("/", methods=['POST'])
def search_connection():
    data = {}
    for key, value in request.form.items():
        if value:
            data.update({key : value})
    search_response = search_connections("tivit", **data)
    graphviz_generate(search_response)
    return render_template("search_statistics.html")


@bp.route("/project")
def project():
    # Actions from projects
    if request.args.get('action') == "delete":
        indice = request.args.get('indice')
        print(request.args.get('indice'))
        delete_indice(indice)

        redirect("/project")
    if request.args.get('action') == "clean":
        print("limpo")

    # List all indices from ElasticSearch for Project 
    indices = get_all_indices()
    for indice in indices:
        count = get_total_docs(indice)
        indices[indice] = count[2]

    return render_template("project.html", indices=indices)

@bp.route("/project", methods=['POST'])
def add_project():
    create_indice(request.form['project'])
    return redirect("/project")
