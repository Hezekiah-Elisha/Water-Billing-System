from flask import jsonify, request
from .models.Admin import Admin
from .models.MaAdmin import admin_schema, admins_schema
from werkzeug.security import generate_password_hash, check_password_hash


from . import admin


@admin.cli.command('create_admin')
def create_admin():
    """Create admin: Contains auto filled fields"""
    hashed_password = generate_password_hash('Myadminpassword123', method='sha256')
    admin = Admin(name='Admin',
                    email='admin@water_system.com',
                    phone='08012345678',
                    location='Nairobi',
                    password='hashed_password')
    admin.save()
    print('Admin created')


@admin.route('/test', methods=['GET'])
def test():
    return jsonify(message='Admin endpoint working'), 200


@admin.route('/', methods=['GET'])
def get_all_admins():
    admins = Admin.get_all_admins()
    if not admins:
        return jsonify(message='No admins found'), 404
    result = admins_schema.dump(admins)
    return jsonify(result), 200