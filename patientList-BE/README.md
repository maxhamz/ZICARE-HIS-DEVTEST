**## Available Features by Models**



\1. Users:

  \- Register

  \- Get All

  \- Get By ID

  \- Get By NIK

  \- Edit 

  \- Delete User



<hr>





**## USERS**



**### Register**



Registers new user



\* ***\*URL\****



 /users/register



\* ***\*Method:\****



 `POST`



\* ***\*URL Params\****

 None



\* ***\*Body/Form Params\****<br>

 ***\*Required\****



  \- `nama`: string,

  \- `nik`: string,

  \- `jenis_kelamin`: string,

  \- `no_hp`: string,

  \- `alamat`: string,

  \- `agama`: string,

  \- `pendidikan`: string,

  \- `golongan_darah`: string





\* ***\*Success Response:\****



 \* ***\*Code:\**** 201 <br />

  ***\*Content:\****<br>



  `{`

   `"message": "REGISTER SUCCESS",`

   `"result": {`

​    `"address": "kampung keling",`

​    `"blood_type": "O",`

​    `"cell_no": "08xxxxxxxxxx",`

​    `"created_at": "Thu, 15 Oct 2020 14:07:47 GMT",`

​    `"education": "S1",`

​    `"id": 5,`

​    `"modified_at": "Thu, 15 Oct 2020 14:07:47 GMT",`

​    `"name": "suzanna",`

​    `"nik": "3171060101650005",`

​    `"religion": "Katolik",`

​    `"saab": "L"`

  `},`

  `"status": 201`

  `}`



\* ***\*Error Responses:\****



 \* ***\*Code:\**** 400 BAD REQUEST<br />

  ***\*Content:\****<br>`{`

   `"message": "BAD REQUEST",`

   `"status": 400`

  `}`



  <br>



<hr>

<br>





***\*Fetch All\****

**----**



 Fetch list of all users



\* ***\*URL\****



 /users/getall



\* ***\*Method:\****



 `GET`



\* ***\*URL Params\****

 None



\* ***\*Body/Form Params\****<br>

 None





\* ***\*Success Response:\****



 \* ***\*Code:\**** 200 <br />

  ***\*Content:\****<br>



 `{`

  `"message": "FETCH ALL SUCCESS",`

  `"result": [`

​    `{`

​      `"address": "gang kelinci",`

​      `"blood_type": "A",`

​      `"cell_no": "08xxxxxxxxxx",`

​      `"created_at": "Thu, 15 Oct 2020 01:58:43 GMT",`

​      `"education": "S1",`

​      `"id": 1,`

​      `"modified_at": "Thu, 15 Oct 2020 01:58:43 GMT",`

​      `"name": "rhoma",`

​      `"nik": "3171060101650001",`

​      `"religion": "Islam",`

​      `"saab": "L"`

​    `},`

​    `{`

​      `"address": "gang lombok",`

​      `"blood_type": "B",`

​      `"cell_no": "08xxxxxxxxxx",`

​      `"created_at": "Thu, 15 Oct 2020 01:59:24 GMT",`

​      `"education": "S1",`

​      `"id": 2,`

​      `"modified_at": "Thu, 15 Oct 2020 01:59:24 GMT",`

​      `"name": "elvy",`

​      `"nik": "3171060101650002",`

​      `"religion": "Konghucu",`

​      `"saab": "P"`

​    `},`

​    `{`

​      `"address": "desa petitenget",`

​      `"blood_type": "AB",`

​      `"cell_no": "08xxxxxxxxxx",`

​      `"created_at": "Thu, 15 Oct 2020 02:02:23 GMT",`

​      `"education": "S1",`

​      `"id": 3,`

​      `"modified_at": "Thu, 15 Oct 2020 02:02:23 GMT",`

​      `"name": "komang",`

​      `"nik": "3171060101650003",`

​      `"religion": "Buddha",`

​      `"saab": "P"`

​    `},`

​    `{`

​      `"address": "kampung keling",`

​      `"blood_type": "O",`

​      `"cell_no": "08xxxxxxxxxx",`

​      `"created_at": "Thu, 15 Oct 2020 14:07:47 GMT",`

​      `"education": "S1",`

​      `"id": 5,`

​      `"modified_at": "Thu, 15 Oct 2020 14:07:47 GMT",`

​      `"name": "suzanna",`

​      `"nik": "3171060101650005",`

​      `"religion": "Katolik",`

​      `"saab": "L"`

​    `}`

  `],`

  `"status": 200`

 `}`



<br>



<hr>

<br>



***\*Fetch By NIK

**----**



 Fetch one user by NIK



\* ***\*URL\****



 /users/getByNIK/<:nik>



\* ***\*Method:\****



 `GET`



\* ***\*URL Params\****

 nik: string



\* ***\*Body/Form Params\****<br>

 None





\* ***\*Success Response:\****



 \* ***\*Code:\**** 200 <br />

  ***\*Content:\****<br>



 `{`

  `"message": "SUCCESS: GET BY NIK",`

  `"result": {`

​    `"address": "gang lombok",`

​    `"blood_type": "B",`

​    `"cell_no": "08xxxxxxxxxx",`

​    `"created_at": "Thu, 15 Oct 2020 01:59:24 GMT",`

​    `"education": "S1",`

​    `"id": 2,`

​    `"modified_at": "Thu, 15 Oct 2020 01:59:24 GMT",`

​    `"name": "elvy",`

​    `"nik": "3171060101650002",`

​    `"religion": "Konghucu",`

​    `"saab": "P"`

  `},`

  `"status": 200`

`}`

\* ***\*Error Responses:\****



 \* ***\*Code:\**** 404 NOT FOUND<br />

  ***\*Content:\****<br>`{`



   `"message": "NOT FOUND",`



   `"status": 404`



  `}`

<br>



<hr>

<br>

***\*Fetch By ID\****

**----**



 Fetch one user by ID



\* ***\*URL\****



 /users/getById/<:userid>



\* ***\*Method:\****



 `GET`



\* ***\*URL Params\****

 `userid`: string



\* ***\*Body/Form Params\****<br>

 None





\* ***\*Success Response:\****



 \* ***\*Code:\**** 200 <br />

  ***\*Content:\****<br>



 `{`

  `"message": "SUCCESS: GET BY ID",`

  `"result": {`

​    `"address": "gang lombok",`

​    `"blood_type": "B",`

​    `"cell_no": "08xxxxxxxxxx",`

​    `"created_at": "Thu, 15 Oct 2020 01:59:24 GMT",`

​    `"education": "S1",`

​    `"id": 2,`

​    `"modified_at": "Thu, 15 Oct 2020 01:59:24 GMT",`

​    `"name": "elvy",`

​    `"nik": "3171060101650002",`

​    `"religion": "Konghucu",`

​    `"saab": "P"`

  `},`

  `"status": 200`

`}`

\* ***\*Error Responses:\****



 \* ***\*Code:\**** 404 NOT FOUND<br />

  ***\*Content:\****<br>`{`



   `"message": "NOT FOUND",`



   `"status": 404`



  `}`



<br>



<hr>



**### Edit **



Edit User Data



\* ***\*URL\****



 /users/editUser/<:userid>



\* ***\*Method:\****



 `PUT`



\* ***\*URL Params\****

 None



\* ***\*Body/Form Params\****<br>

 ***\*Required\****



  \- `nama`: string,

  \- `nik`: string,

  \- `jenis_kelamin`: string,

  \- `no_hp`: string,

  \- `alamat`: string,

  \- `agama`: string,

  \- `pendidikan`: string,

  \- `golongan_darah`: string





\* ***\*Success Response:\****



 \* ***\*Code:\**** 200 <br />

  ***\*Content:\****<br>



  `{`

  	`"message": "Patient Info Edited",`

  	`"status": 200`

`	}`

\* ***\*Error Responses:\****



 \* ***\*Code:\**** 400 BAD REQUEST<br />

  ***\*Content:\****<br>`{`

   `"message": "BAD REQUEST",`

   `"status": 400`

  `}`



 \* ***\*Code:\**** 404 NOT FOUND<br />

  ***\*Content:\****<br>`{`

   `"message": "NOT FOUND",`

   `"status": 404`

  `}`



  <br>





<br>



<hr>



Delete User

**----**



 Drops user from database



\* ***\*URL\****



 /users/reset_password



\* ***\*Method:\****



 `PUT`



\* ***\*URL Params\****

 None



\* ***\*Header Params\****

 `access_token`: string (required)



\* ***\*Body/Form Params\****



 \- `new_password`: string

 \- `confirm_new_password`: string

 \- `OTP`: integer





\* ***\*Success Response:\****



 \* ***\*Code:\**** 200 <br />

  ***\*Content:\****<br>



 `{`



  `"message": "User dropped.",`



  `"status": 200`



 `}`



\* ***\*Error Responses:\****



 \* ***\*Code:\**** 404 NOT FOUND<br />

  ***\*Content:\****<br>`{`



   `"message": "NOT FOUND",`



   `"status": 404`



  `}`



<br>

