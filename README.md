# CloudSek_task

Submitted as the first stage of screening for internship process for Python - Backend Engineer

## About the task

Aim: Build random number generator API and add a rate limiting service on top of it.
You have an API (API A) which does some work. For the sake of the task, assume the API
simply returns a random number every time a GET request is made to it.
You need to develop another service, which allows users to login and access the above API.
Rate limiting rules: A user is allowed to make maximum 5 requests to the endpoint A in a
minute.

Expectations:
1. An API running which returns a random number . (referred to as API A )
2. An service which sits between users and the above API A which allows for the following:
- Endpoint for User signup. (just username and password)
- Endpoint for User authentication.
- Endpoint: /call_api Only callable by authenticated user. If the user is
authenticated and has not exhausted it’s rate limits, call API A and return the
answer back to the user. If a user is not authenticated or does not have api calls
left, return 403.
- Endpoint: /see_remaining_limits Only callable by authenticated user. Returns
how many requests are left for that user in that hour.

API A: You are expected to use fast-api ( https://fastapi.tiangolo.com ) for developing API A.
The rate limiting service: can be built in any framework / language (flask / django / node etc)
You can use any services you need to complete this like cache / database etc.
Package your code as a docker container (preferred) or provide a bash script which we can
execute which will install all dependencies and start the necessary services.

## Endpoints

-[ip]:8000/login

-[ip]:8000/signup

-[ip]:8000/logout

-[ip]:8000/call_api

-[ip]:8000/see_remaining_limit

## Pending/Improvement in tasks 

**not implemented** - currently working on it

- front end not fully implemented. current frontend is borrowed.

-flask-limiter has been used to provide rate limiting functionality with in-memory storage

    -[ip]:8000/see_remaining_limit is unable to accurately track requests remaining per hour since the granularity of "5 per minute" for /call_api is finer and hence was what was accessible in code
  
    -also not a viable idea to store remaining requests in a variable - wont get updated dynamically
  
    -currently implemented a share_limit - doesnt capture the requirement
  
    -further clarification of requirement would be helpful because rate limit is 5 per minute but asked remaining limit for duration of an hour
  
    -possible solution for multiple rate limits could be different storage - currently exploring
