title = input()
description = input()


def youtube_video(title, description, likes, dislikes, comments):
	youtube_video = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}} 
	return youtube_video
def likes(youtube_video):
	if ("likes" in youtube_video):
		youtube_video["likes"]+= 1
   else:
   	"likes" = 0
   return youtube_video

def dislikes(youtube_video):
	if ("dislikes" in youtube_video):
		youtube_video['dislikes'] += 1
	else:
		dislikes = 0
	 	return number_dislikes
   return youtube_video

def add_comment(youtube_video, username, comment):
	youtube_video["comments"][username] = comment 
	return youtube_video
	

def youtube_video(title, description, likes, dislikes, add_comments):
   youtube_video = {"title": title, "description": description, "likes": likes, "dislikes": dislikes, "add_comments": add_comments }
 