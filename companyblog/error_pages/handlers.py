## Views.py file for error handling

from flask import Blueprint, render_template

error_pages = Blueprint('error_pages', __name__)

## not "route" since we need to connect to general error
@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html'), 404 ## tuple

@error_pages.app_errorhandler(403)
def error_403(error): ## when something is forbidden
    return render_template('error_pages/403.html'), 403