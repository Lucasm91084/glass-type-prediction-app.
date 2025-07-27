{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Glass Type Prediction App\
\
This is a Streamlit-based web application that predicts the type of glass based on its chemical composition using a trained machine learning model.\
\
## Features\
\
- Input features: RI, Na, Mg, Al, Si, K, Ca, Ba, Fe\
- Predicts glass type (e.g. windows, containers, headlamps)\
- Displays class label meaning\
- Interactive interface built with Streamlit\
\
## Model\
\
- Trained using a Random Forest Classifier\
- Includes StandardScaler for preprocessing\
\
## How to Run\
\
```bash\
streamlit run app.py\
}