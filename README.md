# Conceptnet Microservice
A microservice to handle ontology lookups through conceptnet's API.

# Endpoints
`/getrelated?term=<CONCEPT>`: Provides a list of related concepts with weights corresponding to how strongly they relate.

Example:
```bash
curl -X GET "http://127.0.0.1:5000/getrelated?term=swimming"
```
```json
{
  "aerobic_exercise": 0.483,
  "aquacade": 0.503,
  "aquatic_centre": 0.471,
  "aquatics": 0.599,
  "backstroke": 0.64,
  "bathing_suits": 0.547,
  "bathing_trunks": 0.469,
  "breaststroke": 0.611,
  ...
}
```
