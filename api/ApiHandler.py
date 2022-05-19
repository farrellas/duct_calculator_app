from flask_restful import Api, Resource, reqparse

class ApiHandler(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'Testing 123'
        }

    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('message', type=str)

        args = parser.parse_args()

        print(args)

        request_type = args['type']
        request_json = args['message']

        ret_status = request_type
        ret_msg = request_json

        if ret_msg:
            message = f"Your Message Requested: {ret_msg}"
        else:
            message = "No Message"

        final_ret = {'status': 'success', 'message': message}

        return final_ret