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
    <ul>
    <li>Usage: create <class><li>
    </ul>
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
<li>destroy</li>
<li>all</li>
<li>count</li>
<li>update</li>

</ul>
