
# HashTable consist of:
# Lst = list of list
# size = number of items
# cap = Table size
class HashTable:
	def __init__(self, size):
		self.table = [[]] * size # A Python list that represents a hash table.
		self.total_count = 0 # number of items
		self.size = size # size of table
		self.collisions = 0
	def __eq__(self, other):
		return (type(other) == HashTable
				and self.table == other.table
				and self.size == other.size
				and self.total_count == other.total_count
				and self.collisions == other.collisions
				)
	def __repr__(self):
		return "Table: %r \nSize: %r \nItems: %r \nCollisions: %r\n" % (self.table, self.size, self.total_count, self.collisions)

####################################################

# Null -> ht
# returns empty hash table with initial size of 8.
# def empty_hash_table():
#	pass
def empty_hash_table():
	return HashTable(8)

# ht, key, item -> ht
# Takes in key and item, and inserts into hashtable. 
# If load factor 1.5, doubles table .
# Rehashes on duplicate keys.
# def insert(ht, key, item):
#	pass
def insert(ht, key, item):
	hasher = hash(key) % ht.size
	if ht.table[hasher] == []:
		ht.table[hasher] = ht.table[hasher] + [(key,item)]
		ht.total_count += 1

	elif ht.table[hasher] != []:
		has_duplicate = False
		for i in ht.table[hasher]:
			if i[0] == key:
				ht = remove(ht, key)
				ht.table[hasher] = ht.table[hasher] + [(key,item)]
				ht.total_count += 1
				ht.collisions += 1
				has_duplicate = True

		if has_duplicate == False:
			ht.table[hasher] = ht.table[hasher] + [(key, item)]
			ht.total_count += 1
			ht.collisions += 1

	if load_factor(ht) > 1.5:
		return rehash(ht)

	return ht

# ht, key -> item
# returns item in hash table associated to key.
# If key pair not found, returns LookupError.
# def get(ht,key):
#	pass
def get(ht, key):
	hasher = hash(key) % ht.size
	for i in ht.table[hasher]:
		if i[0] == key:
			return i[1]

	raise LookupError()

# ht, key -> ht
# remove key-value pair from hash table, and returns resulting hash table.
# If key pair not found, returns LookupError.
# def remove(ht,key):
#	pass
def remove(ht,key):
	hasher = hash(key) % ht.size
	for i in ht.table[hasher]:
		if i[0] == key:
			ht.table[hasher].remove(i)
			ht.total_count -= 1
			return ht

	raise LookupError()

# ht -> value
# returns size of hash table.
# def size(ht):
#	pass
def size(ht):
	return ht.total_count

# ht -> value
# returns load factor of hash table.
# def load_factor(ht):
#	pass
def load_factor(ht):
	return ht.total_count / ht.size

# ht -> value
# returns number of collisions that occured during hashing.
# def collisions(ht):
#	pass
def collisions(ht):
	return ht.collisions

#ht -> ht
# returns ht with double size and rehashes all values.
# def rehash(ht):
#	pass
def rehash(ht):
	new_table = HashTable(ht.size * 2)
	for chain_list in ht.table:
		for i in chain_list:
			new_table = insert(new_table, i[0], i[1])
	return new_table

####################################################