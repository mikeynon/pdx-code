# FUN WITH DATA STRUCTURES
NFLTEAMS = {
    {AFC,
{East,
{Buffalo Bills,
        Miami Dolphins,
        New England Patriots,
        New York Jets}}
{North,
    {Baltimore Ravens,
        Cincinnati Bengals,
        Cleveland Browns,
        Pittsburgh Steelers}}
{South,
{Houston Texans,
        Indianapolis Colts,
        Jacksonville Jaguars,
        Tennessee Titans}}
{West,
 {Denver Broncos,
        Kansas City Chiefs,
        Oakland Raiders,
        San Diego Chargers}}}
{NFC
{East,
{Dallas Cowboys,
        New York Giants,
        Philadelphia Eagles,
        Washington Redskins}}
{North,
 {Chicago Bears,
        Detroit Lions,
        Green Bay Packers,
        Minnesota Vikings}}
{South,
 {Atlanta Falcons,
        Carolina Panthers,
        New Orleans Saints,
        Tampa Bay Buccaneers}}
{West,
 {Arizona Cardinals,
        Los Angeles Rams,
        San Francisco 49ers,
        Seattle Seahawks}}}
}
# LAB: FUN WITH DATA STRUCTURES

#
# OBJECTIVE
#
# Prompt the user with something like the following:
conf_name = input("Enter NFC or AFC:"\n)
# Enter the name of either a conference or team:
# If the user enters the name of a conference (either ‘AFC’ or ‘NFC’), prompt them for a division (‘East’, ‘North’, ‘South’, or ‘West’) and print out the names of the corresponding teams.
if conf_name = "N":
    div_name = input("Enter E, N, S or W:"\n)
elif conf_name = "A":
    div_name = input("Enter E, N, S or W:"\n)
else:
    return
    # If the user enters the name of a team, print out the corresponding conference and division (e.g., if the user enters ‘Seattle Seahawks’, print ‘NFC West’).
#
# If the user enters input that doesn’t match your data, prompt them again.
#
# Open Atom or PyCharm
# Create a file named nflteams.py
# Think through the problem in terms of the following:
# Setup
# Input
# Transform
# Output
# Stub out functions to handle small, discrete parts of the larger problem
# Bonus: For your pure functions, write doctests to ensure they work as expected
# # KEY CONCEPTS
#
# Data structures
# Comparison operators
# DATA
#
# You will need to put the following data into a data structure that allows you to access it using the input you expect from the user:
#

# EXTRA CREDIT
#
# If you get through the basic assignment and want to push yourself, try one or more of the following:
#
# Make your program work with another layer of data (e.g., players on each team)
# Make your program resilient to missing data (e.g., delete the teams from the AFC East [Sorry, Pats fans!])
# Make your program work with a different data set altogether (e.g., Cuisines/Dishes/Ingredients)