#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
#
# Original author: Ellen Kidane
#
import datatier

##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:
   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone):
      self._Lobbyist_ID = Lobbyist_ID
      self._First_Name = First_Name
      self._Last_Name = Last_Name
      self._Phone = Phone

   # getters
   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Phone(self):
      return self._Phone


 
##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
   def __init__(self, Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2,
                 City, State_Initial, Zip_Code, Country, Email, Phone, Fax, Years_Registered=[], Employers=[], Total_Compensation=0.0):
        self._Lobbyist_ID = Lobbyist_ID
        self._Salutation = Salutation
        self._First_Name = First_Name
        self._Middle_Initial = Middle_Initial
        self._Last_Name = Last_Name
        self._Suffix = Suffix
        self._Address_1 = Address_1
        self._Address_2 = Address_2
        self._City = City
        self._State_Initial = State_Initial
        self._Zip_Code = Zip_Code
        self._Country = Country
        self._Email = Email
        self._Phone = Phone
        self._Fax = Fax
        self._Years_Registered = Years_Registered
        self._Employers = Employers
        self._Total_Compensation = Total_Compensation

   # getters
   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def Salutation(self):
      return self._Salutation

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Middle_Initial(self):
      return self._Middle_Initial

   @property
   def Last_Name(self):
      return self._Last_Name
   @property
   def Suffix(self):
      return self._Suffix

   @property
   def Address_1(self):
      return self._Address_1

   @property
   def Address_2(self):
      return self._Address_2

   @property
   def City(self):
      return self._City

   @property
   def State_Initial(self):
      return self._State_Initial

   @property
   def Zip_Code(self):
      return self._Zip_Code

   @property
   def Country(self):
      return self._Country

   @property
   def Email(self):
      return self._Email

   @property
   def Phone(self):
      return self._Phone

   @property
   def Fax(self):
      return self._Fax

   @property
   def Years_Registered(self):
      return self._Years_Registered

   @property
   def Employers(self):
      return self._Employers

   @property
   def Total_Compensation(self):
      return self._Total_Compensation


 
##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone, Total_Compensation, Clients=[]):
      self._Lobbyist_ID = Lobbyist_ID
      self._First_Name = First_Name
      self._Last_Name = Last_Name
      self._Phone = Phone
      self._Total_Compensation = Total_Compensation
      self._Clients = Clients

   # getters
   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Phone(self):
      return self._Phone
   
   @property
   def Total_Compensation(self):
      return self._Total_Compensation

   @property
   def Clients(self):
      return self._Clients

##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
   try:
      return datatier.select_one_row(dbConn, '''
         SELECT COUNT(Lobbyist_ID)
         FROM LobbyistInfo;
      ''')[0]
   
   except Exception as e:
      return -1

##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
   try:
      return datatier.select_one_row(dbConn, '''
         SELECT COUNT(Employer_ID)
         FROM EmployerInfo;
      ''')[0]
   
   except Exception as e:
      return -1

##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
   try:
      return datatier.select_one_row(dbConn, '''
         SELECT COUNT(Client_ID)
         FROM ClientInfo;
      ''')[0]
   
   except Exception as e:
      return -1

##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
   lobbylist = []
   try:
      # get info
      rows = datatier.select_n_rows(dbConn, '''
         SELECT Lobbyist_ID, First_Name, Last_name, Phone
         FROM LobbyistInfo
         WHERE First_Name LIKE ? OR Last_Name LIKE ?
         ORDER BY Lobbyist_ID ASC;
      ''', (pattern, pattern))

      # process info
      for row in rows:
         Lobbyist_ID, First_Name , Last_Name, Phone = row
         lobbyist = Lobbyist(Lobbyist_ID, First_Name , Last_Name, Phone)
         lobbylist.append(lobbyist)

      return lobbylist
   
   except Exception as e:
      return []


##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):
   try:
      # get info
      details = datatier.select_one_row(dbConn, '''
         SELECT Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, 
            Address_1, Address_2,City, State_Initial, ZipCode, Country, 
            Email, Phone, Fax
         FROM LobbyistInfo
         WHERE Lobbyist_ID = ?
         GROUP BY Lobbyist_ID;
      ''', (lobbyist_id,))

      Total_Compensation = datatier.select_one_row(dbConn, '''
         SELECT SUM(Compensation_Amount)
         FROM Compensation
         WHERE Lobbyist_ID = ?;
      ''', (lobbyist_id,))[0]
      if (Total_Compensation is None):
         Total_Compensation = 0
      
      Years_Registered = datatier.select_n_rows(dbConn, '''
         SELECT Year
         FROM LobbyistYears
         WHERE Lobbyist_ID = ?
         ORDER BY Year ASC;
      ''', (lobbyist_id,))
      Years_Registered = [str(row[0]) for row in Years_Registered]
      
      Employers = datatier.select_n_rows(dbConn, '''
         SELECT DISTINCT Employer_Name
         FROM EmployerInfo
         JOIN LobbyistAndEmployer le ON le.Employer_ID = EmployerInfo.Employer_ID
         WHERE le.Lobbyist_ID = ?
         ORDER BY Employer_Name ASC;
      ''', (lobbyist_id,))
      Employers = [row[0] for row in Employers]

      # process info
      Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2, \
      City, State_Initial, Zip_Code, Country, Email, Phone, Fax = details

      Lobbyist_details = LobbyistDetails(Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, \
                                         Suffix, Address_1, Address_2, City, State_Initial, Zip_Code, Country, \
                                          Email, Phone, Fax, Years_Registered, Employers, Total_Compensation)

      return Lobbyist_details
   
   
   except Exception as e:
      return None
         

##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total 
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid. 
#          An empty list is also returned if an internal error 
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
   lobbylist = []
   try:
      # get info
      rows = datatier.select_n_rows(dbConn, '''
         SELECT l.Lobbyist_ID, l.First_Name, l.Last_Name, l.Phone,
            SUM(c.Compensation_Amount) AS Total_Compensation
         FROM LobbyistInfo l
         JOIN Compensation c ON c.Lobbyist_ID = l.Lobbyist_ID
         JOIN ClientInfo ci ON c.Client_ID = ci.Client_ID
         WHERE strftime('%Y', c.Period_Start) = ?
         GROUP BY l.Lobbyist_ID
         ORDER BY Total_Compensation DESC
         LIMIT ?;
      ''', (year, N,))

      for row in rows:
         Lobbyist_ID, First_Name, Last_Name, Phone, Total_Compensation = row
         
         Clients = datatier.select_n_rows(dbConn, '''
            SELECT ci.Client_Name
            FROM ClientInfo ci
            JOIN Compensation c ON ci.Client_ID = c.Client_ID
            JOIN LobbyistInfo l ON c.Lobbyist_ID = l.Lobbyist_ID
            WHERE strftime('%Y', c.Period_Start) = ?
            AND l.Lobbyist_ID = ?
            GROUP BY c.Client_ID
            ORDER BY ci.Client_Name ASC;
         ''', (year, Lobbyist_ID))
         Clients = [client[0] for client in Clients]
         
         # process info
         if (Total_Compensation is None):
            Total_Compensation = 0

         lobbyclient = LobbyistClients(Lobbyist_ID, First_Name, Last_Name, Phone, Total_Compensation, Clients)
         lobbylist.append(lobbyclient)
      return lobbylist
   except Exception as e:
      return []


##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
   try:
      # check if lobbyist exists
      exists = datatier.select_n_rows(dbConn, '''
         SELECT * 
         FROM LobbyistInfo 
         WHERE Lobbyist_ID = ?
      ''', (lobbyist_id,))

      if not exists or len(exists) < 1:
         return 0
      
      # insert
      datatier.perform_action(dbConn, '''
         INSERT INTO LobbyistYears (Lobbyist_ID, Year) 
         VALUES (?, ?)
      ''', (lobbyist_id, year))

      return 1
   except Exception as e:
      return 0



##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
   try:
      # check if lobbyist exists
      exists = datatier.select_n_rows(dbConn, '''
         SELECT * 
         FROM LobbyistInfo 
         WHERE Lobbyist_ID = ?
      ''', (lobbyist_id,))

      if not exists or len(exists) < 1:
         return 0
      
      # update
      datatier.perform_action(dbConn, '''
         UPDATE LobbyistInfo
         SET Salutation = ?
         WHERE Lobbyist_ID = ?;
      ''', (salutation, lobbyist_id))

      return 1
   except Exception as e:
      return 0
   