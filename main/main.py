import dash_core_components as dcc
import dash_dangerously_set_inner_html
import dash
from dash.dependencies import Input, Output,State
import dash_bootstrap_components as dbc
import dash_html_components as html
import grasia_dash_components as gdc
import datafr
import pyttsx3
import dash_table_experiments as dt
import base64
import webbrowser as wb
import datetime
import matplotlib.pyplot as plt
import plotly.plotly as py
import dash_daq as daq
from PIL import Image
from base64 import decodestring
import numpy as np
import cv2  # only used for loading the image, you can use anything that returns the image as a np.ndarray
import os,sys
import datetime
import imageio
from io import BytesIO
import pythoncom
from grad_cam  import build_model,build_guided_model,compute_saliency
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from win10toast import ToastNotifier
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
import sys
sys.path.insert(0, '/one')
from one.one import build,path_img,plot_activations
from one import data123
#from google.cloud import storage
#from firebase import firebase
import urllib


#For firebase no need
'''
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'visker-c7e9b-firebase-adminsdk-1uux2-7438cacf30.json'
firebase=firebase.FirebaseApplication('https://visker-c7e9b.appspot.com/')
client=storage.Client()
bucket=client.get_bucket('visker-c7e9b.appspot.com')
blobs=bucket.list_blobs()
#storage = firebase.storage()
#storage.child("images/example.jpg").download("img")
'''





external_scripts = [
    'https://www.google-analytics.com/analytics.js',
    "https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js",
    {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
        'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
        'crossorigin': 'anonymous'
    }
]

# external CSS stylesheets
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    },

    {
        'href': 'https://fonts.googleapis.com/css?family=Varela',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }

    
]


app = dash.Dash(__name__,meta_tags=[
    {
        'name': 'description',
        'content': 'My description'
    },
    {
        'http-equiv': 'X-UA-Compatible',
        'content': 'IE=edge'
    }
],
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets,
                static_folder='assets')

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True
app.title = 'Visker'
app.config['suppress_callback_exceptions']=True



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

PLOTLY_LOGO = "/"

index_page = html.Div([

    dcc.Interval(id="interval", interval=250, n_intervals=0),
    dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="assets/keras-logo-small-wb-1.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Visker", className="ml-4")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/",
            ),
            
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.NavItem(dbc.NavLink("Page1", href="/page-1")),
            dbc.NavItem(dbc.NavLink("Page2", href="/page-2")),
          
        ],
        color="dark",      
        dark=True,
        sticky="top",
    ),

   
    html.Div(id='cardinv'),
    html.Div([
    html.Div(
            [
                dbc.Button("About Visker 	\ud83d\udc4b", id="collapse-button", className="mr-1",color="warning",outline=True,style={"margin-bottom":"10px","margin-top":"20px",'border':"#FFC107 2px solid "}),
                dbc.Collapse(

                   
                 
                    
                    dbc.Card(dbc.CardBody(          html.Div([dash_dangerously_set_inner_html.DangerouslySetInnerHTML(
                        '''





                <!-- some content to allow scrolling :)-->
<div class="page-hero d-flex align-items-center justify-content-center">
<img src="assets/robo1.gif" style="margin-left: auto; margin-right: auto" height="160px">
</div>
<div class="main-content">
  <section>
    <div class="container">
    <h2>Project Scope and Vision</h2>
                      <p>One of the most debated topics in deep learning is how to interpret and understand a trained model – particularly in the context of high-risk industries like healthcare. The term “black box” has often been associated with deep learning algorithms. How can we trust the results of a model if we can’t explain how it works? It’s a legitimate question.
Take the example of a deep learning model trained for detecting cancerous tumors. The model tells you that it is 99% sure that it has detected cancer – but it does not tell you why or how it made that decision.
Did it find an important clue in the MRI scan? Or was it just a smudge on the scan that was incorrectly detected as a tumor? This is a matter of life and death for the patient and doctors cannot afford to be wrong.
As we have seen in the cancerous tumor example, it is crucial that we know what our model is doing – and how it’s making decisions on its predictions. Typically, the reasons listed below are the most important points for a deep learning practitioner to remember:

1     Understanding how the model works
2.	Assistance in Hyperparameter tuning
3.	Finding out the failures of the model and getting an intuition of why they fail
4.	Explaining the decisions to a consumer / end-user or a business executive

Neural nets are black boxes. In the recent years, several approaches for understanding and visualizing Convolutional Networks have been developed in the literature. They give us a way to peer into the black boxes, diagnose mis-classifications, and assess whether the network is over/under fitting.
Guided backpropagation can also be used to create trippy art, neural/texture style transfer among the list of other growing applications. The purpose of the project is to design a Visualization Tool for Keras to visualize and debug what CNN’s are learning and to show heatmaps for a large variety of models. We also intend to develop an algorithm of our own. We plan to deliver the basic version of the toolkit in our sprint 1 evaluation and further we are planning to add all combinations possible for activation function and different models, etc. The final delivery of the product will be in April 2019.
</p>    
    </div>
  </section>
  <section>
    <div class="container">
      <h2>Your journey starts here.</h2>
      <p> This is it. You've made it so far. There is no going back.</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dicta iste molestias vel commodi, quae quaerat ex numquam. Consectetur corporis explicabo, qui labore, repellat dignissimos illo molestias maxime nisi a consequuntur?</p>
      <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Impedit fuga autem dolore, ex nobis, iste quasi, asperiores esse repellendus tempore, obcaecati numquam minima maxime! Laboriosam, ut ipsam magnam corporis aut.</p>
      <h3>Get lost and find yourself.</h3>
      <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sequi placeat dolor molestias facere veritatis culpa amet fugiat debitis dolorem qui quidem consequuntur mollitia, nesciunt pariatur voluptatum! Dolor accusamus labore, sequi.</p>
    </div>
  </section>
  <section>
    <div class="container">
      <h2>Your journey starts here.</h2>
      <p> This is it. You've made it so far. There is no going back.</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dicta iste molestias vel commodi, quae quaerat ex numquam. Consectetur corporis explicabo, qui labore, repellat dignissimos illo molestias maxime nisi a consequuntur?</p>
      <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Impedit fuga autem dolore, ex nobis, iste quasi, asperiores esse repellendus tempore, obcaecati numquam minima maxime! Laboriosam, ut ipsam magnam corporis aut.</p>
      <h3>Get lost and find yourself.</h3>
      <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sequi placeat dolor molestias facere veritatis culpa amet fugiat debitis dolorem qui quidem consequuntur mollitia, nesciunt pariatur voluptatum! Dolor accusamus labore, sequi.</p>
    </div>
  </section>
  <section>
    <div class="container">
      <h2>Your journey starts here.</h2>
      <p> This is it. You've made it so far. There is no going back.</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dicta iste molestias vel commodi, quae quaerat ex numquam. Consectetur corporis explicabo, qui labore, repellat dignissimos illo molestias maxime nisi a consequuntur?</p>
      <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Impedit fuga autem dolore, ex nobis, iste quasi, asperiores esse repellendus tempore, obcaecati numquam minima maxime! Laboriosam, ut ipsam magnam corporis aut.</p>
      <h3>Get lost and find yourself.</h3>
      <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sequi placeat dolor molestias facere veritatis culpa amet fugiat debitis dolorem qui quidem consequuntur mollitia, nesciunt pariatur voluptatum! Dolor accusamus labore, sequi.</p>
    </div>
  </section>
  <section>
    <div class="container">
      <h2>Your journey starts here.</h2>
      <p> This is it. You've made it so far. There is no going back.</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dicta iste molestias vel commodi, quae quaerat ex numquam. Consectetur corporis explicabo, qui labore, repellat dignissimos illo molestias maxime nisi a consequuntur?</p>
      <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Impedit fuga autem dolore, ex nobis, iste quasi, asperiores esse repellendus tempore, obcaecati numquam minima maxime! Laboriosam, ut ipsam magnam corporis aut.</p>
      <h3>Get lost and find yourself.</h3>
      <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sequi placeat dolor molestias facere veritatis culpa amet fugiat debitis dolorem qui quidem consequuntur mollitia, nesciunt pariatur voluptatum! Dolor accusamus labore, sequi.</p>
    </div>
  </section>
  <section>
    <div class="container">
      <h2>Your journey starts here.</h2>
      <p> This is it. You've made it so far. There is no going back.</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dicta iste molestias vel commodi, quae quaerat ex numquam. Consectetur corporis explicabo, qui labore, repellat dignissimos illo molestias maxime nisi a consequuntur?</p>
      <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Impedit fuga autem dolore, ex nobis, iste quasi, asperiores esse repellendus tempore, obcaecati numquam minima maxime! Laboriosam, ut ipsam magnam corporis aut.</p>
      <h3>Get lost and find yourself.</h3>
      <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sequi placeat dolor molestias facere veritatis culpa amet fugiat debitis dolorem qui quidem consequuntur mollitia, nesciunt pariatur voluptatum! Dolor accusamus labore, sequi.</p>
    </div>
  </section>
  <section>
    <div class="container">
      <h2>Your journey starts here.</h2>
      <p> This is it. You've made it so far. There is no going back.</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dicta iste molestias vel commodi, quae quaerat ex numquam. Consectetur corporis explicabo, qui labore, repellat dignissimos illo molestias maxime nisi a consequuntur?</p>
      <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Impedit fuga autem dolore, ex nobis, iste quasi, asperiores esse repellendus tempore, obcaecati numquam minima maxime! Laboriosam, ut ipsam magnam corporis aut.</p>
      <h3>Get lost and find yourself.</h3>
      <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sequi placeat dolor molestias facere veritatis culpa amet fugiat debitis dolorem qui quidem consequuntur mollitia, nesciunt pariatur voluptatum! Dolor accusamus labore, sequi.</p>
    </div>
  </section>
  <section>
    <div class="container">
      <h2>Your journey starts here.</h2>
      <p> This is it. You've made it so far. There is no going back.</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dicta iste molestias vel commodi, quae quaerat ex numquam. Consectetur corporis explicabo, qui labore, repellat dignissimos illo molestias maxime nisi a consequuntur?</p>
      <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Impedit fuga autem dolore, ex nobis, iste quasi, asperiores esse repellendus tempore, obcaecati numquam minima maxime! Laboriosam, ut ipsam magnam corporis aut.</p>
      <h3>Get lost and find yourself.</h3>
      <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sequi placeat dolor molestias facere veritatis culpa amet fugiat debitis dolorem qui quidem consequuntur mollitia, nesciunt pariatur voluptatum! Dolor accusamus labore, sequi.</p>
    </div>
  </section>
  <section>
    <div class="container">
      <h2>Your journey starts here.</h2>
      <p> This is it. You've made it so far. There is no going back.</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dicta iste molestias vel commodi, quae quaerat ex numquam. Consectetur corporis explicabo, qui labore, repellat dignissimos illo molestias maxime nisi a consequuntur?</p>
      <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Impedit fuga autem dolore, ex nobis, iste quasi, asperiores esse repellendus tempore, obcaecati numquam minima maxime! Laboriosam, ut ipsam magnam corporis aut.</p>
      <h3>Get lost and find yourself.</h3>
      <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sequi placeat dolor molestias facere veritatis culpa amet fugiat debitis dolorem qui quidem consequuntur mollitia, nesciunt pariatur voluptatum! Dolor accusamus labore, sequi.</p>
    </div>
  </section>
</div>

                        '''



                        )]))),
                    id="collapse",
          


                    
                ),
            ]
        ),
    ],className="ten columns offset-by-one"),

    html.Div([
        
    dbc.Card([dbc.CardBody([
    html.Div([
    
     html.Div(
         [dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''

<div id="wave" style="width":"45%"><div id="separatediv"><h5>	&#x1F3AE; An Interactive Tool &#x1F389;</h5></div></div>

    '''
    )],style={"margin-top":"-16px","margin-left":"-6px"}),

        
                dbc.Row(
          [
              dbc.Col(
                  html.Div(id='card-1',children=[
],className='seven columns offset-by-four'),

       ),

              dbc.Col(
    html.Div([
        
        html.Img(src="assets/bob.png",style={"height":"210px"}),
        daq.PowerButton(
        id='startbtn',
        on=False,
        size=48,
        color="#FFD300",
        label="Help 	\ud83d\udc4d"
    ),
         html.Div(id="startbtnoutput",children=[]),
                    
              ]),
    ),


    ],  no_gutters=True),

        ],style={'margin-bottom':'10px','margin-top':'10px'}),
 ]
                    )
                ],

                outline=True,
                color="#ffaa00",
                style={"border": "#ffaa00 1px solid"}
            ),

],className="r columns offset-by-r",style={"margin-bottom":"40px","margin-top":"20px"}),


    html.Div([
    
     dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
     ],className="ten columns offset-by-one"),



    html.Div([

    dash_dangerously_set_inner_html.DangerouslySetInnerHTML(
        '''
       <div class="footer">
  <div id="button"></div>
<div id="container">
<div id="cont">
<div class="footer_center">







        
	   <h3 style="color:white;">Made With <img height=45px src="assets/heart.gif"></h3>

                  <div class="container">
      <div class="row">
        <div class="col-sm">
          
          <img style="border:#FFC107 5px solid;" src = "assets/download.png" height=60px class = "rounded-circle" border-radius="500px" border-color="#FFC107">
   
          <p style="color:white;">Arjun Mohnot</p>
      </div>
        <div class="col-sm">
           <img style="border:#FFC107 5px solid;" src = "assets/akshita.png" height=60px class = "rounded-circle" border-radius="500px" border-color="#FFC107">
   
          <p style="color:white;">Akshita Mehta</p>
      </div>
        <div class="col-sm">
          <img style="border:#FFC107 5px solid;" src = "assets/siddhanth.png" height=60px class = "rounded-circle" border-radius="500px" border-color="#FFC107">
   
          <p style="color:white;">Siddhanth Iyer</p>
      </div>
              </div>
            </div>

     <div class="container">
      <div class="row">
        <div class="col-sm">
            <img style="border:#FFC107 5px solid;" src = "assets/Monisha.png" height=60px class = "rounded-circle" border-radius="500px" border-color="#FFC107">
   
          <p style="color:white;">G Monisha</p>
        
        </div>


           <div class="col-sm">
            <img style="border:#FFC107 5px solid;" src = "assets/ayushi.png" height=60px class = "rounded-circle" border-radius="500px" border-color="#FFC107">
   
          <p style="color:white;">Ayushi Agarwal</p>
        
        </div>
        
          </div>
            </div>

        

</div>
</div>
</div>
</div>
        '''


),




        ]),
 
   
])









'''    

    print()
    import speech_recognition
     
    speech_engine = pyttsx3.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
    speech_engine.setProperty('rate', 150)
     
    def speak(text):
        speech_engine.say(text)
        speech_engine.runAndWait()
     
    recognizer = speech_recognition.Recognizer()
     
    def listen():
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
     
        try:
            return recognizer.recognize_sphinx(audio)
            # or: return recognizer.recognize_google(audio)
        except speech_recognition.UnknownValueError:
            print("Could not understand audio")
        except speech_recognition.RequestError as e:
            print("Recog Error; {0}".format(e))
     
        return ""
     
    speak("Say something!")
    speak("I heard you say " + listen())


'''



@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(dash.dependencies.Output('cardinv', 'children'),
              [Input('startbtn','on')])
def page_1_dropdown(on):
    try:
        pythoncom.CoInitialize()
        engine = pyttsx3.init()
       
        if on==False:
            engine.stop()
        elif on==True:
             
            if datafr.countvol==0:
                
                
                datafr.countvol=1
                engine.say("Hello")
                engine.setProperty('rate',90)
                engine.setProperty('volume', 0.9)
                engine.runAndWait()
                engine.say("I am Visker")
                engine.setProperty('rate',120)
                engine.setProperty('volume', 1.0)
                engine.runAndWait()
                engine.say("What you want to do")
                engine.setProperty('rate',170)
                engine.setProperty('volume', 0.9)
                engine.runAndWait()
                engine.say("Visualize Image")
                engine.setProperty('rate',170)
                engine.setProperty('volume', 0.9)
                engine.runAndWait()
                engine.say("See Intermediate Layers")
                engine.setProperty('rate',170)
                engine.setProperty('volume', 0.9)
                engine.runAndWait()
                datafr.countvol=0
            return []  
        return []

    except Exception as e:
        print(e)
        return []
@app.callback(dash.dependencies.Output('card-1', 'children'),
              [Input("interval", "n_intervals"),Input('startbtn','on')])
def page_1_dropdown(value,on):
    children=[]
    
            
    
    if on==True:
        
        
    
        if datafr.tempflag==0:
            if(datafr.steps==0):
                
                      
                        
                finals="Hello"
                finals1="I am Visker..."

                

                
                if datafr.temps!=finals:
                    datafr.temps+=finals[datafr.varcount]
                    datafr.varcount+=1
                else:
                    datafr.varcount=0
                    if datafr.temps1!=finals1:
                        datafr.temps1+=finals1[datafr.varcount1]
                        datafr.varcount1+=1
                    else:
                        datafr.varcont1=0
                        datafr.steps+=1

                children=[dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                dbc.CardTitle(datafr.temps),
                                dbc.CardText(datafr.temps1),
                            ]
                        )
                    ],
                    outline=True,
                    color="#ffaa00",
                    style={"border": "#ffaa00 1px solid"}
                    
                )]
                return children
            if(datafr.steps==1):
                
                children=[dbc.Card(
                [
                    dbc.CardBody(
                        [
                            dbc.CardTitle("What you want to do ? "),
                            dbc.CardText("Visualize Image ?"),
                            dcc.Link('Go to Page 1', href='/page-1'),
                            dbc.CardText("See Intermediate Layers ?"),
                            dcc.Link('Go to Page 2', href='/page-2'),  
                        ]
                    )
                ],
                outline=True,
                color="#ffaa00",
                style={"border": "#ffaa00 1px solid"}
            )]

    
            return children

                    
                        

                
            


    elif on==False:
        datafr.steps=0
        datafr.varcount=0
        datafr.temps=''
        datafr.varcount1=0
        datafr.temps1=''
        datafr.names=''
        datafr.tempflag=0
        children=[dbc.Card(
            [
                dbc.CardHeader("Visker \u2b50"),
                dbc.CardBody(
                    [
                        dbc.CardTitle("Visualization Tool For Keras"),
                        dbc.CardText("Need some help ? press Help !"),
                    ]
                ),
            ] ,color="dark",
            inverse=True,
        ),]
        return children
          
    return children
        




app.config['suppress_callback_exceptions']=True







page_1_layout = html.Div([

        dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="assets/keras-logo-small-wb-1.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Visker", className="ml-4")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/",
            ),
            
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.NavItem(dbc.NavLink("Page1", href="/page-1")),
            dbc.NavItem(dbc.NavLink("Page2", href="/page-2")),
          
        ],
        color="dark",      
        dark=True,
        sticky="top",
    ),


    
     html.Div([    
     html.Div([


         


         html.Div([dcc.Interval(
                    id='interval-component',
                    interval=1*1000, # in milliseconds
                    n_intervals=0
                )]),




     html.Div(
        [
            dbc.Button("Instructions 	\ud83d\udcd4", id="collapse-button1", className="mr-1",color="warning",outline=True,style={"margin-bottom":"10px","margin-top":"20px",'border':"#FFC107 2px solid "}),
            dbc.Collapse(
                            html.Div([html.P("Dash: A web application framework made with Python \ud83d\udc8e "),
                                html.H5("	\ud83d\udd38 Coming Soon! 	\ud83c\udfae ")]),
                            id='collapse1',
                            



                )],style={"margin-top":"10px","margin-bottom":"10px"}),


       dbc.Card(
            [
                dbc.CardHeader("Visker \u2b50"),
                dbc.CardBody(
                    [
                         html.Div([
                              html.Div([
                              html.Div([html.H6("	\u231a Time: ")],className='one columns'),      
                              html.Div(children=[
                                                daq.LEDDisplay(
                                                    id='my-LED-display',
                                                    color="#FF5E5E",
                                                    size=14,
                                                    value=str(datetime.datetime.now().strftime('%H:%M:%S'))
                                                ),],style={'margin-bottom':'0.6%'},className='five columns'),


                              ],className='row')],className="twelve columns offset-by-lil"),


                            

                              html.H5('Enter Your Email \ud83d\udce7'),
                              html.Div([

                                    dcc.Input(
                                    id="email",
                                    placeholder='Enter Your Email ✉',
                                    type='email',
                                    value=''
                                ),
                                                    




                                  ],className="twelve columns",style={'margin-bottom':'10px'}),


                        

                            html.H5('Choose Model 		\ud83d\udcbb'),
                            html.Div([
                            html.Div([dcc.Dropdown(id='dropdown-1',
                                                        
                            options=[{'label': 'Vgg16', 'value': 0},
                            {'label': 'ResNet50', 'value': 1},
                                     {'label': 'Nasnet', 'value': 2},
                                     {'label': 'Mobilenet', 'value': 3}
                             ],
                            value=0,
                            ),],className='three columns',style={'margin-bottom':'10px'}),
                            ],className="twelve columns",style={'margin-bottom':'10px'}),

        

                                                                

                                      html.H5('No. of Prediction \ud83d\udc68\u200d\ud83d\udcbb'),

                                     html.Div([
                                      html.Div([
                                      daq.Knob(
                                      id="knob",
                                      size=70,
                                      value=5,
                                      color="#ffaa00",
                                      max=10,
                                      min=1,
                                    ),

                                      ],className="three columns"),
                                       ],className="twelve columns",style={'margin-bottom':'10px'}),



                               

                  
                     
                     
                      html.Hr(style={"visibility":"hidden"}),    
                      html.Div(
                            [


                            html.Div(id='upload-check'),
                            
                            
                           ],style={"margin-top":"30px"}),

                 

                        
                    ]
                ),
            ]
        ),   


         
         

         html.Div(id='output-image',style={"margin-top":"10px","margin-":"10px"}),

         html.Div(id='graph',style={"margin-top":"10px","margin-":"10px"}),







         dbc.Card(
            [
                dbc.CardHeader("Select other probability/model to compare with the original prediction \ud83d\udc41\ufe0f "),
                dbc.CardBody(
                    [
                        
                     html.Div([
                   
                             
                     html.Div([dcc.Dropdown(id='dropdown',
                            options=[],
                        ),],style={"margin-top":"10px","margin-":"10px"},className='five columns'),

                     ]),
                      
                    ]
                ),
            ]
        ),

      

          html.Div(id='output-image-3',style={"margin-top":"10px","margin-":"10px"}),
        
         html.Div(id='graph1',style={"margin-top":"10px","margin-":"10px"}),
         
       
          html.Div(id='output-image-1',style={"margin-top":"10px","margin-":"10px"}),
     

         
                 
                


    ],className='ten columns offset-by-one'),
     ]),

])

@app.callback(
        dash.dependencies.Output('graph', 'children'),
        [dash.dependencies.Input('interval-component', 'n_intervals')]
    )
def update_output(value):
        if len(datafr.d)!=0:
            x=[]
            y=[]
            title="Probability For "+str(datafr.label1)+" Model"
            for i in datafr.d:
                y.append(i)
                x.append(datafr.d[i][1])
            fig=[ dcc.Graph(
        id='example-graph-1',
        figure={
            'data': [
                {'x': y, 'y': x, 'type': 'bar', 'name': 'Probability'},
            ],
            'layout': {
                'title': title
            }
        }
    )]
            return [

                  html.Div([
         dbc.Card(
            [
                dbc.CardHeader("Visker \u2b50"),
                dbc.CardBody(
                    [
                        html.Div(fig),
                    ]
                ),
            ]
        ),],style={"margin-top":"10px","margin-":"10px"}),

         



                ]
        else:
            return []


@app.callback(
        dash.dependencies.Output('graph1', 'children'),
        [dash.dependencies.Input('interval-component', 'n_intervals')]
    )
def update_output(value):
        if len(datafr.d1)!=0 and datafr.flags1!=0:
            x=[]
            y=[]
            title="Probability For "+str(datafr.label2)+" Model"
            for i in datafr.d1:
                y.append(i)
                x.append(datafr.d1[i][1])
            fig=[ dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': y, 'y': x, 'type': 'bar', 'name': 'Probability'},
            ],
            'layout': {
                'title': title
            }
        }
    )]
            return [

                  html.Div([
         dbc.Card(
            [
                dbc.CardHeader("Visker \u2b50"),
                dbc.CardBody(
                    [
                        html.Div(fig),
                    ]
                ),
            ]
        ),],style={"margin-top":"10px","margin-":"10px"}),

         



                ]
        else:
            return []






@app.callback(
dash.dependencies.Output('dropdown', 'options'),
[Input('interval-component', 'n_intervals')])
def set_cities_options(value):
    if (len(datafr.d)!=0) and (datafr.check1==1) and (datafr.check==1):
        return [{'label': k, 'value': k} for k in datafr.d.keys()]
    else:
        return []





@app.callback(
dash.dependencies.Output('upload-check', 'children'),
[Input('interval-component', 'n_intervals')])
def set_cities_options(value):
    if datafr.check1==1 and datafr.check==1:
        return [
            html.Div([
            html.H5('Choose Image 	\ud83d\uddc3\ufe0f'),
            dcc.Upload(
                    id='upload-data',
                    children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
            ,' 	\ud83d\udcc1'
                    ]),
                    style={
                        'width': '100%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin-bottom':'100%',
                        'margin': '1%'
                    },
                    # Allow multiple files to be uploaded
                   accept='image/*'
                )],className="ten columns offset-by-one")]
    elif datafr.check1==0:
        psps="..."
        if(value%6==0):
            psps='...'
        elif(value%2==0):
            psps='..'
        elif(value%3==0):
            psps='.'


        return [html.Div([html.Div([
                            html.Div([html.Div([html.P(str(datafr.loader)+"%",style={'top':'-2px','heigth':'25px','width':'25%','position': 'relative','left': '53%','transform':'translateX(-50%)'})
                            ],style={'background-color': 'orange','width':str(datafr.loader)+"%",'height': '20px','border-radius':'10px'})
                                                ],style={'background-color':'black','padding':'3px','border-radius': '13px'}),html.P("",style={"margin-bottom":"10px"}),html.P("\ud83d\udcdc Getting Analysed"+psps,style={"margin-bottom":"10px","margin-top":"30px"}),html.P(""),
                                      html.Hr(style={'margin-top':'2%','margin-bottom':'6%'})]),],className="ten columns offset-by-one",style={"margin-top":"10px"})]

    else:
        psps="..."
        if(value%6==0):
            psps='...'
        elif(value%2==0):
            psps='..'
        elif(value%3==0):
            psps='.'

        
        return [html.Div([html.Div([
                            html.Div([html.Div([html.P(str(datafr.loader)+"%",style={'top':'-2px','heigth':'25px','width':'25%','position': 'relative','left': '53%','transform':'translateX(-50%)'})
                            ],style={'background-color': 'orange','width':str(datafr.loader)+"%",'height': '20px','border-radius':'10px'})
                                                ],style={'background-color':'black','padding':'3px','border-radius': '13px'}),html.P("",style={"margin-bottom":"10px"}),html.P("\ud83d\udcdc Getting Analysed"+psps,style={"margin-bottom":"10px","margin-top":"30px"}),html.P(""),
                                      html.Hr(style={'margin-top':'2%','margin-bottom':'6%'})]),],className="ten columns offset-by-one",style={"margin-top":"10px"})]






        
@app.callback(
    Output("collapse1", "is_open"),
    [Input("collapse-button1", "n_clicks")],
    [State("collapse1", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


   



@app.callback(
        dash.dependencies.Output('my-LED-display', 'value'),
        [dash.dependencies.Input('interval-component', 'n_intervals')]
    )
def update_output(value):
        return str(datetime.datetime.now().strftime('%H:%M:%S'))






@app.callback(Output('output-image', 'children'),
              [Input('upload-data','contents')],
              [State('upload-data', 'filename'),State('dropdown-1', 'value'),State('knob','value'),State('email','value'),State('dropdown-1', 'options')])
def update_graph_interactive_image(content,new_filename,number,knob,email,label):
    #print(content,new_filename,number,knob,email,datafr.check1)
    if (content is not None) and (datafr.check1==1):
        for i in label:
            if i['value']==number:
                datafr.label1=i['label']
        
        datafr.predict=knob
        datafr.loader=0
        datafr.check1=0
        datafr.d=dict()
        datafr.flag=1
        string = content.split(';base64,')[-1]
        imgdata = base64.b64decode(string)
        filename = 'some_image.png'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)

        #image = Image.fromstring('RGB',(200,200),decodestring(string))
        basewidth = 224
        img = Image.open('some_image.png')
        img=img.convert('RGB')
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        datafr.H=224
        img = img.resize((224, 224),resample=0)
        datafr.W=224
        img.save('some_image.png')
        #######maybee this is te
        #print("Image----------------------")
        #buff = BytesIO()
        #img.save(buff, format="PNG")
        #img.save('some_image.png')
        #cat = cv2.imread("some_image.png")
        #model = Sequential()
        #model.add(Convolution2D(3,    # number of filter layers
                            #3,    # y dimension of kernel (we're going for a 3x3 kernel)
                            #3,    # x dimension of kernel
                            #input_shape=cat.shape,dim_ordering="tf"))
        
        #image_array=visualize_cat(model, cat)
        #image1 = Image.fromarray(image_array.astype('uint8'))
        #buff = BytesIO()
        #image1.save(buff, format="PNG")
        #new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
        #return [html.Img(src='data:image/png;base64,{}'.format(new_image_string)),]
        
        #print(cat)

        #print('dididid')
        #print(buff.getvalue())
        #print('lolololo')
        #b=[os.remove(file) for file in os.listdir('assets') if file.endswith('.jpg')]
        '''
        try:
            os.remove('assets/gradcam.jpg')
            os.remove('assets/guided_backprop.jpg')
            os.remove('assets/guided_gradcam.jpg')
        except:
            pass
        '''
        number=number
        model = build_model(number)
        guided_model = build_guided_model(number)
        layer_name=''
        if number==1:
            layer_name='res5c_branch2c'
        elif number==0:
            layer_name='block5_conv3'
        elif number==2:
            layer_name='normal_add_2_12'
        elif number==3:
            layer_name='conv_dw_13'
            
        gradcam, gb, guided_gradcam = compute_saliency(model, guided_model,layer_name=layer_name,img_path=img, cls=-1, visualize=False, save=True,string=number)
        img1=''
        with open("assets/gradcam.jpg", "rb") as imageFile:
            img1=base64.b64encode(imageFile.read()).decode("utf-8")
        img2=''
        with open("assets/guided_backprop.jpg", "rb") as imageFile:
            img2=base64.b64encode(imageFile.read()).decode("utf-8")
        img3=''
        with open("assets/guided_gradcam.jpg", "rb") as imageFile:
            img3=base64.b64encode(imageFile.read()).decode("utf-8")
        
        #print(datafr.d[0][1])
        ac=str(list(datafr.d)[0])
        datafr.new_filename=new_filename
        try:
            img_data = open('some_image.png', 'rb').read()
            msg = MIMEMultipart()
            msg['Subject'] = 'Keras Visualtion Tool Report'
            tempstring="The probability predicted by the "+datafr.label1+" model are"+str(datafr.d)
            text = MIMEText(tempstring)
            msg.attach(text)
            image_data = MIMEImage(img_data, name=os.path.basename('some_image.png'))
            msg.attach(image_data)
            img_data = open('assets/gradcam.jpg', 'rb').read()
            image_data = MIMEImage(img_data, name=os.path.basename('assets/gradcam.jpg'))
            msg.attach(image_data)
            img_data = open('assets/guided_backprop.jpg', 'rb').read()
            image_data = MIMEImage(img_data, name=os.path.basename('assets/guided_backprop.jpg'))
            msg.attach(image_data)
            img_data = open('assets/guided_gradcam.jpg', 'rb').read()
            image_data = MIMEImage(img_data, name=os.path.basename('assets/guided_gradcam.jpg'))
            msg.attach(image_data)
            FROM = "visker.keras@gmail.com"
            TO = str(email).split(",")

            import smtplib
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
            except:
                 server = smtplib.SMTP('smtp.gmail.com', 465)
            server.starttls()
            server.login("visker.keras@gmail.com", "Pass@1234")
            server.sendmail(FROM, TO, msg.as_string())
            server.quit()
        except Exception as e:
            print('mail error'+str(e))

        #for firebase no need.
        '''
        imageBlob=bucket.blob("images/"+new_filename)
        imageBlob.upload_from_filename('some_image.png')
        imageBlob=bucket.blob("gradcam/"+'gradcam_'+datafr.label1+"_"+ac+"_"+new_filename.split(".")[0])
        imageBlob.upload_from_filename('assets/gradcam.jpg')
        imageBlob=bucket.blob("guided_backprop/"+'guided_backprop_'+"_"+datafr.label1+"_"+ac+"_"+new_filename.split(".")[0])
        imageBlob.upload_from_filename('assets/guided_backprop.jpg')
        imageBlob=bucket.blob("guided_gradcams/"+'guided_gradcam_'+"_"+datafr.label1+"_"+ac+"_"+new_filename.split(".")[0])
        imageBlob.upload_from_filename('assets/guided_gradcam.jpg')
        '''
        filename = "some_image.png"
        parser = createParser(filename)
        metadata = extractMetadata(parser)
        linestring=[]
        counterline=0
        for line in metadata.exportPlaintext():
            if counterline==0:
                linestring.append(html.Div([html.H5(line)]))
                counterline+=1
            else:
                linestring.append(html.Div([html.P(line)]))

        datafr.loader+=10
        try:
            linestring=linestring.split("\n")[1:]
            linestring="\n".join(linestring)
        except:
            pass



        

        
        originalcard=html.Div([
        dbc.Card(
    [
        dbc.CardBody(
            [dbc.CardTitle(new_filename)]
        ),
        dbc.CardImg(
            src=(
                'data:image/png;base64,{}'.format(string)
            )
        ),
         dbc.CardBody(
            [
                dbc.CardText(
                   html.P("Original Image")
                ),
            ]
        ),
    ],
    style={"max-width": "250px"},
),
],className="twelve columns")
        

        cardgradcam=dbc.Card(
    [
        dbc.CardBody(
            [dbc.CardTitle("Gradcam")]
        ),
        dbc.CardImg(
            src=(
                'data:image/jpg;base64,{}'.format(img1)
            )
        ),
         dbc.CardBody(
            [
                dbc.CardText(
                   ac
                ),
            ]
        ),
    ],
    style={"max-width": "250px"},
)

        cardprop=dbc.Card(
    [
        dbc.CardBody(
            [dbc.CardTitle("Guided Backpropogation")]
        ),
        dbc.CardImg(
            src=(
                'data:image/jpg;base64,{}'.format(img2)
            )
        ),
         dbc.CardBody(
            [
                dbc.CardText(
                   ac
                ),
            ]
        ),
    ],
    style={"max-width": "250px"},
)
        cardguided=dbc.Card(
    [
        dbc.CardBody(
            [dbc.CardTitle("Guided Gradcam")]
        ),
        dbc.CardImg(
            src=(
                'data:image/jpg;base64,{}'.format(img3)
            )
        ),
         dbc.CardBody(
            [
                dbc.CardText(
                   ac
                ),
            ]
        ),
    ],
    style={"max-width": "250px"},
)




        nnn = ToastNotifier() 
        datafr.loader+=10
        nnn.show_toast("Visker ", "Task is Completed", duration = 5, 
         icon_path ="assets/favicon.ico") 

        
        datafr.check1=1
        return [


            html.Div([

                 dbc.Card(
            [
                dbc.CardHeader("Visker \u2b50"),
                dbc.CardBody(
                    [   html.Div([



                        html.Div([
                        originalcard],className="five columns offset-by-one"),
                        html.Div([

                            html.Div([
                                
                                html.Div(linestring),
                                ],className='eight columns'),
                            ],className="six columns"),

                        ],className='row'




                                 ),
                    ]
                ),
            ]
        )

                ],className="twelve columns"),



            dbc.Card(
            [
                dbc.CardHeader(datafr.label1+" thinks that it is "+ ac),
                dbc.CardBody(
                    [


                        html.Div([
                         html.Div([

            html.Div([
                cardgradcam


                ],className="four columns"),


            html.Div([
                cardprop

                ],className="four columns"),


            html.Div([

                cardguided
                ],className="four columns"),






            ],className="row"),



                    ],className="eleven columns offset-by-one",style={"margin-top":"10px","margin-":"10px"}),



                         ]),])]




        return [
            html.Div([cardgradcam]),
            html.Img(src='data:image/jpg;base64,{}'.format(img1)),
                 html.Img(src='data:image/jpg;base64,{}'.format(img2)),
                 html.Img(src='data:image/jpg;base64,{}'.format(img3)),
                    ]



           
    else:
        return []




@app.callback(Output('output-image-3', 'children'),
              [Input('dropdown', 'value')],
              [State('dropdown-1','value'),
               State('dropdown-1','options'),
               State('knob','value'),
               State('email','value')])
def update_graph_interactive_image(content,number,label,knob,email):
    if (content is not None) and (datafr.check)==1:
        for i in label:
            if i['value']==number:
                datafr.label2=i['label']
        datafr.check=0
        datafr.loader=0
        datafr.d1=dict()
        datafr.predict=knob
        datafr.flags1=1
        img=Image.open('some_image.png')
        print(img)
        number=number
        print('-----------')
        aa=datafr.d[content][0]
        model = build_model(number)
        guided_model = build_guided_model(number)
        layer_name=''
        if number==1:
            layer_name='res5c_branch2c'
        elif number==0:
            layer_name='block5_conv3'
        elif number==2:
            layer_name='normal_add_2_12'
        elif number==3:
            layer_name='conv_dw_13'
            
        gradcam, gb, guided_gradcam = compute_saliency(model, guided_model,layer_name=layer_name,img_path=img, cls=aa, visualize=False, save=True,string=number)
        
        img1=''
        with open("assets/gradcam.jpg", "rb") as imageFile:
            img1=base64.b64encode(imageFile.read()).decode("utf-8")
        img2=''
        with open("assets/guided_backprop.jpg", "rb") as imageFile:
            img2=base64.b64encode(imageFile.read()).decode("utf-8")
        img3=''
        with open("assets/guided_gradcam.jpg", "rb") as imageFile:
            img3=base64.b64encode(imageFile.read()).decode("utf-8")
      
        ac=content
        try:
            img_data = open('some_image.png', 'rb').read()
            msg = MIMEMultipart()
            msg['Subject'] = 'Keras Visualtion Tool Report'
            tempstring="The probability predicted by the "+datafr.label2+" model are"+str(datafr.d1)
            text = MIMEText(tempstring)
            msg.attach(text)
            image_data = MIMEImage(img_data, name=os.path.basename('some_image.png'))
            msg.attach(image_data)
            img_data = open('assets/gradcam.png', 'rb').read()
            image_data = MIMEImage(img_data, name=os.path.basename('assets/gradcam.png'))
            msg.attach(image_data)
            img_data = open('assets/guided_backprop.png', 'rb').read()
            image_data = MIMEImage(img_data, name=os.path.basename('assets/guided_backprop.png'))
            msg.attach(image_data)
            img_data = open('assets/guided_gradcam.png', 'rb').read()
            image_data = MIMEImage(img_data, name=os.path.basename('assets/guided_gradcam.png'))
            msg.attach(image_data)
            FROM = "visker.keras@gmail.com"
            TO = str(email).split(",")

            import smtplib
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
            except:
                 server = smtplib.SMTP('smtp.gmail.com', 465)
            server.starttls()
            server.login("visker.keras@gmail.com", "Pass@1234")
            server.sendmail(FROM, TO, msg.as_string())
            server.quit()
        except Exception as e:
            print('mail error'+str(e))


        ##for firebase no need
        '''
        imageBlob=bucket.blob("gradcam/"+'gradcam_'+datafr.label1+"_"+content+"_"+datafr.new_filename.split(".")[0])
        imageBlob.upload_from_filename('assets/gradcam.jpg')
        imageBlob=bucket.blob("guided_backprop/"+'guided_backprop_'+"_"+datafr.label1+content+"_"+datafr.new_filename.split(".")[0])
        imageBlob.upload_from_filename('assets/guided_backprop.jpg')
        imageBlob=bucket.blob("guided_gradcams/"+'guided_gradcam_'+"_"+datafr.label1+content+"_"+datafr.new_filename.split(".")[0])
        imageBlob.upload_from_filename('assets/guided_gradcam.jpg')

        '''
        datafr.loader+=10
        cardgradcam=dbc.Card(
    [
        dbc.CardBody(
            [dbc.CardTitle("Gradcam")]
        ),
        dbc.CardImg(
            src=(
                'data:image/jpg;base64,{}'.format(img1)
            )
        ),
         dbc.CardBody(
            [
                dbc.CardText(
                   ac
                ),
            ]
        ),
    ],
    style={"max-width": "250px"},
)

        cardprop=dbc.Card(
    [
        dbc.CardBody(
            [dbc.CardTitle("Guided Backpropogation")]
        ),
        dbc.CardImg(
            src=(
                'data:image/jpg;base64,{}'.format(img2)
            )
        ),
         dbc.CardBody(
            [
                dbc.CardText(
                   ac
                ),
            ]
        ),
    ],
    style={"max-width": "250px"},
)
        cardguided=dbc.Card(
    [
        dbc.CardBody(
            [dbc.CardTitle("Guided Gradcam")]
        ),
        dbc.CardImg(
            src=(
                'data:image/jpg;base64,{}'.format(img3)
            )
        ),
         dbc.CardBody(
            [
                dbc.CardText(
                   ac
                ),
            ]
        ),
    ],
    style={"max-width": "250px"},
)
        nnn = ToastNotifier() 
        datafr.loader+=10
        nnn.show_toast("Visker ", "Task is Completed", duration = 5, 
         icon_path ="assets/favicon.ico") 

        datafr.check=1
        return [dbc.Card(
            [
                dbc.CardHeader(datafr.label2+" thinks that it is "+ str(list(datafr.d1)[0])),
                dbc.CardBody(
                    [


                        html.Div([
                         html.Div([

            html.Div([
                cardgradcam


                ],className="four columns"),


            html.Div([
                cardprop

                ],className="four columns"),


            html.Div([

                cardguided
                ],className="four columns"),






            ],className="row"),



                    ],className="eleven columns offset-by-one",style={"margin-top":"10px","margin-":"10px"}),



                         ]),])]




        return [
            html.Div([cardgradcam]),
            html.Img(src='data:image/jpg;base64,{}'.format(img1)),
                 html.Img(src='data:image/jpg;base64,{}'.format(img2)),
                 html.Img(src='data:image/jpg;base64,{}'.format(img3)),
                    ]



           
    else:
        return []

        return [html.Img(src='data:image/jpg;base64,{}'.format(img1)),
                 html.Img(src='data:image/jpg;base64,{}'.format(img2)),
                 html.Img(src='data:image/jpg;base64,{}'.format(img3)),]




'''
@app.callback(Output('output-image-1', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename')])
def update_graph_interactive_image(content,new_filename):
    if content is not None:
         new_image_string = base64.b64encode(buff123.getvalue()).decode("utf-8")
         return [html.Img(src='data:image/gif;base64,{}'.format(new_image_string))]
'''

page_2_layout = html.Div([

    dcc.Interval(id="interval123", interval=1000, n_intervals=0),
    dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="assets/keras-logo-small-wb-1.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Visker", className="ml-4")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/",
            ),
            
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.NavItem(dbc.NavLink("Page1", href="/page-1")),
            dbc.NavItem(dbc.NavLink("Page2", href="/page-2")),
          
        ],
        color="dark",      
        dark=True,
        sticky="top",
    ),

    
        html.Div(id='upload-check-123'),

    html.Div([
    dbc.Button("Generate Gif 	\ud83d\udc4b", id="submitthree", className="mr-1",color="warning",outline=True,style={"margin-bottom":"5px","margin-top":"5px",'border':"#FFC107 2px solid "}),
    ],className="ten columns offset-by-one",style={"margin-bottom":"5px"}),
    html.Div( id='output-images-123',className="ten columns offset-by-one",style={"margin-bottom":"3px"}),
           html.Div( id='output-image-123',className="ten columns offset-by-one"),
 
   
])



buff123 = BytesIO()
def getaddress():
    try:
        filenames = sorted((os.getcwd()+'/one/three/'+fn for fn in os.listdir('./one/three') if fn.endswith('.jpg')))
        images = []
        for filename in filenames:
            images.append(imageio.imread(filename))
        imageio.mimsave(data123.databuff, images,duration=1.1,format="GIF")
        return 1
    except Exception as e:
        print(e)
        
        return 0



def load_images_from_folder(folder):
    images = []
    filename_list=[]
    for filename in os.listdir(folder):
        filename_list.append(filename)
        imageFile=os.path.join(folder,filename)
        with open(imageFile, "rb") as imageFile:
            img=base64.b64encode(imageFile.read()).decode("utf-8")
        if img is not None:
            images.append(img)
    return images,filename_list



@app.callback(Output('output-images-123', 'children'),
              [Input('submitthree', 'n_clicks')])
def update_graph_interactive_image(content):
    if data123.third123>=90:
         data123.flags123=1
         zz=getaddress()
         if zz==1:
             new_image_string = base64.b64encode(data123.databuff.getvalue()).decode("utf-8")
             return [
                 html.H5("Output Gif"),
                 html.Img(src='data:image/gif;base64,{}'.format(new_image_string))]
         else:
            return []
    else:
        return []






@app.callback(Output('output-image-123', 'children'),
              [Input('upload-data-123','contents')],
              [State('upload-data-123', 'filename')])
def update_graph_interactive_image(content,new_filename):
    #print(content,new_filename,number,knob,email,datafr.check1)
    if (content is not None) and (datafr.check1==1):
        datafr.load123=1
        data123.third123=0
        data123.databuff=BytesIO()
        data123.flags123=0
        string = content.split(';base64,')[-1]
        imgdata = base64.b64decode(string)
        filename = 'one/two/intermediate.png'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)
            
        model=build()
        imagetensor=path_img('one/two/intermediate.png')
        #print(imagetensor)
        
        b=plot_activations(model=model, img_tensor=imagetensor, images_per_row=16, verbose=False, do_postprocess=True)
        print(b)
        array,name=load_images_from_folder('one/one')
        arrays123=[html.H5("Output Layers")]
        maxwidth=1300
        data123.third123+=5
        for i in range(len(array)):
            namesr=name[i].split(".")
            namesr=namesr[0]
            
            arrays123.append(html.Div([

                
                dbc.Card(
                            [
                                dbc.CardBody(
                                    [dbc.CardTitle(namesr)]
                                ),
                                dbc.CardImg(
                                    src=(
                                        'data:image/jpg;base64,{}'.format(array[i])
                                    )
                                ),
                                
                            ],
                            style={"max-width": str(maxwidth)},
                        )
                                      



       



                ],style={"margin-top:":"5px","margin-bottom:":"5px"}))
            maxwidth-=30
        datafr.load123=0
        data123.third123+=5
        nnn = ToastNotifier() 
        nnn.show_toast("Visker ", "Task is Completed", duration = 5, 
         icon_path ="assets/favicon.ico") 
        return arrays123




@app.callback(
dash.dependencies.Output('upload-check-123', 'children'),
[Input('interval123', 'n_intervals')])
def set_cities_options(value):
    if datafr.load123==0:
        return [
            html.Div([
            html.H5('Choose Image 	\ud83d\uddc3\ufe0f'),
            dcc.Upload(
                    id='upload-data-123',
                    children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
            ,' 	\ud83d\udcc1'
                    ]),
                    style={
                        'width': '100%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin-bottom':'100%',
                        'margin': '1%'
                    },
                    # Allow multiple files to be uploaded
                   accept='image/*'
                )],className="ten columns offset-by-one")]
    elif datafr.load123==1:
        psps="..."
        if(value%6==0):
            psps='...'
        elif(value%2==0):
            psps='..'
        elif(value%3==0):
            psps='.'


        return [html.Div([html.Div([
                            html.Div([html.Div([html.P(str(data123.third123)+"%",style={'top':'-2px','heigth':'25px','width':'25%','position': 'relative','left': '53%','transform':'translateX(-50%)'})
                            ],style={'background-color': 'orange','width':str(data123.third123)+"%",'height': '20px','border-radius':'10px'})
                                                ],style={'background-color':'black','padding':'3px','border-radius': '13px'}),html.P("",style={"margin-bottom":"10px"}),html.P("\ud83d\udcdc Getting Analysed"+psps,style={"margin-bottom":"10px"}),html.P(""),
                                      html.Hr(style={'margin-top':'2%','margin-bottom':'1%'})]),],className="ten columns offset-by-one",style={"margin-top":"10px"})]









# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here

wb.open('http://127.0.0.1:8050/')
if __name__ == '__main__':
    app.run_server(debug=True,threaded=True,host ='0.0.0.0',use_reloader=False)

