from PIL import Image,ImageOps
import os
from moviepy.editor import VideoFileClip,CompositeVideoClip,ImageClip
from tempfile import TemporaryDirectory


# Convert each of file content to photo/Video

def Convert(Media_list):

    Convert_List = []
    
    for i in range(len(Media_list)):

        print(i)

        Media_item = Media_list[i]

        Media_Num = format(i,'07d')
        
        if Media_item.content_type.startswith('image') and not Media_item.content_type.endswith('gif'):

            Med_type = 1

            Get_item = Image.open(Media_item)
            Get_item = ImageOps.exif_transpose(Get_item).convert('RGB')

  
            Get_item.save(f"{Temp_Path}\\temp2_{Media_Num}.jpg")
            Get_item = Image.open(f"{Temp_Path}\\temp2_{Media_Num}.jpg")

            


        else:

            Med_type = 2
            
            Media_item.save(f'{Temp_Path}\\temp2_{Media_Num}.mp4')      
            Get_item = VideoFileClip(f'{Temp_Path}\\temp2_{Media_Num}.mp4') 

        
        output = (i,Med_type,Get_item)
        Convert_List.append(output)

    
    return Convert_List


# Get dimension of each media and decide portrait/landscape background image

def Orient(Convert_Media_List):
    
    land_cnt = 0
    port_cnt = 0

    for item in Convert_Media_List:
        
        Media = item[2]

        x,y = Media.size

        if x > y:
            
            land_cnt += 1

        else:

            port_cnt += 1

    
    if land_cnt > port_cnt:

        Ratio = 'land'
    
    else:

        Ratio = 'port'


    return Ratio


# Edit background photo size

def New_dimension(Media_item,Media_Type,dimens_type):



    x,y = Media_item.size

    filled_color = (255,255,255)

    dimen_func = lambda x: 4/3 if x == "land" else 3/4    
    dimension = dimen_func(dimens_type)

        
    if (x/y < dimension) :

        back_y = int(y)
        back_x = int((dimension) * y)

    else:

        back_x = x
        back_y = int(x/(dimension))




    if back_x % 2 !=0:
        back_x += 1
    
    if back_y % 2 !=0:
        back_y += 1

    Back_Img = Image.new('RGB', (back_x,back_y), filled_color)

    box = (int((back_x - x)/ 2), int((back_y - y)/2))


    if Media_Type == 2:
        

            
        Back_Img.save(f'{Temp_Path}\\temp.jpg')
        Back_Img = ImageClip(f"{Temp_Path}\\temp.jpg")
        

    return Back_Img,box



# compose media and background photo

def Media_Resize(Media_List):


    global Temp_File
    global Temp_Path


    Temp_File = TemporaryDirectory()
    Temp_Path = Temp_File.name

    

    Modified_Media_List = []

    Convert_Media_List = Convert(Media_List)
    dimens_type = Orient(Convert_Media_List)


    for i in range(len(Convert_Media_List)):

        Media_Num = format(Convert_Media_List[i][0],'07d')
        Media_Type = Convert_Media_List[i][1]
        Get_item = Convert_Media_List[i][2]



        Back_Img,box = New_dimension(Get_item,Media_Type,dimens_type)


        if Media_Type == 1:

            
            FileName = f'Updated_{Media_Num}.jpg'
            
            Back_Img.paste(Get_item,box)
            Back_Img.save(FileName)



        else:
            

            FileName = f'Updated_{Media_Num}.mp4'

            Back_Img = Back_Img.set_duration(Get_item.duration)
            Compo_clip = CompositeVideoClip([Back_Img,Get_item.set_position((box))])
            Compo_clip.write_videofile(FileName)

            
            Get_item.close()



        

        Modified_Media_List.append(FileName)        




    if len(Convert_Media_List) > 1:
        
        Media_Type = 2

    return Modified_Media_List,Media_Type




