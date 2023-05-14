<h1>AirBnB Clone - The Console</h1>
<hr style="size: 1;">
<ul>
    <li>Data Model</li>
    <li>Object management via a console/command interpreter</li>
    <li>Conversion to a file (JSON)</li>
</ul>
<h3>Language: Python</h3>
<hr style="size: 1;">
<h3>Project Description </h3>
<hr style="size: 1;">
<p>To create a sandboxed command line interface through which we can create,
    modify and delete objects in our file storage. This project currently only
    implements the back-end console. It is a complete web application, integrates
    database storage and front-end interfacing in a clone of AirBnB.</p>
<h3>Classes</h3>
<hr style="size: 1;">
<p style="color: grey; font-weight: lighter; font-size: 12rem;">AirBnB utilizes the following classes:</p>
<hr style="size: 1;">
<h3>Storage</h3>
<hr style="size: 1;">
<p>The above classes are handled by the abstracted storage engine defined in the <strong style="color: blue; font-weight: Bold;">FileStorage</strong>  class.
    Every time the backend is initialized, AirBnB instantiates an instance of FileStorage called Storage. 
    The storage object is loaded/re-loaded from any class instances stored in the JSON file file.json. 
    As class instances are created, updated, or deleted, the storage object is used to register 
    corresponding chnages in the file.json.</p>
<hr style="size: 1;">
<h3>Console</h3>
<hr style="size: 1;">
<p>The console is a command line interpreter that permits management
    of the backend of AirBnB. It can be used to handle and manipulate
    all classes utilized by the application (achieved by calls on the
    storage object defined above).</p>
<h3>Using the Console</h3>
<p>The AirBnB console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file console.py at the command line.</p>
<div>
<p>$ echo "help" | ./console.py
        (hbnb) 
        Documented commands (type help <topic>):
        ========================================
        EOF  all  count  create  destroy  help  quit  show  update

        (hbnb)
        $

</p>

</div>
<p>Alternatively, to use the AirBnB console in interactive mode, run the file console.py by itself:</p>
<div>
    <p>$ ./console.py</p>
</div>
<p>While running in interactive mode, the console displays a prompt for input:</p>
<div>
    <p>$ ./console.py</p>
    <p>(hbnb)</p>
</div>
<p>To quit the console, enter the command quit, or input an EOF signal (ctrl-D).</p>
<div>
    <p>$ ./console.py</p>
    <p>(hbnb) quit</p>
    <p>$</p>
</div>
<div>
<p>$ ./console.py</p>
<p>(hbnb) EOF</p>
<p>$</p>
</div>
<h3>Console Commands</h3>
<p>The AirBnB console supports the following commands:</p>
<ul>
<li>create</li>
    <ul><li>Usage: create <class></li></ul>
    <p>Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.</p>
    <p>
    $ ./console.py
(hbnb) create BaseModel
119be863-6fe5-437e-a180-b9892e8746b8
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.119be863-6fe5-437e-a180-b9892e8746b8": {"updated_at": "2019-02-17T2
1:30:42.215277", "created_at": "2019-02-17T21:30:42.215277", "__class__": "Base
Model", "id": "119be863-6fe5-437e-a180-b9892e8746b8"}}
    </p>
<li>show</li>
<ul>
    <li>Usage: show <class> <id> or <class>.show(<id>)</li>
</ul>
<p>Prints the string representation of a class instance based on a given id.</p>
<p>
$ ./console.py
(hbnb) create User
1e32232d-5a63-4d92-8092-ac3240b29f46
(hbnb)
(hbnb) show User 1e32232d-5a63-4d92-8092-ac3240b29f46
[User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-a
c3240b29f46', 'created_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828), 
'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
(hbnb) 
(hbnb) User.show(1e32232d-5a63-4d92-8092-ac3240b29f46)
[User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-a
c3240b29f46', 'created_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828), 
'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
(hbnb) 
</p>

<li>destroy</li>
<ul>
<li>Usage: destroy <class> <id> or <class>.destroy(<id>)</li>
</ul>
<p>Deletes a class instance based on a given id. The storage file file.json is updated accordingly.</p>
<p>
$ ./console.py
(hbnb) create State
d2d789cd-7427-4920-aaae-88cbcf8bffe2
(hbnb) create Place
3e-8329-4f47-9947-dca80c03d3ed
(hbnb)
(hbnb) destroy State d2d789cd-7427-4920-aaae-88cbcf8bffe2
(hbnb) Place.destroy(03486a3e-8329-4f47-9947-dca80c03d3ed)
(hbnb) quit
$ cat file.json ; echo ""
{}
</p>
<li>all</li>
<ul>
<li>Usage: all or all <class> or <class>.all()</li>
</ul>
<p
>Prints the string representations of all instances of a given class. If no class name is provided, the command prints all instances of every class.
</p>
<p>
$ ./console.py
(hbnb) create BaseModel
fce2124c-8537-489b-956e-22da455cbee8
(hbnb) create BaseModel
450490fd-344e-47cf-8342-126244c2ba99
(hbnb) create User
b742dbc3-f4bf-425e-b1d4-165f52c6ff81
(hbnb) create User
8f2d75c8-fb82-48e1-8ae5-2544c909a9fe
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.da
tetime(2019, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2
, 17, 21, 45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[Bas
eModel] (fce2124c-8537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime
(2019, 2, 17, 21, 43, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17,
21, 43, 56, 899348), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
(hbnb)
(hbnb) User.all()
["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetim
e(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17
, 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[User] 
(b742dbc3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2019, 2
, 17, 21, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44,
15, 974608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}"]
(hbnb) 
(hbnb) all
["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetim
e(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17
, 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[BaseMo
del] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.datetime(20
19, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2, 17, 21,
45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[User] (b742db
c3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2019, 2, 17, 2
1, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44, 15, 97
4608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}", "[BaseModel] (fce2124c-8
537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime(2019, 2, 17, 21, 4
3, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17, 21, 43, 56, 899348
), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
(hbnb) 
</p>

<li>count</li>
<ul>
<li>Usage: count <class> or <class>.count()</li>
</ul>
<p>Retrieves the number of instances of a given class.</p>
<p>
$ ./console.py
(hbnb) create Place
12c73223-f3d3-4dec-9629-bd19c8fadd8a
(hbnb) create Place
aa229cbb-5b19-4c32-8562-f90a3437d301
(hbnb) create City
22a51611-17bd-4d8f-ba1b-3bf07d327208
(hbnb) 
(hbnb) count Place
2
(hbnb) city.count()
1
(hbnb)
 </p>

<li>update</li>
<ul>
<li>Usage: update <class> <id> <attribute name> "<attribute value>" or <class>.update(<id>, <attribute name>, <attribute value>) or <class>.update( <id>, <attribute dictionary>).</li>
</ul>
<p>
Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pairs. If update is called with a single key/value attribute pair, only "simple" attributes can be updated (ie. not id, created_at, and updated_at). However, any attribute can be updated by providing a dictionary.
</p>
<p>
$ ./console.py
(hbnb) create User
6f348019-0499-420f-8eec-ef0fdc863c02
(hbnb)
(hbnb) update User 6f348019-0499-420f-8eec-ef0fdc863c02 first_name "Holberton"
(hbnb) show User 6f348019-0499-420f-8eec-ef0fdc863c02
[User] (6f348019-0499-420f-8eec-ef0fdc863c02) {'created_at': datetime.datetime(
2019, 2, 17, 21, 54, 39, 234382), 'first_name': 'Holberton', 'updated_at': date
time.datetime(2019, 2, 17, 21, 54, 39, 234382), 'id': '6f348019-0499-420f-8eec-
ef0fdc863c02'}
(hbnb)
(hbnb) User.update(6f348019-0499-420f-8eec-ef0fdc863c02, address, "98 Mission S
t")
(hbnb) User.show(6f348019-0499-420f-8eec-ef0fdc863c02)
[User] (6f348019-0499-420f-8eec-ef0fdc863c02) {'created_at': datetime.datetime(
2019, 2, 17, 21, 54, 39, 234382), 'address': '98 Mission St', 'first_name': 'Ho
lberton', 'updated_at': datetime.datetime(2019, 2, 17, 21, 54, 39, 234382), 'id
': '6f348019-0499-420f-8eec-ef0fdc863c02'}
(hbnb)
(hbnb) User.update(6f348019-0499-420f-8eec-ef0fdc863c02, {'email': 'holberton@h
olberton.com', 'last_name': 'School'})
[User] (6f348019-0499-420f-8eec-ef0fdc863c02) {'email': 'holberton@holberton.co
m', 'first_name': 'Holberton', 'updated_at': datetime.datetime(2019, 2, 17, 21,
54, 39, 234382), 'address': '98 Mission St', 'last_name': 'School', 'id': '6f34
8019-0499-420f-8eec-ef0fdc863c02', 'created_at': datetime.datetime(2019, 2, 17,
21, 54, 39, 234382)}
(hbnb) 
</p>

</ul>
<h3>Testing 📏</h3>
<p>
Unittests for the AirBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:
</p>
<p>$ python3 unittest -m discover tests</p>
<p>Alternatively, you can specify a single test file to run at a time:</p>
<p>$ python3 unittest -m tests/test_console.py</p>
<h3>Authors ✒️</h3>
<ul>
<li>Oladunjoye Olaoluwa<li>
<li>Sikiru Yaya</li>
<ul>
