# Test Project
Web Application for Recognizing Completed Forms.

## Description:
A web application designed to identify completed forms.
The database stores a list of form templates.
```commandline
# template_example
{
    "name": "ClientForm",
    "user_name": "text",
    "user_email": "email",
    "register_date": "date",
    "phone_number": "phone"
}
```
Four types of field data are supported:
* email
* phone
* date
* text

The following type of data is sent to the input via the URL `/get_form` POST request:
`f_name1=value1&f_name2=value2`

In response, you need to return the name of the form template if it was found.

If the data does not pass validation, then returns it as a response
```commandline
{
    f_name1: FIELD_TYPE,
    f_name2: FIELD_TYPE
}
```
where FIELD_TYPE is the field type selected based on the validation rules.

If no suitable form is found, the response is returned:
```commandline
{"error": "Template not found"}
```

## Usage:

Clone the repository
```commandline
git clone git@github.com:cghael/test_task_ecom.git
cd test_task_ecom
```
Run the script
```commandline
./run_tests.sh
```
