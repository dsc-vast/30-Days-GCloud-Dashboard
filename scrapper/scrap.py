def scrap(url):
    import requests
    import json
    from bs4 import BeautifulSoup

    # Challenges according to syllabus
    CHALLENGES_AVAILABLE = [
      'Integrate with Machine Learning APIs', 
      'Perform Foundational Data, ML, and AI Tasks in Google Cloud', 
      'Explore Machine Learning Models with Explainable AI', 
      'Engineer Data in Google Cloud', 
      'Insights from Data with BigQuery', 
      'Deploy to Kubernetes in Google Cloud', 
      'Build and Secure Networks in Google Cloud', 
      'Deploy and Manage Cloud Environments with Google Cloud', 
      'Set up and Configure a Cloud Environment in Google Cloud', 
      'Perform Foundational Infrastructure Tasks in Google Cloud', 
      'Getting Started: Create and Manage Cloud Resources',
      ]

    #Empty array to hold the completed quests
    COMPLETED_QUESTS = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Get the profile details
    profile = soup.findAll('div', attrs = {'class':'public-profile__hero'})[0]
    name = profile.h1.text.strip()
    # Gets an array with no. of labs in index:1 and no. of quests in index:4 
    total = str(soup.find('p', attrs = {'class':'public-profile__hero__details l-mbm'}).text).split('\n')

    # Get all the completed quest details into quests
    quests = soup.findAll('ql-badge')
    
    for row in quests:
        
        # Compare with the syllabus and add if it is in the syllabus
        if json.loads(row['badge'])['title'] in CHALLENGES_AVAILABLE:
            COMPLETED_QUESTS.append(json.loads(row['badge'])['title'])

    
    total_completed = {'Name': name, 'completed_quests':COMPLETED_QUESTS ,'labs': total[1], 'quests': total[4] }
    return(total_completed)
