import pandas as pd

df = pd.read_csv("app/data/matches_clean.csv")

venue_mapping = {
    "Arun Jaitley Stadium, Delhi": "Arun Jaitley Stadium",
    "Brabourne Stadium, Mumbai": "Brabourne Stadium",
    "Eden Gardens, Kolkata": "Eden Gardens",
    "Narendra Modi Stadium, Ahmedabad": "Narendra Modi Stadium",
    "Rajiv Gandhi International Stadium, Uppal, Hyderabad": "Rajiv Gandhi International Stadium",
    "Sawai Mansingh Stadium, Jaipur": "Sawai Mansingh Stadium",
    "Wankhede Stadium, Mumbai": "Wankhede Stadium",
    "Punjab Cricket Association Stadium, Mohali": "Punjab Cricket Association Stadium",
    "Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh":
        "Punjab Cricket Association Stadium",
    "MA Chidambaram Stadium, Chepauk, Chennai":
        "MA Chidambaram Stadium",
    "Dr DY Patil Sports Academy, Mumbai":
        "Dr DY Patil Sports Academy",
    "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam":
        "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
    "Barsapara Cricket Stadium, Guwahati":
        "Barsapara Cricket Stadium",
    "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow":
        "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium",
    "Himachal Pradesh Cricket Association Stadium, Dharamsala":
        "Himachal Pradesh Cricket Association Stadium",
    "Maharashtra Cricket Association Stadium, Pune":
        "Maharashtra Cricket Association Stadium",
    "Maharaja Yadavindra Singh International Cricket Stadium, New Chandigarh":
        "Maharaja Yadavindra Singh International Cricket Stadium",
    "Vidarbha Cricket Association Stadium, Jamtha":
        "Vidarbha Cricket Association Stadium",
    "Zayed Cricket Stadium, Abu Dhabi":
        "Zayed Cricket Stadium",
}

df["venue"] = df["venue"].replace(venue_mapping)

df.to_csv("app/data/matches_clean.csv", index=False)

print("Dataset cleaned successfully.")