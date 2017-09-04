import pypyodbc
from DFSFootball_Lib import TeamReformat

pypyodbc.lowercase = False
conn = pypyodbc.connect(
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" +
    r"Dbq=C:\Users\mille\OneDrive\Documents\DFSFootball.accdb;")
matchups_cur = conn.cursor()
matchups_cur.execute("SELECT ID, AwayTeam, HomeTeam FROM Matchups");

def_cur = conn.cursor()
def_cur.execute("SELECT Team, DefDVOA FROM DefensiveStats");


while True:
    matchup_row = matchups_cur.fetchone()
    if matchup_row is None:
        break
    Away = TeamReformat(matchup_row.get("AwayTeam"))
    Home = TeamReformat(matchup_row.get("HomeTeam"))

    while True:
        def_row = def_cur.fetchone()
        if def_row is None:
            print(Away + " error")
            break
        if def_row.get("Team") == Away:
            Away_DVOA = def_row.get("DefDVOA")
            break
        


    print(Away + "'s DVOA = " + Away_DVOA)

matchups_cur.close()
def_cur.close()
conn.close()