<h1>HUMA CHALLENGE - Service</h1>
<p>A Django powered back-end which will act as a gateway using the gRPC protocol to communicate with Server.<br/>
Consists of following parts:</p>
<ul>
    <li>account: responsible for managing authenticating custom user and communications with Server</li>
    <li>protos: contains the gRPC generated files for communications</li>
    <li>service_1: core configuration of djando framework</li>
</ul>

<hr/>
<h3>How to Run:</h3>
<p>In root folder of project run command <br/>
<code>python manage.py runserver</code><br/>
The default port would be <code>:8000</code>, 
if changed remember to also change the connection port in front-end 
or postman configuration.
</p>
<h4>Server PORT Change:</h4>
<p>To update server port changes, simply edit the
<b>gRPC_SERVER_CONNECTION</b> variable
located in <code>protos/__init__.py</code>
</p>


<hr/>
<h3>Database:</h3>
<p>This server is configured to connect to local SQLite database. <br/>
Or alternatively create your own database and update the settings located at 
<code>service_1/settings.py</code> </p>

<hr/>
<h3>Swagger:</h3>
<p>Basic swagger UI is accessible via following url:
<code>/swagger/schema/</code>
</p>
