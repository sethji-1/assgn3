import MapReduce
import sys
 

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
#as if I am going to :p

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    
    mr.emit_intermediate(value[:-10], key)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mr.emit(list_of_values)
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open('data/dna.json')
    mr.execute(inputdata, mapper, reducer)
