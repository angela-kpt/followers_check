import json, os

def check_followers(data):
    following_list = []
    followers_list = []
    unfollowed_list = []

    if 'following.json' in data and 'followers_1.json' in data:
        # Opening JSON file
        with open('following.json', 'r') as openfile:
        
            # Reading from json file
            json_object = json.load(openfile)
        
        # print(json_object)
        # print(type(json_object))

        # print(json_object['relationships_following'])

        for i in range(len(json_object['relationships_following'])):
            following = json_object['relationships_following'][i]['string_list_data'][0]['value']
            following_list.append(following)


        with open('followers_1.json', 'r') as openfile2:
            json_object = json.load(openfile2)

            for i in range(len(json_object)):
                followers = json_object[i]['string_list_data'][0]['value']
                followers_list.append(followers)
                

        openfile.close
        openfile2.close

        print(following_list)
        print(followers_list)

        unfollowed_list = [i for i in following_list if i not in followers_list]


        print('Not Following You Back:\n')
        for i in unfollowed_list:
            print(i)

        return unfollowed_list
    
    else:
        print('Wrong files')
        exit

# data = ['following.json', 'followers_1.json']
# check_followers(data)
