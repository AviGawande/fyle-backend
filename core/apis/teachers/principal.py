# from flask import Blueprint
# from core.apis import decorators
# from core.apis.responses import APIResponse
# from core.models.teachers import Teacher
# from .schema import TeacherSchema

# principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)

# @principal_teachers_resources.route('', methods=['GET'], strict_slashes=False)
# @decorators.authenticate_principal
# def list_teachers(p):
#     """Returns list of all teachers"""
#     teachers = Teacher.get_all().limit(1).all()  # Limit to 1 teacher
#     teachers_dump = TeacherSchema().dump(teachers, many=True)
#     return APIResponse.respond(data=teachers_dump)

from flask import Blueprint
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher
from .schema import TeacherSchema

principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)

@principal_teachers_resources.route('', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of all teachers"""
    teachers = Teacher.query.limit(1).all()  # This will limit the result to 1 teacher
    teachers_dump = TeacherSchema().dump(teachers, many=True)
    return APIResponse.respond(data=teachers_dump)