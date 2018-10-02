import requests
import sys
import json

stats={ 1:"experience",
        2:"experience",
        3:"magic",
        4:"magic",
        5:"shielding",
        6:"shielding",
        7:"distance",
        8:"distance",
        9:"sword",
        10:"sword",
        11:"club",
        12:"club",
        13:"axe",
        14:"axe",
        15:"fist",
        16:"fist",
        17:"fishing",
        18:"fishing",
        19:"achievements",
        20:"achievements",
        21:"loyalty",
        22:"loyalty"}

voclist=["all","no","druid","knight","paladin","sorcerer"]

def get_char(character):
    char_api="https://api.tibiadata.com/v2/characters/"
    char_api+=character
    char_api+=".json"
    raw=json.loads(requests.get(char_api).text)["characters"]["data"]
    return raw

def get_highscore(character, world, specific_stat, voc="all"):
    char_api="https://api.tibiadata.com/v2/highscores/"
    char_api+=world
    char_api+="/"
    char_api+=specific_stat
    if voc !="all":
        char_api+="/"
        char_api+=voc
    char_api+=".json"
    raw=json.loads(requests.get(char_api).text)["highscores"]
    rlist=[voc,raw]
    return rlist

def specific_char(character, json):
    west,east =json
    category=east["type"]
    for each in east["data"]:
        if each["name"] == character:
            print("Category",category)
            print("Sub-category",west)
            print("Rank",each["rank"])
            if "level" in each:
                print("Level",each["level"])
            if "points" in each:
                print("Points",each["points"])


def generate_page(character):
    basic=get_char(character)
    for key, items in basic.iteritems():
        print(key, items)
    searchvoc="all"
    for prof in voclist:
        if prof.lower() in basic["vocation"].lower():
            searchvoc=prof
    for key, value in sorted(stats.iteritems()):
        if key%2==0:
            specific_char(basic["name"], get_highscore(basic["name"], basic["world"], value, searchvoc))
        else:
            specific_char(basic["name"], get_highscore(basic["name"], basic["world"], value))



def section():
    print("_"*15)

if __name__ == "__main__":
    generate_page(sys.argv[1])
    


