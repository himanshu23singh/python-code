names={"rojer","syd"}#they do not repeate the same value in. set
set1={"syd"}
intersect=names & set1#finding common value
print(intersect)
union=names | set1#given in form of union
print(union)
j=names - set1#remove common value
subset=names > set1 #set1 is subset of names if change < than  names is subset if set1