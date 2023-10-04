import json
import os

class User:
    def __init__(self, name, mention, id):
        self.name = name
        self.mention = mention
        self.id = id
    
    # appends users data to the json file
    # needs to implement a check to prevent duplication
    def push_to_JSON(self):
        info = {
            "name": self.name,
            "mention": self.mention,
            "id": self.id
        }

        json_object = json.dumps(info, indent=4)
        
        #file_check = os.stat("users.json").st_size

        with open("users.json", "r+") as outfile:
            check = os.stat("users.json").st_size
            # outfile.seek(-2, os.SEEK_END)
            # outfile.truncate()

            if check == 0:
                outfile.write(json_object)
            else:
                loaded = json.load(outfile)
                loaded.update(info)
                #outfile.seek(0)
                outfile.write(',\n')
                json.dump(info, outfile, indent=4)

    # TODO append the users week picks to their unique registered ID     
    def append_week_pickems():
        return