from flask import Flask, render_template, request,url_for
from Photo_Resize import *
from ig_post import *




app = Flask(__name__)



#=====================================================================================================

# Go to the login page
@app.route('/')

def index():

    return render_template('Login.html')

#=====================================================================================================


# Login in to Next page
@app.route('/index', methods=['POST'])

def Login():
    
    global bot

    # Get Login information from form
    username = request.form['username']
    password = request.form['password']

    
    # Call login function from ig_post.py
    bot = Login_ig(username,password)


    return render_template('index.html')


#=====================================================================================================

# Go back to post Again within same account if need
@app.route('/upload_again', methods=['POST'])

def back_to_index():

    

    return render_template('index.html')


def delete(Media_List):
     
    for item in Media_List:
        os.remove(item)
        print(item)

        try:                         
                os.remove(item + ".jpg")
        
        except:
            
            pass


#=====================================================================================================

# Submit to Post
@app.route('/submit_form', methods=['POST'])

def submit_form():
    

    # Get IG Post 
    caption = request.form['caption']
    hashtag = request.form['hashtag']
    uploaded_pic = request.files.getlist('pictures')



    # resize photo
    Media_List,media_type = Media_Resize(uploaded_pic)
    
    # ig release post
    Post_Detail = [Media_List,caption,hashtag]
    
    Post_ig(Post_Detail,media_type)

    

    delete(Media_List)


    return """


    <style>

        input[type="submit"] {
            align-self: center;
            background-color: #5d68fc;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 17px;
            width: 230px;
            height: 35px;
            margin-left: 30px;
        }        
        
		label {
			font-size: 35px;
			margin-bottom: 20px;
            margin-left: 30px;
		}


        input[type="submit"]:hover {
            background-color: #b4ee6;
            margin-left: 30px;
        }



    </style> 





    <form id = "form1" method="post" action="http://localhost:5000/upload_again" enctype="multipart/form-data">

		
        <label>Form submitted successfully</label> <br><br><br><br>        
        
        <input type="submit" value="Go back for another post">
	
	</form>   

    """



#=====================================================================================================



if __name__ == '__main__':
    
    app.run(debug=True)