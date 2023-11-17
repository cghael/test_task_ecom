const fs = require('fs');

db = db.getSiblingDB('mydb');
db.createCollection('templates', {
//  validator: {
//    $jsonSchema: {
//      bsonType: 'object',
//      required: ['name'],
//      properties: {
//        name: {
//          bsonType: 'string',
//          description: 'must be a string and is required',
//        },
//        user_name: {
//          bsonType: 'string',
//          description: 'must be a string',
//        },
//        user_email: {
//          bsonType: 'string',
//          description: 'must be a string',
//          pattern: '^$|^\\S+@\\S+\\.\\S+$',
//        },
//        phone_number: {
//          bsonType: 'string',
//          description: 'must be a string or null',
//          pattern: '^$|^\\+7\\d{10}$',
//        },
//        customer_name: {
//          bsonType: 'string',
//          description: 'must be a string or null',
//        },
//        customer_phone: {
//          bsonType: 'string',
//          description: 'must be a string or null',
//          pattern: '^$|^\\+7\\d{10}$',
//        },
//        customer_email: {
//          bsonType: 'string',
//          description: 'must be a string',
//          pattern: '^$|^\\S+@\\S+\\.\\S+$',
//        },
//        order_date: {
//          bsonType: ['date', 'null'],
//          description: 'must be a date or null',
//        },
//        product_description: {
//          bsonType: 'string',
//          description: 'must be a string',
//        },
//        participant_name: {
//          bsonType: 'string',
//          description: 'must be a string',
//        },
//        feedback_date: {
//          bsonType: ['date', 'null'],
//          description: 'must be a date or null',
//        },
//        comments: {
//          bsonType: 'string',
//          description: 'must be a string or null',
//        },
//      },
//    },
//  },
});

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