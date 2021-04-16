isldata=[
    {"team":"mumbai","mp":20,"won":12,"drwan":4,"loss":4,"pts":40},
    {"team":"mp","mp":20,"won":12,"drwan":4,"loss":4,"pts":40},
    {"team":"ne","mp":20,"won":8,"drwan":9,"loss":3,"pts":33},
    {"team":"fcg","mp":20,"won":7,"drwan":10,"loss":3,"pts":31},
    {"team":"hybd","mp":20,"won":6,"drwan":11,"loss":3,"pts":29}
]

#highest drawn
# no of teams
teamno=len(isldata)
print(teamno)
#team name
team_name=list(map(lambda data:data["team"],isldata))
print(team_name)
#highest point
h_points=max(list(map(lambda data:data["pts"],isldata)))
print(h_points)
#team having highest points
h_p_team=list(filter(lambda team:team["pts"]==h_points,isldata))
print(h_p_team)
h_p_t_name=list(map(lambda  team:team["team"],h_p_team))
print(h_p_t_name)
#30 to 40 range points team
range_team=list(filter(lambda data: (data["pts"]<=40) & (data["pts"]>30),isldata))
print(len(range_team))




