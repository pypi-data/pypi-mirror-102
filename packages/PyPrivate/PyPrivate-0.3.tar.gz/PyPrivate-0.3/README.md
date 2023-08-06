# Python private

This package is adding [private/protected/public fields](https://en.wikipedia.org/wiki/Access_modifiers) to Python.

**Without PyPrivate:**
```python
class Foo():
	__x = 7 # Private "x"
	def baz(self):
		self.__x += 7

def bar(f, n):
	try:
		getattr(f, n)
	except:
		print('"' + n + '" not found')
	else:
		print('"' + n + '" found')

myfoo = Foo()
myfoo.baz()
bar(myfoo, "__x")     # "__x" not found
bar(myfoo, "_Foo__x") # "_Foo__x" found
```
**With PyPrivate:**
```python
from privatefields import privatefields

@privatefields
class Foo():
	private_x = 7 # Private "x"
	def baz(self):
		self.private_x += 7

def bar(f, n):
	try:
		getattr(f, n)
	except:
		print('"' + n + '" not found')
	else:
		print('"' + n + '" found')

myfoo = Foo()
myfoo.baz()
bar(myfoo, "private_x") # "private_x" not found
print(dir(myfoo)) # no "x"
```

## How to use

PyPrivate is easy to use. To use private/protected fields import "privatefields":
```python
from privatefields import privatefields
```
Next, use it with your classes:
```python
@privatefields
class Foo():
	pass
```
And add prefixes private_/protected_ to your variables/methods names:
```python
self.z           # Public
self.protected_y # Protected
self.private_x   # Private
```

### Friends

You can declare "friend" [classes](https://en.wikipedia.org/wiki/Friend_class)/[functions](https://en.wikipedia.org/wiki/Friend_function). For this add this line to your class:
```python
class Baz(): # This class can use "x"
	pass
class Bar(): # This class can't use "x"
	pass
@privatefields
class Foo():
	friends = [Baz]
	private_x = "Secret data" # Private "x"
```

## What's new

**0.2**
* Added support for removing attributes (__delattr__).
* Replaced error message from "(name) object has no attribute (attribute)" to "attribute (attribute) is private/protected"
* Bugs fixed

**0.3**
* Added suppression of replacing `__attribute` with `_Class__attribute`
* Added flag pythonStyle. This flag replaces `private_` with `__` and `protected_` with `_`
* Bugs fixed

**0.4**
* A global improvement will be added. There will no longer be a need to use the `@privatefields` decorator. All classes will automatically have a private/protected fields system.

**Planned before 0.9**
* Added updated system (beta). Use flag updatedSystem to enable new system.
