from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        data = pd.read_csv('users.csv',delimiter=',')
        data = data.to_dict('records')
        print(data)
        return {'data' : data}, 200


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('carinfo', required=True)
        parser.add_argument('coordinates', required=True)
        parser.add_argument('speed', required=True)
        args = parser.parse_args()

        data = pd.read_csv('users.csv',delimiter=',')

        new_data = pd.DataFrame({
            'name'          : [args['name']],
            'carinfo'       : [args['carinfo']],
            'coordinates'   : [args['coordinates']],
            'speed'         : [args['speed']]
        })

        data = data.append(new_data, ignore_index = True)
        data.to_csv('users.csv', index=False)
        return {'data' : new_data.to_dict('records')}, 201

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()

        data = pd.read_csv('users.csv')

        data = data[data['name'] != args['name']]

        data.to_csv('users.csv', index=False)
        return {'message' : 'Record deleted successfully.'}, 200



# Add URL endpoints
api.add_resource(Users, '/users')

@app.route("/")
def index():
    data = pd.read_csv('users.csv',delimiter=',')
    data = data.to_dict('records')
    return render_template('pf.html',data=data)

if __name__ == '__main__':
    app.run()
