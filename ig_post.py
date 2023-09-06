from instagrapi import Client
import os



def Login_ig(UserName,PW):

    global bot

    bot = Client()



    bot.login(UserName,PW)

    return bot




def Post_ig(Post_Detail,type):


    Media_List = Post_Detail[0]

    caption = Post_Detail[1]

    hashtag = ""
    
    if Post_Detail[2] !='':        
        

        for line in Post_Detail[2].splitlines():
            
            if line == "":
                
                hashtag += "\r\n"
            
            else:
                
                hashtag += f"\r\n#{line}"


                
                      
    
    Post_caption = caption  + '\n' + hashtag



    if len(Media_List) >1 :

        bot.album_upload(
            Media_List,
            caption = Post_caption
        )

    elif type == 1:

        bot.photo_upload(
            Media_List[0],
            caption = Post_caption
        )

    else:

        bot.video_upload(
            Media_List[0],
            caption = Post_caption
        )        


