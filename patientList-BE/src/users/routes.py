# users/routes.py
import json
from flask import render_template, url_for, flash, redirect, request, Blueprint, jsonify, abort
from flask_login import login_user, current_user, logout_user, login_required
from src import db, bcrypt
from src.models import User
from src.config import Config
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, decode_token
)


SECRETKEY = Config.SECRET_KEY

users = Blueprint("users", __name__)

# DECLARE NECESSARY GLOBALS
response = {
    'status': 200,
    'message': 'OK',
    'result': []
}

@staticmethod
@users.route("/users/register", methods=['POST'])
def register():
    print("REGSITER NEW USER")
    print(request.form, "\n\n")
    nik =  request.form.get('nik')

    rawUser = {
        'name': request.form.get('name'),
        'nik': request.form.get('nik'),
        'saab': request.form.get('saab'),
        'cell_no': request.form.get('cell_no'),
        'address': request.form.get('address'),
        'religion': request.form.get('religion'),
        'education': request.form.get('education'),
        'blood_type':  request.form.get('blood_type')
    }

    print("this is rawUSer")
    print(rawUser)


    userExist = User.query.filter_by(nik=nik).first()

    if (userExist is not None):
        abort(400)
    else:
        user = User(rawUser)
        user.save()

        newUser = User.query.filter_by(nik=nik).first()
        newUser1 = User.as_dict(newUser)

        response['status'] = 201
        response['message'] = 'REGISTER SUCCESS'
        response['result'] = newUser1

        return jsonify(response)


@staticmethod
@users.route("/users/getall", methods=['GET'])
def getAll():
    print("GETTING ALL USER @ USER ROUTES")
    listUsers = User.get_all()

    newUserList = []

    # SERIALIZE EACH OBJECT INSIDE A LIST
    for user in listUsers:
        userJSON = User.as_dict(user)
        newUserList.append(userJSON)
    
    # print("HELLO LADIES! LET'S SEE USERS' LIST \n\n")
    # print(newUserList)

    response['status'] = 200
    response['message'] = 'FETCH ALL SUCCESS'
    response['result'] = newUserList

    return jsonify(response)



@staticmethod
@users.route("/users/getByNIK/<string:nik>", methods=['GET'])
def getOneByNIK(nik):
    user = User.query.filter_by(nik=nik).first_or_404()

    # print("GETTING ONE USERNAME BY USERNAME \n")
    # print(user)

    userJSON = User.as_dict(user)

    response['status'] = 200
    response['message'] = 'SUCCESS: GET BY USERNAME'
    response['result'] = userJSON

    return jsonify(response)



@staticmethod
@users.route("/users/getById/<string:userid>", methods=['GET'])
def getOneById(userid):
    user = User.query.filter_by(id=userid).first_or_404()

    # print("GETTING ONE USERNAME BY ID \n")
    # print(user)

    userJSON = User.as_dict(user)

    response['status'] = 200
    response['message'] = 'SUCCESS: GET BY ID'
    response['result'] = userJSON

    return jsonify(response)



# update user
@users.route("/users/editUser/<string:userid>", methods=['PUT'])
def editUser(userid):
    user2Edit = User.query.filter_by(id=int(userid)).first_or_404()

    print("USER2 EDIT")
    print(user2Edit, "\n")

    print("UPDATING USER")
    print(request.form, "\n")

    updInfo = {
        'name': request.form.get('name'),
        'nik': request.form.get('nik'),
        'saab': request.form.get('saab'),
        'cell_no': request.form.get('cell_no'),
        'address': request.form.get('address'),
        'religion': request.form.get('religion'),
        'education': request.form.get('education'),
        'blood_type':  request.form.get('blood_type')
    }

    user2Edit.update(updInfo)

    responseMsg = {
        "status": 200,
        "message": "Patient Info Edited"
    }

    return responseMsg



# delete user
@users.route("/users/deleteUser/<string:userid>", methods=['DELETE'])
def dropUser(userid):
    user2Drop = User.query.filter_by(id=userid).first_or_404()
    db.session.delete(user2Drop)
    db.session.commit()

    responseMsg = {
        "status": 200,
        "message": "Patient Dropped From List."
    }

    return responseMsg