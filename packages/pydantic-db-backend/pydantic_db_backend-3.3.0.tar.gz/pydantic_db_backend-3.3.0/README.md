# Testing

### CouchDB

http://localhost:5984/_utils/#

- user: admin
- passwd: pytest

## Initialization

### Automatic initialization from environment

```python
init_backend()
```

### Manual initialization

Example for MongoDB with alias.

If missing, the default for alias is _"default"_
```python
MongoDbBackend(alias="people")

client = Backend.client(alias="people")
```


## Pagination


### Usage with routers

```python        
@router.get("/people")
@pagination()
def people_get():
    return Backend.client().get_instances(PeopleModel)
```


### Custom usage in code

```python        
pagination_params = PaginationParameterModel
with pagination_provider(pagination_params) as p:
    Backend.client().get_instances(PeopleModel)

```



```python        
pagination_params = PaginationParameterModel
with pagination_provider(pagination_params) as p:
    Backend.client().get_instances(PeopleModel)


pagination_params = PaginationParameterModel
with pagination_parameter_provider(pagination_params):
    objs, max_results = Backend.client().pagination_aggregate(agg)
    


return pagination_result((objs, max_results))
```
