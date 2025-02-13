#
# header comment!
#
import sqlite3
import objecttier



# prints general statistics about lobbyist database
def genStats(dbConn):
    print()
    print("General Statistics:")
    print("  Number of Lobbyists:", f"{objecttier.num_lobbyists(dbConn):,}")
    print("  Number of Employers:", f"{objecttier.num_employers(dbConn):,}")
    print("  Number of Clients:", f"{objecttier.num_clients(dbConn):,}")


# Given user input of a name, find and output basic information for all lobbyists 
# where either their first or last name can match that name. 
# User can enter SQL wildcards such as % or _
def basic_lobbyists_info(dbConn):
    name = input("\nEnter lobbyist name (first or last, wildcards _ and % supported): ")
    lobbylist = objecttier.get_lobbyists(dbConn, name)

    print("\nNumber of lobbyists found:", len(lobbylist))
    print()
    if len(lobbylist) > 1000:
        print("There are too many lobbyists to display, please narrow your search and try again...")
    else:
        for l in lobbylist:
            print(f"{l.Lobbyist_ID} : {l.First_Name} {l.Last_Name} Phone: {l.Phone}")


# Given a lobbyist ID, find and output detailed information about the lobbyist
def detailed_lobbyist_info(dbConn):
    l_id = input("\nEnter Lobbyist ID: ")
    lobbyist = objecttier.get_lobbyist_details(dbConn, l_id)
    print()
    if lobbyist:
        print(l_id, ':')
        print("  Full Name:", lobbyist.Salutation, lobbyist.First_Name, lobbyist.Middle_Initial, lobbyist.Last_Name, lobbyist.Suffix)
        print(f"  Address: {lobbyist.Address_1} {lobbyist.Address_2} , {lobbyist.City} , {lobbyist.State_Initial} {lobbyist.Zip_Code} {lobbyist.Country}")
        print("  Email:", lobbyist.Email)
        print("  Phone:", lobbyist.Phone)
        print("  Fax:", lobbyist.Fax)
        print("  Years Registered:", ", ".join([str(y) for y in lobbyist.Years_Registered]) + ", ")
        print("  Employers:", ", ".join(lobbyist.Employers) + ", ")
        print(f"  Total Compensation: ${lobbyist.Total_Compensation:,.2f}")
    else:
        print("No lobbyist with that ID was found.")


# Given year and N, output the top N lobbyists based on their total compensation for that year.
def top_n_lobbyists(dbConn):
    N = input("\nEnter the value of N: ")
    if int(N) < 0: # error check
        print("Please enter a positive value for N...")
        return
    year = input("Enter the year: ")
    lobbylist = objecttier.get_top_N_lobbyists(dbConn, int(N), year)
    print()
    count = 0;
    for l in lobbylist:
        count += 1
        print(  count, '.', l.First_Name, l.Last_Name)
        print("  Phone:", l.Phone)
        print("  Total Compensation:", f"${l.Total_Compensation:,.2f}")
        print("  Clients:", ', '.join(l.Clients) + ', ')


# Register an existing lobbyist for a new year. Allow the user to enter the ID of 
# the lobbyist and the year, and then insert this information into the database.
def register_new_year(dbConn):
    year = input("\nEnter year: ")
    l_id = input("Enter the lobbyist ID: ")
    if objecttier.add_lobbyist_year(dbConn, l_id, year) > 0:
        print("\nLobbyist successfully registered.")
    else:
        print("\nNo lobbyist with that ID was found.")


# Set the salutation for a given lobbyist. If the lobbyist already has a salutation, 
# it will be replaced by this new value. 
def set_salutation(dbConn):
    l_id = input("\nEnter the lobbyist ID: ")
    salutation = input("Enter the salutation: ")
    if objecttier.set_salutation(dbConn, l_id, salutation) > 0:
        print("\nSalutation successfully set.")
    else:
        print("\nNo lobbyist with that ID was found.")


##################################################################  
#
# main
#
print('** Welcome to the Chicago Lobbyist Database Application **')

dbConn = sqlite3.connect('Chicago_Lobbyists.db')
genStats(dbConn)

print()
cmd = input("Please enter a command (1-5, x to exit): ")
while cmd != "x":
    if cmd == "1":
        basic_lobbyists_info(dbConn)
    elif cmd == "2":
        detailed_lobbyist_info(dbConn)
    elif cmd == "3":
        top_n_lobbyists(dbConn)
    elif cmd == "4":
        register_new_year(dbConn)
    elif cmd == "5":
        set_salutation(dbConn)
    else:
        print("**Error, unknown command, try again...")

    print()
    cmd = input("Please enter a command (1-5, x to exit): ")

dbConn.close()
#
# done
#
