#usr/bin/python
import psycopg2
import json
import dbConnect
from flask import Flask, request, Response, Blueprint
import itertools
import operator

getUserOrg_api = Blueprint('getUserOrg_api', __name__)

@getUserOrg_api.route("/py/getUserOrg", methods=['POST'])
def orgStructure():
	"""
	"""  
	conn = dbConnect.connect()
	curs = conn.cursor()
	myOutput = {}
        myjson = request.json
        userId = 1
	data = []
        #Fetch the teamIds/repoIds the user is associated with 
        stmt = "select repoids,teamids from users where userid = '%d'"%(userId);
	curs.execute(stmt)
	result = curs.fetchall()
        print result
        for i in result:
            i = list(i)
            for repo in i[0]:
                userOrg = {}
                userOrg['repo'] = 'Repo %d'%(repo)
                getTeamIdQuery = "select team_id from team_repo where repo_id = '%d'"%(repo)
                curs.execute(getTeamIdQuery)
                teamId = curs.fetchone()
                if teamId:
                    userOrg['team'] = 'Team %d'%(teamId)
                getOrgIdQuery = "select org_id from org_team where team_id = (select parent_team_id from team_under_team where child_team_id = (select team_id from team_repo where repo_id = '%d'))"%(repo)
                curs.execute(getOrgIdQuery)
                orgId = curs.fetchone()
                if orgId:
                    userOrg['org'] = 'Org %d'%(orgId)
                else:
                    getOrgIdQuery1 = "select org_id from org_team where team_id = '%d'"%(teamId)
                    curs.execute(getOrgIdQuery1)
                    orgId1 = curs.fetchone()
                    if orgId1:
                        userOrg['org'] = 'Org %d'%(orgId1)
                data.append(userOrg)
            for team in i[1]:
                userOrg = {}
                userOrg['team'] = 'Team %d'%(team)
                query = "select org_id from org_team where team_id = '%d'"%(team)
                curs.execute(query)
                orgId = curs.fetchone()
                if orgId:
                    userOrg['org'] = 'Org %d'%(orgId)
                data.append(userOrg)
        newData = {}
        repos = []
        for key,grp in itertools.groupby(data, key=operator.itemgetter('team')):
                a = list(grp)  
                              
                newData[key] = a
        print newData                                         
	myOutput['status'] = 'OK'
        myOutput['data'] = newData
	JSONOutput = json.dumps(myOutput)
	JSONResponse = Response(JSONOutput, status=200, mimetype='application/json')
	return JSONResponse
