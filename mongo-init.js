const fs = require('fs');
db = db.getSiblingDB('mydb');
db.createCollection('templates');
var templateData = JSON.parse(fs.readFileSync('/docker-entrypoint-initdb.d/template_data.json', 'utf8'));
db.templates.insertMany(templateData)
db.createUser({
  user: 'admin',
  pwd: 'VRuAd2Nvmp4ELHh5',
  roles: [
    {
      role: 'readWrite',
      db: 'mydb'
    }
  ]
});