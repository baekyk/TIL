* HashMap, HashTable
  * stores values in key-value pair
  * contains unique keys
*  HashSet
   *  contains unique elements


### HashSet
   1. AbstractSet class 상속
   2. Set interface 구현
   3. objects are always unique
   4. one null key value is allowed
   5. hashing mechanism을 삽입 시 사용

### HashMap
   1. HashTable을 사용하여 Map interface 구현
   2. AbstaractMap class 상속
   3. key-value pair form
   4. no order for its elements
   5. key is unique
   6. one null as key and multiple null as values

### HashTable
   1. Dictionary class 상속 Map interface 구현
   2. contains elements/objects/items in key-value pair
   3. not allow any duplicate key
   4. 동기화된 특성으로 스레드에서 안전하다
   5. null is not allowed for both key and value
   6. hashcode() : find the position of the elements
    
||HashSet|HashMap|HashTable|
|--|--|--|--|
|allow null |1 value	|1 key , n value|-|
|order|	no|	no|	no|



    
		
