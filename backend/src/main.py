from fastapi import FastAPI
from users.route import user_router
from courses.route import course_router

app = FastAPI()

app.include_router(user_router)
app.include_router(course_router)


    
