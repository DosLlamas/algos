
# Possible output values
TEAM_1_WINS = 1
TEAM_2_WINS = 2
TIE = 0

# Function to get the score of a basketball game from input
def getScore():
   # Read in the number of each shot made
   oneShots,twoShots,threeShots = map(int, input().split())
   
   # Compute the score based on the number of shots made of each type
   resultingScore = oneShots * 1 + twoShots * 2 + threeShots * 3
   
   # Return the resulting score
   return resultingScore


# Get the score for both teams
team1Score = getScore()
team2Score = getScore()

# Determine which score was better
if team1Score > team2Score:
   print(TEAM_1_WINS)
elif team1Score < team2Score:
   print(TEAM_2_WINS)
else:
   print(TIE)
