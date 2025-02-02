from flask_restful import Resource
from src.apps.services import Tokens as Service, layout_cache
from . import helpers


class Tokens(Resource):
    @layout_cache.cached(query_string=True)
    @helpers.with_errors_handler
    @helpers.with_help(
        f"""Get tokens information
        {helpers.OUTPUT_FORMATTER_HELP}
        """
    )
    @helpers.with_output_formatter
    def get(self):
        return Service().all()
