import streamlit as st 
import pandas as pd


def portfolio():
    st.title("PORTOFOLIO")
    
    st.markdown("""
    <style> .main > div {
        padding-left: 12rem;
        padding-right: 12rem;
        }
        </style> """, unsafe_allow_html=True)
   
    st.markdown("")
    st.header("RFM Analysis")
    st.markdown('''
                <div> 
                <div style='text-align: justify;'>
                <p style="font-family: monospace; font-size: 14px; ">
                <style>
                [data-testid="stMarkdownContainer"] ul{
                padding-left:15px;
                }
                </style>
                
                Recency, Frequency, and Monetary Analysis (RFM Analysis) is the analysis used to identify a group of customers or behavior 
                based on the historical record of their purchases. Recency means the interval between the last transaction and the latest event, 
                Frequency means the number of successful purchases from the customer, and monetary means how high the value of the total customer was made. 
                Each component (Recency, Frequency, Monetary) must be defined first and the number of the category is determined based on the objective of the analysis, 
                and a group combination of RFM value will be defined as customer segmentation.
                
                </p>
                </div>
                ''', unsafe_allow_html=True)
    
    st.markdown("")
    st.subheader("Data Preprocessing")
    st.markdown('''
                Dataset: Thelook_ecommerce
                ''')
    
    st.code('''
            -- Query Variable 
            WITH RecencyData AS (
                SELECT 
                    oi.user_id,
                    datediff('2024-03-31', max(oi.created_at)) as Last_order, 
                    count(oi.user_id) as Number_of_transaction, 
                    sum(round(sale_price, 0)) as Total_transaction 
                FROM  
                    tem.order_items as oi
                WHERE 
                    oi.status in ('complete', 'shipped', 'processing') AND oi.created_at >= '2023-01-01'
                GROUP BY 
                    user_id ), 
                
                RFM_Calculated AS (
                SELECT 
                    user_id,
                    Last_order,
                    Number_of_transaction,
                    Total_transaction,

                    -- Conditional Recency
                    CASE 
                        WHEN Last_order BETWEEN 315 AND 455 THEN '1' 
                        WHEN Last_order BETWEEN 172 AND 314 THEN '2' 
                        WHEN Last_order BETWEEN 29 AND 171 THEN '3'  
                        ELSE 'Unknown'
                    END AS Recency,

                    -- Conditional Frequency
                    CASE 
                        WHEN Number_of_transaction BETWEEN 1 AND 4 THEN '1'
                        WHEN Number_of_transaction BETWEEN 5 AND 8 THEN '2' 
                        WHEN Number_of_transaction BETWEEN 9 AND 13 THEN '3' 
                        ELSE 'Unknown'
                    END AS Frequency,

                    -- Conditional Monetary
                    CASE 
                        WHEN Total_transaction BETWEEN 0 AND 596 THEN '1' 
                        WHEN Total_transaction BETWEEN 597 AND 1193 THEN '2' 
                        WHEN Total_transaction BETWEEN 1194 AND 1789 THEN '3' 
                        ELSE 'Unknown'
                    END AS Monetary
                FROM
                    RecencyData )

                -- Main Query
                SELECT 
                    user_id,
                    Last_order,
                    Number_of_transaction,
                    Total_transaction,
                    Recency,
                    Frequency,
                    Monetary,
                    concat(Recency, Frequency, Monetary) as RFM,

                    CASE
                        WHEN concat(Recency, Frequency, Monetary) in ('333', '332', '331', '323') THEN 'Stars'
                        WHEN concat(Recency, Frequency, Monetary) in ('322', '321', '313', '312', '311') THEN 'Betrayers'
                        WHEN concat(Recency, Frequency, Monetary) in ('233', '232', '231', '223', '222', '221') THEN 'Frustrated'
                        WHEN concat(Recency, Frequency, Monetary) in ('213', '212', '211') THEN 'Lost'
                        WHEN concat(Recency, Frequency, Monetary) in ('133', '132', '131', '123', '122', '121', '113', '112') THEN 'New'
                        WHEN concat(Recency, Frequency, Monetary) in ('111') THEN 'Tail'

                        ELSE 'UNKNOWN'
                    END AS Segmentation

                FROM RFM_Calculated
                ORDER BY 
                    user_id;

            ''', language="sql")
    
    st.markdown('''
                <div> 
                <div style='text-align: justify;'>
                <p style="font-family: monospace; font-size: 14px; ">
                <style>
                [data-testid="stMarkdownContainer"] ul{
                padding-left:15px;
                }
                </style>
                
                A lower recency score indicates stronger customer engagement, reflecting more recent transactions. 
                Conversely, a higher frequency score demonstrates that the customer engages more frequently. 
                A higher monetary score signifies greater value for the customer. Overall, a higher index score represents better overall performance, 
                with customers showing frequent, recent, and high-value transactions.
                </p>
                </div>
                ''', unsafe_allow_html=True)
    
    # Create a DataFrame
    data = {
        'Index' : ['1', '2', '3'],
        'Recency': ['315 - 455 days', '172 - 314 days', '29 - 171 days'],
        'Frequency': ['1 - 4 times', '5 - 8 times', '9 - 13 times'],
        'Monetery': ['0 - 596 dollar', '597 - 1193 dollar', '1194 - 1789 dollar']
    }

    table = pd.DataFrame(data)

    # Add custom CSS to make the column headers bold
    st.markdown("""
        <style>
        th {
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True)
    
    

    # Render the DataFrame as an HTML table
    st.markdown(table.to_html(index=False), unsafe_allow_html=True)
    
    
    st.markdown('''
                <div> 
                <div style='text-align: justify;'>
                <p style="font-family: monospace; font-size: 14px; ">
                <style>
                [data-testid="stMarkdownContainer"] ul{
                padding-left:15px;
                }
                </style>
                
                There are six customer segment categories, and in each category, there is a score based on the previous table. 
                The stars category is the best, at each customer segment some suggestions can be given to increase "engagement" or "sales". 
                Adjust customer scores to the right categories to get bigger opportunities.
                </p>
                </div
                ''',unsafe_allow_html=True)
    
    # Create a DataFrame with HTML for line breaks
    data = {
       'Category': [
        '3x3x3<br>3x3x2<br>3x3x1<br>3x2x3',  # Stars
        '3x2x2<br>3x2x1<br>3x1x3<br>3x1x2<br>3x1x1',  # Betrayers
        '2x3x3<br>2x3x2<br>2x3x1<br>2x2x3<br>2x2x2<br>2x2x1',  # Frustrated
        '2x1x3<br>2x1x2<br>2x1x1',  # Lost
        '1x3x3<br>1x3x2<br>1x3x1<br>1x2x3<br>1x2x2<br>1x2x1<br>1x1x3<br>1x1x2<br>',  # New
        '1x1x1'  # Tail
    ],

        
        'Label': [
            'Stars', 
            'Betrayers', 
            'Frustrated', 
            'Lost', 
            'New', 
            'Tail'
        ],
        'Explanation': [
            'Top customers with high recency, and high or medium frequency and monetary value',
            'High recency, but medium or low frequency and monetary values. These customers may have purchased from competitors',
            'Customers who have been inactive for about the last six months. Their frequency is moderate, indicating a risk of losing them',
            'Customers who have been inactive for about six months, with medium or low purchase volume. The likelihood of loss is high',
            'Customers who have not been active for over a year, with medium frequency and recency',
            'Low-volume customers who have not been active for more than a year, likely having made only a single purchase'
        ],
        'Action': [
            'Retain these customers: Keep engaging high-value customers. Analyze why their volumes are high and offer tailored solutions. Consider loyalty rewards or exclusive deals to maintain their loyalty',
            'Expand product variety: Use product variety gaps to boost sales by offering more options. Improve the range based on feedback, create targeted promotions, and explore partnerships for exclusive products. Add personalized pricing and recommendations to drive sales',
            'Reach out to them: Engage through personalized outreach, offering tailored promotions or product bundles. Use surveys or focus groups to gather insights for improvement.',
            'Contact them immediately: Quickly re-engage these customers with exclusive, limited-time deals. Assign account managers for personalized service and offer tailored solutions like discounts or invitations to VIP events. Send product recommendations and provide free trials or upgrades, using multiple channels—phone, email, and social media—to maximize outreach.',
            'Strengthen customer relationships: Maintain regular contact with customers to discuss their needs and preferences. Offer tailored product recommendations based on their previous purchases and provide updates on new arrivals or relevant promotions.',
            'Engage high-potential customers: Target these customers with personalized campaigns, product trials, or limited-time offers. Use follow-ups and targeted ads to convert interest into sales.'
        ]
    }

    # Convert DataFrame to HTML and allow unsafe HTML rendering for line breaks
    df = pd.DataFrame(data)

    # Inject custom CSS for text justification
    st.markdown("""
    <style>
    table {
        width: 100%;
    }
    th, td {
        text-align: justify;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Render the table with justifying text
    st.markdown(df.to_html(index=False, escape=False), unsafe_allow_html=True)
    
    st.subheader("Result")
    segmen = {
        'Segmentation' : ['Betrayers', 'Lost', 'Tail', 'Frustrated', 'New', 'Stars'],
        'Total User': ['21,710', '11,226', '8,172', '318', '103', '52' ],
        'Avg Recency' : ['86.8', '239.1', '380.9', '224.2', '356.5', '66.1'],
        'Avg Frequency': ['2.04', '1.6', '1.5', '5.5', '4.2', '9.2'],
        'Avg Monetary': ['121.3', '97.4', '85.8', '325.1', '480.07', '641.3']
        
    }

    table_1 = pd.DataFrame(segmen)

    # Render the DataFrame as an HTML table
    st.markdown("""
    <div style="display: inline-block; width: auto;">
        {}
    </div>
    """.format(table_1.to_html(index=False)), unsafe_allow_html=True)

