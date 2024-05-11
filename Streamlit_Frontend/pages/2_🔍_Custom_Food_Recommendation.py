import streamlit as st
from Generate_Recommendations import Generator
from ImageFinder.ImageFinder import get_images_links as find_image
import pandas as pd
from streamlit_echarts import st_echarts

st.set_page_config(page_title="Custom Food Recommendation", page_icon="🔍",layout="wide",initial_sidebar_state="collapsed")
nutrition_values=['Calories','FatContent','SaturatedFatContent','CholesterolContent','SodiumContent','CarbohydrateContent','FiberContent','SugarContent','ProteinContent']
if 'generated' not in st.session_state:
    st.session_state.generated = False
    st.session_state.recommendations=None

video_container_css = """
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
"""

video_css = """
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
"""

st.markdown(
    """
    <div style="{}">
        <video autoplay muted loop style="{}">
            <source src="https://cloudconvert-files.s3.eu-central-1.amazonaws.com/a584e468-9ee6-47e5-b184-be1ecd7ebd0d/bggbgbgb%20%281%29.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAI2WCZ54772T33JEQ%2F20240511%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20240511T160555Z&X-Amz-Expires=86400&X-Amz-Signature=2c8964a52d3cc816200021130ba6392be9774053c9ffa2886000d5822298b8c1&X-Amz-SignedHeaders=host&response-content-disposition=inline%3B%20filename%3D%22bggbgbgb%20%281%29.mp4%22&response-content-type=video%2Fmp4&x-id=GetObject" type="video/mp4">
            Your browser does not support HTML5 video.
        </video>
    </div>
    """.format(video_container_css, video_css),
    unsafe_allow_html=True
)

class Recommendation:
    def __init__(self,nutrition_list,nb_recommendations,ingredient_txt):
        self.nutrition_list=nutrition_list
        self.nb_recommendations=nb_recommendations
        self.ingredient_txt=ingredient_txt
        pass
    def generate(self,):
        params={'n_neighbors':self.nb_recommendations,'return_distance':False}
        ingredients=self.ingredient_txt.split(';')
        generator=Generator(self.nutrition_list,ingredients,params)
        recommendations=generator.generate()
        recommendations = recommendations.json()['output']
        if recommendations!=None:              
            for recipe in recommendations:
                recipe['image_link']=find_image(recipe['Name'])
        return recommendations

class Display:
    def __init__(self):
        self.nutrition_values=nutrition_values

    def display_recommendation(self,recommendations):
        st.subheader('Recommended recipes:')
        if recommendations!=None:
            rows=len(recommendations)//5
            for column,row in zip(st.columns(5),range(5)):
                with column:
                    for recipe in recommendations[rows*row:rows*(row+1)]:                             
                        recipe_name=recipe['Name']
                        expander = st.expander(recipe_name)
                        recipe_link=recipe['image_link']
                        recipe_img=f'<div><center><img src={recipe_link} alt={recipe_name}></center></div>'     
                        nutritions_df=pd.DataFrame({value:[recipe[value]] for value in nutrition_values})      
                        
                        expander.markdown(recipe_img,unsafe_allow_html=True)  
                        expander.markdown(f'<h5 style="text-align: center;font-family:sans-serif;">Nutritional Values (g):</h5>', unsafe_allow_html=True)                   
                        expander.dataframe(nutritions_df)
                        expander.markdown(f'<h5 style="text-align: center;font-family:sans-serif;">Ingredients:</h5>', unsafe_allow_html=True)
                        for ingredient in recipe['RecipeIngredientParts']:
                            expander.markdown(f"""
                                        - {ingredient}
                            """)
                        expander.markdown(f'<h5 style="text-align: center;font-family:sans-serif;">Recipe Instructions:</h5>', unsafe_allow_html=True)    
                        for instruction in recipe['RecipeInstructions']:
                            expander.markdown(f"""
                                        - {instruction}
                            """) 
                        expander.markdown(f'<h5 style="text-align: center;font-family:sans-serif;">Cooking and Preparation Time:</h5>', unsafe_allow_html=True)   
                        expander.markdown(f"""
                                - Cook Time       : {recipe['CookTime']}min
                                - Preparation Time: {recipe['PrepTime']}min
                                - Total Time      : {recipe['TotalTime']}min
                            """)                       
        else:
            st.info('Couldn\'t find any recipes with the specified ingredients', icon="🙁")
    def display_overview(self,recommendations):
        if recommendations!=None:
            st.subheader('Overview:')
            col1,col2,col3=st.columns(3)
            with col2:
                selected_recipe_name=st.selectbox('Select a recipe',[recipe['Name'] for recipe in recommendations])
            st.markdown(f'<h5 style="text-align: center;font-family:sans-serif;">Nutritional Values:</h5>', unsafe_allow_html=True)
            for recipe in recommendations:
                if recipe['Name']==selected_recipe_name:
                    selected_recipe=recipe
            options = {
        "title": {"text": "Nutrition values", "subtext": f"{selected_recipe_name}", "left": "center"},
        "tooltip": {"trigger": "item"},
        "legend": {"orient": "vertical", "left": "left",},
        "series": [
            {
                "name": "Nutrition values",
                "type": "pie",
                "radius": "50%",
                "data": [{"value":selected_recipe[nutrition_value],"name":nutrition_value} for nutrition_value in self.nutrition_values],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
            }
        ],
    }
            st_echarts(options=options, height="600px",)
            st.caption('You can select/deselect an item (nutrition value) from the legend.')

title="<h1 style='text-align: center;'>Custom Food Recommendation</h1>"
st.markdown(title, unsafe_allow_html=True)


display=Display()

with st.form("recommendation_form"):
    st.header('Nutritional values:')
    Calories = st.slider('Calories', 0, 2000, 500)
    FatContent = st.slider('FatContent', 0, 100, 50)
    SaturatedFatContent = st.slider('SaturatedFatContent', 0, 13, 0)
    CholesterolContent = st.slider('CholesterolContent', 0, 300, 0)
    SodiumContent = st.slider('SodiumContent', 0, 2300, 400)
    CarbohydrateContent = st.slider('CarbohydrateContent', 0, 325, 100)
    FiberContent = st.slider('FiberContent', 0, 50, 10)
    SugarContent = st.slider('SugarContent', 0, 40, 10)
    ProteinContent = st.slider('ProteinContent', 0, 40, 10)
    nutritions_values_list=[Calories,FatContent,SaturatedFatContent,CholesterolContent,SodiumContent,CarbohydrateContent,FiberContent,SugarContent,ProteinContent]
    st.header('Recommendation options (OPTIONAL):')
    nb_recommendations = st.slider('Number of recommendations', 5, 20,step=5)
    ingredient_txt=st.text_input('Specify ingredients to include in the recommendations separated by ";" :',placeholder='Ingredient1;Ingredient2;...')
    st.caption('Example: Milk;eggs;butter;chicken...')
    generated = st.form_submit_button("Generate")
if generated:
    with st.spinner('Generating recommendations...'): 
        recommendation=Recommendation(nutritions_values_list,nb_recommendations,ingredient_txt)
        recommendations=recommendation.generate()
        st.session_state.recommendations=recommendations
    st.session_state.generated=True 

if st.session_state.generated:
    with st.container():
        display.display_recommendation(st.session_state.recommendations)
    with st.container():
        display.display_overview(st.session_state.recommendations)