import dash_core_components as dcc
import dash_dangerously_set_inner_html
import dash
from dash.dependencies import Input, Output,State
import dash_bootstrap_components as dbc
import dash_html_components as html
import grasia_dash_components as gdc
import datafr

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
app.title = 'My Title'
app.config['suppress_callback_exceptions']=True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

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
                href="https://plot.ly",
            ),
            
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Col(dbc.NavItem(dbc.NavLink("Page", href="#",className="offset-8"))),
          
        ],
        color="dark",      
        dark=True,
        sticky="top",
    ),
    html.Div([

                dbc.Row(
          [


              dbc.Col(

                  html.Div(id='card-1',children=[

],className='five columns offset-by-six'),

       ),

              dbc.Col(
    


    html.Div([
        
        html.Img(src="assets/bob.png",style={"height":"300px"}),
        html.Div(id="outputs",children=[]),
         html.Div(id="startbtnoutput",children=[]),
       
        

      
             
              ]),
    ),




  

    ],  no_gutters=True),








        ],style={'margin-bottom':'300px','margin-top':'20px'}),



    
    html.Div([
    html.Div([
    dbc.Card(
            
            [
                dbc.CardBody(
                    [
                        dbc.CardTitle("This card has a title"),
                        dbc.CardText("and some text, but no header"),
                    ]
                )
            ],
            outline=True,
            color="primary",
            className="card",
        ),

    ],className='card'),
    ],className='ten columns offset-by-one'),


    html.Link(href='/assets/stylesheet.css', rel='stylesheet'),
    gdc.Import(src="https://code.jquery.com/jquery-3.3.1.min.js"),
    gdc.Import(src="assets\z.js"),
    html.Div([dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
        



<!-- some content to allow scrolling :)-->
<div class="hero">
  <div class="overlay"></div>
</div>
<div class="main-content">
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








''')]),


     dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
 
   
])





'''
@app.callback(dash.dependencies.Output('outputs', 'children'),
              [Input("interval", "n_intervals")])
def page_1_dropdown(value):
    if datafr.tempflag==0:
        return [  html.Button("start",id="startbtn")]
    return []


'''


@app.callback(dash.dependencies.Output('card-1', 'children'),
              [Input("interval", "n_intervals")])
def page_1_dropdown(value):
    children=[]
    
    if datafr.tempflag==0:
        if(datafr.steps==0):
            finals="Hello"
            finals1="Press start to continue..."
            if datafr.temps!=finals:
                datafr.temps+=finals[datafr.varcount]
                datafr.varcount+=1
            if datafr.temps==finals:
                datafr.varcount=0
                if datafr.temps1!=finals1:
                    datafr.temps1+=finals1[datafr.varcount1]
                    datafr.varcount1+=1
                if datafr.temps1==finals1:
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
                color="primary",
            )]
        if(datafr.steps==1):
           
            
            children=[dbc.Card(
            [
                dbc.CardBody(
                    [
                        dbc.CardTitle("Enter Your Name"),
                        dbc.CardText("Hi"),
                        dcc.Link('Go to Page 1', href='/page-1'),  
                    ]
                )
            ],
            outline=True,
            color="primary",
        )]

                    
                        

                
            


        
        
    return children
        
            


'''
@app.callback(dash.dependencies.Output('startbtnoutput', 'children'),
              [Input("startbtn", "n_clicks")])
def page_1_dropdown(value):
    datafr.tempflag=1
    return [html.P("Hi hello")]
      

'''        


    






app.config['suppress_callback_exceptions']=True

page_1_layout = html.Div([
    html.H1('Page 1'),
    dcc.Dropdown(
        id='page-1-dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='page-1-content'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),

])

@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              [dash.dependencies.Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)


page_2_layout = html.Div([
    html.H1('Page 2'),
    dcc.RadioItems(
        id='page-2-radios',
        options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
        value='Orange'
    ),
    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])

@app.callback(dash.dependencies.Output('page-2-content', 'children'),
              [dash.dependencies.Input('page-2-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)


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


if __name__ == '__main__':
    app.run_server(debug=True)
