# Conceptnet Microservice
A microservice to handle ontology lookups through conceptnet's API.

# Endpoints

### Get Related Concepts
`/getrelated?term=<CONCEPT>`: Provides a list of related concepts with weights corresponding to how strongly they relate.

#### Example:
```bash
curl -X GET "http://127.0.0.1:5000/getrelated?term=swimming"
```
```json
{                                                                                                                                                             
  "0": {                                                                                                                                                      
    "concept": "swimming",                                                                                                                                    
    "weight": 1                                                                                                                                               
  },                                                                                                                                                          
  "1": {                                                                                                                                                      
    "concept": "natation",
    "weight": 0.853
  },
  "2": {
    "concept": "swim",
    "weight": 0.845
  },
  "3": {
    "concept": "synchronized_swimmer",
    "weight": 0.839
  },
  "4": {
    "concept": "swims",
    "weight": 0.82
  },
  ...
}
```

### Query 'Is A' Relationships

`/IsA?subject=<SUBJECT>&prednom=<PREDICATE NOMITAVE>`: Provides a list of concepts with the relation 'Is A' (<SUBJECT> is a <PREDICATE NOMITAVE>)
Both the `?subject` and `?prednom` are optional, however **atleast one** is required.

#### Examples

##### Querying the Subject
```bash
curl -X GET "http://127.0.0.1:5000/IsA?subject=dog"
```
```json
{                                                                                                                                                             
  "0": {                                                                                                                                                      
    "pred_nom": "a loyal friend",                                                                                                                             
    "sentence": "[A dog] is a kind of [a loyal friend]",                                                                                                      
    "subject": "A dog",                                                                                                                                       
    "weight": 6.6332495807108
  },
  "1": {
    "pred_nom": "pet",
    "sentence": "[a dog] is a kind of [pet]",
    "subject": "a dog",
    "weight": 6
  },
  "2": {
    "pred_nom": "mammal",
    "sentence": "[a dog] is a kind of [mammal]",
    "subject": "a dog",
    "weight": 5.291502622129181
  },
  ...
}
```

##### Querying the Predicate Nomitave

```bash
curl -X GET "http://127.0.0.1:5000/IsA?prednom=sport"
```
```json
{                                                                                                                                                             
  "0": {                                                                                                                                                      
    "pred_nom": "a sport",                                                                                                                                    
    "sentence": "[baseball] is a kind of [a sport]",                                                                                                          
    "subject": "baseball",                                                                                                                                    
    "weight": 22.891046284519195                                                                                                                              
  },                                                                                                                                                          
  "1": {                                                                                                                                                      
    "pred_nom": "a sport",                                                                                                                                    
    "sentence": "[Tennis] is a kind of [a sport]",                                                                                                            
    "subject": "Tennis",                                                                                                                                      
    "weight": 9.591663046625438                                                                                                                               
  },                                                                                                                                                          
  "2": {
    "pred_nom": "sport",
    "sentence": "[Soccer] is a kind of [sport]",
    "subject": "Soccer",
    "weight": 9.16515138991168
  },
  ...
}
```

##### Querying both

```bash
curl -X GET "http://127.0.0.1:5000/IsA?subject=guitar&prednom=instrument"
```
```json
{
  "0": {
    "pred_nom": "instrument",
    "sentence": "[guitar] is a kind of [instrument]",
    "subject": "guitar",
    "weight": 2
  }
}
```
