from fastapi import FastAPI

import uvicorn

from get_numerator import get_is_numerator
from get_schedule import get_schedule_from_json
from transliterate import ukrainian_to_english

app = FastAPI()

@app.get("/faculties")
async def get_faculties():
    return ['фрекс']

@app.get("/specialties")
async def get_specialties(faculty: str):
    return ['кі', 'пф', 'рт']

@app.get("/courses")
async def get_courses():
    return ['1 бакалавр', '2 бакалавр', '3 бакалавр', '4 бакалавр', '1 магістр', '2 магістр']

@app.get("/groups")
async def get_groups(specialty: str, course: str):
    return ['птфе', 'нфне']

@app.get("/schedule")
async def get_schedule(date: str, faculty: str, specialty: str, course: str, group: str):
    identifier = ukrainian_to_english(f"{faculty}_{specialty}_{course}_{group}")
    schedule = get_schedule_from_json(identifier, date) or {}

    return {
        'identifier': identifier,
        'date': date,
        'is_online': schedule.get('is_online', True),
        'is_numerator': get_is_numerator(date),
        'lessons': schedule.get('lessons', [])
    }

@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == '__main__':
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=3000,
        log_level="debug",
    )
