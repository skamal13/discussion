# Discussion

## Merge Sort
### 1) Is your algorithm correct?
The answer Yes. In theory, Merge Sort divides the array into two halves, recursively sorts them, and finally merges the two sorted halves. so in below code using those steps:
https://github.com/skamal13/discussion/blob/main/merge_sort.py


### 2) Time Complexity?
Time Complexity works in O(n*log n). This is because the list is being split in log(n) calls and the merging process takes linear time in each call.

### 3) Space Complexity?
Space complexity is always O(n). This is because the list have to store the elements somewhere, in this case using arrays.

### 4) Advanced: Improvements on the algorithm? parallelize using multithreading/multiprocessing

### 5) Advanced: What is the recurrence relation of this particular algorithm?

## Operating Systems and Systems Programming

### 1) B trees (B+ Trees) and their relation to data storage (Postgres)
PostgreSQL B-Tree indexes are multi-level tree structures. B-tree indexes can be used for equality and range queries efficiently.
The command to add an index to a column is:
CREATE INDEX name ON table USING btree (column);

### 2) A B tree vs hash table # range queries vs specific 1 element queries
B-tree support range queries in Log(n), but in hash table range queries can result in a full table scan O(n) because indexs can access elements by their primary key in a hashtable. Hash Index really good for specific 1 element queries.

### 3) Postgres Indices
according to postgreSQL documentation, there are 3 Index Types : B-tree, R-tree, and Hash.
B-tree : CREATE INDEX name ON table USING btree (column);
R-tree : CREATE INDEX name ON table USING RTREE (column);
Hash : CREATE INDEX name ON table USING HASH (column);

