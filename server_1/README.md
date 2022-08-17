<h1>HUMA CHALLENGE - Server</h1>
<p>A Django powered back-end which utilizes the gRPC communication.<br/>
Consists of following parts:</p>
<ul>
    <li>account: responsible for managing custom user model throughout the project via gRPC services, handlers and serializers</li>
    <li>protos: contains the gRPC configurations and generated files for communications</li>
    <li>server_1: core configuration of djando framework</li>
</ul>

<hr/>
<h3>How to Run:</h3>
<p>In root folder of project run command <br/>
<code>python manage.py grpcrunserver --dev</code><br/>
The default port would be <code>:50051</code>,
if changed remember to also change the connection port in front-end or back-end services.
</p>

<hr/>
<h3>Database:</h3>
<p>This server is configured to connect to Postgres database.
Run an instance of this db in background by following configuration:
<code>

    'NAME': 'DjangoGRPC',
    'USER': 'postgres',
    'PASSWORD': 'admin',
    'HOST': 'localhost',
    'PORT': '5432',
</code>
</p>
<p>Or alternatively create your own database and update the settings located at 
<code>server_1/settings.py</code> </p>

