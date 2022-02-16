# gpt_chatbot


## Endpoints
* ### "/id" 
 has json format in the request like the below example and the server will return two parameters 
  1. Unique **id** for each company will be used in future request for chatting with the Bot 
  2. encrypted jwt **token** used by the admin for training and updating the behaviour of the model chatbot
```json
{
    "email":"admin@gmail.com",
    "name":"ADMIN",
    "password":"12345"
}
```
* ### "/train" 
 **used only by the admin** :exclamation: :exclamation: :exclamation:     the request will have json format like the below and the response will have three possible status codes 
 1. **" 200 OK "** that the provided parameters are valid and also the token is valid 
 2. **" 401 Unauthorized "** that the token provided it's time is expired and in that case you need to send request to **"/token"** to refresh the token will talk more later  
 3. **" 403 Forbidden "** that the token is unvalid
```json
{
    "id":"rtsNftTnnDYk",
    "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImlicmFoaW1lbHNhd3lAZ21haWwuY29tIiwibmFtZSI6ImlicmFoaW0iLCJwYXNzd29yZCI6ImlicmFoaW0iLCJleHAiOjE2NDUzODIyMzB9.aQHjr_BBrTBSEdtbXSRLiXkC5m2Vh4W_OS6d31iIHlQ",
    "info":"The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.",
    "questions":["how often should we be replying to fans? ", "Is there any value to creating and using Facebook groups? "],
    "answers":["Respond to fans and people who “like” your company as many times as possible. If they have a question or a request, spend the time to address these. Though this is a very time-consuming activity, it helps you increase brand awareness and drive happy reviews. ", "Facebook groups enable you to demonstrate your expertise in a specific area. If you remain an active member of the group community, your opinion will be valued and sought. As you build relationships with others immersed in the same field, you can increase your thought leadership and gain brand recognition. "]
}
```
* ### "/token"
  **used only by the admin** :exclamation: :exclamation: :exclamation:
 has json format like below example and the response will have one paramter
  1. **" token "** this is new jwt token will be used by admin instead of the expired one
 ```json
 {
  "id": "rtsNftTnnDYk",
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImlicmFoaW1lbHNhd3lAZ21haWwuY29tIiwibmFtZSI6ImlicmFoaW0iLCJwYXNzd29yZCI6ImlicmFoaW0iLCJleHAiOjE2NDQ3NzA4NjV9.-MH8tAvpHuXcaYyI3v4BMCC2uglGQTxx13HjDPV2Hvo"
}
 ```
 * ### "/req"
 used by any user has the the id of the company has json format like below example and the response will have one paramter
  1. **" response "** the response of the chatbot to the query the user sent
 ```json
 {
    "id": "rtsNftTnnDYk",
    "query":"How can Facebook ads be used in a campaign? What makes them effective?"
}
 ```
