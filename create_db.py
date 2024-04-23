
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import errorcode

try:
    cnx1 = mysql.connector.connect(user="root", password="tanish", host="127.0.0.1", database="politicalParties")
    print("success")
    mycursor = cnx1.cursor()
    CREATE_TABLE_SQL = """
    CREATE TABLE political (
        Sr_No VARCHAR(10), 
        Date_of_Encashment DATE, 
        Name_of_the_Political_Party TEXT, 
        Account_no_of_Political_Party TEXT, 
        Prefix TEXT, 
        Bond_Number TEXT, 
        Denominations INT, 
        Pay_Branch_Code TEXT, 
        Pay_Teller TEXT 
    );
    """
    # mycursor.execute(CREATE_TABLE_SQL)
    print("Table political created successfully")
    CREATE_TABLE_two_SQL = """
    CREATE TABLE companies (
    Sr_No VARCHAR(10), 
    Reference_No_URN TEXT, 
    Journal_Date DATE, 
    Date_of_Purchase DATE,
    Date_of_Expiry DATE,
    Name_of_the_Purchaser TEXT, 
    Prefix TEXT, 
    Bond_Number TEXT, 
    Denominations INT, 
    Issue_Branch_Code TEXT, 
    Issue_Teller TEXT, 
    Status TEXT 
);
    
    """
    # mycursor.execute(CREATE_TABLE_two_SQL)
    print("Table companies created successfully")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
    
  else:
    print(err)
else:
  LOAD_DATA_SQL = """
  LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/political_csv.csv'
  INTO TABLE political
  FIELDS TERMINATED BY ','
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 ROWS;
  """

  mycursor.execute(LOAD_DATA_SQL)
  print("CSV data imported into the political table successfully")

  LOAD_DATA_two_SQL = """
  LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/companies_csv.csv'
  INTO TABLE companies
  FIELDS TERMINATED BY ','
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 ROWS;
  """

  mycursor.execute(LOAD_DATA_two_SQL)
  print("CSV data imported into the companies table successfully")
  cnx1.close()
