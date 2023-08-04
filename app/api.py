from flask import request
from flask_appbuilder.api import BaseApi, expose, rison, safe
from flask_appbuilder.security.decorators import protect

from . import appbuilder

greeting_schema = {"type": "object", "properties": {"name": {"type": "string"}}}


class ExampleApi(BaseApi):

    resource_name = "example"
    apispec_parameter_schemas = {"greeting_schema": greeting_schema}

    @expose("/persisting_engin")
    def greeting(self):
        """Send a greeting
        ---
        get:
          responses:
            200:
              description: Greet the user
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      message:
                        type: string
        """

        return self.response(200, message="sucess")


    @expose("/error")
    @protect()
    @safe
    def error(self):
        """Error 500
        ---
        get:
          responses:
            500:
              $ref: '#/components/responses/500'
        """
        raise Exception


appbuilder.add_api(Api)
