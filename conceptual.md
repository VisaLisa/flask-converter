### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  Python allows for comparison of dictionaries and lists whereas Javascript doesn't. For example, [1,2,3] !== [1,2,3] in JS however in python [1,2,3] == [1,2,3]. 
  
  Python has an out of the box data structure called a tuple which is not natively out of the box for JS. 
  Python and Javascript also have very different syntax. 
  
  Another difference is that Python has out of the box testing with doctests unlike JS which requires writing tests in another file. Python throws more errors than JS whereas JS will return undefined instead of throwing an error. This can make it difficult to debug JS but also allows someone to take advantage of the idea that JS doesn't throw errors.

  Javascript is a scripting language, where it is commonly used for web development and application
  Python is a object-oriented programming language, which allows the developer to create individual objects (virtual set of building blocks) that are then able to interact with each other or perform actions on their own

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  1. get() method
    print(dict.get('c', 'missing'))
  2. setdefault() method
    print(dict.setdefault('c', 'missing'))
  3. except method
    try: dict['c']
    except: print('missing')


- What is a unit test?
  testing method that an individual unit of source code or individual class/methods/functions

- What is an integration test?
  Testing method that a group of modules/components are tested together

- What is the role of web application framework, like Flask?
  It is a set of functions, classes, etc. that help define which requests to respond to as well as how to respond to requests

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  Depends on the case. For route URL, it is best used for describing the object you are on. However, the query string parameters can provide more "parameters"/description to the object.


- How do you collect data from a URL placeholder parameter using Flask?
  You can specify the variable in the app.route and then use that variable as a paramater in the routing function. Here is an example of the pretzel:

  ```py
  @app.route('/foods/<food>')
  def grocery(food):
   x = food
  ```
  (/foods/pretzel)

- How do you collect data from the query string using Flask?

  With a query string the data can be found in the request.args dictionary:

  ```py
  @app.route('/foods')
  def grocery():
    x = request.args.get('type')
  ```
  (foods?type=pretzel)

- How do you collect data from the body of the request using Flask?
  You can get the data form a post request in the body using the request.form dictionary

  ```py
  @app.route('/foods')
  def grocery():
    x = request.form.get('type')
  ```

- What is a cookie and what kinds of things are they commonly used for?

  A cookie is piece of information which stores the domain, "key", and "value" that gets sent from the server to the client. It allows the client to send back that information to the server so the server can use that information. It allows for a user to go back in to a session to resume where they left off.

- What is the session object in Flask?
  The session object is built off of using cookies. It allows the server to set many different things in the in the session for the client to remember wihout having to create many different cookies and just have one session. It is also encoded so that someone can't change session data on the client before sending it to the server.

- What does Flask's `jsonify()` do?
  jsonify will take JSON serializeable data in python and convert it to a JSON string.
