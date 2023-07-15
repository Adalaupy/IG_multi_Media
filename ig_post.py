from instagrapi import Client
import os



def Login_ig(UserName,PW):

    global bot

    bot = Client()

    if UserName == "":
        UserName = "iamutuber"
        PW = "s00401240843130!"

    bot.login(UserName,PW)

    return bot




def Post_ig(Post_Detail):


    Media_List = Post_Detail[0]

    caption = Post_Detail[1]
    
    if Post_Detail[2] !='':        
        
        Post_Detail[2]

        hashtag = ""

        for line in Post_Detail[2].splitlines():
            
            if line == "":
                
                hashtag += "\r\n"
            
            else:
                
                hashtag += f"\r\n#{line}"
                      
    
    Post_caption = caption  + '\n' + hashtag




    bot.album_upload(
        Media_List,
        caption = Post_caption
    )


    


