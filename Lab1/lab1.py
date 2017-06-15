#* Section 1 (Git)

#* persnickety

#* Section 2 (Data Definitions)

#* 1) A degCelsius is a float value that represents a temperature in Celsius.
# A degFahrenheit is a float value that represents a temperature in Fahrenheit. 

#* 2) A Price is an integer value that represents a price of something in cents.

#* 3) Represents a record for both an item and its price.
class PriceRecord:
  def __init__(self,name,cents):
    self.name = name  # A string that represents an item's name.
    self.cents = cents # An integer that represents an item's price in cents.
    
  def __eq__(self,other):
    type_eq = (type(other) == PriceRecord)
    cents_eq = (self.cents == other.cents)
    name_eq = (self.name == other.name)
    return cents_eq and name_eq and type_eq
  
  def __repr__(self):
    return '%s = %f cents' % (self.name,self.cents)

#* 4) Represents an open tab in a web browser. 
class Tabs:
  def __init__(self,url,month,day,year):
    self.url = url # A string that represents the url in a tab.
    self.month = month  # An integer that represents the month of the access date.
    self.day = day  # An integer that represents the day of the access date.
    self.year = year # An integer that represents the year of the access date.
    
  def __eq__(self,other):
    type_eq = (type(other) == Tabs)
    url_eq = (self.url = other.url)
    month_eq = (self.month == other.month)
    day_eq = (self.day == other.day)
    year_eq = (self.year == other.year)
    return url_eq and month_eq and day_eq and year_eq and type_eq
  
  def __repr__(self):
    return '%s on %d/%d/%d' % (self.url,self.day,self.month,self.year)
  
#* Section 3 (Signature, Purpose Statements, Headers)

#* 1)
#float float --> float
#Returns a price withadded sales tax.
def addTax(price,tax):
  pass

#* 2)
# str -> float
# Takes in an item name as a string and returns a price for that item.
def findPrice(name):
  pass

#* 3)
# Database GeoRegion -> int
# Takes in a certain database and geographic region and returns a median income for said region.
def findMedIncome(database, geoRegion):
  pass

#* 4)
# Database GeoRegion -> City(s)
# Takes in a certain database and geographic region inside the database. Returns cities that overlap with said region.
def findCitiesOverlap(database, geoRegion):
  pass
    
#* Section 4 (Test Cases)

#* 1)
#int int int --> int
#Takes in three numbers and returns the second largest.
def secondLargest(x,y,z):
  pass

def test_1(self):
  self.assertEqual(secondLargest(1,2,3),2)
  
def test_2(self):
  self.assertEqual(secondLargest(4,5,7),5)
  
#* 2)
#str --> bool
#Takes in a string and returns true if no capital letters, and false if not.
def LookforCapitals(string):
  pass

def test_capitals(self):
  string = "I suck Apple Nuts"
  test = LookForCaptials(string)
  self.assertEqual(test,False)

def test_capitals(self):
  string = "hey dude"
  test = LookForCaptials(string)
  self.assertEqual(test,True)

#* 3)
#State State --> State
#Takes in 2 States and returns the one closest to the north pole.
def MostNorth(state1,state2):
  pass

def test_closest_state_1(self):
  state1 = "Alabama"
  state2 = "California"
  self.assertEqual(MostNorth(state1,state2),"California")
  
def test_closest_state_2(self):
  state1 = "Michigan"
  state2 = "Florida"
  self.assertEqual(MostNorth(state1,state2_,"Michigan")
                   
#* Section 5 (Whole Functions)

#* 1)
#float --> float
#Converts feet to meters.
def f2m(feet):
	meters = 0.3048 * feet
	return meters
                
#* 2)
#Represents a musical note with pitch and its duration in seconds
class MusicalNote:
	def __init__(self,pitch,length):
		self.pitch = pitch #pich is a float
		self.length = length #length is a float that represents duration of time in seconds

	def __eq__(self,other):
		type_eq = (type(other) == MusicalNote)
		pitch_eq = (self.pitch == other.pitch)
		length_eq = (self.length == other.length)
		return type_eq and pitch_eq and length_eq

	def __repr__(self):
		return "Pitch: %f, Duration: %f secs" % (self.pitch,self.length)                  

#* 3)
#MusicalNote --> MusicalNote
#Returns a musical note that has two times the frequency of the input note.
def up_one_octave(note):
	new_note = note.pitch * 2
	return MusicalNote(new_note,note.length)

#* 4)
#MusicalNote --> None
#Doubles the frequency the of a musical note without having to return a new note.
def up_one_octave_m(note):
	note.pitch *= 2
	return None
