# HUMA_CHALLENGE - Interview coding task
<p>
A django microservice with gRPC framework.<br/>
consits of:
<ul>
    <li>service_1: Back-end serving as gateway</li>
    <li>server_1: Back-end serving as server</li>
    <li>postman collection</li>
</ul>
There are README files for both path, located in each folder.
</p>

<hr>
<h3>Covered Tasks:</h3>
<ul>
    <li>Gatway service via DRF + CRUD</li>
    <li>Server via Django-gRPC framework + Postgres</li>
    <li>gRPC Connection for both services</li>
    <li>Basic Swagger Documentations</li>
    <li>JWT athentication</li>
</ul>

<hr>
<h3>Postman:</h3>
<p>A postman collection is located in the folder:
<code>Huma_Challenge.postman_collection.json</code> <br/>
after download connect it to an environment with following configurations:
<code>

    BASE_DIR = http://127.0.0.1:8000
    AUTH_DIR = {{BASE_URL}}/account/auth/login/
</code>
An auth token will automaticaly be generated 
after running the first connection in the postman collection: <b>Login</b> <br/>
Other connections requires JWT authentication.
</p>

<hr>
<h3>To Do:</h3>
<ul>
    <li>Dockerrizing the project</li>
    <li>Advance Swagger Documentations</li>
    <li>Inbound requests loggings</li>
</ul>