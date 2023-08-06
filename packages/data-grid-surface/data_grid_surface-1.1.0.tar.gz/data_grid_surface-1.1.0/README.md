
# DATA-GRID-SURFACE
SDK to communicate with data-grid API service.
It uses the API service and it's end-points to determine if the given emails or passwords have been compromised.


## Installation

Install data-grid-surface SDK:

```
pip install data-grid-surface
```

## Using data-grid-access sdk

Import DataGrid class from library

```
from data_grid_surface.data_grid import DataGrid
```

You will need to provide username and password parameters to DataGrid class constructor. These are credentials for data-grid API service.

NOTE: Passwords and emails are hashed with SHA256 algorithm before being sent to the API service.

### DataGrid methods

DataGrid methods return dictionary as a result.

You can pass raw email/password or its hashed value. If you are passing hashed value you need to hash it with SHA256 algorithm and encode it in base64 format.

**Methods:**
* check_email(email, is_hashed) 
    * email **_\<String\>_**
    * is_hashed **_\<Boolean\>_** default value is True

* check_password(password, is_hashed)
    * password **_\<String\>_**
    * is_hashed **_\<Boolean\>_** default value is True

**Use example:**

```
from data_grid_surface.data_grid import DataGrid

dg = DataGrid(
    username='testuser', 
    password='testpassword'
)
res = dg.check_email('email@example.com', False)
```

```
res = dg.check_password('passwordexample', False)
```

**Response:**

```
{
    'status': 'success', 
    'data': {
        'exposed': True|False
    }
}
```