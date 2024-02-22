from flask import Blueprint, request, jsonify
from backup import backup_dir

backup_route = Blueprint('backup', __name__)

@backup_route.route('/backup', methods=['POST'])
def backup():
    data = request.get_json()
    userdir = data.get('userdir')
    backup_dir_name = data.get('backup_dir_name')
    dir_for_backup = data.get('dir_for_backup')

    backup_result = backup_dir(userdir=userdir, backup_dir_name=backup_dir_name, dir_for_backup=dir_for_backup)
    return jsonify({ "backup_result":backup_result })