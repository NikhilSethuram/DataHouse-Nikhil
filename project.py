#build an application that takes an input: an array of applicants and an array of team
#members, and produces an output: an array of applicants with their respective compatibility
#score.
#TODO : come up with a logic for generating compatability score 
#input : JSON  output : JSON 
#compatibility score ranges 0-1


def compatibility_calculator(team, applicants):
    average_attributes= {'intelligence': 0, 'strength': 0, 'endurance': 0, 'spicyFoodTolerance': 0}
    #lets calculate a standard using team's attributes to compare applicants
    for team_member in team: #team is the list of dict of team members in our input json, here we access each member induvidually
        for attribute, attribute_value in team_member['attributes'].items(): #iterates over key-value pairs in our attributes dict 
            average_attributes[attribute]+= attribute_value #add the respective values to our average attribute dict
    
    #our average_attributes is now complete
    #calculate the average of each attribute [ average = total score/ number of members ]
    for attribute in average_attributes:
        average_attributes[attribute]/=len(team)

    # now lets calculate the score for applicants using the average_attributes we calculated
    applicant_scores = []
    for applicant in applicants: #applicant is the list of dict of applicants in our input json, here we access each applicant induvidually
        compatibilty_score = 0
        for attribute, attribute_value in applicant['attributes'].items(): #iterates over key-value pairs in our attributes dict
            #calculate the difference between applicant's attributes and team's average attributes
            compatibilty_score += 1 - abs(attribute_value - average_attributes[attribute])/10
       #NOTE : we use abs to ensure non negative values
       #       attribute scores are expected to be between 1-10 so we divide by 10 to ensure the value remains between 0-1
       #       finally we subtract this from 1 , this is done so that now a higher value means a better match     
        compatibilty_score /= len(applicant['attributes'])  #average the score
        applicant_scores.append({'name': applicant['name'], 'score': compatibilty_score})
    
    return {'scoredApplicants': applicant_scores}

#Testing 
data = {
    "team": [
        {"name": "Eddie", "attributes": {"intelligence": 1, "strength": 5, "endurance": 3, "spicyFoodTolerance": 1}},
        {"name": "Will", "attributes": {"intelligence": 9, "strength": 4, "endurance": 1, "spicyFoodTolerance": 6}},
        {"name": "Mike", "attributes": {"intelligence": 3, "strength": 2, "endurance": 9, "spicyFoodTolerance": 5}}
    ],
    "applicants": [
        {"name": "John", "attributes": {"intelligence": 4, "strength": 5, "endurance": 2, "spicyFoodTolerance": 1}},
        {"name": "Jane", "attributes": {"intelligence": 7, "strength": 4, "endurance": 3, "spicyFoodTolerance": 2}},
        {"name": "Joe", "attributes": {"intelligence": 1, "strength": 1, "endurance": 1, "spicyFoodTolerance": 10}}
    ]
}


final_scores = compatibility_calculator(data['team'], data['applicants'])
print(final_scores)