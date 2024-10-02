import streamlit as st
import webbrowser
import numpy as np
# from helper import *

emotion_video_recommendations = {
    'angry': [
        'Calming music',
        'Relaxation techniques',
        'Workout videos for venting stress'
        'Guided Meditation for Anger Management',
        'Relaxing Nature Sounds',
        'Yoga for Anger Release',
        'Stress-Relief Music',
        'Boxing Workout for Stress Relief',
        'Motivational Speech: Overcoming Anger',
        'Deep Breathing Exercises',
        'Therapeutic Art',
        'Progressive Muscle Relaxation',
        'Anger Management Techniques'
    ],
    'disgust': [
        'Funny videos',
        'Feel-good content',
        'Positive or inspirational stories',
        'Heartwarming Animal Rescue Stories',
        'Positive Affirmations for a Better Day',
        'Comedy Skits to Make You Laugh',
        'Funny Bloopers Compilation',
        'Feel-Good Stories: Acts of Kindness',
        'Motivational Talks on Positive Thinking',
        'Stand-up Comedy Clips',
        'Uplifting Music Playlist',
        'Overcoming Negativity: Mental Health Tips'
    ],
    'fear': [
        'Motivational content',
        'Self-help videos',
        'Meditation',
        'Breathing exercises',
        'Overcoming Fear: Motivational Speech',
        'Relaxing Sounds for Anxiety Relief',
        'Meditation for Calming Fear and Anxiety',
        'Guided Visualization for Fear Reduction',
        'Breathing Exercises for Anxiety',
        'Inspirational Stories of Courage',
        'Fear of Failure: How to Overcome It',
        'TED Talks on Facing Fears',
        'Stress Relief Yoga for Anxiety',
        'How to Conquer Public Speaking Fear'
    ],
    'happy': [
        'Music videos',
        'Happy Songs That Instantly Boost Your Mood',
        'Top 10 Funniest Stand-Up Comedy Moments',
        'Upbeat Music Playlist for Happiness',
        'Feel-Good Dance Music Videos',
        'Uplifting Inspirational Stories',
        'Comedies',
        'Dance videos',
        'Feel-good movie clips'
    ],
    'neutral': [
        'Documentaries',
        'Tech/gadget reviews',
        'Interesting Documentaries You Should Watch',
        'Informative Ted Talks on Technology and Innovation',
        'Best Tech Gadget Reviews of the Year',
        'Day in the Life Vlogs from Around the World',
        'Historical Documentaries on Fascinating Topics',
        'Educational Videos on Latest Scientific Discoveries',
        'Relaxing Ambient Music for Focus',
        'Productivity Tips for a Balanced Life',
        'Interviews with Thought Leaders',
        'Educational Podcasts and Video Lessons on Any Subject'
    ],
    'sad': [
        'Inspirational talks',
        'Soothing music',
        'Mental health awareness videos',
        'Motivational Videos for Overcoming Sadness',
        'Guided Meditation for Emotional Healing',
        'Soothing Piano Music for Relaxation',
        'Mental Health Awareness Talks',
        'Inspiring Stories of Overcoming Adversity',
        'Comforting Music for Sad Days',
        'How to Stay Positive During Hard Times',
        'Therapist Talks on Dealing with Grief',
        'Relaxing Rain Sounds for Peaceful Sleep',
        'Mindfulness Meditation for Emotional Balance'
    ],
    'surprise': [
        'Pranks',
        'Magic tricks',
        'Reaction videos'
        'Mind-Blowing Optical Illusions',
        'Top 10 Prank Videos to Blow Your Mind',
        'Unbelievable Magic Tricks You Won’t Believe',
        'Surprising Facts You Didn’t Know',
    ]
}



st.sidebar.title("Dashboard")

app_mode = st.sidebar.selectbox("Select Page", ["Image Emotion Prediction"])


# Home Page
if(app_mode == "Image Emotion Prediction"):
    st.header("Emotion Detection")
    
    # Load image
    test_image = st.file_uploader("Choose an Image")
    
    if(st.button("Show Image")):
        st.image(test_image, use_column_width=True)
    
    if(st.button("Predict")):
        st.write("Our Prediction")
    
        result = "angry"
        st.success(f"{result}")

        size = len(emotion_video_recommendations[result])
        index = int(np.random.rand()*size)
        video_type = emotion_video_recommendations[result][index]
        # webbrowser.open(f"https://www.youtube.com/results?search_query={video_type}")
        # st.markdown(f"[Click here for YouTube recommendations](https://www.youtube.com/results?search_query={video_type})")
        st.components.v1.html(f"<iframe width='560' height='315' src='https://www.youtube.com/results?search_query={video_type}' frameborder='0'></iframe>")



        
        
