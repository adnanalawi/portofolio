import streamlit as st 

def cv():
    st.title("ADNAN ALAWI")
    st.text("adnan.alawi46@gmail.com"  " |"  "linkedin.com/in/adnanalawi"  "|"  "github.com/adnanalawi/portofolio")
    

    st.subheader("About")
    
    st.markdown("""
    <style> .main > div {
        padding-left: 12rem;
        padding-right: 12rem;
        }
        </style> """, unsafe_allow_html=True)
    
    st.markdown('''
                <div style='text-align: justify;'>
                A self-driven industrial engineer graduate from Institut Teknologi Bandung (ITB), 
                seeking opportunities to leverage his diverse skills in the field of industrial engineering. 
                He is passionate about gaining practical experience through internships or job roles that will enhance his expertise. 
                During his studies, he excelled in independent work and performed well in collaborative environments. 
                With a strong curiosity and commitment to continuous learning, he is eager to explore new knowledge, 
                particularly in data analyst, manufacturing, production systems, and quality management to foster personal and professional growth.
                ''',
                unsafe_allow_html=True)
    
 
    st.subheader("Experience")
    st.markdown('''
                <div> 
                <div style='text-align: justify;'>
                <p style="font-family: monospace; font-size: 14px; ">
                <style>
                [data-testid="stMarkdownContainer"] ul{
                padding-left:15px;
                }
                </style>
                
                **Production System Intern** | Makmur Group (Oct 2023 - June 2024)
                - Analyzing the causes of discrepancies between targets and actual results (Root-Cause Analysis)
                - Proposing improvements in work methods to minimize cycle time
                - Proposing improvements in task assignment to workstations (line balancing)
                - Determining the standard time
                - Determining production capacity
                - Conducting sensitivity analysis

                </p>
                </div>
                ''', unsafe_allow_html=True)
    
    
    st.markdown('''
                <div> 
                <div style='text-align: justify;'>
                <p style="font-family: monospace; font-size: 14px; ">
                <style>
                [data-testid="stMarkdownContainer"] ul{
                padding-left:15px;
                }
                </style>
                
                **MSIB Studi Independen** | Data Science (Feb 2024 - June 2024)
                - Lean SQL, Python, Deployment, etc.
                - Learn and creating an interactive dashboard using Tableau
                - Learn traditional machine learning methods (classification, regression, clustering), time series. 
                
                
                </p>
                </div>
                ''', unsafe_allow_html=True)
    
    st.markdown('''
                <div> 
                <div style='text-align: justify;'>
                <p style="font-family: monospace; font-size: 14px; ">
                <style>
                [data-testid="stMarkdownContainer"] ul{
                padding-left:15px;
                }
                </style>
                
                **Assistant Academic of Integrated-System Design and Practicum IV (PPST IV)** | (Aug 2023 - Dec 2023)
                - Handle 2 groups each consisting of 3-4 people, to understand the practicum module (5 modules).
                - Conduct assistance activities for each module & provide feedback at the end of each module.
                - Responsible for Module 4 activities & create supporting videos for the implementation of Module 4.
                
                </p>
                </div> 
                ''', unsafe_allow_html=True)
    st.markdown('''
                <div> 
                <div style='text-align: justify;'>
                <p style="font-family: monospace; font-size: 14px; ">
                <style>
                [data-testid="stMarkdownContainer"] ul{
                padding-left:15px;
                }
                </style>
                
                **Quality Control Intern** | PT Artheria Daya Mulia (Dec 2022 - Feb 2023)
                - Identifying types of defects in the production system
                - Analyzing the causes of the defect, and providing recommendations to reduce it.
                </p>
                </div>
                ''', unsafe_allow_html=True)
    
    st.subheader("Education")
    st.markdown(
        '''
        <div> 
        <div style='text-align: justify;'>
        <style>
        [data-testid="stMarkdownContainer"] ul{
        padding-left:15px;
        }
        </style>
        
        **Institut Teknologi Bandung** | Industrial Engineer
        - GPA: 2,69
        - Thesis: Proposed Workstation Improvement Using Gang Process Chart and a Mathematical Model Approach In 
        the Jellygum Product Packaging Line at PT Makmur Artha Sejahtera
        - Related Course : Database System, Probability and Statistics, Data Analytics, and Data Science (at MSIB Studi Independen)
        </div>
        ''', unsafe_allow_html=True)
    
    st.subheader("Skills")
    st.markdown(
        '''
        <div> 
        <style>
        [data-testid="stMarkdownContainer"] ul{
        padding-left:15px; }
        </style>
        
        - Programming : Python, SQL 
        - Data Visualization : Tableau, Python Data Visualization Library (with documentation)
        - Office : Microsoft Office (Word, Excel, PowerPoint, Visio)
        </div>
        ''', unsafe_allow_html=True
    )
    
