# DataHouse-Nikhil

Coding challenge for DataHouse

## Title : Compatibility calculator

An application that gives us the compaitbility score of applicants based on the attributes of the team and the applicants.

## Usage :

Once you clone/fork the repo and setup the project,
Run python3 project.py

If you want to use your own data with a new team and applicants
in project.py, assign your new data to our data variable
data = <your data>
and after saving your changes
Run python3 project.py

## How does it calculate the compatibility of applicants?

1. Calculate average attributes of team : We first calculate the average value for each attribute (intelligence, strength, endurance, spicyFoodTolerance) across all team members. This average serves as a benchmark for assessing the compatibility of applicants.
   [Why use python dict {} for average_attributes : since we store a key value pair , dictionary comes very handy for this approach]

2. Calculate compatibility score for each applicant : For each applicant, we then calculate a compatibility score based on the difference between the applicant's attributes and the team's average attributes. The score for each attribute is calculated as follows:
   1. Subtract the applicant's attribute value from the team's average attribute value.
   2. Take the absolute value of the difference to ensure it is non-negative.
   3. Divide by 10,as attribute scores are between 1 and 10 and this gives us a score between 0 and 1.
   4. Subtract the result from 1, so that now a higher score indicates a better match .
   5. Average the scores.

Finally, we return a list of applicants along with their compatibility scores

## How can we improve this?

1. Come up with a better logic to compare compatibility
2. we can always sort the result out to show most compatibile person to least
