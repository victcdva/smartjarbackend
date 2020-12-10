from flask_restful import Resource
from flask import Flask, request
from models import db, JarDevice, JarDeviceSchema

jardevice_schema = JarDeviceSchema()
jardevices_schema = JarDeviceSchema(many=True)

# https://rahmanfadhil.com/flask-rest-api/


class getAllJar(Resource):
    def get(self):
        jardevices = JarDevice.query.all()
        jardevices = jardevices_schema.dump(jardevices)
        return {'error': False, 'data': jardevices, 'count': len(jardevices)}, 200


class getJarById(Resource):
    def get(self, jardevice_id):
        jardevice = WeightData.query.get_or_404(jardevice_id)
        jardevice = jardevice_schema.dump(jardevice)
        return {'error': False, 'data': jardevice}, 200


class addJar(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {"error": True, "message": "No input data provided"}, 400

        jardevice = JarDevice(
            name=json_data['name'],
            value=json_data['value'],
            weight_id=json_data['weight_id'],
        )

        db.session.add(jardevice)
        db.session.commit()

        result = jardevice_schema.dump(jardevice)
        return {"error": False, "message": "Device was added successfully", "data": result}, 201
