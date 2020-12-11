from flask_restful import Resource
from flask import Flask, request
from models import db, WeightData, WeightDataSchema

weight_data = WeightDataSchema()
weights_data = WeightDataSchema(many=True)

# https://rahmanfadhil.com/flask-rest-api/


class getAll(Resource):
    def get(self):
        weights = WeightData.query.all()
        weights = weights_data.dump(weights)
        return {'error': False, 'data': weights, 'count': len(weights)}, 200


class getById(Resource):
    def get(self, weight_id):
        weight = WeightData.query.get_or_404(weight_id)
        weight = weight_data.dump(weight)
        return {'error': False, 'data': weight}, 200


class addWeight(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {"error": True, "message": "No input data provided"}, 400

        weight = WeightData(
            value=json_data['value'],
            description=json_data['description']
        )

        db.session.add(weight)
        db.session.commit()

        result = weight_data.dump(weight)
        return {"error": False, "message": "Weight was added successfully", "data": result}, 201
