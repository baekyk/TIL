### Decorator
* A decorator is any callable Python object that is used to modify a function, method or class definition. A decorator is passed the original object being defined and returns a modified object, which is then bound to the name in the definition.
  *   μΆμ²: <https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators> 
	
	
* μμ  
    1   @viking_chorus  
	2   def menu_item():  
	3   print("spam")

	    is equivalent to
	
	1 	def menu_item():  
	2 	print("spam")  
	3 	menu_item = viking_chorus(menu_item)
	
	
	
	
	
	
