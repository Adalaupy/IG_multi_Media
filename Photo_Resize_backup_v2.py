from PIL import Image,ImageOps
import os
from moviepy.editor import VideoFileClip,CompositeVideoClip,ImageClip
import random



def New_dimension(Media_item,Media_Type):
    
    x,y = Media_item.size

    filled_color = (255,255,255)

    dimens_type = "pro"    
    dimen_func = lambda x: 4/3 if x == "land" else 3/4    
    dimension = dimen_func(dimens_type)


    #"""
        
    if (x/y < dimension) :

        back_y = int(y)
        back_x = int((dimension) * y)

    else:

        back_x = x
        back_y = int(x/(dimension))

    print(back_x,back_y)


    if back_x % 2 !=0:
        back_x += 1
    
    if back_y % 2 !=0:
        back_y += 1

    Back_Img = Image.new('RGB', (back_x,back_y), filled_color)

    box = (int((back_x - x)/ 2), int((back_y - y)/2))

    print(box)




    if Media_Type == 'video':
        
        Back_Img.save('temp.jpg')
        Back_Img = ImageClip("temp.jpg")
        
        os.remove("temp.jpg")



    return Back_Img,box




def Media_Resize(Media_List):

    Modified_Media_List = []

    


    for i in range(len(Media_List)):
        
        Rand_FileName = format(random.randint(0,1000000), '07d')

        Media_item = Media_List[i]


        #Classify Media Type
        if Media_item.content_type.startswith('image') and not Media_item.content_type.endswith('gif'):

            Media_Type = 'image'
            Get_item = Image.open(Media_item)
            
            Get_item = ImageOps.exif_transpose(Get_item).convert('RGB')

            Get_item.save(f"temp2_{Rand_FileName}.jpg")
            Get_item = Image.open(f"temp2_{Rand_FileName}.jpg")

            Back_Img,box = New_dimension(Get_item,Media_Type)
            Back_Img.paste(Get_item,box)


            FileName = f'Updated_{Rand_FileName}.jpg'
            Back_Img.save(FileName)

            os.remove(f"temp2_{Rand_FileName}.jpg")


            


        else:

            Media_Type = 'video'
            Media_item.save("temp.mp4")
            
            Get_item = VideoFileClip("temp.mp4")

            Back_Img,box = New_dimension(Get_item,Media_Type)
            
            Back_Img = Back_Img.set_duration(Get_item.duration)


            
            Compo_clip = CompositeVideoClip([Back_Img,Get_item.set_position((box))])




            FileName = f'Updated_{Rand_FileName}.mp4'
            Compo_clip.write_videofile(FileName)



            Get_item.close()
            
            os.remove('temp.mp4')
            
            



        Modified_Media_List.append(FileName)


    return Modified_Media_List
            

