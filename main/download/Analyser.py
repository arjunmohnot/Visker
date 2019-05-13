## Bootstrap Grid tutorial - adding style to the app
# -*- coding: utf-8 -*-

import dash 
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import base64
import webbrowser as wb
import datetime
import matplotlib.pyplot as plt
import plotly.plotly as py
import dash_daq as daq
import os,sys
import datetime
import datafr
import dash_table
import numpy as np
import pandas as pd

'''
def csvDf(dat,**kwargs): 
  from numpy import array
  data = array(dat)
  if data is None or len(data)==0 or len(data[0])==0:
    return None
  else:
    print(pd.DataFrame(data[:,:],index=data[:,0],columns=data[0,:],**kwargs))
    return pd.DataFrame(data[1:,1:],index=data[1:,0],columns=data[0,1:],**kwargs)


data=[['name','number']]
for i in range(5):
    data.append([str(i),str(i+990)])
df1=csvDf(data)
print(df1.to_dict("rows"))
'''

app = dash.Dash(__name__)
# Boostrap CSS.
#app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})  # noqa: E501
#dcc._css_dist[0]['/assets'].append('stylesheet.css')
app.config['suppress_callback_exceptions']=True
app.layout = html.Div(

          html.Div(
            [   html.Div([
                html.H1("Keras Visualization Tool"),
                html.Img(src='/assets/bennett.png'),
                ],className="banner"),
    html.Div([
         html.Div([dcc.Interval(
                    id='interval-component',
                    interval=1*1000, # in milliseconds
                    n_intervals=0
                )]),
    html.Div([
            
                html.Div(children='''
                        Dash: A web application framework made with Python \ud83d\udc8e 
                        ''',
                        className='nine columns'    )
            ], className="row"
        ),
      html.Div([
      html.Div([html.H6("	\u231a Time: ")],className='one columns'),    
      html.Div([
                        daq.LEDDisplay(
                            id='my-LED-display',
                            color="#FF5E5E",
                            size=14,
                            value=str(datetime.datetime.now().strftime('%H:%M:%S'))
                        ),],style={'margin-bottom':'0.6%'},className='five columns'),
      ],className='row'),



               
]),


 html.Div([

          html.Div(id='output-1'),
          html.Div(id='output-2'),



          html.Div([
                         html.Button(id='my-button-1', n_clicks=0,children='Download',style={'border': 'solid #0069D9 1px', 'color': 'black'}),
                    ],style={'margin-top': '1.0%'}),

          ]),

          html.Div([
          dcc.ConfirmDialogProvider(
        children=html.Button(
            'Delete Database',style={'border': 'solid #0069D9 1px', 'color': 'black'}
        ),
        id='danger-danger-provider',
        message='Total database is going to be deleted! Are you sure you want to continue?'
    ),
    ],style={'margin-top': '1.0%','margin-bottom':'1.0%'}),
    html.Div(id='output-provider'),

                
                ]),
         

          )



@app.callback(Output('output-provider', 'children'),
              [Input('danger-danger-provider', 'submit_n_clicks')])
def update_output(submit_n_clicks):
    if not submit_n_clicks:
        return ''


    from google.cloud import storage
    from firebase import firebase
    import os
    import urllib
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'visker-c7e9b-firebase-adminsdk-1uux2-7438cacf30.json'
    firebase=firebase.FirebaseApplication('https://visker-c7e9b.firebaseio.com/')
    client=storage.Client()
    bucket=client.get_bucket('visker-c7e9b.appspot.com')
    blobs=bucket.list_blobs()
    audios=[]
    videos=[]
    pdf=[]
    images=[]
    for blob in blobs:
        blob=str(blob).split("Audio Records /")
        try:
            blob=blob[1]
            audios.append(blob)
        except:
            pass
        blob=str(blob).split("Video/")
        try:
            blob=blob[1]
            videos.append(blob)
        except:
            pass
        blob=str(blob).split("Pdfs/")
        try:
            blob=blob[1]
            pdf.append(blob)
        except:
            pass



    for i in range(len(audios)):
        bucket=client.get_bucket('hire-1457d.appspot.com')
        blob = bucket.blob('Audio Records /'+audios[i][:-1:])
        blob.delete()

    for i in range(len(videos)):
        bucket=client.get_bucket('hire-1457d.appspot.com')
        blob = bucket.blob('Video/'+videos[i][:-3:])
        blob.delete()

    for i in range(len(pdf)):
        bucket=client.get_bucket('hire-1457d.appspot.com')
        blob = bucket.blob('Pdfs/'+pdf[i][:-5:])
        blob.delete()


    
    return """
        Database Deleted !
        
    """





@app.callback(
        dash.dependencies.Output('output-1', 'children'),
        [dash.dependencies.Input('my-button-1', 'n_clicks')])
def update_image_src(n):
    if n and datafr.var==0:
        datafr.var=1
        from google.cloud import storage
        from firebase import firebase
        import os
        import urllib
        if not os.path.exists("gradcam"):
            os.makedirs("gradcam")
        if not os.path.exists("guided_backprop"):
            os.makedirs("guided_backprop")
        if not os.path.exists("guided_gradcams"):
            os.makedirs("guided_gradcams")
        if not os.path.exists("images"):
            os.makedirs("images")
        
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'visker-c7e9b-firebase-adminsdk-1uux2-7438cacf30.json'
        firebase=firebase.FirebaseApplication('https://visker-c7e9b.firebaseio.com/')
        client=storage.Client()
        bucket=client.get_bucket('visker-c7e9b.appspot.com')
        blobs=bucket.list_blobs()
        audios=[]
        videos=[]
        pdf=[]
        images=[]
        for blob in blobs:
            print(blob)
            blob=str(blob).split("gradcam/")
            try:
                blob=blob[1]
                audios.append(blob)
            except:
                pass
            blob=str(blob).split("guided_backprop/")
            try:
                blob=blob[1]
                videos.append(blob)
            except:
                pass
            blob=str(blob).split("guided_gradcams/")
            try:
                blob=blob[1]
                pdf.append(blob)
            except:
                pass
            blob=str(blob).split("images/")
            try:
                blob=blob[1]
                images.append(blob)
            except:
                pass


        for i in range(len(audios)):
            bucket=client.get_bucket('visker-c7e9b.appspot.com')
            blob = bucket.blob('gradcam/'+audios[i][:-1:])

            print('gradcam/'+audios[i][:-1:])
            if not os.path.exists('gradcam/'+audios[i][:-1:]):
                blob.download_to_filename('gradcam/'+audios[i][:-1:])
        
        print(videos)
        for i in range(len(videos)):
            try:
                bucket=client.get_bucket('visker-c7e9b.appspot.com')
                blob = bucket.blob('guided_backprop/'+videos[i][:-1:])
                print('guided_backprop/'+videos[i][:-1:])
                if not os.path.exists('guided_backprop/'+videos[i][:-1:]):
                    blob.download_to_filename('guided_backprop/'+videos[i][:-1:])
            except Exception as e:
                print(e)
        
        for i in range(len(pdf)):
            bucket=client.get_bucket('visker-c7e9b.appspot.com')
            blob = bucket.blob('guided_gradcams/'+pdf[i][:-1:])
            print('guided_gradcam/'+pdf[i][:-1:])
            if not os.path.exists('guided_gradcams/'+pdf[i][:-1:]):
                blob.download_to_filename('guided_gradcams/'+pdf[i][:-1:])
        
        datafr.var=0
        return []





        
   



@app.callback(
        dash.dependencies.Output('my-LED-display', 'value'),
        [dash.dependencies.Input('interval-component', 'n_intervals')]
    )
def update_output(value):
        return str(datetime.datetime.now().strftime('%H:%M:%S'))


@app.callback(
        dash.dependencies.Output('output-2', 'children'),
        [dash.dependencies.Input('interval-component', 'n_intervals')]
    )
def update_output(n):
       
        
        if datafr.var==1:
            return [
                
                html.Div([html.Img(src="assets/image.gif")])]               
        else:
            return []




wb.open('http://127.0.0.1:8060/')
if __name__ == '__main__':
    app.run_server(debug=True,threaded=True,host ='0.0.0.0',use_reloader=False,port=8060)

    
        

