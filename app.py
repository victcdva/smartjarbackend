from flask import Blueprint
from flask_restful import Api
from resources.WeightData import getAll, getById, addWeight
from resources.JarDevice import getAllJar, getJarById, addJar

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# weight
api.add_resource(getAll, '/getAll')
api.add_resource(getById, '/getById/<int:weight_id>')
api.add_resource(addWeight, '/addWeight')


# jardevice
api.add_resource(getAllJar, '/getAllJar')
api.add_resource(getJarById, '/getJarById/<int:jardevice_id>')
api.add_resource(addJar, '/addJar')
