# mongo.py
from copy import copy
import logging

from bson.objectid import ObjectId
from bson.errors import InvalidId
from flask import Response
from flask import jsonify
from flask import request

from json_validator import validate_json
from consts import *
from schema import add_tabs_schema
from config import app, mongo, tabs


LOGGER = logging.getLogger("api.py")

@app.route('/tabs', methods=['GET'])
def get_all_tabs():
    """
    Get All Tabs in DB
    :return: list of dictionaries
    """
    tab_records = tabs.find()
    if not tab_records:
        return Response(status=404)
    result = []
    for tab_record in tab_records:
        tab_record[ID] = tab_record[ID].__str__()
        result.append(tab_record)
    resp = jsonify({
        "result": result
    })
    resp.status_code = 202
    return resp


@app.route('/tabs/<tabsID>', methods=['GET'])
def get_one_tabs(tabsID):
    """
    Get Tabs Record Matching with ID
    :param tabsID: tabsID <str>
    :return: dictionary
    """
    try:
        tab_record = tabs.find_one({ID: ObjectId(tabsID)})
    except InvalidId as ex:
        response = jsonify({"message": f"Invalid Object ID: {tabsID}"})
        response.status_code = 400
        return response
    if not tab_record:
        return Response(status=404)
    tab_record[ID] = tab_record[ID].__str__()
    resp = jsonify({
        "result": tab_record
    })
    resp.status_code = 202
    return resp


# TODO Fix issue in json validator
@app.route('/tabs', methods=['POST'])
@validate_json(add_tabs_schema)
def add_star():
    """
    Insert One record in tabs DB
    :return: tabsID <str>
    """
    data = request.get_json(force=True)
    insertedID = tabs.insert(data)
    return jsonify({'tabsID': insertedID.__str__()})


@app.route('/tabs/<tabsID>', methods=['DELETE'])
def delete_one_tabs(tabsID):
    """
    Delete Tabs record from DB
    :param tabsID: tabsID
    :return: Success Message
    """
    tabs = mongo.db.tabs
    tab_record = tabs.delete_one({ID: ObjectId(tabsID)})
    if not tab_record.deleted_count:
        return Response(status=404)
    return jsonify({"Message": f"Record DELETED Successfully for ID: {tabsID}!"})


@app.route('/tabs/<tabsID>', methods=['PUT'])
def update_one_tabs(tabsID):
    """
    Update existing Record
    :param tabsID: TabsID <str>
    :return: successs message
    """
    data = request.get_json(force=True)
    tab_record = tabs.find_one({ID: ObjectId(tabsID)})
    if not tab_record:
        return Response(status=404)

    updated_record = copy(tab_record)
    if data.get(NAME):
        updated_record[NAME] = data[NAME]

    if data.get(DESCRIPTION):
        updated_record[DESCRIPTION] = data[DESCRIPTION]

    if data.get(DATA_POINTS):
        if updated_record.get(DATA_POINTS):
            updated_record[DATA_POINTS].append(data[DATA_POINTS])
        else:
            updated_record[DATA_POINTS] = data[DATA_POINTS]
    res = tabs.save(updated_record)
    return jsonify({"Message": f"Record Updated Successfully for ID: {res.__str__()}!"})


if __name__ == '__main__':
    app.run(debug=True)
