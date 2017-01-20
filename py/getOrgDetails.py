#usr/bin/python
import psycopg2
import json
import dbConnect
from flask import Flask, request, Response, Blueprint

getOrgDetails_api = Blueprint('getOrgDetails_api', __name__)

@getOrgDetails_api.route("/py/getOrgDetails", methods=['POST'])
def orgList():
	"""
	"""  
	conn = dbConnect.connect()
	curs = conn.cursor()
	myOutput = {}
        myjson = request.json
        organisationId = int(myjson['organisationId'])
        #organisationId = 1
	data = []
	stmt = "select * from org_team full outer join team_under_team on (org_team.team_id = team_under_team.parent_team_id) or (org_team.team_id = team_under_team.child_team_id) right outer join team_repo on (team_repo.team_id = team_under_team.parent_team_id) or (team_repo.team_id = team_under_team.child_team_id) full outer join new_records on (org_team.team_id = new_records.parent_team_id) where org_team.org_id = '%d'"%(organisationId,)
	curs.execute(stmt)
	result = curs.fetchall()
        print result
        for i in result:
            #print "=============iteration ===================data",data
            if organisationId == i[0]:
                teamAlreadyPresent = 0
                subTeamAlreadyPresent = 0 
                flagTeam = 0
                flagRepo = 0
                if i[1] == i[2]:#organisation-team mapping
                     #make a list of team details under the organisation
                     nodes = []
                     orgDetails = {}
                     teamDetails = {}
                     for teams in data:
                         print "teams",teams
                         if teams['title'] == 'team %d'%(i[1]):
                             teamAlreadyPresent = teamAlreadyPresent + 1
                             teamDetails = {'title':'team %d'%(i[3]),'id':'1.2','nodes':[]}
                             print "team already there"
                             if i[3] == i[4]:
                                 for subTeams in teams['nodes']:
                                     if subTeams['title'] == 'team %d'%(i[3]):
                                          print "data already there"
                                          subTeamAlreadyPresent = subTeamAlreadyPresent + 1
                                          repoDetails = {'title':'repo %d'%(i[5]), 'id':'1.2.1', 'nodes':[]}
                                          subTeams['nodes'].append(repoDetails)
                                          for childTeam in subTeams['nodes']:
                                              if childTeam['title'] == 'team %d'%(i[3]):
                                                  childTeam['nodes'].append(repoDetails)
                                 if subTeamAlreadyPresent < 1:
                                     repoDetails = {'title':'repo %d'%(i[5]), 'id':'1.2.1', 'nodes':[]}
                                     teamDetails['nodes'].append(repoDetails)   
                                     teams['nodes'].append(teamDetails)#do only if there is no sub team present
                             else:
                                 for teamList in teams['nodes']:
                                     if teamList['title'] == 'team %d'%(i[3]):
                                         flagTeam = flagTeam + 1
                                         pass
                                     elif teamList['title'] == 'repo %d'%(i[5]):
                                         flagRepo = flagRepo + 1
                                 if flagTeam < 1:
                                     teams['nodes'].append(teamDetails)
                                 if flagRepo < 1:
                                     repoDetails = {'title':'repo %d'%(i[5]), 'id':'1.2.1', 'nodes':[]}
                                     teams['nodes'].append(repoDetails)
                             if i[6] != 'None':
                                 if i[5] == i[6]:
                                     subChildDeatils = {'title':'team %d'%(i[8]), 'id':'1.2.1', 'nodes':[]}
                                     for subTeams in teams['nodes']:
                                         if subTeams['title'] == 'team %d'%(i[7]):
                                             subTeams['nodes'].append(subChildDeatils)
                                             query = "select repo_id from team_repo where team_id = '%d'"%(i[8])
                                             curs.execute(query)
                                             result = curs.fetchone()
                                             if len(result) > 0:
                                                 for node in subTeams['nodes']:
                                                     if node['title'] == 'team %d'%(i[8]):
                                                         print "nodesssssssssssssssssss==========",node['nodes']
                                                         repoDetails = {'title':'repo %d'%(result), 'nodes':[]}
                                                         node['nodes'].append(repoDetails)
                                         #node['nodes'].append({'title':'repo %d'%(result),nodes:[]})
                     if teamAlreadyPresent < 1:                  
                         orgDetails['title'] = 'team %d'%(i[1])
                         orgDetails['id'] = '1'
                         teamDetails = {'title':'team %d'%(i[3]),'id':'1.1','nodes':[]}
                         if i[3] == i[4]:#team-repo mapping
                             repoDetails = {'title':'repo %d'%(i[5]), 'id':'1.1.1', 'nodes':[]}
                             teamDetails['nodes'].append(repoDetails)
                             nodes.append(teamDetails)
                             orgDetails['nodes'] = nodes
                             data.append(orgDetails)
                         else:
                             for i in nodes:
                                 if i['title'] == 'repo %d'%(i[5]):
                                     flagRepo = flagRepo + 1
                             if flagRepo < 1:
                                 repoDetails = {'title':'repo %d'%(i[5]), 'id':'1.2.1', 'nodes':[]}
                                 nodes.append(repoDetails)
                                 orgDetails['nodes'] = nodes
                                 data.append(orgDetails)
        stmt1 = "select * from org_team full outer join team_repo on (team_repo.team_id = org_team.team_id);"
        curs.execute(stmt1)
        result = curs.fetchall()
        for i in result:
            teamPresent = 0
            repoPresent = 0
            print "iiiii",i
            if i[0] == organisationId:
                if i[1] == i[2]:
                    for orgData in data:
                        print orgData
                        if orgData['title'] == 'team %d'%(i[2]):
                            teamPresent = teamPresent + 1
                            for orgNodes in orgData['nodes']:
                                if orgNodes['title'] == 'repo %d'%(i[3]):
                                    repoPresent = repoPresent + 1
                            if repoPresent < 1:
                                repoDetails = {'title':'repo %d'%(i[3]),'nodes':[]}
                                orgData['nodes'].append(repoDetails)
                            pass
                    if teamPresent < 1:
                        orgDetails = {'title':'team %d'%(i[2]),'nodes':[]}
                        data.append(orgDetails)
                                             
        #print "data===============",data
#	if len(result) != 0:
#		for user in result:
#			data.append({'userId' : user[0], 'userName' : user[1], 'fullName' : user[2].title() + " " + user[3].title()})
#
#		myOutput['data'] = data
#	else:
#		myOutput['data'] = data
        	
	myOutput['status'] = 'OK'
        myOutput['data'] = data
	JSONOutput = json.dumps(myOutput)
	JSONResponse = Response(JSONOutput, status=200, mimetype='application/json')
	return JSONResponse
