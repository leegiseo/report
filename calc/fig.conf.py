WSGIScriptAlias /fig /usr/local/swp1/fig.py
WSGIPythonPath /usr/local/swp1

<Directory "/usr/local/swp1">
    AllowOverride None
    Order deny,allow
    Require all granted
</Directory>
