import streamlit as st
from orchestrator_agent import OrchestratorAgent
from assessment_agent import AssessmentAgent  
from nutrition_agent import NutritionAgent
from exercise_agent import ExerciseAgent
from motivation_agent import MotivationAgent
st.set_page_config(page_title="Fitness Helper", layout="wide")
st.markdown("""
<style>
.content-box {
    padding: 20px;
    margin: 10px;
    border: 3px solid orange;
    background: lightyellow;
}
</style>
""", unsafe_allow_html=True)


if 'agents' not in st.session_state:
    agents = {
        'assessor': AssessmentAgent(),
        'nutrition': NutritionAgent(),
        'exercise': ExerciseAgent(),
        'motivation': MotivationAgent()
    }
    
    for agent in agents.values():
        agent.start()
    
    coordinator = OrchestratorAgent()
    coordinator.start(agents['assessor'], agents['nutrition'], agents['exercise'], agents['motivation'])
    
    st.session_state.agents = agents
    st.session_state.coordinator = coordinator


st.title('Fitness Planning Tool')
st.write('Get a custom fitness plan made just for you')


st.write('Your Info')


c1, c2, c3 = st.columns(3)


name = c1.text_input('Name:')
age = c1.number_input('Age:')
weight = c1.number_input('Weight (kg):')
height = c2.number_input('Height (cm):') 
goal = c2.selectbox('Goal:', ['lose weight', 'gain muscle', 'get fit'])
activity = c2.selectbox('Activity:', ['low', 'medium', 'high'])
days = c3.slider('Days per week:', 1, 6, 3)
equipment = c3.selectbox('Equipment:', ['none', 'dumbbells', 'gym', 'home gym'])

# make the big button
if st.button('Make My Plan', type="primary") and name:
    user_info = {
        'name': name, 
        'age': age, 
        'weight': weight, 
        'height': height,
        'goal': goal, 
        'activity_level': activity, 
        'days': days, 
        'equipment': equipment
    }
    
    agents = st.session_state.agents
    
    st.write('Your Personal Plan')
    
    # assessment
    assessment = agents['assessor'].assess(user_info)
    st.write('Assessment:')
    st.write(assessment['plan'])
    
    st.write('Nutrition:')
    nutrition = agents['nutrition'].make_meal_plan(name, user_info)
    st.write(nutrition)
    
    st.write('Exercise:') 
    exercise_plan = agents['exercise'].makeplan(name, user_info)
    st.write(exercise_plan)
    
    # motivation
    st.write('Motivation:')
    motivation = agents['motivation'].give_boost(user_info)
    st.write(motivation)
    
    final_plan = st.session_state.coordinator.buildplan(name, user_info)
    
    if 'error' in final_plan:
        st.error(f"Error: {final_plan['error']}")
    else:
        st.success('Plan completed!')
        st.info(f"Created {final_plan['when']} for {name}")

elif st.button('Make My Plan', type="primary"):
    st.warning('Enter your name first!')