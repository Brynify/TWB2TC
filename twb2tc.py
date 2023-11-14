import sys
import os
import shutil

# A Python dictionary mapping out TWBlue sounds to TC sounds.
sounds_list={
	"audio":"media",
	"create_timeline":"open_timeline",
	"delete_timeline":"close_timeline",
	"dm_received":"new_dm",
	"dm_sent":"send_dm",
	"error":"error",
	"favorite":"favorite",
	"favourites_timeline_updated":"favorites",
	"limit":"boundary",
	"max_length":"max",
	"mention_received":"new_mention",
	"new_event":"new_notification",
	"reply_send":"send_reply",
	"retweet_send":"send_boost",
	"search_updated":"search_updated",
	"tweet_received":"new_toot",
	"tweet_send":"send_toot",
	"tweet_timeline":"user",
	"update_followers":"follow",
}

#Ask the user for an input. Check for errors.
f=input("Enter the name of the folder you want to convert to a TC soundpack.")
name=f.replace("\\","/").split("/")[-1]
if f=="": sys.exit()
if not os.path.isdir(f):
	print("Error. This path does not exist.")
	sys.exit()

# Create our working directory.
if not os.path.isdir(name+"_tc"): os.makedirs(name+"_tc")
used_sounds=0

# Copy sounds from the TWBlue soundpack to the TC one using our soundmap for replacing the names.
for i in os.listdir(f):
# Separate extension from filename for use with the map and to be able to preserve original extension
	ext=i.split(".")[-1]
	soundname=i.replace("."+ext,"")
	if soundname in sounds_list:
		shutil.copy(f+"/"+i,name+"_tc/"+sounds_list[soundname]+"."+ext)
		used_sounds+=1

# Tell the user what we did
print(str(used_sounds)+" sounds used out of a total "+str(len(os.listdir(f)))+".")