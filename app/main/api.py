from flask_restful import Api
from app.main.errors import errors

# Flask API Configuration
api = Api(
    catch_all_404s=True,
    errors=errors
)
