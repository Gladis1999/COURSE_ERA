import requests_with_caching
import json
def get_movies_from_tastedive(name):
    baseurl="https://tastedive.com/api/similar"
    p={}
    p["q"]=name
    p["type"]="movies"
    p["limit"]=5
    resp = requests_with_caching.get(baseurl,params=p)
    data = json.loads(resp.text)
    return data
def extract_movie_titles(d):
    new_list=[]
    ls=d['Similar']['Results']
    for i in ls:
           new_list.append(i['Name'])
    return new_list
def get_related_titles(lst):
    new_ls=[]
    for name in lst:
        d=get_movies_from_tastedive(name)
        related=extract_movie_titles(d)
        for i in related:
            if i not in new_ls:
                    new_ls.append(i)
    return new_ls
def get_movie_data(movie_name):
    baseurl="http://www.omdbapi.com/"
    p={}
    p["t"]=movie_name
    p["r"]='json'
    resp = requests_with_caching.get(baseurl,params=p)
    data = json.loads(resp.text)
    return data
def get_movie_rating(d):
    
    if len(d['Ratings'])>1:
        ls=d['Ratings'][1]["Source"]
        if ls=="Rotten Tomatoes":
                result=d['Ratings'][1]["Value"][:2]
                result=int(result)
    else:
            result=0
    return result
def find(item):
    return item[1]
def get_sorted_recommendations(lst):
    ratings=[]
    slist=[]
    dlist=get_related_titles(lst)
    for movie in dlist:
        data=get_movie_data(movie)
        ratings.append(get_movie_rating(data))
  
    l1=list(zip(dlist,ratings))
    l2=sorted(l1,key=find,reverse=True)
    for i in range(len(l2)-1):
        if l2[i][0] not in slist:
            if l2[i][1]==l2[i+1][1]:
                if l2[i][0]<l2[i+1][0]:
                    slist.append(l2[i+1][0])
                    slist.append(l2[i][0])
            else:
                slist.append(l2[i][0])
            
    return slist
                