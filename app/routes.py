"""
routes.py
~~~~~~~~
Module containing helper function for configuring routes
"""


class Routes(object):

    @staticmethod
    def register_routes(api, app):
        """
        Method to register each entity's route for API Gateway.
        :param: api
        :param: app
        """
        from app.controllers import register_routes
        # Add routes
        register_routes(api, app)
