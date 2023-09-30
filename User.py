import json
import os

class User:
    def __init__(self, name, mention, id):
        self.name = name
        self.mention = mention
        self.id = id

    def push_to_JSON(self):
        info = {
            "name": self.name,
            "mention": self.mention,
            "id": self.id
        }

        with open("usersList.json", "a") as outfile:

            outfile.write("{")
            for key in info:
                outfile.write("\n\"{key}\": \"{value}\",".format(key = key, value = info[key]))
            outfile.write("}")

            # if os.stat("usersList.json").st_size == 0:
            #     json.dump(info, outfile)
            
            # else:
            #     #read line and delete bracket

            #     outfile.write(",{user_json}\n".format(user_json=json.dumps(info)))