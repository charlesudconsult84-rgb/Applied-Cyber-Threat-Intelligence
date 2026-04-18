# Applied-Cyber-Threat-Intelligence
This lab focuses on leveraging the cyber threat intelligence (CTI) process, guiding you through data collection, analysis, contextualization, and integration. You will enhance a starter Python script to fetch data from the OTX API and display relevant threat intelligence.

# The Scenario
You are a cybersecurity analyst tasked with gathering threat intelligence from AlienVault's Open Threat Exchange (OTX) to identify Indicators of Compromise (IOCs) and assess potential risks to your organization. The goal is to create a Python script that interacts with the OTX API to collect data, analyze and prioritize threats, and prepare the intelligence for integration into security operations.

# Tools and Resources
. (Optional) Sign up for an account on AlienVault’s OTX website
  (You only need an account if you want to run the script against real threat intel data)
. IDE: VS Code
. Starter python script otx_starter.py Links to an external site.

# Instructions
Lab Setup:
For the script to pull in threat intel data from OTX, you would need to sign up for an account on AlienVault’s OTX website. 

Step 1: Collecting Threat Data
. Open the provided otx_starter.pyLinks to an external site. in VS Code.
. Rename your file otx.py and then save. You will be submitting this file in Code Grade, so it is important to use this    naming convention. 
. Add a temporary if __name__ == '__main__' block to test the fetch_threat_intelligence function.

Step 2: Analyzing and Processing Data
. Create a new function, parse_threat_intelligence, below the fetch_threat_intelligence function. 
. This function should do the following:
    . Validate the retrieved data.
    . Extract key details, such as pulse names, tags, and indicators.
    . Display the information in a human-readable format.
. Next, update the if __name__ == '__main__' block to call parse_threat_intelligence

Step 3: Contextualizing and Prioritizing Data
Enhance the parse_threat_intelligence function to:
    . Flag high-priority threats based on tags, such as "ransomware" or "phishing."
    . Add a priority field to the displayed output, categorizing threats as "HIGH" or "LOW."

Step 4: Integrating with Security Operations
Update the parse_threat_intelligence function to export the prioritized data to a text file:
    . Write the extracted and prioritized information into a file named otx_intelligence_report.txt.

# Submission and Grading Criteria
Use the rubric below as a guide for how this lab is graded.
Your submission will be automatically scored in CodeGrade. All criterion must be met to pass the AutoTest. 
You can review your submission in CodeGrade and see your final score in your Canvas gradebook.
When you are ready to submit, launch CodeGrade.
    . Click on + Create Submission. Connect your repository for this lab.
    . For additional information on submitting assignments in CodeGrade: Getting Started in CanvasLinks to an external         site.

# Rubic
Lab: Cyber Threat Intelligence (CTI) (1)
Criteria	                                              Ratings
Check fetch_threat_intelligence function                AutoTest Passed                AutoTest Did Not Pass
Check parse_threat_intelligence function                AutoTest Passed                AutoTest Did Not Pass
