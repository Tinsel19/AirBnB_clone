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
